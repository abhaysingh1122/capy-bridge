# capy-bridge

**Control Claude Code on your computer — from your phone, over Telegram.**

capy-bridge turns Claude Code into your own AI sidekick that you can talk to from anywhere. Text it and it reads, writes, runs commands, and builds on your machine — with full conversation memory and a personality **you** define.

No API key. No cloud. It runs on *your* machine, on *your* existing Claude Code login.

---

## Why

You're not always at your desk. Ideas, fixes, and "oh I should build that" moments happen on the move. capy-bridge lets you fire them at your computer the second they hit — and your machine does the work while you're out.

## Features

- 📱 **Full Claude Code over Telegram** — chat naturally, no terminal needed
- 🎭 **Bring your own persona** — define your assistant's name and voice in [`persona.md`](persona.md); it's a template you customize
- 🔐 **Locked to you** — whitelist by Telegram user ID; nobody else can talk to it
- 💾 **Persistent, resumable conversations** — pick up where you left off
- 🧠 **Runs on your Claude Code login** — no Anthropic API key required
- 🛠️ **Real power** — read/write files, run commands, git, file & image uploads
- 🧱 **Safe by default** — directory sandboxing, rate limiting, audit logging

---

## Setup (zero → running)

### Prerequisites
- **Python 3.11+** — https://www.python.org/downloads/
- **Claude Code CLI**, logged in — https://claude.ai/code (run `claude auth login` once; verify with `claude auth status`)
- **[uv](https://github.com/astral-sh/uv)** — fast Python package manager
- A **Telegram** account

### Step 1 — Create your bot
1. Open Telegram and message [@BotFather](https://t.me/botfather)
2. Send `/newbot`, give it a display name and a username ending in `bot`
3. Copy the **bot token** it gives you (looks like `1234567890:AA...`)

### Step 2 — Get your Telegram user ID
Message [@userinfobot](https://t.me/userinfobot) — it replies with your numeric **user ID**. This is your whitelist; only this ID will be allowed to talk to your bot.

### Step 3 — Install
```bash
git clone https://github.com/abhaysingh1122/capy-bridge.git
cd capy-bridge
uv venv --python 3.12
uv pip install -e .
```

### Step 4 — Configure
```bash
cp .env.example .env
```
Open `.env` and set at minimum:
```bash
TELEGRAM_BOT_TOKEN=your_token_from_botfather
TELEGRAM_BOT_USERNAME=your_bot_username      # without the @
APPROVED_DIRECTORY=/absolute/path/to/projects # the folder the bot may access
ALLOWED_USERS=123456789                       # YOUR Telegram user ID from Step 2
USE_SDK=true                                  # use your Claude Code login (no API key)
```
> ⚠️ Never commit `.env` — it's gitignored for a reason. Your token is a password.

### Step 5 — Name it & give it a personality
Edit [`persona.md`](persona.md) — its contents are prepended to the system prompt on every message, so you decide your assistant's name, voice, and rules. Want to keep your persona private (not committed)? Put it in `persona.local.md` (gitignored) and it'll be used instead. The same works for private machine context — drop it in `CONTEXT.local.md`.

### Step 6 — Run it
```bash
# Windows
./.venv/Scripts/claude-telegram-bot

# macOS / Linux
.venv/bin/claude-telegram-bot
# or simply:
make run
```

### Step 7 — Use it
Message your bot on Telegram. Say hi. It's now running on your machine.

---

## Troubleshooting

**Bot doesn't reply at all**
- Double-check `TELEGRAM_BOT_TOKEN` is correct
- Make sure your user ID is in `ALLOWED_USERS` (anyone else is silently rejected — by design)

**"Claude" errors / auth failures**
- Run `claude auth status` — you must be logged in
- With `USE_SDK=true` and an empty `ANTHROPIC_API_KEY`, it uses your existing Claude Code login

**Want it always-on?**
- Keep the machine awake and the process running (e.g. a Windows Task Scheduler entry on login, a `systemd` service on Linux, or `tmux` on macOS)

---

## Configuration

Every option is documented in [`.env.example`](.env.example) — model settings, rate limits, voice transcription, sandboxing, and more.

## Security

- **Whitelist-only access** — set `ALLOWED_USERS` to your own Telegram ID; everyone else is rejected before reaching Claude
- **Directory sandboxing** — the bot can only touch files under `APPROVED_DIRECTORY`
- Treat your bot token like a password. Keep `.env` out of git (it already is).

## License

[MIT](LICENSE).
