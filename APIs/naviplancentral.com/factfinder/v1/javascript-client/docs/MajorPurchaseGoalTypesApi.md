# AdvicentFactFinderService.MajorPurchaseGoalTypesApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

Method | HTTP request | Description
------------- | ------------- | -------------
[**majorPurchaseGoalTypesGetByCountry**](MajorPurchaseGoalTypesApi.md#majorPurchaseGoalTypesGetByCountry) | **GET** /api/MajorPurchaseGoalTypes | 
[**majorPurchaseGoalTypesGetById**](MajorPurchaseGoalTypesApi.md#majorPurchaseGoalTypesGetById) | **GET** /api/MajorPurchaseGoalTypes/{id} | 



## majorPurchaseGoalTypesGetByCountry

> MajorPurchaseGoalTypesModel majorPurchaseGoalTypesGetByCountry(country)



Description: This operation retrieves all Major Purchase Goal Types for the specified country.&lt;br /&gt;                Purpose: Provides access to the Major Purchase Goal Types including id and type description.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.MajorPurchaseGoalTypesApi();
let country = "country_example"; // String | The country used to filter Major Purchase Goal Types
apiInstance.majorPurchaseGoalTypesGetByCountry(country, (error, data, response) => {
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
 **country** | **String**| The country used to filter Major Purchase Goal Types | 

### Return type

[**MajorPurchaseGoalTypesModel**](MajorPurchaseGoalTypesModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## majorPurchaseGoalTypesGetById

> MajorPurchaseGoalTypeModel majorPurchaseGoalTypesGetById(id)



Description: This operation retrieves the Major Purchase Goal Type for the specified id.&lt;br /&gt;                Purpose: Provides access to the Major Purchase Goal Types including id and type description.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.MajorPurchaseGoalTypesApi();
let id = 56; // Number | The ID of Major Purchase Goal Type used to retreive the Major Purchase Goal Type information
apiInstance.majorPurchaseGoalTypesGetById(id, (error, data, response) => {
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
 **id** | **Number**| The ID of Major Purchase Goal Type used to retreive the Major Purchase Goal Type information | 

### Return type

[**MajorPurchaseGoalTypeModel**](MajorPurchaseGoalTypeModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

