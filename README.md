## Code to paraphrase constituency tree in English

### To check the solution:
1. **git clone https://github.com/botvyns/constituency_tree_paraphrasing.git**
2. **pip install -r requirements.txt**
3. **python main.py**
4. You hould see messages like "Uvicorn running ...", "Aplication startup complete."
5. Enter into your browser this URL with tree included


http://localhost:8080/paraphrase?tree=(S (NP (NP (DT The) (JJ charming) (NNP Gothic) (NNP Quarter) ) (, ,) (CC or) (NP (NNP Barri) (NNP Gòtic) ) ) (, ,) (VP (VBZ has) (NP (NP (JJ narrow) (JJ medieval) (NNS streets) ) (VP (VBN filled) (PP (IN with) (NP (NP (JJ trendy) (NNS bars) ) (, ,) (NP (NNS clubs) ) (CC and) (NP (JJ Catalan) (NNS restaurants) ) ) ) ) ) ) )


8. Now you should see the output of 20 paraphrased trees
9. The code solution itself is available at [api.py](https://github.com/botvyns/constituency_tree_paraphrasing/blob/master/app/api.py)
