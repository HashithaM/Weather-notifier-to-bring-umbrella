# Rain and Umbrella Notifier

A Python automation exercise that checks the next 24 hours of OpenWeatherMap forecast data and sends an email when rain is expected. Commented code also sketches an optional Twilio SMS flow.

## Workflow

- Request eight three-hour forecast periods
- Inspect weather condition IDs for rain
- Send an umbrella reminder through Gmail SMTP
- Optionally adapt the Twilio example for SMS notifications

## Requirements

```bash
pip install requests
```

## Configuration and privacy

The current script has an empty weather API key and references undefined email credentials. Refactor it to read the API key, sender address, SMTP credential, and recipient from environment variables or a secret manager.

Personal-looking recipient addresses, phone numbers, and precise coordinates are present in the source. Replace them with approved configuration or obvious placeholders before publishing or running the project. Never commit API keys, passwords, or Twilio tokens.

## Run

After safe configuration:

```bash
python main.py
```
