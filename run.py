from app import app
import os

port = int(os.environ.get('PORT', 8081))
app.run(debug=True,host='0.0.0.0', port=port)