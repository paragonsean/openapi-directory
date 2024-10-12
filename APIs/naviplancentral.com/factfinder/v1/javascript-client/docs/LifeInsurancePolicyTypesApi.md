# AdvicentFactFinderService.LifeInsurancePolicyTypesApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lifeInsurancePolicyTypesGetByCountry**](LifeInsurancePolicyTypesApi.md#lifeInsurancePolicyTypesGetByCountry) | **GET** /api/LifeInsurancePolicyTypes | 
[**lifeInsurancePolicyTypesGetById**](LifeInsurancePolicyTypesApi.md#lifeInsurancePolicyTypesGetById) | **GET** /api/LifeInsurancePolicyTypes/{id} | 



## lifeInsurancePolicyTypesGetByCountry

> LifeInsurancePolicyTypesModel lifeInsurancePolicyTypesGetByCountry(country)



Description: This operation retrieves all Life Insurance Policy Types for the specified country.&lt;br /&gt;                Purpose: Provides access to the Life Insurance Policy Types including id and type description.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.LifeInsurancePolicyTypesApi();
let country = "country_example"; // String | The country used to filter Life Insurance Policy Types
apiInstance.lifeInsurancePolicyTypesGetByCountry(country, (error, data, response) => {
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
 **country** | **String**| The country used to filter Life Insurance Policy Types | 

### Return type

[**LifeInsurancePolicyTypesModel**](LifeInsurancePolicyTypesModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## lifeInsurancePolicyTypesGetById

> LifeInsurancePolicyTypeModel lifeInsurancePolicyTypesGetById(id)



Description: This operation retrieves the Life Insurance Policy Type for the specified id.&lt;br /&gt;                Purpose: Provides access to the Life Insurance Policy Types including id and type description.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.LifeInsurancePolicyTypesApi();
let id = 56; // Number | The ID of Life Insurance Policy Type used to retreive the Life Insurance Policy Type information
apiInstance.lifeInsurancePolicyTypesGetById(id, (error, data, response) => {
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
 **id** | **Number**| The ID of Life Insurance Policy Type used to retreive the Life Insurance Policy Type information | 

### Return type

[**LifeInsurancePolicyTypeModel**](LifeInsurancePolicyTypeModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

