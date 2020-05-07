from crud import module as ml
from crud import app

@app.route("/edit_post", methods=['POST','GET'])
@ml.cross_origin()
def editpost():
    if ml.request.method == 'POST':
        if ml.request.is_json:
            data = ml.request.get_json()
            id = data['id']
            post_title = data['post_title']
            post_desc = data['post_desc']
            author = data['author']
        else:
            id = ml.request.form.get('id')
            post_title = ml.request.form.get('post_title')
            post_desc = ml.request.form.get('post_desc')
            author = ml.request.form.get('author')
        postID = ml.config.article.find_one({'_id':ml.ObjectId(id)})
        print('put')
        if postID:
            query = {'$set': {'post_title':post_title, 'post_desc':post_desc,
                                  'author':author ,"created_at":ml.currentdate}}
            ml.config.article.update_one({"_id":ml.ObjectId(id)},query)
            return ml.jsonify({'status':200, 'message':'Post Updated Successfully', 'error':''})
        else:
            return ml.jsonify({'status':404, 'message':'post not found', 'error':'_id not found'})
    return ml.render_template('account/editpost.html', title='MobileAPP-Edit')
