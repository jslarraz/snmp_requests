### Generating distribution files ####

# Make sure you have the latest versions of setuptools and wheel installed:
python3 -m pip install --user --upgrade setuptools wheel

# Generate dist files
python3 setup.py sdist bdist_wheel


### Uploading distribution files ####

# Install Twine
python3 -m pip install --user --upgrade twine

# Use Twine to upload all of the archives under dist
python3 -m twine upload dist/*


### Clean project folder ###

# Remove distribution files
rm -r build
rm -r dist
rm -r snmp_requests.egg-info
