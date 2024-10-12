# AdvicentFactFinderService.LifeInsurancePoliciesApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lifeInsurancePoliciesDeleteById**](LifeInsurancePoliciesApi.md#lifeInsurancePoliciesDeleteById) | **DELETE** /api/LifeInsurancePolicies/{id} | 
[**lifeInsurancePoliciesDeleteSubaccountByLifeinsurancepolicyidId**](LifeInsurancePoliciesApi.md#lifeInsurancePoliciesDeleteSubaccountByLifeinsurancepolicyidId) | **DELETE** /api/LifeInsurancePolicies/{lifeInsurancePolicyId}/Subaccounts/{id} | 
[**lifeInsurancePoliciesGetById**](LifeInsurancePoliciesApi.md#lifeInsurancePoliciesGetById) | **GET** /api/LifeInsurancePolicies/{id} | 
[**lifeInsurancePoliciesGetLifeInsurancePoliciesByFactFinderIdByFactfinderid**](LifeInsurancePoliciesApi.md#lifeInsurancePoliciesGetLifeInsurancePoliciesByFactFinderIdByFactfinderid) | **GET** /api/LifeInsurancePolicies | 
[**lifeInsurancePoliciesGetSubaccountByLifeinsurancepolicyidId**](LifeInsurancePoliciesApi.md#lifeInsurancePoliciesGetSubaccountByLifeinsurancepolicyidId) | **GET** /api/LifeInsurancePolicies/{lifeInsurancePolicyId}/Subaccounts/{id} | 
[**lifeInsurancePoliciesGetSubaccountsByLifeinsurancepolicyid**](LifeInsurancePoliciesApi.md#lifeInsurancePoliciesGetSubaccountsByLifeinsurancepolicyid) | **GET** /api/LifeInsurancePolicies/{lifeInsurancePolicyId}/Subaccounts | 
[**lifeInsurancePoliciesPostByModel**](LifeInsurancePoliciesApi.md#lifeInsurancePoliciesPostByModel) | **POST** /api/LifeInsurancePolicies | 
[**lifeInsurancePoliciesPostSubaccountByLifeinsurancepolicyidModel**](LifeInsurancePoliciesApi.md#lifeInsurancePoliciesPostSubaccountByLifeinsurancepolicyidModel) | **POST** /api/LifeInsurancePolicies/{lifeInsurancePolicyId}/Subaccounts | 
[**lifeInsurancePoliciesPutByIdModel**](LifeInsurancePoliciesApi.md#lifeInsurancePoliciesPutByIdModel) | **PUT** /api/LifeInsurancePolicies/{id} | 
[**lifeInsurancePoliciesPutSubaccountByLifeinsurancepolicyidIdModel**](LifeInsurancePoliciesApi.md#lifeInsurancePoliciesPutSubaccountByLifeinsurancepolicyidIdModel) | **PUT** /api/LifeInsurancePolicies/{lifeInsurancePolicyId}/Subaccounts/{id} | 



## lifeInsurancePoliciesDeleteById

> lifeInsurancePoliciesDeleteById(id)



Description: The operation removes a Life Insurance Policy tied to a Fact Finder.&lt;br /&gt;                Purpose: Allows for removal of a Life Insurance Policy and associated subaccounts from a Fact Finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.LifeInsurancePoliciesApi();
let id = 56; // Number | The Life Insurance Policy ID used to identify which Life Insurance Policy to remove
apiInstance.lifeInsurancePoliciesDeleteById(id, (error, data, response) => {
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
 **id** | **Number**| The Life Insurance Policy ID used to identify which Life Insurance Policy to remove | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## lifeInsurancePoliciesDeleteSubaccountByLifeinsurancepolicyidId

> lifeInsurancePoliciesDeleteSubaccountByLifeinsurancepolicyidId(lifeInsurancePolicyId, id)



Description: Deletes an existing Life Insurance Policy Subaccount for an existing Life Insurance Policy.&lt;br /&gt;                Purpose: Allows for removal of a subaccount from a Life Insurance Policy.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.LifeInsurancePoliciesApi();
let lifeInsurancePolicyId = 56; // Number | The ID of the Life Insurance Policy used to delete the Life Insurance Policy Subaccount.
let id = 56; // Number | The ID of the Life Insurance Policy Subaccount.
apiInstance.lifeInsurancePoliciesDeleteSubaccountByLifeinsurancepolicyidId(lifeInsurancePolicyId, id, (error, data, response) => {
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
 **lifeInsurancePolicyId** | **Number**| The ID of the Life Insurance Policy used to delete the Life Insurance Policy Subaccount. | 
 **id** | **Number**| The ID of the Life Insurance Policy Subaccount. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## lifeInsurancePoliciesGetById

> LifeInsurancePolicyWithIdModel lifeInsurancePoliciesGetById(id)



Description: This operation retrieves a single Life Insurance Policy for the specified Life Insurance Policy ID.&lt;br /&gt;                Purpose: Provides access to the Life Insurance Policy including description and policy type.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.LifeInsurancePoliciesApi();
let id = 56; // Number | The ID of the Life Insurance Policy used to retreive the Life Insurance Policy
apiInstance.lifeInsurancePoliciesGetById(id, (error, data, response) => {
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
 **id** | **Number**| The ID of the Life Insurance Policy used to retreive the Life Insurance Policy | 

### Return type

[**LifeInsurancePolicyWithIdModel**](LifeInsurancePolicyWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## lifeInsurancePoliciesGetLifeInsurancePoliciesByFactFinderIdByFactfinderid

> LifeInsurancePoliciesModel lifeInsurancePoliciesGetLifeInsurancePoliciesByFactFinderIdByFactfinderid(factFinderId)



Description: This operation retrieves all Life Insurance Policies for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Life Insurance Policies including description and policy type.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.LifeInsurancePoliciesApi();
let factFinderId = 56; // Number | The ID of the Fact Finder used to retrieve Life Insurance Policies
apiInstance.lifeInsurancePoliciesGetLifeInsurancePoliciesByFactFinderIdByFactfinderid(factFinderId, (error, data, response) => {
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
 **factFinderId** | **Number**| The ID of the Fact Finder used to retrieve Life Insurance Policies | 

### Return type

[**LifeInsurancePoliciesModel**](LifeInsurancePoliciesModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## lifeInsurancePoliciesGetSubaccountByLifeinsurancepolicyidId

> LifeInsurancePolicySubaccountWithIdModel lifeInsurancePoliciesGetSubaccountByLifeinsurancepolicyidId(lifeInsurancePolicyId, id)



Description: Get a specific subaccount for an existing Life Insurance Policy.&lt;br /&gt;                Purpose: Provides access to the Life Insurance Policy subaccount.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.LifeInsurancePoliciesApi();
let lifeInsurancePolicyId = 56; // Number | The ID of the Life Insurance Policy used to retrieve the Life Insurance Policy Subaccount.
let id = 56; // Number | The ID of the Life Insurance Policy Subaccount.
apiInstance.lifeInsurancePoliciesGetSubaccountByLifeinsurancepolicyidId(lifeInsurancePolicyId, id, (error, data, response) => {
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
 **lifeInsurancePolicyId** | **Number**| The ID of the Life Insurance Policy used to retrieve the Life Insurance Policy Subaccount. | 
 **id** | **Number**| The ID of the Life Insurance Policy Subaccount. | 

### Return type

[**LifeInsurancePolicySubaccountWithIdModel**](LifeInsurancePolicySubaccountWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## lifeInsurancePoliciesGetSubaccountsByLifeinsurancepolicyid

> LifeInsurancePolicySubaccountsModel lifeInsurancePoliciesGetSubaccountsByLifeinsurancepolicyid(lifeInsurancePolicyId)



Description: Get all the subaccounts for an existing Life Insurance Policy.&lt;br /&gt;                Purpose: Provides access to all the Life Insurance Policy subaccounts.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.LifeInsurancePoliciesApi();
let lifeInsurancePolicyId = 56; // Number | The ID of the Life Insurance Policy used to retrieve the Life Insurance Policy Subaccounts.
apiInstance.lifeInsurancePoliciesGetSubaccountsByLifeinsurancepolicyid(lifeInsurancePolicyId, (error, data, response) => {
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
 **lifeInsurancePolicyId** | **Number**| The ID of the Life Insurance Policy used to retrieve the Life Insurance Policy Subaccounts. | 

### Return type

[**LifeInsurancePolicySubaccountsModel**](LifeInsurancePolicySubaccountsModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## lifeInsurancePoliciesPostByModel

> LifeInsurancePolicyWithIdModel lifeInsurancePoliciesPostByModel(model)



Description: The operation creates a Life Insurance Policy.&lt;br /&gt;                Purpose: Allows for creation of Life Insurance Policies on a Fact Finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.LifeInsurancePoliciesApi();
let model = new AdvicentFactFinderService.LifeInsurancePolicyModel(); // LifeInsurancePolicyModel | The Life Insurance Policy to be added to the Fact Finder
apiInstance.lifeInsurancePoliciesPostByModel(model, (error, data, response) => {
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
 **model** | [**LifeInsurancePolicyModel**](LifeInsurancePolicyModel.md)| The Life Insurance Policy to be added to the Fact Finder | 

### Return type

[**LifeInsurancePolicyWithIdModel**](LifeInsurancePolicyWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## lifeInsurancePoliciesPostSubaccountByLifeinsurancepolicyidModel

> LifeInsurancePolicySubaccountWithIdModel lifeInsurancePoliciesPostSubaccountByLifeinsurancepolicyidModel(lifeInsurancePolicyId, model)



Description: Creates a subaccount and adds it to an existing Life Insurance Policy.&lt;br /&gt;                Purpose: Allows for creation of subaccount on a Life Insurance Policy.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.LifeInsurancePoliciesApi();
let lifeInsurancePolicyId = 56; // Number | The ID of the Life Insurance Policy used to create the Life Insurance Policy Subaccount.
let model = new AdvicentFactFinderService.LifeInsurancePolicySubaccountModel(); // LifeInsurancePolicySubaccountModel | The Life Insurance Policy Subaccount model.
apiInstance.lifeInsurancePoliciesPostSubaccountByLifeinsurancepolicyidModel(lifeInsurancePolicyId, model, (error, data, response) => {
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
 **lifeInsurancePolicyId** | **Number**| The ID of the Life Insurance Policy used to create the Life Insurance Policy Subaccount. | 
 **model** | [**LifeInsurancePolicySubaccountModel**](LifeInsurancePolicySubaccountModel.md)| The Life Insurance Policy Subaccount model. | 

### Return type

[**LifeInsurancePolicySubaccountWithIdModel**](LifeInsurancePolicySubaccountWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## lifeInsurancePoliciesPutByIdModel

> LifeInsurancePolicyWithIdModel lifeInsurancePoliciesPutByIdModel(id, model)



Description: The operation updates a Life Insurance Policy, deletes associated sub-accounts if the policy type changes.&lt;br /&gt;                Purpose: Allows for complete replacement of a Life Insurance Policy on a Fact Finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.LifeInsurancePoliciesApi();
let id = 56; // Number | The existing Life Insurance Policy ID used to identify which Life Insurance Policy to update
let model = new AdvicentFactFinderService.LifeInsurancePolicyModel(); // LifeInsurancePolicyModel | The Life Insurance Policy to be updated on a Fact Finder
apiInstance.lifeInsurancePoliciesPutByIdModel(id, model, (error, data, response) => {
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
 **id** | **Number**| The existing Life Insurance Policy ID used to identify which Life Insurance Policy to update | 
 **model** | [**LifeInsurancePolicyModel**](LifeInsurancePolicyModel.md)| The Life Insurance Policy to be updated on a Fact Finder | 

### Return type

[**LifeInsurancePolicyWithIdModel**](LifeInsurancePolicyWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## lifeInsurancePoliciesPutSubaccountByLifeinsurancepolicyidIdModel

> LifeInsurancePolicySubaccountModel lifeInsurancePoliciesPutSubaccountByLifeinsurancepolicyidIdModel(lifeInsurancePolicyId, id, model)



Description: Updates an existing Life Insurance Policy Subaccount for an existing Life Insurance Policy.&lt;br /&gt;                Purpose: Allows for complete replacement of a subaccount on a Life Insurance Policy.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.LifeInsurancePoliciesApi();
let lifeInsurancePolicyId = 56; // Number | The ID of the Life Insurance Policy used to update the Life Insurance Policy Subaccount.
let id = 56; // Number | The ID of the Life Insurance Policy Subaccount.
let model = new AdvicentFactFinderService.LifeInsurancePolicySubaccountModel(); // LifeInsurancePolicySubaccountModel | The Life Insurance Policy Subaccount model.
apiInstance.lifeInsurancePoliciesPutSubaccountByLifeinsurancepolicyidIdModel(lifeInsurancePolicyId, id, model, (error, data, response) => {
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
 **lifeInsurancePolicyId** | **Number**| The ID of the Life Insurance Policy used to update the Life Insurance Policy Subaccount. | 
 **id** | **Number**| The ID of the Life Insurance Policy Subaccount. | 
 **model** | [**LifeInsurancePolicySubaccountModel**](LifeInsurancePolicySubaccountModel.md)| The Life Insurance Policy Subaccount model. | 

### Return type

[**LifeInsurancePolicySubaccountModel**](LifeInsurancePolicySubaccountModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json

