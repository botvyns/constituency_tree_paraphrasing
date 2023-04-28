from fastapi import FastAPI
from fastapi import Response
import re
import json
from itertools import permutations

app = FastAPI()

@app.get("/paraphrase")
def paraphrase(tree: str, limit=20) -> dict:
  """Takes constituency tree based on English text and returns n possible paraphrases of that tree

  Parameters
  ----------
  tree : str
         The tree to be paraphrased
  limit : int, optional
  How many paraphrased trees to create

  Returns
  -------
  json_result
  paraphrased trees in json format"""
  
  tree = str(tree)

  tree_np_replaced = re.sub(r'\(NP \((?!NP).*?\) \)', '...', tree)

  nps = re.findall(r'\(NP \((?!NP).*?\) \)', tree)

  all_permutations = list(permutations(nps))

  all_variants = []

  for permutation in all_permutations:
    variant = tree_np_replaced[:]
    for constituent in permutation:
      variant = variant.replace("...", constituent, 1)
    all_variants.append(variant)

  result = {"paraphrases": []}

  for i in all_variants[:limit]:
    result["paraphrases"].append({"tree": i})

  json_result = json.dumps(result, indent=4, default=str)
  return Response(content=json_result, media_type='application/json')