# 📈 Crypto Price Monitor & SMS Alerts

A Python-based cryptocurrency price monitoring tool that tracks real-time price changes for XRP, Bitcoin (BTC), and Hedera Hashgraph (HBAR) and sends SMS notifications when significant price movements occur.

## 🚀 Features

- **Real-time Price Monitoring**: Fetches live cryptocurrency prices from CoinDesk API
- **Smart Alerts**: Only sends notifications when price changes exceed predefined thresholds
- **SMS Notifications**: Automatically sends text messages via TextBelt API
- **Multi-Currency Support**: Monitors XRP, BTC, and HBAR simultaneously
- **Customizable Thresholds**: Different alert thresholds for each cryptocurrency
- **Environment-based Configuration**: Secure API key management using environment variables

## 📊 Monitored Cryptocurrencies

| Currency | Symbol | Alert Threshold |
|----------|---------|----------------|
| XRP      | XRP-USD | ±$0.01         |
| Bitcoin  | BTC-USD | ±$1,000        |
| Hedera   | HBAR-USD| ±$0.01         |

## 🛠️ Prerequisites

- Python 3.6 or higher
- CoinDesk API key ([Get one here](https://data.coindesk.com/))
- TextBelt API key ([Get one here](https://textbelt.com/))
- A valid phone number for receiving SMS alerts

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd crypto-price-monitor
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   COINDESK_API_KEY=your_coindesk_api_key_here
   TEXTBELT_KEY=your_textbelt_api_key_here
   PHONE_NUMBER=+1234567890
   ```

## 🚀 Usage

### Basic Usage

Run the price monitor once:
```bash
python main.py
```

### Automated Monitoring

For continuous monitoring, set up a cron job or use a task scheduler:

**Linux/macOS (using cron)**:
```bash
# Edit crontab
crontab -e

# Add line to check prices every 5 minutes
*/5 * * * * /usr/bin/python3 /path/to/your/project/main.py
```

**Windows (using Task Scheduler)**:
1. Open Task Scheduler
2. Create Basic Task
3. Set trigger (e.g., every 5 minutes)
4. Set action to run `python main.py`

## 📱 Sample SMS Alert

When significant price changes are detected, you'll receive an SMS like:
```
XRP: $0.6234 Change: -0.0156
BTC: $43521.45 Change: -1205.33
```

## 🔧 Configuration

### Customizing Alert Thresholds

Edit the threshold values in `main.py`:

```python
# Current thresholds
if abs(xrp_change) > 0.01:     # XRP: $0.01
if abs(btc_change) > 1000:     # BTC: $1,000
if abs(hbar_change) > 0.01:    # HBAR: $0.01
```

### Adding New Cryptocurrencies

1. Create a new function following the existing pattern:
   ```python
   def eth():
       url = f"https://data-api.coindesk.com/spot/v1/latest/tick?apply_mapping=true&market=coinbase&instruments=ETH-USD&groups=CURRENT_HOUR,VALUE&api_key={COINDESK_API_KEY}"
       return requests.get(url)
   ```

2. Add the monitoring logic in the main section:
   ```python
   e = eth().json()
   eth_change = e['Data']['ETH-USD']['CURRENT_HOUR_CHANGE']
   
   if abs(eth_change) > 100:  # $100 threshold for ETH
       s += f"ETH: {e['Data']['ETH-USD']['PRICE']} Change: {eth_change}\n"
   ```

## 🔒 Security Notes

- Never commit your `.env` file to version control
- Keep your API keys secure and rotate them regularly
- Consider using environment variables or a secrets manager in production
- The `.env` file is already included in `.gitignore`

## 📋 Dependencies

- **requests**: HTTP library for API calls
- **python-dotenv**: Environment variable management

## 🐛 Troubleshooting

### Common Issues

1. **API Key Errors**:
   - Verify your CoinDesk API key is valid and active
   - Check that environment variables are properly set

2. **SMS Not Sending**:
   - Verify your TextBelt API key has sufficient credits
   - Ensure phone number is in correct format (+1234567890)

3. **Network Issues**:
   - Check internet connectivity
   - Verify API endpoints are accessible

### Debug Mode

Add debug prints to troubleshoot:
```python
print(f"XRP Change: {xrp_change}")
print(f"Message to send: {s}")
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This tool is for informational purposes only. Cryptocurrency investments are risky and you should do your own research before making any financial decisions. The authors are not responsible for any financial losses.

## 🙏 Acknowledgments

- [CoinDesk](https://data.coindesk.com/) for providing cryptocurrency price data
- [TextBelt](https://textbelt.com/) for SMS services
- The Python community for excellent libraries

---

**Happy Trading! 🚀📊**