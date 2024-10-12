# AdvicentFactFinderService.IncomeTypesApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

Method | HTTP request | Description
------------- | ------------- | -------------
[**incomeTypesGetByCountry**](IncomeTypesApi.md#incomeTypesGetByCountry) | **GET** /api/IncomeTypes | 
[**incomeTypesGetById**](IncomeTypesApi.md#incomeTypesGetById) | **GET** /api/IncomeTypes/{id} | 



## incomeTypesGetByCountry

> IncomeTypesModel incomeTypesGetByCountry(country)



Description: This operation retrieves all Income Types for the specified country.&lt;br /&gt;                Purpose: Provides access to the Income Types including id and type description.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.IncomeTypesApi();
let country = "country_example"; // String | The country used to filter Income Types
apiInstance.incomeTypesGetByCountry(country, (error, data, response) => {
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
 **country** | **String**| The country used to filter Income Types | 

### Return type

[**IncomeTypesModel**](IncomeTypesModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## incomeTypesGetById

> IncomeTypeModel incomeTypesGetById(id)



Description: This operation retrieves the Income Type for the specified id.&lt;br /&gt;                Purpose: Provides access to the Income Types including id and type description.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.IncomeTypesApi();
let id = 56; // Number | The ID of Income Type used to retreive the Income Type information
apiInstance.incomeTypesGetById(id, (error, data, response) => {
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
 **id** | **Number**| The ID of Income Type used to retreive the Income Type information | 

### Return type

[**IncomeTypeModel**](IncomeTypeModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

