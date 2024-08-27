# Render the presentation slides

    source ~/envs/pres/bin/activate
    voila --template=reveal slideshow.ipynb

Edit the slides:

    jupyter notebook

Convert slides to HTML:

    deactivate
    python3.11 -m venv ~/envs/nbconvert
    source ~/envs/nbconvert/bin/activate
    pip install --upgrade pip
    pip install nbconvert
    jupyter nbconvert --to html --template reveal slideshow.ipynb
