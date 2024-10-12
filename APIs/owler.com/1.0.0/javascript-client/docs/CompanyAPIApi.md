# Owler.CompanyAPIApi

All URIs are relative to *https://api.owler.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**basicCompanySearch**](CompanyAPIApi.md#basicCompanySearch) | **GET** /v1/company/basicsearch | Basic Search Company by Ticker or Website or Name or PermID
[**fuzzyCompanySearch**](CompanyAPIApi.md#fuzzyCompanySearch) | **GET** /v1/company/fuzzysearch | Fuzzy Search Company by Name or Address or Phone
[**searchCompany**](CompanyAPIApi.md#searchCompany) | **GET** /v1/company/search | Search Company by Ticker or Website or Name or PermID
[**v1CompanyIdCompanyIdGet**](CompanyAPIApi.md#v1CompanyIdCompanyIdGet) | **GET** /v1/company/id/{companyId} | Get Company by Id
[**v1CompanyUrlWebsiteGet**](CompanyAPIApi.md#v1CompanyUrlWebsiteGet) | **GET** /v1/company/url/{website} | Get Company by URL



## basicCompanySearch

> BasicResults basicCompanySearch(q, opts)

Basic Search Company by Ticker or Website or Name or PermID

The Company Basic Search API searches for a company based on the input and will returns results containing basic details about matching companies. By default the API returns the top 10 available results unless the limit is specified. The maximum limit is restricted to 30.

### Example

```javascript
import Owler from 'owler';
let defaultClient = Owler.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new Owler.CompanyAPIApi();
let q = "q_example"; // String | Search term
let opts = {
  'fields': ["null"], // [String] | Fields to be searched - name, website, ticker, permid. If not specfied, will be searched against all fields
  'limit': "limit_example", // String | Number of results to be displayed - 10 (by default, if not specified) to 30
  'format': "'json'" // String | Format of the response content - json (by default if not specified), xml
};
apiInstance.basicCompanySearch(q, opts, (error, data, response) => {
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
 **q** | **String**| Search term | 
 **fields** | [**[String]**](String.md)| Fields to be searched - name, website, ticker, permid. If not specfied, will be searched against all fields | [optional] 
 **limit** | **String**| Number of results to be displayed - 10 (by default, if not specified) to 30 | [optional] 
 **format** | **String**| Format of the response content - json (by default if not specified), xml | [optional] [default to &#39;json&#39;]

### Return type

[**BasicResults**](BasicResults.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## fuzzyCompanySearch

> Object fuzzyCompanySearch(q, fields, opts)

Fuzzy Search Company by Name or Address or Phone

The Company Fuzzy Search API searches for a company based on the input and will return results containing basic details about matching companies. By default the API returns at most top 10 available results unless the limit is specified. The maximum limit is restricted to 30.

### Example

```javascript
import Owler from 'owler';
let defaultClient = Owler.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new Owler.CompanyAPIApi();
let q = "q_example"; // String | Search term
let fields = ["null"]; // [String] | Fields to be searched - name, website, ticker, permid, address, phone. Each field and its corresponding value has to be specified
let opts = {
  'limit': "limit_example", // String | Number of results to be displayed - 10 (by default, if not specified) to 30
  'format': "'json'" // String | Format of the response content - json (by default if not specified), xml
};
apiInstance.fuzzyCompanySearch(q, fields, opts, (error, data, response) => {
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
 **q** | **String**| Search term | 
 **fields** | [**[String]**](String.md)| Fields to be searched - name, website, ticker, permid, address, phone. Each field and its corresponding value has to be specified | 
 **limit** | **String**| Number of results to be displayed - 10 (by default, if not specified) to 30 | [optional] 
 **format** | **String**| Format of the response content - json (by default if not specified), xml | [optional] [default to &#39;json&#39;]

### Return type

**Object**

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## searchCompany

> Results searchCompany(q, opts)

Search Company by Ticker or Website or Name or PermID

The Company Search API searches for a company based on the input and will returns results containing basic details about matching companies. By default the API returns the top 10 available results unless the limit is specified. The maximum limit is restricted to 30.

### Example

```javascript
import Owler from 'owler';
let defaultClient = Owler.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new Owler.CompanyAPIApi();
let q = "q_example"; // String | Search term
let opts = {
  'fields': ["null"], // [String] | Fields to be searched - name, website, ticker. If not specified, will be searched against all fields
  'limit': "limit_example", // String | Number of results to be displayed - 10 (by default, if not specified) to 30
  'format': "'json'" // String | Format of the response content - json (by default if not specified), xml
};
apiInstance.searchCompany(q, opts, (error, data, response) => {
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
 **q** | **String**| Search term | 
 **fields** | [**[String]**](String.md)| Fields to be searched - name, website, ticker. If not specified, will be searched against all fields | [optional] 
 **limit** | **String**| Number of results to be displayed - 10 (by default, if not specified) to 30 | [optional] 
 **format** | **String**| Format of the response content - json (by default if not specified), xml | [optional] [default to &#39;json&#39;]

### Return type

[**Results**](Results.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## v1CompanyIdCompanyIdGet

> Company v1CompanyIdCompanyIdGet(companyId, opts)

Get Company by Id

The Company Data API provides complete information about a company for the specified Company Id 

### Example

```javascript
import Owler from 'owler';
let defaultClient = Owler.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new Owler.CompanyAPIApi();
let companyId = "companyId_example"; // String | Company Id
let opts = {
  'format': "'json'" // String | Format of the response content - json (by default if not specified), xml
};
apiInstance.v1CompanyIdCompanyIdGet(companyId, opts, (error, data, response) => {
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
 **companyId** | **String**| Company Id | 
 **format** | **String**| Format of the response content - json (by default if not specified), xml | [optional] [default to &#39;json&#39;]

### Return type

[**Company**](Company.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## v1CompanyUrlWebsiteGet

> Company v1CompanyUrlWebsiteGet(website, opts)

Get Company by URL

The Company Data API provides complete information about a company for the specified URL 

### Example

```javascript
import Owler from 'owler';
let defaultClient = Owler.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new Owler.CompanyAPIApi();
let website = "website_example"; // String | Company Domain
let opts = {
  'format': "'json'" // String | Format of the response content - json (by default if not specified), xml
};
apiInstance.v1CompanyUrlWebsiteGet(website, opts, (error, data, response) => {
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
 **website** | **String**| Company Domain | 
 **format** | **String**| Format of the response content - json (by default if not specified), xml | [optional] [default to &#39;json&#39;]

### Return type

[**Company**](Company.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

