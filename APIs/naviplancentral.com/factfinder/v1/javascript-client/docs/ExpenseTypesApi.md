# AdvicentFactFinderService.ExpenseTypesApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

Method | HTTP request | Description
------------- | ------------- | -------------
[**expenseTypesGetByCountry**](ExpenseTypesApi.md#expenseTypesGetByCountry) | **GET** /api/ExpenseTypes | 
[**expenseTypesGetById**](ExpenseTypesApi.md#expenseTypesGetById) | **GET** /api/ExpenseTypes/{id} | 



## expenseTypesGetByCountry

> ExpenseTypesModel expenseTypesGetByCountry(country)



Description: This operation retrieves all Expense Types for the specified country.&lt;br /&gt;                Purpose: Provides access to the Expense Types including id and type description.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.ExpenseTypesApi();
let country = "country_example"; // String | The country used to filter Expense Types
apiInstance.expenseTypesGetByCountry(country, (error, data, response) => {
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
 **country** | **String**| The country used to filter Expense Types | 

### Return type

[**ExpenseTypesModel**](ExpenseTypesModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## expenseTypesGetById

> ExpenseTypeModel expenseTypesGetById(id)



Description: This operation retrieves all Expense Types for the specified country.&lt;br /&gt;                Purpose: Provides access to the Expense Types including id and type description.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.ExpenseTypesApi();
let id = 56; // Number | The ID of Expense Type used to retreive the Expense Type information
apiInstance.expenseTypesGetById(id, (error, data, response) => {
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
 **id** | **Number**| The ID of Expense Type used to retreive the Expense Type information | 

### Return type

[**ExpenseTypeModel**](ExpenseTypeModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

