# GroundwaterWellsAquifersAndRegistryApi.WellsApi

All URIs are relative to *https://apps.nrs.gov.bc.ca/gwells/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**wellsFilesList**](WellsApi.md#wellsFilesList) | **GET** /wells/{tag}/files | 
[**wellsList**](WellsApi.md#wellsList) | **GET** /wells/ | 
[**wellsRead**](WellsApi.md#wellsRead) | **GET** /wells/{well_tag_number} | 
[**wellsTagsList**](WellsApi.md#wellsTagsList) | **GET** /wells/tags/ | 



## wellsFilesList

> AquifersFilesList200Response wellsFilesList(tag)



list files found for the well identified in the uri

### Example

```javascript
import GroundwaterWellsAquifersAndRegistryApi from 'groundwater_wells_aquifers_and_registry_api';
let defaultClient = GroundwaterWellsAquifersAndRegistryApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new GroundwaterWellsAquifersAndRegistryApi.WellsApi();
let tag = "tag_example"; // String | 
apiInstance.wellsFilesList(tag, (error, data, response) => {
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
 **tag** | **String**|  | 

### Return type

[**AquifersFilesList200Response**](AquifersFilesList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## wellsList

> WellsList200Response wellsList(opts)



returns a list of wells

### Example

```javascript
import GroundwaterWellsAquifersAndRegistryApi from 'groundwater_wells_aquifers_and_registry_api';
let defaultClient = GroundwaterWellsAquifersAndRegistryApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new GroundwaterWellsAquifersAndRegistryApi.WellsApi();
let opts = {
  'limit': 56, // Number | Number of results to return per page.
  'offset': 56 // Number | The initial index from which to return the results.
};
apiInstance.wellsList(opts, (error, data, response) => {
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
 **limit** | **Number**| Number of results to return per page. | [optional] 
 **offset** | **Number**| The initial index from which to return the results. | [optional] 

### Return type

[**WellsList200Response**](WellsList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## wellsRead

> WellDetail wellsRead(wellTagNumber)



Return well detail. This view is open to all, and has no permissions.

### Example

```javascript
import GroundwaterWellsAquifersAndRegistryApi from 'groundwater_wells_aquifers_and_registry_api';
let defaultClient = GroundwaterWellsAquifersAndRegistryApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new GroundwaterWellsAquifersAndRegistryApi.WellsApi();
let wellTagNumber = 56; // Number | A unique integer value identifying this well.
apiInstance.wellsRead(wellTagNumber, (error, data, response) => {
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
 **wellTagNumber** | **Number**| A unique integer value identifying this well. | 

### Return type

[**WellDetail**](WellDetail.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## wellsTagsList

> [WellTagSearch] wellsTagsList(opts)



seach for wells by tag or owner

### Example

```javascript
import GroundwaterWellsAquifersAndRegistryApi from 'groundwater_wells_aquifers_and_registry_api';
let defaultClient = GroundwaterWellsAquifersAndRegistryApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new GroundwaterWellsAquifersAndRegistryApi.WellsApi();
let opts = {
  'search': "search_example", // String | A search term.
  'ordering': "ordering_example" // String | Which field to use when ordering the results.
};
apiInstance.wellsTagsList(opts, (error, data, response) => {
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
 **search** | **String**| A search term. | [optional] 
 **ordering** | **String**| Which field to use when ordering the results. | [optional] 

### Return type

[**[WellTagSearch]**](WellTagSearch.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

