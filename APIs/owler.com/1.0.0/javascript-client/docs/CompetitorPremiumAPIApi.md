# Owler.CompetitorPremiumAPIApi

All URIs are relative to *https://api.owler.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1CompanyCompetitorpremiumIdCompanyIdGet**](CompetitorPremiumAPIApi.md#v1CompanyCompetitorpremiumIdCompanyIdGet) | **GET** /v1/company/competitorpremium/id/{companyId} | Get Competitor information by Id
[**v1CompanyCompetitorpremiumUrlWebsiteGet**](CompetitorPremiumAPIApi.md#v1CompanyCompetitorpremiumUrlWebsiteGet) | **GET** /v1/company/competitorpremium/url/{website} | Get Competitor information by Url



## v1CompanyCompetitorpremiumIdCompanyIdGet

> Competitors v1CompanyCompetitorpremiumIdCompanyIdGet(companyId, opts)

Get Competitor information by Id

The Competitors API provides basic information about all competitors of a given company Id

### Example

```javascript
import Owler from 'owler';
let defaultClient = Owler.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new Owler.CompetitorPremiumAPIApi();
let companyId = "companyId_example"; // String | Company Id
let opts = {
  'paginationId': "paginationId_example", // String | Pass pagination_id as * in the first API request. The API response will return top competitors along with the next pagination_id which can be passed in the subsequent API request to get the next set of competitors. Repeat this process until needed or till the pagination_id returned is blank. Note:Every response will have maximum of 50 competitors.
  'format': "'json'" // String | Format of the response content - json (by default if not specified), xml
};
apiInstance.v1CompanyCompetitorpremiumIdCompanyIdGet(companyId, opts, (error, data, response) => {
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
 **paginationId** | **String**| Pass pagination_id as * in the first API request. The API response will return top competitors along with the next pagination_id which can be passed in the subsequent API request to get the next set of competitors. Repeat this process until needed or till the pagination_id returned is blank. Note:Every response will have maximum of 50 competitors. | [optional] 
 **format** | **String**| Format of the response content - json (by default if not specified), xml | [optional] [default to &#39;json&#39;]

### Return type

[**Competitors**](Competitors.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## v1CompanyCompetitorpremiumUrlWebsiteGet

> Competitors v1CompanyCompetitorpremiumUrlWebsiteGet(website, opts)

Get Competitor information by Url

The Competitors API provides basic information about all competitors of a given company Id

### Example

```javascript
import Owler from 'owler';
let defaultClient = Owler.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new Owler.CompetitorPremiumAPIApi();
let website = "website_example"; // String | Company Id
let opts = {
  'paginationId': "paginationId_example", // String | Pass pagination_id as * in the first API request. The API response will return top competitors along with the next pagination_id which can be passed in the subsequent API request to get the next set of competitors. Repeat this process until needed or till the pagination_id returned is blank. Note:Every response will have maximum of 50 competitors.
  'format': "'json'" // String | Format of the response content - json (by default if not specified), xml
};
apiInstance.v1CompanyCompetitorpremiumUrlWebsiteGet(website, opts, (error, data, response) => {
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
 **paginationId** | **String**| Pass pagination_id as * in the first API request. The API response will return top competitors along with the next pagination_id which can be passed in the subsequent API request to get the next set of competitors. Repeat this process until needed or till the pagination_id returned is blank. Note:Every response will have maximum of 50 competitors. | [optional] 
 **format** | **String**| Format of the response content - json (by default if not specified), xml | [optional] [default to &#39;json&#39;]

### Return type

[**Competitors**](Competitors.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

