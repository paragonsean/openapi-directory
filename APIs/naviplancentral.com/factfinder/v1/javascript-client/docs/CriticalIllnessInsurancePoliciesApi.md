# AdvicentFactFinderService.CriticalIllnessInsurancePoliciesApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

Method | HTTP request | Description
------------- | ------------- | -------------
[**criticalIllnessInsurancePoliciesDeleteById**](CriticalIllnessInsurancePoliciesApi.md#criticalIllnessInsurancePoliciesDeleteById) | **DELETE** /api/CriticalIllnessInsurancePolicies/{id} | 
[**criticalIllnessInsurancePoliciesGetById**](CriticalIllnessInsurancePoliciesApi.md#criticalIllnessInsurancePoliciesGetById) | **GET** /api/CriticalIllnessInsurancePolicies/{id} | 
[**criticalIllnessInsurancePoliciesGetCriticalIllnessInsurancePoliciesByFactFinderIdByFactfinderid**](CriticalIllnessInsurancePoliciesApi.md#criticalIllnessInsurancePoliciesGetCriticalIllnessInsurancePoliciesByFactFinderIdByFactfinderid) | **GET** /api/CriticalIllnessInsurancePolicies | 
[**criticalIllnessInsurancePoliciesPostByModel**](CriticalIllnessInsurancePoliciesApi.md#criticalIllnessInsurancePoliciesPostByModel) | **POST** /api/CriticalIllnessInsurancePolicies | 
[**criticalIllnessInsurancePoliciesPutByIdModel**](CriticalIllnessInsurancePoliciesApi.md#criticalIllnessInsurancePoliciesPutByIdModel) | **PUT** /api/CriticalIllnessInsurancePolicies/{id} | 



## criticalIllnessInsurancePoliciesDeleteById

> criticalIllnessInsurancePoliciesDeleteById(id)



Description: The operation removes a Critical Illness Insurance Policy tied to a Fact Finder.&lt;br /&gt;                Purpose: Allows for removal of a Critical Illness Insurance Policy from a Fact Finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.CriticalIllnessInsurancePoliciesApi();
let id = 56; // Number | The Critical Illness Insurance Policy ID used to identify which Critical Illness Insurance Policy to remove
apiInstance.criticalIllnessInsurancePoliciesDeleteById(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| The Critical Illness Insurance Policy ID used to identify which Critical Illness Insurance Policy to remove | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## criticalIllnessInsurancePoliciesGetById

> CriticalIllnessInsurancePolicyWithIdModel criticalIllnessInsurancePoliciesGetById(id)



Description: This operation retrieves a single Critical Illness Insurance Policy for the specified Critical Illness Insurance Policy ID.&lt;br /&gt;                Purpose: Provides access to the Critical Illness Insurance Policy including description and policy type.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.CriticalIllnessInsurancePoliciesApi();
let id = 56; // Number | The ID of the Critical Illness Insurance Policy used to retreive the Critical Illness Insurance Policy
apiInstance.criticalIllnessInsurancePoliciesGetById(id, (error, data, response) => {
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
 **id** | **Number**| The ID of the Critical Illness Insurance Policy used to retreive the Critical Illness Insurance Policy | 

### Return type

[**CriticalIllnessInsurancePolicyWithIdModel**](CriticalIllnessInsurancePolicyWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## criticalIllnessInsurancePoliciesGetCriticalIllnessInsurancePoliciesByFactFinderIdByFactfinderid

> CriticalIllnessInsurancePoliciesModel criticalIllnessInsurancePoliciesGetCriticalIllnessInsurancePoliciesByFactFinderIdByFactfinderid(factFinderId)



Description: This operation retrieves all Critical Illness Insurance Policies for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Critical Illness Insurance Policies including description and policy type.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.CriticalIllnessInsurancePoliciesApi();
let factFinderId = 56; // Number | The ID of the Fact Finder used to retrieve Critical Illness Insurance Policies
apiInstance.criticalIllnessInsurancePoliciesGetCriticalIllnessInsurancePoliciesByFactFinderIdByFactfinderid(factFinderId, (error, data, response) => {
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
 **factFinderId** | **Number**| The ID of the Fact Finder used to retrieve Critical Illness Insurance Policies | 

### Return type

[**CriticalIllnessInsurancePoliciesModel**](CriticalIllnessInsurancePoliciesModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## criticalIllnessInsurancePoliciesPostByModel

> CriticalIllnessInsurancePolicyWithIdModel criticalIllnessInsurancePoliciesPostByModel(model)



Description: The operation creates a Critical Illness Insurance Policy.&lt;br /&gt;                Purpose: Allows for creation of Critical Illness Insurance Policies on a Fact Finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.CriticalIllnessInsurancePoliciesApi();
let model = new AdvicentFactFinderService.CriticalIllnessInsurancePolicyModel(); // CriticalIllnessInsurancePolicyModel | The Critical Illness Insurance Policy to be added to the Fact Finder
apiInstance.criticalIllnessInsurancePoliciesPostByModel(model, (error, data, response) => {
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
 **model** | [**CriticalIllnessInsurancePolicyModel**](CriticalIllnessInsurancePolicyModel.md)| The Critical Illness Insurance Policy to be added to the Fact Finder | 

### Return type

[**CriticalIllnessInsurancePolicyWithIdModel**](CriticalIllnessInsurancePolicyWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## criticalIllnessInsurancePoliciesPutByIdModel

> CriticalIllnessInsurancePolicyWithIdModel criticalIllnessInsurancePoliciesPutByIdModel(id, model)



Description: The operation updates a Critical Illness Insurance Policy.&lt;br /&gt;                Purpose: Allows for complete replacement of a Critical Illness Insurance Policy on a Fact Finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.CriticalIllnessInsurancePoliciesApi();
let id = 56; // Number | The existing Critical Illness Insurance Policy ID used to identify which Critical Illness Insurance Policy to update
let model = new AdvicentFactFinderService.CriticalIllnessInsurancePolicyModel(); // CriticalIllnessInsurancePolicyModel | The Critical Illness Insurance Policy to be updated on a Fact Finder
apiInstance.criticalIllnessInsurancePoliciesPutByIdModel(id, model, (error, data, response) => {
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
 **id** | **Number**| The existing Critical Illness Insurance Policy ID used to identify which Critical Illness Insurance Policy to update | 
 **model** | [**CriticalIllnessInsurancePolicyModel**](CriticalIllnessInsurancePolicyModel.md)| The Critical Illness Insurance Policy to be updated on a Fact Finder | 

### Return type

[**CriticalIllnessInsurancePolicyWithIdModel**](CriticalIllnessInsurancePolicyWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json

