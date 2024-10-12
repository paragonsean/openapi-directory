# LinodeApi.LinodeTypesApi

All URIs are relative to *https://api.linode.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getLinodeType**](LinodeTypesApi.md#getLinodeType) | **GET** /linode/types/{typeId} | Type View
[**getLinodeTypes**](LinodeTypesApi.md#getLinodeTypes) | **GET** /linode/types | Types List



## getLinodeType

> LinodeType getLinodeType(typeId)

Type View

Returns information about a specific Linode Type, including pricing and specifications. This is used when [creating](/docs/api/linode-instances/#linode-create) or [resizing](/docs/api/linode-instances/#linode-resize) Linodes. 

### Example

```javascript
import LinodeApi from 'linode_api';

let apiInstance = new LinodeApi.LinodeTypesApi();
let typeId = "typeId_example"; // String | The ID of the Linode Type to look up.
apiInstance.getLinodeType(typeId, (error, data, response) => {
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
 **typeId** | **String**| The ID of the Linode Type to look up. | 

### Return type

[**LinodeType**](LinodeType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLinodeTypes

> GetLinodeTypes200Response getLinodeTypes()

Types List

Returns collection of Linode Types, including pricing and specifications for each Type. These are used when [creating](/docs/api/linode-instances/#linode-create) or [resizing](/docs/api/linode-instances/#linode-resize) Linodes. 

### Example

```javascript
import LinodeApi from 'linode_api';

let apiInstance = new LinodeApi.LinodeTypesApi();
apiInstance.getLinodeTypes((error, data, response) => {
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

[**GetLinodeTypes200Response**](GetLinodeTypes200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

