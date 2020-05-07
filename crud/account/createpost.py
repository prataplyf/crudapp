from crud import module as ml
from crud import app

@app.route("/create_post", methods=['POST','GET'])
@ml.cross_origin()
def createpost():
    if ml.request.method == 'POST':
        if ml.request.is_json:
            data = ml.request.get_json()
            post_title = data['post_title']
            post_desc = data['post_desc']
            author = data['author']
        else:
            data = ml.request.form
            post_title = data.get('post_title')
            post_desc = data.get('post_desc')
            author = data.get('author')
        print(post_desc,post_title,author)
        # insert post data into db
        ml.config.article.insert_one({'post_title':post_title, 'post_desc':post_desc, 'author':author, 'likes':0, 'dislikes':0, 'created_at':ml.currentdate})
        # return data
        return ml.jsonify({'status':200, 'message':'Post Created Successfully', 'error':''})
    return ml.render_template('account/createpost.html', title='createpost')
