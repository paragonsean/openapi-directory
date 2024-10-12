# AdvicentFactFinderService.FactFinderModulesApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

Method | HTTP request | Description
------------- | ------------- | -------------
[**factFinderModulesGetByFactfinderid**](FactFinderModulesApi.md#factFinderModulesGetByFactfinderid) | **GET** /api/FactFinders/{factFinderId}/Modules | 
[**factFinderModulesGetByFactfinderidId**](FactFinderModulesApi.md#factFinderModulesGetByFactfinderidId) | **GET** /api/FactFinders/{factFinderId}/Modules/{id} | 
[**factFinderModulesPutByModelFactfinderidId**](FactFinderModulesApi.md#factFinderModulesPutByModelFactfinderidId) | **PUT** /api/FactFinders/{factFinderId}/Modules/{id} | 



## factFinderModulesGetByFactfinderid

> FactFinderModulesModel factFinderModulesGetByFactfinderid(factFinderId)



Description: This operation retrieves all Fact Finder Modules for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Fact Finder Modules including description and policy type.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.FactFinderModulesApi();
let factFinderId = 56; // Number | The ID of the Fact Finder used to retrieve Fact Finder Modules
apiInstance.factFinderModulesGetByFactfinderid(factFinderId, (error, data, response) => {
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
 **factFinderId** | **Number**| The ID of the Fact Finder used to retrieve Fact Finder Modules | 

### Return type

[**FactFinderModulesModel**](FactFinderModulesModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## factFinderModulesGetByFactfinderidId

> FactFinderModuleWithIdModel factFinderModulesGetByFactfinderidId(factFinderId, id)



Description: This operation retrieves a single Fact Finder Module for the specified Fact Finder Module ID.&lt;br /&gt;                Purpose: Provides access to the Fact Finder Module including description and policy type.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.FactFinderModulesApi();
let factFinderId = 56; // Number | The ID of the Fact Finder used to retrieve Fact Finder Module
let id = 56; // Number | The ID of the Fact Finder Module used to retreive the Fact Finder Module
apiInstance.factFinderModulesGetByFactfinderidId(factFinderId, id, (error, data, response) => {
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
 **factFinderId** | **Number**| The ID of the Fact Finder used to retrieve Fact Finder Module | 
 **id** | **Number**| The ID of the Fact Finder Module used to retreive the Fact Finder Module | 

### Return type

[**FactFinderModuleWithIdModel**](FactFinderModuleWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## factFinderModulesPutByModelFactfinderidId

> FactFinderModuleWithIdModel factFinderModulesPutByModelFactfinderidId(factFinderId, id, model)



Description: The operation updates a Fact Finder Module.&lt;br /&gt;                Purpose: Allows for complete replacement of a Fact Finder Module on a Fact Finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.FactFinderModulesApi();
let factFinderId = 56; // Number | The ID of the Fact Finder used to identify the Fact Finder Module to update
let id = 56; // Number | The existing Fact Finder Module ID used to identify which Fact Finder Module to update
let model = new AdvicentFactFinderService.FactFinderModuleModel(); // FactFinderModuleModel | The Fact Finder Module to be updated on a Fact Finder
apiInstance.factFinderModulesPutByModelFactfinderidId(factFinderId, id, model, (error, data, response) => {
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
 **factFinderId** | **Number**| The ID of the Fact Finder used to identify the Fact Finder Module to update | 
 **id** | **Number**| The existing Fact Finder Module ID used to identify which Fact Finder Module to update | 
 **model** | [**FactFinderModuleModel**](FactFinderModuleModel.md)| The Fact Finder Module to be updated on a Fact Finder | 

### Return type

[**FactFinderModuleWithIdModel**](FactFinderModuleWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json

