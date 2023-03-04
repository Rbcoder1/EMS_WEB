from flask import Flask, render_template, request, session, redirect, jsonify
import requests
from flask_mysqldb import MySQL

app = Flask(__name__)

app.secret_key = "dfdmdsfdzlfld"
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'eventmanage'

mysql = MySQL(app)

# application data stores in variable
outside_events = [
    {
        "name": "Migrating On-Premises Infrastructure and Data",
        "desc":
        "Learn how to assess and evaluate an existing on-premises environment in preparation for a cloud migration—as well as how to monitor and optimize Azure-based workloads to maximize your return on investment.",
        "link": "https://mktoevents.com/Microsoft+Event/380554/157-GQE-382",
        # "img": "{{ url_for('static', filename='img/azure.jfif') }}"
    },
    {
        "name": "Digitally Transform with Modern Analytics",
        "desc":
        "Learn how to assess and evaluate an existing on-premises environment in preparation for a cloud migration—as well as how to monitor and optimize Azure-based workloads to maximize your return on investment.",
        "link": "https://mktoevents.com/Microsoft+Event/383567/157-GQE-382",
        # "img": "{{ url_for('static', filename='img/azure.jfif') }}"
    },
    {
        "name": "Linux OSS DB Migration",
        "desc":
        "Learn how to plan, manage, and optimize your migration to maximize your impact and your return on investment. Migrate open-source applications and data workloads at scale to take full advantage of Azure.",
        "link": "https://mktoevents.com/Microsoft+Event/384868/157-GQE-382",
        # "img": "{{ url_for('static', filename='img/azure.jfif') }}"
    },
    {
        "name": "Implementing Hybrid Infrastructure",
        "desc":
        "Implementing Hybrid InfrastructureLearn how to govern and manage on-premises and cloud resources with a single control plane using Azure Arc—including your Linux and Windows virtual machines (VMs), Kubernetes clusters, and databases.",
        "link": "https://mktoevents.com/Microsoft+Event/384868/157-GQE-382",
        # "img": "{{ url_for('static', filename='img/azure.jfif') }}"
    },
    {
        "name": "Modernize .NET Apps",
        "desc":
        "Learn how to auto scale apps, protect against threats, and create pipelines to build and deploy solutions faster and more reliably.",
        "link": "https://mktoevents.com/Microsoft+Event/385016/157-GQE-382",
        # "img": "{{ url_for('static', filename='img/azure.jfif') }}"
    }
]

inside_events = []
osession = []
allevents = [
    {
        "name": "Migrating On-Premises Infrastructure and Data",
        "desc":
        "Learn how to assess and evaluate an existing on-premises environment in preparation for a cloud migration—as well as how to monitor and optimize Azure-based workloads to maximize your return on investment.",
        "link": "https://mktoevents.com/Microsoft+Event/380554/157-GQE-382",
        # "img": "{{ url_for('static', filename='img/azure.jfif') }}"
    },
    {
        "name": "Digitally Transform with Modern Analytics",
        "desc":
        "Learn how to assess and evaluate an existing on-premises environment in preparation for a cloud migration—as well as how to monitor and optimize Azure-based workloads to maximize your return on investment.",
        "link": "https://mktoevents.com/Microsoft+Event/383567/157-GQE-382",
        # "img": "{{ url_for('static', filename='img/azure.jfif') }}"
    },
    {
        "name": "Linux OSS DB Migration",
        "desc":
        "Learn how to plan, manage, and optimize your migration to maximize your impact and your return on investment. Migrate open-source applications and data workloads at scale to take full advantage of Azure.",
        "link": "https://mktoevents.com/Microsoft+Event/384868/157-GQE-382",
        # "img": "{{ url_for('static', filename='img/azure.jfif') }}"
    },
    {
        "name": "Implementing Hybrid Infrastructure",
        "desc":
        "Implementing Hybrid InfrastructureLearn how to govern and manage on-premises and cloud resources with a single control plane using Azure Arc—including your Linux and Windows virtual machines (VMs), Kubernetes clusters, and databases.",
        "link": "https://mktoevents.com/Microsoft+Event/384868/157-GQE-382",
        # "img": "{{ url_for('static', filename='img/azure.jfif') }}"
    },
    {
        "name": "Modernize .NET Apps",
        "desc":
        "Learn how to auto scale apps, protect against threats, and create pipelines to build and deploy solutions faster and more reliably.",
        "link": "https://mktoevents.com/Microsoft+Event/385016/157-GQE-382",
        # "img": "{{ url_for('static', filename='img/azure.jfif') }}"
    },
    {
        "name": "HACKATHON 3.0",
        "desc":
        "This Hackathon Is Based On AI Tecnologies You have to make project based on AI technologies like NLP,Machine Learning,Computer Vision ,Etc.",
        "link": "no",
        "img": "https://source.unsplash.com/300x200/?AI robot"
    }
]

# routes for main pages
@app.route('/')
def home():
    if 'loggedin' in session:
        return render_template('home.html', username=session['username'])

    return render_template('home.html')


@app.route('/about')
def about():
    if 'loggedin' in session:
        return render_template('about.html', username=session['username'])

    return render_template('about.html')


@app.route('/contact')
def contact():
    if 'loggedin' in session:
        return render_template('contact.html', username=session['username'])

    return render_template('home.html')


# routes for events pages
@app.route('/events')
def all_events():
    if 'loggedin' in session:
        return render_template('all_events.html',
                               username=session['username'],
                               event=allevents)

    return render_template('login.html')


@app.route('/outside_event')
def outside_event():
    if 'loggedin' in session:
        return render_template('AllEvents.html', event=outside_events,username=session['username'])
    else:
        return render_template('AllEvents.html', event=outside_events)


@app.route('/inside_event')
def inside_event():
    if 'loggedin' in session:
        return render_template('AllEvents.html', username=session['username'])

    return render_template('login.html', event=inside_events)


# route for internal hackathons
@app.route('/hackathons')
def hackathon():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM hackathons')
        hk = cursor.fetchall();
        return render_template('hackathon.html',
                               username=session['username'],
                               event=hk)

    return render_template('login.html')


@app.route('/online_session')
def sessions():
    if 'loggedin' in session:
        return render_template('AllEvents.html', event=osession,username=session['username'])
    return render_template('AllEvents.html', event=osession)


@app.route('/closed_event')
def closedEvent():
    if 'loggedin' in session:
        return render_template('Allevents.html', username=session['username'])

    return render_template("login.html")


# routes for authentication register and login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        cursor = mysql.connection.cursor()
        cursor.execute(
            'SELECT * FROM users WHERE email = %s AND password = %s',
            (email, password))

        user = cursor.fetchone()

        if user:
            session['loggedin'] = True
            session['id'] = user[2]
            session['username'] = user[0]

            msg = "Successfully login "
            return render_template('home.html',
                                   username=user[0],
                                   session=session,msg=msg)
        else:
            error = "Loggin with correct username and password"
            return render_template('login.html', error=error)

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        password = request.form['password']
        # phone_number = request.form['phone']

        try:
            # inserting new user entry into users table in database
            cursor = mysql.connection.cursor()
            cursor.execute(
                "INSERT INTO users(fname,lname,email,password) VALUES(%s,%s,%s,%s)",
                (fname, lname, email, password))
            mysql.connection.commit()
            cursor.close()

            msg = "Successfully Registered "
            # returning template after user is successfully inserted 
            return render_template('login.html',msg = msg )
        except Exception as e:
            error = "Please fill form properly"
            return render_template('register.html', error=error,err=e)
 
    return render_template('register.html')


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect('/login')


@app.route('/profile')
def profile():
    if 'loggedin' in session:
        return render_template("profile.html", username=session['username'])

    return redirect("/")


# single pages for inside events and hackathon
@app.route('/single_page/<name>', methods=['GET', 'POST'])
def single_page(name):
    if 'loggedin' in session:
        try:
            # fetching event from event table in database 
            cursor = mysql.connection.cursor()
            cursor.execute('SELECT * FROM hackathons WHERE event_id= %s',(name))
            hk = cursor.fetchone()

            # rendering template after successfully event is fetch 
            return render_template('single_page.html', hack=hk,username=session['username'])
            
        except Exception as e:
            return render_template('error.html', err=e,username=session['username'])
    else:
        return redirect('/login')

@app.route("/hackathon/user_registration/<name>" , methods=['GET', 'POST'])
def user_register(name):
    if 'loggedin' in session:

        if request.method == 'POST':
            tname = request.form['tname']
            lname = request.form['lname']
            m1name = request.form['m1name']
            m2name = request.form['m2name']
            m3name = request.form['m3name']
            m4name = request.form['m4name']
            tech = request.form['tech']
            pname = request.form['pname']

            try:
                # inserting user data into database 
                cursor = mysql.connection.cursor()
                cursor.execute('INSERT INTO event_registration(id,team_name, leader_name, memeber1_name,memeber2_name,memeber3_name,memeber4_name,techonology_used,project_name) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);',(name,tname,lname,m1name,m2name,m3name,m4name,tech,pname))
                mysql.connection.commit()
                msg = "Event Registration Successfull"

                # fetching event from database with event_id
                cursor.execute('SELECT * FROM hackathons WHERE event_id= %s',(name))
                hk = cursor.fetchone()

                # cursor close 
                cursor.close()

                # rendering template after successfully register with message and event 
                return render_template('single_page.html',hack=hk,msg=msg,username=session['username'])

            except Exception as e:
                error = "Please Check Value in Fields"
                return render_template('single_page.html',hack=hk,error=error,err=e,username=session['username'])

        return "please Post the request"
    else:
        return redirect('/login')


# route for api calling 

@app.route('/jobs')
def JobSession():

    # url = "https://linkedin-jobs-search.p.rapidapi.com/"

    # payload = {
    #     "search_terms": "python programmer",
    #     "location": "Chicago, IL",
    #     "page": "1"
    # }
    # headers = {
    #     "content-type": "application/json",
    #     "X-RapidAPI-Key": "3c05e5717fmshb9cb14ced90af95p16376fjsn703abfabb9f2",
    #     "X-RapidAPI-Host": "linkedin-jobs-search.p.rapidapi.com"
    # }

    # response = requests.request("POST", url, json=payload, headers=headers)

    # # response = jsonify(response.text)
    # return render_template('jobs.html',jobs=response)
    from serpapi import GoogleSearch

    params = {
    "engine": "google_jobs",
    "q": "barista new york",
    "hl": "en",
    "api_key": "25f356d132750d01b7b1c531209efc065322bba1e8df57197a7d0fd0bb585eeb"
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    jobs_results = results["jobs_results"]
    # t = type(search)
    return render_template('jobs.html',jobs=jobs_results)

if __name__ == "__main__":
    app.run(debug=True)
