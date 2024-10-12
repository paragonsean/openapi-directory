# GameSparksGameDetailsApi.ExperimentsApi

All URIs are relative to *http://config2.gamesparks.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createExperimentUsingPOST**](ExperimentsApi.md#createExperimentUsingPOST) | **POST** /restv2/game/{apiKey}/manage/experiments | createExperiment
[**deleteExperimentUsingDELETE**](ExperimentsApi.md#deleteExperimentUsingDELETE) | **DELETE** /restv2/game/{apiKey}/manage/experiments/{id} | deleteExperiment
[**doActionExperimentUsingPOST**](ExperimentsApi.md#doActionExperimentUsingPOST) | **POST** /restv2/game/{apiKey}/manage/experiments/{id}/{action} | doActionExperiment
[**getExperimentUsingGET**](ExperimentsApi.md#getExperimentUsingGET) | **GET** /restv2/game/{apiKey}/manage/experiments/{id} | getExperiment
[**getExperimentsUsingGET**](ExperimentsApi.md#getExperimentsUsingGET) | **GET** /restv2/game/{apiKey}/manage/experiments | getExperiments
[**updateExperimentUsingPUT**](ExperimentsApi.md#updateExperimentUsingPUT) | **PUT** /restv2/game/{apiKey}/manage/experiments/{id} | updateExperiment



## createExperimentUsingPOST

> ExperimentModel createExperimentUsingPOST(apiKey, experimentModel)

createExperiment

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.ExperimentsApi();
let apiKey = "apiKey_example"; // String | apiKey
let experimentModel = new GameSparksGameDetailsApi.ExperimentModel(); // ExperimentModel | input
apiInstance.createExperimentUsingPOST(apiKey, experimentModel, (error, data, response) => {
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
 **apiKey** | **String**| apiKey | 
 **experimentModel** | [**ExperimentModel**](ExperimentModel.md)| input | 

### Return type

[**ExperimentModel**](ExperimentModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json;charset=UTF-8


## deleteExperimentUsingDELETE

> MessageModel deleteExperimentUsingDELETE(apiKey, id)

deleteExperiment

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.ExperimentsApi();
let apiKey = "apiKey_example"; // String | apiKey
let id = 789; // Number | id
apiInstance.deleteExperimentUsingDELETE(apiKey, id, (error, data, response) => {
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
 **apiKey** | **String**| apiKey | 
 **id** | **Number**| id | 

### Return type

[**MessageModel**](MessageModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## doActionExperimentUsingPOST

> ExperimentModel doActionExperimentUsingPOST(apiKey, id, action)

doActionExperiment

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.ExperimentsApi();
let apiKey = "apiKey_example"; // String | apiKey
let id = 789; // Number | id
let action = "action_example"; // String | action
apiInstance.doActionExperimentUsingPOST(apiKey, id, action, (error, data, response) => {
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
 **apiKey** | **String**| apiKey | 
 **id** | **Number**| id | 
 **action** | **String**| action | 

### Return type

[**ExperimentModel**](ExperimentModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## getExperimentUsingGET

> ExperimentModel getExperimentUsingGET(apiKey, id)

getExperiment

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.ExperimentsApi();
let apiKey = "apiKey_example"; // String | apiKey
let id = 789; // Number | id
apiInstance.getExperimentUsingGET(apiKey, id, (error, data, response) => {
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
 **apiKey** | **String**| apiKey | 
 **id** | **Number**| id | 

### Return type

[**ExperimentModel**](ExperimentModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## getExperimentsUsingGET

> [ExperimentModel] getExperimentsUsingGET(apiKey)

getExperiments

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.ExperimentsApi();
let apiKey = "apiKey_example"; // String | apiKey
apiInstance.getExperimentsUsingGET(apiKey, (error, data, response) => {
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
 **apiKey** | **String**| apiKey | 

### Return type

[**[ExperimentModel]**](ExperimentModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## updateExperimentUsingPUT

> ExperimentModel updateExperimentUsingPUT(apiKey, id, experimentModel)

updateExperiment

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.ExperimentsApi();
let apiKey = "apiKey_example"; // String | apiKey
let id = 789; // Number | id
let experimentModel = new GameSparksGameDetailsApi.ExperimentModel(); // ExperimentModel | input
apiInstance.updateExperimentUsingPUT(apiKey, id, experimentModel, (error, data, response) => {
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
 **apiKey** | **String**| apiKey | 
 **id** | **Number**| id | 
 **experimentModel** | [**ExperimentModel**](ExperimentModel.md)| input | 

### Return type

[**ExperimentModel**](ExperimentModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json;charset=UTF-8

