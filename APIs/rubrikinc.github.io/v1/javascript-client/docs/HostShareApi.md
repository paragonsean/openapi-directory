# RubrikRestApi.HostShareApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulkAddHostShares**](HostShareApi.md#bulkAddHostShares) | **POST** /host/share/bulk | Add NAS shares in bulk
[**bulkUpdateHostShare**](HostShareApi.md#bulkUpdateHostShare) | **PATCH** /host/share/bulk | Update network shares



## bulkAddHostShares

> BulkShareAddResponse bulkAddHostShares(nasSharesToAdd)

Add NAS shares in bulk

Add NAS shares for a NAS host to the Rubrik cluster in bulk. This operation does not validate share credentials. If the default share credentials are incorrect, the share status on shares UI displays as \&quot;Wrong credential\&quot;. Use the PATCH /v1/host/share/bulk endpoint to enter the correct credentials when this status displays.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.HostShareApi();
let nasSharesToAdd = new RubrikRestApi.NasSharesToAdd(); // NasSharesToAdd | The properties used to add the NAS Shares to the Rubrik cluster.
apiInstance.bulkAddHostShares(nasSharesToAdd, (error, data, response) => {
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
 **nasSharesToAdd** | [**NasSharesToAdd**](NasSharesToAdd.md)| The properties used to add the NAS Shares to the Rubrik cluster. | 

### Return type

[**BulkShareAddResponse**](BulkShareAddResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## bulkUpdateHostShare

> [HostShareDetail] bulkUpdateHostShare(hostShareUpdate)

Update network shares

Update the properties of the objects that represent the specified network share.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.HostShareApi();
let hostShareUpdate = [new RubrikRestApi.HostShareUpdate()]; // [HostShareUpdate] | Properties to use for the update of network share objects.
apiInstance.bulkUpdateHostShare(hostShareUpdate, (error, data, response) => {
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
 **hostShareUpdate** | [**[HostShareUpdate]**](HostShareUpdate.md)| Properties to use for the update of network share objects. | 

### Return type

[**[HostShareDetail]**](HostShareDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

