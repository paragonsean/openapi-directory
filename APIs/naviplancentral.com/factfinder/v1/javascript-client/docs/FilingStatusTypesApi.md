# AdvicentFactFinderService.FilingStatusTypesApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

Method | HTTP request | Description
------------- | ------------- | -------------
[**filingStatusTypesGetByCountry**](FilingStatusTypesApi.md#filingStatusTypesGetByCountry) | **GET** /api/FilingStatusTypes | 
[**filingStatusTypesGetById**](FilingStatusTypesApi.md#filingStatusTypesGetById) | **GET** /api/FilingStatusTypes/{id} | 



## filingStatusTypesGetByCountry

> FilingStatusTypesModel filingStatusTypesGetByCountry(country)



Description: This operation retrieves all Filing Status Types for the specified country.&lt;br /&gt;                Purpose: Provides access to the Filing Status Types including id and type description.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.FilingStatusTypesApi();
let country = "country_example"; // String | The country used to filter Filing Status Types
apiInstance.filingStatusTypesGetByCountry(country, (error, data, response) => {
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
 **country** | **String**| The country used to filter Filing Status Types | 

### Return type

[**FilingStatusTypesModel**](FilingStatusTypesModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## filingStatusTypesGetById

> FilingStatusTypeModel filingStatusTypesGetById(id)



Description: This operation retrieves all Filing Status Type for the specified id.&lt;br /&gt;                Purpose: Provides access to the Filing Status Types including id and type description.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.FilingStatusTypesApi();
let id = 56; // Number | The ID of Filing Status Type used to retreive the Filing Status Type information
apiInstance.filingStatusTypesGetById(id, (error, data, response) => {
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
 **id** | **Number**| The ID of Filing Status Type used to retreive the Filing Status Type information | 

### Return type

[**FilingStatusTypeModel**](FilingStatusTypeModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

