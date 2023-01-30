from flask import Flask, render_template, request, session, redirect
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
        "desc": "Learn how to assess and evaluate an existing on-premises environment in preparation for a cloud migration—as well as how to monitor and optimize Azure-based workloads to maximize your return on investment.",
        "link": "https://mktoevents.com/Microsoft+Event/380554/157-GQE-382",
        # "img": "{{ url_for('static', filename='img/azure.jfif') }}"
    },
    {
        "name": "Digitally Transform with Modern Analytics",
        "desc": "Learn how to assess and evaluate an existing on-premises environment in preparation for a cloud migration—as well as how to monitor and optimize Azure-based workloads to maximize your return on investment.",
        "link": "https://mktoevents.com/Microsoft+Event/383567/157-GQE-382",
        # "img": "{{ url_for('static', filename='img/azure.jfif') }}"
    },
    {
        "name": "Linux OSS DB Migration",
        "desc": "Learn how to plan, manage, and optimize your migration to maximize your impact and your return on investment. Migrate open-source applications and data workloads at scale to take full advantage of Azure.",
        "link": "https://mktoevents.com/Microsoft+Event/384868/157-GQE-382",
        # "img": "{{ url_for('static', filename='img/azure.jfif') }}"
    },
    {
        "name": "Implementing Hybrid Infrastructure",
        "desc": "Implementing Hybrid InfrastructureLearn how to govern and manage on-premises and cloud resources with a single control plane using Azure Arc—including your Linux and Windows virtual machines (VMs), Kubernetes clusters, and databases.",
        "link": "https://mktoevents.com/Microsoft+Event/384868/157-GQE-382",
        # "img": "{{ url_for('static', filename='img/azure.jfif') }}"
    },
    {
        "name": "Modernize .NET Apps",
        "desc": "Learn how to auto scale apps, protect against threats, and create pipelines to build and deploy solutions faster and more reliably.",
        "link": "https://mktoevents.com/Microsoft+Event/385016/157-GQE-382",
        # "img": "{{ url_for('static', filename='img/azure.jfif') }}"
    }
]

inside_events = []
hackathons = [
    {
        "name": "HACKATHON 3.0",
        "desc": "This Hackathon Is Based On AI Tecnologies You have to make project based on AI technologies like NLP,Machine Learning,Computer Vision ,Etc.",
        "link": "no",
        "img": "https://source.unsplash.com/300x200/?AI robot"
    }
]

osession = []

allevents = [
    {
        "name": "Migrating On-Premises Infrastructure and Data",
        "desc": "Learn how to assess and evaluate an existing on-premises environment in preparation for a cloud migration—as well as how to monitor and optimize Azure-based workloads to maximize your return on investment.",
        "link": "https://mktoevents.com/Microsoft+Event/380554/157-GQE-382",
        # "img": "{{ url_for('static', filename='img/azure.jfif') }}"
    },
    {
        "name": "Digitally Transform with Modern Analytics",
        "desc": "Learn how to assess and evaluate an existing on-premises environment in preparation for a cloud migration—as well as how to monitor and optimize Azure-based workloads to maximize your return on investment.",
        "link": "https://mktoevents.com/Microsoft+Event/383567/157-GQE-382",
        # "img": "{{ url_for('static', filename='img/azure.jfif') }}"
    },
    {
        "name": "Linux OSS DB Migration",
        "desc": "Learn how to plan, manage, and optimize your migration to maximize your impact and your return on investment. Migrate open-source applications and data workloads at scale to take full advantage of Azure.",
        "link": "https://mktoevents.com/Microsoft+Event/384868/157-GQE-382",
        # "img": "{{ url_for('static', filename='img/azure.jfif') }}"
    },
    {
        "name": "Implementing Hybrid Infrastructure",
        "desc": "Implementing Hybrid InfrastructureLearn how to govern and manage on-premises and cloud resources with a single control plane using Azure Arc—including your Linux and Windows virtual machines (VMs), Kubernetes clusters, and databases.",
        "link": "https://mktoevents.com/Microsoft+Event/384868/157-GQE-382",
        # "img": "{{ url_for('static', filename='img/azure.jfif') }}"
    },
    {
        "name": "Modernize .NET Apps",
        "desc": "Learn how to auto scale apps, protect against threats, and create pipelines to build and deploy solutions faster and more reliably.",
        "link": "https://mktoevents.com/Microsoft+Event/385016/157-GQE-382",
        # "img": "{{ url_for('static', filename='img/azure.jfif') }}"
    },
    {
        "name": "HACKATHON 3.0",
        "desc": "This Hackathon Is Based On AI Tecnologies You have to make project based on AI technologies like NLP,Machine Learning,Computer Vision ,Etc.",
        "link": "no",
        "img": "https://source.unsplash.com/300x200/?AI robot"
    }
]

closeE = [
    {
        "name": "HACKATHON 1.0",
        "desc": "This Hackathon is Based on web technologies you have to make website based on html css and javascript",
        "link": "no",
        "img": "https://source.unsplash.com/300x200/?web"
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
    return render_template("all_events.html", event=allevents)


@app.route('/outside_event')
def outside_event():
    return render_template('AllEvents.html', event=outside_events)


@app.route('/inside_event')
def inside_event():
    return render_template('AllEvents.html', event=inside_events)


@app.route('/hackathons')
def hackathon():
    return render_template('hackathon.html', event=hackathons)


@app.route('/online_session')
def sessions():
    return render_template('AllEvents.html', event=osession)


@app.route('/closed_event')
def closedEvent():
    return render_template("Allevents.html", event=closeE)


# routes for authentication register and login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        cursor = mysql.connection.cursor()
        cursor.execute(
            'SELECT * FROM users WHERE email = %s AND password = %s', (email, password))

        user = cursor.fetchone()

        if user:
            session['loggedin'] = True
            session['id'] = user[2]
            session['username'] = user[0]

            return render_template('home.html', username=user[0], session=session)
        else:
            msg = "Loggin with correct username and password"

        return render_template('login.html', msg=msg)
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        password = request.form['password']
        phone_number = request.form['phone']

        try:
            cursor = mysql.connection.cursor()
            cursor.execute("INSERT INTO users(fname,lname,email,password,phone_number) VALUES(%s,%s,%s,%s,%s)",
                           (fname, lname, email, password, phone_number))

            mysql.connection.commit()
            cursor.close()
        except Exception as e:
            return render_template('register.html', error=e)

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


if __name__ == "__main__":
    app.run(debug=True)
