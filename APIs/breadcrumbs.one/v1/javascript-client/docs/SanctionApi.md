# BreadcrumbsOne.SanctionApi

All URIs are relative to *https://api.breadcrumbs.one*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sanctionedAddressPost**](SanctionApi.md#sanctionedAddressPost) | **POST** /sanctioned_address | Verify if the addresses provided are in our sanctioned lists



## sanctionedAddressPost

> BreadcrumbsAPIModelsSanctionSanctionedResponse sanctionedAddressPost(opts)

Verify if the addresses provided are in our sanctioned lists

### Example

```javascript
import BreadcrumbsOne from 'breadcrumbs_one';
let defaultClient = BreadcrumbsOne.ApiClient.instance;
// Configure API key authorization: X-API-KEY
let X-API-KEY = defaultClient.authentications['X-API-KEY'];
X-API-KEY.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-API-KEY.apiKeyPrefix = 'Token';

let apiInstance = new BreadcrumbsOne.SanctionApi();
let opts = {
  'breadcrumbsAPIModelsSanctionSanctionedRequest': [new BreadcrumbsOne.BreadcrumbsAPIModelsSanctionSanctionedRequest()] // [BreadcrumbsAPIModelsSanctionSanctionedRequest] | 
};
apiInstance.sanctionedAddressPost(opts, (error, data, response) => {
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
 **breadcrumbsAPIModelsSanctionSanctionedRequest** | [**[BreadcrumbsAPIModelsSanctionSanctionedRequest]**](BreadcrumbsAPIModelsSanctionSanctionedRequest.md)|  | [optional] 

### Return type

[**BreadcrumbsAPIModelsSanctionSanctionedResponse**](BreadcrumbsAPIModelsSanctionSanctionedResponse.md)

### Authorization

[X-API-KEY](../README.md#X-API-KEY)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/json

