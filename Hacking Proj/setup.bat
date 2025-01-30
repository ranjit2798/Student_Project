@echo off
setlocal enabledelayedexpansion

echo Setting up University ERP Flask Application...

:: Create project directory
mkdir UniversityERP
cd UniversityERP

:: Create virtual environment
echo Creating virtual environment...
python -m venv venv
call venv\Scripts\activate

:: Create requirements.txt
echo Creating requirements.txt...
(
echo Flask==2.2.3
echo Flask-SQLAlchemy==3.0.3
) > requirements.txt

:: Install required packages
echo Installing required packages...
pip install -r requirements.txt

:: Create templates directory
echo Creating template directories...
mkdir templates
mkdir templates\students
mkdir templates\courses
mkdir templates\enrollments

echo Setup complete!
echo.
echo Next steps:
echo 1. Create the following Python files manually:
echo    - app.py
echo    - templates\base.html
echo    - templates\index.html
echo    - templates\students\list.html
echo    - templates\students\add.html
echo    - templates\students\edit.html
echo    - templates\courses\list.html
echo    - templates\courses\add.html
echo    - templates\courses\edit.html
echo    - templates\enrollments\list.html
echo    - templates\enrollments\add.html
echo.
echo 2. After creating the files, activate the virtual environment: venv\Scripts\activate
echo 3. Run the Flask application: python app.py
echo 4. Open a web browser and go to: http://localhost:5000

endlocal