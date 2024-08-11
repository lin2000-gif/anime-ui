from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/recommendations/<username>', methods = ['GET']) 
def ReturnJSON(username):
    response = jsonify(return_result())
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

def return_result():
   return {
    "recommendationList": [
        {
        "english_title": "Attack on Titan",
        "favourites": 163844,
        "image_url": "https://cdn.myanimelist.net/images/anime/10/47347.jpg",
        "mal_id": "16498",
        "members": 3744541,
        "popularity": 1,
        "title": "Shingeki no Kyojin"
        },
        {
        "english_title": "No Game, No Life",
        "favourites": 47444,
        "image_url": "https://cdn.myanimelist.net/images/anime/1074/111944.jpg",
        "mal_id": "19815",
        "members": 2305805,
        "popularity": 16,
        "title": "No Game No Life"
        },
        {
        "english_title": "A Silent Voice",
        "favourites": 83356,
        "image_url": "https://cdn.myanimelist.net/images/anime/1122/96435.jpg",
        "mal_id": "28851",
        "members": 2193966,
        "popularity": 19,
        "title": "Koe no Katachi"
        },
        {
        "english_title": "One Piece",
        "favourites": 198986,
        "image_url": "https://cdn.myanimelist.net/images/anime/6/73245.jpg",
        "mal_id": "21",
        "members": 2168904,
        "popularity": 20,
        "title": "One Piece"
        },
        {
        "english_title": "Toradora!",
        "favourites": 55666,
        "image_url": "https://cdn.myanimelist.net/images/anime/13/22128.jpg",
        "mal_id": "4224",
        "members": 2121399,
        "popularity": 22,
        "title": "Toradora!"
        },
        {
        "english_title": "Your Lie in April",
        "favourites": 83560,
        "image_url": "https://cdn.myanimelist.net/images/anime/3/67177.jpg",
        "mal_id": "23273",
        "members": 2111376,
        "popularity": 23,
        "title": "Shigatsu wa Kimi no Uso"
        },
        {
        "english_title": "The Seven Deadly Sins",
        "favourites": 19160,
        "image_url": "https://cdn.myanimelist.net/images/anime/8/65409.jpg",
        "mal_id": "23755",
        "members": 1974171,
        "popularity": 31,
        "title": "Nanatsu no Taizai"
        },
        {
        "english_title": "The Promised Neverland",
        "favourites": 32144,
        "image_url": "https://cdn.myanimelist.net/images/anime/1830/118780.jpg",
        "mal_id": "37779",
        "members": 1866038,
        "popularity": 37,
        "title": "Yakusoku no Neverland"
        },
        {
        "english_title": "Dr. Stone",
        "favourites": 27001,
        "image_url": "https://cdn.myanimelist.net/images/anime/1613/102576.jpg",
        "mal_id": "38691",
        "members": 1630125,
        "popularity": 55,
        "title": "Dr. Stone"
        },
        {
        "english_title": "Anohana: The Flower We Saw That Day",
        "favourites": 32233,
        "image_url": "https://cdn.myanimelist.net/images/anime/5/79697.jpg",
        "mal_id": "9989",
        "members": 1554178,
        "popularity": 63,
        "title": "Ano Hi Mita Hana no Namae wo Bokutachi wa Mada Shiranai."
        }
    ]
}   

if __name__=='__main__': 
	app.run(debug=True)