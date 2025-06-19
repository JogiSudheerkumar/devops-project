Flask App Deployment using Docker & AWS EC2
This project shows how to create a basic web app using Flask and host it on a cloud server (AWS EC2) using Docker. Perfect for DevOps beginners!

What We Built
A very simple web app using Python and Flask:
----
app.py
Shows:

bash
Copy code
Hello from AWS EC2 + Docker + Flask!
Tools Used
Tool	Why We Used It
Flask	Simple Python web framework
Docker	To package the app and run it anywhere
VS Code	To write the code
AWS EC2	To host the app on the cloud
PowerShell/Terminal	For commands
Git (optional)	To push to GitHub

Folder Structure
bash
Copy code
devops-project/
│
├── app.py             # Flask app
├── requirements.txt   # Python dependencies
├── Dockerfile         # Docker setupHow It Works (Step-by-Step)

Step 1: Create Flask App
app.py:

python
Copy code
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from AWS EC2 + Docker + Flask!"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
requirements.txt:

ini
Copy code
Flask==2.2.5--------
Step 2: Build & Run Locally
bash
Copy code
docker build -t flask-app .
docker run -d -p 5000:5000 --name flask_container flask-app
docker ps-------
Step 3: Set up AWS EC2 (Ubuntu)
Create an EC2 instance

Download flask-key.pem

Allow port 5000 in security group-------

Step 4: Connect EC2 from Your PC
powershell
Copy code
icacls "C:\ec2-keys\flask-key.pem" /inheritance:r
icacls "C:\ec2-keys\flask-key.pem" /grant:r "your-username:R"
ssh -i "C:\ec2-keys\flask-key.pem" ubuntu@<your-ec2-ip>-----
Step 5: Install Docker & Git on EC2
bash
Copy code
sudo apt update
sudo apt install docker.io git -y
sudo systemctl start docker
sudo systemctl enable docker
docker --version
git --version------------
Step 6: Upload Project to EC2
bash
Copy code
scp -i "C:\ec2-keys\flask-key.pem" -r devops-project ubuntu@<your-ec2-ip>:/home/ubuntu/-------
Step 7: Build & Run Flask App on EC2
bash
Copy code
cd devops-project
sudo docker build -t flask-app .
sudo docker run -d -p 5000:5000 --name flask_container flask-app
sudo docker ps----------------
Step 8: See App in Browser
Go to:

bash
Copy code
http://<your-ec2-ip>:5000-------------
Step 9: To Update the App
bash
Copy code
sudo docker rm -f flask_container
sudo docker build -t flask-app .
sudo docker run -d -p 5000:5000 --name flask_container flask-app# myapp
