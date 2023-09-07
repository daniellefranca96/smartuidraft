from flask import Flask, jsonify, render_template, request, session, abort, Response
from generator import generate_code, get_last_code

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/generate', methods=['POST'])
def generate():
    memory = None
    user_req = request.get_json().get('request')
    result = generate_code(user_req)
    session['memory'] = result
    return jsonify({'data':result})
    
@app.route('/download')
def download():
    print(session)
    if "memory" not in session:
        abort(400, description="No generated data available for download")
       
    memory = session.get('memory')
    data = get_last_code(memory)

    response = Response(data)
    response.headers['Content-Type'] = 'text/html'
    response.headers['Content-Disposition'] = 'attachment; filename=generated.html'
    return response

if __name__ == '__main__':
    app.run(debug=True)