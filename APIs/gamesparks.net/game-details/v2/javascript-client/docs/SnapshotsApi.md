# GameSparksGameDetailsApi.SnapshotsApi

All URIs are relative to *http://config2.gamesparks.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**copySnapshotToExistingGameUsingPOST1**](SnapshotsApi.md#copySnapshotToExistingGameUsingPOST1) | **POST** /restv2/game/{apiKey}/admin/snapshots/{snapshotId}/copy/to/{targetApiKey} | copySnapshotToExistingGame
[**copySnapshotToNewGameUsingPOST**](SnapshotsApi.md#copySnapshotToNewGameUsingPOST) | **POST** /restv2/game/{apiKey}/admin/snapshots/{snapshotId}/copy | copySnapshotToNewGame
[**createSnapshotsUsingPOST**](SnapshotsApi.md#createSnapshotsUsingPOST) | **POST** /restv2/game/{apiKey}/admin/snapshots | createSnapshots
[**deleteSnapshotUsingDELETE1**](SnapshotsApi.md#deleteSnapshotUsingDELETE1) | **DELETE** /restv2/game/{apiKey}/admin/snapshots/{snapshotId} | deleteSnapshot
[**getLiveSnapshotIdUsingGET**](SnapshotsApi.md#getLiveSnapshotIdUsingGET) | **GET** /restv2/game/{apiKey}/admin/snapshots/liveSnapshotId | getLiveSnapshotId
[**getSnapshotUsingGET**](SnapshotsApi.md#getSnapshotUsingGET) | **GET** /restv2/game/{apiKey}/admin/snapshots/{snapshotId} | getSnapshot
[**getSnapshotsUsingGET**](SnapshotsApi.md#getSnapshotsUsingGET) | **GET** /restv2/game/{apiKey}/admin/snapshots/page/{page} | getSnapshots
[**getSnapshotsUsingGET1**](SnapshotsApi.md#getSnapshotsUsingGET1) | **GET** /restv2/game/{apiKey}/admin/snapshots | getSnapshots
[**publishSnapshotUsingPOST1**](SnapshotsApi.md#publishSnapshotUsingPOST1) | **POST** /restv2/game/{apiKey}/admin/snapshots/{snapshotId}/publish | publishSnapshot
[**revertToSnapshotUsingPOST**](SnapshotsApi.md#revertToSnapshotUsingPOST) | **POST** /restv2/game/{apiKey}/admin/snapshots/revert/to/{snapshotId} | revertToSnapshot
[**unpublishSnapshotUsingPOST**](SnapshotsApi.md#unpublishSnapshotUsingPOST) | **POST** /restv2/game/{apiKey}/admin/snapshots/{snapshotId}/unpublish | unpublishSnapshot



## copySnapshotToExistingGameUsingPOST1

> SnapshotCreationSuccessModel copySnapshotToExistingGameUsingPOST1(apiKey, snapshotId, targetApiKey, opts)

copySnapshotToExistingGame

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.SnapshotsApi();
let apiKey = "apiKey_example"; // String | apiKey
let snapshotId = "snapshotId_example"; // String | snapshotId
let targetApiKey = "targetApiKey_example"; // String | targetApiKey
let opts = {
  'includeGameConfig': true, // Boolean | includeGameConfig
  'includeMetadata': true, // Boolean | includeMetadata
  'includeBinaries': true, // Boolean | includeBinaries
  'includeCollaborators': true // Boolean | includeCollaborators
};
apiInstance.copySnapshotToExistingGameUsingPOST1(apiKey, snapshotId, targetApiKey, opts, (error, data, response) => {
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
 **includeGameConfig** | **Boolean**| includeGameConfig | [optional] [default to true]
 **includeMetadata** | **Boolean**| includeMetadata | [optional] [default to true]
 **includeBinaries** | **Boolean**| includeBinaries | [optional] [default to true]
 **includeCollaborators** | **Boolean**| includeCollaborators | [optional] [default to true]

### Return type

[**SnapshotCreationSuccessModel**](SnapshotCreationSuccessModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## copySnapshotToNewGameUsingPOST

> SnapshotCreationSuccessModel copySnapshotToNewGameUsingPOST(apiKey, snapshotId, opts)

copySnapshotToNewGame

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.SnapshotsApi();
let apiKey = "apiKey_example"; // String | apiKey
let snapshotId = "snapshotId_example"; // String | snapshotId
let opts = {
  'includeGameConfig': true, // Boolean | includeGameConfig
  'includeMetadata': true, // Boolean | includeMetadata
  'includeBinaries': true, // Boolean | includeBinaries
  'includeCollaborators': true // Boolean | includeCollaborators
};
apiInstance.copySnapshotToNewGameUsingPOST(apiKey, snapshotId, opts, (error, data, response) => {
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
 **includeGameConfig** | **Boolean**| includeGameConfig | [optional] [default to true]
 **includeMetadata** | **Boolean**| includeMetadata | [optional] [default to true]
 **includeBinaries** | **Boolean**| includeBinaries | [optional] [default to true]
 **includeCollaborators** | **Boolean**| includeCollaborators | [optional] [default to true]

### Return type

[**SnapshotCreationSuccessModel**](SnapshotCreationSuccessModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## createSnapshotsUsingPOST

> SnapshotModel createSnapshotsUsingPOST(apiKey, snapshotCreationModel)

createSnapshots

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.SnapshotsApi();
let apiKey = "apiKey_example"; // String | apiKey
let snapshotCreationModel = new GameSparksGameDetailsApi.SnapshotCreationModel(); // SnapshotCreationModel | description
apiInstance.createSnapshotsUsingPOST(apiKey, snapshotCreationModel, (error, data, response) => {
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
 **snapshotCreationModel** | [**SnapshotCreationModel**](SnapshotCreationModel.md)| description | 

### Return type

[**SnapshotModel**](SnapshotModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json;charset=UTF-8


## deleteSnapshotUsingDELETE1

> MessageModel deleteSnapshotUsingDELETE1(apiKey, snapshotId)

deleteSnapshot

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.SnapshotsApi();
let apiKey = "apiKey_example"; // String | apiKey
let snapshotId = "snapshotId_example"; // String | snapshotId
apiInstance.deleteSnapshotUsingDELETE1(apiKey, snapshotId, (error, data, response) => {
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

[**MessageModel**](MessageModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## getLiveSnapshotIdUsingGET

> MessageModel getLiveSnapshotIdUsingGET(apiKey)

getLiveSnapshotId

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.SnapshotsApi();
let apiKey = "apiKey_example"; // String | apiKey
apiInstance.getLiveSnapshotIdUsingGET(apiKey, (error, data, response) => {
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

[**MessageModel**](MessageModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## getSnapshotUsingGET

> SnapshotModel getSnapshotUsingGET(apiKey, snapshotId)

getSnapshot

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.SnapshotsApi();
let apiKey = "apiKey_example"; // String | apiKey
let snapshotId = "snapshotId_example"; // String | snapshotId
apiInstance.getSnapshotUsingGET(apiKey, snapshotId, (error, data, response) => {
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

[**SnapshotModel**](SnapshotModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## getSnapshotsUsingGET

> [SnapshotModel] getSnapshotsUsingGET(apiKey, page, opts)

getSnapshots

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.SnapshotsApi();
let apiKey = "apiKey_example"; // String | apiKey
let page = 56; // Number | page
let opts = {
  'pageSize': 20 // Number | pageSize
};
apiInstance.getSnapshotsUsingGET(apiKey, page, opts, (error, data, response) => {
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
 **page** | **Number**| page | 
 **pageSize** | **Number**| pageSize | [optional] [default to 20]

### Return type

[**[SnapshotModel]**](SnapshotModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## getSnapshotsUsingGET1

> [SnapshotModel] getSnapshotsUsingGET1(apiKey, opts)

getSnapshots

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.SnapshotsApi();
let apiKey = "apiKey_example"; // String | apiKey
let opts = {
  'pageSize': 20 // Number | pageSize
};
apiInstance.getSnapshotsUsingGET1(apiKey, opts, (error, data, response) => {
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
 **pageSize** | **Number**| pageSize | [optional] [default to 20]

### Return type

[**[SnapshotModel]**](SnapshotModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## publishSnapshotUsingPOST1

> publishSnapshotUsingPOST1(apiKey, snapshotId)

publishSnapshot

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.SnapshotsApi();
let apiKey = "apiKey_example"; // String | apiKey
let snapshotId = "snapshotId_example"; // String | snapshotId
apiInstance.publishSnapshotUsingPOST1(apiKey, snapshotId, (error, data, response) => {
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


## revertToSnapshotUsingPOST

> MessageModel revertToSnapshotUsingPOST(apiKey, snapshotId)

revertToSnapshot

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.SnapshotsApi();
let apiKey = "apiKey_example"; // String | apiKey
let snapshotId = "snapshotId_example"; // String | snapshotId
apiInstance.revertToSnapshotUsingPOST(apiKey, snapshotId, (error, data, response) => {
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

[**MessageModel**](MessageModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## unpublishSnapshotUsingPOST

> MessageModel unpublishSnapshotUsingPOST(apiKey, snapshotId)

unpublishSnapshot

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.SnapshotsApi();
let apiKey = "apiKey_example"; // String | apiKey
let snapshotId = "snapshotId_example"; // String | snapshotId
apiInstance.unpublishSnapshotUsingPOST(apiKey, snapshotId, (error, data, response) => {
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

[**MessageModel**](MessageModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8

