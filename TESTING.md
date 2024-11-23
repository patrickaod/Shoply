# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| bag | bag.html | ![screenshot](documentation/html_validation/bag_val.png) | |
| checkout | checkout.html | ![screenshot](documentation/html_validation/checkout_val.png) | |
| checkout | checkout_success.html | ![screenshot](documentation/html_validation/success_val.png) | |
| home | index.html | ![screenshot](documentation/html_validation/home_val.png) | |
| products | add_products.html | ![screenshot](documentation/html_validation/add_prod_val.png) | |
| products | edit_products.html | ![screenshot](documentation/html_validation/edit_prod_val.png) | |
| products | product_detail.html | ![screenshot](documentation/html_validation/prod_det_val.png) | |
| products | products.html | ![screenshot](documentation/html_validation/prod_val.png) | |
| user profile | profile.html | ![screenshot](documentation/html_validation/user_profile.png) | |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| checkout | checkout.css | ![screenshot](documentation/css_validation/checkout_css_val.png) | |
| profiles | profile.css | ![screenshot](documentation/css_validation/profile_css_val.png) | |
| static | style.css | ![screenshot](documentation/css_validation/style_css_val.png) | |

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| checkout | stripe_elements.js | ![screenshot](documentation/js_validation/stripe_js_val.png) | |
| profiles | countryfield.js | ![screenshot](documentation/js_validation/prof_js_val.png) | |
| static | main.js | ![screenshot](documentation/js_validation/main_js_val.png) | The errors shown in this screenshot are related to the Bootstrap Tooltip JavaScript. For reference, I've included the official documentation here: [Bootstrap Tooltip Documentation](https://getbootstrap.com/docs/5.0/components/tooltips/).|

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| bag | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/patrickaod/Shoply/main/bag/admin.py) | ![screenshot](documentation/python_validation/pep8ci.herokuapp.com_https___raw.githubusercontent.com_patrickaod_Shoply_main_bag_admin.py.png) | |
| bag | contexts.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/patrickaod/Shoply/main/bag/contexts.py) | ![screenshot](documentation/python_validation/pep8ci.herokuapp.com_https___raw.githubusercontent.com_patrickaod_Shoply_main_bag_contexts.py (1).png) | |
| bag | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/patrickaod/Shoply/main/bag/models.py) | ![screenshot](documentation/python_validation/pep8ci.herokuapp.com_https___raw.githubusercontent.com_patrickaod_Shoply_main_bag_models.py.png) | |
| bag | bag_tools.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/patrickaod/Shoply/main/bag/templatetags/bag_tools.py) | ![screenshot](documentation/python_validation/pep8ci.herokuapp.com_https___raw.githubusercontent.com_patrickaod_Shoply_main_bag_templatetags_bag_tools.py.png) | |
| bag | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/patrickaod/Shoply/main/bag/urls.py) | ![screenshot](documentation/python_validation/pep8ci.herokuapp.com_https___raw.githubusercontent.com_patrickaod_Shoply_main_bag_urls.py.png) | |
| bag | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/patrickaod/Shoply/main/bag/views.py) | ![screenshot](documentation/python_validation/pep8ci.herokuapp.com_https___raw.githubusercontent.com_patrickaod_Shoply_main_bag_views.py.png) | |
| checkout | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/patrickaod/Shoply/main/checkout/admin.py) | ![screenshot](documentation/python_validation/pep8ci.herokuapp.com_https___raw.githubusercontent.com_patrickaod_Shoply_main_checkout_admin.py.png) | |
| checkout | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/patrickaod/Shoply/main/checkout/forms.py) | ![screenshot](documentation/python_validation/pep8ci.herokuapp.com_https___raw.githubusercontent.com_patrickaod_Shoply_main_checkout_forms.py.png) | |
| checkout | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/patrickaod/Shoply/main/checkout/models.py) | ![screenshot](documentation/python_validation/pep8ci.herokuapp.com_https___raw.githubusercontent.com_patrickaod_Shoply_main_checkout_models.py.png) | |
| checkout | signals.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/patrickaod/Shoply/main/checkout/signals.py) | ![screenshot](documentation/python_validation/pep8ci.herokuapp.com_https___raw.githubusercontent.com_patrickaod_Shoply_main_checkout_signals.py.png) | |
| checkout | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/patrickaod/Shoply/main/checkout/urls.py) | ![screenshot](documentation/python_validation/pep8ci.herokuapp.com_https___raw.githubusercontent.com_patrickaod_Shoply_main_checkout_urls.py.png) | |
| checkout | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/patrickaod/Shoply/main/checkout/views.py) | ![screenshot](documentation/python_validation/pep8ci.herokuapp.com_https___raw.githubusercontent.com_patrickaod_Shoply_main_checkout_views.py.png) | |
| checkout | webhook_handler.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/patrickaod/Shoply/main/checkout/webhook_handler.py) | ![screenshot](documentation/python_validation/pep8ci.herokuapp.com_https___raw.githubusercontent.com_patrickaod_Shoply_main_checkout_webhook_handler.py.png) | |
| checkout | webhooks.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/patrickaod/Shoply/main/checkout/webhooks.py) | ![screenshot](documentation/python_validation/pep8ci.herokuapp.com_https___raw.githubusercontent.com_patrickaod_Shoply_main_checkout_webhooks.py.png) | |
| home | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/patrickaod/Shoply/main/home/admin.py) | ![screenshot](documentation/python_validation/pep8ci.herokuapp.com_https___raw.githubusercontent.com_patrickaod_Shoply_main_home_admin.py.png) | |
| home | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/patrickaod/Shoply/main/home/models.py) | ![screenshot](documentation/python_validation/pep8ci.herokuapp.com_https___raw.githubusercontent.com_patrickaod_Shoply_main_home_models.py.png) | |
| home | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/patrickaod/Shoply/main/home/urls.py) | ![screenshot](documentation/python_validation/pep8ci.herokuapp.com_https___raw.githubusercontent.com_patrickaod_Shoply_main_home_urls.py.png) | |
| home | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/patrickaod/Shoply/main/home/views.py) | ![screenshot](documentation/python_validation/pep8ci.herokuapp.com_https___raw.githubusercontent.com_patrickaod_Shoply_main_home_views.py.png) | |
|  | manage.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/patrickaod/Shoply/main/manage.py) | ![screenshot](documentation/python_validation/pep8ci.herokuapp.com_https___raw.githubusercontent.com_patrickaod_Shoply_main_manage.py.png) | |
| products | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/patrickaod/Shoply/main/products/admin.py) | ![screenshot](documentation/python_validation/pep8ci.herokuapp.com_https___raw.githubusercontent.com_patrickaod_Shoply_main_products_admin.py.png) | |
| products | contexts.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/patrickaod/Shoply/main/products/contexts.py) | ![screenshot](documentation/python_validation/pep8ci.herokuapp.com_https___raw.githubusercontent.com_patrickaod_Shoply_main_products_contexts.py.png) | |
| products | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/patrickaod/Shoply/main/products/forms.py) | ![screenshot](documentation/python_validation/pep8ci.herokuapp.com_https___raw.githubusercontent.com_patrickaod_Shoply_main_products_forms.py.png) | |
| products | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/patrickaod/Shoply/main/products/models.py) | ![screenshot](documentation/python_validation/pep8ci.herokuapp.com_https___raw.githubusercontent.com_patrickaod_Shoply_main_products_models.py.png) | |
| products | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/patrickaod/Shoply/main/products/urls.py) | ![screenshot](documentation/python_validation/pep8ci.herokuapp.com_https___raw.githubusercontent.com_patrickaod_Shoply_main_products_urls.py.png) | |
| products | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/patrickaod/Shoply/main/products/views.py) | ![screenshot](documentation/python_validation/pep8ci.herokuapp.com_https___raw.githubusercontent.com_patrickaod_Shoply_main_products_views.py.png) | |
| profiles | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/patrickaod/Shoply/main/profiles/admin.py) | ![screenshot](documentation/python_validation/pep8ci.herokuapp.com_https___raw.githubusercontent.com_patrickaod_Shoply_main_profiles_admin.py.png) | |
| profiles | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/patrickaod/Shoply/main/profiles/forms.py) | ![screenshot](documentation/python_validation/pep8ci.herokuapp.com_https___raw.githubusercontent.com_patrickaod_Shoply_main_profiles_forms.py.png) | |
| profiles | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/patrickaod/Shoply/main/profiles/models.py) | ![screenshot](documentation/python_validation/pep8ci.herokuapp.com_https___raw.githubusercontent.com_patrickaod_Shoply_main_profiles_models.py.png) | |
| profiles | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/patrickaod/Shoply/main/profiles/urls.py) | ![screenshot](documentation/python_validation/pep8ci.herokuapp.com_https___raw.githubusercontent.com_patrickaod_Shoply_main_profiles_urls.py.png) | |
| profiles | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/patrickaod/Shoply/main/profiles/views.py) | ![screenshot](documentation/python_validation/pep8ci.herokuapp.com_https___raw.githubusercontent.com_patrickaod_Shoply_main_profiles_views.py.png) | |
| shoply | cvs_to_json.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/patrickaod/Shoply/main/shoply/management/commands/cvs_to_json.py) | ![screenshot](documentation/python_validation/pep8ci.herokuapp.com_https___raw.githubusercontent.com_patrickaod_Shoply_main_shoply_management_commands_cvs_to_json.py.png) | |
| shoply | dataset_processor.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/patrickaod/Shoply/main/shoply/management/commands/dataset_processor.py) | ![screenshot](documentation/python_validation/pep8ci.herokuapp.com_https___raw.githubusercontent.com_patrickaod_Shoply_main_shoply_management_commands_dataset_processor.py.png) | |
| shoply | kaggle_api_handler.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/patrickaod/Shoply/main/shoply/management/commands/kaggle_api_handler.py) | ![screenshot](documentation/python_validation/pep8ci.herokuapp.com_https___raw.githubusercontent.com_patrickaod_Shoply_main_shoply_management_commands_kaggle_api_handler.py.png) | |
| shoply | settings.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/patrickaod/Shoply/main/shoply/settings.py) | ![screenshot](documentation/python_validation/pep8ci.herokuapp.com_https___raw.githubusercontent.com_patrickaod_Shoply_main_shoply_settings.py.png) | |
| shoply | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/patrickaod/Shoply/main/shoply/urls.py) | ![screenshot](documentation/python_validation/pep8ci.herokuapp.com_https___raw.githubusercontent.com_patrickaod_Shoply_main_shoply_urls.py.png) | |
| user_activity | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/patrickaod/Shoply/main/user_activity/admin.py) | ![screenshot](documentation/python_validation/pep8ci.herokuapp.com_https___raw.githubusercontent.com_patrickaod_Shoply_main_user_activity_admin.py.png) | |
| user_activity | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/patrickaod/Shoply/main/user_activity/models.py) | ![screenshot](documentation/python_validation/pep8ci.herokuapp.com_https___raw.githubusercontent.com_patrickaod_Shoply_main_user_activity_models.py.png) | |
| user_activity | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/patrickaod/Shoply/main/user_activity/views.py) | ![screenshot](documentation/python_validation/pep8ci.herokuapp.com_https___raw.githubusercontent.com_patrickaod_Shoply_main_user_activity_views.py.png) | |

## Browser Compatibility

Cross-browser testing is important to make sure your website works well on different browsers, like Chrome, Firefox, Safari, and Edge. Since each browser can show things a little differently, testing helps catch any problems with how your site looks or works.

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Home | Product | Product Details | Checkout | Notes |
| --- | --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/browser_compat/chrome_home.png) | ![screenshot](documentation/browser_compat/chrome_products.png) | ![screenshot](documentation/browser_compat/chrome_prod_details.png) | ![screenshot](documentation/browser_compat/chrome_checkout.png) | Works as expected |
| Edge | ![screenshot](documentation/browser_compat/edge_home.png) | ![screenshot](documentation/browser_compat/edge_products.png) | ![screenshot](documentation/browser_compat/edge_prod_details.png) | ![screenshot](documentation/browser_compat/edge_checkout.png) | Works as expected |
| Firefox | ![screenshot](documentation/browser_compat/fox_home.png) | ![screenshot](documentation/browser_compat/fox_products.png) | ![screenshot](documentation/browser_compat/fox_prod_details.png) | ![screenshot](documentation/browser_compat/fox_checkout.png) | Works as expected |
