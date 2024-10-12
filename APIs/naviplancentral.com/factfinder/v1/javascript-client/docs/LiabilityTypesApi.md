# AdvicentFactFinderService.LiabilityTypesApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

Method | HTTP request | Description
------------- | ------------- | -------------
[**liabilityTypesGetByCountry**](LiabilityTypesApi.md#liabilityTypesGetByCountry) | **GET** /api/LiabilityTypes | 
[**liabilityTypesGetById**](LiabilityTypesApi.md#liabilityTypesGetById) | **GET** /api/LiabilityTypes/{id} | 



## liabilityTypesGetByCountry

> LiabilityTypesModel liabilityTypesGetByCountry(country)



Description: This operation retrieves all Liability Types for the specified country.&lt;br /&gt;                Purpose: Provides access to the Liability Types including id and type description.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.LiabilityTypesApi();
let country = "country_example"; // String | The country used to filter Liability Types
apiInstance.liabilityTypesGetByCountry(country, (error, data, response) => {
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
 **country** | **String**| The country used to filter Liability Types | 

### Return type

[**LiabilityTypesModel**](LiabilityTypesModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## liabilityTypesGetById

> LiabilityTypeModel liabilityTypesGetById(id)



Description: This operation retrieves the Liability Type for the specified id.&lt;br /&gt;                Purpose: Provides access to the Liability Types including id and type description.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.LiabilityTypesApi();
let id = 56; // Number | The ID of Liability Type used to retreive the Liability Type information
apiInstance.liabilityTypesGetById(id, (error, data, response) => {
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
 **id** | **Number**| The ID of Liability Type used to retreive the Liability Type information | 

### Return type

[**LiabilityTypeModel**](LiabilityTypeModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

