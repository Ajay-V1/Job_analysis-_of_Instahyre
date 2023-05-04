# pip install flask
# pip install ntlk
from flask import Flask,request,render_template
import pandas as pd
from Ml_capstone import count_jobs,Company_Class,common_industry,Common_experience,complete
app = Flask(__name__,static_folder ="static")

@app.route("/")
def home():
    return render_template('main.html')

@app.route("/all")
def all():
    return render_template('all.html')

@app.route("/result",methods=['GET', 'POST'])
def result():
    if request.method=="POST":
        skill = request.form.get('Skills')  
        city = request.form.get('City')  
        temp=skill.split(",")
        skills=[x.lower() for x in temp] 
        # print(skills)
        if skills=="": return render_template('main.html')      
        else:
            temp=complete(skills)
            skills=temp
            # print(temp)
            dic={
            "Most Common Experience Level -: ":Common_experience(skills,city),
            "Most Common Industry -: ":common_industry(skills,city),
            "Most Common Company Class  -: ":Company_Class(skills,city),
            "Number of Jobs Available -: ":count_jobs(skills,city)
            }
        return render_template('result.html',result=dic)  
    
if __name__ =="__main__":
    app.run(debug=True,port=8000)

