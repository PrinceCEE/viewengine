# Article Enricher

This Python tool enriches markdown articles by automatically inserting relevant internal links and images, leveraging local databases and a Large Language Model (LLM).

## Overview

Provide a markdown article and a list of keywords, and Article Enricher will:

1. Search local SQLite databases for matching links and images
2. Use an LLM (via OpenRouter API) to select and insert exactly two links and two images in context
3. Output a new markdown file that follows all brand guidelines

## Prerequisites

- Python 3.13 or newer
- OpenRouter API key

## Installation

1. Install `uv` (if not already installed):
   ```bash
   curl -Ls https://astral.sh/uv/install.sh | sh
   source ~/.zshrc
   ```
2. Clone the repository:
   ```bash
   git clone https://github.com/PrinceCEE/viewengine.git viewengine_chimezie
   cd viewengine_chimezie
   ```
3. Install dependencies:
   ```bash
   uv sync
   ```
   This will set up a virtual environment and install all required packages.
4. Add your OpenRouter API key and URL to a `.env` file in the project root:
   ```
   touch .env
   OPENROUTER_API_KEY=your_api_key_here
   OPENROUTER_URL=https://openrouter.ai/api/v1/chat/completions
   ```
   _Note: uv manages the environment automatically. For manual activation, use `source .venv/bin/activate`._

## Database Setup

Ensure you have the following SQLite databases in the project root:

### `links.db`

- Table: `resources`
- Columns: `id`, `url`, `title`, `description`, `topic_tags`, `type`

### `media.db`

- Table: `images`
- Columns: `id`, `url`, `title`, `description`, `tags`

## Usage

To run the enrichment pipeline:

```bash
uv run python run.py --article_path data/article_1.md --keyword_path data/keywords_1.txt
```

### Input Files

**Article file** (`data/article_1.md`):

- Markdown format
- Will be enriched with links and images

**Keywords file** (`data/keywords_1.txt`):

- One keyword per line
- Used to match against database tags
- Example:
  ```
  electric bike commuting
  e‑bike infrastructure
  urban cycling adoption
  ```

### Output

The enriched article is saved as `{original_name}_enriched.md` in the same directory.

## Brand Guidelines

The application follows strict brand rules defined in `data/brand_rules.txt`:

- Friendly-expert tone
- Descriptive alt-text for images (≤125 characters)
- Semantic markdown structure
- Proper link anchor text

## Logging

Logs are written to `logs/app.log` and displayed in the console.

## Project Structure

```
viewengine_chimezie/
├── run.py              # Main entry point
├── agent/              # LLM agent implementation
│   ├── agent.py
│   ├── openai.py
│   └── __init__.py
├── database.py         # Database query functions
├── prompts.py          # LLM prompt construction
├── ingestion.py        # File loading utility
├── logger.py           # Logging configuration
├── config.py           # Environment config
├── data/
│   ├── article_1.md       # Sample article
│   ├── article_2.md       # Sample article
│   ├── keywords_1.txt     # Sample keywords
│   ├── keywords_2.txt     # Sample keywords
│   └── brand_rules.txt    # Style guidelines
├── links.db           # Links database
├── media.db           # Images database
└── logs/              # Log files
```
