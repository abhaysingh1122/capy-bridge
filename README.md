# 🦫 capy-bridge

**Control Claude Code on your computer — from your phone, over Telegram.**

capy-bridge turns Claude Code into **Capybara**: a chill, always-on AI sidekick you talk to from anywhere. Text it and it reads, writes, runs commands, and builds on your machine — with full conversation memory and an actual personality.

No API key. No cloud. It runs on *your* machine, on *your* existing Claude Code login.

---

## Why

You're not always at your desk. Ideas, fixes, and "oh I should build that" moments happen on the move. capy-bridge lets you fire them at your computer the second they hit — and your machine does the work while you're out.

## Features

- 📱 **Full Claude Code over Telegram** — chat naturally, no terminal needed
- 🦫 **Custom persona** — Capybara's voice lives in [`persona.md`](persona.md), edit it to whatever you want
- 🔐 **Locked to you** — whitelist by Telegram user ID; nobody else can talk to it
- 💾 **Persistent, resumable conversations** — pick up where you left off
- 🧠 **Runs on your Claude Code login** — no Anthropic API key required
- 🛠️ **Real power** — read/write files, run commands, git, file & image uploads
- 🧱 **Safe by default** — directory sandboxing, rate limiting, audit logging

## Quick start

**Prerequisites:** Python 3.11+, the [Claude Code CLI](https://claude.ai/code) (logged in), a Telegram bot token from [@BotFather](https://t.me/botfather), and [`uv`](https://github.com/astral-sh/uv).

```bash
git clone https://github.com/abhaysingh1122/capy-bridge.git
cd capy-bridge
uv venv --python 3.12
uv pip install -e .
cp .env.example .env        # then fill in the values below
```

Minimum `.env`:

```bash
TELEGRAM_BOT_TOKEN=...        # from @BotFather
TELEGRAM_BOT_USERNAME=...     # your bot's username
APPROVED_DIRECTORY=...        # base folder the bot may access
ALLOWED_USERS=123456789       # your Telegram user ID (from @userinfobot)
USE_SDK=true                  # use your existing Claude Code login (no API key)
```

Run it:

```bash
./.venv/Scripts/claude-telegram-bot        # Windows
# or: make run
```

Then message your bot. That's it. 🦫

## The persona

Capybara's character is just a text file — [`persona.md`](persona.md) — prepended to the system prompt on every message. Rewrite it to make your assistant talk however you like.

## Configuration

Every option is documented in [`.env.example`](.env.example) — model settings, rate limits, voice transcription, sandboxing, and more.

## License

[MIT](LICENSE).
