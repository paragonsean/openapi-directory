# Owler.CompanyPremiumAPIApi

All URIs are relative to *https://api.owler.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1CompanypremiumIdCompanyIdGet**](CompanyPremiumAPIApi.md#v1CompanypremiumIdCompanyIdGet) | **GET** /v1/companypremium/id/{companyId} | Get Complete Company Info by Id
[**v1CompanypremiumUrlWebsiteGet**](CompanyPremiumAPIApi.md#v1CompanypremiumUrlWebsiteGet) | **GET** /v1/companypremium/url/{website} | Get Basic Company Info by Url



## v1CompanypremiumIdCompanyIdGet

> Company v1CompanypremiumIdCompanyIdGet(companyId, opts)

Get Complete Company Info by Id

The Company Premium Data API provides complete information about a company for the specified Company Id 

### Example

```javascript
import Owler from 'owler';
let defaultClient = Owler.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new Owler.CompanyPremiumAPIApi();
let companyId = "companyId_example"; // String | Company Id
let opts = {
  'format': "'json'" // String | Format of the response content - json (by default if not specified), xml
};
apiInstance.v1CompanypremiumIdCompanyIdGet(companyId, opts, (error, data, response) => {
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


## v1CompanypremiumUrlWebsiteGet

> Company v1CompanypremiumUrlWebsiteGet(website, opts)

Get Basic Company Info by Url

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

let apiInstance = new Owler.CompanyPremiumAPIApi();
let website = "website_example"; // String | Company Domain
let opts = {
  'format': "'json'" // String | Format of the response content - json (by default if not specified), xml
};
apiInstance.v1CompanypremiumUrlWebsiteGet(website, opts, (error, data, response) => {
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

