# AdvicentFactFinderService.FrequencyTypesApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

Method | HTTP request | Description
------------- | ------------- | -------------
[**frequencyTypesGetByEntityCountry**](FrequencyTypesApi.md#frequencyTypesGetByEntityCountry) | **GET** /api/FrequencyTypes | 
[**frequencyTypesGetById**](FrequencyTypesApi.md#frequencyTypesGetById) | **GET** /api/FrequencyTypes/{id} | 



## frequencyTypesGetByEntityCountry

> FrequencyTypesModel frequencyTypesGetByEntityCountry(entity, country)



Description: This operation retrieves all Frequency Types for the specified country and entity.&lt;br /&gt;                Purpose: Provides access to the Frequency Types including id and type description.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.FrequencyTypesApi();
let entity = "entity_example"; // String | The entity used to filter Frequency Types
let country = "country_example"; // String | The country used to filter Frequency Types
apiInstance.frequencyTypesGetByEntityCountry(entity, country, (error, data, response) => {
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
 **entity** | **String**| The entity used to filter Frequency Types | 
 **country** | **String**| The country used to filter Frequency Types | 

### Return type

[**FrequencyTypesModel**](FrequencyTypesModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## frequencyTypesGetById

> FrequencyTypeModel frequencyTypesGetById(id)



Description: This operation retrieves the Frequency Type for the specified id.&lt;br /&gt;                Purpose: Provides access to the Frequency Types including id and type description.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.FrequencyTypesApi();
let id = 56; // Number | The ID of Frequency Type used to retreive the Frequency Type information
apiInstance.frequencyTypesGetById(id, (error, data, response) => {
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
 **id** | **Number**| The ID of Frequency Type used to retreive the Frequency Type information | 

### Return type

[**FrequencyTypeModel**](FrequencyTypeModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

