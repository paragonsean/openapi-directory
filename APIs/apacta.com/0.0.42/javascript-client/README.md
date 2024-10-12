# apacta

Apacta - JavaScript client for apacta
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
This SDK is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.0.42
- Package version: 0.0.42
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.JavascriptClientCodegen

## Installation

### For [Node.js](https://nodejs.org/)

#### npm

To publish the library as a [npm](https://www.npmjs.com/), please follow the procedure in ["Publishing npm packages"](https://docs.npmjs.com/getting-started/publishing-npm-packages).

Then install it via:

```shell
npm install apacta --save
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

To use the link you just defined in your project, switch to the directory you want to use your apacta from, and run:

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
var Apacta = require('apacta');


var api = new Apacta.ActivitiesApi()
var activityId = "activityId_example"; // {String} 
var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
api.activitiesActivityIdDelete(activityId, callback);

```

## Documentation for API Endpoints

All URIs are relative to *https://app.apacta.com/api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*Apacta.ActivitiesApi* | [**activitiesActivityIdDelete**](docs/ActivitiesApi.md#activitiesActivityIdDelete) | **DELETE** /activities/{activity_id} | Delete an activity
*Apacta.ActivitiesApi* | [**activitiesActivityIdPut**](docs/ActivitiesApi.md#activitiesActivityIdPut) | **PUT** /activities/{activity_id} | Edit an activity
*Apacta.ActivitiesApi* | [**activitiesBulkDeleteDelete**](docs/ActivitiesApi.md#activitiesBulkDeleteDelete) | **DELETE** /activities/bulkDelete | Bulk delete activities
*Apacta.ActivitiesApi* | [**activitiesGet**](docs/ActivitiesApi.md#activitiesGet) | **GET** /activities | Get a list of activities
*Apacta.ActivitiesApi* | [**activitiesPost**](docs/ActivitiesApi.md#activitiesPost) | **POST** /activities | Create an activity
*Apacta.ChangelogApi* | [**offersOfferIdChangelogGet**](docs/ChangelogApi.md#offersOfferIdChangelogGet) | **GET** /offers/{offer_id}/changelog | Get list of changelog history for the offer. Returns offer object with contact and user objects if they are provided
*Apacta.CitiesApi* | [**citiesCityIdGet**](docs/CitiesApi.md#citiesCityIdGet) | **GET** /cities/{city_id} | Get details about one city
*Apacta.CitiesApi* | [**citiesGet**](docs/CitiesApi.md#citiesGet) | **GET** /cities | Get list of cities supported in Apacta
*Apacta.ClockingRecordsApi* | [**clockingRecordsCheckoutPost**](docs/ClockingRecordsApi.md#clockingRecordsCheckoutPost) | **POST** /clocking_records/checkout | Checkout active clocking record for authenticated user
*Apacta.ClockingRecordsApi* | [**clockingRecordsClockingRecordIdDelete**](docs/ClockingRecordsApi.md#clockingRecordsClockingRecordIdDelete) | **DELETE** /clocking_records/{clocking_record_id} | Delete a clocking record
*Apacta.ClockingRecordsApi* | [**clockingRecordsClockingRecordIdGet**](docs/ClockingRecordsApi.md#clockingRecordsClockingRecordIdGet) | **GET** /clocking_records/{clocking_record_id} | Details of 1 clocking_record
*Apacta.ClockingRecordsApi* | [**clockingRecordsClockingRecordIdPut**](docs/ClockingRecordsApi.md#clockingRecordsClockingRecordIdPut) | **PUT** /clocking_records/{clocking_record_id} | Edit a clocking record
*Apacta.ClockingRecordsApi* | [**clockingRecordsGet**](docs/ClockingRecordsApi.md#clockingRecordsGet) | **GET** /clocking_records | Get a list of clocking records
*Apacta.ClockingRecordsApi* | [**clockingRecordsPost**](docs/ClockingRecordsApi.md#clockingRecordsPost) | **POST** /clocking_records | Create clocking record for authenticated user
*Apacta.CompaniesApi* | [**companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGet**](docs/CompaniesApi.md#companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGet) | **GET** /companies/{company_id}/companies_integration_feature_settings/{c_integration_feature_setting_id} | View a company integration feature setting
*Apacta.CompaniesApi* | [**companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPut**](docs/CompaniesApi.md#companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPut) | **PUT** /companies/{company_id}/companies_integration_feature_settings/{c_integration_feature_setting_id} | Edit a company integration feature setting
*Apacta.CompaniesApi* | [**companiesCompanyIdCompaniesIntegrationFeatureSettingsGet**](docs/CompaniesApi.md#companiesCompanyIdCompaniesIntegrationFeatureSettingsGet) | **GET** /companies/{company_id}/companies_integration_feature_settings | List a company integration feature settings
*Apacta.CompaniesApi* | [**companiesCompanyIdCompaniesIntegrationFeatureSettingsPost**](docs/CompaniesApi.md#companiesCompanyIdCompaniesIntegrationFeatureSettingsPost) | **POST** /companies/{company_id}/companies_integration_feature_settings | Add a company integration feature setting
*Apacta.CompaniesApi* | [**companiesCompanyIdFormTemplatesFormTemplateIdDelete**](docs/CompaniesApi.md#companiesCompanyIdFormTemplatesFormTemplateIdDelete) | **DELETE** /companies/{company_id}/form_templates/{form_template_id} | Delete a form template company
*Apacta.CompaniesApi* | [**companiesCompanyIdFormTemplatesFormTemplateIdGet**](docs/CompaniesApi.md#companiesCompanyIdFormTemplatesFormTemplateIdGet) | **GET** /companies/{company_id}/form_templates/{form_template_id} | Get a company form template
*Apacta.CompaniesApi* | [**companiesCompanyIdFormTemplatesGet**](docs/CompaniesApi.md#companiesCompanyIdFormTemplatesGet) | **GET** /companies/{company_id}/form_templates/ | Get a list of company form templates
*Apacta.CompaniesApi* | [**companiesCompanyIdGet**](docs/CompaniesApi.md#companiesCompanyIdGet) | **GET** /companies/{company_id} | Details of 1 company
*Apacta.CompaniesApi* | [**companiesCompanyIdIntegrationFeatureSettingsGet**](docs/CompaniesApi.md#companiesCompanyIdIntegrationFeatureSettingsGet) | **GET** /companies/{company_id}/integration_feature_settings | Get a list of integration feature settings
*Apacta.CompaniesApi* | [**companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet**](docs/CompaniesApi.md#companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet) | **GET** /companies/{company_id}/integration_feature_settings/{integration_feature_setting_id} | Show details of 1 integration feature setting
*Apacta.CompaniesApi* | [**companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDelete**](docs/CompaniesApi.md#companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDelete) | **DELETE** /companies/{company_id}/integration_settings/{companies_integration_setting_id} | Delete a company integration setting
*Apacta.CompaniesApi* | [**companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet**](docs/CompaniesApi.md#companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet) | **GET** /companies/{company_id}/integration_settings/{companies_integration_setting_id} | Get a company integration setting
*Apacta.CompaniesApi* | [**companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPut**](docs/CompaniesApi.md#companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPut) | **PUT** /companies/{company_id}/integration_settings/{companies_integration_setting_id} | Edit a company integration setting
*Apacta.CompaniesApi* | [**companiesCompanyIdIntegrationSettingsGet**](docs/CompaniesApi.md#companiesCompanyIdIntegrationSettingsGet) | **GET** /companies/{company_id}/integration_settings | Get a list of company integration settings
*Apacta.CompaniesApi* | [**companiesCompanyIdIntegrationSettingsPost**](docs/CompaniesApi.md#companiesCompanyIdIntegrationSettingsPost) | **POST** /companies/{company_id}/integration_settings | Add a company integration setting
*Apacta.CompaniesApi* | [**companiesCompanyIdPriceMarginsPriceMarginsIdDelete**](docs/CompaniesApi.md#companiesCompanyIdPriceMarginsPriceMarginsIdDelete) | **DELETE** /companies/{company_id}/price_margins/{price_margins_id} | Delete a company price margin
*Apacta.CompaniesApi* | [**companiesCompanyIdPriceMarginsPriceMarginsIdGet**](docs/CompaniesApi.md#companiesCompanyIdPriceMarginsPriceMarginsIdGet) | **GET** /companies/{company_id}/price_margins/{price_margins_id} | Get a list of company price margins
*Apacta.CompaniesApi* | [**companiesCompanyIdPriceMarginsPriceMarginsIdPost**](docs/CompaniesApi.md#companiesCompanyIdPriceMarginsPriceMarginsIdPost) | **POST** /companies/{company_id}/price_margins/{price_margins_id} | Add a company price margin
*Apacta.CompaniesApi* | [**companiesGet**](docs/CompaniesApi.md#companiesGet) | **GET** /companies | Get a list of companies
*Apacta.CompaniesApi* | [**companiesSubscriptionSelfServiceGet**](docs/CompaniesApi.md#companiesSubscriptionSelfServiceGet) | **GET** /companies/subscription_self_service | URL for subscription selfservice
*Apacta.CompaniesVendorsApi* | [**addCompaniesVendor**](docs/CompaniesVendorsApi.md#addCompaniesVendor) | **POST** /companies_vendors | Add a new companies vendor
*Apacta.CompaniesVendorsApi* | [**bulkCompaniesVendors**](docs/CompaniesVendorsApi.md#bulkCompaniesVendors) | **DELETE** /companies_vendors/bulkDelete | Bulk delete companies vendors
*Apacta.CompaniesVendorsApi* | [**companiesVendorsCompaniesVendorIdDelete**](docs/CompaniesVendorsApi.md#companiesVendorsCompaniesVendorIdDelete) | **DELETE** /companies_vendors/{companies_vendor_id} | Delete a companies vendor
*Apacta.CompaniesVendorsApi* | [**editCompaniesVendor**](docs/CompaniesVendorsApi.md#editCompaniesVendor) | **PUT** /companies_vendors/{companies_vendor_id} | Edit a companies vendor
*Apacta.CompaniesVendorsApi* | [**getCompaiesVendorsList**](docs/CompaniesVendorsApi.md#getCompaiesVendorsList) | **GET** /companies_vendors | Get a list of companies vendors
*Apacta.CompaniesVendorsApi* | [**getCompaniesVendor**](docs/CompaniesVendorsApi.md#getCompaniesVendor) | **GET** /companies_vendors/{companies_vendor_id} | Get a companies vendor
*Apacta.CompaniesVendorsApi* | [**getCompaniesVendorsExpenseStatistics**](docs/CompaniesVendorsApi.md#getCompaniesVendorsExpenseStatistics) | **GET** /companies_vendors/{companies_vendor_id}/expense_statistics | Get companies vendor expense statistics
*Apacta.CompanySettingsApi* | [**getCompaySettingsList**](docs/CompanySettingsApi.md#getCompaySettingsList) | **GET** /company_settings | Get a list of company settings
*Apacta.ContactCustomFieldAttributesApi* | [**contactCustomFieldAttributesContactCustomFieldAttributeIdGet**](docs/ContactCustomFieldAttributesApi.md#contactCustomFieldAttributesContactCustomFieldAttributeIdGet) | **GET** /contact_custom_field_attributes/{contact_custom_field_attribute_id} | Details of 1 contact custom field attribute
*Apacta.ContactCustomFieldAttributesApi* | [**contactCustomFieldAttributesGet**](docs/ContactCustomFieldAttributesApi.md#contactCustomFieldAttributesGet) | **GET** /contact_custom_field_attributes | Get a list of contact custom field attributes
*Apacta.ContactCustomFieldValueApi* | [**contactsContactIdContactCustomFieldValuesGet**](docs/ContactCustomFieldValueApi.md#contactsContactIdContactCustomFieldValuesGet) | **GET** /contacts/{contact_id}/contact_custom_field_values | Get a list of contact custom field values
*Apacta.ContactPersonsApi* | [**addContactPerson**](docs/ContactPersonsApi.md#addContactPerson) | **POST** /contacts/{contact_id}/contact_persons | Add a new contact person to a contact
*Apacta.ContactPersonsApi* | [**contactsContactIdContactPersonsContactPersonIdDelete**](docs/ContactPersonsApi.md#contactsContactIdContactPersonsContactPersonIdDelete) | **DELETE** /contacts/{contact_id}/contact_persons/{contact_person_id} | Delete a contact person
*Apacta.ContactPersonsApi* | [**editContactPerson**](docs/ContactPersonsApi.md#editContactPerson) | **PUT** /contacts/{contact_id}/contact_persons/{contact_person_id} | Edit a contact person
*Apacta.ContactPersonsApi* | [**getContactPerson**](docs/ContactPersonsApi.md#getContactPerson) | **GET** /contacts/{contact_id}/contact_persons/{contact_person_id} | Get a contact person
*Apacta.ContactPersonsApi* | [**getContactPersonsList**](docs/ContactPersonsApi.md#getContactPersonsList) | **GET** /contacts/{contact_id}/contact_persons | Get a list of contact people
*Apacta.ContactTypesApi* | [**contactTypesContactTypeIdGet**](docs/ContactTypesApi.md#contactTypesContactTypeIdGet) | **GET** /contact_types/{contact_type_id} | Get details about one contact type
*Apacta.ContactTypesApi* | [**contactTypesGet**](docs/ContactTypesApi.md#contactTypesGet) | **GET** /contact_types | Get list of contact types supported in Apacta
*Apacta.ContactsApi* | [**bulkDeleteContacts**](docs/ContactsApi.md#bulkDeleteContacts) | **DELETE** /contacts/bulkDelete | Bulk delete contacts
*Apacta.ContactsApi* | [**contactsContactIdDelete**](docs/ContactsApi.md#contactsContactIdDelete) | **DELETE** /contacts/{contact_id} | Delete a contact
*Apacta.ContactsApi* | [**contactsContactIdGet**](docs/ContactsApi.md#contactsContactIdGet) | **GET** /contacts/{contact_id} | Details of 1 contact
*Apacta.ContactsApi* | [**contactsContactIdPut**](docs/ContactsApi.md#contactsContactIdPut) | **PUT** /contacts/{contact_id} | Edit a contact
*Apacta.ContactsApi* | [**contactsGet**](docs/ContactsApi.md#contactsGet) | **GET** /contacts | Get a list of contacts
*Apacta.ContactsApi* | [**contactsPost**](docs/ContactsApi.md#contactsPost) | **POST** /contacts | Add a new contact
*Apacta.CountriesApi* | [**countriesCountryIdGet**](docs/CountriesApi.md#countriesCountryIdGet) | **GET** /countries/{country_id} | Get details about one country
*Apacta.CountriesApi* | [**countriesGet**](docs/CountriesApi.md#countriesGet) | **GET** /countries | Get list of countries supported in Apacta
*Apacta.CurrenciesApi* | [**currenciesCurrencyIdGet**](docs/CurrenciesApi.md#currenciesCurrencyIdGet) | **GET** /currencies/{currency_id} | Get details about one currency
*Apacta.CurrenciesApi* | [**currenciesGet**](docs/CurrenciesApi.md#currenciesGet) | **GET** /currencies | Get list of currencies supported in Apacta
*Apacta.DefaultProjectStatusesApi* | [**projectStatusesAddDefaultPost**](docs/DefaultProjectStatusesApi.md#projectStatusesAddDefaultPost) | **POST** /project_statuses/add_default | Add default project statuses to company
*Apacta.DrivingTypesApi* | [**bulkDeleteDrivingTypes**](docs/DrivingTypesApi.md#bulkDeleteDrivingTypes) | **DELETE** /driving_types/bulkDelete | Bulk delete driving types
*Apacta.DrivingTypesApi* | [**deleteDrivingTypesDrivingTypeId**](docs/DrivingTypesApi.md#deleteDrivingTypesDrivingTypeId) | **DELETE** /driving_types/{driving_type_id} | Delete driving type
*Apacta.DrivingTypesApi* | [**getDrivingTypes**](docs/DrivingTypesApi.md#getDrivingTypes) | **GET** /driving_types | List the driving types of the company
*Apacta.DrivingTypesApi* | [**getDrivingTypesDrivingTypeId**](docs/DrivingTypesApi.md#getDrivingTypesDrivingTypeId) | **GET** /driving_types/{driving_type_id} | View driving type
*Apacta.DrivingTypesApi* | [**postDrivingTypes**](docs/DrivingTypesApi.md#postDrivingTypes) | **POST** /driving_types | Create driving type
*Apacta.DrivingTypesApi* | [**putDrivingTypesDrivingTypeId**](docs/DrivingTypesApi.md#putDrivingTypesDrivingTypeId) | **PUT** /driving_types/{driving_type_id} | Edit driving type
*Apacta.EmployeeHoursApi* | [**employeeHoursGet**](docs/EmployeeHoursApi.md#employeeHoursGet) | **GET** /employee_hours | Used to retrieve details about the logged in user&#39;s hours
*Apacta.EventsApi* | [**eventsEventIdDelete**](docs/EventsApi.md#eventsEventIdDelete) | **DELETE** /events/{event_id} | Delete event
*Apacta.EventsApi* | [**eventsEventIdGet**](docs/EventsApi.md#eventsEventIdGet) | **GET** /events/{event_id} | Show event
*Apacta.EventsApi* | [**eventsEventIdPut**](docs/EventsApi.md#eventsEventIdPut) | **PUT** /events/{event_id} | Edit event
*Apacta.EventsApi* | [**eventsGet**](docs/EventsApi.md#eventsGet) | **GET** /events | Show list of events
*Apacta.EventsApi* | [**eventsIsUserFreeGet**](docs/EventsApi.md#eventsIsUserFreeGet) | **GET** /events/is_user_free | Check if user is available at given datetime range
*Apacta.EventsApi* | [**eventsPost**](docs/EventsApi.md#eventsPost) | **POST** /events | Create event
*Apacta.ExpenseFilesApi* | [**expenseFilesExpenseFileIdDelete**](docs/ExpenseFilesApi.md#expenseFilesExpenseFileIdDelete) | **DELETE** /expense_files/{expense_file_id} | Delete file
*Apacta.ExpenseFilesApi* | [**expenseFilesExpenseFileIdGet**](docs/ExpenseFilesApi.md#expenseFilesExpenseFileIdGet) | **GET** /expense_files/{expense_file_id} | Show file
*Apacta.ExpenseFilesApi* | [**expenseFilesExpenseFileIdPut**](docs/ExpenseFilesApi.md#expenseFilesExpenseFileIdPut) | **PUT** /expense_files/{expense_file_id} | Edit file
*Apacta.ExpenseFilesApi* | [**expenseFilesGet**](docs/ExpenseFilesApi.md#expenseFilesGet) | **GET** /expense_files | Show list of expense files
*Apacta.ExpenseFilesApi* | [**expenseFilesPost**](docs/ExpenseFilesApi.md#expenseFilesPost) | **POST** /expense_files | Add file to expense
*Apacta.ExpenseLinesApi* | [**expenseLinesExpenseLineIdDelete**](docs/ExpenseLinesApi.md#expenseLinesExpenseLineIdDelete) | **DELETE** /expense_lines/{expense_line_id} | Delete expense line
*Apacta.ExpenseLinesApi* | [**expenseLinesExpenseLineIdGet**](docs/ExpenseLinesApi.md#expenseLinesExpenseLineIdGet) | **GET** /expense_lines/{expense_line_id} | Show expense line
*Apacta.ExpenseLinesApi* | [**expenseLinesExpenseLineIdPut**](docs/ExpenseLinesApi.md#expenseLinesExpenseLineIdPut) | **PUT** /expense_lines/{expense_line_id} | Edit expense line
*Apacta.ExpenseLinesApi* | [**expenseLinesGet**](docs/ExpenseLinesApi.md#expenseLinesGet) | **GET** /expense_lines | Show list of expense lines
*Apacta.ExpenseLinesApi* | [**expenseLinesPost**](docs/ExpenseLinesApi.md#expenseLinesPost) | **POST** /expense_lines | Add line to expense
*Apacta.ExpenseOIOUBLFilesApi* | [**expensesExpenseIdOriginalFilesFileIdGet**](docs/ExpenseOIOUBLFilesApi.md#expensesExpenseIdOriginalFilesFileIdGet) | **GET** /expenses/{expense_id}/original_files/{file_id} | Show OIOUBL file
*Apacta.ExpenseOIOUBLFilesApi* | [**expensesExpenseIdOriginalFilesGet**](docs/ExpenseOIOUBLFilesApi.md#expensesExpenseIdOriginalFilesGet) | **GET** /expenses/{expense_id}/original_files | Show list of all OIOUBL files for the expense
*Apacta.ExpensesApi* | [**bulkDeleteExpenses**](docs/ExpensesApi.md#bulkDeleteExpenses) | **DELETE** /expenses/bulkDelete | Bulk delete expenses
*Apacta.ExpensesApi* | [**expensesExpenseIdDelete**](docs/ExpensesApi.md#expensesExpenseIdDelete) | **DELETE** /expenses/{expense_id} | Delete expense
*Apacta.ExpensesApi* | [**expensesExpenseIdGet**](docs/ExpensesApi.md#expensesExpenseIdGet) | **GET** /expenses/{expense_id} | Show expense
*Apacta.ExpensesApi* | [**expensesExpenseIdPut**](docs/ExpensesApi.md#expensesExpenseIdPut) | **PUT** /expenses/{expense_id} | Edit expense
*Apacta.ExpensesApi* | [**expensesGet**](docs/ExpensesApi.md#expensesGet) | **GET** /expenses | Show list of expenses
*Apacta.ExpensesApi* | [**expensesHighestAmountGet**](docs/ExpensesApi.md#expensesHighestAmountGet) | **GET** /expenses/highest_amount | Show highest Expense amount(&#x60;total_selling_price&#x60;)
*Apacta.ExpensesApi* | [**expensesPost**](docs/ExpensesApi.md#expensesPost) | **POST** /expenses | Add line to expense
*Apacta.ExpensesApi* | [**sendEmailsExpenses**](docs/ExpensesApi.md#sendEmailsExpenses) | **DELETE** /expenses/sendEmails | Bulk delete expenses
*Apacta.FinancialStatisticsApi* | [**financialStatisticsWorkingHoursGet**](docs/FinancialStatisticsApi.md#financialStatisticsWorkingHoursGet) | **GET** /financial_statistics/workingHours | Get Total working hours grouped by time entry type
*Apacta.FinancialStatisticsApi* | [**getExpensesSalesPrice**](docs/FinancialStatisticsApi.md#getExpensesSalesPrice) | **GET** /financial_statistics/expensesSalesPrice | Get expenses sales price
*Apacta.FinancialStatisticsApi* | [**getFinancialStatistics**](docs/FinancialStatisticsApi.md#getFinancialStatistics) | **GET** /financial_statistics | Get general statistics
*Apacta.FinancialStatisticsApi* | [**getFinancialStatisticsOverview**](docs/FinancialStatisticsApi.md#getFinancialStatisticsOverview) | **GET** /financial_statistics/overview | Get statistics overview
*Apacta.FinancialStatisticsApi* | [**getInvoicedAmount**](docs/FinancialStatisticsApi.md#getInvoicedAmount) | **GET** /financial_statistics/invoicedAmount | Get invoiced amount
*Apacta.FinancialStatisticsApi* | [**getMargin**](docs/FinancialStatisticsApi.md#getMargin) | **GET** /financial_statistics/margin | Get margin
*Apacta.FinancialStatisticsApi* | [**getMaterialRentalsCostPrice**](docs/FinancialStatisticsApi.md#getMaterialRentalsCostPrice) | **GET** /financial_statistics/materialRentalsCostPrice | Get products material rentals cost price
*Apacta.FinancialStatisticsApi* | [**getProductsCostPrice**](docs/FinancialStatisticsApi.md#getProductsCostPrice) | **GET** /financial_statistics/productsCostPrice | Get products cost price
*Apacta.FormFieldTypesApi* | [**formFieldTypesFormFieldTypeIdGet**](docs/FormFieldTypesApi.md#formFieldTypesFormFieldTypeIdGet) | **GET** /form_field_types/{form_field_type_id} | Get details about single &#x60;FormField&#x60;
*Apacta.FormFieldTypesApi* | [**formFieldTypesGet**](docs/FormFieldTypesApi.md#formFieldTypesGet) | **GET** /form_field_types | Get list of form field types
*Apacta.FormFieldsApi* | [**formFieldsFormFieldIdGet**](docs/FormFieldsApi.md#formFieldsFormFieldIdGet) | **GET** /form_fields/{form_field_id} | Get details about single &#x60;FormField&#x60;
*Apacta.FormFieldsApi* | [**formFieldsPost**](docs/FormFieldsApi.md#formFieldsPost) | **POST** /form_fields | Add a new field to a &#x60;Form&#x60;
*Apacta.FormTemplatesApi* | [**formTemplatesFormTemplateIdGet**](docs/FormTemplatesApi.md#formTemplatesFormTemplateIdGet) | **GET** /form_templates/{form_template_id} | View one form template
*Apacta.FormTemplatesApi* | [**formTemplatesGet**](docs/FormTemplatesApi.md#formTemplatesGet) | **GET** /form_templates | Get array of form_templates for your company
*Apacta.FormsApi* | [**formsFormIdDelete**](docs/FormsApi.md#formsFormIdDelete) | **DELETE** /forms/{form_id} | Delete a form
*Apacta.FormsApi* | [**formsFormIdGet**](docs/FormsApi.md#formsFormIdGet) | **GET** /forms/{form_id} | View form
*Apacta.FormsApi* | [**formsFormIdPut**](docs/FormsApi.md#formsFormIdPut) | **PUT** /forms/{form_id} | Edit a form
*Apacta.FormsApi* | [**formsGet**](docs/FormsApi.md#formsGet) | **GET** /forms | Retrieve array of forms
*Apacta.FormsApi* | [**formsPost**](docs/FormsApi.md#formsPost) | **POST** /forms | Add new form
*Apacta.FormsApi* | [**formsUndeleteFormIdGet**](docs/FormsApi.md#formsUndeleteFormIdGet) | **GET** /forms/undelete/{form_id} | Undelete form and related entities to it
*Apacta.FormsApi* | [**formsViewTimeFormPdfFormIdGet**](docs/FormsApi.md#formsViewTimeFormPdfFormIdGet) | **GET** /forms/view_time_form_pdf/{form_id} | Generate time form pdf
*Apacta.IntegrationsApi* | [**getIntegrationsContactsSync**](docs/IntegrationsApi.md#getIntegrationsContactsSync) | **GET** /integrations/contactsSync | Force Synchronization with ERP systems
*Apacta.IntegrationsApi* | [**getIntegrationsList**](docs/IntegrationsApi.md#getIntegrationsList) | **GET** /integrations | Get integrations list
*Apacta.IntegrationsApi* | [**getIntegrationsView**](docs/IntegrationsApi.md#getIntegrationsView) | **GET** /integrations/{integration_id} | View integration details
*Apacta.IntegrationsApi* | [**integrationsBillysAuthenticatePost**](docs/IntegrationsApi.md#integrationsBillysAuthenticatePost) | **POST** /integrations/billysAuthenticate | Authenticate to Billys
*Apacta.IntegrationsApi* | [**integrationsProductsSyncGet**](docs/IntegrationsApi.md#integrationsProductsSyncGet) | **GET** /integrations/productsSync | Sync products from erp integration
*Apacta.InvoiceEmailsApi* | [**getOneInvoiceEmails**](docs/InvoiceEmailsApi.md#getOneInvoiceEmails) | **GET** /invoices/{invoice_id}/emails/{email_id} | Get an invoice emails
*Apacta.InvoiceFilesApi* | [**createInvoiceFile**](docs/InvoiceFilesApi.md#createInvoiceFile) | **POST** /invoices/{invoice_id}/files | Create a new invoice file
*Apacta.InvoiceFilesApi* | [**getInvoiceFiles**](docs/InvoiceFilesApi.md#getInvoiceFiles) | **GET** /invoices/{invoice_id}/files | Get list of invoice files
*Apacta.InvoiceFilesApi* | [**getOneInvoiceFiles**](docs/InvoiceFilesApi.md#getOneInvoiceFiles) | **GET** /invoices/{invoice_id}/files/{file_id} | Get an invoice files
*Apacta.InvoiceFilesApi* | [**invoicesInvoiceIdFilesFileIdDelete**](docs/InvoiceFilesApi.md#invoicesInvoiceIdFilesFileIdDelete) | **DELETE** /invoices/{invoice_id}/files/{file_id} | Delete invoice file
*Apacta.InvoiceLineTextTemplatesApi* | [**invoiceLineTextTemplateGet**](docs/InvoiceLineTextTemplatesApi.md#invoiceLineTextTemplateGet) | **GET** /invoice_line_text_template | Get a list of invoice line text templates
*Apacta.InvoiceLineTextTemplatesApi* | [**invoiceLineTextTemplateInvoiceLineTextTemplateIdDelete**](docs/InvoiceLineTextTemplatesApi.md#invoiceLineTextTemplateInvoiceLineTextTemplateIdDelete) | **DELETE** /invoice_line_text_template/{invoice_line_text_template_id} | Delete an invoice line text template
*Apacta.InvoiceLineTextTemplatesApi* | [**invoiceLineTextTemplateInvoiceLineTextTemplateIdGet**](docs/InvoiceLineTextTemplatesApi.md#invoiceLineTextTemplateInvoiceLineTextTemplateIdGet) | **GET** /invoice_line_text_template/{invoice_line_text_template_id} | Get a single invoice line text template
*Apacta.InvoiceLineTextTemplatesApi* | [**invoiceLineTextTemplateInvoiceLineTextTemplateIdPost**](docs/InvoiceLineTextTemplatesApi.md#invoiceLineTextTemplateInvoiceLineTextTemplateIdPost) | **POST** /invoice_line_text_template/{invoice_line_text_template_id} | Edit an invoice line text template
*Apacta.InvoiceLineTextTemplatesApi* | [**invoiceLineTextTemplatePost**](docs/InvoiceLineTextTemplatesApi.md#invoiceLineTextTemplatePost) | **POST** /invoice_line_text_template | Add a new invoice line text template
*Apacta.InvoiceLinesApi* | [**invoiceLineTextsInvoiceLineTextIdPost**](docs/InvoiceLinesApi.md#invoiceLineTextsInvoiceLineTextIdPost) | **POST** /invoice_line_texts/{invoice_line_text_id} | Edit invoice line text
*Apacta.InvoiceLinesApi* | [**invoiceLineTextsPost**](docs/InvoiceLinesApi.md#invoiceLineTextsPost) | **POST** /invoice_line_texts/ | Add invoice line text
*Apacta.InvoiceLinesApi* | [**invoiceLinesGet**](docs/InvoiceLinesApi.md#invoiceLinesGet) | **GET** /invoice_lines | View list of invoice lines
*Apacta.InvoiceLinesApi* | [**invoiceLinesInvoiceLineIdDelete**](docs/InvoiceLinesApi.md#invoiceLinesInvoiceLineIdDelete) | **DELETE** /invoice_lines/{invoice_line_id} | Delete invoice line
*Apacta.InvoiceLinesApi* | [**invoiceLinesInvoiceLineIdGet**](docs/InvoiceLinesApi.md#invoiceLinesInvoiceLineIdGet) | **GET** /invoice_lines/{invoice_line_id} | View invoice line
*Apacta.InvoiceLinesApi* | [**invoiceLinesInvoiceLineIdPut**](docs/InvoiceLinesApi.md#invoiceLinesInvoiceLineIdPut) | **PUT** /invoice_lines/{invoice_line_id} | Edit invoice line
*Apacta.InvoiceLinesApi* | [**invoiceLinesPost**](docs/InvoiceLinesApi.md#invoiceLinesPost) | **POST** /invoice_lines | Add invoice line
*Apacta.InvoicesApi* | [**bulkDeleteInvoices**](docs/InvoicesApi.md#bulkDeleteInvoices) | **DELETE** /invoices/bulkDelete | Bulk delete invoices
*Apacta.InvoicesApi* | [**invoicesGet**](docs/InvoicesApi.md#invoicesGet) | **GET** /invoices | View list of invoices
*Apacta.InvoicesApi* | [**invoicesInvoiceIdCopyPost**](docs/InvoicesApi.md#invoicesInvoiceIdCopyPost) | **POST** /invoices/{invoice_id}/copy | Create a copy of an invoice
*Apacta.InvoicesApi* | [**invoicesInvoiceIdDelete**](docs/InvoicesApi.md#invoicesInvoiceIdDelete) | **DELETE** /invoices/{invoice_id} | Delete invoice
*Apacta.InvoicesApi* | [**invoicesInvoiceIdGet**](docs/InvoicesApi.md#invoicesInvoiceIdGet) | **GET** /invoices/{invoice_id} | View invoice
*Apacta.InvoicesApi* | [**invoicesInvoiceIdLinkProjectPdfPost**](docs/InvoicesApi.md#invoicesInvoiceIdLinkProjectPdfPost) | **POST** /invoices/{invoice_id}/linkProjectPdf | Creates an invoice file containing the project&#39;s pdf overview
*Apacta.InvoicesApi* | [**invoicesInvoiceIdPut**](docs/InvoicesApi.md#invoicesInvoiceIdPut) | **PUT** /invoices/{invoice_id} | Edit invoice
*Apacta.InvoicesApi* | [**invoicesInvoiceIdUnlinkProjectPdfPost**](docs/InvoicesApi.md#invoicesInvoiceIdUnlinkProjectPdfPost) | **POST** /invoices/{invoice_id}/unlinkProjectPdf | Deletes the linked project overview pdf
*Apacta.InvoicesApi* | [**invoicesPost**](docs/InvoicesApi.md#invoicesPost) | **POST** /invoices | Add invoice
*Apacta.InvoicesApi* | [**invoicesVatOptionsGet**](docs/InvoicesApi.md#invoicesVatOptionsGet) | **GET** /invoices/vatOptions | List VAT options
*Apacta.MassMessagesUsersApi* | [**massMessagesUsersGet**](docs/MassMessagesUsersApi.md#massMessagesUsersGet) | **GET** /mass_messages_users | View list of mass messages for specific user
*Apacta.MassMessagesUsersApi* | [**massMessagesUsersMassMessagesUserIdGet**](docs/MassMessagesUsersApi.md#massMessagesUsersMassMessagesUserIdGet) | **GET** /mass_messages_users/{mass_messages_user_id} | View mass message
*Apacta.MassMessagesUsersApi* | [**massMessagesUsersMassMessagesUserIdPut**](docs/MassMessagesUsersApi.md#massMessagesUsersMassMessagesUserIdPut) | **PUT** /mass_messages_users/{mass_messages_user_id} | Edit mass message
*Apacta.MaterialRentalsApi* | [**materialsMaterialIdRentalsCheckoutPost**](docs/MaterialRentalsApi.md#materialsMaterialIdRentalsCheckoutPost) | **POST** /materials/{material_id}/rentals/checkout/ | Checkout material rental
*Apacta.MaterialRentalsApi* | [**materialsMaterialIdRentalsGet**](docs/MaterialRentalsApi.md#materialsMaterialIdRentalsGet) | **GET** /materials/{material_id}/rentals/ | Show list of rentals for specific material
*Apacta.MaterialRentalsApi* | [**materialsMaterialIdRentalsMaterialRentalIdDelete**](docs/MaterialRentalsApi.md#materialsMaterialIdRentalsMaterialRentalIdDelete) | **DELETE** /materials/{material_id}/rentals/{material_rental_id}/ | Delete material rental
*Apacta.MaterialRentalsApi* | [**materialsMaterialIdRentalsMaterialRentalIdGet**](docs/MaterialRentalsApi.md#materialsMaterialIdRentalsMaterialRentalIdGet) | **GET** /materials/{material_id}/rentals/{material_rental_id}/ | Show rental foor materi
*Apacta.MaterialRentalsApi* | [**materialsMaterialIdRentalsMaterialRentalIdPut**](docs/MaterialRentalsApi.md#materialsMaterialIdRentalsMaterialRentalIdPut) | **PUT** /materials/{material_id}/rentals/{material_rental_id}/ | Edit material rental
*Apacta.MaterialRentalsApi* | [**materialsMaterialIdRentalsPost**](docs/MaterialRentalsApi.md#materialsMaterialIdRentalsPost) | **POST** /materials/{material_id}/rentals/ | Add material rental
*Apacta.MaterialsApi* | [**materialsGet**](docs/MaterialsApi.md#materialsGet) | **GET** /materials | View list of all materials
*Apacta.MaterialsApi* | [**materialsMaterialIdDelete**](docs/MaterialsApi.md#materialsMaterialIdDelete) | **DELETE** /materials/{material_id} | Delete material
*Apacta.MaterialsApi* | [**materialsMaterialIdGet**](docs/MaterialsApi.md#materialsMaterialIdGet) | **GET** /materials/{material_id} | View material
*Apacta.MaterialsApi* | [**materialsMaterialIdPut**](docs/MaterialsApi.md#materialsMaterialIdPut) | **PUT** /materials/{material_id} | Edit material
*Apacta.MaterialsApi* | [**materialsPost**](docs/MaterialsApi.md#materialsPost) | **POST** /materials | Add material
*Apacta.OfferStatusesApi* | [**offerStatusesBulkDeleteDelete**](docs/OfferStatusesApi.md#offerStatusesBulkDeleteDelete) | **DELETE** /offer_statuses/bulkDelete | Bulk delete offer statuses
*Apacta.OfferStatusesApi* | [**offerStatusesGet**](docs/OfferStatusesApi.md#offerStatusesGet) | **GET** /offer_statuses | Get list of offer statuses
*Apacta.OfferStatusesApi* | [**offerStatusesOfferStatusIdDelete**](docs/OfferStatusesApi.md#offerStatusesOfferStatusIdDelete) | **DELETE** /offer_statuses/{offer_status_id} | Delete a offer status
*Apacta.OfferStatusesApi* | [**offerStatusesOfferStatusIdGet**](docs/OfferStatusesApi.md#offerStatusesOfferStatusIdGet) | **GET** /offer_statuses/{offer_status_id} | Get a single offer status
*Apacta.OfferStatusesApi* | [**offerStatusesOfferStatusIdPut**](docs/OfferStatusesApi.md#offerStatusesOfferStatusIdPut) | **PUT** /offer_statuses/{offer_status_id} | Edit a offer status
*Apacta.OfferStatusesApi* | [**offerStatusesPost**](docs/OfferStatusesApi.md#offerStatusesPost) | **POST** /offer_statuses | Create a new offer status
*Apacta.OffersApi* | [**offersGet**](docs/OffersApi.md#offersGet) | **GET** /offers | View list of offers
*Apacta.OffersApi* | [**offersOfferIdDelete**](docs/OffersApi.md#offersOfferIdDelete) | **DELETE** /offers/{offer_id} | Delete an offer
*Apacta.OffersApi* | [**offersOfferIdGet**](docs/OffersApi.md#offersOfferIdGet) | **GET** /offers/{offer_id} | View offer
*Apacta.OffersApi* | [**offersOfferIdPut**](docs/OffersApi.md#offersOfferIdPut) | **PUT** /offers/{offer_id} | Edit an offer
*Apacta.OffersApi* | [**offersPost**](docs/OffersApi.md#offersPost) | **POST** /offers | Add new offer
*Apacta.PaymentTermTypesApi* | [**paymentTermTypesGet**](docs/PaymentTermTypesApi.md#paymentTermTypesGet) | **GET** /payment_term_types | Get a list of payment term types
*Apacta.PaymentTermTypesApi* | [**paymentTermTypesPaymentTermTypeIdGet**](docs/PaymentTermTypesApi.md#paymentTermTypesPaymentTermTypeIdGet) | **GET** /payment_term_types/{payment_term_type_id} | Details of 1 payment term type
*Apacta.PaymentTermsApi* | [**paymentTermsErpGet**](docs/PaymentTermsApi.md#paymentTermsErpGet) | **GET** /payment_terms/erp | Get integration payment terms list
*Apacta.PaymentTermsApi* | [**paymentTermsGet**](docs/PaymentTermsApi.md#paymentTermsGet) | **GET** /payment_terms | Get a list of payment terms
*Apacta.PaymentTermsApi* | [**paymentTermsPaymentTermIdGet**](docs/PaymentTermsApi.md#paymentTermsPaymentTermIdGet) | **GET** /payment_terms/{payment_term_id} | Details of 1 payment term
*Apacta.PingApi* | [**pingGet**](docs/PingApi.md#pingGet) | **GET** /ping | Check if API is up and API key works
*Apacta.ProductVariantsApi* | [**productsProductIdVariantsGet**](docs/ProductVariantsApi.md#productsProductIdVariantsGet) | **GET** /products/{product_id}/variants | Get a product&#39;s variants
*Apacta.ProductVariantsApi* | [**productsProductIdVariantsPost**](docs/ProductVariantsApi.md#productsProductIdVariantsPost) | **POST** /products/{product_id}/variants | Add a new variant to a product
*Apacta.ProductVariantsApi* | [**productsProductIdVariantsVariantTypeVariantIdDelete**](docs/ProductVariantsApi.md#productsProductIdVariantsVariantTypeVariantIdDelete) | **DELETE** /products/{product_id}/variants/{variant_type}/{variant_id} | Delete a product variant
*Apacta.ProductsApi* | [**bulkDeleteProducts**](docs/ProductsApi.md#bulkDeleteProducts) | **DELETE** /products/bulkDelete | Bulk delete products
*Apacta.ProductsApi* | [**productsGet**](docs/ProductsApi.md#productsGet) | **GET** /products | List products
*Apacta.ProductsApi* | [**productsPost**](docs/ProductsApi.md#productsPost) | **POST** /products | Add new product
*Apacta.ProductsApi* | [**productsProductIdDelete**](docs/ProductsApi.md#productsProductIdDelete) | **DELETE** /products/{product_id} | Delete a product
*Apacta.ProductsApi* | [**productsProductIdGet**](docs/ProductsApi.md#productsProductIdGet) | **GET** /products/{product_id} | View single product
*Apacta.ProductsApi* | [**productsProductIdPut**](docs/ProductsApi.md#productsProductIdPut) | **PUT** /products/{product_id} | Edit a product
*Apacta.ProductsApi* | [**productsUndeleteProductIdPost**](docs/ProductsApi.md#productsUndeleteProductIdPost) | **POST** /products/undelete/{product_id} | Restore a deleted product
*Apacta.ProductsApi* | [**uploadOrDeleteProductImage**](docs/ProductsApi.md#uploadOrDeleteProductImage) | **POST** /products/{product_id}/uploadImage | 
*Apacta.ProjectCustomFieldAttributesApi* | [**projectCustomFieldAttributesGet**](docs/ProjectCustomFieldAttributesApi.md#projectCustomFieldAttributesGet) | **GET** /project_custom_field_attributes | Get a list of project custom field attributes
*Apacta.ProjectCustomFieldAttributesApi* | [**projectCustomFieldAttributesProjectCustomFieldAttributeIdGet**](docs/ProjectCustomFieldAttributesApi.md#projectCustomFieldAttributesProjectCustomFieldAttributeIdGet) | **GET** /project_custom_field_attributes/{project_custom_field_attribute_id} | Details of 1 project custom field attribute
*Apacta.ProjectStatusTypesApi* | [**projectStatusTypesGet**](docs/ProjectStatusTypesApi.md#projectStatusTypesGet) | **GET** /project_status_types | Get a list of project status types
*Apacta.ProjectStatusesApi* | [**projectStatusesBulkDeleteDelete**](docs/ProjectStatusesApi.md#projectStatusesBulkDeleteDelete) | **DELETE** /project_statuses/bulkDelete | Bulk delete project statuses
*Apacta.ProjectStatusesApi* | [**projectStatusesGet**](docs/ProjectStatusesApi.md#projectStatusesGet) | **GET** /project_statuses | Get list of project statuses
*Apacta.ProjectStatusesApi* | [**projectStatusesPost**](docs/ProjectStatusesApi.md#projectStatusesPost) | **POST** /project_statuses | Create a new project status
*Apacta.ProjectStatusesApi* | [**projectStatusesProjectStatusIdDelete**](docs/ProjectStatusesApi.md#projectStatusesProjectStatusIdDelete) | **DELETE** /project_statuses/{project_status_id} | Delete a project status
*Apacta.ProjectStatusesApi* | [**projectStatusesProjectStatusIdGet**](docs/ProjectStatusesApi.md#projectStatusesProjectStatusIdGet) | **GET** /project_statuses/{project_status_id} | Get a single project status
*Apacta.ProjectStatusesApi* | [**projectStatusesProjectStatusIdPut**](docs/ProjectStatusesApi.md#projectStatusesProjectStatusIdPut) | **PUT** /project_statuses/{project_status_id} | Edit a project status
*Apacta.ProjectStatusesApi* | [**projectsHasProjectsWithCustomStatusesGet**](docs/ProjectStatusesApi.md#projectsHasProjectsWithCustomStatusesGet) | **GET** /projects/has_projects_with_custom_statuses | Check if the company has projects with custom statuses
*Apacta.ProjectsApi* | [**projectsGet**](docs/ProjectsApi.md#projectsGet) | **GET** /projects | View list of projects
*Apacta.ProjectsApi* | [**projectsHasProjectsWithCustomStatusesGet_0**](docs/ProjectsApi.md#projectsHasProjectsWithCustomStatusesGet_0) | **GET** /projects/has_projects_with_custom_statuses | Check if the company has projects with custom statuses
*Apacta.ProjectsApi* | [**projectsPost**](docs/ProjectsApi.md#projectsPost) | **POST** /projects | Add a project
*Apacta.ProjectsApi* | [**projectsProjectIdAllFilesGet**](docs/ProjectsApi.md#projectsProjectIdAllFilesGet) | **GET** /projects/{project_id}/all_files | Show list of all files uploaded to project
*Apacta.ProjectsApi* | [**projectsProjectIdDelete**](docs/ProjectsApi.md#projectsProjectIdDelete) | **DELETE** /projects/{project_id} | Delete a project
*Apacta.ProjectsApi* | [**projectsProjectIdFilesFileIdDelete**](docs/ProjectsApi.md#projectsProjectIdFilesFileIdDelete) | **DELETE** /projects/{project_id}/files/{file_id}/ | Delete file
*Apacta.ProjectsApi* | [**projectsProjectIdFilesFileIdGet**](docs/ProjectsApi.md#projectsProjectIdFilesFileIdGet) | **GET** /projects/{project_id}/files/{file_id}/ | Show file
*Apacta.ProjectsApi* | [**projectsProjectIdFilesFileIdPut**](docs/ProjectsApi.md#projectsProjectIdFilesFileIdPut) | **PUT** /projects/{project_id}/files/{file_id}/ | Edit file
*Apacta.ProjectsApi* | [**projectsProjectIdFilesGet**](docs/ProjectsApi.md#projectsProjectIdFilesGet) | **GET** /projects/{project_id}/files | Show list of files uploaded to project
*Apacta.ProjectsApi* | [**projectsProjectIdGet**](docs/ProjectsApi.md#projectsProjectIdGet) | **GET** /projects/{project_id} | View specific project
*Apacta.ProjectsApi* | [**projectsProjectIdProjectFilesGet**](docs/ProjectsApi.md#projectsProjectIdProjectFilesGet) | **GET** /projects/{project_id}/project_files | Show list of project files uploaded to project
*Apacta.ProjectsApi* | [**projectsProjectIdProjectFilesPost**](docs/ProjectsApi.md#projectsProjectIdProjectFilesPost) | **POST** /projects/{project_id}/project_files | Add project file to projects
*Apacta.ProjectsApi* | [**projectsProjectIdProjectFilesProjectFileIdDelete**](docs/ProjectsApi.md#projectsProjectIdProjectFilesProjectFileIdDelete) | **DELETE** /projects/{project_id}/project_files/{project_file_id}/ | Delete project file
*Apacta.ProjectsApi* | [**projectsProjectIdProjectFilesProjectFileIdGet**](docs/ProjectsApi.md#projectsProjectIdProjectFilesProjectFileIdGet) | **GET** /projects/{project_id}/project_files/{project_file_id}/ | Show project file
*Apacta.ProjectsApi* | [**projectsProjectIdProjectFilesProjectFileIdPut**](docs/ProjectsApi.md#projectsProjectIdProjectFilesProjectFileIdPut) | **PUT** /projects/{project_id}/project_files/{project_file_id}/ | Edit project file
*Apacta.ProjectsApi* | [**projectsProjectIdPut**](docs/ProjectsApi.md#projectsProjectIdPut) | **PUT** /projects/{project_id} | Edit a project
*Apacta.ProjectsApi* | [**projectsProjectIdSendBulkPdfPost**](docs/ProjectsApi.md#projectsProjectIdSendBulkPdfPost) | **POST** /projects/{project_id}/send_bulk_pdf | Send bulk forms pdf by email
*Apacta.ProjectsApi* | [**projectsProjectIdUsersGet**](docs/ProjectsApi.md#projectsProjectIdUsersGet) | **GET** /projects/{project_id}/users/ | Show list of users added to project
*Apacta.ProjectsApi* | [**projectsProjectIdUsersPost**](docs/ProjectsApi.md#projectsProjectIdUsersPost) | **POST** /projects/{project_id}/users/ | Add user to project
*Apacta.ProjectsApi* | [**projectsProjectIdUsersUserIdDelete**](docs/ProjectsApi.md#projectsProjectIdUsersUserIdDelete) | **DELETE** /projects/{project_id}/users/{user_id} | Delete user from project
*Apacta.ProjectsApi* | [**projectsProjectIdUsersUserIdGet**](docs/ProjectsApi.md#projectsProjectIdUsersUserIdGet) | **GET** /projects/{project_id}/users/{user_id} | View specific user assigned to project
*Apacta.RejectionReasonsApi* | [**overviewRejectionReasonsGet**](docs/RejectionReasonsApi.md#overviewRejectionReasonsGet) | **GET** /overview/rejection_reasons | Get a statistics data for rejection reasons
*Apacta.ReportsApi* | [**reportsGet**](docs/ReportsApi.md#reportsGet) | **GET** /reports | 
*Apacta.RolesApi* | [**rolesGet**](docs/RolesApi.md#rolesGet) | **GET** /roles | Get a list of roles
*Apacta.StockLocationsApi* | [**stockLocationsGet**](docs/StockLocationsApi.md#stockLocationsGet) | **GET** /stock_locations | List stock_locations
*Apacta.StockLocationsApi* | [**stockLocationsLocationIdDelete**](docs/StockLocationsApi.md#stockLocationsLocationIdDelete) | **DELETE** /stock_locations/{location_id} | Delete location
*Apacta.StockLocationsApi* | [**stockLocationsLocationIdGet**](docs/StockLocationsApi.md#stockLocationsLocationIdGet) | **GET** /stock_locations/{location_id} | View single location
*Apacta.StockLocationsApi* | [**stockLocationsLocationIdPut**](docs/StockLocationsApi.md#stockLocationsLocationIdPut) | **PUT** /stock_locations/{location_id} | Edit location
*Apacta.StockLocationsApi* | [**stockLocationsPost**](docs/StockLocationsApi.md#stockLocationsPost) | **POST** /stock_locations | Add new stock_locations
*Apacta.TimeEntriesApi* | [**timeEntriesGet**](docs/TimeEntriesApi.md#timeEntriesGet) | **GET** /time_entries | List time entries
*Apacta.TimeEntriesApi* | [**timeEntriesPost**](docs/TimeEntriesApi.md#timeEntriesPost) | **POST** /time_entries | Add new time entry
*Apacta.TimeEntriesApi* | [**timeEntriesTimeEntryIdDelete**](docs/TimeEntriesApi.md#timeEntriesTimeEntryIdDelete) | **DELETE** /time_entries/{time_entry_id} | Delete time entry
*Apacta.TimeEntriesApi* | [**timeEntriesTimeEntryIdGet**](docs/TimeEntriesApi.md#timeEntriesTimeEntryIdGet) | **GET** /time_entries/{time_entry_id} | View time entry
*Apacta.TimeEntriesApi* | [**timeEntriesTimeEntryIdPut**](docs/TimeEntriesApi.md#timeEntriesTimeEntryIdPut) | **PUT** /time_entries/{time_entry_id} | Edit time entry
*Apacta.TimeEntryIntervalsApi* | [**timeEntryIntervalsGet**](docs/TimeEntryIntervalsApi.md#timeEntryIntervalsGet) | **GET** /time_entry_intervals | List possible time entry intervals
*Apacta.TimeEntryIntervalsApi* | [**timeEntryIntervalsTimeEntryIntervalIdGet**](docs/TimeEntryIntervalsApi.md#timeEntryIntervalsTimeEntryIntervalIdGet) | **GET** /time_entry_intervals/{time_entry_interval_id} | View time entry interval
*Apacta.TimeEntryRateApi* | [**timeEntryRatesTimeEntryRateIdDelete**](docs/TimeEntryRateApi.md#timeEntryRatesTimeEntryRateIdDelete) | **DELETE** /time_entry_rates/{time_entry_rate_id} | Delete time entry rate
*Apacta.TimeEntryRatesApi* | [**timeEntryRatesGet**](docs/TimeEntryRatesApi.md#timeEntryRatesGet) | **GET** /time_entry_rates | List time entry rates
*Apacta.TimeEntryRatesApi* | [**timeEntryRatesPost**](docs/TimeEntryRatesApi.md#timeEntryRatesPost) | **POST** /time_entry_rates | Add new time entry rate
*Apacta.TimeEntryRatesApi* | [**timeEntryRatesTimeEntryRateIdGet**](docs/TimeEntryRatesApi.md#timeEntryRatesTimeEntryRateIdGet) | **GET** /time_entry_rates/{time_entry_rate_id} | View time entry rate
*Apacta.TimeEntryRatesApi* | [**timeEntryRatesTimeEntryRateIdPut**](docs/TimeEntryRatesApi.md#timeEntryRatesTimeEntryRateIdPut) | **PUT** /time_entry_rates/{time_entry_rate_id} | Edit time entry rate
*Apacta.TimeEntryRuleGroupsApi* | [**timeEntryRuleGroupsGet**](docs/TimeEntryRuleGroupsApi.md#timeEntryRuleGroupsGet) | **GET** /time_entry_rule_groups | List time entry rule groups
*Apacta.TimeEntryTypesApi* | [**bulkActivateTimeEntryTypes**](docs/TimeEntryTypesApi.md#bulkActivateTimeEntryTypes) | **POST** /time_entry_types/bulkActivate | Bulk activate time entry types
*Apacta.TimeEntryTypesApi* | [**bulkDeactivateTimeEntryTypes**](docs/TimeEntryTypesApi.md#bulkDeactivateTimeEntryTypes) | **POST** /time_entry_types/bulkDeactivate | Bulk deactivate time entry types
*Apacta.TimeEntryTypesApi* | [**bulkDeleteTimeEntryTypes**](docs/TimeEntryTypesApi.md#bulkDeleteTimeEntryTypes) | **DELETE** /time_entry_types/bulkDelete | Bulk delete time entry types
*Apacta.TimeEntryTypesApi* | [**timeEntryTypesGet**](docs/TimeEntryTypesApi.md#timeEntryTypesGet) | **GET** /time_entry_types | List time entries types
*Apacta.TimeEntryTypesApi* | [**timeEntryTypesPost**](docs/TimeEntryTypesApi.md#timeEntryTypesPost) | **POST** /time_entry_types | Add new time entry type
*Apacta.TimeEntryTypesApi* | [**timeEntryTypesTimeEntryTypeIdDelete**](docs/TimeEntryTypesApi.md#timeEntryTypesTimeEntryTypeIdDelete) | **DELETE** /time_entry_types/{time_entry_type_id} | Delete time entry type
*Apacta.TimeEntryTypesApi* | [**timeEntryTypesTimeEntryTypeIdGet**](docs/TimeEntryTypesApi.md#timeEntryTypesTimeEntryTypeIdGet) | **GET** /time_entry_types/{time_entry_type_id} | View time entry type
*Apacta.TimeEntryTypesApi* | [**timeEntryTypesTimeEntryTypeIdPut**](docs/TimeEntryTypesApi.md#timeEntryTypesTimeEntryTypeIdPut) | **PUT** /time_entry_types/{time_entry_type_id} | Edit time entry type
*Apacta.TimeEntryUnitTypesApi* | [**timeEntryUnitTypesGet**](docs/TimeEntryUnitTypesApi.md#timeEntryUnitTypesGet) | **GET** /time_entry_unit_types | List possible time entry unit types
*Apacta.TimeEntryUnitTypesApi* | [**timeEntryUnitTypesTimeEntryUnitTypeIdGet**](docs/TimeEntryUnitTypesApi.md#timeEntryUnitTypesTimeEntryUnitTypeIdGet) | **GET** /time_entry_unit_types/{time_entry_unit_type_id} | View time entry unit type
*Apacta.TimeEntryValueTypesApi* | [**timeEntryValueTypesGet**](docs/TimeEntryValueTypesApi.md#timeEntryValueTypesGet) | **GET** /time_entry_value_types | List possible time entry value types
*Apacta.TimeEntryValueTypesApi* | [**timeEntryValueTypesTimeEntryValueTypeIdGet**](docs/TimeEntryValueTypesApi.md#timeEntryValueTypesTimeEntryValueTypeIdGet) | **GET** /time_entry_value_types/{time_entry_value_type_id} | View time entry value type
*Apacta.UserCustomFieldAttributesApi* | [**userCustomFieldAttributesGet**](docs/UserCustomFieldAttributesApi.md#userCustomFieldAttributesGet) | **GET** /user_custom_field_attributes | Get a list of user custom field attributes
*Apacta.UserCustomFieldAttributesApi* | [**userCustomFieldAttributesUserCustomFieldAttributeIdGet**](docs/UserCustomFieldAttributesApi.md#userCustomFieldAttributesUserCustomFieldAttributeIdGet) | **GET** /user_custom_field_attributes/{user_custom_field_attribute_id} | Details of 1 user custom field attribute
*Apacta.UserCustomFieldValueApi* | [**usersUserIdUserCustomFieldValueGet**](docs/UserCustomFieldValueApi.md#usersUserIdUserCustomFieldValueGet) | **GET** /users/{user_id}/user_custom_field_value | Get a list of user custom field values
*Apacta.UserCustomFieldValueApi* | [**usersUserIdUserCustomFieldValueUserCustomFieldValueIdGet**](docs/UserCustomFieldValueApi.md#usersUserIdUserCustomFieldValueUserCustomFieldValueIdGet) | **GET** /users/{user_id}/user_custom_field_value/{user_custom_field_value_id} | Get a single record of user custom field value
*Apacta.UserCustomFieldValueApi* | [**usersUserIdUserCustomFieldValueUserCustomFieldValueIdPut**](docs/UserCustomFieldValueApi.md#usersUserIdUserCustomFieldValueUserCustomFieldValueIdPut) | **PUT** /users/{user_id}/user_custom_field_value/{user_custom_field_value_id} | Update a single record of user custom field value
*Apacta.UsersApi* | [**usersBulkActivate**](docs/UsersApi.md#usersBulkActivate) | **POST** /users/bulkActivate | Activate multiple users
*Apacta.UsersApi* | [**usersBulkDeactivate**](docs/UsersApi.md#usersBulkDeactivate) | **POST** /users/bulkDeactivate | Deactivate multiple users
*Apacta.UsersApi* | [**usersGet**](docs/UsersApi.md#usersGet) | **GET** /users | Get list of users in company
*Apacta.UsersApi* | [**usersPost**](docs/UsersApi.md#usersPost) | **POST** /users | Add user to company
*Apacta.UsersApi* | [**usersResendWelcomeSmsGet**](docs/UsersApi.md#usersResendWelcomeSmsGet) | **GET** /users/resendWelcomeSms | Resend Welcome SMS to the user
*Apacta.UsersApi* | [**usersUserIdDelete**](docs/UsersApi.md#usersUserIdDelete) | **DELETE** /users/{user_id} | Delete user
*Apacta.UsersApi* | [**usersUserIdGet**](docs/UsersApi.md#usersUserIdGet) | **GET** /users/{user_id} | View user
*Apacta.UsersApi* | [**usersUserIdIntegrationSettingsGet**](docs/UsersApi.md#usersUserIdIntegrationSettingsGet) | **GET** /users/{user_id}/integration_settings | Get a list of user integration settings
*Apacta.UsersApi* | [**usersUserIdIntegrationSettingsIntegrationSettingsUserIdDelete**](docs/UsersApi.md#usersUserIdIntegrationSettingsIntegrationSettingsUserIdDelete) | **DELETE** /users/{user_id}/integration_settings/{integration_settings_user_id} | Delete a user integration setting
*Apacta.UsersApi* | [**usersUserIdIntegrationSettingsIntegrationSettingsUserIdGet**](docs/UsersApi.md#usersUserIdIntegrationSettingsIntegrationSettingsUserIdGet) | **GET** /users/{user_id}/integration_settings/{integration_settings_user_id} | Get a user integration setting
*Apacta.UsersApi* | [**usersUserIdIntegrationSettingsIntegrationSettingsUserIdPut**](docs/UsersApi.md#usersUserIdIntegrationSettingsIntegrationSettingsUserIdPut) | **PUT** /users/{user_id}/integration_settings/{integration_settings_user_id} | Edit a user integration setting
*Apacta.UsersApi* | [**usersUserIdIntegrationSettingsPost**](docs/UsersApi.md#usersUserIdIntegrationSettingsPost) | **POST** /users/{user_id}/integration_settings | Add a user integration setting
*Apacta.UsersApi* | [**usersUserIdPut**](docs/UsersApi.md#usersUserIdPut) | **PUT** /users/{user_id} | Edit user
*Apacta.UsersApi* | [**usersUserIdUploadImagePost**](docs/UsersApi.md#usersUserIdUploadImagePost) | **POST** /users/{user_id}/uploadImage | Upload a new image to a user
*Apacta.VendorProductPriceFilesApi* | [**vendorProductPriceFilesGet**](docs/VendorProductPriceFilesApi.md#vendorProductPriceFilesGet) | **GET** /vendor_product_price_files | Get a list of price files
*Apacta.VendorProductPriceFilesApi* | [**vendorProductPriceFilesPost**](docs/VendorProductPriceFilesApi.md#vendorProductPriceFilesPost) | **POST** /vendor_product_price_files | Upload a vendor price file
*Apacta.VendorProductPriceFilesApi* | [**vendorProductPriceFilesVendorProductPriceFileIdGet**](docs/VendorProductPriceFilesApi.md#vendorProductPriceFilesVendorProductPriceFileIdGet) | **GET** /vendor_product_price_files/{vendor_product_price_file_id} | Get a single price file
*Apacta.VendorProductsApi* | [**vendorProductsGet**](docs/VendorProductsApi.md#vendorProductsGet) | **GET** /vendor_products | List vendor products
*Apacta.VendorProductsApi* | [**vendorProductsVendorProductIdGet**](docs/VendorProductsApi.md#vendorProductsVendorProductIdGet) | **GET** /vendor_products/{vendor_product_id} | View single vendor product
*Apacta.VendorsApi* | [**addVendor**](docs/VendorsApi.md#addVendor) | **POST** /vendors | Add a new vendor
*Apacta.VendorsApi* | [**editVendor**](docs/VendorsApi.md#editVendor) | **PUT** /vendors/{vendor_id} | Edit a vendor
*Apacta.VendorsApi* | [**getVendor**](docs/VendorsApi.md#getVendor) | **GET** /vendors/{vendor_id} | Get a vendor
*Apacta.VendorsApi* | [**getVendorsList**](docs/VendorsApi.md#getVendorsList) | **GET** /vendors | Get a list of vendors
*Apacta.VendorsApi* | [**vendorsVendorIdDelete**](docs/VendorsApi.md#vendorsVendorIdDelete) | **DELETE** /vendors/{vendor_id} | Delete a vendor
*Apacta.WagesApi* | [**wagesDownloadSalaryFileGet**](docs/WagesApi.md#wagesDownloadSalaryFileGet) | **GET** /wages/downloadSalaryFile | Download salary file
*Apacta.WallCommentsApi* | [**wallCommentsPost**](docs/WallCommentsApi.md#wallCommentsPost) | **POST** /wall_comments | Add wall comment
*Apacta.WallCommentsApi* | [**wallCommentsWallCommentIdGet**](docs/WallCommentsApi.md#wallCommentsWallCommentIdGet) | **GET** /wall_comments/{wall_comment_id} | View wall comment
*Apacta.WallPostsApi* | [**wallPostsGet**](docs/WallPostsApi.md#wallPostsGet) | **GET** /wall_posts | View list of wall posts
*Apacta.WallPostsApi* | [**wallPostsPost**](docs/WallPostsApi.md#wallPostsPost) | **POST** /wall_posts | Add a wall post
*Apacta.WallPostsApi* | [**wallPostsWallPostIdGet**](docs/WallPostsApi.md#wallPostsWallPostIdGet) | **GET** /wall_posts/{wall_post_id} | View wall post
*Apacta.WallPostsApi* | [**wallPostsWallPostIdWallCommentsGet**](docs/WallPostsApi.md#wallPostsWallPostIdWallCommentsGet) | **GET** /wall_posts/{wall_post_id}/wall_comments | See wall comments to a wall post


## Documentation for Models

 - [Apacta.ActivitiesGet200Response](docs/ActivitiesGet200Response.md)
 - [Apacta.ActivitiesPostRequest](docs/ActivitiesPostRequest.md)
 - [Apacta.Activity](docs/Activity.md)
 - [Apacta.AddCompaniesVendorRequest](docs/AddCompaniesVendorRequest.md)
 - [Apacta.AddContactPersonRequest](docs/AddContactPersonRequest.md)
 - [Apacta.AddDefaultProjectStatusesError](docs/AddDefaultProjectStatusesError.md)
 - [Apacta.AddDefaultProjectStatusesSuccess](docs/AddDefaultProjectStatusesSuccess.md)
 - [Apacta.AddVendorRequest](docs/AddVendorRequest.md)
 - [Apacta.BadRequestResponse](docs/BadRequestResponse.md)
 - [Apacta.BadRequestResponseData](docs/BadRequestResponseData.md)
 - [Apacta.BulkActionRequestBody](docs/BulkActionRequestBody.md)
 - [Apacta.BulkEditIntegrationSettingsUsersItemsRequestBody](docs/BulkEditIntegrationSettingsUsersItemsRequestBody.md)
 - [Apacta.BulkEditIntegrationSettingsUsersRequestBody](docs/BulkEditIntegrationSettingsUsersRequestBody.md)
 - [Apacta.CitiesCityIdGet200Response](docs/CitiesCityIdGet200Response.md)
 - [Apacta.CitiesGet200Response](docs/CitiesGet200Response.md)
 - [Apacta.City](docs/City.md)
 - [Apacta.ClockingRecord](docs/ClockingRecord.md)
 - [Apacta.ClockingRecordsCheckoutPost201Response](docs/ClockingRecordsCheckoutPost201Response.md)
 - [Apacta.ClockingRecordsClockingRecordIdDelete200Response](docs/ClockingRecordsClockingRecordIdDelete200Response.md)
 - [Apacta.ClockingRecordsClockingRecordIdGet200Response](docs/ClockingRecordsClockingRecordIdGet200Response.md)
 - [Apacta.ClockingRecordsClockingRecordIdPut200Response](docs/ClockingRecordsClockingRecordIdPut200Response.md)
 - [Apacta.ClockingRecordsGet200Response](docs/ClockingRecordsGet200Response.md)
 - [Apacta.ClockingRecordsPost201Response](docs/ClockingRecordsPost201Response.md)
 - [Apacta.ClockingRecordsPost201ResponseData](docs/ClockingRecordsPost201ResponseData.md)
 - [Apacta.ClockingRecordsPostRequest](docs/ClockingRecordsPostRequest.md)
 - [Apacta.CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response](docs/CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response.md)
 - [Apacta.CompaniesCompanyIdCompaniesIntegrationFeatureSettingsPostRequest](docs/CompaniesCompanyIdCompaniesIntegrationFeatureSettingsPostRequest.md)
 - [Apacta.CompaniesCompanyIdFormTemplatesGet200Response](docs/CompaniesCompanyIdFormTemplatesGet200Response.md)
 - [Apacta.CompaniesCompanyIdGet200Response](docs/CompaniesCompanyIdGet200Response.md)
 - [Apacta.CompaniesCompanyIdIntegrationFeatureSettingsGet200Response](docs/CompaniesCompanyIdIntegrationFeatureSettingsGet200Response.md)
 - [Apacta.CompaniesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet200Response](docs/CompaniesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet200Response.md)
 - [Apacta.CompaniesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet200Response](docs/CompaniesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet200Response.md)
 - [Apacta.CompaniesCompanyIdIntegrationSettingsGet200Response](docs/CompaniesCompanyIdIntegrationSettingsGet200Response.md)
 - [Apacta.CompaniesCompanyIdIntegrationSettingsPostRequest](docs/CompaniesCompanyIdIntegrationSettingsPostRequest.md)
 - [Apacta.CompaniesCompanyIdPriceMarginsPriceMarginsIdGet200Response](docs/CompaniesCompanyIdPriceMarginsPriceMarginsIdGet200Response.md)
 - [Apacta.CompaniesCompanyIdPriceMarginsPriceMarginsIdPostRequest](docs/CompaniesCompanyIdPriceMarginsPriceMarginsIdPostRequest.md)
 - [Apacta.CompaniesFormTemplates](docs/CompaniesFormTemplates.md)
 - [Apacta.CompaniesGet200Response](docs/CompaniesGet200Response.md)
 - [Apacta.CompaniesIntegrationFeatureSetting](docs/CompaniesIntegrationFeatureSetting.md)
 - [Apacta.CompaniesIntegrationSetting](docs/CompaniesIntegrationSetting.md)
 - [Apacta.CompaniesSubscriptionSelfServiceGet200Response](docs/CompaniesSubscriptionSelfServiceGet200Response.md)
 - [Apacta.CompaniesVendor](docs/CompaniesVendor.md)
 - [Apacta.Company](docs/Company.md)
 - [Apacta.CompanyPriceMargins](docs/CompanyPriceMargins.md)
 - [Apacta.CompanySettings](docs/CompanySettings.md)
 - [Apacta.Contact](docs/Contact.md)
 - [Apacta.ContactCustomFieldAttribute](docs/ContactCustomFieldAttribute.md)
 - [Apacta.ContactCustomFieldAttributesContactCustomFieldAttributeIdGet200Response](docs/ContactCustomFieldAttributesContactCustomFieldAttributeIdGet200Response.md)
 - [Apacta.ContactCustomFieldAttributesGet200Response](docs/ContactCustomFieldAttributesGet200Response.md)
 - [Apacta.ContactCustomFieldValue](docs/ContactCustomFieldValue.md)
 - [Apacta.ContactPerson](docs/ContactPerson.md)
 - [Apacta.ContactType](docs/ContactType.md)
 - [Apacta.ContactTypesContactTypeIdGet200Response](docs/ContactTypesContactTypeIdGet200Response.md)
 - [Apacta.ContactTypesGet200Response](docs/ContactTypesGet200Response.md)
 - [Apacta.ContactsContactIdContactCustomFieldValuesGet200Response](docs/ContactsContactIdContactCustomFieldValuesGet200Response.md)
 - [Apacta.ContactsContactIdGet200Response](docs/ContactsContactIdGet200Response.md)
 - [Apacta.ContactsGet200Response](docs/ContactsGet200Response.md)
 - [Apacta.ContactsPostRequest](docs/ContactsPostRequest.md)
 - [Apacta.ContactsPostRequestContactTypes](docs/ContactsPostRequestContactTypes.md)
 - [Apacta.Countries](docs/Countries.md)
 - [Apacta.CountriesCountryIdGet200Response](docs/CountriesCountryIdGet200Response.md)
 - [Apacta.CountriesGet200Response](docs/CountriesGet200Response.md)
 - [Apacta.CreateSuccessResponse](docs/CreateSuccessResponse.md)
 - [Apacta.CurrenciesCurrencyIdGet200Response](docs/CurrenciesCurrencyIdGet200Response.md)
 - [Apacta.CurrenciesGet200Response](docs/CurrenciesGet200Response.md)
 - [Apacta.Currency](docs/Currency.md)
 - [Apacta.DrivingType](docs/DrivingType.md)
 - [Apacta.Email](docs/Email.md)
 - [Apacta.EmployeeHoursGet200Response](docs/EmployeeHoursGet200Response.md)
 - [Apacta.EmployeeHoursGet200ResponseDataInner](docs/EmployeeHoursGet200ResponseDataInner.md)
 - [Apacta.EmptySuccessResponse](docs/EmptySuccessResponse.md)
 - [Apacta.ErrorNotFound](docs/ErrorNotFound.md)
 - [Apacta.ErrorNotFoundData](docs/ErrorNotFoundData.md)
 - [Apacta.ErrorValidation](docs/ErrorValidation.md)
 - [Apacta.ErrorValidationData](docs/ErrorValidationData.md)
 - [Apacta.Event](docs/Event.md)
 - [Apacta.EventsEventIdGet200Response](docs/EventsEventIdGet200Response.md)
 - [Apacta.EventsGet200Response](docs/EventsGet200Response.md)
 - [Apacta.EventsIsUserFreeGet200Response](docs/EventsIsUserFreeGet200Response.md)
 - [Apacta.EventsPostRequest](docs/EventsPostRequest.md)
 - [Apacta.Expense](docs/Expense.md)
 - [Apacta.ExpenseFile](docs/ExpenseFile.md)
 - [Apacta.ExpenseFilesExpenseFileIdGet200Response](docs/ExpenseFilesExpenseFileIdGet200Response.md)
 - [Apacta.ExpenseFilesExpenseFileIdPut200Response](docs/ExpenseFilesExpenseFileIdPut200Response.md)
 - [Apacta.ExpenseFilesGet200Response](docs/ExpenseFilesGet200Response.md)
 - [Apacta.ExpenseLine](docs/ExpenseLine.md)
 - [Apacta.ExpenseLinesExpenseLineIdGet200Response](docs/ExpenseLinesExpenseLineIdGet200Response.md)
 - [Apacta.ExpenseLinesGet200Response](docs/ExpenseLinesGet200Response.md)
 - [Apacta.ExpenseLinesPostRequest](docs/ExpenseLinesPostRequest.md)
 - [Apacta.ExpensesExpenseIdGet200Response](docs/ExpensesExpenseIdGet200Response.md)
 - [Apacta.ExpensesGet200Response](docs/ExpensesGet200Response.md)
 - [Apacta.ExpensesHighestAmountGet200Response](docs/ExpensesHighestAmountGet200Response.md)
 - [Apacta.ExpensesHighestAmountGet200ResponseDataInner](docs/ExpensesHighestAmountGet200ResponseDataInner.md)
 - [Apacta.ExpensesPostRequest](docs/ExpensesPostRequest.md)
 - [Apacta.FinancialStatisticsWorkingHoursGet200Response](docs/FinancialStatisticsWorkingHoursGet200Response.md)
 - [Apacta.FinancialStatisticsWorkingHoursGet200ResponseTimeEntriesInner](docs/FinancialStatisticsWorkingHoursGet200ResponseTimeEntriesInner.md)
 - [Apacta.ForbiddenError](docs/ForbiddenError.md)
 - [Apacta.ForbiddenErrorData](docs/ForbiddenErrorData.md)
 - [Apacta.Form](docs/Form.md)
 - [Apacta.FormField](docs/FormField.md)
 - [Apacta.FormFieldType](docs/FormFieldType.md)
 - [Apacta.FormFieldTypesFormFieldTypeIdGet200Response](docs/FormFieldTypesFormFieldTypeIdGet200Response.md)
 - [Apacta.FormFieldTypesGet200Response](docs/FormFieldTypesGet200Response.md)
 - [Apacta.FormFieldsFormFieldIdGet200Response](docs/FormFieldsFormFieldIdGet200Response.md)
 - [Apacta.FormFieldsPostRequest](docs/FormFieldsPostRequest.md)
 - [Apacta.FormTemplate](docs/FormTemplate.md)
 - [Apacta.FormTemplatesFormTemplateIdGet200Response](docs/FormTemplatesFormTemplateIdGet200Response.md)
 - [Apacta.FormTemplatesGet200Response](docs/FormTemplatesGet200Response.md)
 - [Apacta.FormsFormIdGet200Response](docs/FormsFormIdGet200Response.md)
 - [Apacta.FormsGet200Response](docs/FormsGet200Response.md)
 - [Apacta.FormsPostRequest](docs/FormsPostRequest.md)
 - [Apacta.GetCompaiesVendorsList200Response](docs/GetCompaiesVendorsList200Response.md)
 - [Apacta.GetCompaniesVendor200Response](docs/GetCompaniesVendor200Response.md)
 - [Apacta.GetCompaniesVendorsExpenseStatistics200Response](docs/GetCompaniesVendorsExpenseStatistics200Response.md)
 - [Apacta.GetCompaniesVendorsExpenseStatistics200ResponseDataInner](docs/GetCompaniesVendorsExpenseStatistics200ResponseDataInner.md)
 - [Apacta.GetCompaniesVendorsExpenseStatistics200ResponseDataInnerLastMonthInner](docs/GetCompaniesVendorsExpenseStatistics200ResponseDataInnerLastMonthInner.md)
 - [Apacta.GetCompaySettingsList200Response](docs/GetCompaySettingsList200Response.md)
 - [Apacta.GetContactPerson200Response](docs/GetContactPerson200Response.md)
 - [Apacta.GetContactPersonsList200Response](docs/GetContactPersonsList200Response.md)
 - [Apacta.GetDrivingTypes200Response](docs/GetDrivingTypes200Response.md)
 - [Apacta.GetExpensesSalesPrice200Response](docs/GetExpensesSalesPrice200Response.md)
 - [Apacta.GetFinancialStatistics200Response](docs/GetFinancialStatistics200Response.md)
 - [Apacta.GetFinancialStatistics200ResponseData](docs/GetFinancialStatistics200ResponseData.md)
 - [Apacta.GetFinancialStatisticsOverview200Response](docs/GetFinancialStatisticsOverview200Response.md)
 - [Apacta.GetFinancialStatisticsOverview200ResponseData](docs/GetFinancialStatisticsOverview200ResponseData.md)
 - [Apacta.GetIntegrationsList200Response](docs/GetIntegrationsList200Response.md)
 - [Apacta.GetInvoiceFiles200Response](docs/GetInvoiceFiles200Response.md)
 - [Apacta.GetInvoicedAmount200Response](docs/GetInvoicedAmount200Response.md)
 - [Apacta.GetMargin200Response](docs/GetMargin200Response.md)
 - [Apacta.GetMaterialRentalsCostPrice200Response](docs/GetMaterialRentalsCostPrice200Response.md)
 - [Apacta.GetOneInvoiceEmails200Response](docs/GetOneInvoiceEmails200Response.md)
 - [Apacta.GetOneInvoiceFiles200Response](docs/GetOneInvoiceFiles200Response.md)
 - [Apacta.GetProductsCostPrice200Response](docs/GetProductsCostPrice200Response.md)
 - [Apacta.GetVendor200Response](docs/GetVendor200Response.md)
 - [Apacta.GetVendorsList200Response](docs/GetVendorsList200Response.md)
 - [Apacta.IntegrationFeatureSetting](docs/IntegrationFeatureSetting.md)
 - [Apacta.IntegrationSettingsUser](docs/IntegrationSettingsUser.md)
 - [Apacta.IntegrationSettingsUsers](docs/IntegrationSettingsUsers.md)
 - [Apacta.IntegrationsBillysAuthenticatePost200Response](docs/IntegrationsBillysAuthenticatePost200Response.md)
 - [Apacta.IntegrationsProductsSyncGet200Response](docs/IntegrationsProductsSyncGet200Response.md)
 - [Apacta.Invoice](docs/Invoice.md)
 - [Apacta.InvoiceFile](docs/InvoiceFile.md)
 - [Apacta.InvoiceLine](docs/InvoiceLine.md)
 - [Apacta.InvoiceLineText](docs/InvoiceLineText.md)
 - [Apacta.InvoiceLineTextTemplate](docs/InvoiceLineTextTemplate.md)
 - [Apacta.InvoiceLineTextTemplateGet200Response](docs/InvoiceLineTextTemplateGet200Response.md)
 - [Apacta.InvoiceLineTextTemplateInvoiceLineTextTemplateIdGet200Response](docs/InvoiceLineTextTemplateInvoiceLineTextTemplateIdGet200Response.md)
 - [Apacta.InvoiceLinesGet200Response](docs/InvoiceLinesGet200Response.md)
 - [Apacta.InvoiceLinesInvoiceLineIdGet200Response](docs/InvoiceLinesInvoiceLineIdGet200Response.md)
 - [Apacta.InvoiceLinesInvoiceLineIdPutRequest](docs/InvoiceLinesInvoiceLineIdPutRequest.md)
 - [Apacta.InvoiceLinesPostRequest](docs/InvoiceLinesPostRequest.md)
 - [Apacta.InvoicesGet200Response](docs/InvoicesGet200Response.md)
 - [Apacta.InvoicesInvoiceIdGet200Response](docs/InvoicesInvoiceIdGet200Response.md)
 - [Apacta.InvoicesInvoiceIdPutRequest](docs/InvoicesInvoiceIdPutRequest.md)
 - [Apacta.InvoicesPostRequest](docs/InvoicesPostRequest.md)
 - [Apacta.MassMessage](docs/MassMessage.md)
 - [Apacta.MassMessagesUser](docs/MassMessagesUser.md)
 - [Apacta.MassMessagesUsersGet200Response](docs/MassMessagesUsersGet200Response.md)
 - [Apacta.MassMessagesUsersMassMessagesUserIdGet200Response](docs/MassMessagesUsersMassMessagesUserIdGet200Response.md)
 - [Apacta.Material](docs/Material.md)
 - [Apacta.MaterialRental](docs/MaterialRental.md)
 - [Apacta.MaterialsGet200Response](docs/MaterialsGet200Response.md)
 - [Apacta.MaterialsMaterialIdGet200Response](docs/MaterialsMaterialIdGet200Response.md)
 - [Apacta.MaterialsMaterialIdRentalsCheckoutPostRequest](docs/MaterialsMaterialIdRentalsCheckoutPostRequest.md)
 - [Apacta.MaterialsMaterialIdRentalsGet200Response](docs/MaterialsMaterialIdRentalsGet200Response.md)
 - [Apacta.MaterialsMaterialIdRentalsMaterialRentalIdGet200Response](docs/MaterialsMaterialIdRentalsMaterialRentalIdGet200Response.md)
 - [Apacta.MaterialsMaterialIdRentalsPostRequest](docs/MaterialsMaterialIdRentalsPostRequest.md)
 - [Apacta.MaterialsPostRequest](docs/MaterialsPostRequest.md)
 - [Apacta.Offer](docs/Offer.md)
 - [Apacta.OfferLine](docs/OfferLine.md)
 - [Apacta.OfferStatus](docs/OfferStatus.md)
 - [Apacta.OfferStatusesGet200Response](docs/OfferStatusesGet200Response.md)
 - [Apacta.OfferStatusesOfferStatusIdGet200Response](docs/OfferStatusesOfferStatusIdGet200Response.md)
 - [Apacta.OfferStatusesPostRequest](docs/OfferStatusesPostRequest.md)
 - [Apacta.OffersGet200Response](docs/OffersGet200Response.md)
 - [Apacta.OffersOfferIdChangelogGet200Response](docs/OffersOfferIdChangelogGet200Response.md)
 - [Apacta.OffersOfferIdGet200Response](docs/OffersOfferIdGet200Response.md)
 - [Apacta.OffersPostRequest](docs/OffersPostRequest.md)
 - [Apacta.OverviewRejectionReasonsGet200Response](docs/OverviewRejectionReasonsGet200Response.md)
 - [Apacta.PaginationDetails](docs/PaginationDetails.md)
 - [Apacta.PaymentTerm](docs/PaymentTerm.md)
 - [Apacta.PaymentTermType](docs/PaymentTermType.md)
 - [Apacta.PaymentTermTypesGet200Response](docs/PaymentTermTypesGet200Response.md)
 - [Apacta.PaymentTermTypesPaymentTermTypeIdGet200Response](docs/PaymentTermTypesPaymentTermTypeIdGet200Response.md)
 - [Apacta.PaymentTermsData](docs/PaymentTermsData.md)
 - [Apacta.PaymentTermsErpGet200Response](docs/PaymentTermsErpGet200Response.md)
 - [Apacta.PaymentTermsGet200Response](docs/PaymentTermsGet200Response.md)
 - [Apacta.PaymentTermsPaymentTermIdGet200Response](docs/PaymentTermsPaymentTermIdGet200Response.md)
 - [Apacta.PingGet200Response](docs/PingGet200Response.md)
 - [Apacta.PlannedProduct](docs/PlannedProduct.md)
 - [Apacta.PostDrivingTypesRequest](docs/PostDrivingTypesRequest.md)
 - [Apacta.Product](docs/Product.md)
 - [Apacta.ProductVariant](docs/ProductVariant.md)
 - [Apacta.ProductsGet200Response](docs/ProductsGet200Response.md)
 - [Apacta.ProductsPostRequest](docs/ProductsPostRequest.md)
 - [Apacta.ProductsProductIdGet200Response](docs/ProductsProductIdGet200Response.md)
 - [Apacta.ProductsProductIdVariantsGet200Response](docs/ProductsProductIdVariantsGet200Response.md)
 - [Apacta.Project](docs/Project.md)
 - [Apacta.ProjectCustomFieldAttribute](docs/ProjectCustomFieldAttribute.md)
 - [Apacta.ProjectCustomFieldAttributesGet200Response](docs/ProjectCustomFieldAttributesGet200Response.md)
 - [Apacta.ProjectCustomFieldAttributesProjectCustomFieldAttributeIdGet200Response](docs/ProjectCustomFieldAttributesProjectCustomFieldAttributeIdGet200Response.md)
 - [Apacta.ProjectCustomFieldValue](docs/ProjectCustomFieldValue.md)
 - [Apacta.ProjectStatus](docs/ProjectStatus.md)
 - [Apacta.ProjectStatusType](docs/ProjectStatusType.md)
 - [Apacta.ProjectStatusTypesGet200Response](docs/ProjectStatusTypesGet200Response.md)
 - [Apacta.ProjectStatusesGet200Response](docs/ProjectStatusesGet200Response.md)
 - [Apacta.ProjectStatusesPostRequest](docs/ProjectStatusesPostRequest.md)
 - [Apacta.ProjectStatusesProjectStatusIdGet200Response](docs/ProjectStatusesProjectStatusIdGet200Response.md)
 - [Apacta.ProjectsGet200Response](docs/ProjectsGet200Response.md)
 - [Apacta.ProjectsHasProjectsWithCustomStatusesGet200Response](docs/ProjectsHasProjectsWithCustomStatusesGet200Response.md)
 - [Apacta.ProjectsPostRequest](docs/ProjectsPostRequest.md)
 - [Apacta.ProjectsProjectIdAllFilesGet200Response](docs/ProjectsProjectIdAllFilesGet200Response.md)
 - [Apacta.ProjectsProjectIdGet200Response](docs/ProjectsProjectIdGet200Response.md)
 - [Apacta.ProjectsProjectIdPutRequest](docs/ProjectsProjectIdPutRequest.md)
 - [Apacta.ProjectsProjectIdSendBulkPdfPostRequest](docs/ProjectsProjectIdSendBulkPdfPostRequest.md)
 - [Apacta.ProjectsProjectIdUsersGet200Response](docs/ProjectsProjectIdUsersGet200Response.md)
 - [Apacta.ProjectsProjectIdUsersPostRequest](docs/ProjectsProjectIdUsersPostRequest.md)
 - [Apacta.ProjectsProjectIdUsersUserIdGet200Response](docs/ProjectsProjectIdUsersUserIdGet200Response.md)
 - [Apacta.Role](docs/Role.md)
 - [Apacta.RolesGet200Response](docs/RolesGet200Response.md)
 - [Apacta.Sender](docs/Sender.md)
 - [Apacta.SharedProjectContact](docs/SharedProjectContact.md)
 - [Apacta.SharedProjectVendor](docs/SharedProjectVendor.md)
 - [Apacta.StockLocation](docs/StockLocation.md)
 - [Apacta.StockLocationsGet200Response](docs/StockLocationsGet200Response.md)
 - [Apacta.StockLocationsLocationIdGet200Response](docs/StockLocationsLocationIdGet200Response.md)
 - [Apacta.StockLocationsPostRequest](docs/StockLocationsPostRequest.md)
 - [Apacta.SubscriptionSelfServiceRequestBody](docs/SubscriptionSelfServiceRequestBody.md)
 - [Apacta.TimeEntriesGet200Response](docs/TimeEntriesGet200Response.md)
 - [Apacta.TimeEntriesPostRequest](docs/TimeEntriesPostRequest.md)
 - [Apacta.TimeEntriesTimeEntryIdGet200Response](docs/TimeEntriesTimeEntryIdGet200Response.md)
 - [Apacta.TimeEntry](docs/TimeEntry.md)
 - [Apacta.TimeEntryInterval](docs/TimeEntryInterval.md)
 - [Apacta.TimeEntryIntervalsGet200Response](docs/TimeEntryIntervalsGet200Response.md)
 - [Apacta.TimeEntryIntervalsTimeEntryIntervalIdGet200Response](docs/TimeEntryIntervalsTimeEntryIntervalIdGet200Response.md)
 - [Apacta.TimeEntryRate](docs/TimeEntryRate.md)
 - [Apacta.TimeEntryRatesGet200Response](docs/TimeEntryRatesGet200Response.md)
 - [Apacta.TimeEntryRatesTimeEntryRateIdGet200Response](docs/TimeEntryRatesTimeEntryRateIdGet200Response.md)
 - [Apacta.TimeEntryRuleGroup](docs/TimeEntryRuleGroup.md)
 - [Apacta.TimeEntryRuleGroupsGet200Response](docs/TimeEntryRuleGroupsGet200Response.md)
 - [Apacta.TimeEntryType](docs/TimeEntryType.md)
 - [Apacta.TimeEntryTypesGet200Response](docs/TimeEntryTypesGet200Response.md)
 - [Apacta.TimeEntryTypesPostRequest](docs/TimeEntryTypesPostRequest.md)
 - [Apacta.TimeEntryTypesTimeEntryTypeIdGet200Response](docs/TimeEntryTypesTimeEntryTypeIdGet200Response.md)
 - [Apacta.TimeEntryUnitType](docs/TimeEntryUnitType.md)
 - [Apacta.TimeEntryUnitTypesGet200Response](docs/TimeEntryUnitTypesGet200Response.md)
 - [Apacta.TimeEntryUnitTypesTimeEntryUnitTypeIdGet200Response](docs/TimeEntryUnitTypesTimeEntryUnitTypeIdGet200Response.md)
 - [Apacta.TimeEntryValueType](docs/TimeEntryValueType.md)
 - [Apacta.TimeEntryValueTypesGet200Response](docs/TimeEntryValueTypesGet200Response.md)
 - [Apacta.TimeEntryValueTypesTimeEntryValueTypeIdGet200Response](docs/TimeEntryValueTypesTimeEntryValueTypeIdGet200Response.md)
 - [Apacta.UnauthorizedError](docs/UnauthorizedError.md)
 - [Apacta.UnauthorizedErrorData](docs/UnauthorizedErrorData.md)
 - [Apacta.User](docs/User.md)
 - [Apacta.UserCustomFieldAttribute](docs/UserCustomFieldAttribute.md)
 - [Apacta.UserCustomFieldAttributesGet200Response](docs/UserCustomFieldAttributesGet200Response.md)
 - [Apacta.UserCustomFieldAttributesUserCustomFieldAttributeIdGet200Response](docs/UserCustomFieldAttributesUserCustomFieldAttributeIdGet200Response.md)
 - [Apacta.UserCustomFieldValue](docs/UserCustomFieldValue.md)
 - [Apacta.UsersPostRequest](docs/UsersPostRequest.md)
 - [Apacta.UsersResendWelcomeSmsGet200Response](docs/UsersResendWelcomeSmsGet200Response.md)
 - [Apacta.UsersResendWelcomeSmsGet200ResponseData](docs/UsersResendWelcomeSmsGet200ResponseData.md)
 - [Apacta.UsersUserIdIntegrationSettingsGet200Response](docs/UsersUserIdIntegrationSettingsGet200Response.md)
 - [Apacta.UsersUserIdIntegrationSettingsIntegrationSettingsUserIdGet200Response](docs/UsersUserIdIntegrationSettingsIntegrationSettingsUserIdGet200Response.md)
 - [Apacta.UsersUserIdUserCustomFieldValueGet200Response](docs/UsersUserIdUserCustomFieldValueGet200Response.md)
 - [Apacta.UsersUserIdUserCustomFieldValueUserCustomFieldValueIdGet200Response](docs/UsersUserIdUserCustomFieldValueUserCustomFieldValueIdGet200Response.md)
 - [Apacta.UsersUserIdUserCustomFieldValueUserCustomFieldValueIdPut200Response](docs/UsersUserIdUserCustomFieldValueUserCustomFieldValueIdPut200Response.md)
 - [Apacta.Vendor](docs/Vendor.md)
 - [Apacta.VendorProduct](docs/VendorProduct.md)
 - [Apacta.VendorProductPriceFile](docs/VendorProductPriceFile.md)
 - [Apacta.VendorProductPriceFilesGet200Response](docs/VendorProductPriceFilesGet200Response.md)
 - [Apacta.VendorProductPriceFilesVendorProductPriceFileIdGet200Response](docs/VendorProductPriceFilesVendorProductPriceFileIdGet200Response.md)
 - [Apacta.VendorProductPriceFilesVendorProductPriceFileIdGet200ResponseData](docs/VendorProductPriceFilesVendorProductPriceFileIdGet200ResponseData.md)
 - [Apacta.VendorProductsGet200Response](docs/VendorProductsGet200Response.md)
 - [Apacta.VendorProductsVendorProductIdGet200Response](docs/VendorProductsVendorProductIdGet200Response.md)
 - [Apacta.WallComment](docs/WallComment.md)
 - [Apacta.WallCommentsPostRequest](docs/WallCommentsPostRequest.md)
 - [Apacta.WallCommentsWallCommentIdGet200Response](docs/WallCommentsWallCommentIdGet200Response.md)
 - [Apacta.WallPost](docs/WallPost.md)
 - [Apacta.WallPostsGet200Response](docs/WallPostsGet200Response.md)
 - [Apacta.WallPostsPostRequest](docs/WallPostsPostRequest.md)
 - [Apacta.WallPostsWallPostIdGet200Response](docs/WallPostsWallPostIdGet200Response.md)
 - [Apacta.WallPostsWallPostIdWallCommentsGet200Response](docs/WallPostsWallPostIdWallCommentsGet200Response.md)


## Documentation for Authorization


Authentication schemes defined for the API:
### X-Auth-Token


- **Type**: API key
- **API key parameter name**: X-Auth-Token
- **Location**: HTTP header

### api_key


- **Type**: API key
- **API key parameter name**: api_token
- **Location**: URL query string

