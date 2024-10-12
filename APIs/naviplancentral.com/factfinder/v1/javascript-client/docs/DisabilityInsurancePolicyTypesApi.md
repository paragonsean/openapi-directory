# AdvicentFactFinderService.DisabilityInsurancePolicyTypesApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

Method | HTTP request | Description
------------- | ------------- | -------------
[**disabilityInsurancePolicyTypesGetByCountry**](DisabilityInsurancePolicyTypesApi.md#disabilityInsurancePolicyTypesGetByCountry) | **GET** /api/DisabilityInsurancePolicyTypes | 
[**disabilityInsurancePolicyTypesGetById**](DisabilityInsurancePolicyTypesApi.md#disabilityInsurancePolicyTypesGetById) | **GET** /api/DisabilityInsurancePolicyTypes/{id} | 



## disabilityInsurancePolicyTypesGetByCountry

> DisabilityInsurancePolicyTypesModel disabilityInsurancePolicyTypesGetByCountry(country)



Description: This operation retrieves all Disability Insurance Policy Types for the specified country.&lt;br /&gt;                Purpose: Provides access to the Disability Insurance Policy Types including id and type description.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.DisabilityInsurancePolicyTypesApi();
let country = "country_example"; // String | The country used to filter Disability Insurance Policy Types
apiInstance.disabilityInsurancePolicyTypesGetByCountry(country, (error, data, response) => {
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
 **country** | **String**| The country used to filter Disability Insurance Policy Types | 

### Return type

[**DisabilityInsurancePolicyTypesModel**](DisabilityInsurancePolicyTypesModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## disabilityInsurancePolicyTypesGetById

> DisabilityInsurancePolicyTypeModel disabilityInsurancePolicyTypesGetById(id)



Description: This operation retrieves all Disability Insurance Policy Types for the specified id.&lt;br /&gt;                Purpose: Provides access to the Disability Insurance Policy Types including id and type description.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.DisabilityInsurancePolicyTypesApi();
let id = 56; // Number | The ID of Disability Insurance Policy Type used to retreive the Disability Insurance Policy Type information
apiInstance.disabilityInsurancePolicyTypesGetById(id, (error, data, response) => {
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
 **id** | **Number**| The ID of Disability Insurance Policy Type used to retreive the Disability Insurance Policy Type information | 

### Return type

[**DisabilityInsurancePolicyTypeModel**](DisabilityInsurancePolicyTypeModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

