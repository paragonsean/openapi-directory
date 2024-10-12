# AgcoApi.UpdateSystemApi

All URIs are relative to *https://secure.agco-ats.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**updateSystemGetCachedFiles**](UpdateSystemApi.md#updateSystemGetCachedFiles) | **GET** /api/v2/Clients/{ClientID}/CachedFiles | Get a list of Cached Files installed on the client Machine.
[**updateSystemGetCheckin**](UpdateSystemApi.md#updateSystemGetCheckin) | **GET** /api/v2/UpdateSystem | Checks the Client ID into the Update System.



## updateSystemGetCachedFiles

> [String] updateSystemGetCachedFiles(clientID, expired)

Get a list of Cached Files installed on the client Machine.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.UpdateSystemApi();
let clientID = "clientID_example"; // String | The ClientID of the Client
let expired = true; // Boolean | Only Expired Files (true|false)
apiInstance.updateSystemGetCachedFiles(clientID, expired, (error, data, response) => {
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
 **clientID** | **String**| The ClientID of the Client | 
 **expired** | **Boolean**| Only Expired Files (true|false) | 

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## updateSystemGetCheckin

> UpdateSystemModelsCheckinResult updateSystemGetCheckin(clientID, preview, opts)

Checks the Client ID into the Update System.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.UpdateSystemApi();
let clientID = "clientID_example"; // String | The Client ID to check-in.  If this is a new client ID it will be added to Clients.
let preview = true; // Boolean | Get Pkgs w\\o updating Datetimes(true|false)
let opts = {
  'runAllInventories': true // Boolean | Force return inventories. Defaults to false.
};
apiInstance.updateSystemGetCheckin(clientID, preview, opts, (error, data, response) => {
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
 **clientID** | **String**| The Client ID to check-in.  If this is a new client ID it will be added to Clients. | 
 **preview** | **Boolean**| Get Pkgs w\\o updating Datetimes(true|false) | 
 **runAllInventories** | **Boolean**| Force return inventories. Defaults to false. | [optional] 

### Return type

[**UpdateSystemModelsCheckinResult**](UpdateSystemModelsCheckinResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

