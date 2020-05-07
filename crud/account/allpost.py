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
        tempID = [str(temp['_id']) for temp in ml.config.article.find({},{'_id':1})]
        print(tempID)
        postID = ml.config.article.find_one({'_id':ml.ObjectId(id)})
        if id in tempID:
            query = {'$set':{'likes':vlike, 'dislikes':vdislike}}
            ml.config.article.update({"_id":ml.ObjectId(id)},query)
            return ml.jsonify({'status':200, 'message':'like and dislike updated','error':''})
        else:
            return ml.jsonify({'status':404, 'message':'post not found', 'error':'_id not found'})
