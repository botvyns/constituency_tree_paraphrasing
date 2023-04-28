## Code to paraphrase constituency tree in English

### To run the code:
1. clone this repository 
2. intall requirements in the file [requirements.txt](https://github.com/botvyns/constituency_tree_paraphrasing/blob/master/requirements.txt)
3. run python file [main.py](https://github.com/botvyns/constituency_tree_paraphrasing/blob/master/main.py)
4. You hould see messages like "Uvicorn running ...", "Aplication startup complete."
5. Enter into your browser this URL http://localhost:8080/paraphrase?tree=(S (NP (NP (DT The) (JJ charming) (NNP Gothic) (NNP Quarter) ) (, ,) (CC or) (NP (NNP Barri) (NNP Gòtic) ) ) (, ,) (VP (VBZ has) (NP (NP (JJ narrow) (JJ medieval) (NNS streets) ) (VP (VBN filled) (PP (IN with) (NP (NP (JJ trendy) (NNS bars) ) (, ,) (NP (NNS clubs) ) (CC and) (NP (JJ Catalan) (NNS restaurants) ) ) ) ) ) ) )
6. Now you shoul see the output of 20 paraphrased trees
7. The code solution itself is available at [api.py](https://github.com/botvyns/constituency_tree_paraphrasing/blob/master/app/api.py)
