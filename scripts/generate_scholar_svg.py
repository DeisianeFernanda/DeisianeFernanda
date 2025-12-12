from scholarly import scholarly
import svgwrite

SCHOLAR_ID = "RamdUesAAAAJ"

# Buscar perfil
author = scholarly.search_author_id(SCHOLAR_ID)
author = scholarly.fill(author)

citations = author["citedby"]
h_index = author["hindex"]
i10_index = author["i10index"]

# Criar SVG
dwg = svgwrite.Drawing("scholar-stats.svg", size=("300px", "120px"))

dwg.add(dwg.text(f"Citations: {citations}", insert=("10px", "30px"), fill="black"))
dwg.add(dwg.text(f"h-index: {h_index}", insert=("10px", "60px"), fill="black"))
dwg.add(dwg.text(f"i10-index: {i10_index}", insert=("10px", "90px"), fill="black"))

dwg.save()
