from setuptools import setup, find_packages

# To make the project pip installable
setup(
    name="sld",  # Sign Language Detection
    version="1.0.0",
    description="Sign Language Gesture Recognition project: Python, OpenCV, Mediapipe, and Random Forest algorithm "
                "combine to capture, preprocess, and classify hand landmarks for accurate real-time sign language "
                "gesture recognition.",
    author="Erick Carrillo, Raudel Casas, Andres Peña",
    author_email="sansepiol26@gmail.com",
    url="https://github.com/RaudelCasas1603/Monky-Detection-",  # Update with the correct URL

    packages=find_packages(exclude=["test*"]),
    install_requires=[
        "opencv-python",
        "mediapipe",
        "scikit-learn",
        "tqdm",
        "tensorflow"
        # Add other dependencies here
    ],
    
    # Add the features to here
    entry_points={
        "console_scripts": [
            "sld = src.__main__:main",
        ]
    },

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    license = "MIT",
)
