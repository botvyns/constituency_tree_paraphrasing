import json
from itertools import permutations
import re
import stanza
stanza.download("en")
# import benepar, spacy
# benepar.download('benepar_en3')

nlp = stanza.Pipeline(lang="en", processors="tokenize, pos, constituency", verbose=False)

def parse_user_input(user_input, limit=20):
  """Use stanza to parse user's string and return paraphrase trees using function paraphrase()
  
  Parameters
  ----------
  user_input : str
        The text to be parsed
  limit : int, optional
        How many paraphrased trees to create

  Returns
  -------
  json_result
  paraphrased trees in json format"""

  doc = nlp(user_input)

  for sentence in doc.sentences:
    print(sentence.constituency)
    return paraphrase(sentence.constituency)

def paraphrase(tree: str, limit=20) -> dict:
  """Takes constituency tree based on English text and returns N possible paraphrases of that tree

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

  tree_np_replaced = re.sub(r'\(NP\s(?:\([^()]*\)|[^()])+\)', '...', tree)

  nps = re.findall(r'\(NP\s(?:\([^()]*\)|[^()])+\)', tree)

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
  return json_result

# print(parse_user_input("""The cat and the dog sat on the mat"""))