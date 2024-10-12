# GameSparksGameDetailsApi.TestHarnessApi

All URIs are relative to *http://config2.gamesparks.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createTestHarnessScenarioUsingPOST**](TestHarnessApi.md#createTestHarnessScenarioUsingPOST) | **POST** /restv2/game/{apiKey}/admin/testHarness/scenarios | createTestHarnessScenario
[**deleteTestHarnessScenarioUsingDELETE**](TestHarnessApi.md#deleteTestHarnessScenarioUsingDELETE) | **DELETE** /restv2/game/{apiKey}/admin/testHarness/scenarios/{scenarioName} | deleteTestHarnessScenario
[**getTestHarnessScenarioUsingGET**](TestHarnessApi.md#getTestHarnessScenarioUsingGET) | **GET** /restv2/game/{apiKey}/admin/testHarness/scenarios/{scenarioName} | getTestHarnessScenario
[**getTestHarnessScenariosUsingGET**](TestHarnessApi.md#getTestHarnessScenariosUsingGET) | **GET** /restv2/game/{apiKey}/admin/testHarness/scenarios | getTestHarnessScenarios
[**updateTestHarnessScenarioUsingPUT**](TestHarnessApi.md#updateTestHarnessScenarioUsingPUT) | **PUT** /restv2/game/{apiKey}/admin/testHarness/scenarios/{scenarioName} | updateTestHarnessScenario



## createTestHarnessScenarioUsingPOST

> TestHarnessScenarioModel createTestHarnessScenarioUsingPOST(apiKey, testHarnessScenarioModel)

createTestHarnessScenario

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.TestHarnessApi();
let apiKey = "apiKey_example"; // String | apiKey
let testHarnessScenarioModel = new GameSparksGameDetailsApi.TestHarnessScenarioModel(); // TestHarnessScenarioModel | testHarnessScenarioDTO
apiInstance.createTestHarnessScenarioUsingPOST(apiKey, testHarnessScenarioModel, (error, data, response) => {
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
 **testHarnessScenarioModel** | [**TestHarnessScenarioModel**](TestHarnessScenarioModel.md)| testHarnessScenarioDTO | 

### Return type

[**TestHarnessScenarioModel**](TestHarnessScenarioModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json;charset=UTF-8


## deleteTestHarnessScenarioUsingDELETE

> MessageModel deleteTestHarnessScenarioUsingDELETE(apiKey, scenarioName)

deleteTestHarnessScenario

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.TestHarnessApi();
let apiKey = "apiKey_example"; // String | apiKey
let scenarioName = "scenarioName_example"; // String | scenarioName
apiInstance.deleteTestHarnessScenarioUsingDELETE(apiKey, scenarioName, (error, data, response) => {
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
 **scenarioName** | **String**| scenarioName | 

### Return type

[**MessageModel**](MessageModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## getTestHarnessScenarioUsingGET

> TestHarnessScenarioModel getTestHarnessScenarioUsingGET(apiKey, scenarioName)

getTestHarnessScenario

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.TestHarnessApi();
let apiKey = "apiKey_example"; // String | apiKey
let scenarioName = "scenarioName_example"; // String | scenarioName
apiInstance.getTestHarnessScenarioUsingGET(apiKey, scenarioName, (error, data, response) => {
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
 **scenarioName** | **String**| scenarioName | 

### Return type

[**TestHarnessScenarioModel**](TestHarnessScenarioModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## getTestHarnessScenariosUsingGET

> [TestHarnessScenarioModel] getTestHarnessScenariosUsingGET(apiKey)

getTestHarnessScenarios

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.TestHarnessApi();
let apiKey = "apiKey_example"; // String | apiKey
apiInstance.getTestHarnessScenariosUsingGET(apiKey, (error, data, response) => {
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

[**[TestHarnessScenarioModel]**](TestHarnessScenarioModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## updateTestHarnessScenarioUsingPUT

> TestHarnessScenarioModel updateTestHarnessScenarioUsingPUT(apiKey, scenarioName, testHarnessScenarioModel)

updateTestHarnessScenario

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.TestHarnessApi();
let apiKey = "apiKey_example"; // String | apiKey
let scenarioName = "scenarioName_example"; // String | scenarioName
let testHarnessScenarioModel = new GameSparksGameDetailsApi.TestHarnessScenarioModel(); // TestHarnessScenarioModel | testHarnessScenarioDTO
apiInstance.updateTestHarnessScenarioUsingPUT(apiKey, scenarioName, testHarnessScenarioModel, (error, data, response) => {
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
 **scenarioName** | **String**| scenarioName | 
 **testHarnessScenarioModel** | [**TestHarnessScenarioModel**](TestHarnessScenarioModel.md)| testHarnessScenarioDTO | 

### Return type

[**TestHarnessScenarioModel**](TestHarnessScenarioModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json;charset=UTF-8

