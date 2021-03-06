from flask import Flask, jsonify, abort

UNIVERSAL_TREES = {}


def listen(trees=None, taxids=None,port=None):
    print("Listening")
    print(trees)
    print(taxids)
    global UNIVERSAL_TREES

    for txs, tr in zip(taxids, trees):
        for tx in txs:
            if tx in UNIVERSAL_TREES:
                raise KeyError(f"{tx} tree already exists")
        
            UNIVERSAL_TREES[tx] = tr
    
    print(UNIVERSAL_TREES)
    app = Flask(__name__)

    app.add_url_rule('/', 'index', index)
    
    app.add_url_rule('/taxids', 'view_taxids', view_taxids)
    
    app.add_url_rule('/unigo/<taxid>', 'view_unigo', view_unigo)
    
    return app


def index():
    return "Hello world"

def view_taxids():
    global UNIVERSAL_TREES
    return str( list(UNIVERSAL_TREES.keys()) )


def view_unigo(taxid):
    print(f"/unigo/{taxid}")
    global UNIVERSAL_TREES
    if taxid in UNIVERSAL_TREES:
        d = UNIVERSAL_TREES[taxid].serialize()
        return jsonify(d)
    abort(404)

