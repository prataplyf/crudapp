from crud import module as ml
from crud import app

@app.route("/all_posts", methods=['GET'])
@ml.cross_origin()
def allpost():
    if ml.request.method == 'GET':
        allpost = []
        data = ml.config.article.find({},{'_id':1, 'post_title':1, 'post_desc':1, 'likes':1, 'dislikes':1})
        for x in data:
            x['_id'] = str(x['_id'])
            allpost.append(x)
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
        # tempID = [str(temp['_id']) for temp in ml.config.article.find({},{'_id':1})]
        postID = ml.config.article.find_one({'_id':ml.ObjectId(id)})
        if  id == str(postID['_id']):
            query = {'$set':{'likes':vlike, 'dislikes':vdislike}}
            ml.config.article.update({"_id":ml.ObjectId(id)},query)
            return ml.jsonify({'status':200, 'message':'like and dislike updated','error':''})
        else:
            return ml.jsonify({'status':404, 'message':'post not found', 'error':'_id not found'})
