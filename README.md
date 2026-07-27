# EcoWander

## Overview

EcoWander is a web application developed to promote **ecotourism in Colombia** by connecting travelers with sustainable tourism experiences across different regions of the country. The platform provides an intuitive interface where users can discover eco tours, explore destinations, and make informed decisions before booking their next adventure.

The project was developed as part of the **Project Integrator I** course during the **2024-2 academic semester**.

## Project Motivation

Colombia is home to an extraordinary diversity of natural landscapes, ecosystems, and cultural heritage. However, many municipalities and rural regions with great ecotourism potential lack the digital visibility necessary to attract visitors.

EcoWander addresses this challenge by providing a centralized platform where travelers can easily discover eco-friendly destinations while supporting local communities and promoting responsible tourism.

The project aims to:

- Promote sustainable tourism throughout Colombia.
- Increase the visibility of lesser-known ecological destinations.
- Support local communities through tourism.
- Encourage environmental conservation.
- Provide travelers with reliable information about eco tours.

## Features

The platform allows users to:

- Explore available eco tours across Colombia.
- View detailed information about each tour.
- Filter tours by category.
- Search tours by department and municipality.
- Filter tours by price range.
- Make reservations for available tours.
- Browse destinations through a clean and responsive interface.

## Technologies Used

### Backend

- Python
- Django Framework

### Frontend

- HTML5
- CSS3
- Bootstrap
- JavaScript

### Database

- SQLite

## System Architecture

The application follows the **Model-View-Template (MVT)** architecture provided by Django.

The project is organized into several Django applications, including:

- **authentication** – User authentication and account management.
- **booking** – Reservation management.
- **tour** – Tour management and information.
- **ecoWander** – Core project configuration.
- **ecoWanderApp** – Main application logic and user interface.

## Project Objectives

The main objective of EcoWander is to create an accessible digital platform that promotes ecotourism by connecting travelers with sustainable tourism experiences while contributing to the economic and social development of local communities.

## Implemented Solution

To address the identified need, EcoWander provides an interactive web application where users can explore a wide variety of ecological tours available throughout Colombia.

The platform offers filtering options that allow users to search tours based on:

- Tour category
- Department
- Municipality
- Price range

Each tour includes detailed information to help users compare destinations and make informed decisions before booking.

By combining accessibility, usability, and sustainability, EcoWander seeks to encourage responsible tourism while increasing the visibility of regions with significant ecological and cultural value.

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/EcoWander.git
```

Navigate to the project directory:

```bash
cd EcoWander
```

Create a virtual environment:

```bash
python -m venv env
```

Activate the virtual environment.

**Windows**

```bash
env\Scripts\activate
```

**Linux/macOS**

```bash
source env/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Apply database migrations:

```bash
python manage.py migrate
```

Run the development server:

```bash
python manage.py runserver
```

The application will be available at:

```
http://127.0.0.1:8000/
```

## Project Structure

```text
EcoWander/
│
├── authentication/
├── booking/
├── ecoWander/
├── ecoWanderApp/
├── tour/
├── manage.py
├── README.md
└── requirements.txt
```

## Future Improvements

Some possible future enhancements include:

- Online payment integration.
- Interactive maps using Google Maps or OpenStreetMap.
- Tour reviews and ratings.
- Favorite destinations.
- Recommendation system based on user preferences.
- Mobile application.
- Administrator dashboard with tourism analytics.
- Integration with weather services.
- Multilingual support.

## License

This project is intended for academic purposes.

## Author

**Jeferson Alexander Del Rio Herrera**

Project Integrator I  
2024-2 Academic Semester
