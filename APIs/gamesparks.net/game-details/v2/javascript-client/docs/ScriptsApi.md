# GameSparksGameDetailsApi.ScriptsApi

All URIs are relative to *http://config2.gamesparks.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**exportZipUsingGET**](ScriptsApi.md#exportZipUsingGET) | **GET** /restv2/game/{apiKey}/admin/scripts/export | exportZip
[**getScriptDifferencesUsingGET**](ScriptsApi.md#getScriptDifferencesUsingGET) | **GET** /restv2/game/{apiKey}/admin/scripts/differences/{snapshotId1}/{snapshotId2} | getScriptDifferences
[**getScriptVersionsUsingGET**](ScriptsApi.md#getScriptVersionsUsingGET) | **GET** /restv2/game/{apiKey}/admin/scripts/versions/{page} | getScriptVersions
[**getScriptVersionsUsingGET1**](ScriptsApi.md#getScriptVersionsUsingGET1) | **GET** /restv2/game/{apiKey}/admin/scripts/versions | getScriptVersions
[**importAcceptUsingPOST**](ScriptsApi.md#importAcceptUsingPOST) | **POST** /restv2/game/{apiKey}/admin/scripts/import/accept | importAccept
[**importZipUsingPOST**](ScriptsApi.md#importZipUsingPOST) | **POST** /restv2/game/{apiKey}/admin/scripts/import/preview | importZip



## exportZipUsingGET

> exportZipUsingGET(apiKey)

exportZip

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.ScriptsApi();
let apiKey = "apiKey_example"; // String | apiKey
apiInstance.exportZipUsingGET(apiKey, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getScriptDifferencesUsingGET

> ScriptsDifferenceListModel getScriptDifferencesUsingGET(apiKey, snapshotId1, snapshotId2)

getScriptDifferences

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.ScriptsApi();
let apiKey = "apiKey_example"; // String | apiKey
let snapshotId1 = "snapshotId1_example"; // String | snapshotId1
let snapshotId2 = "snapshotId2_example"; // String | snapshotId2
apiInstance.getScriptDifferencesUsingGET(apiKey, snapshotId1, snapshotId2, (error, data, response) => {
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
 **snapshotId1** | **String**| snapshotId1 | 
 **snapshotId2** | **String**| snapshotId2 | 

### Return type

[**ScriptsDifferenceListModel**](ScriptsDifferenceListModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getScriptVersionsUsingGET

> SnapshotScriptVersionListModel getScriptVersionsUsingGET(apiKey, page, opts)

getScriptVersions

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.ScriptsApi();
let apiKey = "apiKey_example"; // String | apiKey
let page = 56; // Number | page
let opts = {
  'pageSize': 100 // Number | pageSize
};
apiInstance.getScriptVersionsUsingGET(apiKey, page, opts, (error, data, response) => {
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
 **pageSize** | **Number**| pageSize | [optional] [default to 100]

### Return type

[**SnapshotScriptVersionListModel**](SnapshotScriptVersionListModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getScriptVersionsUsingGET1

> SnapshotScriptVersionListModel getScriptVersionsUsingGET1(apiKey, opts)

getScriptVersions

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.ScriptsApi();
let apiKey = "apiKey_example"; // String | apiKey
let opts = {
  'pageSize': 100 // Number | pageSize
};
apiInstance.getScriptVersionsUsingGET1(apiKey, opts, (error, data, response) => {
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
 **pageSize** | **Number**| pageSize | [optional] [default to 100]

### Return type

[**SnapshotScriptVersionListModel**](SnapshotScriptVersionListModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## importAcceptUsingPOST

> MessageModel importAcceptUsingPOST(apiKey, body, file)

importAccept

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.ScriptsApi();
let apiKey = "apiKey_example"; // String | apiKey
let body = "body_example"; // String | body
let file = "/path/to/file"; // File | file
apiInstance.importAcceptUsingPOST(apiKey, body, file, (error, data, response) => {
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
 **body** | **String**| body | 
 **file** | **File**| file | 

### Return type

[**MessageModel**](MessageModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json;charset=UTF-8


## importZipUsingPOST

> ScriptsDifferenceListModel importZipUsingPOST(apiKey, file)

importZip

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.ScriptsApi();
let apiKey = "apiKey_example"; // String | apiKey
let file = "/path/to/file"; // File | file
apiInstance.importZipUsingPOST(apiKey, file, (error, data, response) => {
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
 **file** | **File**| file | 

### Return type

[**ScriptsDifferenceListModel**](ScriptsDifferenceListModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json;charset=UTF-8

