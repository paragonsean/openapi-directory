# MagentoB2B.CreditmemoIdEmailsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**salesCreditmemoManagementV1NotifyPost**](CreditmemoIdEmailsApi.md#salesCreditmemoManagementV1NotifyPost) | **POST** /V1/creditmemo/{id}/emails | creditmemo/{id}/emails



## salesCreditmemoManagementV1NotifyPost

> Boolean salesCreditmemoManagementV1NotifyPost(id)

creditmemo/{id}/emails

Emails a user a specified credit memo.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CreditmemoIdEmailsApi();
let id = 56; // Number | The credit memo ID.
apiInstance.salesCreditmemoManagementV1NotifyPost(id, (error, data, response) => {
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
 **id** | **Number**| The credit memo ID. | 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

