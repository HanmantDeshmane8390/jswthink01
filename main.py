from flask import Flask,jsonify,render_template,request
from models.utils import CouponPredict

app = Flask(__name__)

@app.route('/')
def hello_flask():
    print("Welcome to JSW Paints Prediction of Product Coupon Code")
    return render_template("index.html")


@app.route('/predict_Coupon', methods = ["POST", "GET"])
def get_coupon_status():
    if request.method == "GET":
        print("We are using GET Method")

    

        Plant = request.args.get("Plant")
        Surface= request.args.get("Surface")
        Pack=int(request.args.get("Pack"))
        Price=int(request.args.get("Price"))
        Year=int(request.args.get("Year"))
        Awarded_points=int(request.args.get("Awarded_points"))
        
       # one hot encoded 
        Manufacturing_Plant =request.args.get("Manufacturing_Plant")
        Hub_Location=request.args.get("Hub_Location")
        Brand = request.args.get("Brand")
        
        print('Plant, Surface, Pack, Price, Year, Awarded_points,Manufacturing_Plant,Hub_Location,Brand',Plant, Surface, Pack, Price, Year, Awarded_points,Manufacturing_Plant,Hub_Location,Brand)
        class_coupon = CouponPredict(Plant, Surface, Pack, Price, Year, Awarded_points,Manufacturing_Plant,Hub_Location,Brand)

        Prediction = class_coupon.get_prediction()
        if Prediction == 1:
            return render_template("index.html", prediction='As per the provided inputs deatils product Barcode/coupon code is valid.')
        else:
            return render_template("index.html", prediction='As per the provided inputs deatils product Barcode/coupon code is invalidt.')

    else: 
       
        Plant = request.form.get("Plant")
        Surface= request.form.get("Surface")
        Pack=int(request.form.get("Pack"))
        Price=int(request.form.get("Price"))
        Year=int(request.form.get("Year"))
        Awarded_points=int(request.form.get("Awarded_points"))
        
       # one hot encoded 
        Manufacturing_Plant =request.form.get("Manufacturing_Plant")
        Hub_Location=request.form.get("Hub_Location")
        Brand = request.form.get("Brand")
        
        print('Plant, Surface, Pack, Price, Year, Awarded_points,Manufacturing_Plant,Hub_Location,Brand',Plant, Surface, Pack, Price, Year, Awarded_points,Manufacturing_Plant,Hub_Location,Brand)
        class_coupon = CouponPredict(Plant, Surface, Pack, Price, Year, Awarded_points,Manufacturing_Plant,Hub_Location,Brand)
        Prediction = class_coupon.get_prediction()

        #return render_template("index.html", prediction = Prediction )
        if Prediction == 1:
            return render_template("index.html", prediction='As per the provided input deatils product Barcode/coupon code is valid.')
        else:
            return render_template("index.html", prediction='As per the provided input deatils product Barcode/coupon code is invalid.')


  
if __name__ == "__main__":
    app.run(host='0.0.0.0' , port= 5000, debug=True)     
        

        


