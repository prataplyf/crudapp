from crud import module as ml
from crud import app

@app.route("/all_posts", methods=['GET'])
@ml.cross_origin()
def allpost():
    if ml.request.method == 'GET':
        allpost = []
        for x in ml.config.article.find({},{'_id':1, 'post_title':1, 'post_desc':1, 'likes':1, 'dislikes':1}):
            allpost.append({'id': str(x['_id']),
                            'post_title':x['post_title'],
                            'post_desc':x['post_desc'],
                            'likes':x['likes'],
                            'dislikes':x['dislikes']})
        return ml.jsonify({"status":200,"message":"All Posts", "data":allpost, 'error':''})



@app.route('/like_dislike', methods=['POST'])
@ml.cross_origin()
def like():
    if ml.request.method == 'POST':
        if ml.request.is_json:
            data = ml.request.get_json()
        print(data)
        vlike = data['likes']
        vdislike = data['dislikes']
        id = data['id']
        print(vlike, vdislike)
        for x in ml.config.article.find({},{'_id':1}):
            postID = str(x['_id'])  # Author's article id in which likes and dislikes will be count and store in db
            if id == postID:
                ml.config.article.update({"_id":x['_id']},{'$push':{'likes':vlike, 'dislikes':vdislike}})
        return ml.jsonify({'status':200, 'message':'','error':''})
