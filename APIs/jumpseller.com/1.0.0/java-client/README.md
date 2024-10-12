# openapi-java-client

Jumpseller API
- API version: 1.0.0
  - Build date: 2024-10-12T12:31:37.537066-04:00[America/New_York]
  - Generator version: 7.9.0

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



*Automatically generated by the [OpenAPI Generator](https://openapi-generator.tech)*


## Requirements

Building the API client library requires:
1. Java 1.8+
2. Maven (3.8.3+)/Gradle (7.2+)

## Installation

To install the API client library to your local Maven repository, simply execute:

```shell
mvn clean install
```

To deploy it to a remote Maven repository instead, configure the settings of the repository and execute:

```shell
mvn clean deploy
```

Refer to the [OSSRH Guide](http://central.sonatype.org/pages/ossrh-guide.html) for more information.

### Maven users

Add this dependency to your project's POM:

```xml
<dependency>
  <groupId>org.openapitools</groupId>
  <artifactId>openapi-java-client</artifactId>
  <version>1.0.0</version>
  <scope>compile</scope>
</dependency>
```

### Gradle users

Add this dependency to your project's build file:

```groovy
  repositories {
    mavenCentral()     // Needed if the 'openapi-java-client' jar has been published to maven central.
    mavenLocal()       // Needed if the 'openapi-java-client' jar has been published to the local maven repo.
  }

  dependencies {
     implementation "org.openapitools:openapi-java-client:1.0.0"
  }
```

### Others

At first generate the JAR by executing:

```shell
mvn clean package
```

Then manually install the following JARs:

* `target/openapi-java-client-1.0.0.jar`
* `target/lib/*.jar`

## Getting Started

Please follow the [installation](#installation) instruction and execute the following Java code:

```java

// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.model.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    String code = "code_example"; // String | Code of the App
    try {
      String result = apiInstance.jsappsCodeJsonDelete(login, authtoken, code);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#jsappsCodeJsonDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

## Documentation for API Endpoints

All URIs are relative to *https://api.jumpseller.com/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AppsApi* | [**jsappsCodeJsonDelete**](docs/AppsApi.md#jsappsCodeJsonDelete) | **DELETE** /jsapps/{code}.json | Delete an existing JSApp.
*AppsApi* | [**jsappsCodeJsonGet**](docs/AppsApi.md#jsappsCodeJsonGet) | **GET** /jsapps/{code}.json | Retrieve a JSApp.
*AppsApi* | [**jsappsJsonGet**](docs/AppsApi.md#jsappsJsonGet) | **GET** /jsapps.json | Retrieve all the Store&#39;s JSApps.
*AppsApi* | [**jsappsJsonPost**](docs/AppsApi.md#jsappsJsonPost) | **POST** /jsapps.json | Create a Store JSApp.
*CategoriesApi* | [**categoriesCountJsonGet**](docs/CategoriesApi.md#categoriesCountJsonGet) | **GET** /categories/count.json | Count all Categories.
*CategoriesApi* | [**categoriesIdJsonDelete**](docs/CategoriesApi.md#categoriesIdJsonDelete) | **DELETE** /categories/{id}.json | Delete an existing Category.
*CategoriesApi* | [**categoriesIdJsonGet**](docs/CategoriesApi.md#categoriesIdJsonGet) | **GET** /categories/{id}.json | Retrieve a single Category.
*CategoriesApi* | [**categoriesIdJsonPut**](docs/CategoriesApi.md#categoriesIdJsonPut) | **PUT** /categories/{id}.json | Modify an existing Category.
*CategoriesApi* | [**categoriesJsonGet**](docs/CategoriesApi.md#categoriesJsonGet) | **GET** /categories.json | Retrieve all Categories.
*CategoriesApi* | [**categoriesJsonPost**](docs/CategoriesApi.md#categoriesJsonPost) | **POST** /categories.json | Create a new Category.
*CheckoutCustomFieldsApi* | [**checkoutCustomFieldsIdJsonDelete**](docs/CheckoutCustomFieldsApi.md#checkoutCustomFieldsIdJsonDelete) | **DELETE** /checkout_custom_fields/{id}.json | Delete an existing CheckoutCustomField.
*CheckoutCustomFieldsApi* | [**checkoutCustomFieldsIdJsonGet**](docs/CheckoutCustomFieldsApi.md#checkoutCustomFieldsIdJsonGet) | **GET** /checkout_custom_fields/{id}.json | Retrieve a single CheckoutCustomField.
*CheckoutCustomFieldsApi* | [**checkoutCustomFieldsIdJsonPut**](docs/CheckoutCustomFieldsApi.md#checkoutCustomFieldsIdJsonPut) | **PUT** /checkout_custom_fields/{id}.json | Update a CheckoutCustomField.
*CheckoutCustomFieldsApi* | [**checkoutCustomFieldsJsonGet**](docs/CheckoutCustomFieldsApi.md#checkoutCustomFieldsJsonGet) | **GET** /checkout_custom_fields.json | Retrieve all Checkout Custom Fields.
*CheckoutCustomFieldsApi* | [**checkoutCustomFieldsJsonPost**](docs/CheckoutCustomFieldsApi.md#checkoutCustomFieldsJsonPost) | **POST** /checkout_custom_fields.json | Create a new CheckoutCustomField.
*CountriesApi* | [**countriesCountryCodeJsonGet**](docs/CountriesApi.md#countriesCountryCodeJsonGet) | **GET** /countries/{country_code}.json | Retrieve a single Country information.
*CountriesApi* | [**countriesCountryCodeRegionsJsonGet**](docs/CountriesApi.md#countriesCountryCodeRegionsJsonGet) | **GET** /countries/{country_code}/regions.json | Retrieve all Regions from a single Country.
*CountriesApi* | [**countriesCountryCodeRegionsRegionCodeJsonGet**](docs/CountriesApi.md#countriesCountryCodeRegionsRegionCodeJsonGet) | **GET** /countries/{country_code}/regions/{region_code}.json | Retrieve a single Region information object.
*CountriesApi* | [**countriesJsonGet**](docs/CountriesApi.md#countriesJsonGet) | **GET** /countries.json | Retrieve all Countries.
*CustomFieldSelectOptionsApi* | [**customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonGet**](docs/CustomFieldSelectOptionsApi.md#customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonGet) | **GET** /custom_fields/{id}/select_options/{custom_field_select_option_id}.json | Retrieve a single SelectOption from a CustomField.
*CustomFieldSelectOptionsApi* | [**customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonPut**](docs/CustomFieldSelectOptionsApi.md#customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonPut) | **PUT** /custom_fields/{id}/select_options/{custom_field_select_option_id}.json | Update a SelectOption from a CustomField.
*CustomFieldSelectOptionsApi* | [**customFieldsIdSelectOptionsJsonGet**](docs/CustomFieldSelectOptionsApi.md#customFieldsIdSelectOptionsJsonGet) | **GET** /custom_fields/{id}/select_options.json | Retrieve all Store&#39;s Custom Fields.
*CustomFieldSelectOptionsApi* | [**customFieldsIdSelectOptionsJsonPost**](docs/CustomFieldSelectOptionsApi.md#customFieldsIdSelectOptionsJsonPost) | **POST** /custom_fields/{id}/select_options.json | Create a new Custom Field Select Option.
*CustomFieldsApi* | [**customFieldsIdJsonDelete**](docs/CustomFieldsApi.md#customFieldsIdJsonDelete) | **DELETE** /custom_fields/{id}.json | Delete an existing CustomField.
*CustomFieldsApi* | [**customFieldsIdJsonGet**](docs/CustomFieldsApi.md#customFieldsIdJsonGet) | **GET** /custom_fields/{id}.json | Retrieve a single CustomField.
*CustomFieldsApi* | [**customFieldsIdJsonPut**](docs/CustomFieldsApi.md#customFieldsIdJsonPut) | **PUT** /custom_fields/{id}.json | Update a CustomField.
*CustomFieldsApi* | [**customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonDelete**](docs/CustomFieldsApi.md#customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonDelete) | **DELETE** /custom_fields/{id}/select_options/{custom_field_select_option_id}.json | Delete an existing CustomFieldSelectOption.
*CustomFieldsApi* | [**customFieldsJsonGet**](docs/CustomFieldsApi.md#customFieldsJsonGet) | **GET** /custom_fields.json | Retrieve all Store&#39;s Custom Fields.
*CustomFieldsApi* | [**customFieldsJsonPost**](docs/CustomFieldsApi.md#customFieldsJsonPost) | **POST** /custom_fields.json | Create a new Custom Field.
*CustomerAdditionalFieldsApi* | [**customersIdFieldsFieldIdDelete**](docs/CustomerAdditionalFieldsApi.md#customersIdFieldsFieldIdDelete) | **DELETE** /customers/{id}/fields/{field_id} | Delete a Customer Additional Field.
*CustomerAdditionalFieldsApi* | [**customersIdFieldsFieldIdGet**](docs/CustomerAdditionalFieldsApi.md#customersIdFieldsFieldIdGet) | **GET** /customers/{id}/fields/{field_id} | Retrieve a single Customer Additional Field.
*CustomerAdditionalFieldsApi* | [**customersIdFieldsFieldIdPut**](docs/CustomerAdditionalFieldsApi.md#customersIdFieldsFieldIdPut) | **PUT** /customers/{id}/fields/{field_id} | Update a Customer Additional Field.
*CustomerAdditionalFieldsApi* | [**customersIdFieldsGet**](docs/CustomerAdditionalFieldsApi.md#customersIdFieldsGet) | **GET** /customers/{id}/fields | Retrieves the Customer Additional Field of a Customer.
*CustomerAdditionalFieldsApi* | [**customersIdFieldsPost**](docs/CustomerAdditionalFieldsApi.md#customersIdFieldsPost) | **POST** /customers/{id}/fields | Adds Customer Additional Fields to a Customer.
*CustomerCategoriesApi* | [**customerCategoriesIdCustomersJsonDelete**](docs/CustomerCategoriesApi.md#customerCategoriesIdCustomersJsonDelete) | **DELETE** /customer_categories/{id}/customers.json | Delete Customers from an existing CustomerCategory.
*CustomerCategoriesApi* | [**customerCategoriesIdCustomersJsonGet**](docs/CustomerCategoriesApi.md#customerCategoriesIdCustomersJsonGet) | **GET** /customer_categories/{id}/customers.json | Retrieves the customers in a CustomerCategory.
*CustomerCategoriesApi* | [**customerCategoriesIdCustomersJsonPost**](docs/CustomerCategoriesApi.md#customerCategoriesIdCustomersJsonPost) | **POST** /customer_categories/{id}/customers.json | Adds Customers to a CustomerCategory.
*CustomerCategoriesApi* | [**customerCategoriesIdJsonDelete**](docs/CustomerCategoriesApi.md#customerCategoriesIdJsonDelete) | **DELETE** /customer_categories/{id}.json | Delete an existing CustomerCategory.
*CustomerCategoriesApi* | [**customerCategoriesIdJsonGet**](docs/CustomerCategoriesApi.md#customerCategoriesIdJsonGet) | **GET** /customer_categories/{id}.json | Retrieve a single CustomerCategory.
*CustomerCategoriesApi* | [**customerCategoriesIdJsonPut**](docs/CustomerCategoriesApi.md#customerCategoriesIdJsonPut) | **PUT** /customer_categories/{id}.json | Update a CustomerCategory.
*CustomerCategoriesApi* | [**customerCategoriesJsonGet**](docs/CustomerCategoriesApi.md#customerCategoriesJsonGet) | **GET** /customer_categories.json | Retrieve all Customer Categories.
*CustomerCategoriesApi* | [**customerCategoriesJsonPost**](docs/CustomerCategoriesApi.md#customerCategoriesJsonPost) | **POST** /customer_categories.json | Create a new CustomerCategory.
*CustomersApi* | [**customersCountJsonGet**](docs/CustomersApi.md#customersCountJsonGet) | **GET** /customers/count.json | Count all Customers.
*CustomersApi* | [**customersEmailEmailJsonGet**](docs/CustomersApi.md#customersEmailEmailJsonGet) | **GET** /customers/email/{email}.json | Retrieve a single Customer by email.
*CustomersApi* | [**customersIdJsonDelete**](docs/CustomersApi.md#customersIdJsonDelete) | **DELETE** /customers/{id}.json | Delete an existing Customer.
*CustomersApi* | [**customersIdJsonGet**](docs/CustomersApi.md#customersIdJsonGet) | **GET** /customers/{id}.json | Retrieve a single Customer by id.
*CustomersApi* | [**customersIdJsonPut**](docs/CustomersApi.md#customersIdJsonPut) | **PUT** /customers/{id}.json | Update a new Customer.
*CustomersApi* | [**customersJsonGet**](docs/CustomersApi.md#customersJsonGet) | **GET** /customers.json | Retrieve all Customers.
*CustomersApi* | [**customersJsonPost**](docs/CustomersApi.md#customersJsonPost) | **POST** /customers.json | Create a new Customer.
*FulfillmentsApi* | [**fulfillmentsCountJsonGet**](docs/FulfillmentsApi.md#fulfillmentsCountJsonGet) | **GET** /fulfillments/count.json | Count all Fulfillments.
*FulfillmentsApi* | [**fulfillmentsIdJsonGet**](docs/FulfillmentsApi.md#fulfillmentsIdJsonGet) | **GET** /fulfillments/{id}.json | Retrieve a single Fulfillment.
*FulfillmentsApi* | [**fulfillmentsJsonGet**](docs/FulfillmentsApi.md#fulfillmentsJsonGet) | **GET** /fulfillments.json | Retrieve all Fulfillments.
*FulfillmentsApi* | [**orderIdFulfillmentsJsonGet**](docs/FulfillmentsApi.md#orderIdFulfillmentsJsonGet) | **GET** /order/{id}/fulfillments.json | Retrieve the Fulfillments associated with the Order.
*HooksApi* | [**hooksIdJsonDelete**](docs/HooksApi.md#hooksIdJsonDelete) | **DELETE** /hooks/{id}.json | Delete an existing Hook.
*HooksApi* | [**hooksIdJsonGet**](docs/HooksApi.md#hooksIdJsonGet) | **GET** /hooks/{id}.json | Retrieve a single Hook.
*HooksApi* | [**hooksIdJsonPut**](docs/HooksApi.md#hooksIdJsonPut) | **PUT** /hooks/{id}.json | Update a Hook.
*HooksApi* | [**hooksJsonGet**](docs/HooksApi.md#hooksJsonGet) | **GET** /hooks.json | Retrieve all Hooks.
*HooksApi* | [**hooksJsonPost**](docs/HooksApi.md#hooksJsonPost) | **POST** /hooks.json | Create a new Hook.
*OrdersApi* | [**ordersAfterIdJsonGet**](docs/OrdersApi.md#ordersAfterIdJsonGet) | **GET** /orders/after/{id}.json | Retrieve orders filtered by Order Id.
*OrdersApi* | [**ordersCountJsonGet**](docs/OrdersApi.md#ordersCountJsonGet) | **GET** /orders/count.json | Count all Orders.
*OrdersApi* | [**ordersIdHistoryJsonGet**](docs/OrdersApi.md#ordersIdHistoryJsonGet) | **GET** /orders/{id}/history.json | Retrieve all Order History.
*OrdersApi* | [**ordersIdHistoryJsonPost**](docs/OrdersApi.md#ordersIdHistoryJsonPost) | **POST** /orders/{id}/history.json | Create a new Order History Entry.
*OrdersApi* | [**ordersIdJsonGet**](docs/OrdersApi.md#ordersIdJsonGet) | **GET** /orders/{id}.json | Retrieve a single Order.
*OrdersApi* | [**ordersIdJsonPut**](docs/OrdersApi.md#ordersIdJsonPut) | **PUT** /orders/{id}.json | Modify an existing Order.
*OrdersApi* | [**ordersJsonGet**](docs/OrdersApi.md#ordersJsonGet) | **GET** /orders.json | Retrieve all Orders.
*OrdersApi* | [**ordersJsonPost**](docs/OrdersApi.md#ordersJsonPost) | **POST** /orders.json | Create a new Order.
*OrdersApi* | [**ordersStatusStatusJsonGet**](docs/OrdersApi.md#ordersStatusStatusJsonGet) | **GET** /orders/status/{status}.json | Retrieve orders filtered by status.
*PagesApi* | [**pagesCountJsonGet**](docs/PagesApi.md#pagesCountJsonGet) | **GET** /pages/count.json | Count all Pages.
*PagesApi* | [**pagesIdJsonDelete**](docs/PagesApi.md#pagesIdJsonDelete) | **DELETE** /pages/{id}.json | Delete an existing Page.
*PagesApi* | [**pagesIdJsonGet**](docs/PagesApi.md#pagesIdJsonGet) | **GET** /pages/{id}.json | Retrieve a single Page by id.
*PagesApi* | [**pagesIdJsonPut**](docs/PagesApi.md#pagesIdJsonPut) | **PUT** /pages/{id}.json | Update a Page.
*PagesApi* | [**pagesJsonGet**](docs/PagesApi.md#pagesJsonGet) | **GET** /pages.json | Retrieve all Pages.
*PagesApi* | [**pagesJsonPost**](docs/PagesApi.md#pagesJsonPost) | **POST** /pages.json | Create a new Page.
*PartnersApi* | [**partnersStoresJsonGet**](docs/PartnersApi.md#partnersStoresJsonGet) | **GET** /partners/stores.json | Retrieve statistics.
*PartnersApi* | [**storeCheckStatusJsonGet**](docs/PartnersApi.md#storeCheckStatusJsonGet) | **GET** /store/check_status.json | Retrive store creation status.
*PartnersApi* | [**storeCreateJsonPost**](docs/PartnersApi.md#storeCreateJsonPost) | **POST** /store/create.json | Create a Partnered Store
*PaymentMethodsApi* | [**paymentMethodsIdJsonGet**](docs/PaymentMethodsApi.md#paymentMethodsIdJsonGet) | **GET** /payment_methods/{id}.json | Retrieve a single Payment Method.
*PaymentMethodsApi* | [**paymentMethodsJsonGet**](docs/PaymentMethodsApi.md#paymentMethodsJsonGet) | **GET** /payment_methods.json | Retrieve all Store&#39;s Payment Methods.
*ProductAttachmentsApi* | [**productsIdAttachmentsAttachmentIdJsonDelete**](docs/ProductAttachmentsApi.md#productsIdAttachmentsAttachmentIdJsonDelete) | **DELETE** /products/{id}/attachments/{attachment_id}.json | Delete a Product Attachment.
*ProductAttachmentsApi* | [**productsIdAttachmentsAttachmentIdJsonGet**](docs/ProductAttachmentsApi.md#productsIdAttachmentsAttachmentIdJsonGet) | **GET** /products/{id}/attachments/{attachment_id}.json | Retrieve a single Product Attachment.
*ProductAttachmentsApi* | [**productsIdAttachmentsCountJsonGet**](docs/ProductAttachmentsApi.md#productsIdAttachmentsCountJsonGet) | **GET** /products/{id}/attachments/count.json | Count all Product Attachments.
*ProductAttachmentsApi* | [**productsIdAttachmentsJsonGet**](docs/ProductAttachmentsApi.md#productsIdAttachmentsJsonGet) | **GET** /products/{id}/attachments.json | Retrieve all Product Attachments.
*ProductAttachmentsApi* | [**productsIdAttachmentsJsonPost**](docs/ProductAttachmentsApi.md#productsIdAttachmentsJsonPost) | **POST** /products/{id}/attachments.json | Create a new Product Attachment.
*ProductCustomFieldsApi* | [**productsIdFieldsCountJsonGet**](docs/ProductCustomFieldsApi.md#productsIdFieldsCountJsonGet) | **GET** /products/{id}/fields/count.json | Count all Product Custom Fields.
*ProductCustomFieldsApi* | [**productsIdFieldsJsonGet**](docs/ProductCustomFieldsApi.md#productsIdFieldsJsonGet) | **GET** /products/{id}/fields.json | Retrieve all Product Custom Fields
*ProductCustomFieldsApi* | [**productsIdFieldsJsonPost**](docs/ProductCustomFieldsApi.md#productsIdFieldsJsonPost) | **POST** /products/{id}/fields.json | Add an existing Custom Field to a Product.
*ProductCustomFieldsApi* | [**productsProductIdFieldsFieldIdJsonDelete**](docs/ProductCustomFieldsApi.md#productsProductIdFieldsFieldIdJsonDelete) | **DELETE** /products/{product_id}/fields/{field_id}.json | Delete value of Product Custom Field
*ProductCustomFieldsApi* | [**productsProductIdFieldsFieldIdJsonPut**](docs/ProductCustomFieldsApi.md#productsProductIdFieldsFieldIdJsonPut) | **PUT** /products/{product_id}/fields/{field_id}.json | Update value of Product Custom Field
*ProductDigitalProductsApi* | [**productsIdDigitalProductsCountJsonGet**](docs/ProductDigitalProductsApi.md#productsIdDigitalProductsCountJsonGet) | **GET** /products/{id}/digital_products/count.json | Count all Product DigitalProducts.
*ProductDigitalProductsApi* | [**productsIdDigitalProductsDigitalProductIdJsonDelete**](docs/ProductDigitalProductsApi.md#productsIdDigitalProductsDigitalProductIdJsonDelete) | **DELETE** /products/{id}/digital_products/{digital_product_id}.json | Delete a Product DigitalProduct.
*ProductDigitalProductsApi* | [**productsIdDigitalProductsDigitalProductIdJsonGet**](docs/ProductDigitalProductsApi.md#productsIdDigitalProductsDigitalProductIdJsonGet) | **GET** /products/{id}/digital_products/{digital_product_id}.json | Retrieve a single Product DigitalProduct.
*ProductDigitalProductsApi* | [**productsIdDigitalProductsJsonGet**](docs/ProductDigitalProductsApi.md#productsIdDigitalProductsJsonGet) | **GET** /products/{id}/digital_products.json | Retrieve all Product DigitalProducts.
*ProductDigitalProductsApi* | [**productsIdDigitalProductsJsonPost**](docs/ProductDigitalProductsApi.md#productsIdDigitalProductsJsonPost) | **POST** /products/{id}/digital_products.json | Create a new Product DigitalProduct.
*ProductImagesApi* | [**productsIdImagesCountJsonGet**](docs/ProductImagesApi.md#productsIdImagesCountJsonGet) | **GET** /products/{id}/images/count.json | Count all Product Images.
*ProductImagesApi* | [**productsIdImagesImageIdJsonDelete**](docs/ProductImagesApi.md#productsIdImagesImageIdJsonDelete) | **DELETE** /products/{id}/images/{image_id}.json | Delete a Product Image.
*ProductImagesApi* | [**productsIdImagesImageIdJsonGet**](docs/ProductImagesApi.md#productsIdImagesImageIdJsonGet) | **GET** /products/{id}/images/{image_id}.json | Retrieve a single Product Image.
*ProductImagesApi* | [**productsIdImagesJsonGet**](docs/ProductImagesApi.md#productsIdImagesJsonGet) | **GET** /products/{id}/images.json | Retrieve all Product Images.
*ProductImagesApi* | [**productsIdImagesJsonPost**](docs/ProductImagesApi.md#productsIdImagesJsonPost) | **POST** /products/{id}/images.json | Create a new Product Image.
*ProductOptionValuesApi* | [**productsIdOptionsOptionIdValuesCountJsonGet**](docs/ProductOptionValuesApi.md#productsIdOptionsOptionIdValuesCountJsonGet) | **GET** /products/{id}/options/{option_id}/values/count.json | Count all Product Option Values.
*ProductOptionValuesApi* | [**productsIdOptionsOptionIdValuesJsonGet**](docs/ProductOptionValuesApi.md#productsIdOptionsOptionIdValuesJsonGet) | **GET** /products/{id}/options/{option_id}/values.json | Retrieve all Product Option Values.
*ProductOptionValuesApi* | [**productsIdOptionsOptionIdValuesJsonPost**](docs/ProductOptionValuesApi.md#productsIdOptionsOptionIdValuesJsonPost) | **POST** /products/{id}/options/{option_id}/values.json | Create a new Product Option Value.
*ProductOptionValuesApi* | [**productsIdOptionsOptionIdValuesValueIdJsonDelete**](docs/ProductOptionValuesApi.md#productsIdOptionsOptionIdValuesValueIdJsonDelete) | **DELETE** /products/{id}/options/{option_id}/values/{value_id}.json | Delete a Product Option Value.
*ProductOptionValuesApi* | [**productsIdOptionsOptionIdValuesValueIdJsonGet**](docs/ProductOptionValuesApi.md#productsIdOptionsOptionIdValuesValueIdJsonGet) | **GET** /products/{id}/options/{option_id}/values/{value_id}.json | Retrieve a single Product Option Value.
*ProductOptionValuesApi* | [**productsIdOptionsOptionIdValuesValueIdJsonPut**](docs/ProductOptionValuesApi.md#productsIdOptionsOptionIdValuesValueIdJsonPut) | **PUT** /products/{id}/options/{option_id}/values/{value_id}.json | Modify an existing Product Option Value.
*ProductOptionsApi* | [**productsIdOptionsCountJsonGet**](docs/ProductOptionsApi.md#productsIdOptionsCountJsonGet) | **GET** /products/{id}/options/count.json | Count all Product Options.
*ProductOptionsApi* | [**productsIdOptionsJsonGet**](docs/ProductOptionsApi.md#productsIdOptionsJsonGet) | **GET** /products/{id}/options.json | Retrieve all Product Options.
*ProductOptionsApi* | [**productsIdOptionsJsonPost**](docs/ProductOptionsApi.md#productsIdOptionsJsonPost) | **POST** /products/{id}/options.json | Create a new Product Option.
*ProductOptionsApi* | [**productsIdOptionsOptionIdJsonDelete**](docs/ProductOptionsApi.md#productsIdOptionsOptionIdJsonDelete) | **DELETE** /products/{id}/options/{option_id}.json | Delete a Product Option.
*ProductOptionsApi* | [**productsIdOptionsOptionIdJsonGet**](docs/ProductOptionsApi.md#productsIdOptionsOptionIdJsonGet) | **GET** /products/{id}/options/{option_id}.json | Retrieve a single Product Option.
*ProductOptionsApi* | [**productsIdOptionsOptionIdJsonPut**](docs/ProductOptionsApi.md#productsIdOptionsOptionIdJsonPut) | **PUT** /products/{id}/options/{option_id}.json | Modify an existing Product Option.
*ProductVariantsApi* | [**productsIdVariantsCountJsonGet**](docs/ProductVariantsApi.md#productsIdVariantsCountJsonGet) | **GET** /products/{id}/variants/count.json | Count all Product Variants.
*ProductVariantsApi* | [**productsIdVariantsJsonGet**](docs/ProductVariantsApi.md#productsIdVariantsJsonGet) | **GET** /products/{id}/variants.json | Retrieve all Product Variants.
*ProductVariantsApi* | [**productsIdVariantsJsonPost**](docs/ProductVariantsApi.md#productsIdVariantsJsonPost) | **POST** /products/{id}/variants.json | Create a new Product Variant.
*ProductVariantsApi* | [**productsIdVariantsVariantIdJsonGet**](docs/ProductVariantsApi.md#productsIdVariantsVariantIdJsonGet) | **GET** /products/{id}/variants/{variant_id}.json | Retrieve a single Product Variant.
*ProductVariantsApi* | [**productsIdVariantsVariantIdJsonPut**](docs/ProductVariantsApi.md#productsIdVariantsVariantIdJsonPut) | **PUT** /products/{id}/variants/{variant_id}.json | Modify an existing Product Variant.
*ProductsApi* | [**productsAfterIdJsonGet**](docs/ProductsApi.md#productsAfterIdJsonGet) | **GET** /products/after/{id}.json | Retrieves Products after the given id.
*ProductsApi* | [**productsCategoryCategoryIdCountJsonGet**](docs/ProductsApi.md#productsCategoryCategoryIdCountJsonGet) | **GET** /products/category/{category_id}/count.json | Count Products filtered by category.
*ProductsApi* | [**productsCategoryCategoryIdJsonGet**](docs/ProductsApi.md#productsCategoryCategoryIdJsonGet) | **GET** /products/category/{category_id}.json | Retrieve Products filtered by category.
*ProductsApi* | [**productsCountJsonGet**](docs/ProductsApi.md#productsCountJsonGet) | **GET** /products/count.json | Count all Products.
*ProductsApi* | [**productsIdJsonDelete**](docs/ProductsApi.md#productsIdJsonDelete) | **DELETE** /products/{id}.json | Delete an existing Product.
*ProductsApi* | [**productsIdJsonGet**](docs/ProductsApi.md#productsIdJsonGet) | **GET** /products/{id}.json | Retrieve a single Product.
*ProductsApi* | [**productsIdJsonPut**](docs/ProductsApi.md#productsIdJsonPut) | **PUT** /products/{id}.json | Modify an existing Product.
*ProductsApi* | [**productsJsonGet**](docs/ProductsApi.md#productsJsonGet) | **GET** /products.json | Retrieve all Products.
*ProductsApi* | [**productsJsonPost**](docs/ProductsApi.md#productsJsonPost) | **POST** /products.json | Create a new Product.
*ProductsApi* | [**productsSearchJsonGet**](docs/ProductsApi.md#productsSearchJsonGet) | **GET** /products/search.json | Retrieve a Product List from a query.
*ProductsApi* | [**productsStatusStatusCountJsonGet**](docs/ProductsApi.md#productsStatusStatusCountJsonGet) | **GET** /products/status/{status}/count.json | Count Products filtered by status.
*ProductsApi* | [**productsStatusStatusJsonGet**](docs/ProductsApi.md#productsStatusStatusJsonGet) | **GET** /products/status/{status}.json | Retrieve Products filtered by status.
*PromotionsApi* | [**promotionsIdJsonDelete**](docs/PromotionsApi.md#promotionsIdJsonDelete) | **DELETE** /promotions/{id}.json | Delete an existing Promotion.
*PromotionsApi* | [**promotionsIdJsonGet**](docs/PromotionsApi.md#promotionsIdJsonGet) | **GET** /promotions/{id}.json | Retrieve a single Promotion.
*PromotionsApi* | [**promotionsIdJsonPut**](docs/PromotionsApi.md#promotionsIdJsonPut) | **PUT** /promotions/{id}.json | Update a Promotion.
*PromotionsApi* | [**promotionsJsonGet**](docs/PromotionsApi.md#promotionsJsonGet) | **GET** /promotions.json | Retrieve all Promotions.
*PromotionsApi* | [**promotionsJsonPost**](docs/PromotionsApi.md#promotionsJsonPost) | **POST** /promotions.json | Create a new Promotion.
*RegionsApi* | [**countriesCountryCodeRegionsJsonGet_0**](docs/RegionsApi.md#countriesCountryCodeRegionsJsonGet_0) | **GET** /countries/{country_code}/regions.json | Retrieve all Regions from a single Country.
*RegionsApi* | [**countriesCountryCodeRegionsRegionCodeJsonGet_0**](docs/RegionsApi.md#countriesCountryCodeRegionsRegionCodeJsonGet_0) | **GET** /countries/{country_code}/regions/{region_code}.json | Retrieve a single Region information object.
*ShippingMethodsApi* | [**shippingMethodsIdJsonDelete**](docs/ShippingMethodsApi.md#shippingMethodsIdJsonDelete) | **DELETE** /shipping_methods/{id}.json | Delete an existing Shipping Method.
*ShippingMethodsApi* | [**shippingMethodsIdJsonGet**](docs/ShippingMethodsApi.md#shippingMethodsIdJsonGet) | **GET** /shipping_methods/{id}.json | Retrieve a single Shipping Method.
*ShippingMethodsApi* | [**shippingMethodsIdJsonPut**](docs/ShippingMethodsApi.md#shippingMethodsIdJsonPut) | **PUT** /shipping_methods/{id}.json | Update a Shipping Method.
*ShippingMethodsApi* | [**shippingMethodsJsonGet**](docs/ShippingMethodsApi.md#shippingMethodsJsonGet) | **GET** /shipping_methods.json | Retrieve all Store&#39;s Shipping Methods.
*ShippingMethodsApi* | [**shippingMethodsJsonPost**](docs/ShippingMethodsApi.md#shippingMethodsJsonPost) | **POST** /shipping_methods.json | Creates a Shipping Method.
*StoresApi* | [**storeInfoJsonGet**](docs/StoresApi.md#storeInfoJsonGet) | **GET** /store/info.json | Retrieve Store Information.
*StoresApi* | [**storeLanguagesJsonGet**](docs/StoresApi.md#storeLanguagesJsonGet) | **GET** /store/languages.json | Retrieve Store Languages.
*TaxesApi* | [**taxesIdJsonGet**](docs/TaxesApi.md#taxesIdJsonGet) | **GET** /taxes/{id}.json | Retrieve a single Tax information.
*TaxesApi* | [**taxesJsonGet**](docs/TaxesApi.md#taxesJsonGet) | **GET** /taxes.json | Retrieve all Taxes.
*TaxesApi* | [**taxesJsonPost**](docs/TaxesApi.md#taxesJsonPost) | **POST** /taxes.json | Create a new Tax.


## Documentation for Models

 - [AddProductCustomField](docs/AddProductCustomField.md)
 - [AddProductCustomFieldFields](docs/AddProductCustomFieldFields.md)
 - [App](docs/App.md)
 - [AppFields](docs/AppFields.md)
 - [Attachment](docs/Attachment.md)
 - [AttachmentEdit](docs/AttachmentEdit.md)
 - [AttachmentEditFields](docs/AttachmentEditFields.md)
 - [AttachmentFields](docs/AttachmentFields.md)
 - [BadParams](docs/BadParams.md)
 - [BestSold](docs/BestSold.md)
 - [BillingAddress](docs/BillingAddress.md)
 - [Category](docs/Category.md)
 - [CategoryEdit](docs/CategoryEdit.md)
 - [CategoryEditFields](docs/CategoryEditFields.md)
 - [CategoryFields](docs/CategoryFields.md)
 - [CheckoutCustomField](docs/CheckoutCustomField.md)
 - [CheckoutCustomFieldEdit](docs/CheckoutCustomFieldEdit.md)
 - [CheckoutCustomFieldEditFields](docs/CheckoutCustomFieldEditFields.md)
 - [CheckoutCustomFieldFields](docs/CheckoutCustomFieldFields.md)
 - [Count](docs/Count.md)
 - [Country](docs/Country.md)
 - [CountryOrders](docs/CountryOrders.md)
 - [CustomField](docs/CustomField.md)
 - [CustomFieldEdit](docs/CustomFieldEdit.md)
 - [CustomFieldEditFields](docs/CustomFieldEditFields.md)
 - [CustomFieldFields](docs/CustomFieldFields.md)
 - [CustomFieldSelectOption](docs/CustomFieldSelectOption.md)
 - [CustomFieldSelectOptionEdit](docs/CustomFieldSelectOptionEdit.md)
 - [CustomFieldSelectOptionEditFields](docs/CustomFieldSelectOptionEditFields.md)
 - [CustomFieldSelectOptionFields](docs/CustomFieldSelectOptionFields.md)
 - [Customer](docs/Customer.md)
 - [CustomerAdditionalField](docs/CustomerAdditionalField.md)
 - [CustomerAdditionalFieldEdit](docs/CustomerAdditionalFieldEdit.md)
 - [CustomerAdditionalFieldEditFields](docs/CustomerAdditionalFieldEditFields.md)
 - [CustomerAdditionalFieldFields](docs/CustomerAdditionalFieldFields.md)
 - [CustomerCategory](docs/CustomerCategory.md)
 - [CustomerCategoryEdit](docs/CustomerCategoryEdit.md)
 - [CustomerCategoryEditFields](docs/CustomerCategoryEditFields.md)
 - [CustomerCategoryFields](docs/CustomerCategoryFields.md)
 - [CustomerFields](docs/CustomerFields.md)
 - [CustomerFieldsWithBillingAddressAndShippingAddressFields](docs/CustomerFieldsWithBillingAddressAndShippingAddressFields.md)
 - [CustomerFieldsWithPassword](docs/CustomerFieldsWithPassword.md)
 - [CustomerFieldsWithPasswordNoID](docs/CustomerFieldsWithPasswordNoID.md)
 - [CustomerToCustomerCategory](docs/CustomerToCustomerCategory.md)
 - [CustomerWithPassword](docs/CustomerWithPassword.md)
 - [CustomerWithPasswordNoID](docs/CustomerWithPasswordNoID.md)
 - [CustomersToCustomerCategory](docs/CustomersToCustomerCategory.md)
 - [DailyVisits](docs/DailyVisits.md)
 - [DigitalProduct](docs/DigitalProduct.md)
 - [DigitalProductEdit](docs/DigitalProductEdit.md)
 - [DigitalProductEditFields](docs/DigitalProductEditFields.md)
 - [DigitalProductFields](docs/DigitalProductFields.md)
 - [Fulfillment](docs/Fulfillment.md)
 - [FulfillmentCreate](docs/FulfillmentCreate.md)
 - [FulfillmentCreateFields](docs/FulfillmentCreateFields.md)
 - [FulfillmentEdit](docs/FulfillmentEdit.md)
 - [FulfillmentEditFields](docs/FulfillmentEditFields.md)
 - [FulfillmentFields](docs/FulfillmentFields.md)
 - [Hook](docs/Hook.md)
 - [HookEdit](docs/HookEdit.md)
 - [HookEditFields](docs/HookEditFields.md)
 - [HookFields](docs/HookFields.md)
 - [Id](docs/Id.md)
 - [Image](docs/Image.md)
 - [ImageEdit](docs/ImageEdit.md)
 - [ImageEditFields](docs/ImageEditFields.md)
 - [ImageFields](docs/ImageFields.md)
 - [JSApp](docs/JSApp.md)
 - [JSAppEdit](docs/JSAppEdit.md)
 - [Language](docs/Language.md)
 - [MessageObject](docs/MessageObject.md)
 - [NewPartnerStore](docs/NewPartnerStore.md)
 - [NewPartnerStoreStore](docs/NewPartnerStoreStore.md)
 - [NewVsReturning](docs/NewVsReturning.md)
 - [NotFound](docs/NotFound.md)
 - [Order](docs/Order.md)
 - [OrderAdditionalFields](docs/OrderAdditionalFields.md)
 - [OrderBillingAddress](docs/OrderBillingAddress.md)
 - [OrderCreate](docs/OrderCreate.md)
 - [OrderCreateFields](docs/OrderCreateFields.md)
 - [OrderEdit](docs/OrderEdit.md)
 - [OrderEditFields](docs/OrderEditFields.md)
 - [OrderFields](docs/OrderFields.md)
 - [OrderHistory](docs/OrderHistory.md)
 - [OrderHistoryEdit](docs/OrderHistoryEdit.md)
 - [OrderHistoryEditFields](docs/OrderHistoryEditFields.md)
 - [OrderHistoryFields](docs/OrderHistoryFields.md)
 - [OrderProduct](docs/OrderProduct.md)
 - [OrderProductOrderCreate](docs/OrderProductOrderCreate.md)
 - [OrderProductTax](docs/OrderProductTax.md)
 - [OrderShippingAddress](docs/OrderShippingAddress.md)
 - [OrderShippingTax](docs/OrderShippingTax.md)
 - [OrdersData](docs/OrdersData.md)
 - [Page](docs/Page.md)
 - [PageCategory](docs/PageCategory.md)
 - [PageFields](docs/PageFields.md)
 - [PageFieldsImage](docs/PageFieldsImage.md)
 - [PageModify](docs/PageModify.md)
 - [PageModifyFields](docs/PageModifyFields.md)
 - [PageTemplate](docs/PageTemplate.md)
 - [PartnerError](docs/PartnerError.md)
 - [PartnerStoreCode](docs/PartnerStoreCode.md)
 - [PartnerStoreCodeStore](docs/PartnerStoreCodeStore.md)
 - [PartnerStoreCreate](docs/PartnerStoreCreate.md)
 - [PartnerStoreStatus](docs/PartnerStoreStatus.md)
 - [PartnerStoreStatusStatus](docs/PartnerStoreStatusStatus.md)
 - [PaymentMethod](docs/PaymentMethod.md)
 - [PaymentMethodFields](docs/PaymentMethodFields.md)
 - [PaymentMethodFreq](docs/PaymentMethodFreq.md)
 - [Product](docs/Product.md)
 - [ProductCustomField](docs/ProductCustomField.md)
 - [ProductCustomFieldFields](docs/ProductCustomFieldFields.md)
 - [ProductEdit](docs/ProductEdit.md)
 - [ProductEditFields](docs/ProductEditFields.md)
 - [ProductFields](docs/ProductFields.md)
 - [ProductOption](docs/ProductOption.md)
 - [ProductOptionEdit](docs/ProductOptionEdit.md)
 - [ProductOptionEditFields](docs/ProductOptionEditFields.md)
 - [ProductOptionFields](docs/ProductOptionFields.md)
 - [ProductOptionValue](docs/ProductOptionValue.md)
 - [ProductOptionValueEdit](docs/ProductOptionValueEdit.md)
 - [ProductOptionValueEditFields](docs/ProductOptionValueEditFields.md)
 - [ProductOptionValueFields](docs/ProductOptionValueFields.md)
 - [ProductOptionVariantEdit](docs/ProductOptionVariantEdit.md)
 - [Promotion](docs/Promotion.md)
 - [PromotionEdit](docs/PromotionEdit.md)
 - [PromotionEditFields](docs/PromotionEditFields.md)
 - [PromotionFields](docs/PromotionFields.md)
 - [Referrer](docs/Referrer.md)
 - [Region](docs/Region.md)
 - [RegionOrders](docs/RegionOrders.md)
 - [ShippingAddress](docs/ShippingAddress.md)
 - [ShippingMethod](docs/ShippingMethod.md)
 - [ShippingMethodEdit](docs/ShippingMethodEdit.md)
 - [ShippingMethodEditShippingMethod](docs/ShippingMethodEditShippingMethod.md)
 - [ShippingMethodFields](docs/ShippingMethodFields.md)
 - [ShippingMethodFreq](docs/ShippingMethodFreq.md)
 - [ShippingService](docs/ShippingService.md)
 - [StatusInvalid](docs/StatusInvalid.md)
 - [Store](docs/Store.md)
 - [StoreAddress](docs/StoreAddress.md)
 - [StoreCheckStatusJsonGet200Response](docs/StoreCheckStatusJsonGet200Response.md)
 - [StoreStats](docs/StoreStats.md)
 - [StoreStatsConversions](docs/StoreStatsConversions.md)
 - [StoreStatsNewVsReturningCustomers](docs/StoreStatsNewVsReturningCustomers.md)
 - [StoreStatsOrders](docs/StoreStatsOrders.md)
 - [StoreStatsRegionOrders](docs/StoreStatsRegionOrders.md)
 - [Tax](docs/Tax.md)
 - [TaxEdit](docs/TaxEdit.md)
 - [TaxEditFields](docs/TaxEditFields.md)
 - [TaxFields](docs/TaxFields.md)
 - [TrafficSource](docs/TrafficSource.md)
 - [TrafficType](docs/TrafficType.md)
 - [Type](docs/Type.md)
 - [Variant](docs/Variant.md)
 - [VariantEdit](docs/VariantEdit.md)
 - [VariantEditFields](docs/VariantEditFields.md)
 - [VariantFields](docs/VariantFields.md)


<a id="documentation-for-authorization"></a>
## Documentation for Authorization

Endpoints do not require authorization.


## Recommendation

It's recommended to create an instance of `ApiClient` per thread in a multithreaded environment to avoid any potential issues.

## Author



