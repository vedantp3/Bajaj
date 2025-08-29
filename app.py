from flask import Flask, request, jsonify

app = Flask(__name__)


FULL_NAME = "vedant vinod patil" 
DOB = "17052004" 
EMAIL = "work.vedant0505@gmail.com"
ROLL_NUMBER = "22BCE0019"

@app.route("/bfhl", methods=["POST"])  
def bfhl():
    try:
        data = request.get_json()
        if not data or "data" not in data:
            return jsonify({"is_success": False, "message": "Invalid input"}), 400

        arr = data["data"]

        odd_numbers = []
        even_numbers = []
        alphabets = []
        special_chars = []
        total_sum = 0
        concat_alpha = []

        for item in arr:
            if item.isdigit():  
                num = int(item)
                total_sum += num
                if num % 2 == 0:
                    even_numbers.append(item)
                else:
                    odd_numbers.append(item)
            elif item.isalpha():  
                alphabets.append(item.upper())
                concat_alpha.append(item)
            else:  
                special_chars.append(item)

       
        concat_alpha = "".join(concat_alpha)[::-1]
        alt_caps = "".join(
            ch.upper() if i % 2 == 0 else ch.lower()
            for i, ch in enumerate(concat_alpha)
        )

        response = {
            "is_success": True,
            "user_id": f"{FULL_NAME.replace(' ', '_')}_{DOB}",  
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_chars,
            "sum": str(total_sum),  
            "concat_string": alt_caps
        }

        return jsonify(response), 200

    except Exception as e:
        return jsonify({"is_success": False, "message": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
