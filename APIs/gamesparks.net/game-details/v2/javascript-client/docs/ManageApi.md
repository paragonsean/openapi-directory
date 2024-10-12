# GameSparksGameDetailsApi.ManageApi

All URIs are relative to *http://config2.gamesparks.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**copySnapshotToExistingGameUsingPOST**](ManageApi.md#copySnapshotToExistingGameUsingPOST) | **POST** /restv2/game/{apiKey}/manage/snapshots/{snapshotId}/copy/to/{targetApiKey} | copySnapshotToExistingGame
[**createQueryUsingPOST**](ManageApi.md#createQueryUsingPOST) | **POST** /restv2/game/{apiKey}/manage/queries | createQuery
[**createScreenUsingPOST**](ManageApi.md#createScreenUsingPOST) | **POST** /restv2/game/{apiKey}/manage/screens | createScreen
[**createSnapshotUsingPOST**](ManageApi.md#createSnapshotUsingPOST) | **POST** /restv2/game/{apiKey}/manage/snapshots | createSnapshot
[**createSnippetUsingPOST**](ManageApi.md#createSnippetUsingPOST) | **POST** /restv2/game/{apiKey}/manage/snippets | createSnippet
[**deleteQueryUsingDELETE**](ManageApi.md#deleteQueryUsingDELETE) | **DELETE** /restv2/game/{apiKey}/manage/queries/{shortCode} | deleteQuery
[**deleteScreenUsingDELETE**](ManageApi.md#deleteScreenUsingDELETE) | **DELETE** /restv2/game/{apiKey}/manage/screens/{shortCode} | deleteScreen
[**deleteSnapshotUsingDELETE**](ManageApi.md#deleteSnapshotUsingDELETE) | **DELETE** /restv2/game/{apiKey}/manage/snapshots/{snapshotId} | deleteSnapshot
[**deleteSnippetUsingDELETE**](ManageApi.md#deleteSnippetUsingDELETE) | **DELETE** /restv2/game/{apiKey}/manage/snippets/{shortCode} | deleteSnippet
[**getQueryUsingGET**](ManageApi.md#getQueryUsingGET) | **GET** /restv2/game/{apiKey}/manage/queries/{shortCode} | getQuery
[**getScreenUsingGET**](ManageApi.md#getScreenUsingGET) | **GET** /restv2/game/{apiKey}/manage/screens/{shortCode} | getScreen
[**getSnippetUsingGET**](ManageApi.md#getSnippetUsingGET) | **GET** /restv2/game/{apiKey}/manage/snippets/{shortCode} | getSnippet
[**listExecutableScreensUsingGET**](ManageApi.md#listExecutableScreensUsingGET) | **GET** /restv2/game/{apiKey}/manage/screens/executable | listExecutableScreens
[**listQueriesUsingGET**](ManageApi.md#listQueriesUsingGET) | **GET** /restv2/game/{apiKey}/manage/queries | listQueries
[**listScreensUsingGET**](ManageApi.md#listScreensUsingGET) | **GET** /restv2/game/{apiKey}/manage/screens | listScreens
[**listSnapshotsUsingGET**](ManageApi.md#listSnapshotsUsingGET) | **GET** /restv2/game/{apiKey}/manage/snapshots | listSnapshots
[**listSnippetsUsingGET**](ManageApi.md#listSnippetsUsingGET) | **GET** /restv2/game/{apiKey}/manage/snippets | listSnippets
[**publishSnapshotUsingPOST**](ManageApi.md#publishSnapshotUsingPOST) | **POST** /restv2/game/{apiKey}/manage/snapshots/{snapshotId}/publish | publishSnapshot
[**revertSnapshotUsingPOST**](ManageApi.md#revertSnapshotUsingPOST) | **POST** /restv2/game/{apiKey}/manage/snapshots/{snapshotId}/revert | revertSnapshot
[**updateQueryUsingPUT**](ManageApi.md#updateQueryUsingPUT) | **PUT** /restv2/game/{apiKey}/manage/queries/{shortCode} | updateQuery
[**updateScreenUsingPUT**](ManageApi.md#updateScreenUsingPUT) | **PUT** /restv2/game/{apiKey}/manage/screens/{shortCode} | updateScreen
[**updateSnippetUsingPUT**](ManageApi.md#updateSnippetUsingPUT) | **PUT** /restv2/game/{apiKey}/manage/snippets/{shortCode} | updateSnippet



## copySnapshotToExistingGameUsingPOST

> ManageResult copySnapshotToExistingGameUsingPOST(apiKey, snapshotId, targetApiKey)

copySnapshotToExistingGame

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.ManageApi();
let apiKey = "apiKey_example"; // String | apiKey
let snapshotId = "snapshotId_example"; // String | snapshotId
let targetApiKey = "targetApiKey_example"; // String | targetApiKey
apiInstance.copySnapshotToExistingGameUsingPOST(apiKey, snapshotId, targetApiKey, (error, data, response) => {
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
 **snapshotId** | **String**| snapshotId | 
 **targetApiKey** | **String**| targetApiKey | 

### Return type

[**ManageResult**](ManageResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## createQueryUsingPOST

> ManageQuery createQueryUsingPOST(apiKey, manageQuery)

createQuery

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.ManageApi();
let apiKey = "apiKey_example"; // String | apiKey
let manageQuery = new GameSparksGameDetailsApi.ManageQuery(); // ManageQuery | query
apiInstance.createQueryUsingPOST(apiKey, manageQuery, (error, data, response) => {
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
 **manageQuery** | [**ManageQuery**](ManageQuery.md)| query | 

### Return type

[**ManageQuery**](ManageQuery.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json;charset=UTF-8


## createScreenUsingPOST

> ManageScreen createScreenUsingPOST(apiKey, manageScreen)

createScreen

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.ManageApi();
let apiKey = "apiKey_example"; // String | apiKey
let manageScreen = new GameSparksGameDetailsApi.ManageScreen(); // ManageScreen | screen
apiInstance.createScreenUsingPOST(apiKey, manageScreen, (error, data, response) => {
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
 **manageScreen** | [**ManageScreen**](ManageScreen.md)| screen | 

### Return type

[**ManageScreen**](ManageScreen.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json;charset=UTF-8


## createSnapshotUsingPOST

> ManageSnapshot createSnapshotUsingPOST(apiKey, snapshotCreationModel)

createSnapshot

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.ManageApi();
let apiKey = "apiKey_example"; // String | apiKey
let snapshotCreationModel = new GameSparksGameDetailsApi.SnapshotCreationModel(); // SnapshotCreationModel | model
apiInstance.createSnapshotUsingPOST(apiKey, snapshotCreationModel, (error, data, response) => {
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
 **snapshotCreationModel** | [**SnapshotCreationModel**](SnapshotCreationModel.md)| model | 

### Return type

[**ManageSnapshot**](ManageSnapshot.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json;charset=UTF-8


## createSnippetUsingPOST

> ManageSnippet createSnippetUsingPOST(apiKey, manageSnippet)

createSnippet

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.ManageApi();
let apiKey = "apiKey_example"; // String | apiKey
let manageSnippet = new GameSparksGameDetailsApi.ManageSnippet(); // ManageSnippet | snippet
apiInstance.createSnippetUsingPOST(apiKey, manageSnippet, (error, data, response) => {
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
 **manageSnippet** | [**ManageSnippet**](ManageSnippet.md)| snippet | 

### Return type

[**ManageSnippet**](ManageSnippet.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json;charset=UTF-8


## deleteQueryUsingDELETE

> ManageResult deleteQueryUsingDELETE(apiKey, shortCode)

deleteQuery

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.ManageApi();
let apiKey = "apiKey_example"; // String | apiKey
let shortCode = "shortCode_example"; // String | shortCode
apiInstance.deleteQueryUsingDELETE(apiKey, shortCode, (error, data, response) => {
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
 **shortCode** | **String**| shortCode | 

### Return type

[**ManageResult**](ManageResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## deleteScreenUsingDELETE

> ManageResult deleteScreenUsingDELETE(apiKey, shortCode)

deleteScreen

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.ManageApi();
let apiKey = "apiKey_example"; // String | apiKey
let shortCode = "shortCode_example"; // String | shortCode
apiInstance.deleteScreenUsingDELETE(apiKey, shortCode, (error, data, response) => {
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
 **shortCode** | **String**| shortCode | 

### Return type

[**ManageResult**](ManageResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## deleteSnapshotUsingDELETE

> deleteSnapshotUsingDELETE(apiKey, snapshotId)

deleteSnapshot

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.ManageApi();
let apiKey = "apiKey_example"; // String | apiKey
let snapshotId = "snapshotId_example"; // String | snapshotId
apiInstance.deleteSnapshotUsingDELETE(apiKey, snapshotId, (error, data, response) => {
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
 **apiKey** | **String**| apiKey | 
 **snapshotId** | **String**| snapshotId | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## deleteSnippetUsingDELETE

> ManageResult deleteSnippetUsingDELETE(apiKey, shortCode)

deleteSnippet

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.ManageApi();
let apiKey = "apiKey_example"; // String | apiKey
let shortCode = "shortCode_example"; // String | shortCode
apiInstance.deleteSnippetUsingDELETE(apiKey, shortCode, (error, data, response) => {
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
 **shortCode** | **String**| shortCode | 

### Return type

[**ManageResult**](ManageResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## getQueryUsingGET

> ManageQuery getQueryUsingGET(apiKey, shortCode)

getQuery

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.ManageApi();
let apiKey = "apiKey_example"; // String | apiKey
let shortCode = "shortCode_example"; // String | shortCode
apiInstance.getQueryUsingGET(apiKey, shortCode, (error, data, response) => {
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
 **shortCode** | **String**| shortCode | 

### Return type

[**ManageQuery**](ManageQuery.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## getScreenUsingGET

> ManageScreen getScreenUsingGET(apiKey, shortCode)

getScreen

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.ManageApi();
let apiKey = "apiKey_example"; // String | apiKey
let shortCode = "shortCode_example"; // String | shortCode
apiInstance.getScreenUsingGET(apiKey, shortCode, (error, data, response) => {
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
 **shortCode** | **String**| shortCode | 

### Return type

[**ManageScreen**](ManageScreen.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## getSnippetUsingGET

> ManageSnippet getSnippetUsingGET(apiKey, shortCode)

getSnippet

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.ManageApi();
let apiKey = "apiKey_example"; // String | apiKey
let shortCode = "shortCode_example"; // String | shortCode
apiInstance.getSnippetUsingGET(apiKey, shortCode, (error, data, response) => {
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
 **shortCode** | **String**| shortCode | 

### Return type

[**ManageSnippet**](ManageSnippet.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## listExecutableScreensUsingGET

> [ManageItemSummary] listExecutableScreensUsingGET(apiKey)

listExecutableScreens

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.ManageApi();
let apiKey = "apiKey_example"; // String | apiKey
apiInstance.listExecutableScreensUsingGET(apiKey, (error, data, response) => {
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

[**[ManageItemSummary]**](ManageItemSummary.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## listQueriesUsingGET

> [ManageItemSummary] listQueriesUsingGET(apiKey)

listQueries

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.ManageApi();
let apiKey = "apiKey_example"; // String | apiKey
apiInstance.listQueriesUsingGET(apiKey, (error, data, response) => {
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

[**[ManageItemSummary]**](ManageItemSummary.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## listScreensUsingGET

> [ManageItemSummary] listScreensUsingGET(apiKey)

listScreens

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.ManageApi();
let apiKey = "apiKey_example"; // String | apiKey
apiInstance.listScreensUsingGET(apiKey, (error, data, response) => {
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

[**[ManageItemSummary]**](ManageItemSummary.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## listSnapshotsUsingGET

> [ManageSnapshot] listSnapshotsUsingGET(apiKey)

listSnapshots

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.ManageApi();
let apiKey = "apiKey_example"; // String | apiKey
apiInstance.listSnapshotsUsingGET(apiKey, (error, data, response) => {
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

[**[ManageSnapshot]**](ManageSnapshot.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## listSnippetsUsingGET

> [ManageItemSummary] listSnippetsUsingGET(apiKey)

listSnippets

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.ManageApi();
let apiKey = "apiKey_example"; // String | apiKey
apiInstance.listSnippetsUsingGET(apiKey, (error, data, response) => {
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

[**[ManageItemSummary]**](ManageItemSummary.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## publishSnapshotUsingPOST

> ManageResult publishSnapshotUsingPOST(apiKey, snapshotId)

publishSnapshot

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.ManageApi();
let apiKey = "apiKey_example"; // String | apiKey
let snapshotId = "snapshotId_example"; // String | snapshotId
apiInstance.publishSnapshotUsingPOST(apiKey, snapshotId, (error, data, response) => {
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
 **snapshotId** | **String**| snapshotId | 

### Return type

[**ManageResult**](ManageResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## revertSnapshotUsingPOST

> ManageResult revertSnapshotUsingPOST(apiKey, snapshotId)

revertSnapshot

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.ManageApi();
let apiKey = "apiKey_example"; // String | apiKey
let snapshotId = "snapshotId_example"; // String | snapshotId
apiInstance.revertSnapshotUsingPOST(apiKey, snapshotId, (error, data, response) => {
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
 **snapshotId** | **String**| snapshotId | 

### Return type

[**ManageResult**](ManageResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## updateQueryUsingPUT

> ManageQuery updateQueryUsingPUT(apiKey, shortCode, manageQuery)

updateQuery

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.ManageApi();
let apiKey = "apiKey_example"; // String | apiKey
let shortCode = "shortCode_example"; // String | shortCode
let manageQuery = new GameSparksGameDetailsApi.ManageQuery(); // ManageQuery | query
apiInstance.updateQueryUsingPUT(apiKey, shortCode, manageQuery, (error, data, response) => {
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
 **shortCode** | **String**| shortCode | 
 **manageQuery** | [**ManageQuery**](ManageQuery.md)| query | 

### Return type

[**ManageQuery**](ManageQuery.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json;charset=UTF-8


## updateScreenUsingPUT

> ManageScreen updateScreenUsingPUT(apiKey, shortCode, manageScreen)

updateScreen

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.ManageApi();
let apiKey = "apiKey_example"; // String | apiKey
let shortCode = "shortCode_example"; // String | shortCode
let manageScreen = new GameSparksGameDetailsApi.ManageScreen(); // ManageScreen | screen
apiInstance.updateScreenUsingPUT(apiKey, shortCode, manageScreen, (error, data, response) => {
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
 **shortCode** | **String**| shortCode | 
 **manageScreen** | [**ManageScreen**](ManageScreen.md)| screen | 

### Return type

[**ManageScreen**](ManageScreen.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json;charset=UTF-8


## updateSnippetUsingPUT

> ManageSnippet updateSnippetUsingPUT(apiKey, shortCode, manageSnippet)

updateSnippet

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.ManageApi();
let apiKey = "apiKey_example"; // String | apiKey
let shortCode = "shortCode_example"; // String | shortCode
let manageSnippet = new GameSparksGameDetailsApi.ManageSnippet(); // ManageSnippet | snippet
apiInstance.updateSnippetUsingPUT(apiKey, shortCode, manageSnippet, (error, data, response) => {
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
 **shortCode** | **String**| shortCode | 
 **manageSnippet** | [**ManageSnippet**](ManageSnippet.md)| snippet | 

### Return type

[**ManageSnippet**](ManageSnippet.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json;charset=UTF-8

