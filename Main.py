from flask import Flask, send_from_directory
import os

app = Flask(__name__)

TILES_DIR = 'vector_tiles'

@app.route('/tiles/<int:z>/<int:x>/<int:y>.pbf')
def get_tile(z, x, y):
    tile_path = os.path.join(TILES_DIR, f'{z}/{x}/{y}.pbf')
    return send_from_directory(os.path.dirname(tile_path), os.path.basename(tile_path), mimetype='application/x-protobuf')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
