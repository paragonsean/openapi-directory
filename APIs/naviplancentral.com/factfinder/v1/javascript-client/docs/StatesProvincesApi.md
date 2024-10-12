# AdvicentFactFinderService.StatesProvincesApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

Method | HTTP request | Description
------------- | ------------- | -------------
[**statesProvincesGetByCountry**](StatesProvincesApi.md#statesProvincesGetByCountry) | **GET** /api/StatesProvinces | 
[**statesProvincesGetById**](StatesProvincesApi.md#statesProvincesGetById) | **GET** /api/StatesProvinces/{id} | 



## statesProvincesGetByCountry

> StatesProvincesModel statesProvincesGetByCountry(country)



Description: This operation retrieves all States and Provinces for the specified country.&lt;br /&gt;                Purpose: Provides access to the States and Provinces.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.StatesProvincesApi();
let country = "country_example"; // String | The country used to filter States and Provinces
apiInstance.statesProvincesGetByCountry(country, (error, data, response) => {
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
 **country** | **String**| The country used to filter States and Provinces | 

### Return type

[**StatesProvincesModel**](StatesProvincesModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## statesProvincesGetById

> StateProvinceModel statesProvincesGetById(id)



Description: This operation retrieves the States and Provinces for the specified id.&lt;br /&gt;                Purpose: Provides access to the States and Provinces.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.StatesProvincesApi();
let id = 56; // Number | The ID of the State or Province used to retreive the State or Province information
apiInstance.statesProvincesGetById(id, (error, data, response) => {
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
 **id** | **Number**| The ID of the State or Province used to retreive the State or Province information | 

### Return type

[**StateProvinceModel**](StateProvinceModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

