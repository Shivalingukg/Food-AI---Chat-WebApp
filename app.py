from flask import Flask, render_template, request, jsonify, redirect, url_for


app = Flask(__name__)

restaurants = [
    {
        "id": 1,
        "name": "Tasty Bites",
        "cuisine": "Italian",
        "rating": 4.5,
        "area": "Downtown",
        "distance": 2.3,
        "image_url": "https://tse2.mm.bing.net/th/id/OIP.sSsa8LHMIdvyIdQf_61E_gHaFZ?w=222&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7",
        "menu": [
            {"name": "Margherita Pizza", "price": 12},
            {"name": "Spaghetti Carbonara", "price": 14},
            {"name": "Tiramisu", "price": 8}
        ]
    },
    
    
    
    {
        
        "id": 2,
        "name": "Sushi Paradise",
        "cuisine": "Japanese",
        "rating": 4.7,
        "area": "Uptown",
        "distance": 3.1,
        "image_url": "https://tse2.mm.bing.net/th/id/OIP.KpJXI4BKZm5BjJYS8qQrlgHaE7?w=286&h=190&c=7&r=0&o=5&dpr=1.3&pid=1.7",
        "menu": [
            {"name": "California Roll", "price": 10},
            {"name": "Salmon Nigiri", "price": 15},
            {"name": "Miso Soup", "price": 5}
        ]
    },
    {
        "id": 3,
        "name": "Burger Haven",
        "cuisine": "American",
        "rating": 4.2,
        "area": "Midtown",
        "distance": 1.8,
        "image_url": "https://tse2.mm.bing.net/th/id/OIP.nFYl5vh3CTgR_w8qXDrplQHaE2?w=291&h=190&c=7&r=0&o=5&dpr=1.3&pid=1.7",
        "menu": [
            {"name": "Classic Cheeseburger", "price": 9},
            {"name": "Bacon Deluxe Burger", "price": 11},
            {"name": "Veggie Burger", "price": 8}
        ]
    },
    {
        "id": 4,
        "name": "Spice Route",
        "cuisine": "Indian",
        "rating": 4.6,
        "area": "West End",
        "distance": 4.0,
        "image_url": "https://tse1.mm.bing.net/th/id/OIP.sdCefo2Y74KqDqs9zzk6CgHaE8?w=290&h=193&c=7&r=0&o=5&dpr=1.3&pid=1.7",
        "menu": [
            {"name": "Butter Chicken", "price": 13},
            {"name": "Vegetable Biryani", "price": 11},
            {"name": "Garlic Naan", "price": 3}
        ]
    },
    {
        "id": 5,
        "name": "Green Leaf",
        "cuisine": "Vegetarian",
        "rating": 4.3,
        "area": "East Side",
        "distance": 2.7,
        "image_url": "https://tse3.mm.bing.net/th/id/OIP.BlbFgy-X1NpAlxpCM0eFZAHaEK?w=314&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7",
        "menu": [
            {"name": "Quinoa Salad", "price": 9},
            {"name": "Vegetable Stir Fry", "price": 10},
            {"name": "Fruit Smoothie", "price": 5}
        ]
    }
]

responses = {
    'Top 5 foods of Karnataka': """Here are the top 5 foods of Karnataka:
1. Bisi Bele Bath
2. Mysore Pak
3. Ragi Mudde
4. Mysore Masala Dosa
5.  """,
    'Top 5 foods of Tamil Nadu': """Here are the top 5 foods of Tamil Nadu:
1. Idli
2. Dosa
3. Pongal
4. Chettinad Chicken
5. Madurai Halwa""",
    'Top 5 foods of Assam': """Here are the top 5 foods of Assam:
1. Assam Laksa
2. Pitha
3. Khar
4. Masor Tenga
5. Papaya Khar""",
    'Top 5 foods of Delhi': """Here are the top 5 foods of Delhi:
1. Chole Bhature
2. Butter Chicken
3. Paranthe Wali Gali
4. Daulat Ki Chaat
5. Aloo Tikki""",

    'how to make bisibelebath?': "<a href='/another-page'>Please click here to go for Bisibelebath recipe </a>",
    'hello': "Hello! How can I help you today?",
    'Hello': "Hello! How can I help you today?",
    'hi': "Yeah, what's up?",
    'Hi': "Yeah, what's up?",
    'whats your name': "Voxbot",
    'take me to google browser': "<a href='https://www.google.com/'>Google Browser</a>",
    'how to make pulao?': "<a href='/pulao-page'>Please click here to go for pulao recipe </a>",
    'bye': "Goodbye! Have a great day!",
    'how are you': "I'm just a bunch of code, but I'm functioning as expected!",
    'favorite dish you would recommend': "I would recommend you an authentic South Indian dish BisiBelebath. <a href='https://www.vegrecipesofindia.com/bisi-bele-bath-recipe/'>Click here to go for the recipe</a>",
    'i want to order something': "<a href='/restaurants'>Click here to view restaurants and order food</a>",
    'order food': "<a href='/restaurants'>Click here to view restaurants and order food</a>",
    'how to make masala dosa?': "<a href='/dosa-page'>Please click here to go for MysoreMasalaDosa recipe </a>",
    'how to make Finger Millet Halwa?':"<a href='/haalbai-page'>Please click here to go for Finger Millet recipe </a>",
    'how to make Neer Dosa?':"<a href='/neerdosa-page'>Please click here to go for Neer Dosa Recipe </a>",
    'how to make Ragi Mudde?':"<a href='/ragimude-page'>Please click here to go for Ragi mude recipe </a>",
    'how to make khara Pongal?':"<a href='/kp-page'>Please click here to go for khara pongal recipe </a>",
    'how to make Jolad roti?':"<a href='/joladroti-page'>Please click here to go for jolad roti recipe </a>",

}

def get_bot_response(user_input):
    user_input = user_input.lower().strip()
    for key, value in responses.items():
        if user_input == key.lower():
            return value
    return "I'm sorry, I don't understand that. Can you ask something else?"

def get_autocomplete_suggestions(query):
    suggestions = [
        "top 5 foods of Karnataka",
        "top 5 foods of Tamil Nadu",
        "top 5 foods of Assam",
        "top 5 foods of Delhi",
        "i want to order something",
        "how to make masala dosa?",
        "how to make Finger Millet Halwa?",
        "how to make Neer Dosa?",
        "how to make Ragi Mudde?",
        "how to make khara Pongal?",
        "how to make Jolad roti?",
        "hello",
        "whats your name",
        "hi",
        "take me to google browser",
        
        # Add more states as needed
    ]
    return [s for s in suggestions if query.lower() in s.lower()]

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/chatbot')
def chatbot():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    bot_response = get_bot_response(user_input)
    return jsonify({'response': bot_response})

@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    query = request.args.get('query', '')
    suggestions = get_autocomplete_suggestions(query)
    return jsonify(suggestions)

@app.route('/another-page')
def another_page():
    return render_template('bisibelebath.html')

@app.route('/dosa-page')
def doas_page():
    return render_template('MysoreMasalaDosa.html')

@app.route('/pulao-page')
def pulao_page():
    return render_template('pulao.html')

@app.route('/neerdosa-page')
def neerdosa_page():
    return render_template('NeerDosa.html')

@app.route('/joladroti-page')
def joladroti_page():
    return render_template('JoladRotti.html')

@app.route('/ragimude-page')
def ragimude_page():
    return render_template('RagiMude.html')

@app.route('/kp-page')
def kp_page():
    return render_template('KharaPongal.html')

@app.route('/haalbai-page')
def haalbai_page():
    return render_template('haalbai.html')

@app.route('/restaurants')
def list_restaurants():
    return render_template('restaurants.html', restaurants=restaurants)

@app.route('/restaurant/<int:restaurant_id>')
def restaurant_menu(restaurant_id):
    restaurant = next((r for r in restaurants if r['id'] == restaurant_id), None)
    if restaurant:
        return render_template('restaurant_menu.html', restaurant=restaurant)
    else:
        return "Restaurant not found", 404

if __name__ == "__main__":
    app.run(debug=True)
