# AdvicentFactFinderService.AccountTypesApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accountTypesGetByCountry**](AccountTypesApi.md#accountTypesGetByCountry) | **GET** /api/AccountTypes | 
[**accountTypesGetById**](AccountTypesApi.md#accountTypesGetById) | **GET** /api/AccountTypes/{id} | 



## accountTypesGetByCountry

> AccountTypesModel accountTypesGetByCountry(country)



Description: This operation retrieves all Account Types for the specified country.&lt;br /&gt;                Purpose: Provides access to the Account Types including id and type description.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.AccountTypesApi();
let country = "country_example"; // String | The country used to filter Account Types
apiInstance.accountTypesGetByCountry(country, (error, data, response) => {
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
 **country** | **String**| The country used to filter Account Types | 

### Return type

[**AccountTypesModel**](AccountTypesModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## accountTypesGetById

> AccountTypeModel accountTypesGetById(id)



Description: This operation retrieves all Account Types for the specified id.&lt;br /&gt;                Purpose: Provides access to the Account Types including id and type description.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.AccountTypesApi();
let id = 56; // Number | The ID of Account Type used to retreive the Account Type information
apiInstance.accountTypesGetById(id, (error, data, response) => {
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
 **id** | **Number**| The ID of Account Type used to retreive the Account Type information | 

### Return type

[**AccountTypeModel**](AccountTypeModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

