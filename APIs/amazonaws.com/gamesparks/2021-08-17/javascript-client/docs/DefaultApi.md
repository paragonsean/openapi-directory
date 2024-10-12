# GameSparks.DefaultApi

All URIs are relative to *http://gamesparks.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createGame**](DefaultApi.md#createGame) | **POST** /game | 
[**createSnapshot**](DefaultApi.md#createSnapshot) | **POST** /game/{GameName}/snapshot | 
[**createStage**](DefaultApi.md#createStage) | **POST** /game/{GameName}/stage | 
[**deleteGame**](DefaultApi.md#deleteGame) | **DELETE** /game/{GameName} | 
[**deleteStage**](DefaultApi.md#deleteStage) | **DELETE** /game/{GameName}/stage/{StageName} | 
[**disconnectPlayer**](DefaultApi.md#disconnectPlayer) | **POST** /runtime/game/{GameName}/stage/{StageName}/player/{PlayerId}/disconnect | 
[**exportSnapshot**](DefaultApi.md#exportSnapshot) | **GET** /game/{GameName}/snapshot/{SnapshotId}/export | 
[**getExtension**](DefaultApi.md#getExtension) | **GET** /extension/{Namespace}/{Name} | 
[**getExtensionVersion**](DefaultApi.md#getExtensionVersion) | **GET** /extension/{Namespace}/{Name}/version/{ExtensionVersion} | 
[**getGame**](DefaultApi.md#getGame) | **GET** /game/{GameName} | 
[**getGameConfiguration**](DefaultApi.md#getGameConfiguration) | **GET** /game/{GameName}/configuration | 
[**getGeneratedCodeJob**](DefaultApi.md#getGeneratedCodeJob) | **GET** /game/{GameName}/snapshot/{SnapshotId}/generated-sdk-code-job/{JobId} | 
[**getPlayerConnectionStatus**](DefaultApi.md#getPlayerConnectionStatus) | **GET** /runtime/game/{GameName}/stage/{StageName}/player/{PlayerId}/connection | 
[**getSnapshot**](DefaultApi.md#getSnapshot) | **GET** /game/{GameName}/snapshot/{SnapshotId} | 
[**getStage**](DefaultApi.md#getStage) | **GET** /game/{GameName}/stage/{StageName} | 
[**getStageDeployment**](DefaultApi.md#getStageDeployment) | **GET** /game/{GameName}/stage/{StageName}/deployment | 
[**importGameConfiguration**](DefaultApi.md#importGameConfiguration) | **PUT** /game/{GameName}/configuration | 
[**listExtensionVersions**](DefaultApi.md#listExtensionVersions) | **GET** /extension/{Namespace}/{Name}/version | 
[**listExtensions**](DefaultApi.md#listExtensions) | **GET** /extension | 
[**listGames**](DefaultApi.md#listGames) | **GET** /game | 
[**listGeneratedCodeJobs**](DefaultApi.md#listGeneratedCodeJobs) | **GET** /game/{GameName}/snapshot/{SnapshotId}/generated-sdk-code-jobs | 
[**listSnapshots**](DefaultApi.md#listSnapshots) | **GET** /game/{GameName}/snapshot | 
[**listStageDeployments**](DefaultApi.md#listStageDeployments) | **GET** /game/{GameName}/stage/{StageName}/deployments | 
[**listStages**](DefaultApi.md#listStages) | **GET** /game/{GameName}/stage | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /tags/{ResourceArn} | 
[**startGeneratedCodeJob**](DefaultApi.md#startGeneratedCodeJob) | **POST** /game/{GameName}/snapshot/{SnapshotId}/generated-sdk-code-job | 
[**startStageDeployment**](DefaultApi.md#startStageDeployment) | **POST** /game/{GameName}/stage/{StageName}/deployment | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /tags/{ResourceArn} | 
[**untagResource**](DefaultApi.md#untagResource) | **DELETE** /tags/{ResourceArn}#tagKeys | 
[**updateGame**](DefaultApi.md#updateGame) | **PATCH** /game/{GameName} | 
[**updateGameConfiguration**](DefaultApi.md#updateGameConfiguration) | **PATCH** /game/{GameName}/configuration | 
[**updateSnapshot**](DefaultApi.md#updateSnapshot) | **PATCH** /game/{GameName}/snapshot/{SnapshotId} | 
[**updateStage**](DefaultApi.md#updateStage) | **PATCH** /game/{GameName}/stage/{StageName} | 



## createGame

> CreateGameResult createGame(createGameRequest, opts)



 Creates a new game with an empty configuration. After creating your game, you can update the configuration using &lt;code&gt;UpdateGameConfiguration&lt;/code&gt; or &lt;code&gt;ImportGameConfiguration&lt;/code&gt;. 

### Example

```javascript
import GameSparks from 'game_sparks';
let defaultClient = GameSparks.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new GameSparks.DefaultApi();
let createGameRequest = new GameSparks.CreateGameRequest(); // CreateGameRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createGame(createGameRequest, opts, (error, data, response) => {
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
 **createGameRequest** | [**CreateGameRequest**](CreateGameRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateGameResult**](CreateGameResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createSnapshot

> CreateSnapshotResult createSnapshot(gameName, createSnapshotRequest, opts)



Creates a snapshot of the game configuration.

### Example

```javascript
import GameSparks from 'game_sparks';
let defaultClient = GameSparks.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new GameSparks.DefaultApi();
let gameName = "gameName_example"; // String | The name of the game.
let createSnapshotRequest = new GameSparks.CreateSnapshotRequest(); // CreateSnapshotRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createSnapshot(gameName, createSnapshotRequest, opts, (error, data, response) => {
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
 **gameName** | **String**| The name of the game. | 
 **createSnapshotRequest** | [**CreateSnapshotRequest**](CreateSnapshotRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateSnapshotResult**](CreateSnapshotResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createStage

> CreateStageResult createStage(gameName, createStageRequest, opts)



Creates a new stage for stage-by-stage game development and deployment.

### Example

```javascript
import GameSparks from 'game_sparks';
let defaultClient = GameSparks.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new GameSparks.DefaultApi();
let gameName = "gameName_example"; // String | The name of the game.
let createStageRequest = new GameSparks.CreateStageRequest(); // CreateStageRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createStage(gameName, createStageRequest, opts, (error, data, response) => {
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
 **gameName** | **String**| The name of the game. | 
 **createStageRequest** | [**CreateStageRequest**](CreateStageRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateStageResult**](CreateStageResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteGame

> Object deleteGame(gameName, opts)



Deletes a game.

### Example

```javascript
import GameSparks from 'game_sparks';
let defaultClient = GameSparks.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new GameSparks.DefaultApi();
let gameName = "gameName_example"; // String | The name of the game to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteGame(gameName, opts, (error, data, response) => {
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
 **gameName** | **String**| The name of the game to delete. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteStage

> Object deleteStage(gameName, stageName, opts)



Deletes a stage from a game, along with the associated game runtime.

### Example

```javascript
import GameSparks from 'game_sparks';
let defaultClient = GameSparks.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new GameSparks.DefaultApi();
let gameName = "gameName_example"; // String | The name of the game.
let stageName = "stageName_example"; // String | The name of the stage to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteStage(gameName, stageName, opts, (error, data, response) => {
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
 **gameName** | **String**| The name of the game. | 
 **stageName** | **String**| The name of the stage to delete. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## disconnectPlayer

> DisconnectPlayerResult disconnectPlayer(gameName, playerId, stageName, opts)



&lt;p&gt;Disconnects a player from the game runtime.&lt;/p&gt; &lt;p&gt; If a player has multiple connections, this operation attempts to close all of them. &lt;/p&gt;

### Example

```javascript
import GameSparks from 'game_sparks';
let defaultClient = GameSparks.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new GameSparks.DefaultApi();
let gameName = "gameName_example"; // String | The name of the game.
let playerId = "playerId_example"; // String | The unique identifier representing a player.
let stageName = "stageName_example"; // String | The name of the stage.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.disconnectPlayer(gameName, playerId, stageName, opts, (error, data, response) => {
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
 **gameName** | **String**| The name of the game. | 
 **playerId** | **String**| The unique identifier representing a player. | 
 **stageName** | **String**| The name of the stage. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DisconnectPlayerResult**](DisconnectPlayerResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## exportSnapshot

> ExportSnapshotResult exportSnapshot(gameName, snapshotId, opts)



Exports a game configuration snapshot.

### Example

```javascript
import GameSparks from 'game_sparks';
let defaultClient = GameSparks.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new GameSparks.DefaultApi();
let gameName = "gameName_example"; // String | The name of the game.
let snapshotId = "snapshotId_example"; // String | The identifier of the snapshot to export.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.exportSnapshot(gameName, snapshotId, opts, (error, data, response) => {
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
 **gameName** | **String**| The name of the game. | 
 **snapshotId** | **String**| The identifier of the snapshot to export. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ExportSnapshotResult**](ExportSnapshotResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getExtension

> GetExtensionResult getExtension(name, namespace, opts)



Gets details about a specified extension.

### Example

```javascript
import GameSparks from 'game_sparks';
let defaultClient = GameSparks.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new GameSparks.DefaultApi();
let name = "name_example"; // String | The name of the extension.
let namespace = "namespace_example"; // String | The namespace (qualifier) of the extension.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getExtension(name, namespace, opts, (error, data, response) => {
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
 **name** | **String**| The name of the extension. | 
 **namespace** | **String**| The namespace (qualifier) of the extension. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetExtensionResult**](GetExtensionResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getExtensionVersion

> GetExtensionVersionResult getExtensionVersion(extensionVersion, name, namespace, opts)



Gets details about a specified extension version.

### Example

```javascript
import GameSparks from 'game_sparks';
let defaultClient = GameSparks.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new GameSparks.DefaultApi();
let extensionVersion = "extensionVersion_example"; // String | The version of the extension.
let name = "name_example"; // String | The name of the extension.
let namespace = "namespace_example"; // String | The namespace (qualifier) of the extension.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getExtensionVersion(extensionVersion, name, namespace, opts, (error, data, response) => {
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
 **extensionVersion** | **String**| The version of the extension. | 
 **name** | **String**| The name of the extension. | 
 **namespace** | **String**| The namespace (qualifier) of the extension. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetExtensionVersionResult**](GetExtensionVersionResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGame

> GetGameResult getGame(gameName, opts)



Gets details about a game.

### Example

```javascript
import GameSparks from 'game_sparks';
let defaultClient = GameSparks.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new GameSparks.DefaultApi();
let gameName = "gameName_example"; // String | The name of the game.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getGame(gameName, opts, (error, data, response) => {
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
 **gameName** | **String**| The name of the game. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetGameResult**](GetGameResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGameConfiguration

> GetGameConfigurationResult getGameConfiguration(gameName, opts)



Gets the configuration of the game.

### Example

```javascript
import GameSparks from 'game_sparks';
let defaultClient = GameSparks.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new GameSparks.DefaultApi();
let gameName = "gameName_example"; // String | The name of the game.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'sections': ["null"] // [String] | The list of sections to return.
};
apiInstance.getGameConfiguration(gameName, opts, (error, data, response) => {
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
 **gameName** | **String**| The name of the game. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **sections** | [**[String]**](String.md)| The list of sections to return. | [optional] 

### Return type

[**GetGameConfigurationResult**](GetGameConfigurationResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGeneratedCodeJob

> GetGeneratedCodeJobResult getGeneratedCodeJob(gameName, jobId, snapshotId, opts)



Gets details about a job that is generating code for a snapshot.

### Example

```javascript
import GameSparks from 'game_sparks';
let defaultClient = GameSparks.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new GameSparks.DefaultApi();
let gameName = "gameName_example"; // String | The name of the game.
let jobId = "jobId_example"; // String | The identifier of the code generation job.
let snapshotId = "snapshotId_example"; // String | The identifier of the snapshot for the code generation job.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getGeneratedCodeJob(gameName, jobId, snapshotId, opts, (error, data, response) => {
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
 **gameName** | **String**| The name of the game. | 
 **jobId** | **String**| The identifier of the code generation job. | 
 **snapshotId** | **String**| The identifier of the snapshot for the code generation job. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetGeneratedCodeJobResult**](GetGeneratedCodeJobResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPlayerConnectionStatus

> GetPlayerConnectionStatusResult getPlayerConnectionStatus(gameName, playerId, stageName, opts)



&lt;p&gt;Gets the status of a player&#39;s connection to the game runtime.&lt;/p&gt; &lt;p&gt; It&#39;s possible for a single player to have multiple connections to the game runtime. If a player is not connected, this operation returns an empty list. &lt;/p&gt;

### Example

```javascript
import GameSparks from 'game_sparks';
let defaultClient = GameSparks.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new GameSparks.DefaultApi();
let gameName = "gameName_example"; // String | The name of the game.
let playerId = "playerId_example"; // String | The unique identifier representing a player.
let stageName = "stageName_example"; // String | The name of the stage.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getPlayerConnectionStatus(gameName, playerId, stageName, opts, (error, data, response) => {
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
 **gameName** | **String**| The name of the game. | 
 **playerId** | **String**| The unique identifier representing a player. | 
 **stageName** | **String**| The name of the stage. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetPlayerConnectionStatusResult**](GetPlayerConnectionStatusResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSnapshot

> GetSnapshotResult getSnapshot(gameName, snapshotId, opts)



Gets a copy of the game configuration in a snapshot.

### Example

```javascript
import GameSparks from 'game_sparks';
let defaultClient = GameSparks.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new GameSparks.DefaultApi();
let gameName = "gameName_example"; // String | The name of the game.
let snapshotId = "snapshotId_example"; // String | The identifier of the snapshot.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'sections': ["null"] // [String] | The list of game configuration sections to be described.
};
apiInstance.getSnapshot(gameName, snapshotId, opts, (error, data, response) => {
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
 **gameName** | **String**| The name of the game. | 
 **snapshotId** | **String**| The identifier of the snapshot. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **sections** | [**[String]**](String.md)| The list of game configuration sections to be described. | [optional] 

### Return type

[**GetSnapshotResult**](GetSnapshotResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getStage

> GetStageResult getStage(gameName, stageName, opts)



Gets information about a stage.

### Example

```javascript
import GameSparks from 'game_sparks';
let defaultClient = GameSparks.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new GameSparks.DefaultApi();
let gameName = "gameName_example"; // String | The name of the game.
let stageName = "stageName_example"; // String | The name of the stage.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getStage(gameName, stageName, opts, (error, data, response) => {
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
 **gameName** | **String**| The name of the game. | 
 **stageName** | **String**| The name of the stage. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetStageResult**](GetStageResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getStageDeployment

> GetStageDeploymentResult getStageDeployment(gameName, stageName, opts)



Gets information about a stage deployment.

### Example

```javascript
import GameSparks from 'game_sparks';
let defaultClient = GameSparks.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new GameSparks.DefaultApi();
let gameName = "gameName_example"; // String | The name of the game.
let stageName = "stageName_example"; // String | The name of the stage.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'deploymentId': "deploymentId_example" // String |  The identifier of the stage deployment. <code>StartStageDeployment</code> returns the identifier that you use here. 
};
apiInstance.getStageDeployment(gameName, stageName, opts, (error, data, response) => {
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
 **gameName** | **String**| The name of the game. | 
 **stageName** | **String**| The name of the stage. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **deploymentId** | **String**|  The identifier of the stage deployment. &lt;code&gt;StartStageDeployment&lt;/code&gt; returns the identifier that you use here.  | [optional] 

### Return type

[**GetStageDeploymentResult**](GetStageDeploymentResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## importGameConfiguration

> ImportGameConfigurationResult importGameConfiguration(gameName, importGameConfigurationRequest, opts)



&lt;p&gt;Imports a game configuration.&lt;/p&gt; &lt;p&gt; This operation replaces the current configuration of the game with the provided input. This is not a reversible operation. If you want to preserve the previous configuration, use &lt;code&gt;CreateSnapshot&lt;/code&gt; to make a new snapshot before importing. &lt;/p&gt;

### Example

```javascript
import GameSparks from 'game_sparks';
let defaultClient = GameSparks.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new GameSparks.DefaultApi();
let gameName = "gameName_example"; // String | The name of the game.
let importGameConfigurationRequest = new GameSparks.ImportGameConfigurationRequest(); // ImportGameConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.importGameConfiguration(gameName, importGameConfigurationRequest, opts, (error, data, response) => {
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
 **gameName** | **String**| The name of the game. | 
 **importGameConfigurationRequest** | [**ImportGameConfigurationRequest**](ImportGameConfigurationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ImportGameConfigurationResult**](ImportGameConfigurationResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listExtensionVersions

> ListExtensionVersionsResult listExtensionVersions(name, namespace, opts)



&lt;p&gt;Gets a paginated list of available versions for the extension.&lt;/p&gt; &lt;p&gt; Each time an API change is made to an extension, the version is incremented. The list retrieved by this operation shows the versions that are currently available. &lt;/p&gt;

### Example

```javascript
import GameSparks from 'game_sparks';
let defaultClient = GameSparks.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new GameSparks.DefaultApi();
let name = "name_example"; // String | The name of the extension.
let namespace = "namespace_example"; // String | The namespace (qualifier) of the extension.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | <p>The maximum number of results to return.</p> <p> Use this parameter with NextToken to get results as a set of sequential pages. </p>
  'nextToken': "nextToken_example" // String | <p>The token that indicates the start of the next sequential page of results.</p> <p> Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value. </p>
};
apiInstance.listExtensionVersions(name, namespace, opts, (error, data, response) => {
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
 **name** | **String**| The name of the extension. | 
 **namespace** | **String**| The namespace (qualifier) of the extension. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| &lt;p&gt;The maximum number of results to return.&lt;/p&gt; &lt;p&gt; Use this parameter with NextToken to get results as a set of sequential pages. &lt;/p&gt; | [optional] 
 **nextToken** | **String**| &lt;p&gt;The token that indicates the start of the next sequential page of results.&lt;/p&gt; &lt;p&gt; Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value. &lt;/p&gt; | [optional] 

### Return type

[**ListExtensionVersionsResult**](ListExtensionVersionsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listExtensions

> ListExtensionsResult listExtensions(opts)



&lt;p&gt;Gets a paginated list of available extensions.&lt;/p&gt; &lt;p&gt; Extensions provide features that games can use from scripts. &lt;/p&gt;

### Example

```javascript
import GameSparks from 'game_sparks';
let defaultClient = GameSparks.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new GameSparks.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | <p>The maximum number of results to return.</p> <p> Use this parameter with NextToken to get results as a set of sequential pages. </p>
  'nextToken': "nextToken_example" // String | <p>The token that indicates the start of the next sequential page of results.</p> <p> Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value. </p>
};
apiInstance.listExtensions(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| &lt;p&gt;The maximum number of results to return.&lt;/p&gt; &lt;p&gt; Use this parameter with NextToken to get results as a set of sequential pages. &lt;/p&gt; | [optional] 
 **nextToken** | **String**| &lt;p&gt;The token that indicates the start of the next sequential page of results.&lt;/p&gt; &lt;p&gt; Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value. &lt;/p&gt; | [optional] 

### Return type

[**ListExtensionsResult**](ListExtensionsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listGames

> ListGamesResult listGames(opts)



Gets a paginated list of games.

### Example

```javascript
import GameSparks from 'game_sparks';
let defaultClient = GameSparks.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new GameSparks.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | <p>The maximum number of results to return.</p> <p> Use this parameter with NextToken to get results as a set of sequential pages. </p>
  'nextToken': "nextToken_example" // String | <p>The token that indicates the start of the next sequential page of results.</p> <p> Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value. </p>
};
apiInstance.listGames(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| &lt;p&gt;The maximum number of results to return.&lt;/p&gt; &lt;p&gt; Use this parameter with NextToken to get results as a set of sequential pages. &lt;/p&gt; | [optional] 
 **nextToken** | **String**| &lt;p&gt;The token that indicates the start of the next sequential page of results.&lt;/p&gt; &lt;p&gt; Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value. &lt;/p&gt; | [optional] 

### Return type

[**ListGamesResult**](ListGamesResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listGeneratedCodeJobs

> ListGeneratedCodeJobsResult listGeneratedCodeJobs(gameName, snapshotId, opts)



Gets a paginated list of code generation jobs for a snapshot.

### Example

```javascript
import GameSparks from 'game_sparks';
let defaultClient = GameSparks.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new GameSparks.DefaultApi();
let gameName = "gameName_example"; // String | The name of the game.
let snapshotId = "snapshotId_example"; // String | The identifier of the snapshot.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | <p>The maximum number of results to return.</p> <p> Use this parameter with NextToken to get results as a set of sequential pages. </p>
  'nextToken': "nextToken_example" // String | <p>The token that indicates the start of the next sequential page of results.</p> <p> Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value. </p>
};
apiInstance.listGeneratedCodeJobs(gameName, snapshotId, opts, (error, data, response) => {
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
 **gameName** | **String**| The name of the game. | 
 **snapshotId** | **String**| The identifier of the snapshot. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| &lt;p&gt;The maximum number of results to return.&lt;/p&gt; &lt;p&gt; Use this parameter with NextToken to get results as a set of sequential pages. &lt;/p&gt; | [optional] 
 **nextToken** | **String**| &lt;p&gt;The token that indicates the start of the next sequential page of results.&lt;/p&gt; &lt;p&gt; Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value. &lt;/p&gt; | [optional] 

### Return type

[**ListGeneratedCodeJobsResult**](ListGeneratedCodeJobsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSnapshots

> ListSnapshotsResult listSnapshots(gameName, opts)



Gets a paginated list of snapshot summaries from the game.

### Example

```javascript
import GameSparks from 'game_sparks';
let defaultClient = GameSparks.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new GameSparks.DefaultApi();
let gameName = "gameName_example"; // String | The name of the game.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | <p>The maximum number of results to return.</p> <p> Use this parameter with NextToken to get results as a set of sequential pages. </p>
  'nextToken': "nextToken_example" // String | <p>The token that indicates the start of the next sequential page of results.</p> <p> Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value. </p>
};
apiInstance.listSnapshots(gameName, opts, (error, data, response) => {
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
 **gameName** | **String**| The name of the game. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| &lt;p&gt;The maximum number of results to return.&lt;/p&gt; &lt;p&gt; Use this parameter with NextToken to get results as a set of sequential pages. &lt;/p&gt; | [optional] 
 **nextToken** | **String**| &lt;p&gt;The token that indicates the start of the next sequential page of results.&lt;/p&gt; &lt;p&gt; Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value. &lt;/p&gt; | [optional] 

### Return type

[**ListSnapshotsResult**](ListSnapshotsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listStageDeployments

> ListStageDeploymentsResult listStageDeployments(gameName, stageName, opts)



Gets a paginated list of stage deployment summaries from the game.

### Example

```javascript
import GameSparks from 'game_sparks';
let defaultClient = GameSparks.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new GameSparks.DefaultApi();
let gameName = "gameName_example"; // String | The name of the game.
let stageName = "stageName_example"; // String | The name of the stage.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | <p>The maximum number of results to return.</p> <p> Use this parameter with NextToken to get results as a set of sequential pages. </p>
  'nextToken': "nextToken_example" // String | <p>The token that indicates the start of the next sequential page of results.</p> <p> Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value. </p>
};
apiInstance.listStageDeployments(gameName, stageName, opts, (error, data, response) => {
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
 **gameName** | **String**| The name of the game. | 
 **stageName** | **String**| The name of the stage. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| &lt;p&gt;The maximum number of results to return.&lt;/p&gt; &lt;p&gt; Use this parameter with NextToken to get results as a set of sequential pages. &lt;/p&gt; | [optional] 
 **nextToken** | **String**| &lt;p&gt;The token that indicates the start of the next sequential page of results.&lt;/p&gt; &lt;p&gt; Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value. &lt;/p&gt; | [optional] 

### Return type

[**ListStageDeploymentsResult**](ListStageDeploymentsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listStages

> ListStagesResult listStages(gameName, opts)



Gets a paginated list of stage summaries from the game.

### Example

```javascript
import GameSparks from 'game_sparks';
let defaultClient = GameSparks.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new GameSparks.DefaultApi();
let gameName = "gameName_example"; // String | The name of the game.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | <p>The maximum number of results to return.</p> <p> Use this parameter with NextToken to get results as a set of sequential pages. </p>
  'nextToken': "nextToken_example" // String | <p>The token that indicates the start of the next sequential page of results.</p> <p> Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value. </p>
};
apiInstance.listStages(gameName, opts, (error, data, response) => {
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
 **gameName** | **String**| The name of the game. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| &lt;p&gt;The maximum number of results to return.&lt;/p&gt; &lt;p&gt; Use this parameter with NextToken to get results as a set of sequential pages. &lt;/p&gt; | [optional] 
 **nextToken** | **String**| &lt;p&gt;The token that indicates the start of the next sequential page of results.&lt;/p&gt; &lt;p&gt; Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value. &lt;/p&gt; | [optional] 

### Return type

[**ListStagesResult**](ListStagesResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceResult listTagsForResource(resourceArn, opts)



Lists the tags associated with a GameSparks resource.

### Example

```javascript
import GameSparks from 'game_sparks';
let defaultClient = GameSparks.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new GameSparks.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the GameSparks resource.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listTagsForResource(resourceArn, opts, (error, data, response) => {
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
 **resourceArn** | **String**| The Amazon Resource Name (ARN) of the GameSparks resource. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ListTagsForResourceResult**](ListTagsForResourceResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## startGeneratedCodeJob

> StartGeneratedCodeJobResult startGeneratedCodeJob(gameName, snapshotId, startGeneratedCodeJobRequest, opts)



 Starts an asynchronous process that generates client code for system-defined and custom messages. The resulting code is collected as a .zip file and uploaded to a pre-signed Amazon S3 URL. 

### Example

```javascript
import GameSparks from 'game_sparks';
let defaultClient = GameSparks.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new GameSparks.DefaultApi();
let gameName = "gameName_example"; // String | The name of the game.
let snapshotId = "snapshotId_example"; // String | The identifier of the snapshot for which to generate code.
let startGeneratedCodeJobRequest = new GameSparks.StartGeneratedCodeJobRequest(); // StartGeneratedCodeJobRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startGeneratedCodeJob(gameName, snapshotId, startGeneratedCodeJobRequest, opts, (error, data, response) => {
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
 **gameName** | **String**| The name of the game. | 
 **snapshotId** | **String**| The identifier of the snapshot for which to generate code. | 
 **startGeneratedCodeJobRequest** | [**StartGeneratedCodeJobRequest**](StartGeneratedCodeJobRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartGeneratedCodeJobResult**](StartGeneratedCodeJobResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startStageDeployment

> StartStageDeploymentResult startStageDeployment(gameName, stageName, startStageDeploymentRequest, opts)



&lt;p&gt;Deploys a snapshot to the stage and creates a new game runtime.&lt;/p&gt; &lt;p&gt; After you call this operation, you can check the deployment status by using &lt;code&gt;GetStageDeployment&lt;/code&gt;. &lt;/p&gt; &lt;p&gt; If there are any players connected to the previous game runtime, then both runtimes persist. Existing connections to the previous runtime are maintained. When players disconnect and reconnect, they connect to the new runtime. After there are no connections to the previous game runtime, it is deleted. &lt;/p&gt;

### Example

```javascript
import GameSparks from 'game_sparks';
let defaultClient = GameSparks.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new GameSparks.DefaultApi();
let gameName = "gameName_example"; // String | The name of the game.
let stageName = "stageName_example"; // String | The name of the stage to deploy the snapshot onto.
let startStageDeploymentRequest = new GameSparks.StartStageDeploymentRequest(); // StartStageDeploymentRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startStageDeployment(gameName, stageName, startStageDeploymentRequest, opts, (error, data, response) => {
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
 **gameName** | **String**| The name of the game. | 
 **stageName** | **String**| The name of the stage to deploy the snapshot onto. | 
 **startStageDeploymentRequest** | [**StartStageDeploymentRequest**](StartStageDeploymentRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartStageDeploymentResult**](StartStageDeploymentResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tagResource

> Object tagResource(resourceArn, tagResourceRequest, opts)



Adds tags to a GameSparks resource.

### Example

```javascript
import GameSparks from 'game_sparks';
let defaultClient = GameSparks.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new GameSparks.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the resource to add the tags to.
let tagResourceRequest = new GameSparks.TagResourceRequest(); // TagResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.tagResource(resourceArn, tagResourceRequest, opts, (error, data, response) => {
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
 **resourceArn** | **String**| The Amazon Resource Name (ARN) of the resource to add the tags to. | 
 **tagResourceRequest** | [**TagResourceRequest**](TagResourceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## untagResource

> Object untagResource(resourceArn, tagKeys, opts)



Removes tags from a GameSparks resource.

### Example

```javascript
import GameSparks from 'game_sparks';
let defaultClient = GameSparks.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new GameSparks.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the resource to remove the tags from.
let tagKeys = ["null"]; // [String] | The keys of the tags to remove.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.untagResource(resourceArn, tagKeys, opts, (error, data, response) => {
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
 **resourceArn** | **String**| The Amazon Resource Name (ARN) of the resource to remove the tags from. | 
 **tagKeys** | [**[String]**](String.md)| The keys of the tags to remove. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateGame

> UpdateGameResult updateGame(gameName, updateGameRequest, opts)



Updates details of the game.

### Example

```javascript
import GameSparks from 'game_sparks';
let defaultClient = GameSparks.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new GameSparks.DefaultApi();
let gameName = "gameName_example"; // String | The name of the game.
let updateGameRequest = new GameSparks.UpdateGameRequest(); // UpdateGameRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateGame(gameName, updateGameRequest, opts, (error, data, response) => {
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
 **gameName** | **String**| The name of the game. | 
 **updateGameRequest** | [**UpdateGameRequest**](UpdateGameRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateGameResult**](UpdateGameResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateGameConfiguration

> UpdateGameConfigurationResult updateGameConfiguration(gameName, updateGameConfigurationRequest, opts)



Updates one or more sections of the game configuration.

### Example

```javascript
import GameSparks from 'game_sparks';
let defaultClient = GameSparks.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new GameSparks.DefaultApi();
let gameName = "gameName_example"; // String | The name of the game.
let updateGameConfigurationRequest = new GameSparks.UpdateGameConfigurationRequest(); // UpdateGameConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateGameConfiguration(gameName, updateGameConfigurationRequest, opts, (error, data, response) => {
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
 **gameName** | **String**| The name of the game. | 
 **updateGameConfigurationRequest** | [**UpdateGameConfigurationRequest**](UpdateGameConfigurationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateGameConfigurationResult**](UpdateGameConfigurationResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateSnapshot

> UpdateSnapshotResult updateSnapshot(gameName, snapshotId, createSnapshotRequest, opts)



Updates the metadata of a GameSparks snapshot.

### Example

```javascript
import GameSparks from 'game_sparks';
let defaultClient = GameSparks.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new GameSparks.DefaultApi();
let gameName = "gameName_example"; // String | The name of the game.
let snapshotId = "snapshotId_example"; // String | The identifier of the snapshot.
let createSnapshotRequest = new GameSparks.CreateSnapshotRequest(); // CreateSnapshotRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateSnapshot(gameName, snapshotId, createSnapshotRequest, opts, (error, data, response) => {
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
 **gameName** | **String**| The name of the game. | 
 **snapshotId** | **String**| The identifier of the snapshot. | 
 **createSnapshotRequest** | [**CreateSnapshotRequest**](CreateSnapshotRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateSnapshotResult**](UpdateSnapshotResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateStage

> UpdateStageResult updateStage(gameName, stageName, updateStageRequest, opts)



Updates the metadata of a stage.

### Example

```javascript
import GameSparks from 'game_sparks';
let defaultClient = GameSparks.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new GameSparks.DefaultApi();
let gameName = "gameName_example"; // String | The name of the game.
let stageName = "stageName_example"; // String | The name of the stage.
let updateStageRequest = new GameSparks.UpdateStageRequest(); // UpdateStageRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateStage(gameName, stageName, updateStageRequest, opts, (error, data, response) => {
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
 **gameName** | **String**| The name of the game. | 
 **stageName** | **String**| The name of the stage. | 
 **updateStageRequest** | [**UpdateStageRequest**](UpdateStageRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateStageResult**](UpdateStageResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

