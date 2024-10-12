# SalesLoftPlatform.MimeEmailPayloadsApi

All URIs are relative to *https://api.salesloft.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2MimeEmailPayloadsIdJsonGet**](MimeEmailPayloadsApi.md#v2MimeEmailPayloadsIdJsonGet) | **GET** /v2/mime_email_payloads/{id}.json | Fetch the MIME content for email



## v2MimeEmailPayloadsIdJsonGet

> MimeEmailPayload v2MimeEmailPayloadsIdJsonGet(id)

Fetch the MIME content for email

Fetch the MIME content for email. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.MimeEmailPayloadsApi();
let id = "id_example"; // String | ID of Email
apiInstance.v2MimeEmailPayloadsIdJsonGet(id, (error, data, response) => {
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
 **id** | **String**| ID of Email | 

### Return type

[**MimeEmailPayload**](MimeEmailPayload.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

