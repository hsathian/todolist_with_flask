from flask import Flask, render_template, request, jsonify

app = Flask(__name__,static_folder='static', static_url_path='/static')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/add_task", methods=['POST'])
def add_task():
    data = request.get_json()
    task_name = data.get('taskName')
    return jsonify({'status': 'success'})

@app.route('/edit_task', methods=['POST'])
def edit_task():
    data = request.get_json()
    task_id = data.get('taskId')
    task_name = data.get('taskName')
    return jsonify({'status': 'success'})

@app.route('/delete_task', methods=['POST'])
def delete_task():
    data = request.get_json()
    task_id = data.get('taskId')
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
