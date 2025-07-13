from flask import Flask, render_template_string

app = Flask(__name__)

# HTML template with embedded CSS
# HTML_TEMPLATE = """
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Azure Deployment Success</title>
#     <style>
#         * {
#             margin: 0;
#             padding: 0;
#             box-sizing: border-box;
#         }

#         body {
#             font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
#             background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
#             min-height: 100vh;
#             display: flex;
#             align-items: center;
#             justify-content: center;
#             color: white;
#         }

#         .container {
#             text-align: center;
#             padding: 3rem;
#             background: rgba(255, 255, 255, 0.1);
#             border-radius: 20px;
#             backdrop-filter: blur(10px);
#             border: 1px solid rgba(255, 255, 255, 0.2);
#             box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
#             max-width: 600px;
#             margin: 2rem;
#         }

#         h1 {
#             font-size: 2.5rem;
#             margin-bottom: 1rem;
#             background: linear-gradient(45deg, #FFD700, #FFA500);
#             -webkit-background-clip: text;
#             -webkit-text-fill-color: transparent;
#             background-clip: text;
#         }

#         .subtitle {
#             font-size: 1.2rem;
#             margin-bottom: 2rem;
#             opacity: 0.9;
#         }

#         .success-badge {
#             display: inline-block;
#             padding: 0.5rem 1.5rem;
#             background: linear-gradient(45deg, #4CAF50, #45a049);
#             border-radius: 25px;
#             font-weight: bold;
#             margin: 1rem 0;
#             box-shadow: 0 4px 15px rgba(76, 175, 80, 0.3);
#         }
        
#         .professor-thanks {
#             background: linear-gradient(45deg, #FF6B6B, #FF8E8E);
#             color: white;
#             padding: 1rem 2rem;
#             border-radius: 15px;
#             margin: 1.5rem 0;
#             font-style: italic;
#             font-size: 2.1rem;
#             box-shadow: 0 4px 15px rgba(255, 107, 107, 0.3);
#             border: 1px solid rgba(255, 255, 255, 0.3);
#         }

#         .features {
#             display: grid;
#             grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
#             gap: 1.5rem;
#             margin: 2rem 0;
#         }

#         .feature-card {
#             background: rgba(255, 255, 255, 0.1);
#             padding: 1.5rem;
#             border-radius: 15px;
#             border: 1px solid rgba(255, 255, 255, 0.2);
#             transition: transform 0.3s ease;
#         }

#         .feature-card:hover {
#             transform: translateY(-5px);
#         }

#         .footer {
#             margin-top: 2rem;
#             padding-top: 2rem;
#             border-top: 1px solid rgba(255, 255, 255, 0.2);
#             opacity: 0.8;
#         }

#         .pulse {
#             animation: pulse 2s infinite;
#         }

#         @keyframes pulse {
#             0% { transform: scale(1); }
#             50% { transform: scale(1.05); }
#             100% { transform: scale(1); }
#         }

#         @media (max-width: 768px) {
#             h1 { font-size: 2rem; }
#             .container { padding: 2rem; }
#         }
#     </style>
# </head>
# <body>
#     <div class="container">
#         <h1 class="pulse">Deployment Success!</h1>
#         <div class="subtitle">Azure Automated Deployment Complete</div>
        
#         <div class="success-badge">
#             Congratulations, Myself!
#         </div>
        
#         <div class="professor-thanks">
#             Special thanks to my Professor Kingsley Ibomo for your guidance and support
#         </div>

#         <div class="features">
#             <div class="feature-card">
#                 <h3>Cloud Deployed</h3>
#                 <p>Successfully deployed to Azure with automated CI/CD pipeline</p>
#             </div>
            
#             <div class="feature-card">
#                 <h3>Auto Deploy</h3>
#                 <p>GitHub Actions automatically builds and deploys the code</p>
#             </div>
            
#             <div class="feature-card">
#                 <h3>Containerized</h3>
#                 <p>Running in Docker container for consistency across environments</p>
#             </div>
            
#             <div class="feature-card">
#                 <h3>Fast & Scalable</h3>
#                 <p>Optimized Flask application ready for production traffic</p>
#             </div>
#         </div>

#         <div class="footer">
#             <p>My networking project is now live and running!</p>
#             <p><small>Powered by Flask • Docker • Azure • GitHub Actions</small></p>
#         </div>
#     </div>
# </body>
# </html>
# """

# @app.route('/')
# def home():
#     return render_template_string(HTML_TEMPLATE)

# @app.route('/health')
# def health():
#     return {"status": "healthy", "message": "Application is running successfully"}

# @app.route('/api/info')
# def info():
#     return {
#         "application": "Azure Deployment Demo",
#         "author": "Wai Yan Phyp",
#         "status": "deployed",
#         "platform": "Azure",
#         "technology": ["Flask", "Docker", "GitHub Actions"]
#     }

if __name__ == '__main__':
    print ("Hello World ! My Name  is Wai Yan Phyo");
    app.run(host='0.0.0.0', port=80, debug=False)