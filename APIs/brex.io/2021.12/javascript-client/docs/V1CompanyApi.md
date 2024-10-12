# KycApiDocumentation.V1CompanyApi

All URIs are relative to *https://api.kompany.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companyAlternativeSearch**](V1CompanyApi.md#companyAlternativeSearch) | **POST** /api/v1/company/search/{country} | Retrieves a list of companies from the KYC API company index
[**companyAnnouncement**](V1CompanyApi.md#companyAnnouncement) | **GET** /api/v1/company/announcement/{id} | Retrieves announcement data
[**companyDeepsearchISIN**](V1CompanyApi.md#companyDeepsearchISIN) | **POST** /api/v1/company/deepsearch/isin | Retrieves a list of stock exchange listings
[**companyDeepsearchLEI**](V1CompanyApi.md#companyDeepsearchLEI) | **GET** /api/v1/company/deepsearch/lei/{number} | Retrieves a list of companies
[**companyDeepsearchName**](V1CompanyApi.md#companyDeepsearchName) | **GET** /api/v1/company/deepsearch/name/{country}/{name} | Retrieves a list of companies from the official business register
[**companyDeepsearchNumber**](V1CompanyApi.md#companyDeepsearchNumber) | **GET** /api/v1/company/deepsearch/number/{country}/{number} | Retrieves a list of companies from the official business register
[**companyIdAnnouncements**](V1CompanyApi.md#companyIdAnnouncements) | **GET** /api/v1/company/{id}/announcements | Retrieves company announcements
[**companyIdDataset**](V1CompanyApi.md#companyIdDataset) | **GET** /api/v1/company/{id}/{dataset} | Retrieves company details
[**companyIdSuper**](V1CompanyApi.md#companyIdSuper) | **GET** /api/v1/company/{id}/super/{country} | Retrieves structured data extracted from a company document
[**companyMonitorChangeTypesList**](V1CompanyApi.md#companyMonitorChangeTypesList) | **GET** /api/v1/company/monitoring/changeTypes | Get available ChangeTypes
[**companyMonitorId**](V1CompanyApi.md#companyMonitorId) | **GET** /api/v1/company/monitoring/list/{id} | Get monitor status for specific company id
[**companyMonitorList**](V1CompanyApi.md#companyMonitorList) | **GET** /api/v1/company/monitoring/list | Retrieves a list of registered monitors
[**companyMonitorRegister**](V1CompanyApi.md#companyMonitorRegister) | **POST** /api/v1/company/monitoring/register/{id} | Register a Company for monitoring
[**companyMonitorUnregister**](V1CompanyApi.md#companyMonitorUnregister) | **POST** /api/v1/company/monitoring/unregister/{id} | Deactivates an active notification
[**companyNotificationId**](V1CompanyApi.md#companyNotificationId) | **GET** /api/v1/company/notification/list/{id} | Retrieves a list of registered notifications
[**companyNotificationList**](V1CompanyApi.md#companyNotificationList) | **GET** /api/v1/company/notification/list | Retrieves a list of registered notifications
[**companyNotificationRegister**](V1CompanyApi.md#companyNotificationRegister) | **POST** /api/v1/company/notification/register/{id} | Creates a new notification
[**companyNotificationUnregister**](V1CompanyApi.md#companyNotificationUnregister) | **POST** /api/v1/company/notification/unregister/{id} | Unregister a company from Monitoring
[**companySearchName**](V1CompanyApi.md#companySearchName) | **GET** /api/v1/company/search/name/{country}/{name} | Retrieves a list of companies from the KYC API company index
[**companySearchNumber**](V1CompanyApi.md#companySearchNumber) | **GET** /api/v1/company/search/number/{country}/{number} | Retrieves a list of companies from the KYC API company index



## companyAlternativeSearch

> companyAlternativeSearch(country, opts)

Retrieves a list of companies from the KYC API company index

KYC API company index lookup by country and mixed parameters. This function requires a country code then a mixture of name

### Example

```javascript
import KycApiDocumentation from 'kyc_api_documentation';
let defaultClient = KycApiDocumentation.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new KycApiDocumentation.V1CompanyApi();
let country = "country_example"; // String | ISO_3166-1_alpha-2 representation of a country name - 2 chars
let opts = {
  'address': "address_example", // String | Company address (or address partial)
  'name': "name_example", // String | Company name
  'number': "number_example", // String | Company registration number
  'phone': "phone_example", // String | Company contact phone number
  'url': "url_example", // String | Company url
  'vat': "vat_example" // String | Company VAT number
};
apiInstance.companyAlternativeSearch(country, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **String**| ISO_3166-1_alpha-2 representation of a country name - 2 chars | 
 **address** | **String**| Company address (or address partial) | [optional] 
 **name** | **String**| Company name | [optional] 
 **number** | **String**| Company registration number | [optional] 
 **phone** | **String**| Company contact phone number | [optional] 
 **url** | **String**| Company url | [optional] 
 **vat** | **String**| Company VAT number | [optional] 

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined


## companyAnnouncement

> [CompanyAnnouncement200ResponseInner] companyAnnouncement(id)

Retrieves announcement data

Request full announcement data identified by announcement id

### Example

```javascript
import KycApiDocumentation from 'kyc_api_documentation';
let defaultClient = KycApiDocumentation.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new KycApiDocumentation.V1CompanyApi();
let id = "id_example"; // String | announcement hex ID
apiInstance.companyAnnouncement(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| announcement hex ID | 

### Return type

[**[CompanyAnnouncement200ResponseInner]**](CompanyAnnouncement200ResponseInner.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## companyDeepsearchISIN

> [CompanyDeepsearchISIN200ResponseInner] companyDeepsearchISIN(opts)

Retrieves a list of stock exchange listings

Lookup stock exchange listings identified by an ISIN (International Securities Identification Number) number. Search is forwarded to a provider.

### Example

```javascript
import KycApiDocumentation from 'kyc_api_documentation';
let defaultClient = KycApiDocumentation.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new KycApiDocumentation.V1CompanyApi();
let opts = {
  'isin': "isin_example" // String | A list of ISIN numbers seperated by comma (maximum) is 100
};
apiInstance.companyDeepsearchISIN(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **isin** | **String**| A list of ISIN numbers seperated by comma (maximum) is 100 | [optional] 

### Return type

[**[CompanyDeepsearchISIN200ResponseInner]**](CompanyDeepsearchISIN200ResponseInner.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## companyDeepsearchLEI

> CompanyDeepsearchLEI200Response companyDeepsearchLEI(number, opts)

Retrieves a list of companies

Lookup companies identified by a LEI (Legal Entity Identifier) number. Search is forwarded to a provider.

### Example

```javascript
import KycApiDocumentation from 'kyc_api_documentation';
let defaultClient = KycApiDocumentation.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new KycApiDocumentation.V1CompanyApi();
let number = "number_example"; // String | lei number
let opts = {
  'page': 1 // Number | Pagination for the ISIN number results (1000 numbers per page)
};
apiInstance.companyDeepsearchLEI(number, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **number** | **String**| lei number | 
 **page** | **Number**| Pagination for the ISIN number results (1000 numbers per page) | [optional] 

### Return type

[**CompanyDeepsearchLEI200Response**](CompanyDeepsearchLEI200Response.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## companyDeepsearchName

> companyDeepsearchName(country, name)

Retrieves a list of companies from the official business register

Search for companies with a certain name. Search is forwarded to the respective business register of the country.

### Example

```javascript
import KycApiDocumentation from 'kyc_api_documentation';
let defaultClient = KycApiDocumentation.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new KycApiDocumentation.V1CompanyApi();
let country = "country_example"; // String | ISO_3166-1_alpha-2 representation of a country name - 2 chars
let name = "name_example"; // String | company name
apiInstance.companyDeepsearchName(country, name, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **String**| ISO_3166-1_alpha-2 representation of a country name - 2 chars | 
 **name** | **String**| company name | 

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## companyDeepsearchNumber

> companyDeepsearchNumber(country, number)

Retrieves a list of companies from the official business register

Search for companies with a certain register number. Search is forwarded to the respective business register of the country.

### Example

```javascript
import KycApiDocumentation from 'kyc_api_documentation';
let defaultClient = KycApiDocumentation.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new KycApiDocumentation.V1CompanyApi();
let country = "country_example"; // String | ISO_3166-1_alpha-2 representation of a country name - 2 chars
let number = "number_example"; // String | company registration number
apiInstance.companyDeepsearchNumber(country, number, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **String**| ISO_3166-1_alpha-2 representation of a country name - 2 chars | 
 **number** | **String**| company registration number | 

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## companyIdAnnouncements

> companyIdAnnouncements(id, opts)

Retrieves company announcements

Search announcements filed to the business register from a company identified by an id

### Example

```javascript
import KycApiDocumentation from 'kyc_api_documentation';
let defaultClient = KycApiDocumentation.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new KycApiDocumentation.V1CompanyApi();
let id = "id_example"; // String | company hex ID
let opts = {
  'limit': 56, // Number | limit of announcements in response (default 10)
  'offset': 56, // Number | to paginate through results (default 0)
  'data': true // Boolean | If this parameter is set to false, you will only receive ids, and no additional data about announcements and no hits to the metric will be counted. (and potentially minimizing your costs)
};
apiInstance.companyIdAnnouncements(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| company hex ID | 
 **limit** | **Number**| limit of announcements in response (default 10) | [optional] 
 **offset** | **Number**| to paginate through results (default 0) | [optional] 
 **data** | **Boolean**| If this parameter is set to false, you will only receive ids, and no additional data about announcements and no hits to the metric will be counted. (and potentially minimizing your costs) | [optional] 

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## companyIdDataset

> Object companyIdDataset(id, dataset, opts)

Retrieves company details

Get company details by id. The level of details is defined by the dataset parameter

### Example

```javascript
import KycApiDocumentation from 'kyc_api_documentation';
let defaultClient = KycApiDocumentation.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new KycApiDocumentation.V1CompanyApi();
let id = "id_example"; // String | company master data by id
let dataset = "dataset_example"; // String | company master data by id
let opts = {
  'checkStockListing': true, // Boolean | Try to retrieve additional stock information for this company. (Only available on refresh)
  'lang': "lang_example" // String | Optional data translation (only available in limited jurisdictions)
};
apiInstance.companyIdDataset(id, dataset, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| company master data by id | 
 **dataset** | **String**| company master data by id | 
 **checkStockListing** | **Boolean**| Try to retrieve additional stock information for this company. (Only available on refresh) | [optional] 
 **lang** | **String**| Optional data translation (only available in limited jurisdictions) | [optional] 

### Return type

**Object**

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## companyIdSuper

> companyIdSuper(id, country, opts)

Retrieves structured data extracted from a company document

Request company superdata identified by company id

### Example

```javascript
import KycApiDocumentation from 'kyc_api_documentation';
let defaultClient = KycApiDocumentation.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new KycApiDocumentation.V1CompanyApi();
let id = "id_example"; // String | company superdata by id
let country = "country_example"; // String | ISO_3166-1_alpha-2 representation of a country name - 2 chars
let opts = {
  'lang': "lang_example" // String | Optional data translation (only available in limited jurisdictions)
};
apiInstance.companyIdSuper(id, country, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| company superdata by id | 
 **country** | **String**| ISO_3166-1_alpha-2 representation of a country name - 2 chars | 
 **lang** | **String**| Optional data translation (only available in limited jurisdictions) | [optional] 

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## companyMonitorChangeTypesList

> [String] companyMonitorChangeTypesList()

Get available ChangeTypes

Get current list of available ChangeTypes to subscribe to

### Example

```javascript
import KycApiDocumentation from 'kyc_api_documentation';
let defaultClient = KycApiDocumentation.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new KycApiDocumentation.V1CompanyApi();
apiInstance.companyMonitorChangeTypesList((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**[String]**

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## companyMonitorId

> companyMonitorId(id)

Get monitor status for specific company id

Query status of registered monitors for a specific company identified by a company id

### Example

```javascript
import KycApiDocumentation from 'kyc_api_documentation';
let defaultClient = KycApiDocumentation.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new KycApiDocumentation.V1CompanyApi();
let id = "id_example"; // String | Company Hex ID
apiInstance.companyMonitorId(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| Company Hex ID | 

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## companyMonitorList

> companyMonitorList()

Retrieves a list of registered monitors

Query list of all registered monitors for logged in user

### Example

```javascript
import KycApiDocumentation from 'kyc_api_documentation';
let defaultClient = KycApiDocumentation.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new KycApiDocumentation.V1CompanyApi();
apiInstance.companyMonitorList((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## companyMonitorRegister

> companyMonitorRegister(id, callbackUrl, changeType)

Register a Company for monitoring

Add a company to your perpetual monitoring list and register a callback URL to get monitoring alerts.

### Example

```javascript
import KycApiDocumentation from 'kyc_api_documentation';
let defaultClient = KycApiDocumentation.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new KycApiDocumentation.V1CompanyApi();
let id = "id_example"; // String | Company Hex ID
let callbackUrl = "callbackUrl_example"; // String | Callback URL
let changeType = "changeType_example"; // String | ChangeType to monitor
apiInstance.companyMonitorRegister(id, callbackUrl, changeType, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| Company Hex ID | 
 **callbackUrl** | **String**| Callback URL | 
 **changeType** | **String**| ChangeType to monitor | 

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined


## companyMonitorUnregister

> companyMonitorUnregister(id)

Deactivates an active notification

Deactivate a previously registered company monitor identified by the notifier id

### Example

```javascript
import KycApiDocumentation from 'kyc_api_documentation';
let defaultClient = KycApiDocumentation.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new KycApiDocumentation.V1CompanyApi();
let id = "id_example"; // String | Registration id of monitoring request record
apiInstance.companyMonitorUnregister(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| Registration id of monitoring request record | 

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## companyNotificationId

> [CompanyNotificationId200ResponseInner] companyNotificationId(id)

Retrieves a list of registered notifications

Query list of registered notifications for a specific company identified by a company id

### Example

```javascript
import KycApiDocumentation from 'kyc_api_documentation';
let defaultClient = KycApiDocumentation.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new KycApiDocumentation.V1CompanyApi();
let id = "id_example"; // String | Company Hex ID
apiInstance.companyNotificationId(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| Company Hex ID | 

### Return type

[**[CompanyNotificationId200ResponseInner]**](CompanyNotificationId200ResponseInner.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## companyNotificationList

> companyNotificationList()

Retrieves a list of registered notifications

Query list of registered callback URLs for logged in user

### Example

```javascript
import KycApiDocumentation from 'kyc_api_documentation';
let defaultClient = KycApiDocumentation.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new KycApiDocumentation.V1CompanyApi();
apiInstance.companyNotificationList((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## companyNotificationRegister

> CompanyNotificationRegister200Response companyNotificationRegister(id, callbackUrl)

Creates a new notification

Register a new callback URL to get notifications about companies.

### Example

```javascript
import KycApiDocumentation from 'kyc_api_documentation';
let defaultClient = KycApiDocumentation.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new KycApiDocumentation.V1CompanyApi();
let id = "id_example"; // String | Company Hex ID
let callbackUrl = "callbackUrl_example"; // String | Callback URL
apiInstance.companyNotificationRegister(id, callbackUrl, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| Company Hex ID | 
 **callbackUrl** | **String**| Callback URL | 

### Return type

[**CompanyNotificationRegister200Response**](CompanyNotificationRegister200Response.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## companyNotificationUnregister

> companyNotificationUnregister(id)

Unregister a company from Monitoring

Deactivate a previously registered company monitor identified by the notifier id

### Example

```javascript
import KycApiDocumentation from 'kyc_api_documentation';
let defaultClient = KycApiDocumentation.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new KycApiDocumentation.V1CompanyApi();
let id = "id_example"; // String | Registration id of monitoring request record
apiInstance.companyNotificationUnregister(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| Registration id of monitoring request record | 

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## companySearchName

> [CompanySearchName200ResponseInner] companySearchName(country, name, opts)

Retrieves a list of companies from the KYC API company index

KYC API company index lookup for companies with a certain name in a country.

### Example

```javascript
import KycApiDocumentation from 'kyc_api_documentation';
let defaultClient = KycApiDocumentation.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new KycApiDocumentation.V1CompanyApi();
let country = "country_example"; // String | ISO_3166-1_alpha-2 representation of a country name - 2 chars
let name = "name_example"; // String | company name
let opts = {
  'limit': 789 // Number | number of search results
};
apiInstance.companySearchName(country, name, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **String**| ISO_3166-1_alpha-2 representation of a country name - 2 chars | 
 **name** | **String**| company name | 
 **limit** | **Number**| number of search results | [optional] 

### Return type

[**[CompanySearchName200ResponseInner]**](CompanySearchName200ResponseInner.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## companySearchNumber

> companySearchNumber(country, number, opts)

Retrieves a list of companies from the KYC API company index

KYC API company index lookup for companies with a certain register number in a country.

### Example

```javascript
import KycApiDocumentation from 'kyc_api_documentation';
let defaultClient = KycApiDocumentation.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new KycApiDocumentation.V1CompanyApi();
let country = "country_example"; // String | ISO_3166-1_alpha-2 representation of a country name - 2 chars
let number = "number_example"; // String | company registration number
let opts = {
  'limit': 789 // Number | number of search results
};
apiInstance.companySearchNumber(country, number, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **String**| ISO_3166-1_alpha-2 representation of a country name - 2 chars | 
 **number** | **String**| company registration number | 
 **limit** | **Number**| number of search results | [optional] 

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

