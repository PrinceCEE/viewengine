from typing import List
from database import Data


def build(
    article_text: str,
    brand_rules: str,
    keywords: List[str],
    images: List[Data],
    links: List[Data]
) -> str:
    """Generate the prompt to serve to the agent"""

    image_instructions = "\n".join([
        f"- Insert {image.url} near content related to `{image.keywords}`, with a clear and descriptive alt text."
        for image in images
    ]) if images else "No images available for insertion."

    link_instructions = "\n".join([
        f"- Insert {link.url} near content related to `{link.keywords}`, formatted as a proper markdown link."
        for link in links
    ]) if links else "No links available for insertion."

    return f"""
You are an AI content editor.  

Your tasks are:  
1. Add **exactly two** internal links from the list provided:  
   - Use the most relevant keywords (or close variations) as the anchor text.  
   - Place links naturally within the article body (not both at the end).  
   - Ensure the phrasing flows smoothly and fits the surrounding context.  

2. Insert **two images** from the provided list:  
   - One near the beginning as a hero image.  
   - One later in the body as an in-context image.  

3. Follow all brand guidelines precisely.  

If you cannot insert exactly two links **and** two images, do not proceed. Instead, return an error clearly stating what is missing.  

### Example  
Given keyword: *carbon capture technology*  

Insert like:  
*"Many cities are adopting policies that encourage [electric bike commuting](https://example.com/e-bike-commuting)..."*  

---

## Brand Rules  
{brand_rules}  

## Keywords to Use  
{', '.join(keywords)}  

## Link Instructions  
{link_instructions}  

## Image Instructions  
{image_instructions}  

---

Here is the markdown content to edit:  

{article_text}  

Return **only** the updated markdown — no explanations, comments, or extra text.  
"""
