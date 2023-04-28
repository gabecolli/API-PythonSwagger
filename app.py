from flask import Flask, render_template
import connexion


#instantiates flask still but with extra swagger functionality
app= connexion.App(__name__, specification_dir='./') #tells connexion where to look for swagger.yml file
app.add_api('swagger.yml') #reads the swagger.yml file to configure the endpoints


@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)
