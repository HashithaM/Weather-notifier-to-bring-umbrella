# Rain and Umbrella Notifier

A Python automation exercise that checks the next 24 hours of OpenWeatherMap forecast data and sends an email when rain is expected.

## Workflow

- Request eight three-hour forecast periods
- Inspect weather condition IDs for rain
- Send an umbrella reminder through Gmail SMTP

## Requirements

```bash
pip install requests
```

## Configuration and privacy

The script reads all sensitive and personal configuration from required environment variables:

- `OPENWEATHER_API_KEY`
- `WEATHER_LATITUDE`
- `WEATHER_LONGITUDE`
- `SMTP_USER`
- `SMTP_PASSWORD`
- `NOTIFICATION_RECIPIENT`

`.env.example` contains only obvious dummy values. Keep real coordinates, addresses, and credentials in a private environment or secret manager; `.env` is ignored by Git.

## Run

After configuring the required environment variables:

```bash
python main.py
```
