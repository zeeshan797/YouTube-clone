# YouTube Clone Project

A Django-based web application that replicates core YouTube functionalities. This project allows users to upload, view, and interact with video content in a familiar YouTube-like interface.

## Features

- User authentication (login/register)
- Video upload functionality
- Video playback
- Thumbnail generation
- User-friendly interface
- Responsive design

## Tech Stack

- Python 3.x
- Django
- SQLite3
- HTML/CSS
- JavaScript


## Installation

1. Clone the repository
```bash
git clone https://github.com/zeeshan797/youtube-clone.git
cd youtube-clone
```

2. Create a virtual environment
```bash
python -m venv myenv
```

3. Activate the virtual environment
```bash
# On Windows
myenv\Scripts\activate

# On macOS/Linux
source myenv/bin/activate
```

4. Install dependencies
```bash
pip install -r requirements.txt
```

5. Run migrations
```bash
cd youtube_clone_project
python manage.py migrate
```

6. Create a superuser (admin)
```bash
python manage.py createsuperuser
```

7. Run the development server
```bash
python manage.py runserver
```

8. Visit `http://127.0.0.1:8000` in your web browser

## Project Structure

```
youtube_clone_project/
├── manage.py
├── youtube_clone_project/    # Project settings
├── youtube_app/             # Main application
├── templates/              # HTML templates
├── static/                # Static files (CSS, JS)
└── media/                 # User uploaded content
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 