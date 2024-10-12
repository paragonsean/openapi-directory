# Owler.CompetitorAPIApi

All URIs are relative to *https://api.owler.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1CompanyCompetitorIdCompanyIdGet**](CompetitorAPIApi.md#v1CompanyCompetitorIdCompanyIdGet) | **GET** /v1/company/competitor/id/{companyId} | Get Competitor information by Id
[**v1CompanyCompetitorUrlWebsiteGet**](CompetitorAPIApi.md#v1CompanyCompetitorUrlWebsiteGet) | **GET** /v1/company/competitor/url/{website} | Get Competitor information by URL



## v1CompanyCompetitorIdCompanyIdGet

> CompanyCompetitorVO v1CompanyCompetitorIdCompanyIdGet(companyId, opts)

Get Competitor information by Id

The Competitors API provides basic information about top 3 competitors of a company specified in the Company Id

### Example

```javascript
import Owler from 'owler';
let defaultClient = Owler.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new Owler.CompetitorAPIApi();
let companyId = "companyId_example"; // String | Company Id
let opts = {
  'format': "'json'" // String | Format of the response content - json (by default if not specified), xml
};
apiInstance.v1CompanyCompetitorIdCompanyIdGet(companyId, opts, (error, data, response) => {
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

[**CompanyCompetitorVO**](CompanyCompetitorVO.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## v1CompanyCompetitorUrlWebsiteGet

> CompanyCompetitorVO v1CompanyCompetitorUrlWebsiteGet(website, opts)

Get Competitor information by URL

The Competitors API provides basic information about top 3 competitors of a company specified in the website

### Example

```javascript
import Owler from 'owler';
let defaultClient = Owler.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new Owler.CompetitorAPIApi();
let website = "website_example"; // String | Company Id
let opts = {
  'format': "'json'" // String | Format of the response content - json (by default if not specified), xml
};
apiInstance.v1CompanyCompetitorUrlWebsiteGet(website, opts, (error, data, response) => {
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
 **website** | **String**| Company Id | 
 **format** | **String**| Format of the response content - json (by default if not specified), xml | [optional] [default to &#39;json&#39;]

### Return type

[**CompanyCompetitorVO**](CompanyCompetitorVO.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

