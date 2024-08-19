# jumpseller_api

JumpsellerApi - JavaScript client for jumpseller_api
# Endpoint Structure

All URLs are in the format: 

```text
https://api.jumpseller.com/v1/path.json?login=XXXXXX&authtoken=storetoken  
```

The path is prefixed by the API version and the URL takes as parameters the login (your store specific API login) and your authentication token.
<br/><br/>
***

# Version

The current version of the API is **v1**.  
If we change the API in backward-incompatible ways, we'll increase the version number and maintain stable support for the old urls.
<br/><br/>
***

# Authentication

The API uses a token-based authentication with a combination of a login key and an auth token. **Both parameters can be found on the left sidebar of the Account section, accessed from the main menu of your Admin Panel**. The auth token of the user can be reset on the same page.

![Store Login](/images/support/api/apilogin.png)

The auth token is a **32 characters** string.

If you are developing a Jumpseller App, the authentication should be done using [OAuth-2](/support/oauth-2). Please read the article [Build an App](/support/apps) for more information.
<br/><br/>
***

# Curl Examples

To request all the products at your store, you would append the products index path to the base url to create an URL with the format:  

```text
https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX
```

In curl, you can invoque that URL with:  

```text
curl -X GET \"https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX\"
```

To create a product, you will include the JSON data and specify the MIME Type:  

```text
curl -X POST -d '{ \"product\" : {\"name\": \"My new Product!\", \"price\": 100} }' \"https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX\" -H \"Content-Type:application/json\"
```

and to update the product identified with 123:  

```text
curl -X PUT -d '{ \"product\" : {\"name\": \"My updated Product!\", \"price\": 99} }' \"https://api.jumpseller.com/v1/products/123.json?login=XXXXXX&authtoken=XXXXX\" -H \"Content-Type:application/json\"
```

or delete it:  

```text
curl -X DELETE \"https://api.jumpseller.com/v1/products/123.json?login=XXXXXX&authtoken=XXXXX\" -H \"Content-Type:application/json\"
```
<br/><br/>
***

# PHP Examples

Create a new Product (POST method)

```php
$url = 'https://api.jumpseller.com/v1/products.json?login=XXXXX&authtoken=XXXXX;
$ch = curl_init($url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));

curl_setopt($ch, CURLOPT_CUSTOMREQUEST, \"POST\"); //post method
curl_setopt($ch, CURLOPT_POSTFIELDS, '{ \"product\" : {\"name\": \"My updated Product!\", \"price\": 99} }');

$result = curl_exec($ch);
print_r($result);
curl_close($ch);
```
<br/><br/>
***

# Plain JSON only. No XML.

* We only support JSON for data serialization.
* Our node format has no root element.  
* We use snake_case to describe attribute keys (like \"created_at\").  
* All empty value are replaced with **null** strings.
* All API URLs end in .json to indicate that they accept and return JSON.
* POST and PUT methods require you to explicitly state the MIME type of your request's body content as **\"application/json\"**.
<br/><br/>
***

# Rate Limit
You can perform a maximum of:

+ 240 (two hundred forty) requests per minute and
+ 8 (eight) requests per second 

If you exceed this limit, you'll get a 403 Forbidden (Rate Limit Exceeded) response for subsequent requests.  

The rate limits apply by IP address and by store. This means that multiple requests on different stores are not counted towards the same rate limit.

This limits are necessary to ensure resources are correctly used. Your application should be aware of this limits and retry any unsuccessful request, check the following Ruby stub:

```ruby
tries = 0; max_tries = 3;
begin
  HTTParty.send(method, uri) # perform an API call.
  sleep 0.5
  tries += 1
rescue
  unless tries >= max_tries
    sleep 1.0 # wait the necessary time before retrying the call again.
    retry
  end
end
```

Finally, you can review the Response Headers of each request:

```text
Jumpseller-PerMinuteRateLimit-Limit: 60  
Jumpseller-PerMinuteRateLimit-Remaining: 59 # requests available on the per-second interval  
Jumpseller-PerSecondRateLimit-Limit: 2  
Jumpseller-PerSecondRateLimit-Remaining: 1 # requests available on the per-second interval
``` 

to better model your application requests intervals.

In the event of getting your IP banned, the Response Header `Jumpseller-BannedByRateLimit-Reset` informs you the time when will your ban be reseted.
<br/><br/>
***

# Pagination

By default we will return 50 objects (products, orders, etc) per page. There is a maximum of 100, using a query string `&limit=100`.
If the result set gets paginated it is your responsibility to check the next page for more objects -- you do this by using query strings `&page=2`, `&page=3` and so on.

```text
https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX&page=3&limit=100
```
<br/><br/>
***

# More
* [Jumpseller API wrapper](https://gitlab.com/jumpseller-api/ruby) provides a public Ruby abstraction over our API;
* [Apps Page](/apps) showcases external integrations with Jumpseller done by technical experts;
* [Imgbb API](https://api.imgbb.com/) provides an easy way to upload and temporaly host for images and files.
<br/><br/>
***
<br/><br/>

This SDK is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.JavascriptClientCodegen

## Installation

### For [Node.js](https://nodejs.org/)

#### npm

To publish the library as a [npm](https://www.npmjs.com/), please follow the procedure in ["Publishing npm packages"](https://docs.npmjs.com/getting-started/publishing-npm-packages).

Then install it via:

```shell
npm install jumpseller_api --save
```

Finally, you need to build the module:

```shell
npm run build
```

##### Local development

To use the library locally without publishing to a remote npm registry, first install the dependencies by changing into the directory containing `package.json` (and this README). Let's call this `JAVASCRIPT_CLIENT_DIR`. Then run:

```shell
npm install
```

Next, [link](https://docs.npmjs.com/cli/link) it globally in npm with the following, also from `JAVASCRIPT_CLIENT_DIR`:

```shell
npm link
```

To use the link you just defined in your project, switch to the directory you want to use your jumpseller_api from, and run:

```shell
npm link /path/to/<JAVASCRIPT_CLIENT_DIR>
```

Finally, you need to build the module:

```shell
npm run build
```

#### git

If the library is hosted at a git repository, e.g.https://github.com/GIT_USER_ID/GIT_REPO_ID
then install it via:

```shell
    npm install GIT_USER_ID/GIT_REPO_ID --save
```

### For browser

The library also works in the browser environment via npm and [browserify](http://browserify.org/). After following
the above steps with Node.js and installing browserify with `npm install -g browserify`,
perform the following (assuming *main.js* is your entry file):

```shell
browserify main.js > bundle.js
```

Then include *bundle.js* in the HTML pages.

### Webpack Configuration

Using Webpack you may encounter the following error: "Module not found: Error:
Cannot resolve module", most certainly you should disable AMD loader. Add/merge
the following section to your webpack config:

```javascript
module: {
  rules: [
    {
      parser: {
        amd: false
      }
    }
  ]
}
```

## Getting Started

Please follow the [installation](#installation) instruction and execute the following JS code:

```javascript
var JumpsellerApi = require('jumpseller_api');


var api = new JumpsellerApi.AppsApi()
var login = "login_example"; // {String} API OAuth login.
var authtoken = "authtoken_example"; // {String} API OAuth token.
var code = "code_example"; // {String} Code of the App
var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
api.jsappsCodeJsonDelete(login, authtoken, code, callback);

```

## Documentation for API Endpoints

All URIs are relative to *https://api.jumpseller.com/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*JumpsellerApi.AppsApi* | [**jsappsCodeJsonDelete**](docs/AppsApi.md#jsappsCodeJsonDelete) | **DELETE** /jsapps/{code}.json | Delete an existing JSApp.
*JumpsellerApi.AppsApi* | [**jsappsCodeJsonGet**](docs/AppsApi.md#jsappsCodeJsonGet) | **GET** /jsapps/{code}.json | Retrieve a JSApp.
*JumpsellerApi.AppsApi* | [**jsappsJsonGet**](docs/AppsApi.md#jsappsJsonGet) | **GET** /jsapps.json | Retrieve all the Store&#39;s JSApps.
*JumpsellerApi.AppsApi* | [**jsappsJsonPost**](docs/AppsApi.md#jsappsJsonPost) | **POST** /jsapps.json | Create a Store JSApp.
*JumpsellerApi.CategoriesApi* | [**categoriesCountJsonGet**](docs/CategoriesApi.md#categoriesCountJsonGet) | **GET** /categories/count.json | Count all Categories.
*JumpsellerApi.CategoriesApi* | [**categoriesIdJsonDelete**](docs/CategoriesApi.md#categoriesIdJsonDelete) | **DELETE** /categories/{id}.json | Delete an existing Category.
*JumpsellerApi.CategoriesApi* | [**categoriesIdJsonGet**](docs/CategoriesApi.md#categoriesIdJsonGet) | **GET** /categories/{id}.json | Retrieve a single Category.
*JumpsellerApi.CategoriesApi* | [**categoriesIdJsonPut**](docs/CategoriesApi.md#categoriesIdJsonPut) | **PUT** /categories/{id}.json | Modify an existing Category.
*JumpsellerApi.CategoriesApi* | [**categoriesJsonGet**](docs/CategoriesApi.md#categoriesJsonGet) | **GET** /categories.json | Retrieve all Categories.
*JumpsellerApi.CategoriesApi* | [**categoriesJsonPost**](docs/CategoriesApi.md#categoriesJsonPost) | **POST** /categories.json | Create a new Category.
*JumpsellerApi.CheckoutCustomFieldsApi* | [**checkoutCustomFieldsIdJsonDelete**](docs/CheckoutCustomFieldsApi.md#checkoutCustomFieldsIdJsonDelete) | **DELETE** /checkout_custom_fields/{id}.json | Delete an existing CheckoutCustomField.
*JumpsellerApi.CheckoutCustomFieldsApi* | [**checkoutCustomFieldsIdJsonGet**](docs/CheckoutCustomFieldsApi.md#checkoutCustomFieldsIdJsonGet) | **GET** /checkout_custom_fields/{id}.json | Retrieve a single CheckoutCustomField.
*JumpsellerApi.CheckoutCustomFieldsApi* | [**checkoutCustomFieldsIdJsonPut**](docs/CheckoutCustomFieldsApi.md#checkoutCustomFieldsIdJsonPut) | **PUT** /checkout_custom_fields/{id}.json | Update a CheckoutCustomField.
*JumpsellerApi.CheckoutCustomFieldsApi* | [**checkoutCustomFieldsJsonGet**](docs/CheckoutCustomFieldsApi.md#checkoutCustomFieldsJsonGet) | **GET** /checkout_custom_fields.json | Retrieve all Checkout Custom Fields.
*JumpsellerApi.CheckoutCustomFieldsApi* | [**checkoutCustomFieldsJsonPost**](docs/CheckoutCustomFieldsApi.md#checkoutCustomFieldsJsonPost) | **POST** /checkout_custom_fields.json | Create a new CheckoutCustomField.
*JumpsellerApi.CountriesApi* | [**countriesCountryCodeJsonGet**](docs/CountriesApi.md#countriesCountryCodeJsonGet) | **GET** /countries/{country_code}.json | Retrieve a single Country information.
*JumpsellerApi.CountriesApi* | [**countriesCountryCodeRegionsJsonGet**](docs/CountriesApi.md#countriesCountryCodeRegionsJsonGet) | **GET** /countries/{country_code}/regions.json | Retrieve all Regions from a single Country.
*JumpsellerApi.CountriesApi* | [**countriesCountryCodeRegionsRegionCodeJsonGet**](docs/CountriesApi.md#countriesCountryCodeRegionsRegionCodeJsonGet) | **GET** /countries/{country_code}/regions/{region_code}.json | Retrieve a single Region information object.
*JumpsellerApi.CountriesApi* | [**countriesJsonGet**](docs/CountriesApi.md#countriesJsonGet) | **GET** /countries.json | Retrieve all Countries.
*JumpsellerApi.CustomFieldSelectOptionsApi* | [**customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonGet**](docs/CustomFieldSelectOptionsApi.md#customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonGet) | **GET** /custom_fields/{id}/select_options/{custom_field_select_option_id}.json | Retrieve a single SelectOption from a CustomField.
*JumpsellerApi.CustomFieldSelectOptionsApi* | [**customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonPut**](docs/CustomFieldSelectOptionsApi.md#customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonPut) | **PUT** /custom_fields/{id}/select_options/{custom_field_select_option_id}.json | Update a SelectOption from a CustomField.
*JumpsellerApi.CustomFieldSelectOptionsApi* | [**customFieldsIdSelectOptionsJsonGet**](docs/CustomFieldSelectOptionsApi.md#customFieldsIdSelectOptionsJsonGet) | **GET** /custom_fields/{id}/select_options.json | Retrieve all Store&#39;s Custom Fields.
*JumpsellerApi.CustomFieldSelectOptionsApi* | [**customFieldsIdSelectOptionsJsonPost**](docs/CustomFieldSelectOptionsApi.md#customFieldsIdSelectOptionsJsonPost) | **POST** /custom_fields/{id}/select_options.json | Create a new Custom Field Select Option.
*JumpsellerApi.CustomFieldsApi* | [**customFieldsIdJsonDelete**](docs/CustomFieldsApi.md#customFieldsIdJsonDelete) | **DELETE** /custom_fields/{id}.json | Delete an existing CustomField.
*JumpsellerApi.CustomFieldsApi* | [**customFieldsIdJsonGet**](docs/CustomFieldsApi.md#customFieldsIdJsonGet) | **GET** /custom_fields/{id}.json | Retrieve a single CustomField.
*JumpsellerApi.CustomFieldsApi* | [**customFieldsIdJsonPut**](docs/CustomFieldsApi.md#customFieldsIdJsonPut) | **PUT** /custom_fields/{id}.json | Update a CustomField.
*JumpsellerApi.CustomFieldsApi* | [**customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonDelete**](docs/CustomFieldsApi.md#customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonDelete) | **DELETE** /custom_fields/{id}/select_options/{custom_field_select_option_id}.json | Delete an existing CustomFieldSelectOption.
*JumpsellerApi.CustomFieldsApi* | [**customFieldsJsonGet**](docs/CustomFieldsApi.md#customFieldsJsonGet) | **GET** /custom_fields.json | Retrieve all Store&#39;s Custom Fields.
*JumpsellerApi.CustomFieldsApi* | [**customFieldsJsonPost**](docs/CustomFieldsApi.md#customFieldsJsonPost) | **POST** /custom_fields.json | Create a new Custom Field.
*JumpsellerApi.CustomerAdditionalFieldsApi* | [**customersIdFieldsFieldIdDelete**](docs/CustomerAdditionalFieldsApi.md#customersIdFieldsFieldIdDelete) | **DELETE** /customers/{id}/fields/{field_id} | Delete a Customer Additional Field.
*JumpsellerApi.CustomerAdditionalFieldsApi* | [**customersIdFieldsFieldIdGet**](docs/CustomerAdditionalFieldsApi.md#customersIdFieldsFieldIdGet) | **GET** /customers/{id}/fields/{field_id} | Retrieve a single Customer Additional Field.
*JumpsellerApi.CustomerAdditionalFieldsApi* | [**customersIdFieldsFieldIdPut**](docs/CustomerAdditionalFieldsApi.md#customersIdFieldsFieldIdPut) | **PUT** /customers/{id}/fields/{field_id} | Update a Customer Additional Field.
*JumpsellerApi.CustomerAdditionalFieldsApi* | [**customersIdFieldsGet**](docs/CustomerAdditionalFieldsApi.md#customersIdFieldsGet) | **GET** /customers/{id}/fields | Retrieves the Customer Additional Field of a Customer.
*JumpsellerApi.CustomerAdditionalFieldsApi* | [**customersIdFieldsPost**](docs/CustomerAdditionalFieldsApi.md#customersIdFieldsPost) | **POST** /customers/{id}/fields | Adds Customer Additional Fields to a Customer.
*JumpsellerApi.CustomerCategoriesApi* | [**customerCategoriesIdCustomersJsonDelete**](docs/CustomerCategoriesApi.md#customerCategoriesIdCustomersJsonDelete) | **DELETE** /customer_categories/{id}/customers.json | Delete Customers from an existing CustomerCategory.
*JumpsellerApi.CustomerCategoriesApi* | [**customerCategoriesIdCustomersJsonGet**](docs/CustomerCategoriesApi.md#customerCategoriesIdCustomersJsonGet) | **GET** /customer_categories/{id}/customers.json | Retrieves the customers in a CustomerCategory.
*JumpsellerApi.CustomerCategoriesApi* | [**customerCategoriesIdCustomersJsonPost**](docs/CustomerCategoriesApi.md#customerCategoriesIdCustomersJsonPost) | **POST** /customer_categories/{id}/customers.json | Adds Customers to a CustomerCategory.
*JumpsellerApi.CustomerCategoriesApi* | [**customerCategoriesIdJsonDelete**](docs/CustomerCategoriesApi.md#customerCategoriesIdJsonDelete) | **DELETE** /customer_categories/{id}.json | Delete an existing CustomerCategory.
*JumpsellerApi.CustomerCategoriesApi* | [**customerCategoriesIdJsonGet**](docs/CustomerCategoriesApi.md#customerCategoriesIdJsonGet) | **GET** /customer_categories/{id}.json | Retrieve a single CustomerCategory.
*JumpsellerApi.CustomerCategoriesApi* | [**customerCategoriesIdJsonPut**](docs/CustomerCategoriesApi.md#customerCategoriesIdJsonPut) | **PUT** /customer_categories/{id}.json | Update a CustomerCategory.
*JumpsellerApi.CustomerCategoriesApi* | [**customerCategoriesJsonGet**](docs/CustomerCategoriesApi.md#customerCategoriesJsonGet) | **GET** /customer_categories.json | Retrieve all Customer Categories.
*JumpsellerApi.CustomerCategoriesApi* | [**customerCategoriesJsonPost**](docs/CustomerCategoriesApi.md#customerCategoriesJsonPost) | **POST** /customer_categories.json | Create a new CustomerCategory.
*JumpsellerApi.CustomersApi* | [**customersCountJsonGet**](docs/CustomersApi.md#customersCountJsonGet) | **GET** /customers/count.json | Count all Customers.
*JumpsellerApi.CustomersApi* | [**customersEmailEmailJsonGet**](docs/CustomersApi.md#customersEmailEmailJsonGet) | **GET** /customers/email/{email}.json | Retrieve a single Customer by email.
*JumpsellerApi.CustomersApi* | [**customersIdJsonDelete**](docs/CustomersApi.md#customersIdJsonDelete) | **DELETE** /customers/{id}.json | Delete an existing Customer.
*JumpsellerApi.CustomersApi* | [**customersIdJsonGet**](docs/CustomersApi.md#customersIdJsonGet) | **GET** /customers/{id}.json | Retrieve a single Customer by id.
*JumpsellerApi.CustomersApi* | [**customersIdJsonPut**](docs/CustomersApi.md#customersIdJsonPut) | **PUT** /customers/{id}.json | Update a new Customer.
*JumpsellerApi.CustomersApi* | [**customersJsonGet**](docs/CustomersApi.md#customersJsonGet) | **GET** /customers.json | Retrieve all Customers.
*JumpsellerApi.CustomersApi* | [**customersJsonPost**](docs/CustomersApi.md#customersJsonPost) | **POST** /customers.json | Create a new Customer.
*JumpsellerApi.FulfillmentsApi* | [**fulfillmentsCountJsonGet**](docs/FulfillmentsApi.md#fulfillmentsCountJsonGet) | **GET** /fulfillments/count.json | Count all Fulfillments.
*JumpsellerApi.FulfillmentsApi* | [**fulfillmentsIdJsonGet**](docs/FulfillmentsApi.md#fulfillmentsIdJsonGet) | **GET** /fulfillments/{id}.json | Retrieve a single Fulfillment.
*JumpsellerApi.FulfillmentsApi* | [**fulfillmentsJsonGet**](docs/FulfillmentsApi.md#fulfillmentsJsonGet) | **GET** /fulfillments.json | Retrieve all Fulfillments.
*JumpsellerApi.FulfillmentsApi* | [**orderIdFulfillmentsJsonGet**](docs/FulfillmentsApi.md#orderIdFulfillmentsJsonGet) | **GET** /order/{id}/fulfillments.json | Retrieve the Fulfillments associated with the Order.
*JumpsellerApi.HooksApi* | [**hooksIdJsonDelete**](docs/HooksApi.md#hooksIdJsonDelete) | **DELETE** /hooks/{id}.json | Delete an existing Hook.
*JumpsellerApi.HooksApi* | [**hooksIdJsonGet**](docs/HooksApi.md#hooksIdJsonGet) | **GET** /hooks/{id}.json | Retrieve a single Hook.
*JumpsellerApi.HooksApi* | [**hooksIdJsonPut**](docs/HooksApi.md#hooksIdJsonPut) | **PUT** /hooks/{id}.json | Update a Hook.
*JumpsellerApi.HooksApi* | [**hooksJsonGet**](docs/HooksApi.md#hooksJsonGet) | **GET** /hooks.json | Retrieve all Hooks.
*JumpsellerApi.HooksApi* | [**hooksJsonPost**](docs/HooksApi.md#hooksJsonPost) | **POST** /hooks.json | Create a new Hook.
*JumpsellerApi.OrdersApi* | [**ordersAfterIdJsonGet**](docs/OrdersApi.md#ordersAfterIdJsonGet) | **GET** /orders/after/{id}.json | Retrieve orders filtered by Order Id.
*JumpsellerApi.OrdersApi* | [**ordersCountJsonGet**](docs/OrdersApi.md#ordersCountJsonGet) | **GET** /orders/count.json | Count all Orders.
*JumpsellerApi.OrdersApi* | [**ordersIdHistoryJsonGet**](docs/OrdersApi.md#ordersIdHistoryJsonGet) | **GET** /orders/{id}/history.json | Retrieve all Order History.
*JumpsellerApi.OrdersApi* | [**ordersIdHistoryJsonPost**](docs/OrdersApi.md#ordersIdHistoryJsonPost) | **POST** /orders/{id}/history.json | Create a new Order History Entry.
*JumpsellerApi.OrdersApi* | [**ordersIdJsonGet**](docs/OrdersApi.md#ordersIdJsonGet) | **GET** /orders/{id}.json | Retrieve a single Order.
*JumpsellerApi.OrdersApi* | [**ordersIdJsonPut**](docs/OrdersApi.md#ordersIdJsonPut) | **PUT** /orders/{id}.json | Modify an existing Order.
*JumpsellerApi.OrdersApi* | [**ordersJsonGet**](docs/OrdersApi.md#ordersJsonGet) | **GET** /orders.json | Retrieve all Orders.
*JumpsellerApi.OrdersApi* | [**ordersJsonPost**](docs/OrdersApi.md#ordersJsonPost) | **POST** /orders.json | Create a new Order.
*JumpsellerApi.OrdersApi* | [**ordersStatusStatusJsonGet**](docs/OrdersApi.md#ordersStatusStatusJsonGet) | **GET** /orders/status/{status}.json | Retrieve orders filtered by status.
*JumpsellerApi.PagesApi* | [**pagesCountJsonGet**](docs/PagesApi.md#pagesCountJsonGet) | **GET** /pages/count.json | Count all Pages.
*JumpsellerApi.PagesApi* | [**pagesIdJsonDelete**](docs/PagesApi.md#pagesIdJsonDelete) | **DELETE** /pages/{id}.json | Delete an existing Page.
*JumpsellerApi.PagesApi* | [**pagesIdJsonGet**](docs/PagesApi.md#pagesIdJsonGet) | **GET** /pages/{id}.json | Retrieve a single Page by id.
*JumpsellerApi.PagesApi* | [**pagesIdJsonPut**](docs/PagesApi.md#pagesIdJsonPut) | **PUT** /pages/{id}.json | Update a Page.
*JumpsellerApi.PagesApi* | [**pagesJsonGet**](docs/PagesApi.md#pagesJsonGet) | **GET** /pages.json | Retrieve all Pages.
*JumpsellerApi.PagesApi* | [**pagesJsonPost**](docs/PagesApi.md#pagesJsonPost) | **POST** /pages.json | Create a new Page.
*JumpsellerApi.PartnersApi* | [**partnersStoresJsonGet**](docs/PartnersApi.md#partnersStoresJsonGet) | **GET** /partners/stores.json | Retrieve statistics.
*JumpsellerApi.PartnersApi* | [**storeCheckStatusJsonGet**](docs/PartnersApi.md#storeCheckStatusJsonGet) | **GET** /store/check_status.json | Retrive store creation status.
*JumpsellerApi.PartnersApi* | [**storeCreateJsonPost**](docs/PartnersApi.md#storeCreateJsonPost) | **POST** /store/create.json | Create a Partnered Store
*JumpsellerApi.PaymentMethodsApi* | [**paymentMethodsIdJsonGet**](docs/PaymentMethodsApi.md#paymentMethodsIdJsonGet) | **GET** /payment_methods/{id}.json | Retrieve a single Payment Method.
*JumpsellerApi.PaymentMethodsApi* | [**paymentMethodsJsonGet**](docs/PaymentMethodsApi.md#paymentMethodsJsonGet) | **GET** /payment_methods.json | Retrieve all Store&#39;s Payment Methods.
*JumpsellerApi.ProductAttachmentsApi* | [**productsIdAttachmentsAttachmentIdJsonDelete**](docs/ProductAttachmentsApi.md#productsIdAttachmentsAttachmentIdJsonDelete) | **DELETE** /products/{id}/attachments/{attachment_id}.json | Delete a Product Attachment.
*JumpsellerApi.ProductAttachmentsApi* | [**productsIdAttachmentsAttachmentIdJsonGet**](docs/ProductAttachmentsApi.md#productsIdAttachmentsAttachmentIdJsonGet) | **GET** /products/{id}/attachments/{attachment_id}.json | Retrieve a single Product Attachment.
*JumpsellerApi.ProductAttachmentsApi* | [**productsIdAttachmentsCountJsonGet**](docs/ProductAttachmentsApi.md#productsIdAttachmentsCountJsonGet) | **GET** /products/{id}/attachments/count.json | Count all Product Attachments.
*JumpsellerApi.ProductAttachmentsApi* | [**productsIdAttachmentsJsonGet**](docs/ProductAttachmentsApi.md#productsIdAttachmentsJsonGet) | **GET** /products/{id}/attachments.json | Retrieve all Product Attachments.
*JumpsellerApi.ProductAttachmentsApi* | [**productsIdAttachmentsJsonPost**](docs/ProductAttachmentsApi.md#productsIdAttachmentsJsonPost) | **POST** /products/{id}/attachments.json | Create a new Product Attachment.
*JumpsellerApi.ProductCustomFieldsApi* | [**productsIdFieldsCountJsonGet**](docs/ProductCustomFieldsApi.md#productsIdFieldsCountJsonGet) | **GET** /products/{id}/fields/count.json | Count all Product Custom Fields.
*JumpsellerApi.ProductCustomFieldsApi* | [**productsIdFieldsJsonGet**](docs/ProductCustomFieldsApi.md#productsIdFieldsJsonGet) | **GET** /products/{id}/fields.json | Retrieve all Product Custom Fields
*JumpsellerApi.ProductCustomFieldsApi* | [**productsIdFieldsJsonPost**](docs/ProductCustomFieldsApi.md#productsIdFieldsJsonPost) | **POST** /products/{id}/fields.json | Add an existing Custom Field to a Product.
*JumpsellerApi.ProductCustomFieldsApi* | [**productsProductIdFieldsFieldIdJsonDelete**](docs/ProductCustomFieldsApi.md#productsProductIdFieldsFieldIdJsonDelete) | **DELETE** /products/{product_id}/fields/{field_id}.json | Delete value of Product Custom Field
*JumpsellerApi.ProductCustomFieldsApi* | [**productsProductIdFieldsFieldIdJsonPut**](docs/ProductCustomFieldsApi.md#productsProductIdFieldsFieldIdJsonPut) | **PUT** /products/{product_id}/fields/{field_id}.json | Update value of Product Custom Field
*JumpsellerApi.ProductDigitalProductsApi* | [**productsIdDigitalProductsCountJsonGet**](docs/ProductDigitalProductsApi.md#productsIdDigitalProductsCountJsonGet) | **GET** /products/{id}/digital_products/count.json | Count all Product DigitalProducts.
*JumpsellerApi.ProductDigitalProductsApi* | [**productsIdDigitalProductsDigitalProductIdJsonDelete**](docs/ProductDigitalProductsApi.md#productsIdDigitalProductsDigitalProductIdJsonDelete) | **DELETE** /products/{id}/digital_products/{digital_product_id}.json | Delete a Product DigitalProduct.
*JumpsellerApi.ProductDigitalProductsApi* | [**productsIdDigitalProductsDigitalProductIdJsonGet**](docs/ProductDigitalProductsApi.md#productsIdDigitalProductsDigitalProductIdJsonGet) | **GET** /products/{id}/digital_products/{digital_product_id}.json | Retrieve a single Product DigitalProduct.
*JumpsellerApi.ProductDigitalProductsApi* | [**productsIdDigitalProductsJsonGet**](docs/ProductDigitalProductsApi.md#productsIdDigitalProductsJsonGet) | **GET** /products/{id}/digital_products.json | Retrieve all Product DigitalProducts.
*JumpsellerApi.ProductDigitalProductsApi* | [**productsIdDigitalProductsJsonPost**](docs/ProductDigitalProductsApi.md#productsIdDigitalProductsJsonPost) | **POST** /products/{id}/digital_products.json | Create a new Product DigitalProduct.
*JumpsellerApi.ProductImagesApi* | [**productsIdImagesCountJsonGet**](docs/ProductImagesApi.md#productsIdImagesCountJsonGet) | **GET** /products/{id}/images/count.json | Count all Product Images.
*JumpsellerApi.ProductImagesApi* | [**productsIdImagesImageIdJsonDelete**](docs/ProductImagesApi.md#productsIdImagesImageIdJsonDelete) | **DELETE** /products/{id}/images/{image_id}.json | Delete a Product Image.
*JumpsellerApi.ProductImagesApi* | [**productsIdImagesImageIdJsonGet**](docs/ProductImagesApi.md#productsIdImagesImageIdJsonGet) | **GET** /products/{id}/images/{image_id}.json | Retrieve a single Product Image.
*JumpsellerApi.ProductImagesApi* | [**productsIdImagesJsonGet**](docs/ProductImagesApi.md#productsIdImagesJsonGet) | **GET** /products/{id}/images.json | Retrieve all Product Images.
*JumpsellerApi.ProductImagesApi* | [**productsIdImagesJsonPost**](docs/ProductImagesApi.md#productsIdImagesJsonPost) | **POST** /products/{id}/images.json | Create a new Product Image.
*JumpsellerApi.ProductOptionValuesApi* | [**productsIdOptionsOptionIdValuesCountJsonGet**](docs/ProductOptionValuesApi.md#productsIdOptionsOptionIdValuesCountJsonGet) | **GET** /products/{id}/options/{option_id}/values/count.json | Count all Product Option Values.
*JumpsellerApi.ProductOptionValuesApi* | [**productsIdOptionsOptionIdValuesJsonGet**](docs/ProductOptionValuesApi.md#productsIdOptionsOptionIdValuesJsonGet) | **GET** /products/{id}/options/{option_id}/values.json | Retrieve all Product Option Values.
*JumpsellerApi.ProductOptionValuesApi* | [**productsIdOptionsOptionIdValuesJsonPost**](docs/ProductOptionValuesApi.md#productsIdOptionsOptionIdValuesJsonPost) | **POST** /products/{id}/options/{option_id}/values.json | Create a new Product Option Value.
*JumpsellerApi.ProductOptionValuesApi* | [**productsIdOptionsOptionIdValuesValueIdJsonDelete**](docs/ProductOptionValuesApi.md#productsIdOptionsOptionIdValuesValueIdJsonDelete) | **DELETE** /products/{id}/options/{option_id}/values/{value_id}.json | Delete a Product Option Value.
*JumpsellerApi.ProductOptionValuesApi* | [**productsIdOptionsOptionIdValuesValueIdJsonGet**](docs/ProductOptionValuesApi.md#productsIdOptionsOptionIdValuesValueIdJsonGet) | **GET** /products/{id}/options/{option_id}/values/{value_id}.json | Retrieve a single Product Option Value.
*JumpsellerApi.ProductOptionValuesApi* | [**productsIdOptionsOptionIdValuesValueIdJsonPut**](docs/ProductOptionValuesApi.md#productsIdOptionsOptionIdValuesValueIdJsonPut) | **PUT** /products/{id}/options/{option_id}/values/{value_id}.json | Modify an existing Product Option Value.
*JumpsellerApi.ProductOptionsApi* | [**productsIdOptionsCountJsonGet**](docs/ProductOptionsApi.md#productsIdOptionsCountJsonGet) | **GET** /products/{id}/options/count.json | Count all Product Options.
*JumpsellerApi.ProductOptionsApi* | [**productsIdOptionsJsonGet**](docs/ProductOptionsApi.md#productsIdOptionsJsonGet) | **GET** /products/{id}/options.json | Retrieve all Product Options.
*JumpsellerApi.ProductOptionsApi* | [**productsIdOptionsJsonPost**](docs/ProductOptionsApi.md#productsIdOptionsJsonPost) | **POST** /products/{id}/options.json | Create a new Product Option.
*JumpsellerApi.ProductOptionsApi* | [**productsIdOptionsOptionIdJsonDelete**](docs/ProductOptionsApi.md#productsIdOptionsOptionIdJsonDelete) | **DELETE** /products/{id}/options/{option_id}.json | Delete a Product Option.
*JumpsellerApi.ProductOptionsApi* | [**productsIdOptionsOptionIdJsonGet**](docs/ProductOptionsApi.md#productsIdOptionsOptionIdJsonGet) | **GET** /products/{id}/options/{option_id}.json | Retrieve a single Product Option.
*JumpsellerApi.ProductOptionsApi* | [**productsIdOptionsOptionIdJsonPut**](docs/ProductOptionsApi.md#productsIdOptionsOptionIdJsonPut) | **PUT** /products/{id}/options/{option_id}.json | Modify an existing Product Option.
*JumpsellerApi.ProductVariantsApi* | [**productsIdVariantsCountJsonGet**](docs/ProductVariantsApi.md#productsIdVariantsCountJsonGet) | **GET** /products/{id}/variants/count.json | Count all Product Variants.
*JumpsellerApi.ProductVariantsApi* | [**productsIdVariantsJsonGet**](docs/ProductVariantsApi.md#productsIdVariantsJsonGet) | **GET** /products/{id}/variants.json | Retrieve all Product Variants.
*JumpsellerApi.ProductVariantsApi* | [**productsIdVariantsJsonPost**](docs/ProductVariantsApi.md#productsIdVariantsJsonPost) | **POST** /products/{id}/variants.json | Create a new Product Variant.
*JumpsellerApi.ProductVariantsApi* | [**productsIdVariantsVariantIdJsonGet**](docs/ProductVariantsApi.md#productsIdVariantsVariantIdJsonGet) | **GET** /products/{id}/variants/{variant_id}.json | Retrieve a single Product Variant.
*JumpsellerApi.ProductVariantsApi* | [**productsIdVariantsVariantIdJsonPut**](docs/ProductVariantsApi.md#productsIdVariantsVariantIdJsonPut) | **PUT** /products/{id}/variants/{variant_id}.json | Modify an existing Product Variant.
*JumpsellerApi.ProductsApi* | [**productsAfterIdJsonGet**](docs/ProductsApi.md#productsAfterIdJsonGet) | **GET** /products/after/{id}.json | Retrieves Products after the given id.
*JumpsellerApi.ProductsApi* | [**productsCategoryCategoryIdCountJsonGet**](docs/ProductsApi.md#productsCategoryCategoryIdCountJsonGet) | **GET** /products/category/{category_id}/count.json | Count Products filtered by category.
*JumpsellerApi.ProductsApi* | [**productsCategoryCategoryIdJsonGet**](docs/ProductsApi.md#productsCategoryCategoryIdJsonGet) | **GET** /products/category/{category_id}.json | Retrieve Products filtered by category.
*JumpsellerApi.ProductsApi* | [**productsCountJsonGet**](docs/ProductsApi.md#productsCountJsonGet) | **GET** /products/count.json | Count all Products.
*JumpsellerApi.ProductsApi* | [**productsIdJsonDelete**](docs/ProductsApi.md#productsIdJsonDelete) | **DELETE** /products/{id}.json | Delete an existing Product.
*JumpsellerApi.ProductsApi* | [**productsIdJsonGet**](docs/ProductsApi.md#productsIdJsonGet) | **GET** /products/{id}.json | Retrieve a single Product.
*JumpsellerApi.ProductsApi* | [**productsIdJsonPut**](docs/ProductsApi.md#productsIdJsonPut) | **PUT** /products/{id}.json | Modify an existing Product.
*JumpsellerApi.ProductsApi* | [**productsJsonGet**](docs/ProductsApi.md#productsJsonGet) | **GET** /products.json | Retrieve all Products.
*JumpsellerApi.ProductsApi* | [**productsJsonPost**](docs/ProductsApi.md#productsJsonPost) | **POST** /products.json | Create a new Product.
*JumpsellerApi.ProductsApi* | [**productsSearchJsonGet**](docs/ProductsApi.md#productsSearchJsonGet) | **GET** /products/search.json | Retrieve a Product List from a query.
*JumpsellerApi.ProductsApi* | [**productsStatusStatusCountJsonGet**](docs/ProductsApi.md#productsStatusStatusCountJsonGet) | **GET** /products/status/{status}/count.json | Count Products filtered by status.
*JumpsellerApi.ProductsApi* | [**productsStatusStatusJsonGet**](docs/ProductsApi.md#productsStatusStatusJsonGet) | **GET** /products/status/{status}.json | Retrieve Products filtered by status.
*JumpsellerApi.PromotionsApi* | [**promotionsIdJsonDelete**](docs/PromotionsApi.md#promotionsIdJsonDelete) | **DELETE** /promotions/{id}.json | Delete an existing Promotion.
*JumpsellerApi.PromotionsApi* | [**promotionsIdJsonGet**](docs/PromotionsApi.md#promotionsIdJsonGet) | **GET** /promotions/{id}.json | Retrieve a single Promotion.
*JumpsellerApi.PromotionsApi* | [**promotionsIdJsonPut**](docs/PromotionsApi.md#promotionsIdJsonPut) | **PUT** /promotions/{id}.json | Update a Promotion.
*JumpsellerApi.PromotionsApi* | [**promotionsJsonGet**](docs/PromotionsApi.md#promotionsJsonGet) | **GET** /promotions.json | Retrieve all Promotions.
*JumpsellerApi.PromotionsApi* | [**promotionsJsonPost**](docs/PromotionsApi.md#promotionsJsonPost) | **POST** /promotions.json | Create a new Promotion.
*JumpsellerApi.RegionsApi* | [**countriesCountryCodeRegionsJsonGet_0**](docs/RegionsApi.md#countriesCountryCodeRegionsJsonGet_0) | **GET** /countries/{country_code}/regions.json | Retrieve all Regions from a single Country.
*JumpsellerApi.RegionsApi* | [**countriesCountryCodeRegionsRegionCodeJsonGet_0**](docs/RegionsApi.md#countriesCountryCodeRegionsRegionCodeJsonGet_0) | **GET** /countries/{country_code}/regions/{region_code}.json | Retrieve a single Region information object.
*JumpsellerApi.ShippingMethodsApi* | [**shippingMethodsIdJsonDelete**](docs/ShippingMethodsApi.md#shippingMethodsIdJsonDelete) | **DELETE** /shipping_methods/{id}.json | Delete an existing Shipping Method.
*JumpsellerApi.ShippingMethodsApi* | [**shippingMethodsIdJsonGet**](docs/ShippingMethodsApi.md#shippingMethodsIdJsonGet) | **GET** /shipping_methods/{id}.json | Retrieve a single Shipping Method.
*JumpsellerApi.ShippingMethodsApi* | [**shippingMethodsIdJsonPut**](docs/ShippingMethodsApi.md#shippingMethodsIdJsonPut) | **PUT** /shipping_methods/{id}.json | Update a Shipping Method.
*JumpsellerApi.ShippingMethodsApi* | [**shippingMethodsJsonGet**](docs/ShippingMethodsApi.md#shippingMethodsJsonGet) | **GET** /shipping_methods.json | Retrieve all Store&#39;s Shipping Methods.
*JumpsellerApi.ShippingMethodsApi* | [**shippingMethodsJsonPost**](docs/ShippingMethodsApi.md#shippingMethodsJsonPost) | **POST** /shipping_methods.json | Creates a Shipping Method.
*JumpsellerApi.StoresApi* | [**storeInfoJsonGet**](docs/StoresApi.md#storeInfoJsonGet) | **GET** /store/info.json | Retrieve Store Information.
*JumpsellerApi.StoresApi* | [**storeLanguagesJsonGet**](docs/StoresApi.md#storeLanguagesJsonGet) | **GET** /store/languages.json | Retrieve Store Languages.
*JumpsellerApi.TaxesApi* | [**taxesIdJsonGet**](docs/TaxesApi.md#taxesIdJsonGet) | **GET** /taxes/{id}.json | Retrieve a single Tax information.
*JumpsellerApi.TaxesApi* | [**taxesJsonGet**](docs/TaxesApi.md#taxesJsonGet) | **GET** /taxes.json | Retrieve all Taxes.
*JumpsellerApi.TaxesApi* | [**taxesJsonPost**](docs/TaxesApi.md#taxesJsonPost) | **POST** /taxes.json | Create a new Tax.


## Documentation for Models

 - [JumpsellerApi.AddProductCustomField](docs/AddProductCustomField.md)
 - [JumpsellerApi.AddProductCustomFieldFields](docs/AddProductCustomFieldFields.md)
 - [JumpsellerApi.App](docs/App.md)
 - [JumpsellerApi.AppFields](docs/AppFields.md)
 - [JumpsellerApi.Attachment](docs/Attachment.md)
 - [JumpsellerApi.AttachmentEdit](docs/AttachmentEdit.md)
 - [JumpsellerApi.AttachmentEditFields](docs/AttachmentEditFields.md)
 - [JumpsellerApi.AttachmentFields](docs/AttachmentFields.md)
 - [JumpsellerApi.BadParams](docs/BadParams.md)
 - [JumpsellerApi.BestSold](docs/BestSold.md)
 - [JumpsellerApi.BillingAddress](docs/BillingAddress.md)
 - [JumpsellerApi.Category](docs/Category.md)
 - [JumpsellerApi.CategoryEdit](docs/CategoryEdit.md)
 - [JumpsellerApi.CategoryEditFields](docs/CategoryEditFields.md)
 - [JumpsellerApi.CategoryFields](docs/CategoryFields.md)
 - [JumpsellerApi.CheckoutCustomField](docs/CheckoutCustomField.md)
 - [JumpsellerApi.CheckoutCustomFieldEdit](docs/CheckoutCustomFieldEdit.md)
 - [JumpsellerApi.CheckoutCustomFieldEditFields](docs/CheckoutCustomFieldEditFields.md)
 - [JumpsellerApi.CheckoutCustomFieldFields](docs/CheckoutCustomFieldFields.md)
 - [JumpsellerApi.Count](docs/Count.md)
 - [JumpsellerApi.Country](docs/Country.md)
 - [JumpsellerApi.CountryOrders](docs/CountryOrders.md)
 - [JumpsellerApi.CustomField](docs/CustomField.md)
 - [JumpsellerApi.CustomFieldEdit](docs/CustomFieldEdit.md)
 - [JumpsellerApi.CustomFieldEditFields](docs/CustomFieldEditFields.md)
 - [JumpsellerApi.CustomFieldFields](docs/CustomFieldFields.md)
 - [JumpsellerApi.CustomFieldSelectOption](docs/CustomFieldSelectOption.md)
 - [JumpsellerApi.CustomFieldSelectOptionEdit](docs/CustomFieldSelectOptionEdit.md)
 - [JumpsellerApi.CustomFieldSelectOptionEditFields](docs/CustomFieldSelectOptionEditFields.md)
 - [JumpsellerApi.CustomFieldSelectOptionFields](docs/CustomFieldSelectOptionFields.md)
 - [JumpsellerApi.Customer](docs/Customer.md)
 - [JumpsellerApi.CustomerAdditionalField](docs/CustomerAdditionalField.md)
 - [JumpsellerApi.CustomerAdditionalFieldEdit](docs/CustomerAdditionalFieldEdit.md)
 - [JumpsellerApi.CustomerAdditionalFieldEditFields](docs/CustomerAdditionalFieldEditFields.md)
 - [JumpsellerApi.CustomerAdditionalFieldFields](docs/CustomerAdditionalFieldFields.md)
 - [JumpsellerApi.CustomerCategory](docs/CustomerCategory.md)
 - [JumpsellerApi.CustomerCategoryEdit](docs/CustomerCategoryEdit.md)
 - [JumpsellerApi.CustomerCategoryEditFields](docs/CustomerCategoryEditFields.md)
 - [JumpsellerApi.CustomerCategoryFields](docs/CustomerCategoryFields.md)
 - [JumpsellerApi.CustomerFields](docs/CustomerFields.md)
 - [JumpsellerApi.CustomerFieldsWithBillingAddressAndShippingAddressFields](docs/CustomerFieldsWithBillingAddressAndShippingAddressFields.md)
 - [JumpsellerApi.CustomerFieldsWithPassword](docs/CustomerFieldsWithPassword.md)
 - [JumpsellerApi.CustomerFieldsWithPasswordNoID](docs/CustomerFieldsWithPasswordNoID.md)
 - [JumpsellerApi.CustomerToCustomerCategory](docs/CustomerToCustomerCategory.md)
 - [JumpsellerApi.CustomerWithPassword](docs/CustomerWithPassword.md)
 - [JumpsellerApi.CustomerWithPasswordNoID](docs/CustomerWithPasswordNoID.md)
 - [JumpsellerApi.CustomersToCustomerCategory](docs/CustomersToCustomerCategory.md)
 - [JumpsellerApi.DailyVisits](docs/DailyVisits.md)
 - [JumpsellerApi.DigitalProduct](docs/DigitalProduct.md)
 - [JumpsellerApi.DigitalProductEdit](docs/DigitalProductEdit.md)
 - [JumpsellerApi.DigitalProductEditFields](docs/DigitalProductEditFields.md)
 - [JumpsellerApi.DigitalProductFields](docs/DigitalProductFields.md)
 - [JumpsellerApi.Fulfillment](docs/Fulfillment.md)
 - [JumpsellerApi.FulfillmentCreate](docs/FulfillmentCreate.md)
 - [JumpsellerApi.FulfillmentCreateFields](docs/FulfillmentCreateFields.md)
 - [JumpsellerApi.FulfillmentEdit](docs/FulfillmentEdit.md)
 - [JumpsellerApi.FulfillmentEditFields](docs/FulfillmentEditFields.md)
 - [JumpsellerApi.FulfillmentFields](docs/FulfillmentFields.md)
 - [JumpsellerApi.Hook](docs/Hook.md)
 - [JumpsellerApi.HookEdit](docs/HookEdit.md)
 - [JumpsellerApi.HookEditFields](docs/HookEditFields.md)
 - [JumpsellerApi.HookFields](docs/HookFields.md)
 - [JumpsellerApi.Id](docs/Id.md)
 - [JumpsellerApi.Image](docs/Image.md)
 - [JumpsellerApi.ImageEdit](docs/ImageEdit.md)
 - [JumpsellerApi.ImageEditFields](docs/ImageEditFields.md)
 - [JumpsellerApi.ImageFields](docs/ImageFields.md)
 - [JumpsellerApi.JSApp](docs/JSApp.md)
 - [JumpsellerApi.JSAppEdit](docs/JSAppEdit.md)
 - [JumpsellerApi.Language](docs/Language.md)
 - [JumpsellerApi.MessageObject](docs/MessageObject.md)
 - [JumpsellerApi.NewPartnerStore](docs/NewPartnerStore.md)
 - [JumpsellerApi.NewPartnerStoreStore](docs/NewPartnerStoreStore.md)
 - [JumpsellerApi.NewVsReturning](docs/NewVsReturning.md)
 - [JumpsellerApi.NotFound](docs/NotFound.md)
 - [JumpsellerApi.Order](docs/Order.md)
 - [JumpsellerApi.OrderAdditionalFields](docs/OrderAdditionalFields.md)
 - [JumpsellerApi.OrderBillingAddress](docs/OrderBillingAddress.md)
 - [JumpsellerApi.OrderCreate](docs/OrderCreate.md)
 - [JumpsellerApi.OrderCreateFields](docs/OrderCreateFields.md)
 - [JumpsellerApi.OrderEdit](docs/OrderEdit.md)
 - [JumpsellerApi.OrderEditFields](docs/OrderEditFields.md)
 - [JumpsellerApi.OrderFields](docs/OrderFields.md)
 - [JumpsellerApi.OrderHistory](docs/OrderHistory.md)
 - [JumpsellerApi.OrderHistoryEdit](docs/OrderHistoryEdit.md)
 - [JumpsellerApi.OrderHistoryEditFields](docs/OrderHistoryEditFields.md)
 - [JumpsellerApi.OrderHistoryFields](docs/OrderHistoryFields.md)
 - [JumpsellerApi.OrderProduct](docs/OrderProduct.md)
 - [JumpsellerApi.OrderProductOrderCreate](docs/OrderProductOrderCreate.md)
 - [JumpsellerApi.OrderProductTax](docs/OrderProductTax.md)
 - [JumpsellerApi.OrderShippingAddress](docs/OrderShippingAddress.md)
 - [JumpsellerApi.OrderShippingTax](docs/OrderShippingTax.md)
 - [JumpsellerApi.OrdersData](docs/OrdersData.md)
 - [JumpsellerApi.Page](docs/Page.md)
 - [JumpsellerApi.PageCategory](docs/PageCategory.md)
 - [JumpsellerApi.PageFields](docs/PageFields.md)
 - [JumpsellerApi.PageFieldsImage](docs/PageFieldsImage.md)
 - [JumpsellerApi.PageModify](docs/PageModify.md)
 - [JumpsellerApi.PageModifyFields](docs/PageModifyFields.md)
 - [JumpsellerApi.PageTemplate](docs/PageTemplate.md)
 - [JumpsellerApi.PartnerError](docs/PartnerError.md)
 - [JumpsellerApi.PartnerStoreCode](docs/PartnerStoreCode.md)
 - [JumpsellerApi.PartnerStoreCodeStore](docs/PartnerStoreCodeStore.md)
 - [JumpsellerApi.PartnerStoreCreate](docs/PartnerStoreCreate.md)
 - [JumpsellerApi.PartnerStoreStatus](docs/PartnerStoreStatus.md)
 - [JumpsellerApi.PartnerStoreStatusStatus](docs/PartnerStoreStatusStatus.md)
 - [JumpsellerApi.PaymentMethod](docs/PaymentMethod.md)
 - [JumpsellerApi.PaymentMethodFields](docs/PaymentMethodFields.md)
 - [JumpsellerApi.PaymentMethodFreq](docs/PaymentMethodFreq.md)
 - [JumpsellerApi.Product](docs/Product.md)
 - [JumpsellerApi.ProductCustomField](docs/ProductCustomField.md)
 - [JumpsellerApi.ProductCustomFieldFields](docs/ProductCustomFieldFields.md)
 - [JumpsellerApi.ProductEdit](docs/ProductEdit.md)
 - [JumpsellerApi.ProductEditFields](docs/ProductEditFields.md)
 - [JumpsellerApi.ProductFields](docs/ProductFields.md)
 - [JumpsellerApi.ProductOption](docs/ProductOption.md)
 - [JumpsellerApi.ProductOptionEdit](docs/ProductOptionEdit.md)
 - [JumpsellerApi.ProductOptionEditFields](docs/ProductOptionEditFields.md)
 - [JumpsellerApi.ProductOptionFields](docs/ProductOptionFields.md)
 - [JumpsellerApi.ProductOptionValue](docs/ProductOptionValue.md)
 - [JumpsellerApi.ProductOptionValueEdit](docs/ProductOptionValueEdit.md)
 - [JumpsellerApi.ProductOptionValueEditFields](docs/ProductOptionValueEditFields.md)
 - [JumpsellerApi.ProductOptionValueFields](docs/ProductOptionValueFields.md)
 - [JumpsellerApi.ProductOptionVariantEdit](docs/ProductOptionVariantEdit.md)
 - [JumpsellerApi.Promotion](docs/Promotion.md)
 - [JumpsellerApi.PromotionEdit](docs/PromotionEdit.md)
 - [JumpsellerApi.PromotionEditFields](docs/PromotionEditFields.md)
 - [JumpsellerApi.PromotionFields](docs/PromotionFields.md)
 - [JumpsellerApi.Referrer](docs/Referrer.md)
 - [JumpsellerApi.Region](docs/Region.md)
 - [JumpsellerApi.RegionOrders](docs/RegionOrders.md)
 - [JumpsellerApi.ShippingAddress](docs/ShippingAddress.md)
 - [JumpsellerApi.ShippingMethod](docs/ShippingMethod.md)
 - [JumpsellerApi.ShippingMethodEdit](docs/ShippingMethodEdit.md)
 - [JumpsellerApi.ShippingMethodEditShippingMethod](docs/ShippingMethodEditShippingMethod.md)
 - [JumpsellerApi.ShippingMethodFields](docs/ShippingMethodFields.md)
 - [JumpsellerApi.ShippingMethodFreq](docs/ShippingMethodFreq.md)
 - [JumpsellerApi.ShippingService](docs/ShippingService.md)
 - [JumpsellerApi.StatusInvalid](docs/StatusInvalid.md)
 - [JumpsellerApi.Store](docs/Store.md)
 - [JumpsellerApi.StoreAddress](docs/StoreAddress.md)
 - [JumpsellerApi.StoreCheckStatusJsonGet200Response](docs/StoreCheckStatusJsonGet200Response.md)
 - [JumpsellerApi.StoreStats](docs/StoreStats.md)
 - [JumpsellerApi.StoreStatsConversions](docs/StoreStatsConversions.md)
 - [JumpsellerApi.StoreStatsNewVsReturningCustomers](docs/StoreStatsNewVsReturningCustomers.md)
 - [JumpsellerApi.StoreStatsOrders](docs/StoreStatsOrders.md)
 - [JumpsellerApi.StoreStatsRegionOrders](docs/StoreStatsRegionOrders.md)
 - [JumpsellerApi.Tax](docs/Tax.md)
 - [JumpsellerApi.TaxEdit](docs/TaxEdit.md)
 - [JumpsellerApi.TaxEditFields](docs/TaxEditFields.md)
 - [JumpsellerApi.TaxFields](docs/TaxFields.md)
 - [JumpsellerApi.TrafficSource](docs/TrafficSource.md)
 - [JumpsellerApi.TrafficType](docs/TrafficType.md)
 - [JumpsellerApi.Type](docs/Type.md)
 - [JumpsellerApi.Variant](docs/Variant.md)
 - [JumpsellerApi.VariantEdit](docs/VariantEdit.md)
 - [JumpsellerApi.VariantEditFields](docs/VariantEditFields.md)
 - [JumpsellerApi.VariantFields](docs/VariantFields.md)


## Documentation for Authorization

Endpoints do not require authorization.

