from scholarly import scholarly
import svgwrite

SCHOLAR_ID = "RamdUesAAAAJ"

WIDTH = 360
HEIGHT = 140

def get_scholar_data():
    try:
        author = scholarly.search_author_id(SCHOLAR_ID)
        author = scholarly.fill(author)

        return {
            "citations": author.get("citedby", "N/A"),
            "hindex": author.get("hindex", "N/A"),
            "i10index": author.get("i10index", "N/A"),
        }

    except Exception as e:
        print("⚠️ Scholar bloqueou a requisição:")
        print(e)
        return {
            "citations": "N/A",
            "hindex": "N/A",
            "i10index": "N/A",
        }

data = get_scholar_data()

dwg = svgwrite.Drawing(
    "scholar-stats.svg",
    size=(f"{WIDTH}px", f"{HEIGHT}px")
)

dwg.add(dwg.rect(
    insert=(0, 0),
    size=(WIDTH, HEIGHT),
    rx=12,
    ry=12,
    fill="#f8f9fa"
))

dwg.add(dwg.text(
    "Google Scholar",
    insert=(20, 30),
    fill="#4c6ef5",
    style="font-size:20px; font-family:Arial; font-weight:bold"
))

dwg.add(dwg.text(
    f"Citations: {data['citations']}",
    insert=(20, 65),
    fill="#222",
    style="font-size:15px; font-family:Arial"
))

dwg.add(dwg.text(
    f"h-index: {data['hindex']}",
    insert=(20, 90),
    fill="#222",
    style="font-size:15px; font-family:Arial"
))

dwg.add(dwg.text(
    f"i10-index: {data['i10index']}",
    insert=(20, 115),
    fill="#222",
    style="font-size:15px; font-family:Arial"
))

dwg.save()
print("✅ SVG gerado")
