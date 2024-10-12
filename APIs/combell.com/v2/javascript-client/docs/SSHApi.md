# PublicApi.SSHApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAllSshKeys**](SSHApi.md#getAllSshKeys) | **GET** /ssh | Overview of SSH keys



## getAllSshKeys

> [SshKeyDetail] getAllSshKeys(opts)

Overview of SSH keys

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.SSHApi();
let opts = {
  'skip': 56, // Number | The number of items to skip in the resultset.
  'take': 56 // Number | The number of items to return in the resultset. The returned count can be equal or less than this number.
};
apiInstance.getAllSshKeys(opts, (error, data, response) => {
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
 **skip** | **Number**| The number of items to skip in the resultset. | [optional] 
 **take** | **Number**| The number of items to return in the resultset. The returned count can be equal or less than this number. | [optional] 

### Return type

[**[SshKeyDetail]**](SshKeyDetail.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

