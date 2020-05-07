from crud import module as ml
from crud import app

@app.route("/post_details", methods=['POST','GET'])
@ml.cross_origin()
def postdetails():
    if ml.request.method == 'POST':
        if ml.request.is_json:
            data = ml.request.get_json()
            id = data['id']
        else:
            data = ml.request.form
            id = data.get('id')
        print(id)
        authorpost = []
        tempID = [str(temp['_id']) for temp in ml.config.article.find({},{'_id':1})]
        print(tempID)
        postID = ml.config.article.find({'_id':ml.ObjectId(id)})
        if id in tempID:
            for x in postID:
                authorpost.append(x)
            print(authorpost)
            authorpost[0]['_id'] = id
            return ml.make_response(ml.jsonify({'status':200, 'message':'author post fetched', 'data':authorpost, 'error':''}))
        else:
            return ml.jsonify({'status':404, 'message':'post not found', 'error':'_id not found'})
    return ml.render_template('account/postdetails.html', title='post details')