# TvApi.ContributorApi

All URIs are relative to *https://tv.api.pressassociation.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getContributor**](ContributorApi.md#getContributor) | **GET** /contributor/{contributorId} | Contributor Detail
[**listContributor**](ContributorApi.md#listContributor) | **GET** /contributor | Contributor Collection



## getContributor

> Object getContributor(contributorId, opts)

Contributor Detail

Return the content of the selected contributor.

### Example

```javascript
import TvApi from 'tv_api';
let defaultClient = TvApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new TvApi.ContributorApi();
let contributorId = "contributorId_example"; // String | Filter the schedule items by contributor ID
let opts = {
  'aliases': true // Boolean | Flag to display Legacy and Provider Ids.
};
apiInstance.getContributor(contributorId, opts, (error, data, response) => {
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
 **contributorId** | **String**| Filter the schedule items by contributor ID | 
 **aliases** | **Boolean**| Flag to display Legacy and Provider Ids. | [optional] [default to true]

### Return type

**Object**

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listContributor

> Object listContributor(opts)

Contributor Collection

Return a collection of Contributors.

### Example

```javascript
import TvApi from 'tv_api';
let defaultClient = TvApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new TvApi.ContributorApi();
let opts = {
  'updatedAfter': "'2015-05-05T00:00:00.000Z'", // String | Updated After
  'limit': 100, // Number | Limit the the number of items to be returned per page. For example: 5.
  'aliases': true // Boolean | Flag to display Legacy and Provider Ids.
};
apiInstance.listContributor(opts, (error, data, response) => {
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
 **updatedAfter** | **String**| Updated After | [optional] [default to &#39;2015-05-05T00:00:00.000Z&#39;]
 **limit** | **Number**| Limit the the number of items to be returned per page. For example: 5. | [optional] [default to 100]
 **aliases** | **Boolean**| Flag to display Legacy and Provider Ids. | [optional] [default to true]

### Return type

**Object**

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

