# GettyImages.AssetChangesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v3AssetChangesChangeSetsChangeSetIdDelete**](AssetChangesApi.md#v3AssetChangesChangeSetsChangeSetIdDelete) | **DELETE** /v3/asset-changes/change-sets/{change-set-id} | Confirm asset change notifications.
[**v3AssetChangesChangeSetsPut**](AssetChangesApi.md#v3AssetChangesChangeSetsPut) | **PUT** /v3/asset-changes/change-sets | Get asset change notifications.
[**v3AssetChangesChannelsGet**](AssetChangesApi.md#v3AssetChangesChannelsGet) | **GET** /v3/asset-changes/channels | Get a list of asset change notification channels.



## v3AssetChangesChangeSetsChangeSetIdDelete

> v3AssetChangesChangeSetsChangeSetIdDelete(changeSetId)

Confirm asset change notifications.

# Delete Asset Changes  Confirm asset changes acknowledges receipt of asset changes (from the PUT asset-changes endpoint).  ##  Quickstart  You&#39;ll need an API key and an access token to use this resource.  Use the change_set_id from the PUT asset-changes/change-sets endpoint to confirm receipt of notifications. 

### Example

```javascript
import GettyImages from 'getty_images';
let defaultClient = GettyImages.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure API key authorization: Api-Key
let Api-Key = defaultClient.authentications['Api-Key'];
Api-Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Api-Key.apiKeyPrefix = 'Token';

let apiInstance = new GettyImages.AssetChangesApi();
let changeSetId = 789; // Number | Specify the change-set-id associated with a transaction resource whose receipt you want to confirm.
apiInstance.v3AssetChangesChangeSetsChangeSetIdDelete(changeSetId, (error, data, response) => {
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
 **changeSetId** | **Number**| Specify the change-set-id associated with a transaction resource whose receipt you want to confirm. | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [Api-Key](../README.md#Api-Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## v3AssetChangesChangeSetsPut

> AssetChanges v3AssetChangesChangeSetsPut(opts)

Get asset change notifications.

# Asset Changes  Get notifications about new, updated or deleted assets for a specific channel.  ##  Quickstart  You&#39;ll need an API key and an access token to use this resource.   Maximum batch size is 2200.  Change-sets must be confirmed before a new batch of notifications can be retrieved from this endpoint. Use the DELETE asset-changes/change-sets/{change-set-id} endpoint to confirm reciept of these notifications.  Values returned for asset_type include Image, Film, and null. Values returned for asset_lifecycle include New, Update, and Delete.  Delete notifications may be provided for asset ids that have not previously been received as New or Update notifications. Delete notifications may return null for the asset_type.  If there are no notifications in the channel an empty response body will be returned.  Notifications older than 60 days will be removed from partner channels. 

### Example

```javascript
import GettyImages from 'getty_images';
let defaultClient = GettyImages.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure API key authorization: Api-Key
let Api-Key = defaultClient.authentications['Api-Key'];
Api-Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Api-Key.apiKeyPrefix = 'Token';

let apiInstance = new GettyImages.AssetChangesApi();
let opts = {
  'channelId': 56, // Number | Specifies the id of the channel for the asset data. Valid channel ids can be found in the results of the Get Partner Channel query.
  'batchSize': 56 // Number | Specifies the number of assets to return. The default is 2200; maximum is 2200.
};
apiInstance.v3AssetChangesChangeSetsPut(opts, (error, data, response) => {
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
 **channelId** | **Number**| Specifies the id of the channel for the asset data. Valid channel ids can be found in the results of the Get Partner Channel query. | [optional] 
 **batchSize** | **Number**| Specifies the number of assets to return. The default is 2200; maximum is 2200. | [optional] 

### Return type

[**AssetChanges**](AssetChanges.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [Api-Key](../README.md#Api-Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## v3AssetChangesChannelsGet

> [Channel] v3AssetChangesChannelsGet()

Get a list of asset change notification channels.

# Get Partner Channels  Retrieves the channel data for the partner. This data can be used to populate the channel_id parameter in the Put Asset Changes query.  ##  Quickstart  You&#39;ll need an API key and an access token to use this resource.  Partners who have a channel that has been removed should contact their sales representative to be set up again.  

### Example

```javascript
import GettyImages from 'getty_images';
let defaultClient = GettyImages.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure API key authorization: Api-Key
let Api-Key = defaultClient.authentications['Api-Key'];
Api-Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Api-Key.apiKeyPrefix = 'Token';

let apiInstance = new GettyImages.AssetChangesApi();
apiInstance.v3AssetChangesChannelsGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[Channel]**](Channel.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [Api-Key](../README.md#Api-Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

