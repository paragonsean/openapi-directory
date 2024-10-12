# AdvicentFactFinderService.CriticalIllnessInsurancePolicyTypesApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

Method | HTTP request | Description
------------- | ------------- | -------------
[**criticalIllnessInsurancePolicyTypesGetByCountry**](CriticalIllnessInsurancePolicyTypesApi.md#criticalIllnessInsurancePolicyTypesGetByCountry) | **GET** /api/CriticalIllnessInsurancePolicyTypes | 
[**criticalIllnessInsurancePolicyTypesGetById**](CriticalIllnessInsurancePolicyTypesApi.md#criticalIllnessInsurancePolicyTypesGetById) | **GET** /api/CriticalIllnessInsurancePolicyTypes/{id} | 



## criticalIllnessInsurancePolicyTypesGetByCountry

> CriticalIllnessInsurancePolicyTypesModel criticalIllnessInsurancePolicyTypesGetByCountry(country)



Description: This operation retrieves all Critical Illness Insurance Policy Types for the specified country.&lt;br /&gt;                Purpose: Provides access to the Critical Illness Insurance Policy Types including id and type description.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.CriticalIllnessInsurancePolicyTypesApi();
let country = "country_example"; // String | The country used to filter Critical Illness Insurance Policy Types
apiInstance.criticalIllnessInsurancePolicyTypesGetByCountry(country, (error, data, response) => {
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
 **country** | **String**| The country used to filter Critical Illness Insurance Policy Types | 

### Return type

[**CriticalIllnessInsurancePolicyTypesModel**](CriticalIllnessInsurancePolicyTypesModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## criticalIllnessInsurancePolicyTypesGetById

> CriticalIllnessInsurancePolicyTypeModel criticalIllnessInsurancePolicyTypesGetById(id)



Description: This operation retrieves the Critical Illness Insurance Policy Type for the specified id.&lt;br /&gt;                Purpose: Provides access to the Critical Illness Insurance Policy Types including id and type description.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.CriticalIllnessInsurancePolicyTypesApi();
let id = 56; // Number | The ID of Critical Illness Insurance Policy Type used to retreive the Critical Illness Insurance Policy Type information
apiInstance.criticalIllnessInsurancePolicyTypesGetById(id, (error, data, response) => {
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
 **id** | **Number**| The ID of Critical Illness Insurance Policy Type used to retreive the Critical Illness Insurance Policy Type information | 

### Return type

[**CriticalIllnessInsurancePolicyTypeModel**](CriticalIllnessInsurancePolicyTypeModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

