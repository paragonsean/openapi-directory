# AdvicentFactFinderService.DemographicsApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

Method | HTTP request | Description
------------- | ------------- | -------------
[**demographicsDeleteDependentByDemographicidId**](DemographicsApi.md#demographicsDeleteDependentByDemographicidId) | **DELETE** /api/Demographics/{demographicId}/Dependents/{id} | 
[**demographicsGetById**](DemographicsApi.md#demographicsGetById) | **GET** /api/Demographics/{id} | 
[**demographicsGetDemographicsByFactFinderIdByFactfinderid**](DemographicsApi.md#demographicsGetDemographicsByFactFinderIdByFactfinderid) | **GET** /api/Demographics | 
[**demographicsGetDependentByDemographicidId**](DemographicsApi.md#demographicsGetDependentByDemographicidId) | **GET** /api/Demographics/{demographicId}/Dependents/{id} | 
[**demographicsGetDependentsByDemographicid**](DemographicsApi.md#demographicsGetDependentsByDemographicid) | **GET** /api/Demographics/{demographicId}/Dependents | 
[**demographicsPostByDemographicidModel**](DemographicsApi.md#demographicsPostByDemographicidModel) | **POST** /api/Demographics/{demographicId}/Dependents | 
[**demographicsPostByModel**](DemographicsApi.md#demographicsPostByModel) | **POST** /api/Demographics | 
[**demographicsPutByDemographicidIdModel**](DemographicsApi.md#demographicsPutByDemographicidIdModel) | **PUT** /api/Demographics/{demographicId}/Dependents/{id} | 
[**demographicsPutByIdModel**](DemographicsApi.md#demographicsPutByIdModel) | **PUT** /api/Demographics/{id} | 



## demographicsDeleteDependentByDemographicidId

> demographicsDeleteDependentByDemographicidId(demographicId, id)



Description: The operation removes a Dependent tied to a Fact Finder.&lt;br /&gt;                Purpose: Allows for removal of a Dependent from a Fact Finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.DemographicsApi();
let demographicId = 56; // Number | The ID of the Demographic information used to identify which Dependent to remove
let id = 56; // Number | The Dependent ID used to identify which Dependent to remove
apiInstance.demographicsDeleteDependentByDemographicidId(demographicId, id, (error, data, response) => {
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
 **demographicId** | **Number**| The ID of the Demographic information used to identify which Dependent to remove | 
 **id** | **Number**| The Dependent ID used to identify which Dependent to remove | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## demographicsGetById

> DemographicsWithIdModel demographicsGetById(id)



Description: This operation retrieves Demographic information for the specified Demographic information ID.&lt;br /&gt;                Purpose: Provides access to the Demographic information including city and state.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.DemographicsApi();
let id = 56; // Number | The ID of the Demographic information used to retreive the Demographic information
apiInstance.demographicsGetById(id, (error, data, response) => {
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
 **id** | **Number**| The ID of the Demographic information used to retreive the Demographic information | 

### Return type

[**DemographicsWithIdModel**](DemographicsWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## demographicsGetDemographicsByFactFinderIdByFactfinderid

> DemographicsWithIdModel demographicsGetDemographicsByFactFinderIdByFactfinderid(factFinderId)



Description: This operation retrieves all Demographic information for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Demographic information including city and state.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.DemographicsApi();
let factFinderId = 56; // Number | The ID of the Fact Finder used to retrieve Demographic information
apiInstance.demographicsGetDemographicsByFactFinderIdByFactfinderid(factFinderId, (error, data, response) => {
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
 **factFinderId** | **Number**| The ID of the Fact Finder used to retrieve Demographic information | 

### Return type

[**DemographicsWithIdModel**](DemographicsWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## demographicsGetDependentByDemographicidId

> DemographicsDependentWithIdModel demographicsGetDependentByDemographicidId(demographicId, id)



Description: This operation retrieves a single Dependent for the specified Dependent ID.&lt;br /&gt;                Purpose: Provides access to the Dependent including first and last name.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.DemographicsApi();
let demographicId = 56; // Number | The ID of the Demographic information used to retrieve Dependents
let id = 56; // Number | The ID of the Dependent used to retreive the Dependent
apiInstance.demographicsGetDependentByDemographicidId(demographicId, id, (error, data, response) => {
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
 **demographicId** | **Number**| The ID of the Demographic information used to retrieve Dependents | 
 **id** | **Number**| The ID of the Dependent used to retreive the Dependent | 

### Return type

[**DemographicsDependentWithIdModel**](DemographicsDependentWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## demographicsGetDependentsByDemographicid

> DemographicsDependentsModel demographicsGetDependentsByDemographicid(demographicId)



Description: This operation retrieves all Dependents for the specified Demographic information ID.&lt;br /&gt;                Purpose: Provides access to the Dependents including first and last name.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.DemographicsApi();
let demographicId = 56; // Number | The ID of the Demographic information used to retrieve Dependents
apiInstance.demographicsGetDependentsByDemographicid(demographicId, (error, data, response) => {
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
 **demographicId** | **Number**| The ID of the Demographic information used to retrieve Dependents | 

### Return type

[**DemographicsDependentsModel**](DemographicsDependentsModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## demographicsPostByDemographicidModel

> DemographicsDependentWithIdModel demographicsPostByDemographicidModel(demographicId, model)



Description: The operation creates a Dependent.&lt;br /&gt;                Purpose: Allows for creation of Dependents on a Fact Finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.DemographicsApi();
let demographicId = 56; // Number | The ID of the Demographic information to add the Dependent to
let model = new AdvicentFactFinderService.DemographicsDependentModel(); // DemographicsDependentModel | The Dependent to be added to the Fact Finder
apiInstance.demographicsPostByDemographicidModel(demographicId, model, (error, data, response) => {
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
 **demographicId** | **Number**| The ID of the Demographic information to add the Dependent to | 
 **model** | [**DemographicsDependentModel**](DemographicsDependentModel.md)| The Dependent to be added to the Fact Finder | 

### Return type

[**DemographicsDependentWithIdModel**](DemographicsDependentWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## demographicsPostByModel

> DemographicsWithIdModel demographicsPostByModel(model)



Description: The operation creates Demographic information.&lt;br /&gt;                Purpose: Allows for creation of Demographic information on a Fact Finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.DemographicsApi();
let model = new AdvicentFactFinderService.DemographicsModel(); // DemographicsModel | The Demographic information to be added to the Fact Finder
apiInstance.demographicsPostByModel(model, (error, data, response) => {
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
 **model** | [**DemographicsModel**](DemographicsModel.md)| The Demographic information to be added to the Fact Finder | 

### Return type

[**DemographicsWithIdModel**](DemographicsWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## demographicsPutByDemographicidIdModel

> DemographicsDependentWithIdModel demographicsPutByDemographicidIdModel(demographicId, id, model)



Description: The operation updates a Dependent.&lt;br /&gt;                Purpose: Allows for complete replacement of a Dependent on a Fact Finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.DemographicsApi();
let demographicId = 56; // Number | The ID of the Demographic information used to identify which Dependent to update
let id = 56; // Number | The existing Dependent ID used to identify which Dependent to update
let model = new AdvicentFactFinderService.DemographicsDependentModel(); // DemographicsDependentModel | The Dependent to be updated on a Fact Finder
apiInstance.demographicsPutByDemographicidIdModel(demographicId, id, model, (error, data, response) => {
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
 **demographicId** | **Number**| The ID of the Demographic information used to identify which Dependent to update | 
 **id** | **Number**| The existing Dependent ID used to identify which Dependent to update | 
 **model** | [**DemographicsDependentModel**](DemographicsDependentModel.md)| The Dependent to be updated on a Fact Finder | 

### Return type

[**DemographicsDependentWithIdModel**](DemographicsDependentWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## demographicsPutByIdModel

> DemographicsWithIdModel demographicsPutByIdModel(id, model)



Description: The operation updates Demographic information.&lt;br /&gt;                Purpose: Allows for complete replacement of Demographic information on a Fact Finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.DemographicsApi();
let id = 56; // Number | The existing Demographic information ID used to identify which Demographic information to update
let model = new AdvicentFactFinderService.DemographicsModel(); // DemographicsModel | The Demographic information to be updated on a Fact Finder
apiInstance.demographicsPutByIdModel(id, model, (error, data, response) => {
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
 **id** | **Number**| The existing Demographic information ID used to identify which Demographic information to update | 
 **model** | [**DemographicsModel**](DemographicsModel.md)| The Demographic information to be updated on a Fact Finder | 

### Return type

[**DemographicsWithIdModel**](DemographicsWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json

