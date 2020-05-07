from crud import module as ml
from crud import app


@app.route("/delete_post", methods=["DELETE"])
@ml.cross_origin()
def deletepost():
    if ml.request.method == 'DELETE':
        if ml.request.is_json:
            data = ml.request.get_json()
            id = data['id']
        else:
            id = ml.request.form.get('id')
        #
        postID = ml.config.article.find_one({'_id':ml.ObjectId(id)})
        if postID:
            ml.config.article.remove({'_id':ml.ObjectId(id)}, {'_id':1, 'post_title':1, 'post_desc':1, 'author':1, 'likes':1, 'dislikes':1, 'created_at':1})
            return ml.jsonify({"status":200,"message":"Post Deleted Successfully", 'error':''})
        else:
            return ml.jsonify({"status":404,"message":"id not found", 'error':'error message'})
    return ml.render_template('account/deletepost.html', title='MobileApp-Delete')
