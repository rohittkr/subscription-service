# 🚀 Subscription Service API

A lightweight and secure **Subscription Management Microservice** built with FastAPI, featuring **JWT authentication**, clean error handling, and modular design. Developed as part of a backend assignment to showcase practical API development, security integration, and system design.

---

## 📌 Key Features

- 🔐 **JWT Authentication**  
- ⚙️ **RESTful API** to manage subscriptions and plans  
- 💡 **Swagger UI** for API testing and documentation  
- 🧪 Fully tested with **Postman**  
- 🗂️ **Modular Code Structure** for scalability  
- 🔧 Supports **.env** configuration for secure settings  

---

## 📁 Project Structure

subscription_service/
├── app/
│ ├── routes/
│ │ ├── subscriptions.py
│ │ └── plans.py
│ ├── utils/
│ │ └── auth.py
│ ├── models.py
│ ├── config.py
├── main.py
├── .env
└── README.md


## 🔐 Authentication

To access protected endpoints, obtain a JWT token.

### Endpoint

POST /token

### Request Body
```json
{
  "user_id": "123"
}

Response

{
  "access_token": "<jwt_token>",
  "token_type": "bearer"
}
Use this token in the Authorization header for all protected routes:

Authorization: Bearer <jwt_token>

📦 Subscription Endpoints
Method	Endpoint	     Description	                    Auth Required
POST	/subscriptions/	Create a subscription	            ✅ Yes
GET	/subscriptions/{user_id}	Get subscription by user	✅ Yes
PUT	/subscriptions/{user_id}	Update a subscription	    ✅ Yes
DELETE	/subscriptions/{user_id}	Cancel a subscription	✅ Yes

🗂️ Plan Endpoint
Method	   Endpoint	       Description	               Auth Required
GET	       /plans/	      List all available plans	   ✅ Yes

🧪 How to Test
▶️ Start the Server

uvicorn main:app --reload
🧪 Test in Swagger UI
Visit: http://127.0.0.1:8000/docs

📬 Test via Postman
1. Get JWT Token

POST http://127.0.0.1:8000/token
Body:

json
Copy code
{
  "user_id": "123"
}
2. Use JWT Token
Copy the token from the response and set it in headers:

Authorization: Bearer <your_token_here>
3. Access Protected Routes
Test:

✅ Creating a subscription
✅ Retrieving a subscription
✅ Updating a subscription
✅ Deleting a subscription
✅ Listing available plans


✅ Completed Tasks
✅ JWT Token Authentication
✅ Subscription CRUD APIs
✅ Plan Listing API
✅ Error Handling (404, 401, validation)
✅ Console Logs and Status Codes
✅ Environment Variables via .env
✅ Postman Testing
✅ Swagger UI Enabled

🌟 About Me
Rohit Thakur
🎓 B.Tech - ECE @ IIIT Dharwad
🔧 Backend Developer | Passionate about Clean Code & Scalable Systems

📄 License
This project is for educational and demonstration purposes.
Feel free to explore, fork, and build upon it!
"# subscription-service" 
