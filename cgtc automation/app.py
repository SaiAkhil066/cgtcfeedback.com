from flask import Flask, render_template, request
import pandas as pd
import datetime
import os
import sys


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('feedback.html')

@app.route('/submit-feedback', methods=['POST'])
def submit():
    # These should be updated
    dates = request.form['dates']
    name = request.form['name']
    rank = request.form['rank']
    Pno = request.form['Pno']
    class_name = request.form['class_name']
    sessions = request.form['sessions']
    strength = request.form['strength']
    subject = request.form['subject'] 
    rating1 = request.form['rating1']
    rating2 = request.form['rating2']
    rating3 = request.form['rating3']
    rating4 = request.form['rating4']
    rating5 = request.form['rating5']
    rating6 = request.form['rating6']
    rating7 = request.form['rating7']
    rating8 = request.form['rating8']
    rating9 = request.form['rating9']
    rating10 = request.form['rating10']
    rating11 = request.form['rating11']
    rating12 = request.form['rating12']
    rating13 = request.form['rating13']
    rating14 = request.form['rating14']
    rating15 = request.form['rating15']
    rating16 = request.form['rating16']
    rating17 = request.form['rating17']
    rating18 = request.form['rating18']
    rating19 = request.form['rating19']
    rating20 = request.form['rating20']
    rating21 = request.form['rating21']
    rating22 = request.form['rating22']
    rating23 = request.form['rating23']
    rating24 = request.form['rating24']







    date = datetime.datetime.now().strftime("%Y-%m-%d")
    # This should be changed
    # Headings in the excel sheets are i.e, 'date', 'name', 'rank'
    data = {'Dates of Sessions': [dates], 'Name of the Instructor': [name], 'Rank / CV': [rank], 'Pno': [Pno], 'Name of the Class' : [class_name], 'Session count' : [sessions], 'Strength of the class' : [strength], 'Subject' : [subject], 'Initiation / Introduction of Lesson' :[rating1], 'Check of previous knowledge': [rating2], 'Communication skills: (a) Language': [rating3], '(b) Pronunciation': [rating4], '(c) Fluency': [rating5], '(d) Clarity': [rating6], '(e) Voice Modulation': [rating7], '(f) Rate of Delivery': [rating8], 'Development of subject: (a) Subject Knowledge':[rating9], '(b) Relevance to objectives':[rating10], '(c) Logical flow':[rating11], 'Training Aids: (a) Quality':[rating12], '(b) Appropriateness':[rating13], '(c) Effectiveness':[rating14], '(d) Utilization techniques':[rating15], 'Questioning Technique':[rating16], 'Interaction with trainess':[rating17], 'Lesson Summarization':[rating18], 'Assesment of knowledge gained':[rating19], 'Time Management':[rating20], 'Class Management':[rating21], 'Intructor Personality: (a) Turnout':[rating22], '(b) Mannerism':[rating23], '(c) Outlook':[rating24]}
    df = pd.DataFrame(data=data)
    df.to_csv(f'Feedback_Report_{date}.csv', mode='a', header=not os.path.exists(f'Feedback_Report_{date}.csv'), index=False)

    print('HI', df, file=sys.stdout)
    return 'Done.Your Feedback has been Submitted! :)'
if __name__ == '__main__':
    app.run(debug=True)
