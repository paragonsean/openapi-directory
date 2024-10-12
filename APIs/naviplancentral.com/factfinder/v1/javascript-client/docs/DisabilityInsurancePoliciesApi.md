# AdvicentFactFinderService.DisabilityInsurancePoliciesApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

Method | HTTP request | Description
------------- | ------------- | -------------
[**disabilityInsurancePoliciesDeleteById**](DisabilityInsurancePoliciesApi.md#disabilityInsurancePoliciesDeleteById) | **DELETE** /api/DisabilityInsurancePolicies/{id} | 
[**disabilityInsurancePoliciesGetById**](DisabilityInsurancePoliciesApi.md#disabilityInsurancePoliciesGetById) | **GET** /api/DisabilityInsurancePolicies/{id} | 
[**disabilityInsurancePoliciesGetDisabilityInsurancePoliciesByFactFinderIdByFactfinderid**](DisabilityInsurancePoliciesApi.md#disabilityInsurancePoliciesGetDisabilityInsurancePoliciesByFactFinderIdByFactfinderid) | **GET** /api/DisabilityInsurancePolicies | 
[**disabilityInsurancePoliciesPostByModel**](DisabilityInsurancePoliciesApi.md#disabilityInsurancePoliciesPostByModel) | **POST** /api/DisabilityInsurancePolicies | 
[**disabilityInsurancePoliciesPutByIdModel**](DisabilityInsurancePoliciesApi.md#disabilityInsurancePoliciesPutByIdModel) | **PUT** /api/DisabilityInsurancePolicies/{id} | 



## disabilityInsurancePoliciesDeleteById

> disabilityInsurancePoliciesDeleteById(id)



Description: The operation removes a Disability Insurance Policy tied to a Fact Finder.&lt;br /&gt;                Purpose: Allows for removal of a Disability Insurance Policy from a Fact Finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.DisabilityInsurancePoliciesApi();
let id = 56; // Number | The Disability Insurance Policy ID used to identify which Disability Insurance Policy to remove
apiInstance.disabilityInsurancePoliciesDeleteById(id, (error, data, response) => {
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
 **id** | **Number**| The Disability Insurance Policy ID used to identify which Disability Insurance Policy to remove | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## disabilityInsurancePoliciesGetById

> DisabilityInsurancePolicyWithIdModel disabilityInsurancePoliciesGetById(id)



Description: This operation retrieves a single Disability Insurance Policy for the specified Disability Insurance Policy ID.&lt;br /&gt;                Purpose: Provides access to the Disability Insurance Policy including description and policy type.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.DisabilityInsurancePoliciesApi();
let id = 56; // Number | The ID of the Disability Insurance Policy used to retreive the Disability Insurance Policy
apiInstance.disabilityInsurancePoliciesGetById(id, (error, data, response) => {
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
 **id** | **Number**| The ID of the Disability Insurance Policy used to retreive the Disability Insurance Policy | 

### Return type

[**DisabilityInsurancePolicyWithIdModel**](DisabilityInsurancePolicyWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## disabilityInsurancePoliciesGetDisabilityInsurancePoliciesByFactFinderIdByFactfinderid

> DisabilityInsurancePoliciesModel disabilityInsurancePoliciesGetDisabilityInsurancePoliciesByFactFinderIdByFactfinderid(factFinderId)



Description: This operation retrieves all Disability Insurance Policies for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Disability Insurance Policies including description and policy type.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.DisabilityInsurancePoliciesApi();
let factFinderId = 56; // Number | The ID of the Fact Finder used to retrieve Disability Insurance Policies
apiInstance.disabilityInsurancePoliciesGetDisabilityInsurancePoliciesByFactFinderIdByFactfinderid(factFinderId, (error, data, response) => {
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
 **factFinderId** | **Number**| The ID of the Fact Finder used to retrieve Disability Insurance Policies | 

### Return type

[**DisabilityInsurancePoliciesModel**](DisabilityInsurancePoliciesModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## disabilityInsurancePoliciesPostByModel

> DisabilityInsurancePolicyWithIdModel disabilityInsurancePoliciesPostByModel(model)



Description: The operation creates a Disability Insurance Policy.&lt;br /&gt;                Purpose: Allows for creation of Disability Insurance Policies on a Fact Finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.DisabilityInsurancePoliciesApi();
let model = new AdvicentFactFinderService.DisabilityInsurancePolicyModel(); // DisabilityInsurancePolicyModel | The Disability Insurance Policy to be added to the Fact Finder
apiInstance.disabilityInsurancePoliciesPostByModel(model, (error, data, response) => {
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
 **model** | [**DisabilityInsurancePolicyModel**](DisabilityInsurancePolicyModel.md)| The Disability Insurance Policy to be added to the Fact Finder | 

### Return type

[**DisabilityInsurancePolicyWithIdModel**](DisabilityInsurancePolicyWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## disabilityInsurancePoliciesPutByIdModel

> DisabilityInsurancePolicyWithIdModel disabilityInsurancePoliciesPutByIdModel(id, model)



Description: The operation updates a Disability Insurance Policy.&lt;br /&gt;                Purpose: Allows for complete replacement of a Disability Insurance Policy on a Fact Finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.DisabilityInsurancePoliciesApi();
let id = 56; // Number | The existing Disability Insurance Policy ID used to identify which Disability Insurance Policy to update
let model = new AdvicentFactFinderService.DisabilityInsurancePolicyModel(); // DisabilityInsurancePolicyModel | The Disability Insurance Policy to be updated on a Fact Finder
apiInstance.disabilityInsurancePoliciesPutByIdModel(id, model, (error, data, response) => {
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
 **id** | **Number**| The existing Disability Insurance Policy ID used to identify which Disability Insurance Policy to update | 
 **model** | [**DisabilityInsurancePolicyModel**](DisabilityInsurancePolicyModel.md)| The Disability Insurance Policy to be updated on a Fact Finder | 

### Return type

[**DisabilityInsurancePolicyWithIdModel**](DisabilityInsurancePolicyWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json

