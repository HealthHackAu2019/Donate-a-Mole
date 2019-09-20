# Donate-A-Mole

## Stack

* Flask web app
* Semantic UI
* Xamarin Forms mobile apps
* Electron desktop apps for analysis

## Authenication Methods

* Local
* Social
  * FB
  * Twitter
  * Github

## My Mole Social Call-to-Arms

* Share via social
  * FB sharer.php e.g. point to static URL
  * Overview; avatar mole position

## Analysis

* Geo-analysis for body location and geo location
  * Clustering and Heatmap
* Other metrics
* Tabular investigation
* Export to R

## App Permissions

* Camera/Image library
* Location
* Web
  * Divert outside links to web and social links to apps (maybe not needed)

## Milestones

### Client side

* Login via social; need online web presence first for auth
* Donate web form, file upload handling, hidden RECAPTCHA
* Display summary, share links
* Xamarin capable: file upload, camera, share links
* live counter of all moles on body map on homepage
* Use geo data to get UV rating for current location
  * methods to match?
* image upload filter (investigate at least)
* User auth desired but not required

### Analysis side

* Analysis maps
* Electron app for dedicated dashboard endpoint
* JSON generators for export and map layers

## To Do

* Frontend UI
  * Pretty everything!
  * Viewport (mobile) responsiveness
  * Consistency
* Graphics
  * Icons
* Static pages
  * Home
  * About DRC
  * About Donate-A-Mole
  * Melanoma in Australia
  * Privacy Policy
  * Contact Us
  * Links

## Setup

```bash
conda create -n dam -c conda-forge python=3 redis nodejs
conda activate dam
npm install -g sass
apt install libpq-dev build-essential
pip install -r requirements.txt

# once off db creation, data population
python manage.py recreate_db
python manage.py setup_dev
python manage.py add_fake_data

# management for dev changing schemas e.g.
python manage.py drop_all
python manage.py drop_mole

honcho start -e config.env -f Local
```

## Mole Metrics

* sex
* age
* location
* geo location
* ancresty
* personal history of melanoma (bool)
* family history of melanoma (bool)
* future research contact bool
* pathology
  * excised
  * consent for us to request pathlogy report
* fake (bool)

## Theming

```hex
  #62efff
  #00bcd4
  #008ba3
  #e1e2e1
  #f5f5f6
```

## Notes

* get emails of people agreeing to be contacted
  * confirmation email

* Sex - NA/NS
  * Dropdown for avatar select
  * Avatar 1
  * Avatar 2

## Extra Files

* dam.service: systemd service file
* dam.nginx: nginx reverse proxy configuration (TBD)
