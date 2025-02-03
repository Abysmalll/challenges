from flask import Flask, request, render_template_string, render_template

app = Flask(__name__)

@app.route('/')
def index():
    with open('flag.txt', 'r') as f:
        flag = f.read()

    input = request.args.get('input', '')
    
    try:
        rendered_output = render_template_string(input, flag=flag)
    
    except Exception as e:
        rendered_output = f"Error: {str(e)}"

    return render_template('index.html', input=input, output=rendered_output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)
