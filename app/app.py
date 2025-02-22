from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/getcode', methods=['GET'])
def getcode():
    with app.app_context():
        return jsonify({"result": "#7308 is my code"}), 200

@app.route('/is_prime/<num>', methods=['GET'])
def is_prime(num):
    with app.app_context():
        try:
            num = int(num)
            result = True
            if num > 1:
                for i in range(2, (num//2)+1):
                    if (num % i) == 0:
                        result = False
                        break 
                else:
                    result = True
            else:
                result = False
            return jsonify({"result": result}), 200
        except Exception as e:
            print(e)
            return jsonify({"err_msg": "Invalid input"}),400
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)