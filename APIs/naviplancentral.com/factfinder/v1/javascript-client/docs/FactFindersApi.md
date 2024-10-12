# AdvicentFactFinderService.FactFindersApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

Method | HTTP request | Description
------------- | ------------- | -------------
[**factFindersDeleteById**](FactFindersApi.md#factFindersDeleteById) | **DELETE** /api/FactFinders/{id} | 
[**factFindersGetByHouseholdIdByHouseholdid**](FactFindersApi.md#factFindersGetByHouseholdIdByHouseholdid) | **GET** /api/FactFinders | 
[**factFindersGetById**](FactFindersApi.md#factFindersGetById) | **GET** /api/FactFinders/{id} | 
[**factFindersGetSnapshotsByFactfinderid**](FactFindersApi.md#factFindersGetSnapshotsByFactfinderid) | **GET** /api/FactFinders/{factFinderId}/Snapshots | 
[**factFindersPostByModel**](FactFindersApi.md#factFindersPostByModel) | **POST** /api/FactFinders | 
[**factFindersPostPopulateByModel**](FactFindersApi.md#factFindersPostPopulateByModel) | **POST** /api/FactFinders/Populate | 
[**factFindersPostSnapshotsByFactfinderid**](FactFindersApi.md#factFindersPostSnapshotsByFactfinderid) | **POST** /api/FactFinders/{factFinderId}/Snapshots | 
[**factFindersPutByIdModel**](FactFindersApi.md#factFindersPutByIdModel) | **PUT** /api/FactFinders/{id} | 
[**factFindersPutPopulateFactFinderByIdModel**](FactFindersApi.md#factFindersPutPopulateFactFinderByIdModel) | **PUT** /api/FactFinders/{id}/Populate | 



## factFindersDeleteById

> Object factFindersDeleteById(id)



Description: This operation deletes a single Fact Finder for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Deletes the fact finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.FactFindersApi();
let id = 56; // Number | The ID of the Fact Finder to be deleted
apiInstance.factFindersDeleteById(id, (error, data, response) => {
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
 **id** | **Number**| The ID of the Fact Finder to be deleted | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## factFindersGetByHouseholdIdByHouseholdid

> [FactFinderWithIdModel] factFindersGetByHouseholdIdByHouseholdid(opts)



Description: This operation retrieves all Fact Finders for the specified householdId,                 or if null, all households associated with the user.&lt;br /&gt;                Purpose: Provides access to the Fact Finder including status.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.FactFindersApi();
let opts = {
  'householdId': 56 // Number | The ID of the household used to retrieve the fact finders. If not set, uses all households associated with the user
};
apiInstance.factFindersGetByHouseholdIdByHouseholdid(opts, (error, data, response) => {
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
 **householdId** | **Number**| The ID of the household used to retrieve the fact finders. If not set, uses all households associated with the user | [optional] 

### Return type

[**[FactFinderWithIdModel]**](FactFinderWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## factFindersGetById

> FactFinderWithIdModel factFindersGetById(id)



Description: This operation retrieves a single Fact Finder for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Fact Finder including status.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.FactFindersApi();
let id = 56; // Number | The ID of the Fact Finder used to retrieve the Fact Finder
apiInstance.factFindersGetById(id, (error, data, response) => {
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
 **id** | **Number**| The ID of the Fact Finder used to retrieve the Fact Finder | 

### Return type

[**FactFinderWithIdModel**](FactFinderWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## factFindersGetSnapshotsByFactfinderid

> FactFinderSnapshotsModel factFindersGetSnapshotsByFactfinderid(factFinderId)



Description: The operation retrieves Snapshots of a Fact Finder.&lt;br /&gt;                Purpose: Allows for advisors to view all Snapshots taken of a Fact Finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.FactFindersApi();
let factFinderId = 56; // Number | The ID of the Fact Finder to retrieve Snapshots for
apiInstance.factFindersGetSnapshotsByFactfinderid(factFinderId, (error, data, response) => {
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
 **factFinderId** | **Number**| The ID of the Fact Finder to retrieve Snapshots for | 

### Return type

[**FactFinderSnapshotsModel**](FactFinderSnapshotsModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## factFindersPostByModel

> Object factFindersPostByModel(model)



Description: The operation creates a completely empty draft Fact Finder.&lt;br /&gt;                Requirements: A householdId and list of modules must be provided.&lt;br /&gt;                Purpose: Stages a Fact Finder for population.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.FactFindersApi();
let model = new AdvicentFactFinderService.FactFinderEntityModel(); // FactFinderEntityModel | The Household the Fact Finder will belong to and the modules that are available.
apiInstance.factFindersPostByModel(model, (error, data, response) => {
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
 **model** | [**FactFinderEntityModel**](FactFinderEntityModel.md)| The Household the Fact Finder will belong to and the modules that are available. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## factFindersPostPopulateByModel

> Object factFindersPostPopulateByModel(model)



Description: The operation creates a new Populated Fact Finder.&lt;br /&gt;                Requirements: A householdId and list of modules must be provided.&lt;br /&gt;                Purpose: Creation of a Fact Finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.FactFindersApi();
let model = new AdvicentFactFinderService.FactFinderPopulatableEntityModel(); // FactFinderPopulatableEntityModel | The Household the Fact Finder will belong to and the modules that are available.               Optional PlanId to populate from
apiInstance.factFindersPostPopulateByModel(model, (error, data, response) => {
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
 **model** | [**FactFinderPopulatableEntityModel**](FactFinderPopulatableEntityModel.md)| The Household the Fact Finder will belong to and the modules that are available.               Optional PlanId to populate from | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## factFindersPostSnapshotsByFactfinderid

> Object factFindersPostSnapshotsByFactfinderid(factFinderId)



Description: The operation creates a Snapshot of a Fact Finder.&lt;br /&gt;                Purpose: Allows for advisors to compare the current fact finder to a snapshot prior to acceptance.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.FactFindersApi();
let factFinderId = 56; // Number | The ID of the Fact Finder used to create the Fact Finder Snapshot
apiInstance.factFindersPostSnapshotsByFactfinderid(factFinderId, (error, data, response) => {
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
 **factFinderId** | **Number**| The ID of the Fact Finder used to create the Fact Finder Snapshot | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## factFindersPutByIdModel

> FactFinderWithIdModel factFindersPutByIdModel(id, model)



Description: The operation updates a Fact Finder.&lt;br /&gt;                Purpose: Allows for the updating of a Fact Finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.FactFindersApi();
let id = 56; // Number | The existing Fact Finder ID used to identify which Fact Finder to update
let model = new AdvicentFactFinderService.FactFinderModel(); // FactFinderModel | The Fact Finder to be updated
apiInstance.factFindersPutByIdModel(id, model, (error, data, response) => {
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
 **id** | **Number**| The existing Fact Finder ID used to identify which Fact Finder to update | 
 **model** | [**FactFinderModel**](FactFinderModel.md)| The Fact Finder to be updated | 

### Return type

[**FactFinderWithIdModel**](FactFinderWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## factFindersPutPopulateFactFinderByIdModel

> FactFinderWithIdModel factFindersPutPopulateFactFinderByIdModel(id, model)



Description: The operation populates a fact finder.&lt;br /&gt;                Purpose: Allows for the population of a Fact Finder based on a NaviPlan plan or client. This                         operation cannot be performed on a Fact Finder more than once.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.FactFindersApi();
let id = 56; // Number | The existing Fact Finder ID used to identify which Fact Finder to populate.
let model = new AdvicentFactFinderService.FactFinderPopulationModel(); // FactFinderPopulationModel | The plan to populate a fact finder from. If not provided, the client id will be inferred.
apiInstance.factFindersPutPopulateFactFinderByIdModel(id, model, (error, data, response) => {
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
 **id** | **Number**| The existing Fact Finder ID used to identify which Fact Finder to populate. | 
 **model** | [**FactFinderPopulationModel**](FactFinderPopulationModel.md)| The plan to populate a fact finder from. If not provided, the client id will be inferred. | 

### Return type

[**FactFinderWithIdModel**](FactFinderWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json

