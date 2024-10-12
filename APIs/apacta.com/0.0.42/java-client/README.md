# openapi-java-client

Apacta
- API version: 0.0.42
  - Build date: 2024-10-12T09:56:16.415087-04:00[America/New_York]
  - Generator version: 7.9.0

API for a tool to craftsmen used to register working hours, material usage and quality assurance.
# Endpoint
The endpoint `https://app.apacta.com/api/v1` should be used to communicate with the API. API access is only allowed with SSL encrypted connection (https).
# Authentication
URL query authentication with an API key is used, so appending `?api_key={api_key}` to the URL where `{api_key}` is found within Apacta settings is used for authentication
# Pagination
If the endpoint returns a `pagination` object it means the endpoint supports pagination - currently it's only possible to change pages with `?page={page_number}` but implementing custom page sizes are on the road map.


# Search/filter
Is experimental but implemented in some cases - see the individual endpoints' docs for further explanation.
# Ordering
Is currently experimental, but on some endpoints it's implemented on URL querys so eg. to order Invoices by `invoice_number` appending `?sort=Invoices.invoice_number&direction=desc` would sort the list descending by the value of `invoice_number`.
# Associations
Is currently implemented on an experimental basis where you can append eg. `?include=Contacts,Projects`  to the `/api/v1/invoices/` endpoint to embed `Contact` and `Project` objects directly.
# Project Files
Currently project files can be retrieved from two endpoints. `/projects/{project_id}/files` handles files uploaded from wall posts or forms. `/projects/{project_id}/project_files` allows uploading and showing files, not belonging to specific form or wall post.
# Errors/Exceptions
## 422 (Validation)
Write something about how the `errors` object contains keys with the properties that failes validation like:
```
  {
      \"success\": false,
      \"data\": {
          \"code\": 422,
          \"url\": \"/api/v1/contacts?api_key=5523be3b-30ef-425d-8203-04df7caaa93a\",
          \"message\": \"A validation error occurred\",
          \"errorCount\": 1,
          \"errors\": {
              \"contact_types\": [ ## Property name that failed validation
                  \"Contacts must have at least one contact type\" ## Message with further explanation
              ]
          }
      }
  }
```
## Code examples
Running examples of how to retrieve the 5 most recent forms registered and embed the details of the User that made the form, and eventual products contained in the form
### Swift
```
```
### Java
#### OkHttp
```
  OkHttpClient client = new OkHttpClient();

  Request request = new Request.Builder()
    .url(\"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\")
    .get()
    .addHeader(\"x-auth-token\", \"{INSERT_YOUR_TOKEN}\")
    .addHeader(\"accept\", \"application/json\")
    .build();

  Response response = client.newCall(request).execute();
```
#### Unirest
```
  HttpResponse<String> response = Unirest.get(\"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\")
    .header(\"x-auth-token\", \"{INSERT_YOUR_TOKEN}\")
    .header(\"accept\", \"application/json\")
    .asString();
```
### Javascript
#### Native
```
  var data = null;

  var xhr = new XMLHttpRequest();

  xhr.addEventListener(\"readystatechange\", function () {
    if (this.readyState === 4) {
      console.log(this.responseText);
    }
  });

  xhr.open(\"GET\", \"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\");
  xhr.setRequestHeader(\"x-auth-token\", \"{INSERT_YOUR_TOKEN}\");
  xhr.setRequestHeader(\"accept\", \"application/json\");

  xhr.send(data);
```
#### jQuery
```
  var settings = {
    \"async\": true,
    \"crossDomain\": true,
    \"url\": \"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\",
    \"method\": \"GET\",
    \"headers\": {
      \"x-auth-token\": \"{INSERT_YOUR_TOKEN}\",
      \"accept\": \"application/json\",
    }
  }

  $.ajax(settings).done(function (response) {
    console.log(response);
  });
```
#### NodeJS (Request)
```
  var request = require(\"request\");

  var options = { method: 'GET',
    url: 'https://app.apacta.com/api/v1/forms',
    qs:
     { extended: 'true',
       sort: 'Forms.created',
       direction: 'DESC',
       include: 'Products,CreatedBy',
       limit: '5' },
    headers:
     { accept: 'application/json',
       'x-auth-token': '{INSERT_YOUR_TOKEN}' } };

  request(options, function (error, response, body) {
    if (error) throw new Error(error);

    console.log(body);
  });

```
### Python 3
```
  import http.client

  conn = http.client.HTTPSConnection(\"app.apacta.com\")

  payload = \"\"

  headers = {
      'x-auth-token': \"{INSERT_YOUR_TOKEN}\",
      'accept': \"application/json\",
      }

  conn.request(\"GET\", \"/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\", payload, headers)

  res = conn.getresponse()
  data = res.read()

  print(data.decode(\"utf-8\"))
```
### C#
#### RestSharp
```
  var client = new RestClient(\"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\");
  var request = new RestRequest(Method.GET);
  request.AddHeader(\"accept\", \"application/json\");
  request.AddHeader(\"x-auth-token\", \"{INSERT_YOUR_TOKEN}\");
  IRestResponse response = client.Execute(request);
```
### Ruby
```
  require 'uri'
  require 'net/http'

  url = URI(\"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\")

  http = Net::HTTP.new(url.host, url.port)
  http.use_ssl = true
  http.verify_mode = OpenSSL::SSL::VERIFY_NONE

  request = Net::HTTP::Get.new(url)
  request[\"x-auth-token\"] = '{INSERT_YOUR_TOKEN}'
  request[\"accept\"] = 'application/json'

  response = http.request(request)
  puts response.read_body
```
### PHP (HttpRequest)
```
  <?php

  $request = new HttpRequest();
  $request->setUrl('https://app.apacta.com/api/v1/forms');
  $request->setMethod(HTTP_METH_GET);

  $request->setQueryData(array(
    'extended' => 'true',
    'sort' => 'Forms.created',
    'direction' => 'DESC',
    'include' => 'Products,CreatedBy',
    'limit' => '5'
  ));

  $request->setHeaders(array(
    'accept' => 'application/json',
    'x-auth-token' => '{INSERT_YOUR_TOKEN}'
  ));

  try {
    $response = $request->send();

    echo $response->getBody();
  } catch (HttpException $ex) {
    echo $ex;
  }
```
### Shell (cURL)
```

  $ curl --request GET --url 'https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5' --header 'accept: application/json' --header 'x-auth-token: {INSERT_YOUR_TOKEN}'

```


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
  <version>0.0.42</version>
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
     implementation "org.openapitools:openapi-java-client:0.0.42"
  }
```

### Others

At first generate the JAR by executing:

```shell
mvn clean package
```

Then manually install the following JARs:

* `target/openapi-java-client-0.0.42.jar`
* `target/lib/*.jar`

## Getting Started

Please follow the [installation](#installation) instruction and execute the following Java code:

```java

// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.model.*;
import org.openapitools.client.api.ActivitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");

    ActivitiesApi apiInstance = new ActivitiesApi(defaultClient);
    UUID activityId = UUID.randomUUID(); // UUID | 
    try {
      EmptySuccessResponse result = apiInstance.activitiesActivityIdDelete(activityId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivitiesApi#activitiesActivityIdDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

## Documentation for API Endpoints

All URIs are relative to *https://app.apacta.com/api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ActivitiesApi* | [**activitiesActivityIdDelete**](docs/ActivitiesApi.md#activitiesActivityIdDelete) | **DELETE** /activities/{activity_id} | Delete an activity
*ActivitiesApi* | [**activitiesActivityIdPut**](docs/ActivitiesApi.md#activitiesActivityIdPut) | **PUT** /activities/{activity_id} | Edit an activity
*ActivitiesApi* | [**activitiesBulkDeleteDelete**](docs/ActivitiesApi.md#activitiesBulkDeleteDelete) | **DELETE** /activities/bulkDelete | Bulk delete activities
*ActivitiesApi* | [**activitiesGet**](docs/ActivitiesApi.md#activitiesGet) | **GET** /activities | Get a list of activities
*ActivitiesApi* | [**activitiesPost**](docs/ActivitiesApi.md#activitiesPost) | **POST** /activities | Create an activity
*ChangelogApi* | [**offersOfferIdChangelogGet**](docs/ChangelogApi.md#offersOfferIdChangelogGet) | **GET** /offers/{offer_id}/changelog | Get list of changelog history for the offer. Returns offer object with contact and user objects if they are provided
*CitiesApi* | [**citiesCityIdGet**](docs/CitiesApi.md#citiesCityIdGet) | **GET** /cities/{city_id} | Get details about one city
*CitiesApi* | [**citiesGet**](docs/CitiesApi.md#citiesGet) | **GET** /cities | Get list of cities supported in Apacta
*ClockingRecordsApi* | [**clockingRecordsCheckoutPost**](docs/ClockingRecordsApi.md#clockingRecordsCheckoutPost) | **POST** /clocking_records/checkout | Checkout active clocking record for authenticated user
*ClockingRecordsApi* | [**clockingRecordsClockingRecordIdDelete**](docs/ClockingRecordsApi.md#clockingRecordsClockingRecordIdDelete) | **DELETE** /clocking_records/{clocking_record_id} | Delete a clocking record
*ClockingRecordsApi* | [**clockingRecordsClockingRecordIdGet**](docs/ClockingRecordsApi.md#clockingRecordsClockingRecordIdGet) | **GET** /clocking_records/{clocking_record_id} | Details of 1 clocking_record
*ClockingRecordsApi* | [**clockingRecordsClockingRecordIdPut**](docs/ClockingRecordsApi.md#clockingRecordsClockingRecordIdPut) | **PUT** /clocking_records/{clocking_record_id} | Edit a clocking record
*ClockingRecordsApi* | [**clockingRecordsGet**](docs/ClockingRecordsApi.md#clockingRecordsGet) | **GET** /clocking_records | Get a list of clocking records
*ClockingRecordsApi* | [**clockingRecordsPost**](docs/ClockingRecordsApi.md#clockingRecordsPost) | **POST** /clocking_records | Create clocking record for authenticated user
*CompaniesApi* | [**companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGet**](docs/CompaniesApi.md#companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGet) | **GET** /companies/{company_id}/companies_integration_feature_settings/{c_integration_feature_setting_id} | View a company integration feature setting
*CompaniesApi* | [**companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPut**](docs/CompaniesApi.md#companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPut) | **PUT** /companies/{company_id}/companies_integration_feature_settings/{c_integration_feature_setting_id} | Edit a company integration feature setting
*CompaniesApi* | [**companiesCompanyIdCompaniesIntegrationFeatureSettingsGet**](docs/CompaniesApi.md#companiesCompanyIdCompaniesIntegrationFeatureSettingsGet) | **GET** /companies/{company_id}/companies_integration_feature_settings | List a company integration feature settings
*CompaniesApi* | [**companiesCompanyIdCompaniesIntegrationFeatureSettingsPost**](docs/CompaniesApi.md#companiesCompanyIdCompaniesIntegrationFeatureSettingsPost) | **POST** /companies/{company_id}/companies_integration_feature_settings | Add a company integration feature setting
*CompaniesApi* | [**companiesCompanyIdFormTemplatesFormTemplateIdDelete**](docs/CompaniesApi.md#companiesCompanyIdFormTemplatesFormTemplateIdDelete) | **DELETE** /companies/{company_id}/form_templates/{form_template_id} | Delete a form template company
*CompaniesApi* | [**companiesCompanyIdFormTemplatesFormTemplateIdGet**](docs/CompaniesApi.md#companiesCompanyIdFormTemplatesFormTemplateIdGet) | **GET** /companies/{company_id}/form_templates/{form_template_id} | Get a company form template
*CompaniesApi* | [**companiesCompanyIdFormTemplatesGet**](docs/CompaniesApi.md#companiesCompanyIdFormTemplatesGet) | **GET** /companies/{company_id}/form_templates/ | Get a list of company form templates
*CompaniesApi* | [**companiesCompanyIdGet**](docs/CompaniesApi.md#companiesCompanyIdGet) | **GET** /companies/{company_id} | Details of 1 company
*CompaniesApi* | [**companiesCompanyIdIntegrationFeatureSettingsGet**](docs/CompaniesApi.md#companiesCompanyIdIntegrationFeatureSettingsGet) | **GET** /companies/{company_id}/integration_feature_settings | Get a list of integration feature settings
*CompaniesApi* | [**companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet**](docs/CompaniesApi.md#companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet) | **GET** /companies/{company_id}/integration_feature_settings/{integration_feature_setting_id} | Show details of 1 integration feature setting
*CompaniesApi* | [**companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDelete**](docs/CompaniesApi.md#companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDelete) | **DELETE** /companies/{company_id}/integration_settings/{companies_integration_setting_id} | Delete a company integration setting
*CompaniesApi* | [**companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet**](docs/CompaniesApi.md#companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet) | **GET** /companies/{company_id}/integration_settings/{companies_integration_setting_id} | Get a company integration setting
*CompaniesApi* | [**companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPut**](docs/CompaniesApi.md#companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPut) | **PUT** /companies/{company_id}/integration_settings/{companies_integration_setting_id} | Edit a company integration setting
*CompaniesApi* | [**companiesCompanyIdIntegrationSettingsGet**](docs/CompaniesApi.md#companiesCompanyIdIntegrationSettingsGet) | **GET** /companies/{company_id}/integration_settings | Get a list of company integration settings
*CompaniesApi* | [**companiesCompanyIdIntegrationSettingsPost**](docs/CompaniesApi.md#companiesCompanyIdIntegrationSettingsPost) | **POST** /companies/{company_id}/integration_settings | Add a company integration setting
*CompaniesApi* | [**companiesCompanyIdPriceMarginsPriceMarginsIdDelete**](docs/CompaniesApi.md#companiesCompanyIdPriceMarginsPriceMarginsIdDelete) | **DELETE** /companies/{company_id}/price_margins/{price_margins_id} | Delete a company price margin
*CompaniesApi* | [**companiesCompanyIdPriceMarginsPriceMarginsIdGet**](docs/CompaniesApi.md#companiesCompanyIdPriceMarginsPriceMarginsIdGet) | **GET** /companies/{company_id}/price_margins/{price_margins_id} | Get a list of company price margins
*CompaniesApi* | [**companiesCompanyIdPriceMarginsPriceMarginsIdPost**](docs/CompaniesApi.md#companiesCompanyIdPriceMarginsPriceMarginsIdPost) | **POST** /companies/{company_id}/price_margins/{price_margins_id} | Add a company price margin
*CompaniesApi* | [**companiesGet**](docs/CompaniesApi.md#companiesGet) | **GET** /companies | Get a list of companies
*CompaniesApi* | [**companiesSubscriptionSelfServiceGet**](docs/CompaniesApi.md#companiesSubscriptionSelfServiceGet) | **GET** /companies/subscription_self_service | URL for subscription selfservice
*CompaniesVendorsApi* | [**addCompaniesVendor**](docs/CompaniesVendorsApi.md#addCompaniesVendor) | **POST** /companies_vendors | Add a new companies vendor
*CompaniesVendorsApi* | [**bulkCompaniesVendors**](docs/CompaniesVendorsApi.md#bulkCompaniesVendors) | **DELETE** /companies_vendors/bulkDelete | Bulk delete companies vendors
*CompaniesVendorsApi* | [**companiesVendorsCompaniesVendorIdDelete**](docs/CompaniesVendorsApi.md#companiesVendorsCompaniesVendorIdDelete) | **DELETE** /companies_vendors/{companies_vendor_id} | Delete a companies vendor
*CompaniesVendorsApi* | [**editCompaniesVendor**](docs/CompaniesVendorsApi.md#editCompaniesVendor) | **PUT** /companies_vendors/{companies_vendor_id} | Edit a companies vendor
*CompaniesVendorsApi* | [**getCompaiesVendorsList**](docs/CompaniesVendorsApi.md#getCompaiesVendorsList) | **GET** /companies_vendors | Get a list of companies vendors
*CompaniesVendorsApi* | [**getCompaniesVendor**](docs/CompaniesVendorsApi.md#getCompaniesVendor) | **GET** /companies_vendors/{companies_vendor_id} | Get a companies vendor
*CompaniesVendorsApi* | [**getCompaniesVendorsExpenseStatistics**](docs/CompaniesVendorsApi.md#getCompaniesVendorsExpenseStatistics) | **GET** /companies_vendors/{companies_vendor_id}/expense_statistics | Get companies vendor expense statistics
*CompanySettingsApi* | [**getCompaySettingsList**](docs/CompanySettingsApi.md#getCompaySettingsList) | **GET** /company_settings | Get a list of company settings
*ContactCustomFieldAttributesApi* | [**contactCustomFieldAttributesContactCustomFieldAttributeIdGet**](docs/ContactCustomFieldAttributesApi.md#contactCustomFieldAttributesContactCustomFieldAttributeIdGet) | **GET** /contact_custom_field_attributes/{contact_custom_field_attribute_id} | Details of 1 contact custom field attribute
*ContactCustomFieldAttributesApi* | [**contactCustomFieldAttributesGet**](docs/ContactCustomFieldAttributesApi.md#contactCustomFieldAttributesGet) | **GET** /contact_custom_field_attributes | Get a list of contact custom field attributes
*ContactCustomFieldValueApi* | [**contactsContactIdContactCustomFieldValuesGet**](docs/ContactCustomFieldValueApi.md#contactsContactIdContactCustomFieldValuesGet) | **GET** /contacts/{contact_id}/contact_custom_field_values | Get a list of contact custom field values
*ContactPersonsApi* | [**addContactPerson**](docs/ContactPersonsApi.md#addContactPerson) | **POST** /contacts/{contact_id}/contact_persons | Add a new contact person to a contact
*ContactPersonsApi* | [**contactsContactIdContactPersonsContactPersonIdDelete**](docs/ContactPersonsApi.md#contactsContactIdContactPersonsContactPersonIdDelete) | **DELETE** /contacts/{contact_id}/contact_persons/{contact_person_id} | Delete a contact person
*ContactPersonsApi* | [**editContactPerson**](docs/ContactPersonsApi.md#editContactPerson) | **PUT** /contacts/{contact_id}/contact_persons/{contact_person_id} | Edit a contact person
*ContactPersonsApi* | [**getContactPerson**](docs/ContactPersonsApi.md#getContactPerson) | **GET** /contacts/{contact_id}/contact_persons/{contact_person_id} | Get a contact person
*ContactPersonsApi* | [**getContactPersonsList**](docs/ContactPersonsApi.md#getContactPersonsList) | **GET** /contacts/{contact_id}/contact_persons | Get a list of contact people
*ContactTypesApi* | [**contactTypesContactTypeIdGet**](docs/ContactTypesApi.md#contactTypesContactTypeIdGet) | **GET** /contact_types/{contact_type_id} | Get details about one contact type
*ContactTypesApi* | [**contactTypesGet**](docs/ContactTypesApi.md#contactTypesGet) | **GET** /contact_types | Get list of contact types supported in Apacta
*ContactsApi* | [**bulkDeleteContacts**](docs/ContactsApi.md#bulkDeleteContacts) | **DELETE** /contacts/bulkDelete | Bulk delete contacts
*ContactsApi* | [**contactsContactIdDelete**](docs/ContactsApi.md#contactsContactIdDelete) | **DELETE** /contacts/{contact_id} | Delete a contact
*ContactsApi* | [**contactsContactIdGet**](docs/ContactsApi.md#contactsContactIdGet) | **GET** /contacts/{contact_id} | Details of 1 contact
*ContactsApi* | [**contactsContactIdPut**](docs/ContactsApi.md#contactsContactIdPut) | **PUT** /contacts/{contact_id} | Edit a contact
*ContactsApi* | [**contactsGet**](docs/ContactsApi.md#contactsGet) | **GET** /contacts | Get a list of contacts
*ContactsApi* | [**contactsPost**](docs/ContactsApi.md#contactsPost) | **POST** /contacts | Add a new contact
*CountriesApi* | [**countriesCountryIdGet**](docs/CountriesApi.md#countriesCountryIdGet) | **GET** /countries/{country_id} | Get details about one country
*CountriesApi* | [**countriesGet**](docs/CountriesApi.md#countriesGet) | **GET** /countries | Get list of countries supported in Apacta
*CurrenciesApi* | [**currenciesCurrencyIdGet**](docs/CurrenciesApi.md#currenciesCurrencyIdGet) | **GET** /currencies/{currency_id} | Get details about one currency
*CurrenciesApi* | [**currenciesGet**](docs/CurrenciesApi.md#currenciesGet) | **GET** /currencies | Get list of currencies supported in Apacta
*DefaultProjectStatusesApi* | [**projectStatusesAddDefaultPost**](docs/DefaultProjectStatusesApi.md#projectStatusesAddDefaultPost) | **POST** /project_statuses/add_default | Add default project statuses to company
*DrivingTypesApi* | [**bulkDeleteDrivingTypes**](docs/DrivingTypesApi.md#bulkDeleteDrivingTypes) | **DELETE** /driving_types/bulkDelete | Bulk delete driving types
*DrivingTypesApi* | [**deleteDrivingTypesDrivingTypeId**](docs/DrivingTypesApi.md#deleteDrivingTypesDrivingTypeId) | **DELETE** /driving_types/{driving_type_id} | Delete driving type
*DrivingTypesApi* | [**getDrivingTypes**](docs/DrivingTypesApi.md#getDrivingTypes) | **GET** /driving_types | List the driving types of the company
*DrivingTypesApi* | [**getDrivingTypesDrivingTypeId**](docs/DrivingTypesApi.md#getDrivingTypesDrivingTypeId) | **GET** /driving_types/{driving_type_id} | View driving type
*DrivingTypesApi* | [**postDrivingTypes**](docs/DrivingTypesApi.md#postDrivingTypes) | **POST** /driving_types | Create driving type
*DrivingTypesApi* | [**putDrivingTypesDrivingTypeId**](docs/DrivingTypesApi.md#putDrivingTypesDrivingTypeId) | **PUT** /driving_types/{driving_type_id} | Edit driving type
*EmployeeHoursApi* | [**employeeHoursGet**](docs/EmployeeHoursApi.md#employeeHoursGet) | **GET** /employee_hours | Used to retrieve details about the logged in user&#39;s hours
*EventsApi* | [**eventsEventIdDelete**](docs/EventsApi.md#eventsEventIdDelete) | **DELETE** /events/{event_id} | Delete event
*EventsApi* | [**eventsEventIdGet**](docs/EventsApi.md#eventsEventIdGet) | **GET** /events/{event_id} | Show event
*EventsApi* | [**eventsEventIdPut**](docs/EventsApi.md#eventsEventIdPut) | **PUT** /events/{event_id} | Edit event
*EventsApi* | [**eventsGet**](docs/EventsApi.md#eventsGet) | **GET** /events | Show list of events
*EventsApi* | [**eventsIsUserFreeGet**](docs/EventsApi.md#eventsIsUserFreeGet) | **GET** /events/is_user_free | Check if user is available at given datetime range
*EventsApi* | [**eventsPost**](docs/EventsApi.md#eventsPost) | **POST** /events | Create event
*ExpenseFilesApi* | [**expenseFilesExpenseFileIdDelete**](docs/ExpenseFilesApi.md#expenseFilesExpenseFileIdDelete) | **DELETE** /expense_files/{expense_file_id} | Delete file
*ExpenseFilesApi* | [**expenseFilesExpenseFileIdGet**](docs/ExpenseFilesApi.md#expenseFilesExpenseFileIdGet) | **GET** /expense_files/{expense_file_id} | Show file
*ExpenseFilesApi* | [**expenseFilesExpenseFileIdPut**](docs/ExpenseFilesApi.md#expenseFilesExpenseFileIdPut) | **PUT** /expense_files/{expense_file_id} | Edit file
*ExpenseFilesApi* | [**expenseFilesGet**](docs/ExpenseFilesApi.md#expenseFilesGet) | **GET** /expense_files | Show list of expense files
*ExpenseFilesApi* | [**expenseFilesPost**](docs/ExpenseFilesApi.md#expenseFilesPost) | **POST** /expense_files | Add file to expense
*ExpenseLinesApi* | [**expenseLinesExpenseLineIdDelete**](docs/ExpenseLinesApi.md#expenseLinesExpenseLineIdDelete) | **DELETE** /expense_lines/{expense_line_id} | Delete expense line
*ExpenseLinesApi* | [**expenseLinesExpenseLineIdGet**](docs/ExpenseLinesApi.md#expenseLinesExpenseLineIdGet) | **GET** /expense_lines/{expense_line_id} | Show expense line
*ExpenseLinesApi* | [**expenseLinesExpenseLineIdPut**](docs/ExpenseLinesApi.md#expenseLinesExpenseLineIdPut) | **PUT** /expense_lines/{expense_line_id} | Edit expense line
*ExpenseLinesApi* | [**expenseLinesGet**](docs/ExpenseLinesApi.md#expenseLinesGet) | **GET** /expense_lines | Show list of expense lines
*ExpenseLinesApi* | [**expenseLinesPost**](docs/ExpenseLinesApi.md#expenseLinesPost) | **POST** /expense_lines | Add line to expense
*ExpenseOioublFilesApi* | [**expensesExpenseIdOriginalFilesFileIdGet**](docs/ExpenseOioublFilesApi.md#expensesExpenseIdOriginalFilesFileIdGet) | **GET** /expenses/{expense_id}/original_files/{file_id} | Show OIOUBL file
*ExpenseOioublFilesApi* | [**expensesExpenseIdOriginalFilesGet**](docs/ExpenseOioublFilesApi.md#expensesExpenseIdOriginalFilesGet) | **GET** /expenses/{expense_id}/original_files | Show list of all OIOUBL files for the expense
*ExpensesApi* | [**bulkDeleteExpenses**](docs/ExpensesApi.md#bulkDeleteExpenses) | **DELETE** /expenses/bulkDelete | Bulk delete expenses
*ExpensesApi* | [**expensesExpenseIdDelete**](docs/ExpensesApi.md#expensesExpenseIdDelete) | **DELETE** /expenses/{expense_id} | Delete expense
*ExpensesApi* | [**expensesExpenseIdGet**](docs/ExpensesApi.md#expensesExpenseIdGet) | **GET** /expenses/{expense_id} | Show expense
*ExpensesApi* | [**expensesExpenseIdPut**](docs/ExpensesApi.md#expensesExpenseIdPut) | **PUT** /expenses/{expense_id} | Edit expense
*ExpensesApi* | [**expensesGet**](docs/ExpensesApi.md#expensesGet) | **GET** /expenses | Show list of expenses
*ExpensesApi* | [**expensesHighestAmountGet**](docs/ExpensesApi.md#expensesHighestAmountGet) | **GET** /expenses/highest_amount | Show highest Expense amount(&#x60;total_selling_price&#x60;)
*ExpensesApi* | [**expensesPost**](docs/ExpensesApi.md#expensesPost) | **POST** /expenses | Add line to expense
*ExpensesApi* | [**sendEmailsExpenses**](docs/ExpensesApi.md#sendEmailsExpenses) | **DELETE** /expenses/sendEmails | Bulk delete expenses
*FinancialStatisticsApi* | [**financialStatisticsWorkingHoursGet**](docs/FinancialStatisticsApi.md#financialStatisticsWorkingHoursGet) | **GET** /financial_statistics/workingHours | Get Total working hours grouped by time entry type
*FinancialStatisticsApi* | [**getExpensesSalesPrice**](docs/FinancialStatisticsApi.md#getExpensesSalesPrice) | **GET** /financial_statistics/expensesSalesPrice | Get expenses sales price
*FinancialStatisticsApi* | [**getFinancialStatistics**](docs/FinancialStatisticsApi.md#getFinancialStatistics) | **GET** /financial_statistics | Get general statistics
*FinancialStatisticsApi* | [**getFinancialStatisticsOverview**](docs/FinancialStatisticsApi.md#getFinancialStatisticsOverview) | **GET** /financial_statistics/overview | Get statistics overview
*FinancialStatisticsApi* | [**getInvoicedAmount**](docs/FinancialStatisticsApi.md#getInvoicedAmount) | **GET** /financial_statistics/invoicedAmount | Get invoiced amount
*FinancialStatisticsApi* | [**getMargin**](docs/FinancialStatisticsApi.md#getMargin) | **GET** /financial_statistics/margin | Get margin
*FinancialStatisticsApi* | [**getMaterialRentalsCostPrice**](docs/FinancialStatisticsApi.md#getMaterialRentalsCostPrice) | **GET** /financial_statistics/materialRentalsCostPrice | Get products material rentals cost price
*FinancialStatisticsApi* | [**getProductsCostPrice**](docs/FinancialStatisticsApi.md#getProductsCostPrice) | **GET** /financial_statistics/productsCostPrice | Get products cost price
*FormFieldTypesApi* | [**formFieldTypesFormFieldTypeIdGet**](docs/FormFieldTypesApi.md#formFieldTypesFormFieldTypeIdGet) | **GET** /form_field_types/{form_field_type_id} | Get details about single &#x60;FormField&#x60;
*FormFieldTypesApi* | [**formFieldTypesGet**](docs/FormFieldTypesApi.md#formFieldTypesGet) | **GET** /form_field_types | Get list of form field types
*FormFieldsApi* | [**formFieldsFormFieldIdGet**](docs/FormFieldsApi.md#formFieldsFormFieldIdGet) | **GET** /form_fields/{form_field_id} | Get details about single &#x60;FormField&#x60;
*FormFieldsApi* | [**formFieldsPost**](docs/FormFieldsApi.md#formFieldsPost) | **POST** /form_fields | Add a new field to a &#x60;Form&#x60;
*FormTemplatesApi* | [**formTemplatesFormTemplateIdGet**](docs/FormTemplatesApi.md#formTemplatesFormTemplateIdGet) | **GET** /form_templates/{form_template_id} | View one form template
*FormTemplatesApi* | [**formTemplatesGet**](docs/FormTemplatesApi.md#formTemplatesGet) | **GET** /form_templates | Get array of form_templates for your company
*FormsApi* | [**formsFormIdDelete**](docs/FormsApi.md#formsFormIdDelete) | **DELETE** /forms/{form_id} | Delete a form
*FormsApi* | [**formsFormIdGet**](docs/FormsApi.md#formsFormIdGet) | **GET** /forms/{form_id} | View form
*FormsApi* | [**formsFormIdPut**](docs/FormsApi.md#formsFormIdPut) | **PUT** /forms/{form_id} | Edit a form
*FormsApi* | [**formsGet**](docs/FormsApi.md#formsGet) | **GET** /forms | Retrieve array of forms
*FormsApi* | [**formsPost**](docs/FormsApi.md#formsPost) | **POST** /forms | Add new form
*FormsApi* | [**formsUndeleteFormIdGet**](docs/FormsApi.md#formsUndeleteFormIdGet) | **GET** /forms/undelete/{form_id} | Undelete form and related entities to it
*FormsApi* | [**formsViewTimeFormPdfFormIdGet**](docs/FormsApi.md#formsViewTimeFormPdfFormIdGet) | **GET** /forms/view_time_form_pdf/{form_id} | Generate time form pdf
*IntegrationsApi* | [**getIntegrationsContactsSync**](docs/IntegrationsApi.md#getIntegrationsContactsSync) | **GET** /integrations/contactsSync | Force Synchronization with ERP systems
*IntegrationsApi* | [**getIntegrationsList**](docs/IntegrationsApi.md#getIntegrationsList) | **GET** /integrations | Get integrations list
*IntegrationsApi* | [**getIntegrationsView**](docs/IntegrationsApi.md#getIntegrationsView) | **GET** /integrations/{integration_id} | View integration details
*IntegrationsApi* | [**integrationsBillysAuthenticatePost**](docs/IntegrationsApi.md#integrationsBillysAuthenticatePost) | **POST** /integrations/billysAuthenticate | Authenticate to Billys
*IntegrationsApi* | [**integrationsProductsSyncGet**](docs/IntegrationsApi.md#integrationsProductsSyncGet) | **GET** /integrations/productsSync | Sync products from erp integration
*InvoiceEmailsApi* | [**getOneInvoiceEmails**](docs/InvoiceEmailsApi.md#getOneInvoiceEmails) | **GET** /invoices/{invoice_id}/emails/{email_id} | Get an invoice emails
*InvoiceFilesApi* | [**createInvoiceFile**](docs/InvoiceFilesApi.md#createInvoiceFile) | **POST** /invoices/{invoice_id}/files | Create a new invoice file
*InvoiceFilesApi* | [**getInvoiceFiles**](docs/InvoiceFilesApi.md#getInvoiceFiles) | **GET** /invoices/{invoice_id}/files | Get list of invoice files
*InvoiceFilesApi* | [**getOneInvoiceFiles**](docs/InvoiceFilesApi.md#getOneInvoiceFiles) | **GET** /invoices/{invoice_id}/files/{file_id} | Get an invoice files
*InvoiceFilesApi* | [**invoicesInvoiceIdFilesFileIdDelete**](docs/InvoiceFilesApi.md#invoicesInvoiceIdFilesFileIdDelete) | **DELETE** /invoices/{invoice_id}/files/{file_id} | Delete invoice file
*InvoiceLineTextTemplatesApi* | [**invoiceLineTextTemplateGet**](docs/InvoiceLineTextTemplatesApi.md#invoiceLineTextTemplateGet) | **GET** /invoice_line_text_template | Get a list of invoice line text templates
*InvoiceLineTextTemplatesApi* | [**invoiceLineTextTemplateInvoiceLineTextTemplateIdDelete**](docs/InvoiceLineTextTemplatesApi.md#invoiceLineTextTemplateInvoiceLineTextTemplateIdDelete) | **DELETE** /invoice_line_text_template/{invoice_line_text_template_id} | Delete an invoice line text template
*InvoiceLineTextTemplatesApi* | [**invoiceLineTextTemplateInvoiceLineTextTemplateIdGet**](docs/InvoiceLineTextTemplatesApi.md#invoiceLineTextTemplateInvoiceLineTextTemplateIdGet) | **GET** /invoice_line_text_template/{invoice_line_text_template_id} | Get a single invoice line text template
*InvoiceLineTextTemplatesApi* | [**invoiceLineTextTemplateInvoiceLineTextTemplateIdPost**](docs/InvoiceLineTextTemplatesApi.md#invoiceLineTextTemplateInvoiceLineTextTemplateIdPost) | **POST** /invoice_line_text_template/{invoice_line_text_template_id} | Edit an invoice line text template
*InvoiceLineTextTemplatesApi* | [**invoiceLineTextTemplatePost**](docs/InvoiceLineTextTemplatesApi.md#invoiceLineTextTemplatePost) | **POST** /invoice_line_text_template | Add a new invoice line text template
*InvoiceLinesApi* | [**invoiceLineTextsInvoiceLineTextIdPost**](docs/InvoiceLinesApi.md#invoiceLineTextsInvoiceLineTextIdPost) | **POST** /invoice_line_texts/{invoice_line_text_id} | Edit invoice line text
*InvoiceLinesApi* | [**invoiceLineTextsPost**](docs/InvoiceLinesApi.md#invoiceLineTextsPost) | **POST** /invoice_line_texts/ | Add invoice line text
*InvoiceLinesApi* | [**invoiceLinesGet**](docs/InvoiceLinesApi.md#invoiceLinesGet) | **GET** /invoice_lines | View list of invoice lines
*InvoiceLinesApi* | [**invoiceLinesInvoiceLineIdDelete**](docs/InvoiceLinesApi.md#invoiceLinesInvoiceLineIdDelete) | **DELETE** /invoice_lines/{invoice_line_id} | Delete invoice line
*InvoiceLinesApi* | [**invoiceLinesInvoiceLineIdGet**](docs/InvoiceLinesApi.md#invoiceLinesInvoiceLineIdGet) | **GET** /invoice_lines/{invoice_line_id} | View invoice line
*InvoiceLinesApi* | [**invoiceLinesInvoiceLineIdPut**](docs/InvoiceLinesApi.md#invoiceLinesInvoiceLineIdPut) | **PUT** /invoice_lines/{invoice_line_id} | Edit invoice line
*InvoiceLinesApi* | [**invoiceLinesPost**](docs/InvoiceLinesApi.md#invoiceLinesPost) | **POST** /invoice_lines | Add invoice line
*InvoicesApi* | [**bulkDeleteInvoices**](docs/InvoicesApi.md#bulkDeleteInvoices) | **DELETE** /invoices/bulkDelete | Bulk delete invoices
*InvoicesApi* | [**invoicesGet**](docs/InvoicesApi.md#invoicesGet) | **GET** /invoices | View list of invoices
*InvoicesApi* | [**invoicesInvoiceIdCopyPost**](docs/InvoicesApi.md#invoicesInvoiceIdCopyPost) | **POST** /invoices/{invoice_id}/copy | Create a copy of an invoice
*InvoicesApi* | [**invoicesInvoiceIdDelete**](docs/InvoicesApi.md#invoicesInvoiceIdDelete) | **DELETE** /invoices/{invoice_id} | Delete invoice
*InvoicesApi* | [**invoicesInvoiceIdGet**](docs/InvoicesApi.md#invoicesInvoiceIdGet) | **GET** /invoices/{invoice_id} | View invoice
*InvoicesApi* | [**invoicesInvoiceIdLinkProjectPdfPost**](docs/InvoicesApi.md#invoicesInvoiceIdLinkProjectPdfPost) | **POST** /invoices/{invoice_id}/linkProjectPdf | Creates an invoice file containing the project&#39;s pdf overview
*InvoicesApi* | [**invoicesInvoiceIdPut**](docs/InvoicesApi.md#invoicesInvoiceIdPut) | **PUT** /invoices/{invoice_id} | Edit invoice
*InvoicesApi* | [**invoicesInvoiceIdUnlinkProjectPdfPost**](docs/InvoicesApi.md#invoicesInvoiceIdUnlinkProjectPdfPost) | **POST** /invoices/{invoice_id}/unlinkProjectPdf | Deletes the linked project overview pdf
*InvoicesApi* | [**invoicesPost**](docs/InvoicesApi.md#invoicesPost) | **POST** /invoices | Add invoice
*InvoicesApi* | [**invoicesVatOptionsGet**](docs/InvoicesApi.md#invoicesVatOptionsGet) | **GET** /invoices/vatOptions | List VAT options
*MassMessagesUsersApi* | [**massMessagesUsersGet**](docs/MassMessagesUsersApi.md#massMessagesUsersGet) | **GET** /mass_messages_users | View list of mass messages for specific user
*MassMessagesUsersApi* | [**massMessagesUsersMassMessagesUserIdGet**](docs/MassMessagesUsersApi.md#massMessagesUsersMassMessagesUserIdGet) | **GET** /mass_messages_users/{mass_messages_user_id} | View mass message
*MassMessagesUsersApi* | [**massMessagesUsersMassMessagesUserIdPut**](docs/MassMessagesUsersApi.md#massMessagesUsersMassMessagesUserIdPut) | **PUT** /mass_messages_users/{mass_messages_user_id} | Edit mass message
*MaterialRentalsApi* | [**materialsMaterialIdRentalsCheckoutPost**](docs/MaterialRentalsApi.md#materialsMaterialIdRentalsCheckoutPost) | **POST** /materials/{material_id}/rentals/checkout/ | Checkout material rental
*MaterialRentalsApi* | [**materialsMaterialIdRentalsGet**](docs/MaterialRentalsApi.md#materialsMaterialIdRentalsGet) | **GET** /materials/{material_id}/rentals/ | Show list of rentals for specific material
*MaterialRentalsApi* | [**materialsMaterialIdRentalsMaterialRentalIdDelete**](docs/MaterialRentalsApi.md#materialsMaterialIdRentalsMaterialRentalIdDelete) | **DELETE** /materials/{material_id}/rentals/{material_rental_id}/ | Delete material rental
*MaterialRentalsApi* | [**materialsMaterialIdRentalsMaterialRentalIdGet**](docs/MaterialRentalsApi.md#materialsMaterialIdRentalsMaterialRentalIdGet) | **GET** /materials/{material_id}/rentals/{material_rental_id}/ | Show rental foor materi
*MaterialRentalsApi* | [**materialsMaterialIdRentalsMaterialRentalIdPut**](docs/MaterialRentalsApi.md#materialsMaterialIdRentalsMaterialRentalIdPut) | **PUT** /materials/{material_id}/rentals/{material_rental_id}/ | Edit material rental
*MaterialRentalsApi* | [**materialsMaterialIdRentalsPost**](docs/MaterialRentalsApi.md#materialsMaterialIdRentalsPost) | **POST** /materials/{material_id}/rentals/ | Add material rental
*MaterialsApi* | [**materialsGet**](docs/MaterialsApi.md#materialsGet) | **GET** /materials | View list of all materials
*MaterialsApi* | [**materialsMaterialIdDelete**](docs/MaterialsApi.md#materialsMaterialIdDelete) | **DELETE** /materials/{material_id} | Delete material
*MaterialsApi* | [**materialsMaterialIdGet**](docs/MaterialsApi.md#materialsMaterialIdGet) | **GET** /materials/{material_id} | View material
*MaterialsApi* | [**materialsMaterialIdPut**](docs/MaterialsApi.md#materialsMaterialIdPut) | **PUT** /materials/{material_id} | Edit material
*MaterialsApi* | [**materialsPost**](docs/MaterialsApi.md#materialsPost) | **POST** /materials | Add material
*OfferStatusesApi* | [**offerStatusesBulkDeleteDelete**](docs/OfferStatusesApi.md#offerStatusesBulkDeleteDelete) | **DELETE** /offer_statuses/bulkDelete | Bulk delete offer statuses
*OfferStatusesApi* | [**offerStatusesGet**](docs/OfferStatusesApi.md#offerStatusesGet) | **GET** /offer_statuses | Get list of offer statuses
*OfferStatusesApi* | [**offerStatusesOfferStatusIdDelete**](docs/OfferStatusesApi.md#offerStatusesOfferStatusIdDelete) | **DELETE** /offer_statuses/{offer_status_id} | Delete a offer status
*OfferStatusesApi* | [**offerStatusesOfferStatusIdGet**](docs/OfferStatusesApi.md#offerStatusesOfferStatusIdGet) | **GET** /offer_statuses/{offer_status_id} | Get a single offer status
*OfferStatusesApi* | [**offerStatusesOfferStatusIdPut**](docs/OfferStatusesApi.md#offerStatusesOfferStatusIdPut) | **PUT** /offer_statuses/{offer_status_id} | Edit a offer status
*OfferStatusesApi* | [**offerStatusesPost**](docs/OfferStatusesApi.md#offerStatusesPost) | **POST** /offer_statuses | Create a new offer status
*OffersApi* | [**offersGet**](docs/OffersApi.md#offersGet) | **GET** /offers | View list of offers
*OffersApi* | [**offersOfferIdDelete**](docs/OffersApi.md#offersOfferIdDelete) | **DELETE** /offers/{offer_id} | Delete an offer
*OffersApi* | [**offersOfferIdGet**](docs/OffersApi.md#offersOfferIdGet) | **GET** /offers/{offer_id} | View offer
*OffersApi* | [**offersOfferIdPut**](docs/OffersApi.md#offersOfferIdPut) | **PUT** /offers/{offer_id} | Edit an offer
*OffersApi* | [**offersPost**](docs/OffersApi.md#offersPost) | **POST** /offers | Add new offer
*PaymentTermTypesApi* | [**paymentTermTypesGet**](docs/PaymentTermTypesApi.md#paymentTermTypesGet) | **GET** /payment_term_types | Get a list of payment term types
*PaymentTermTypesApi* | [**paymentTermTypesPaymentTermTypeIdGet**](docs/PaymentTermTypesApi.md#paymentTermTypesPaymentTermTypeIdGet) | **GET** /payment_term_types/{payment_term_type_id} | Details of 1 payment term type
*PaymentTermsApi* | [**paymentTermsErpGet**](docs/PaymentTermsApi.md#paymentTermsErpGet) | **GET** /payment_terms/erp | Get integration payment terms list
*PaymentTermsApi* | [**paymentTermsGet**](docs/PaymentTermsApi.md#paymentTermsGet) | **GET** /payment_terms | Get a list of payment terms
*PaymentTermsApi* | [**paymentTermsPaymentTermIdGet**](docs/PaymentTermsApi.md#paymentTermsPaymentTermIdGet) | **GET** /payment_terms/{payment_term_id} | Details of 1 payment term
*PingApi* | [**pingGet**](docs/PingApi.md#pingGet) | **GET** /ping | Check if API is up and API key works
*ProductVariantsApi* | [**productsProductIdVariantsGet**](docs/ProductVariantsApi.md#productsProductIdVariantsGet) | **GET** /products/{product_id}/variants | Get a product&#39;s variants
*ProductVariantsApi* | [**productsProductIdVariantsPost**](docs/ProductVariantsApi.md#productsProductIdVariantsPost) | **POST** /products/{product_id}/variants | Add a new variant to a product
*ProductVariantsApi* | [**productsProductIdVariantsVariantTypeVariantIdDelete**](docs/ProductVariantsApi.md#productsProductIdVariantsVariantTypeVariantIdDelete) | **DELETE** /products/{product_id}/variants/{variant_type}/{variant_id} | Delete a product variant
*ProductsApi* | [**bulkDeleteProducts**](docs/ProductsApi.md#bulkDeleteProducts) | **DELETE** /products/bulkDelete | Bulk delete products
*ProductsApi* | [**productsGet**](docs/ProductsApi.md#productsGet) | **GET** /products | List products
*ProductsApi* | [**productsPost**](docs/ProductsApi.md#productsPost) | **POST** /products | Add new product
*ProductsApi* | [**productsProductIdDelete**](docs/ProductsApi.md#productsProductIdDelete) | **DELETE** /products/{product_id} | Delete a product
*ProductsApi* | [**productsProductIdGet**](docs/ProductsApi.md#productsProductIdGet) | **GET** /products/{product_id} | View single product
*ProductsApi* | [**productsProductIdPut**](docs/ProductsApi.md#productsProductIdPut) | **PUT** /products/{product_id} | Edit a product
*ProductsApi* | [**productsUndeleteProductIdPost**](docs/ProductsApi.md#productsUndeleteProductIdPost) | **POST** /products/undelete/{product_id} | Restore a deleted product
*ProductsApi* | [**uploadOrDeleteProductImage**](docs/ProductsApi.md#uploadOrDeleteProductImage) | **POST** /products/{product_id}/uploadImage | 
*ProjectCustomFieldAttributesApi* | [**projectCustomFieldAttributesGet**](docs/ProjectCustomFieldAttributesApi.md#projectCustomFieldAttributesGet) | **GET** /project_custom_field_attributes | Get a list of project custom field attributes
*ProjectCustomFieldAttributesApi* | [**projectCustomFieldAttributesProjectCustomFieldAttributeIdGet**](docs/ProjectCustomFieldAttributesApi.md#projectCustomFieldAttributesProjectCustomFieldAttributeIdGet) | **GET** /project_custom_field_attributes/{project_custom_field_attribute_id} | Details of 1 project custom field attribute
*ProjectStatusTypesApi* | [**projectStatusTypesGet**](docs/ProjectStatusTypesApi.md#projectStatusTypesGet) | **GET** /project_status_types | Get a list of project status types
*ProjectStatusesApi* | [**projectStatusesBulkDeleteDelete**](docs/ProjectStatusesApi.md#projectStatusesBulkDeleteDelete) | **DELETE** /project_statuses/bulkDelete | Bulk delete project statuses
*ProjectStatusesApi* | [**projectStatusesGet**](docs/ProjectStatusesApi.md#projectStatusesGet) | **GET** /project_statuses | Get list of project statuses
*ProjectStatusesApi* | [**projectStatusesPost**](docs/ProjectStatusesApi.md#projectStatusesPost) | **POST** /project_statuses | Create a new project status
*ProjectStatusesApi* | [**projectStatusesProjectStatusIdDelete**](docs/ProjectStatusesApi.md#projectStatusesProjectStatusIdDelete) | **DELETE** /project_statuses/{project_status_id} | Delete a project status
*ProjectStatusesApi* | [**projectStatusesProjectStatusIdGet**](docs/ProjectStatusesApi.md#projectStatusesProjectStatusIdGet) | **GET** /project_statuses/{project_status_id} | Get a single project status
*ProjectStatusesApi* | [**projectStatusesProjectStatusIdPut**](docs/ProjectStatusesApi.md#projectStatusesProjectStatusIdPut) | **PUT** /project_statuses/{project_status_id} | Edit a project status
*ProjectStatusesApi* | [**projectsHasProjectsWithCustomStatusesGet**](docs/ProjectStatusesApi.md#projectsHasProjectsWithCustomStatusesGet) | **GET** /projects/has_projects_with_custom_statuses | Check if the company has projects with custom statuses
*ProjectsApi* | [**projectsGet**](docs/ProjectsApi.md#projectsGet) | **GET** /projects | View list of projects
*ProjectsApi* | [**projectsHasProjectsWithCustomStatusesGet_0**](docs/ProjectsApi.md#projectsHasProjectsWithCustomStatusesGet_0) | **GET** /projects/has_projects_with_custom_statuses | Check if the company has projects with custom statuses
*ProjectsApi* | [**projectsPost**](docs/ProjectsApi.md#projectsPost) | **POST** /projects | Add a project
*ProjectsApi* | [**projectsProjectIdAllFilesGet**](docs/ProjectsApi.md#projectsProjectIdAllFilesGet) | **GET** /projects/{project_id}/all_files | Show list of all files uploaded to project
*ProjectsApi* | [**projectsProjectIdDelete**](docs/ProjectsApi.md#projectsProjectIdDelete) | **DELETE** /projects/{project_id} | Delete a project
*ProjectsApi* | [**projectsProjectIdFilesFileIdDelete**](docs/ProjectsApi.md#projectsProjectIdFilesFileIdDelete) | **DELETE** /projects/{project_id}/files/{file_id}/ | Delete file
*ProjectsApi* | [**projectsProjectIdFilesFileIdGet**](docs/ProjectsApi.md#projectsProjectIdFilesFileIdGet) | **GET** /projects/{project_id}/files/{file_id}/ | Show file
*ProjectsApi* | [**projectsProjectIdFilesFileIdPut**](docs/ProjectsApi.md#projectsProjectIdFilesFileIdPut) | **PUT** /projects/{project_id}/files/{file_id}/ | Edit file
*ProjectsApi* | [**projectsProjectIdFilesGet**](docs/ProjectsApi.md#projectsProjectIdFilesGet) | **GET** /projects/{project_id}/files | Show list of files uploaded to project
*ProjectsApi* | [**projectsProjectIdGet**](docs/ProjectsApi.md#projectsProjectIdGet) | **GET** /projects/{project_id} | View specific project
*ProjectsApi* | [**projectsProjectIdProjectFilesGet**](docs/ProjectsApi.md#projectsProjectIdProjectFilesGet) | **GET** /projects/{project_id}/project_files | Show list of project files uploaded to project
*ProjectsApi* | [**projectsProjectIdProjectFilesPost**](docs/ProjectsApi.md#projectsProjectIdProjectFilesPost) | **POST** /projects/{project_id}/project_files | Add project file to projects
*ProjectsApi* | [**projectsProjectIdProjectFilesProjectFileIdDelete**](docs/ProjectsApi.md#projectsProjectIdProjectFilesProjectFileIdDelete) | **DELETE** /projects/{project_id}/project_files/{project_file_id}/ | Delete project file
*ProjectsApi* | [**projectsProjectIdProjectFilesProjectFileIdGet**](docs/ProjectsApi.md#projectsProjectIdProjectFilesProjectFileIdGet) | **GET** /projects/{project_id}/project_files/{project_file_id}/ | Show project file
*ProjectsApi* | [**projectsProjectIdProjectFilesProjectFileIdPut**](docs/ProjectsApi.md#projectsProjectIdProjectFilesProjectFileIdPut) | **PUT** /projects/{project_id}/project_files/{project_file_id}/ | Edit project file
*ProjectsApi* | [**projectsProjectIdPut**](docs/ProjectsApi.md#projectsProjectIdPut) | **PUT** /projects/{project_id} | Edit a project
*ProjectsApi* | [**projectsProjectIdSendBulkPdfPost**](docs/ProjectsApi.md#projectsProjectIdSendBulkPdfPost) | **POST** /projects/{project_id}/send_bulk_pdf | Send bulk forms pdf by email
*ProjectsApi* | [**projectsProjectIdUsersGet**](docs/ProjectsApi.md#projectsProjectIdUsersGet) | **GET** /projects/{project_id}/users/ | Show list of users added to project
*ProjectsApi* | [**projectsProjectIdUsersPost**](docs/ProjectsApi.md#projectsProjectIdUsersPost) | **POST** /projects/{project_id}/users/ | Add user to project
*ProjectsApi* | [**projectsProjectIdUsersUserIdDelete**](docs/ProjectsApi.md#projectsProjectIdUsersUserIdDelete) | **DELETE** /projects/{project_id}/users/{user_id} | Delete user from project
*ProjectsApi* | [**projectsProjectIdUsersUserIdGet**](docs/ProjectsApi.md#projectsProjectIdUsersUserIdGet) | **GET** /projects/{project_id}/users/{user_id} | View specific user assigned to project
*RejectionReasonsApi* | [**overviewRejectionReasonsGet**](docs/RejectionReasonsApi.md#overviewRejectionReasonsGet) | **GET** /overview/rejection_reasons | Get a statistics data for rejection reasons
*ReportsApi* | [**reportsGet**](docs/ReportsApi.md#reportsGet) | **GET** /reports | 
*RolesApi* | [**rolesGet**](docs/RolesApi.md#rolesGet) | **GET** /roles | Get a list of roles
*StockLocationsApi* | [**stockLocationsGet**](docs/StockLocationsApi.md#stockLocationsGet) | **GET** /stock_locations | List stock_locations
*StockLocationsApi* | [**stockLocationsLocationIdDelete**](docs/StockLocationsApi.md#stockLocationsLocationIdDelete) | **DELETE** /stock_locations/{location_id} | Delete location
*StockLocationsApi* | [**stockLocationsLocationIdGet**](docs/StockLocationsApi.md#stockLocationsLocationIdGet) | **GET** /stock_locations/{location_id} | View single location
*StockLocationsApi* | [**stockLocationsLocationIdPut**](docs/StockLocationsApi.md#stockLocationsLocationIdPut) | **PUT** /stock_locations/{location_id} | Edit location
*StockLocationsApi* | [**stockLocationsPost**](docs/StockLocationsApi.md#stockLocationsPost) | **POST** /stock_locations | Add new stock_locations
*TimeEntriesApi* | [**timeEntriesGet**](docs/TimeEntriesApi.md#timeEntriesGet) | **GET** /time_entries | List time entries
*TimeEntriesApi* | [**timeEntriesPost**](docs/TimeEntriesApi.md#timeEntriesPost) | **POST** /time_entries | Add new time entry
*TimeEntriesApi* | [**timeEntriesTimeEntryIdDelete**](docs/TimeEntriesApi.md#timeEntriesTimeEntryIdDelete) | **DELETE** /time_entries/{time_entry_id} | Delete time entry
*TimeEntriesApi* | [**timeEntriesTimeEntryIdGet**](docs/TimeEntriesApi.md#timeEntriesTimeEntryIdGet) | **GET** /time_entries/{time_entry_id} | View time entry
*TimeEntriesApi* | [**timeEntriesTimeEntryIdPut**](docs/TimeEntriesApi.md#timeEntriesTimeEntryIdPut) | **PUT** /time_entries/{time_entry_id} | Edit time entry
*TimeEntryIntervalsApi* | [**timeEntryIntervalsGet**](docs/TimeEntryIntervalsApi.md#timeEntryIntervalsGet) | **GET** /time_entry_intervals | List possible time entry intervals
*TimeEntryIntervalsApi* | [**timeEntryIntervalsTimeEntryIntervalIdGet**](docs/TimeEntryIntervalsApi.md#timeEntryIntervalsTimeEntryIntervalIdGet) | **GET** /time_entry_intervals/{time_entry_interval_id} | View time entry interval
*TimeEntryRateApi* | [**timeEntryRatesTimeEntryRateIdDelete**](docs/TimeEntryRateApi.md#timeEntryRatesTimeEntryRateIdDelete) | **DELETE** /time_entry_rates/{time_entry_rate_id} | Delete time entry rate
*TimeEntryRatesApi* | [**timeEntryRatesGet**](docs/TimeEntryRatesApi.md#timeEntryRatesGet) | **GET** /time_entry_rates | List time entry rates
*TimeEntryRatesApi* | [**timeEntryRatesPost**](docs/TimeEntryRatesApi.md#timeEntryRatesPost) | **POST** /time_entry_rates | Add new time entry rate
*TimeEntryRatesApi* | [**timeEntryRatesTimeEntryRateIdGet**](docs/TimeEntryRatesApi.md#timeEntryRatesTimeEntryRateIdGet) | **GET** /time_entry_rates/{time_entry_rate_id} | View time entry rate
*TimeEntryRatesApi* | [**timeEntryRatesTimeEntryRateIdPut**](docs/TimeEntryRatesApi.md#timeEntryRatesTimeEntryRateIdPut) | **PUT** /time_entry_rates/{time_entry_rate_id} | Edit time entry rate
*TimeEntryRuleGroupsApi* | [**timeEntryRuleGroupsGet**](docs/TimeEntryRuleGroupsApi.md#timeEntryRuleGroupsGet) | **GET** /time_entry_rule_groups | List time entry rule groups
*TimeEntryTypesApi* | [**bulkActivateTimeEntryTypes**](docs/TimeEntryTypesApi.md#bulkActivateTimeEntryTypes) | **POST** /time_entry_types/bulkActivate | Bulk activate time entry types
*TimeEntryTypesApi* | [**bulkDeactivateTimeEntryTypes**](docs/TimeEntryTypesApi.md#bulkDeactivateTimeEntryTypes) | **POST** /time_entry_types/bulkDeactivate | Bulk deactivate time entry types
*TimeEntryTypesApi* | [**bulkDeleteTimeEntryTypes**](docs/TimeEntryTypesApi.md#bulkDeleteTimeEntryTypes) | **DELETE** /time_entry_types/bulkDelete | Bulk delete time entry types
*TimeEntryTypesApi* | [**timeEntryTypesGet**](docs/TimeEntryTypesApi.md#timeEntryTypesGet) | **GET** /time_entry_types | List time entries types
*TimeEntryTypesApi* | [**timeEntryTypesPost**](docs/TimeEntryTypesApi.md#timeEntryTypesPost) | **POST** /time_entry_types | Add new time entry type
*TimeEntryTypesApi* | [**timeEntryTypesTimeEntryTypeIdDelete**](docs/TimeEntryTypesApi.md#timeEntryTypesTimeEntryTypeIdDelete) | **DELETE** /time_entry_types/{time_entry_type_id} | Delete time entry type
*TimeEntryTypesApi* | [**timeEntryTypesTimeEntryTypeIdGet**](docs/TimeEntryTypesApi.md#timeEntryTypesTimeEntryTypeIdGet) | **GET** /time_entry_types/{time_entry_type_id} | View time entry type
*TimeEntryTypesApi* | [**timeEntryTypesTimeEntryTypeIdPut**](docs/TimeEntryTypesApi.md#timeEntryTypesTimeEntryTypeIdPut) | **PUT** /time_entry_types/{time_entry_type_id} | Edit time entry type
*TimeEntryUnitTypesApi* | [**timeEntryUnitTypesGet**](docs/TimeEntryUnitTypesApi.md#timeEntryUnitTypesGet) | **GET** /time_entry_unit_types | List possible time entry unit types
*TimeEntryUnitTypesApi* | [**timeEntryUnitTypesTimeEntryUnitTypeIdGet**](docs/TimeEntryUnitTypesApi.md#timeEntryUnitTypesTimeEntryUnitTypeIdGet) | **GET** /time_entry_unit_types/{time_entry_unit_type_id} | View time entry unit type
*TimeEntryValueTypesApi* | [**timeEntryValueTypesGet**](docs/TimeEntryValueTypesApi.md#timeEntryValueTypesGet) | **GET** /time_entry_value_types | List possible time entry value types
*TimeEntryValueTypesApi* | [**timeEntryValueTypesTimeEntryValueTypeIdGet**](docs/TimeEntryValueTypesApi.md#timeEntryValueTypesTimeEntryValueTypeIdGet) | **GET** /time_entry_value_types/{time_entry_value_type_id} | View time entry value type
*UserCustomFieldAttributesApi* | [**userCustomFieldAttributesGet**](docs/UserCustomFieldAttributesApi.md#userCustomFieldAttributesGet) | **GET** /user_custom_field_attributes | Get a list of user custom field attributes
*UserCustomFieldAttributesApi* | [**userCustomFieldAttributesUserCustomFieldAttributeIdGet**](docs/UserCustomFieldAttributesApi.md#userCustomFieldAttributesUserCustomFieldAttributeIdGet) | **GET** /user_custom_field_attributes/{user_custom_field_attribute_id} | Details of 1 user custom field attribute
*UserCustomFieldValueApi* | [**usersUserIdUserCustomFieldValueGet**](docs/UserCustomFieldValueApi.md#usersUserIdUserCustomFieldValueGet) | **GET** /users/{user_id}/user_custom_field_value | Get a list of user custom field values
*UserCustomFieldValueApi* | [**usersUserIdUserCustomFieldValueUserCustomFieldValueIdGet**](docs/UserCustomFieldValueApi.md#usersUserIdUserCustomFieldValueUserCustomFieldValueIdGet) | **GET** /users/{user_id}/user_custom_field_value/{user_custom_field_value_id} | Get a single record of user custom field value
*UserCustomFieldValueApi* | [**usersUserIdUserCustomFieldValueUserCustomFieldValueIdPut**](docs/UserCustomFieldValueApi.md#usersUserIdUserCustomFieldValueUserCustomFieldValueIdPut) | **PUT** /users/{user_id}/user_custom_field_value/{user_custom_field_value_id} | Update a single record of user custom field value
*UsersApi* | [**usersBulkActivate**](docs/UsersApi.md#usersBulkActivate) | **POST** /users/bulkActivate | Activate multiple users
*UsersApi* | [**usersBulkDeactivate**](docs/UsersApi.md#usersBulkDeactivate) | **POST** /users/bulkDeactivate | Deactivate multiple users
*UsersApi* | [**usersGet**](docs/UsersApi.md#usersGet) | **GET** /users | Get list of users in company
*UsersApi* | [**usersPost**](docs/UsersApi.md#usersPost) | **POST** /users | Add user to company
*UsersApi* | [**usersResendWelcomeSmsGet**](docs/UsersApi.md#usersResendWelcomeSmsGet) | **GET** /users/resendWelcomeSms | Resend Welcome SMS to the user
*UsersApi* | [**usersUserIdDelete**](docs/UsersApi.md#usersUserIdDelete) | **DELETE** /users/{user_id} | Delete user
*UsersApi* | [**usersUserIdGet**](docs/UsersApi.md#usersUserIdGet) | **GET** /users/{user_id} | View user
*UsersApi* | [**usersUserIdIntegrationSettingsGet**](docs/UsersApi.md#usersUserIdIntegrationSettingsGet) | **GET** /users/{user_id}/integration_settings | Get a list of user integration settings
*UsersApi* | [**usersUserIdIntegrationSettingsIntegrationSettingsUserIdDelete**](docs/UsersApi.md#usersUserIdIntegrationSettingsIntegrationSettingsUserIdDelete) | **DELETE** /users/{user_id}/integration_settings/{integration_settings_user_id} | Delete a user integration setting
*UsersApi* | [**usersUserIdIntegrationSettingsIntegrationSettingsUserIdGet**](docs/UsersApi.md#usersUserIdIntegrationSettingsIntegrationSettingsUserIdGet) | **GET** /users/{user_id}/integration_settings/{integration_settings_user_id} | Get a user integration setting
*UsersApi* | [**usersUserIdIntegrationSettingsIntegrationSettingsUserIdPut**](docs/UsersApi.md#usersUserIdIntegrationSettingsIntegrationSettingsUserIdPut) | **PUT** /users/{user_id}/integration_settings/{integration_settings_user_id} | Edit a user integration setting
*UsersApi* | [**usersUserIdIntegrationSettingsPost**](docs/UsersApi.md#usersUserIdIntegrationSettingsPost) | **POST** /users/{user_id}/integration_settings | Add a user integration setting
*UsersApi* | [**usersUserIdPut**](docs/UsersApi.md#usersUserIdPut) | **PUT** /users/{user_id} | Edit user
*UsersApi* | [**usersUserIdUploadImagePost**](docs/UsersApi.md#usersUserIdUploadImagePost) | **POST** /users/{user_id}/uploadImage | Upload a new image to a user
*VendorProductPriceFilesApi* | [**vendorProductPriceFilesGet**](docs/VendorProductPriceFilesApi.md#vendorProductPriceFilesGet) | **GET** /vendor_product_price_files | Get a list of price files
*VendorProductPriceFilesApi* | [**vendorProductPriceFilesPost**](docs/VendorProductPriceFilesApi.md#vendorProductPriceFilesPost) | **POST** /vendor_product_price_files | Upload a vendor price file
*VendorProductPriceFilesApi* | [**vendorProductPriceFilesVendorProductPriceFileIdGet**](docs/VendorProductPriceFilesApi.md#vendorProductPriceFilesVendorProductPriceFileIdGet) | **GET** /vendor_product_price_files/{vendor_product_price_file_id} | Get a single price file
*VendorProductsApi* | [**vendorProductsGet**](docs/VendorProductsApi.md#vendorProductsGet) | **GET** /vendor_products | List vendor products
*VendorProductsApi* | [**vendorProductsVendorProductIdGet**](docs/VendorProductsApi.md#vendorProductsVendorProductIdGet) | **GET** /vendor_products/{vendor_product_id} | View single vendor product
*VendorsApi* | [**addVendor**](docs/VendorsApi.md#addVendor) | **POST** /vendors | Add a new vendor
*VendorsApi* | [**editVendor**](docs/VendorsApi.md#editVendor) | **PUT** /vendors/{vendor_id} | Edit a vendor
*VendorsApi* | [**getVendor**](docs/VendorsApi.md#getVendor) | **GET** /vendors/{vendor_id} | Get a vendor
*VendorsApi* | [**getVendorsList**](docs/VendorsApi.md#getVendorsList) | **GET** /vendors | Get a list of vendors
*VendorsApi* | [**vendorsVendorIdDelete**](docs/VendorsApi.md#vendorsVendorIdDelete) | **DELETE** /vendors/{vendor_id} | Delete a vendor
*WagesApi* | [**wagesDownloadSalaryFileGet**](docs/WagesApi.md#wagesDownloadSalaryFileGet) | **GET** /wages/downloadSalaryFile | Download salary file
*WallCommentsApi* | [**wallCommentsPost**](docs/WallCommentsApi.md#wallCommentsPost) | **POST** /wall_comments | Add wall comment
*WallCommentsApi* | [**wallCommentsWallCommentIdGet**](docs/WallCommentsApi.md#wallCommentsWallCommentIdGet) | **GET** /wall_comments/{wall_comment_id} | View wall comment
*WallPostsApi* | [**wallPostsGet**](docs/WallPostsApi.md#wallPostsGet) | **GET** /wall_posts | View list of wall posts
*WallPostsApi* | [**wallPostsPost**](docs/WallPostsApi.md#wallPostsPost) | **POST** /wall_posts | Add a wall post
*WallPostsApi* | [**wallPostsWallPostIdGet**](docs/WallPostsApi.md#wallPostsWallPostIdGet) | **GET** /wall_posts/{wall_post_id} | View wall post
*WallPostsApi* | [**wallPostsWallPostIdWallCommentsGet**](docs/WallPostsApi.md#wallPostsWallPostIdWallCommentsGet) | **GET** /wall_posts/{wall_post_id}/wall_comments | See wall comments to a wall post


## Documentation for Models

 - [ActivitiesGet200Response](docs/ActivitiesGet200Response.md)
 - [ActivitiesPostRequest](docs/ActivitiesPostRequest.md)
 - [Activity](docs/Activity.md)
 - [AddCompaniesVendorRequest](docs/AddCompaniesVendorRequest.md)
 - [AddContactPersonRequest](docs/AddContactPersonRequest.md)
 - [AddDefaultProjectStatusesError](docs/AddDefaultProjectStatusesError.md)
 - [AddDefaultProjectStatusesSuccess](docs/AddDefaultProjectStatusesSuccess.md)
 - [AddVendorRequest](docs/AddVendorRequest.md)
 - [BadRequestResponse](docs/BadRequestResponse.md)
 - [BadRequestResponseData](docs/BadRequestResponseData.md)
 - [BulkActionRequestBody](docs/BulkActionRequestBody.md)
 - [BulkEditIntegrationSettingsUsersItemsRequestBody](docs/BulkEditIntegrationSettingsUsersItemsRequestBody.md)
 - [BulkEditIntegrationSettingsUsersRequestBody](docs/BulkEditIntegrationSettingsUsersRequestBody.md)
 - [CitiesCityIdGet200Response](docs/CitiesCityIdGet200Response.md)
 - [CitiesGet200Response](docs/CitiesGet200Response.md)
 - [City](docs/City.md)
 - [ClockingRecord](docs/ClockingRecord.md)
 - [ClockingRecordsCheckoutPost201Response](docs/ClockingRecordsCheckoutPost201Response.md)
 - [ClockingRecordsClockingRecordIdDelete200Response](docs/ClockingRecordsClockingRecordIdDelete200Response.md)
 - [ClockingRecordsClockingRecordIdGet200Response](docs/ClockingRecordsClockingRecordIdGet200Response.md)
 - [ClockingRecordsClockingRecordIdPut200Response](docs/ClockingRecordsClockingRecordIdPut200Response.md)
 - [ClockingRecordsGet200Response](docs/ClockingRecordsGet200Response.md)
 - [ClockingRecordsPost201Response](docs/ClockingRecordsPost201Response.md)
 - [ClockingRecordsPost201ResponseData](docs/ClockingRecordsPost201ResponseData.md)
 - [ClockingRecordsPostRequest](docs/ClockingRecordsPostRequest.md)
 - [CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response](docs/CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response.md)
 - [CompaniesCompanyIdCompaniesIntegrationFeatureSettingsPostRequest](docs/CompaniesCompanyIdCompaniesIntegrationFeatureSettingsPostRequest.md)
 - [CompaniesCompanyIdFormTemplatesGet200Response](docs/CompaniesCompanyIdFormTemplatesGet200Response.md)
 - [CompaniesCompanyIdGet200Response](docs/CompaniesCompanyIdGet200Response.md)
 - [CompaniesCompanyIdIntegrationFeatureSettingsGet200Response](docs/CompaniesCompanyIdIntegrationFeatureSettingsGet200Response.md)
 - [CompaniesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet200Response](docs/CompaniesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet200Response.md)
 - [CompaniesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet200Response](docs/CompaniesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet200Response.md)
 - [CompaniesCompanyIdIntegrationSettingsGet200Response](docs/CompaniesCompanyIdIntegrationSettingsGet200Response.md)
 - [CompaniesCompanyIdIntegrationSettingsPostRequest](docs/CompaniesCompanyIdIntegrationSettingsPostRequest.md)
 - [CompaniesCompanyIdPriceMarginsPriceMarginsIdGet200Response](docs/CompaniesCompanyIdPriceMarginsPriceMarginsIdGet200Response.md)
 - [CompaniesCompanyIdPriceMarginsPriceMarginsIdPostRequest](docs/CompaniesCompanyIdPriceMarginsPriceMarginsIdPostRequest.md)
 - [CompaniesFormTemplates](docs/CompaniesFormTemplates.md)
 - [CompaniesGet200Response](docs/CompaniesGet200Response.md)
 - [CompaniesIntegrationFeatureSetting](docs/CompaniesIntegrationFeatureSetting.md)
 - [CompaniesIntegrationSetting](docs/CompaniesIntegrationSetting.md)
 - [CompaniesSubscriptionSelfServiceGet200Response](docs/CompaniesSubscriptionSelfServiceGet200Response.md)
 - [CompaniesVendor](docs/CompaniesVendor.md)
 - [Company](docs/Company.md)
 - [CompanyPriceMargins](docs/CompanyPriceMargins.md)
 - [CompanySettings](docs/CompanySettings.md)
 - [Contact](docs/Contact.md)
 - [ContactCustomFieldAttribute](docs/ContactCustomFieldAttribute.md)
 - [ContactCustomFieldAttributesContactCustomFieldAttributeIdGet200Response](docs/ContactCustomFieldAttributesContactCustomFieldAttributeIdGet200Response.md)
 - [ContactCustomFieldAttributesGet200Response](docs/ContactCustomFieldAttributesGet200Response.md)
 - [ContactCustomFieldValue](docs/ContactCustomFieldValue.md)
 - [ContactPerson](docs/ContactPerson.md)
 - [ContactType](docs/ContactType.md)
 - [ContactTypesContactTypeIdGet200Response](docs/ContactTypesContactTypeIdGet200Response.md)
 - [ContactTypesGet200Response](docs/ContactTypesGet200Response.md)
 - [ContactsContactIdContactCustomFieldValuesGet200Response](docs/ContactsContactIdContactCustomFieldValuesGet200Response.md)
 - [ContactsContactIdGet200Response](docs/ContactsContactIdGet200Response.md)
 - [ContactsGet200Response](docs/ContactsGet200Response.md)
 - [ContactsPostRequest](docs/ContactsPostRequest.md)
 - [ContactsPostRequestContactTypes](docs/ContactsPostRequestContactTypes.md)
 - [Countries](docs/Countries.md)
 - [CountriesCountryIdGet200Response](docs/CountriesCountryIdGet200Response.md)
 - [CountriesGet200Response](docs/CountriesGet200Response.md)
 - [CreateSuccessResponse](docs/CreateSuccessResponse.md)
 - [CurrenciesCurrencyIdGet200Response](docs/CurrenciesCurrencyIdGet200Response.md)
 - [CurrenciesGet200Response](docs/CurrenciesGet200Response.md)
 - [Currency](docs/Currency.md)
 - [DrivingType](docs/DrivingType.md)
 - [Email](docs/Email.md)
 - [EmployeeHoursGet200Response](docs/EmployeeHoursGet200Response.md)
 - [EmployeeHoursGet200ResponseDataInner](docs/EmployeeHoursGet200ResponseDataInner.md)
 - [EmptySuccessResponse](docs/EmptySuccessResponse.md)
 - [ErrorNotFound](docs/ErrorNotFound.md)
 - [ErrorNotFoundData](docs/ErrorNotFoundData.md)
 - [ErrorValidation](docs/ErrorValidation.md)
 - [ErrorValidationData](docs/ErrorValidationData.md)
 - [Event](docs/Event.md)
 - [EventsEventIdGet200Response](docs/EventsEventIdGet200Response.md)
 - [EventsGet200Response](docs/EventsGet200Response.md)
 - [EventsIsUserFreeGet200Response](docs/EventsIsUserFreeGet200Response.md)
 - [EventsPostRequest](docs/EventsPostRequest.md)
 - [Expense](docs/Expense.md)
 - [ExpenseFile](docs/ExpenseFile.md)
 - [ExpenseFilesExpenseFileIdGet200Response](docs/ExpenseFilesExpenseFileIdGet200Response.md)
 - [ExpenseFilesExpenseFileIdPut200Response](docs/ExpenseFilesExpenseFileIdPut200Response.md)
 - [ExpenseFilesGet200Response](docs/ExpenseFilesGet200Response.md)
 - [ExpenseLine](docs/ExpenseLine.md)
 - [ExpenseLinesExpenseLineIdGet200Response](docs/ExpenseLinesExpenseLineIdGet200Response.md)
 - [ExpenseLinesGet200Response](docs/ExpenseLinesGet200Response.md)
 - [ExpenseLinesPostRequest](docs/ExpenseLinesPostRequest.md)
 - [ExpensesExpenseIdGet200Response](docs/ExpensesExpenseIdGet200Response.md)
 - [ExpensesGet200Response](docs/ExpensesGet200Response.md)
 - [ExpensesHighestAmountGet200Response](docs/ExpensesHighestAmountGet200Response.md)
 - [ExpensesHighestAmountGet200ResponseDataInner](docs/ExpensesHighestAmountGet200ResponseDataInner.md)
 - [ExpensesPostRequest](docs/ExpensesPostRequest.md)
 - [FinancialStatisticsWorkingHoursGet200Response](docs/FinancialStatisticsWorkingHoursGet200Response.md)
 - [FinancialStatisticsWorkingHoursGet200ResponseTimeEntriesInner](docs/FinancialStatisticsWorkingHoursGet200ResponseTimeEntriesInner.md)
 - [ForbiddenError](docs/ForbiddenError.md)
 - [ForbiddenErrorData](docs/ForbiddenErrorData.md)
 - [Form](docs/Form.md)
 - [FormField](docs/FormField.md)
 - [FormFieldType](docs/FormFieldType.md)
 - [FormFieldTypesFormFieldTypeIdGet200Response](docs/FormFieldTypesFormFieldTypeIdGet200Response.md)
 - [FormFieldTypesGet200Response](docs/FormFieldTypesGet200Response.md)
 - [FormFieldsFormFieldIdGet200Response](docs/FormFieldsFormFieldIdGet200Response.md)
 - [FormFieldsPostRequest](docs/FormFieldsPostRequest.md)
 - [FormTemplate](docs/FormTemplate.md)
 - [FormTemplatesFormTemplateIdGet200Response](docs/FormTemplatesFormTemplateIdGet200Response.md)
 - [FormTemplatesGet200Response](docs/FormTemplatesGet200Response.md)
 - [FormsFormIdGet200Response](docs/FormsFormIdGet200Response.md)
 - [FormsGet200Response](docs/FormsGet200Response.md)
 - [FormsPostRequest](docs/FormsPostRequest.md)
 - [GetCompaiesVendorsList200Response](docs/GetCompaiesVendorsList200Response.md)
 - [GetCompaniesVendor200Response](docs/GetCompaniesVendor200Response.md)
 - [GetCompaniesVendorsExpenseStatistics200Response](docs/GetCompaniesVendorsExpenseStatistics200Response.md)
 - [GetCompaniesVendorsExpenseStatistics200ResponseDataInner](docs/GetCompaniesVendorsExpenseStatistics200ResponseDataInner.md)
 - [GetCompaniesVendorsExpenseStatistics200ResponseDataInnerLastMonthInner](docs/GetCompaniesVendorsExpenseStatistics200ResponseDataInnerLastMonthInner.md)
 - [GetCompaySettingsList200Response](docs/GetCompaySettingsList200Response.md)
 - [GetContactPerson200Response](docs/GetContactPerson200Response.md)
 - [GetContactPersonsList200Response](docs/GetContactPersonsList200Response.md)
 - [GetDrivingTypes200Response](docs/GetDrivingTypes200Response.md)
 - [GetExpensesSalesPrice200Response](docs/GetExpensesSalesPrice200Response.md)
 - [GetFinancialStatistics200Response](docs/GetFinancialStatistics200Response.md)
 - [GetFinancialStatistics200ResponseData](docs/GetFinancialStatistics200ResponseData.md)
 - [GetFinancialStatisticsOverview200Response](docs/GetFinancialStatisticsOverview200Response.md)
 - [GetFinancialStatisticsOverview200ResponseData](docs/GetFinancialStatisticsOverview200ResponseData.md)
 - [GetIntegrationsList200Response](docs/GetIntegrationsList200Response.md)
 - [GetInvoiceFiles200Response](docs/GetInvoiceFiles200Response.md)
 - [GetInvoicedAmount200Response](docs/GetInvoicedAmount200Response.md)
 - [GetMargin200Response](docs/GetMargin200Response.md)
 - [GetMaterialRentalsCostPrice200Response](docs/GetMaterialRentalsCostPrice200Response.md)
 - [GetOneInvoiceEmails200Response](docs/GetOneInvoiceEmails200Response.md)
 - [GetOneInvoiceFiles200Response](docs/GetOneInvoiceFiles200Response.md)
 - [GetProductsCostPrice200Response](docs/GetProductsCostPrice200Response.md)
 - [GetVendor200Response](docs/GetVendor200Response.md)
 - [GetVendorsList200Response](docs/GetVendorsList200Response.md)
 - [IntegrationFeatureSetting](docs/IntegrationFeatureSetting.md)
 - [IntegrationSettingsUser](docs/IntegrationSettingsUser.md)
 - [IntegrationSettingsUsers](docs/IntegrationSettingsUsers.md)
 - [IntegrationsBillysAuthenticatePost200Response](docs/IntegrationsBillysAuthenticatePost200Response.md)
 - [IntegrationsProductsSyncGet200Response](docs/IntegrationsProductsSyncGet200Response.md)
 - [Invoice](docs/Invoice.md)
 - [InvoiceFile](docs/InvoiceFile.md)
 - [InvoiceLine](docs/InvoiceLine.md)
 - [InvoiceLineText](docs/InvoiceLineText.md)
 - [InvoiceLineTextTemplate](docs/InvoiceLineTextTemplate.md)
 - [InvoiceLineTextTemplateGet200Response](docs/InvoiceLineTextTemplateGet200Response.md)
 - [InvoiceLineTextTemplateInvoiceLineTextTemplateIdGet200Response](docs/InvoiceLineTextTemplateInvoiceLineTextTemplateIdGet200Response.md)
 - [InvoiceLinesGet200Response](docs/InvoiceLinesGet200Response.md)
 - [InvoiceLinesInvoiceLineIdGet200Response](docs/InvoiceLinesInvoiceLineIdGet200Response.md)
 - [InvoiceLinesInvoiceLineIdPutRequest](docs/InvoiceLinesInvoiceLineIdPutRequest.md)
 - [InvoiceLinesPostRequest](docs/InvoiceLinesPostRequest.md)
 - [InvoicesGet200Response](docs/InvoicesGet200Response.md)
 - [InvoicesInvoiceIdGet200Response](docs/InvoicesInvoiceIdGet200Response.md)
 - [InvoicesInvoiceIdPutRequest](docs/InvoicesInvoiceIdPutRequest.md)
 - [InvoicesPostRequest](docs/InvoicesPostRequest.md)
 - [MassMessage](docs/MassMessage.md)
 - [MassMessagesUser](docs/MassMessagesUser.md)
 - [MassMessagesUsersGet200Response](docs/MassMessagesUsersGet200Response.md)
 - [MassMessagesUsersMassMessagesUserIdGet200Response](docs/MassMessagesUsersMassMessagesUserIdGet200Response.md)
 - [Material](docs/Material.md)
 - [MaterialRental](docs/MaterialRental.md)
 - [MaterialsGet200Response](docs/MaterialsGet200Response.md)
 - [MaterialsMaterialIdGet200Response](docs/MaterialsMaterialIdGet200Response.md)
 - [MaterialsMaterialIdRentalsCheckoutPostRequest](docs/MaterialsMaterialIdRentalsCheckoutPostRequest.md)
 - [MaterialsMaterialIdRentalsGet200Response](docs/MaterialsMaterialIdRentalsGet200Response.md)
 - [MaterialsMaterialIdRentalsMaterialRentalIdGet200Response](docs/MaterialsMaterialIdRentalsMaterialRentalIdGet200Response.md)
 - [MaterialsMaterialIdRentalsPostRequest](docs/MaterialsMaterialIdRentalsPostRequest.md)
 - [MaterialsPostRequest](docs/MaterialsPostRequest.md)
 - [Offer](docs/Offer.md)
 - [OfferLine](docs/OfferLine.md)
 - [OfferStatus](docs/OfferStatus.md)
 - [OfferStatusesGet200Response](docs/OfferStatusesGet200Response.md)
 - [OfferStatusesOfferStatusIdGet200Response](docs/OfferStatusesOfferStatusIdGet200Response.md)
 - [OfferStatusesPostRequest](docs/OfferStatusesPostRequest.md)
 - [OffersGet200Response](docs/OffersGet200Response.md)
 - [OffersOfferIdChangelogGet200Response](docs/OffersOfferIdChangelogGet200Response.md)
 - [OffersOfferIdGet200Response](docs/OffersOfferIdGet200Response.md)
 - [OffersPostRequest](docs/OffersPostRequest.md)
 - [OverviewRejectionReasonsGet200Response](docs/OverviewRejectionReasonsGet200Response.md)
 - [PaginationDetails](docs/PaginationDetails.md)
 - [PaymentTerm](docs/PaymentTerm.md)
 - [PaymentTermType](docs/PaymentTermType.md)
 - [PaymentTermTypesGet200Response](docs/PaymentTermTypesGet200Response.md)
 - [PaymentTermTypesPaymentTermTypeIdGet200Response](docs/PaymentTermTypesPaymentTermTypeIdGet200Response.md)
 - [PaymentTermsData](docs/PaymentTermsData.md)
 - [PaymentTermsErpGet200Response](docs/PaymentTermsErpGet200Response.md)
 - [PaymentTermsGet200Response](docs/PaymentTermsGet200Response.md)
 - [PaymentTermsPaymentTermIdGet200Response](docs/PaymentTermsPaymentTermIdGet200Response.md)
 - [PingGet200Response](docs/PingGet200Response.md)
 - [PlannedProduct](docs/PlannedProduct.md)
 - [PostDrivingTypesRequest](docs/PostDrivingTypesRequest.md)
 - [Product](docs/Product.md)
 - [ProductVariant](docs/ProductVariant.md)
 - [ProductsGet200Response](docs/ProductsGet200Response.md)
 - [ProductsPostRequest](docs/ProductsPostRequest.md)
 - [ProductsProductIdGet200Response](docs/ProductsProductIdGet200Response.md)
 - [ProductsProductIdVariantsGet200Response](docs/ProductsProductIdVariantsGet200Response.md)
 - [Project](docs/Project.md)
 - [ProjectCustomFieldAttribute](docs/ProjectCustomFieldAttribute.md)
 - [ProjectCustomFieldAttributesGet200Response](docs/ProjectCustomFieldAttributesGet200Response.md)
 - [ProjectCustomFieldAttributesProjectCustomFieldAttributeIdGet200Response](docs/ProjectCustomFieldAttributesProjectCustomFieldAttributeIdGet200Response.md)
 - [ProjectCustomFieldValue](docs/ProjectCustomFieldValue.md)
 - [ProjectStatus](docs/ProjectStatus.md)
 - [ProjectStatusType](docs/ProjectStatusType.md)
 - [ProjectStatusTypesGet200Response](docs/ProjectStatusTypesGet200Response.md)
 - [ProjectStatusesGet200Response](docs/ProjectStatusesGet200Response.md)
 - [ProjectStatusesPostRequest](docs/ProjectStatusesPostRequest.md)
 - [ProjectStatusesProjectStatusIdGet200Response](docs/ProjectStatusesProjectStatusIdGet200Response.md)
 - [ProjectsGet200Response](docs/ProjectsGet200Response.md)
 - [ProjectsHasProjectsWithCustomStatusesGet200Response](docs/ProjectsHasProjectsWithCustomStatusesGet200Response.md)
 - [ProjectsPostRequest](docs/ProjectsPostRequest.md)
 - [ProjectsProjectIdAllFilesGet200Response](docs/ProjectsProjectIdAllFilesGet200Response.md)
 - [ProjectsProjectIdGet200Response](docs/ProjectsProjectIdGet200Response.md)
 - [ProjectsProjectIdPutRequest](docs/ProjectsProjectIdPutRequest.md)
 - [ProjectsProjectIdSendBulkPdfPostRequest](docs/ProjectsProjectIdSendBulkPdfPostRequest.md)
 - [ProjectsProjectIdUsersGet200Response](docs/ProjectsProjectIdUsersGet200Response.md)
 - [ProjectsProjectIdUsersPostRequest](docs/ProjectsProjectIdUsersPostRequest.md)
 - [ProjectsProjectIdUsersUserIdGet200Response](docs/ProjectsProjectIdUsersUserIdGet200Response.md)
 - [Role](docs/Role.md)
 - [RolesGet200Response](docs/RolesGet200Response.md)
 - [Sender](docs/Sender.md)
 - [SharedProjectContact](docs/SharedProjectContact.md)
 - [SharedProjectVendor](docs/SharedProjectVendor.md)
 - [StockLocation](docs/StockLocation.md)
 - [StockLocationsGet200Response](docs/StockLocationsGet200Response.md)
 - [StockLocationsLocationIdGet200Response](docs/StockLocationsLocationIdGet200Response.md)
 - [StockLocationsPostRequest](docs/StockLocationsPostRequest.md)
 - [SubscriptionSelfServiceRequestBody](docs/SubscriptionSelfServiceRequestBody.md)
 - [TimeEntriesGet200Response](docs/TimeEntriesGet200Response.md)
 - [TimeEntriesPostRequest](docs/TimeEntriesPostRequest.md)
 - [TimeEntriesTimeEntryIdGet200Response](docs/TimeEntriesTimeEntryIdGet200Response.md)
 - [TimeEntry](docs/TimeEntry.md)
 - [TimeEntryInterval](docs/TimeEntryInterval.md)
 - [TimeEntryIntervalsGet200Response](docs/TimeEntryIntervalsGet200Response.md)
 - [TimeEntryIntervalsTimeEntryIntervalIdGet200Response](docs/TimeEntryIntervalsTimeEntryIntervalIdGet200Response.md)
 - [TimeEntryRate](docs/TimeEntryRate.md)
 - [TimeEntryRatesGet200Response](docs/TimeEntryRatesGet200Response.md)
 - [TimeEntryRatesTimeEntryRateIdGet200Response](docs/TimeEntryRatesTimeEntryRateIdGet200Response.md)
 - [TimeEntryRuleGroup](docs/TimeEntryRuleGroup.md)
 - [TimeEntryRuleGroupsGet200Response](docs/TimeEntryRuleGroupsGet200Response.md)
 - [TimeEntryType](docs/TimeEntryType.md)
 - [TimeEntryTypesGet200Response](docs/TimeEntryTypesGet200Response.md)
 - [TimeEntryTypesPostRequest](docs/TimeEntryTypesPostRequest.md)
 - [TimeEntryTypesTimeEntryTypeIdGet200Response](docs/TimeEntryTypesTimeEntryTypeIdGet200Response.md)
 - [TimeEntryUnitType](docs/TimeEntryUnitType.md)
 - [TimeEntryUnitTypesGet200Response](docs/TimeEntryUnitTypesGet200Response.md)
 - [TimeEntryUnitTypesTimeEntryUnitTypeIdGet200Response](docs/TimeEntryUnitTypesTimeEntryUnitTypeIdGet200Response.md)
 - [TimeEntryValueType](docs/TimeEntryValueType.md)
 - [TimeEntryValueTypesGet200Response](docs/TimeEntryValueTypesGet200Response.md)
 - [TimeEntryValueTypesTimeEntryValueTypeIdGet200Response](docs/TimeEntryValueTypesTimeEntryValueTypeIdGet200Response.md)
 - [UnauthorizedError](docs/UnauthorizedError.md)
 - [UnauthorizedErrorData](docs/UnauthorizedErrorData.md)
 - [User](docs/User.md)
 - [UserCustomFieldAttribute](docs/UserCustomFieldAttribute.md)
 - [UserCustomFieldAttributesGet200Response](docs/UserCustomFieldAttributesGet200Response.md)
 - [UserCustomFieldAttributesUserCustomFieldAttributeIdGet200Response](docs/UserCustomFieldAttributesUserCustomFieldAttributeIdGet200Response.md)
 - [UserCustomFieldValue](docs/UserCustomFieldValue.md)
 - [UsersPostRequest](docs/UsersPostRequest.md)
 - [UsersResendWelcomeSmsGet200Response](docs/UsersResendWelcomeSmsGet200Response.md)
 - [UsersResendWelcomeSmsGet200ResponseData](docs/UsersResendWelcomeSmsGet200ResponseData.md)
 - [UsersUserIdIntegrationSettingsGet200Response](docs/UsersUserIdIntegrationSettingsGet200Response.md)
 - [UsersUserIdIntegrationSettingsIntegrationSettingsUserIdGet200Response](docs/UsersUserIdIntegrationSettingsIntegrationSettingsUserIdGet200Response.md)
 - [UsersUserIdUserCustomFieldValueGet200Response](docs/UsersUserIdUserCustomFieldValueGet200Response.md)
 - [UsersUserIdUserCustomFieldValueUserCustomFieldValueIdGet200Response](docs/UsersUserIdUserCustomFieldValueUserCustomFieldValueIdGet200Response.md)
 - [UsersUserIdUserCustomFieldValueUserCustomFieldValueIdPut200Response](docs/UsersUserIdUserCustomFieldValueUserCustomFieldValueIdPut200Response.md)
 - [Vendor](docs/Vendor.md)
 - [VendorProduct](docs/VendorProduct.md)
 - [VendorProductPriceFile](docs/VendorProductPriceFile.md)
 - [VendorProductPriceFilesGet200Response](docs/VendorProductPriceFilesGet200Response.md)
 - [VendorProductPriceFilesVendorProductPriceFileIdGet200Response](docs/VendorProductPriceFilesVendorProductPriceFileIdGet200Response.md)
 - [VendorProductPriceFilesVendorProductPriceFileIdGet200ResponseData](docs/VendorProductPriceFilesVendorProductPriceFileIdGet200ResponseData.md)
 - [VendorProductsGet200Response](docs/VendorProductsGet200Response.md)
 - [VendorProductsVendorProductIdGet200Response](docs/VendorProductsVendorProductIdGet200Response.md)
 - [WallComment](docs/WallComment.md)
 - [WallCommentsPostRequest](docs/WallCommentsPostRequest.md)
 - [WallCommentsWallCommentIdGet200Response](docs/WallCommentsWallCommentIdGet200Response.md)
 - [WallPost](docs/WallPost.md)
 - [WallPostsGet200Response](docs/WallPostsGet200Response.md)
 - [WallPostsPostRequest](docs/WallPostsPostRequest.md)
 - [WallPostsWallPostIdGet200Response](docs/WallPostsWallPostIdGet200Response.md)
 - [WallPostsWallPostIdWallCommentsGet200Response](docs/WallPostsWallPostIdWallCommentsGet200Response.md)


<a id="documentation-for-authorization"></a>
## Documentation for Authorization


Authentication schemes defined for the API:
<a id="X-Auth-Token"></a>
### X-Auth-Token

- **Type**: API key
- **API key parameter name**: X-Auth-Token
- **Location**: HTTP header

<a id="api_key"></a>
### api_key

- **Type**: API key
- **API key parameter name**: api_token
- **Location**: URL query string


## Recommendation

It's recommended to create an instance of `ApiClient` per thread in a multithreaded environment to avoid any potential issues.

## Author



