# BizForge - AI-Powered Brand Generation Platform

Create complete brand packages instantly with AI-powered branding, copywriting, and design system generation.

## Features

### 🚀 Brand DNA
- AI-generated brand names
- Catchy slogans and taglines
- Logo generation
- Comprehensive brand strategy guides

### ✍️ Copy Catalyst
- Social media post ideas
- Landing page headlines
- Product descriptions
- Email subject lines

### 🎨 Style Architect
- Color palette generation
- Typography recommendations
- Design principles
- Brand consistency guidelines

## Tech Stack

**Backend:**
- FastAPI (Python web framework)
- Pydantic (Data validation)
- Uvicorn (ASGI server)
- Groq API (LLM integration)
- HuggingFace API (ML models)

**Frontend:**
- HTML5 / CSS3 / JavaScript
- Modern UI with gradient design
- Responsive layout
- Real-time API integration

## Installation

### Prerequisites
- Python 3.10+
- Node.js (optional, for frontend tools)
- Git

### Backend Setup

```bash
cd backend
pip install -r requirements.txt
```

### Configure Environment
Create a `.env` file in the `backend` directory:
```
GROQ_API_KEY=your_groq_api_key
HF_API_KEY=your_huggingface_api_key
JWT_SECRET=your_secret_key
ENVIRONMENT=development
DEBUG=true
```

## Running the Application

### Start Backend Server
```bash
cd backend
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Backend will be available at: `http://127.0.0.1:8000`
API Documentation: `http://127.0.0.1:8000/docs`

### Start Frontend Server
```bash
cd Frontend
python -m http.server 8080
```

Frontend will be available at: `http://127.0.0.1:8080`

## API Endpoints

### Branding
- `POST /branding/` - Generate complete brand package
  ```json
  {
    "idea": "AI healthcare startup"
  }
  ```

### Content
- `POST /content/generate` - Generate marketing copy
  ```json
  {
    "idea": "AI healthcare startup"
  }
  ```

### Style System
- `POST /style/generate` - Generate design system
  ```json
  {
    "idea": "AI healthcare startup",
    "industry": "healthcare"
  }
  ```

### Sentiment
- `POST /sentiment/` - Analyze sentiment
  ```json
  {
    "text": "This product is amazing!"
  }
  ```

### Summarize
- `POST /summarize/` - Summarize text
  ```json
  {
    "text": "Long text to summarize..."
  }
  ```

### Health
- `GET /health` - Health check endpoint

## Project Structure

```
Bizforge1-main/
├── backend/
│   ├── app/
│   │   ├── ai/              # AI model integrations
│   │   │   ├── granite.py
│   │   │   ├── groq_llama.py
│   │   │   └── sdxl.py
│   │   ├── api/             # API endpoints
│   │   │   ├── branding.py
│   │   │   ├── content.py
│   │   │   ├── sentiment.py
│   │   │   ├── style.py
│   │   │   └── summarize.py
│   │   ├── services/        # Business logic
│   │   │   ├── branding_service.py
│   │   │   ├── copy_service.py
│   │   │   └── style_service.py
│   │   ├── models/          # Data schemas
│   │   │   └── schemas.py
│   │   ├── auth/            # Authentication
│   │   │   └── jwt.py
│   │   ├── main.py          # FastAPI app
│   │   └── config.py        # Configuration
│   ├── .env                 # Environment variables
│   └── requirements.txt     # Python dependencies
├── Frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
└── README.md
```

## Development

### Adding New Features
1. Create service in `backend/app/services/`
2. Create API endpoint in `backend/app/api/`
3. Add schema to `backend/app/models/schemas.py`
4. Register route in `backend/app/main.py`

### Code Style
- Python: PEP 8
- JavaScript: ES6+
- CSS: BEM naming convention

## Performance Optimizations

✅ Parallel API calls using async/await
✅ Efficient hash-based content generation
✅ CORS middleware for cross-origin requests
✅ Response caching ready
✅ Database integration ready (optional)

## Future Enhancements

- [ ] Real AI integration (Groq, HuggingFace)
- [ ] User authentication and accounts
- [ ] Database storage (MongoDB/PostgreSQL)
- [ ] Brand history and versions
- [ ] Export to PDF/Images
- [ ] Team collaboration features
- [ ] Advanced brand analytics
- [ ] Custom AI model training

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues, questions, or suggestions, please open an issue on GitHub.

## Author

Prashanth (237y1a6697@mlritm.ac.in)

---

**Happy Branding! 🚀**
