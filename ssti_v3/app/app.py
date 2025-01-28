from flask import Flask, request, render_template_string, render_template

app = Flask(__name__)

BLACKLIST = ['class', 'request', 'self', 'config', '_', '.']

def is_blacklisted(user_input):
    for term in BLACKLIST:
        if term in user_input:
            return True
    return False

@app.route('/')
def index():

    user_input = request.args.get('input', '')
    
    if is_blacklisted(user_input):
        rendered_output = "Invalid input detected. Certain characters or keywords are not allowed."
    else:
        try:
            rendered_output = render_template_string(user_input)
        except Exception as e:
            rendered_output = f"Error: {str(e)}"

    return render_template('index.html', input=user_input, output=rendered_output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)
