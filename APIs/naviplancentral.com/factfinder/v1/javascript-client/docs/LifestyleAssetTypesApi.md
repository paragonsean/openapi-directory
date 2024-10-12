# AdvicentFactFinderService.LifestyleAssetTypesApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lifestyleAssetTypesGetByCountry**](LifestyleAssetTypesApi.md#lifestyleAssetTypesGetByCountry) | **GET** /api/LifestyleAssetTypes | 
[**lifestyleAssetTypesGetById**](LifestyleAssetTypesApi.md#lifestyleAssetTypesGetById) | **GET** /api/LifestyleAssetTypes/{id} | 



## lifestyleAssetTypesGetByCountry

> LifestyleAssetTypesModel lifestyleAssetTypesGetByCountry(country)



Description: This operation retrieves all Lifestyle Asset Types for the specified country.&lt;br /&gt;                Purpose: Provides access to the Lifestyle Asset Types including id and type description.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.LifestyleAssetTypesApi();
let country = "country_example"; // String | The country used to filter Lifestyle Asset Types
apiInstance.lifestyleAssetTypesGetByCountry(country, (error, data, response) => {
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
 **country** | **String**| The country used to filter Lifestyle Asset Types | 

### Return type

[**LifestyleAssetTypesModel**](LifestyleAssetTypesModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## lifestyleAssetTypesGetById

> LifestyleAssetTypeModel lifestyleAssetTypesGetById(id)



Description: This operation retrieves the Lifestyle Asset Type for the specified id.&lt;br /&gt;                Purpose: Provides access to the Lifestyle Asset Types including id and type description.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.LifestyleAssetTypesApi();
let id = 56; // Number | The ID of Lifestyle Asset Type used to retreive the Lifestyle Asset Type information
apiInstance.lifestyleAssetTypesGetById(id, (error, data, response) => {
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
 **id** | **Number**| The ID of Lifestyle Asset Type used to retreive the Lifestyle Asset Type information | 

### Return type

[**LifestyleAssetTypeModel**](LifestyleAssetTypeModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

