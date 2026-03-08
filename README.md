# 📱 Vishal Info Module

<div align="center">
  <img src="https://img.shields.io/badge/version-1.0.0-blue.svg" />
  <img src="https://img.shields.io/badge/python-3.6+-green.svg" />
  <img src="https://img.shields.io/badge/license-MIT-orange.svg" />
  <img src="https://img.shields.io/badge/API-vectorxo.online-purple.svg" />
  <br>
  <strong>Made with ❤️ by <a href="https://github.com/Vishal0Hacker">@Vishal0Hacker</a></strong>
</div>

<br>

A Python module to fetch information about Indian mobile numbers using the **vectorxo.online** API. Get details like name, father's name, address, telecom circle, and more!

---

## ✨ Features

- 🔍 **Mobile Number Lookup** - Get detailed information for any Indian mobile number
- 🔒 **Secure** - No API keys hardcoded, uses environment variables
- 📦 **Easy Installation** - One-line pip install from GitHub
- 🎨 **Formatted Output** - Clean, readable display with emojis
- 🛡️ **Error Handling** - Graceful handling of invalid inputs and network issues
- 📚 **Well Documented** - Clear examples and API reference

---

## 🚀 Quick Start

### Installation

```bash
# Install directly from GitHub
pip install git+https://github.com/Vishal0Hacker/vishal-info.git
```

### Basic Usage

```python
from vishal_info import quick_lookup, lookup

# Quick lookup with formatted display
quick_lookup("7068715523")

# Get raw data for processing
data = lookup("7068715523")
for record in data:
    print(f"Name: {record['name']}, Circle: {record['circle']}")
```

---

## 🔑 API Key Setup

This module requires an API key to function. Set it up in one of these ways:

### Method 1: Environment Variable (Recommended)
```bash
# Linux/Mac
export VISHAI_API_KEY='Errnkeor01'

# Windows CMD
set VISHAI_API_KEY=Errnkeor01

# Windows PowerShell
$env:VISHAI_API_KEY="Errnkeor01"
```

### Method 2: .env File
1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
2. Edit `.env` and add your API key:
   ```
   VISHAI_API_KEY=Errnkeor01
   ```

### Method 3: Pass Directly (Not Recommended for Production)
```python
from vishal_info import MobileInfo
info = MobileInfo(api_key="Errnkeor01")
```

---

## 📚 Detailed Usage

### Using the MobileInfo Class

```python
from vishal_info import MobileInfo

# Initialize (API key from environment)
info = MobileInfo()

# Get raw data
data = info.get_info("7068715523")
if data:
    for record in data:
        print(f"👤 {record['name']} - {record['circle']}")

# Display formatted information
info.display_info("7068715523")

# Format address
address = info.format_address("S/O Shyam Lal!!40 Genda Kaboola!!Genda Kabola Jhansi!Uttar Pradesh!284302")
print(address)  # "S/O Shyam Lal, 40 Genda Kaboola, Genda Kabola Jhansi, Uttar Pradesh, 284302"
```

### Using Context Manager

```python
with MobileInfo() as info:
    data = info.get_info("7068715523")
    # Session auto-closes
```

### Error Handling

```python
from vishal_info import MobileInfo
import requests

try:
    info = MobileInfo()
    data = info.get_info("7068715523")
except ValueError as e:
    print(f"Validation Error: {e}")
except requests.exceptions.RequestException as e:
    print(f"Network Error: {e}")
except Exception as e:
    print(f"Error: {e}")
```

### Batch Lookup Example

```python
numbers = ["7068715523", "9936265021", "9876543210"]

with MobileInfo() as info:
    for number in numbers:
        print(f"\n🔍 Looking up: {number}")
        data = info.get_info(number)
        if data:
            for record in data:
                print(f"  - {record.get('name', 'N/A')}")
```

---

## 📋 API Response Format

The API returns data in this format:

```json
[
  {
    "mobile": "7068715523",
    "name": "PRAKASH NARAYAN",
    "fname": "Shyam Lal",
    "address": "S/O Shyam Lal!!40 Genda Kaboola!!Genda Kabola Jhansi!Uttar Pradesh!284302",
    "alt": "919795377623",
    "circle": "JIO UPE",
    "id": null,
    "email": null
  }
]
```

---

## 🧪 Running Tests

```bash
# Install test dependencies
pip install pytest

# Run tests
python -m pytest tests/
```

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- API provided by [vectorxo.online](https://api.vectorxo.online)
- Built with Python and ❤️

---

## 📞 Contact

- **GitHub**: [@Vishal0Hacker](https://github.com/Vishal0Hacker)
- **Project Link**: [https://github.com/Vishal0Hacker/vishal-info](https://github.com/Vishal0Hacker/vishal-info)

---

<div align="center">
  <b>⭐ If you find this module useful, please give it a star! ⭐</b>
</div>