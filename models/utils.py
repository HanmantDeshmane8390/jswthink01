import pickle
import json
import pandas as pd
import numpy as np
#import config


class CouponPredict():
    def __init__(self,Plant, Surface, Pack, Price, Year, Awarded_points,Manufacturing_Plant,Hub_Location,Brand,):
        self.Plant = Plant
        self.Surface = Surface
        self.Pack = Pack
        self.Price = Price
        self.Year = Year
        self.Awarded_points = Awarded_points
        self.Manufacturing_Plant = "Manufacturing_Plant_" + Manufacturing_Plant 
        self.Hub_Location = "Hub_Location_" + Hub_Location
        self.Brand = "Brand_" + Brand

    def load_model(self):
        with open(r"C:\Users\Dell\Desktop\ProjectJsw\models\rf_model.pkl", "rb") as f:
            self.model = pickle.load(f)

        with open(r"C:\Users\Dell\Desktop\ProjectJsw\models\coupon_data.json", "r") as f:
            self.json_data = json.load(f)


    def get_prediction(self):
        self.load_model()  # calling load_file method to get
       
        Manufacturing_Plant__index = self.json_data["columns"].index(self.Manufacturing_Plant)
        Hub_Location__index = self.json_data["columns"].index(self.Hub_Location)
        Brand__index = self.json_data["columns"].index(self.Brand)

        array = np.zeros(len(self.json_data['columns']))
        
        array[0] = self.json_data["Plant"][self.Plant]
        array[1] = self.json_data["Surface"][self.Surface]
        array[2] = self.Pack
        array[3] = self.Price
        array[4] = self.Year
        array[5] = self.Awarded_points

        array[Manufacturing_Plant__index] = 1
        array[Hub_Location__index] = 1
        array[Brand__index] = 1
        

        print("Test Array -->\n",array)
        predicted_coupon = self.model.predict([array])[0]
        return predicted_coupon

        


if __name__ == "__main__":

    Plant = 'One'
    Surface = 'INTERIOR'
    Pack = 20
    Price= 9140
    Year= 2019
    Awarded_points= 87

    # one hot encoded 
    Manufacturing_Plant = "Bellary"
    Hub_Location = "Aurangabad"
    Brand = "ASI"


    class_coupon = CouponPredict(Plant, Surface, Pack, Price, Year, Awarded_points,Manufacturing_Plant,Hub_Location,Brand)
    Prediction = class_coupon.get_prediction()

    print("The Prediction for coupon is : ",Prediction)
    
