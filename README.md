# [Shoply: An eCommerce Platform Built for Success](https://shoply-93586e37ffa3.herokuapp.com)

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/patrickaod/Shoply)](https://github.com/patrickaod/Shoply/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/patrickaod/Shoply)](https://github.com/patrickaod/Shoply/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/patrickaod/Shoply)](https://github.com/patrickaod/Shoply)

Shoply is a full-featured eCommerce platform developed using [Django 5](https://www.djangoproject.com/), designed to demonstrate advanced web development skills while providing a practical, scalable, and modern solution for online shopping. The project leverages a powerful tech stack, including [Stripe](https://stripe.com/gb) for secure payments, [Bootstrap 5](https://getbootstrap.com/) for responsive design, [Django Allauth](https://docs.allauth.org/en/latest/) for seamless authentication, and custom commands for streamlined data integration.

## Project Overview

Shoply is not just a technical exercise but a fully operational eCommerce site that demonstrates the ability to design, build, and deploy a comprehensive web application. A key feature of the platform is its ability to populate content dynamically using datasets sourced from [Kaggle](https://www.kaggle.com/) via [Django management commands](https://docs.djangoproject.com/en/5.1/ref/django-admin/). This feature reflects real-world scenarios where developers must manage and integrate large-scale data efficiently.

Core features include:

- Dynamic Product Listings: Populated using datasets downloaded and processed from [Kaggle](https://www.kaggle.com/).
- Secure Payment Integration: Powered by [Stripe](https://stripe.com/gb) for robust and flexible transactions.
- Responsive Design: A sleek, mobile-first interface built with [Bootstrap 5](https://getbootstrap.com/).
- User Authentication: Simplified and secure logins using [Django Allauth](https://docs.allauth.org/en/latest/).
- Interactive Features: Enhanced accessability, interactivity and usability with [jQuery](https://jquery.com/).

![amIresponsive](documentation/overview/shoply_amiResponsive.png)

## UX

I built Shoply around datasets that I downloaded and processed through my custom data pipeline, using the insights they provided to shape every aspect of the website. By allowing the data to guide the design, I created a platform that’s not only clear and responsive but also deeply engaging for users. Features like "Recently Viewed" and "Top Trending" are powered directly by user behavior and sales data, creating a personalized experience that keeps customers coming back. The dynamic admin interface makes managing product listings effortless, while the navigation automatically adjusts to category changes with liquid formatting, ensuring a smooth and intuitive browsing experience. To further enhance the platform's appeal, I incorporated a unique logo, crafted using DALL·E, giving Shoply a fresh, modern identity that stands out.

### Colour Scheme
I first leveraged [DALL·E](https://openai.com/index/dall-e-3/) to generate an original and distinctive no-image found .jpeg that aligned with the modern aesthetic I wanted for the platform. 

![Shoply no_image found jpeg](static/img/no_image.jpeg)

After obtaining the image from [DALL·E](https://openai.com/index/dall-e-3/), I used [pixlr](https://pixlr.com/express/) (a free photo editing suite) to crop out the site’s logo and isolate it for integration into the design. 

![Shoply Logo](static/img/shoply_logo.png)

Next, I turned to [Coolors](https://coolors.co/), a color palette generator, to select a cohesive color scheme that would complement the logo and enhance the overall aesthetic of the site. After experimenting with various options, chose a color palette that balances cool blues and warm accents to evoke a sense of trust, professionalism, and approachability.

#### Colour Scheme Extraction
![Colour Scheme Extraction](documentation/ux/colour_scheme_extraction.png)
#### Final Colour Scheme
![Final Colour Scheme](documentation/ux/colour_scheme.png)
- Kepple: `#3FB2A5` used for primary text
- Dark Green: `#043A30` used for secondary text
- Honeydew: `#D0EFDF` used for neutral tones
- Black: `#000000` used for dark text
- Gamboge: `#f39c12` used for contrasting accents

I've implemented them as CSS `:root` variables to easily update the global colour scheme by changing only one value, instead of everywhere in the CSS file.

```css
:root {
  /* Light Green */
  --primary-color: #3FB2A5;
  /* Dark Green */
  --secondary-color: #043A30;
  /* Off-White / Light Mint */
  --neutral-light: #D0EFDF;
  /* Black */
  --text-dark: #000000;
  /* Orange */
  --accent-color: #f39c12;
}
```

### Typography

- [Poppins](https://fonts.google.com/specimen/Poppins) was used for the primary headers and titles.

- [Roboto](https://fonts.google.com/specimen/Roboto) was used for all other secondary text.

- [Pacifico](https://fonts.google.com/specimen/Pacifico) was used for the accent text.

- [Font Awesome](https://fontawesome.com) icons were used throughout the site, such as the account and basket icons in the navigation.

## User Stories

### Shopper

- As a shopper, I would like to view a list of products, so that I can select some to purchase.
- As a shopper, I would like to view specific categories, so that I can find something quickly.
- As a shopper, I would like to select out a product, so that I focus on the product itself.


### New Site Users

- As a new site user, I would like to easily login, so that I can access my information quickly.
- As a new site user, I would like to easily register, so that I can view my personal profile.
- As a new site user, I would like to recieve email confirmation, so that I can verify my purchase.

### Returning Site Users

- As a returning site user, I would like to have my orders saved, so that I can review my purchases.
- As a returning site user, I would like to quick access to products I've seen before, so that I don't have to write anything down.
- As a returning site user, I would like to quickly see the most popular items, so that I can find some quick christmas gifts.

### Site Admin

- As a site administrator, I should be able to modify profiles, so that I can maintain site security.
- As a site administrator, I should be able to see all products, so that I can check site inventory.
- As a site administrator, I should be able to see change products, so that I can update site inventory.
## Features

### Existing Features

- **Logo Brand**

    - The logo and brand name provide a easy site wide return to home familiar to all regular internet users.

![Logo Brand](documentation/features/logo_brand.png)

- **Categories Dropdown**

    - The Categories Dropdown dynamically updates depending what data has been uploaded with the field `categoryName`. 

![Categories Dropdown](documentation/features/categories.png)

- **Search Bar**

    - The search bar allows users to quickly narrow the products selection by title or category.

![Search Bar](documentation/features/search.png)

- **Profile Icon**

    - The fontawesome [user icon](https://fontawesome.com/icons/user?f=classic&s=solid) dynamically displays options depending on session status. 

![Profile Icon](documentation/features/user_reg.png)
![Profile Icon](documentation/features/user_admin.png)
![Profile Icon](documentation/features/login.png)

- **Shopping Bag - Basket Icon**

    - The shopping bag is accessed site wide through the navigation's fontawesome [basket icon](https://fontawesome.com/icons/basket-shopping?s=solid)

![Shopping Bag](documentation/features/basket.png)

- **Welcome - Call To Action**

    - Upon arrival the user/shopper is greeted by a busy festive shoppers creating a sense of motion. A big call to action is centered in frosted glass (`The new collections are here`) in Poppins font next to another bright Gamboge orange call to action button with more festive features 🎄. 

![Welcome - Call To Action](documentation/features/welcome.png)

- **Trending Now**

    - The trending now feature looks for items with the `isBestSeller` field and places a random selection using the [random module](https://docs.python.org/3/library/random.html) on a users homescreen.

```py 
# Get all bestseller products
    bestseller_products = list(Product.objects.filter(isBestSeller=True))
    # Shuffle and pick up to 5
    trending_products = random.sample(bestseller_products, min(len(bestseller_products), 5))

```
![Trending Now](documentation/features/trending.png)

- **Recently Viewed**

    - A random selection of up to 5 recently viewed items will be displayed here, sourced from cookies for anonymous users and from the database for account holders.

```py
# Fetch recently viewed products
    recently_viewed_products = []
    if request.user.is_authenticated:
        # For logged-in users: fetch from the database
        recent_views = RecentlyViewedProduct.objects.filter(user=request.user).select_related('product')[:10]
        recently_viewed_products = [view.product for view in recent_views]
    else:
        # For anonymous users: fetch from session
        recently_viewed_ids = request.session.get('recently_viewed', [])
        recently_viewed_products = Product.objects.filter(id__in=recently_viewed_ids)

    # Randomly sample up to 5 recently viewed products
    recently_viewed_sample = random.sample(
        list(recently_viewed_products),
        min(len(recently_viewed_products), 5)
    )
```
![Recently Viewed](documentation/features/recently.png)

- **Price Tag**

    - The updates dynamically according to the items price listed in the database. 

![Price Tag](documentation/features/price_tag.png)

- **Products**

    - The products section utilises using bootstraps helper classes to responively layout all the desired product cards.

![Products](documentation/features/products.png)

- **Product Cards**

    - The product card provides a quick snapshot of the product, displaying only the truncated title and price for simplicity. It includes a subtle hover effect, elevating the card to offer visual feedback to the user. A vibrant gamboge-orange 'View [More] Details' button adds an eye-catching call-to-action.

![Product Cards](documentation/features/product_card.png)

- **Pagination**

    - Pagination improves user experience by breaking down large sets of data into manageable chunks. It also enhances performance by loading only a portion of the data at a time.

![Pagination](documentation/features/pagination.png)

- **Product Details**

    - The Product Details page provides an in-depth view of the product in a clean and user-friendly layout. A large image on the left expands for a closer look, while all the product details are prominently displayed in a section directly beside it. The title is fully visible (untruncated), and the page includes a quantity selector and direct links for seamless navigation back to related products or all products.

![Product Details](documentation/features/product_details.png)

- **Server Messages**

    - Server messages provide users with real-time feedback about their actions, enhancing clarity and ensuring a smoother, more informed user experience.

![Server Messages](documentation/features/messages.png)

- **User Profile**

    - User profiles provide customers with convenient access to delivery information and their order history.

![User Profile](documentation/features/user_profile.png)

- **Admin Profile**

    - The admin profile enables administrators to add products to the site via the Website Management link, with room for future feature expansion.

![Admin Profile](documentation/features/admin_profile.png)

- The admin profile allows administrators to edit or delete products directly from the product cards for easy management.

![Admin Product Options](documentation/features/admin_options.png)

- **Shopping Bag**

    - The shopping bag benefits the user by providing an intuitive, interactive shopping bag interface where they can easily view and manage their selected items, adjust quantities, or remove products. The page also includes a convenient "Continue Shopping" button, allowing users to easily return to browsing.

![Shopping Bag](documentation/features/shopping_bag.png)

- **Shopping Summmary**

    - Additionally, the shopping bag offers a clear breakdown of costs, including delivery fees and free delivery eligibility, ensuring a smooth and informed checkout process.

![Shopping Summmary](documentation/features/shopping_summary.png)

- **Stripe Checkout**

    - The checkout benefits the user by providing a streamlined checkout process with a clear order summary, secure payment integration, and the ability to easily amend thier delivery address.

![Stripe Checkout](documentation/features/checkout.png)

- **Checkout Spinner**

    - The checkout spinner provides users with a visual cue that their payment is being processed, ensuring they know the system is working on their order.

![Checkout Spinner](documentation/features/spinner.png)

- **Checkout Success**

    - This page benefits the user by providing a clear and detailed order confirmation. It also offers convenient options for users to either return to browsing the website.

![Checkout Success](documentation/features/checkout_success.png)

- **Confirmation Email**

    - The dedicated email system allows for future expansion, starting with order confirmations and paving the way for additional notifications and updates.

![Confirmation Email](documentation/features/emails.png)


- **Sign Up, Sign In, Sign Out**

    - The sign-in, sign-out, and registration allauth forms provide a seamless user experience, allowing easy access, secure logout, and the ability to create new accounts, with future scalability for additional user features.

![Register](documentation/features/register.png)
![Sign In](documentation/features/sign_in.png)
![Sign Out](documentation/features/sign_out.png)
### Developer Features

**Kaggle Data Pipeline**

This pipeline consists of three programs designed to download, process, and convert Kaggle datasets. The first command handles downloading datasets from Kaggle, the second processes and filters the dataset according to user preferences, and the third converts the processed data into a structured JSON format suitable for Django fixtures.

**`kaggle_api_handler`**

Downloads and organizes datasets from Kaggle by authenticating with the Kaggle API and saving them to a local directory.

 - Dataset URL input: The user provides the last part of the Kaggle dataset URL to specify which dataset to download.
 - Kaggle authentication: Uses credentials stored in environment variables (KAGGLE_USERNAME and KAGGLE_KEY) for API authentication.
 - Folder creation: Ensures that the necessary directory (data/raw/) exists and creates it if missing.
 - Error handling: Extensive error logging for missing credentials, download failures, and invalid inputs.
 - Progress logging: Provides detailed logs at each step to track the process, from authentication to successful download.

**`dataset_processor`**

Filters and samples a CSV dataset based on user input and saves the processed data to a new CSV file with a timestamp.

 - User inputs: The program prompts the user for the file to process, the header to filter by, elements to sample, and the number of samples per category.
 - Error handling: Handles issues like missing headers, invalid sample sizes, and issues during CSV loading.
 - Data filtering: Filters the dataset based on selected categories or elements from the chosen header column.
 - Data sampling: Allows for both random sampling or taking the first n entries for each element in the dataset.
 - Processed file saving: Saves the processed data to data/processed/ with a timestamped filename to avoid overwriting.

**`csv_to_json_converter`**

Converts a CSV file into a JSON format suitable for Django fixtures, with a replacement timestamp added to the filename for uniqueness.

 - User input: The user provides the path to the processed CSV file that they want to convert into JSON.
 - Timestamp handling: Automatically adds or replaces a timestamp in the filename to ensure the new file name is unique.
 - CSV to JSON conversion: Reads the CSV file, converts it into a structured JSON format suitable for Django models, and saves it to data/json/.
 - Error handling: Catches issues like invalid CSV format and JSON writing errors.
 - Logging: Provides logs for each step, including file processing, conversion, and saving to ensure transparency.

**`Loggers`**

Loggers are a great way for developers to track their projects in real-time. Providing valuable insights into the development process.

```py
LOGGING = {
    'version': 1,  # Use version 1 for Django logging configuration
    'disable_existing_loggers': False,  # Keeps the default Django loggers enabled
    'formatters': {
        'verbose': {  # Defines a format for more detailed logging output
        },
        'simple': {  # Simpler format for quick debugging
        },
    },
    'handlers': {
        'console': {  # Console handler to output logs to the terminal    
        },
        'file': {  # File handler to write logs to a file
        },
    },
    'loggers': {
        '': {  # Root logger - captures all logs
        },
        'django': {  # Logger specifically for Django logs
        },
        'django.request': {  # Logger specifically for HTTP request logs
        },
        'shoply': {  # Custom logger you can use in your applications
            'handlers': ['console', 'file'],
            'level': 'DEBUG',  # Set lower for detailed logs when debugging
            'propagate': False,
        },
    },
}
```
### Future Features

- Persoanlised Recommendations 
    - Upgrade the user_activity application with AI features, heatmaps and session recording, funnel and behavioral analysis.
- Advanced Stripe functionality 
    - Subscriptions to services like "Prime", Better card detail saving, or advanced fraud protections.
- Customer Review & Ratings
    - Written review from verified customers would add to buyer's confidence. 
- Social Media Integration
    - Allows customers to log in, share products, or purchase directly from social media platforms like Instagram or Facebook.
- Open the Marketplace
    - Create an open marketplace like Gumtree or Facebook Marketplace
- Improve Data Pipeline
    - The intergration of large dataset could be refined further with a dashboard to analysis and further customise the filtering process. 
- Dynamic Pricing 
    - Adjusts product pricing based on factors such as demand, competition, or customer loyalty
- Modular Implementation
    - Develop a dynamic website that allows deals to be easily created, uploaded, and automatically displayed in designated sections. The goal is to minimize maintenance while maximizing user engagement through seamless content management and real-time updates.

