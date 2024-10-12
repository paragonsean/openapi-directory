# AdvicentFactFinderService.MajorPurchaseGoalsApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

Method | HTTP request | Description
------------- | ------------- | -------------
[**majorPurchaseGoalsDeleteById**](MajorPurchaseGoalsApi.md#majorPurchaseGoalsDeleteById) | **DELETE** /api/MajorPurchaseGoals/{id} | 
[**majorPurchaseGoalsGetById**](MajorPurchaseGoalsApi.md#majorPurchaseGoalsGetById) | **GET** /api/MajorPurchaseGoals/{id} | 
[**majorPurchaseGoalsGetMajorPurchaseGoalsByFactFinderIdByFactfinderid**](MajorPurchaseGoalsApi.md#majorPurchaseGoalsGetMajorPurchaseGoalsByFactFinderIdByFactfinderid) | **GET** /api/MajorPurchaseGoals | 
[**majorPurchaseGoalsPostByModel**](MajorPurchaseGoalsApi.md#majorPurchaseGoalsPostByModel) | **POST** /api/MajorPurchaseGoals | 
[**majorPurchaseGoalsPutByIdModel**](MajorPurchaseGoalsApi.md#majorPurchaseGoalsPutByIdModel) | **PUT** /api/MajorPurchaseGoals/{id} | 



## majorPurchaseGoalsDeleteById

> majorPurchaseGoalsDeleteById(id)



Description: The operation removes a Major Purchase tied to a Fact Finder.&lt;br /&gt;                Purpose: Allows for removal of a Major Purchase from a Fact Finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.MajorPurchaseGoalsApi();
let id = 56; // Number | The Major Purchase ID used to identify which Major Purchase to remove
apiInstance.majorPurchaseGoalsDeleteById(id, (error, data, response) => {
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
 **id** | **Number**| The Major Purchase ID used to identify which Major Purchase to remove | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## majorPurchaseGoalsGetById

> MajorPurchaseGoalWithIdModel majorPurchaseGoalsGetById(id)



Description: This operation retrieves a single Major Purchase for the specified Major Purchase ID.&lt;br /&gt;                Purpose: Provides access to the Major Purchase including description and amount.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.MajorPurchaseGoalsApi();
let id = 56; // Number | The ID of the Major Purchase used to retreive the Major Purchase
apiInstance.majorPurchaseGoalsGetById(id, (error, data, response) => {
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
 **id** | **Number**| The ID of the Major Purchase used to retreive the Major Purchase | 

### Return type

[**MajorPurchaseGoalWithIdModel**](MajorPurchaseGoalWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## majorPurchaseGoalsGetMajorPurchaseGoalsByFactFinderIdByFactfinderid

> MajorPurchaseGoalsModel majorPurchaseGoalsGetMajorPurchaseGoalsByFactFinderIdByFactfinderid(factFinderId)



Description: This operation retrieves all Major Purchases for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Major Purchases including description and amount.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.MajorPurchaseGoalsApi();
let factFinderId = 56; // Number | The ID of the Fact Finder used to retrieve Major Purchases
apiInstance.majorPurchaseGoalsGetMajorPurchaseGoalsByFactFinderIdByFactfinderid(factFinderId, (error, data, response) => {
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
 **factFinderId** | **Number**| The ID of the Fact Finder used to retrieve Major Purchases | 

### Return type

[**MajorPurchaseGoalsModel**](MajorPurchaseGoalsModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## majorPurchaseGoalsPostByModel

> MajorPurchaseGoalWithIdModel majorPurchaseGoalsPostByModel(model)



Description: The operation creates a Major Purchase.&lt;br /&gt;                Purpose: Allows for creation of Major Purchases on a Fact Finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.MajorPurchaseGoalsApi();
let model = new AdvicentFactFinderService.MajorPurchaseGoalModel(); // MajorPurchaseGoalModel | The Major Purchase to be added to the Fact Finder
apiInstance.majorPurchaseGoalsPostByModel(model, (error, data, response) => {
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
 **model** | [**MajorPurchaseGoalModel**](MajorPurchaseGoalModel.md)| The Major Purchase to be added to the Fact Finder | 

### Return type

[**MajorPurchaseGoalWithIdModel**](MajorPurchaseGoalWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## majorPurchaseGoalsPutByIdModel

> MajorPurchaseGoalWithIdModel majorPurchaseGoalsPutByIdModel(id, model)



Description: The operation updates a Major Purchase.&lt;br /&gt;                Purpose: Allows for complete replacement of a Major Purchase on a Fact Finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.MajorPurchaseGoalsApi();
let id = 56; // Number | The existing Major Purchase ID used to identify which Major Purchase to update
let model = new AdvicentFactFinderService.MajorPurchaseGoalModel(); // MajorPurchaseGoalModel | The Major Purchase to be updated on a Fact Finder
apiInstance.majorPurchaseGoalsPutByIdModel(id, model, (error, data, response) => {
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
 **id** | **Number**| The existing Major Purchase ID used to identify which Major Purchase to update | 
 **model** | [**MajorPurchaseGoalModel**](MajorPurchaseGoalModel.md)| The Major Purchase to be updated on a Fact Finder | 

### Return type

[**MajorPurchaseGoalWithIdModel**](MajorPurchaseGoalWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json

