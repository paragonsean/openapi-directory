# AdvicentFactFinderService.LongTermCareInsurancePoliciesApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

Method | HTTP request | Description
------------- | ------------- | -------------
[**longTermCareInsurancePoliciesDeleteById**](LongTermCareInsurancePoliciesApi.md#longTermCareInsurancePoliciesDeleteById) | **DELETE** /api/LongTermCareInsurancePolicies/{id} | 
[**longTermCareInsurancePoliciesGetById**](LongTermCareInsurancePoliciesApi.md#longTermCareInsurancePoliciesGetById) | **GET** /api/LongTermCareInsurancePolicies/{id} | 
[**longTermCareInsurancePoliciesGetLongTermCareInsurancePoliciesByFactFinderIdByFactfinderid**](LongTermCareInsurancePoliciesApi.md#longTermCareInsurancePoliciesGetLongTermCareInsurancePoliciesByFactFinderIdByFactfinderid) | **GET** /api/LongTermCareInsurancePolicies | 
[**longTermCareInsurancePoliciesPostByModel**](LongTermCareInsurancePoliciesApi.md#longTermCareInsurancePoliciesPostByModel) | **POST** /api/LongTermCareInsurancePolicies | 
[**longTermCareInsurancePoliciesPutByIdModel**](LongTermCareInsurancePoliciesApi.md#longTermCareInsurancePoliciesPutByIdModel) | **PUT** /api/LongTermCareInsurancePolicies/{id} | 



## longTermCareInsurancePoliciesDeleteById

> longTermCareInsurancePoliciesDeleteById(id)



Description: The operation removes a Long Term Care Insurance Policy tied to a Fact Finder.&lt;br /&gt;                Purpose: Allows for removal of a Long Term Care Insurance Policy from a Fact Finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.LongTermCareInsurancePoliciesApi();
let id = 56; // Number | The Long Term Care Insurance Policy ID used to identify which Long Term Care Insurance Policy to remove
apiInstance.longTermCareInsurancePoliciesDeleteById(id, (error, data, response) => {
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
 **id** | **Number**| The Long Term Care Insurance Policy ID used to identify which Long Term Care Insurance Policy to remove | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## longTermCareInsurancePoliciesGetById

> LongTermCareInsurancePolicyWithIdModel longTermCareInsurancePoliciesGetById(id)



Description: This operation retrieves a single Long Term Care Insurance Policy for the specified Long Term Care Insurance Policy ID.&lt;br /&gt;                Purpose: Provides access to the Long Term Care Insurance Policy including description and premium.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.LongTermCareInsurancePoliciesApi();
let id = 56; // Number | The ID of the Long Term Care Insurance Policy used to retreive the Long Term Care Insurance Policy
apiInstance.longTermCareInsurancePoliciesGetById(id, (error, data, response) => {
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
 **id** | **Number**| The ID of the Long Term Care Insurance Policy used to retreive the Long Term Care Insurance Policy | 

### Return type

[**LongTermCareInsurancePolicyWithIdModel**](LongTermCareInsurancePolicyWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## longTermCareInsurancePoliciesGetLongTermCareInsurancePoliciesByFactFinderIdByFactfinderid

> LongTermCareInsurancePoliciesModel longTermCareInsurancePoliciesGetLongTermCareInsurancePoliciesByFactFinderIdByFactfinderid(factFinderId)



Description: This operation retrieves all Long Term Care Insurance Policies for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Long Term Care Insurance Policies including description and premium.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.LongTermCareInsurancePoliciesApi();
let factFinderId = 56; // Number | The ID of the Fact Finder used to retrieve Long Term Care Insurance Policies
apiInstance.longTermCareInsurancePoliciesGetLongTermCareInsurancePoliciesByFactFinderIdByFactfinderid(factFinderId, (error, data, response) => {
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
 **factFinderId** | **Number**| The ID of the Fact Finder used to retrieve Long Term Care Insurance Policies | 

### Return type

[**LongTermCareInsurancePoliciesModel**](LongTermCareInsurancePoliciesModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## longTermCareInsurancePoliciesPostByModel

> LongTermCareInsurancePolicyWithIdModel longTermCareInsurancePoliciesPostByModel(model)



Description: The operation creates a Long Term Care Insurance Policy.&lt;br /&gt;                Purpose: Allows for creation of Long Term Care Insurance Policies on a Fact Finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.LongTermCareInsurancePoliciesApi();
let model = new AdvicentFactFinderService.LongTermCareInsurancePolicyModel(); // LongTermCareInsurancePolicyModel | The Long Term Care Insurance Policy to be added to the Fact Finder
apiInstance.longTermCareInsurancePoliciesPostByModel(model, (error, data, response) => {
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
 **model** | [**LongTermCareInsurancePolicyModel**](LongTermCareInsurancePolicyModel.md)| The Long Term Care Insurance Policy to be added to the Fact Finder | 

### Return type

[**LongTermCareInsurancePolicyWithIdModel**](LongTermCareInsurancePolicyWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## longTermCareInsurancePoliciesPutByIdModel

> LongTermCareInsurancePolicyWithIdModel longTermCareInsurancePoliciesPutByIdModel(id, model)



Description: The operation updates a Long Term Care Insurance Policy.&lt;br /&gt;                Purpose: Allows for complete replacement of a Long Term Care Insurance Policy on a Fact Finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.LongTermCareInsurancePoliciesApi();
let id = 56; // Number | The existing Long Term Care Insurance Policy ID used to identify which Long Term Care Insurance Policy to update
let model = new AdvicentFactFinderService.LongTermCareInsurancePolicyModel(); // LongTermCareInsurancePolicyModel | The Long Term Care Insurance Policy to be updated on a Fact Finder
apiInstance.longTermCareInsurancePoliciesPutByIdModel(id, model, (error, data, response) => {
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
 **id** | **Number**| The existing Long Term Care Insurance Policy ID used to identify which Long Term Care Insurance Policy to update | 
 **model** | [**LongTermCareInsurancePolicyModel**](LongTermCareInsurancePolicyModel.md)| The Long Term Care Insurance Policy to be updated on a Fact Finder | 

### Return type

[**LongTermCareInsurancePolicyWithIdModel**](LongTermCareInsurancePolicyWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json

