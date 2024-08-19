# GroundwaterWellsAquifersAndRegistryApi.DrillersApi

All URIs are relative to *https://apps.nrs.gov.bc.ca/gwells/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**drillersFilesList**](DrillersApi.md#drillersFilesList) | **GET** /drillers/{person_guid}/files/ | 
[**drillersList**](DrillersApi.md#drillersList) | **GET** /drillers/ | 
[**drillersNamesList**](DrillersApi.md#drillersNamesList) | **GET** /drillers/names/ | 



## drillersFilesList

> AquifersFilesList200Response drillersFilesList(personGuid)



list files found for the aquifer identified in the uri

### Example

```javascript
import GroundwaterWellsAquifersAndRegistryApi from 'groundwater_wells_aquifers_and_registry_api';
let defaultClient = GroundwaterWellsAquifersAndRegistryApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new GroundwaterWellsAquifersAndRegistryApi.DrillersApi();
let personGuid = "personGuid_example"; // String | 
apiInstance.drillersFilesList(personGuid, (error, data, response) => {
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
 **personGuid** | **String**|  | 

### Return type

[**AquifersFilesList200Response**](AquifersFilesList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## drillersList

> [PersonList] drillersList(opts)



Returns a list of all person records

### Example

```javascript
import GroundwaterWellsAquifersAndRegistryApi from 'groundwater_wells_aquifers_and_registry_api';
let defaultClient = GroundwaterWellsAquifersAndRegistryApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new GroundwaterWellsAquifersAndRegistryApi.DrillersApi();
let opts = {
  'search': "search_example", // String | A search term.
  'ordering': "ordering_example", // String | Which field to use when ordering the results.
  'limit': 56, // Number | Number of results to return per page.
  'offset': 56 // Number | The initial index from which to return the results.
};
apiInstance.drillersList(opts, (error, data, response) => {
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
 **limit** | **Number**| Number of results to return per page. | [optional] 
 **offset** | **Number**| The initial index from which to return the results. | [optional] 

### Return type

[**[PersonList]**](PersonList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## drillersNamesList

> [PersonName] drillersNamesList(opts)



Search for a person in the Register

### Example

```javascript
import GroundwaterWellsAquifersAndRegistryApi from 'groundwater_wells_aquifers_and_registry_api';
let defaultClient = GroundwaterWellsAquifersAndRegistryApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new GroundwaterWellsAquifersAndRegistryApi.DrillersApi();
let opts = {
  'search': "search_example" // String | A search term.
};
apiInstance.drillersNamesList(opts, (error, data, response) => {
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

### Return type

[**[PersonName]**](PersonName.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

