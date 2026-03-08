"""
Core module for Vishal Info - Mobile Number Lookup
API Source: https://api.vectorxo.online/lookup
GitHub: @Vishal0Hacker
"""

import os
import requests
import json
from typing import Optional, Dict, List, Union, Any
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
env_path = Path(__file__).parent.parent / '.env'
if env_path.exists():
    load_dotenv(env_path)


class MobileInfo:
    """
    Mobile Number Information Lookup Class
    
    Fetches details like name, father's name, address, circle etc.
    for Indian mobile numbers using the vectorxo.online API.
    
    Example:
        >>> info = MobileInfo()
        >>> data = info.get_info("7068715523")
        >>> info.display_info("7068715523")
    """
    
    def __init__(self, api_key: Optional[str] = None, timeout: int = 10):
        """
        Initialize the MobileInfo client.
        
        Args:
            api_key: API key. If None, checks VISHAI_API_KEY env var or .env file.
            timeout: Request timeout in seconds.
            
        Raises:
            ValueError: If no API key is found.
        """
        self.timeout = timeout
        self.base_url = os.getenv('API_BASE_URL', 'https://api.vectorxo.online/lookup')
        
        # Get API key from multiple sources (never hardcoded!)
        self.api_key = self._get_api_key(api_key)
        
        # Setup session
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'VishalInfo-Module/1.0'
        })
        
    def _get_api_key(self, provided_key: Optional[str]) -> str:
        """Retrieve API key from arguments, environment, or .env file."""
        # Priority 1: Direct argument
        if provided_key:
            return provided_key
            
        # Priority 2: Environment variable
        env_key = os.getenv('VISHAI_API_KEY')
        if env_key:
            return env_key
            
        # No key found - raise clear error
        raise ValueError(
            "\n🔑 API Key Required!\n"
            "Please provide your API key in one of these ways:\n"
            "1. Environment variable: export VISHAI_API_KEY='Errnkeor01'\n"
            "2. .env file: Create a '.env' file with VISHAI_API_KEY=Errnkeor01\n"
            "3. Direct: MobileInfo(api_key='Errnkeor01')\n"
        )
    
    def _validate_mobile(self, mobile: str) -> str:
        """
        Validate and clean mobile number.
        
        Args:
            mobile: Input mobile number.
            
        Returns:
            Cleaned 10-digit number.
            
        Raises:
            ValueError: If number is invalid.
        """
        if not mobile or not isinstance(mobile, str):
            raise ValueError("Mobile number must be a string")
        
        # Extract digits
        digits = ''.join(filter(str.isdigit, mobile))
        
        # Handle country code (91) or leading 0
        if len(digits) == 12 and digits.startswith('91'):
            digits = digits[2:]
        elif len(digits) == 11 and digits.startswith('0'):
            digits = digits[1:]
        
        if len(digits) != 10:
            raise ValueError(f"Invalid mobile number. Expected 10 digits, got {len(digits)}")
        
        return digits
    
    def get_info(self, mobile: str) -> Optional[List[Dict[str, Any]]]:
        """
        Fetch information for a mobile number.
        
        Args:
            mobile: 10-digit Indian mobile number.
            
        Returns:
            List of records containing mobile information, or None if not found.
            
        Raises:
            ValueError: For invalid input.
            requests.RequestException: For network/API errors.
        """
        # Validate mobile
        clean_mobile = self._validate_mobile(mobile)
        
        try:
            # Prepare request
            params = {
                "key": self.api_key,
                "mobile": clean_mobile
            }
            
            # Make API call
            response = self.session.get(
                self.base_url,
                params=params,
                timeout=self.timeout
            )
            response.raise_for_status()
            
            # Parse JSON
            data = response.json()
            
            # Handle API response format
            if isinstance(data, list):
                return data if data else None
            elif isinstance(data, dict):
                # Check if response contains a single record
                if "mobile" in data:
                    return [data]
                # Check for nested data
                elif "data" in data and data["data"]:
                    nested = data["data"]
                    return nested if isinstance(nested, list) else [nested]
                # Check for error
                elif "error" in data:
                    print(f"API Error: {data['error']}")
                    return None
            
            return None
            
        except requests.exceptions.Timeout:
            raise requests.exceptions.RequestException(
                f"Request timeout after {self.timeout} seconds"
            )
        except requests.exceptions.HTTPError as e:
            if response.status_code == 401:
                raise ValueError("Invalid API key")
            elif response.status_code == 404:
                return None  # Not found is not an error
            else:
                raise
        except json.JSONDecodeError:
            raise requests.exceptions.RequestException("Invalid JSON response from API")
    
    def format_address(self, address: Optional[str]) -> str:
        """
        Format address by replacing '!' with commas.
        
        Args:
            address: Raw address string with '!' separators.
            
        Returns:
            Clean, human-readable address.
        """
        if not address:
            return "N/A"
        
        # Replace ! with commas and clean up
        formatted = address.replace('!', ', ')
        # Remove multiple spaces
        formatted = ' '.join(formatted.split())
        # Remove trailing commas
        formatted = formatted.strip(', ')
        
        return formatted if formatted else "N/A"
    
    def display_info(self, mobile: str) -> None:
        """
        Fetch and display formatted information for a mobile number.
        
        Args:
            mobile: 10-digit Indian mobile number.
        """
        print(f"\n{'='*60}")
        print(f"📱 Vishal Info Lookup: {mobile}")
        print(f"📅 Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{'='*60}")
        
        try:
            data = self.get_info(mobile)
            
            if not data:
                print("❌ No information found for this mobile number.")
                return
            
            # Display each record
            for idx, record in enumerate(data, 1):
                if len(data) > 1:
                    print(f"\n📌 Record {idx}/{len(data)}")
                    print("-" * 40)
                
                self._print_record(record)
                
                if idx < len(data):
                    print("\n" + "-" * 40)
                    
        except ValueError as e:
            print(f"❌ Validation Error: {e}")
        except requests.exceptions.RequestException as e:
            print(f"❌ Network Error: {e}")
        except Exception as e:
            print(f"❌ Unexpected Error: {e}")
        
        print(f"\n{'='*60}")
    
    def _print_record(self, record: Dict[str, Any]) -> None:
        """Print a single record in a formatted way."""
        # Basic info
        print(f"👤 Name: {record.get('name', 'N/A')}")
        print(f"👨 Father's Name: {record.get('fname', 'N/A')}")
        print(f"📞 Mobile: {record.get('mobile', 'N/A')}")
        
        # Address (formatted)
        address = self.format_address(record.get('address'))
        print(f"🏠 Address: {address}")
        
        # Circle/Operator
        circle = record.get('circle')
        if circle:
            print(f"🔄 Circle: {circle}")
        
        # Alternate mobile
        alt = record.get('alt')
        if alt:
            print(f"📱 Alternate: {alt}")
        
        # ID (if present)
        record_id = record.get('id')
        if record_id:
            print(f"🆔 ID: {record_id}")
        
        # Email (if present)
        email = record.get('email')
        if email:
            print(f"📧 Email: {email}")
    
    def __enter__(self):
        """Context manager entry."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit - close session."""
        self.session.close()


# ========== Convenience Functions ==========

def lookup(mobile: str, api_key: Optional[str] = None) -> Optional[List[Dict[str, Any]]]:
    """
    Quick lookup function that returns raw data.
    
    Args:
        mobile: Mobile number to lookup.
        api_key: Optional API key.
        
    Returns:
        Raw data from API.
        
    Example:
        >>> data = lookup("7068715523")
    """
    with MobileInfo(api_key) as info:
        return info.get_info(mobile)


def quick_lookup(mobile: str, api_key: Optional[str] = None) -> None:
    """
    Quick lookup with formatted display.
    
    Args:
        mobile: Mobile number to lookup.
        api_key: Optional API key.
        
    Example:
        >>> quick_lookup("7068715523")
    """
    with MobileInfo(api_key) as info:
        info.display_info(mobile)


# For backward compatibility
get_mobile_info = lookup