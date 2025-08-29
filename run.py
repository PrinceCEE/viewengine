import argparse
from logger import get_logger
from agent import agent
from database import Database
from ingestion import load_files
import prompts


def main(keyword_path: str, article_path: str) -> None:
    logger = get_logger(__name__)
    logger.info("Script started processing...")

    db = Database()

    logger.info("Loading necessary data for ingestion")
    keywords = load_files(keyword_path)
    article = load_files(article_path)
    brand_rules = load_files("data/brand_rules.txt")
    logger.info("Data to be ingested successfully loaded")

    logger.info("Searching for links and images")
    links = db.get_keyword_links(keywords.splitlines())
    images = db.get_keyword_images(keywords.splitlines())
    logger.info(
        "Links and images found",
        extra={
            "links": links,
            "images": images
        }
    )

    logger.info("Generate prompt")
    prompt = prompts.build(
        article,
        brand_rules,
        keywords.splitlines(),
        images,
        links
    )
    logger.info(f"Generated prompt: {prompt}")

    logger.info("Sending prompt to the agent")
    res = agent.chat(prompt)
    if not res:
        logger.error("No response from the agent")

    output_path = article_path.replace(".md", "_enriched.md")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(res.strip())

    logger.info(f"Enriched markdown successfully saved into {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run the script\nRequires the following: --article_path, --keywords_path"
    )

    parser.add_argument("--keyword_path", required=True,
                        help="Path to the keyword markdown file")
    parser.add_argument("--article_path", required=True,
                        help="Path to the article markdown path")
    args = parser.parse_args()

    main(args.keyword_path, args.article_path)
