# ssps-when-stats

[![Support Ukraine](https://badgen.net/badge/support/UKRAINE/?color=0057B8&labelColor=FFD700)](https://www.gov.uk/government/news/ukraine-what-you-can-do-to-help)

[![Build Status](https://github.com/PerchunPak/ssps-when-stats/actions/workflows/test.yml/badge.svg?branch=master)](https://github.com/PerchunPak/ssps-when-stats/actions?query=workflow%3Atest)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

See https://discord.com/channels/1138194598292885566/1138210016617320659/1211064344071381022 (https://discord.gg/F8pSXtJPMA).

## Installing

```bash
docker run -d \
    --name ssps-when-stats \
    -e DISCORD_WEBHOOK="https://discord.com/api/webhooks/..." \
    --restart unless-stopped \
    perchunpak/ssps-when-stats
```

## Installing for local developing

```bash
git clone https://github.com/PerchunPak/ssps-when-stats.git
cd ssps-when-stats
```

### Installing `poetry`

Next we need install `poetry` with [recommended way](https://python-poetry.org/docs/master/#installation).

If you use Linux, use command:

```bash
curl -sSL https://install.python-poetry.org | python -
```

If you use Windows, open PowerShell with admin privileges and use:

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

### Installing dependencies

```bash
poetry install --no-dev
```

## Thanks

This project was generated with [python-template](https://github.com/PerchunPak/python-template).
