# NetlifysApiDocumentation.AuditLogApi

All URIs are relative to *https://api.netlify.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listAccountAuditEvents**](AuditLogApi.md#listAccountAuditEvents) | **GET** /accounts/{account_id}/audit | 



## listAccountAuditEvents

> [AuditLog] listAccountAuditEvents(accountId, opts)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.AuditLogApi();
let accountId = "accountId_example"; // String | 
let opts = {
  'query': "query_example", // String | 
  'logType': "logType_example", // String | 
  'page': 56, // Number | 
  'perPage': 56 // Number | 
};
apiInstance.listAccountAuditEvents(accountId, opts, (error, data, response) => {
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
 **accountId** | **String**|  | 
 **query** | **String**|  | [optional] 
 **logType** | **String**|  | [optional] 
 **page** | **Number**|  | [optional] 
 **perPage** | **Number**|  | [optional] 

### Return type

[**[AuditLog]**](AuditLog.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

