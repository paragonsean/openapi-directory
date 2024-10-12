# FilesComApi.As2PartnersApi

All URIs are relative to *http://app.files.com/api/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteAs2PartnersId**](As2PartnersApi.md#deleteAs2PartnersId) | **DELETE** /as2_partners/{id} | Delete As2 Partner
[**getAs2Partners**](As2PartnersApi.md#getAs2Partners) | **GET** /as2_partners | List As2 Partners
[**getAs2PartnersId**](As2PartnersApi.md#getAs2PartnersId) | **GET** /as2_partners/{id} | Show As2 Partner
[**patchAs2PartnersId**](As2PartnersApi.md#patchAs2PartnersId) | **PATCH** /as2_partners/{id} | Update As2 Partner
[**postAs2Partners**](As2PartnersApi.md#postAs2Partners) | **POST** /as2_partners | Create As2 Partner



## deleteAs2PartnersId

> deleteAs2PartnersId(id)

Delete As2 Partner

Delete As2 Partner

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.As2PartnersApi();
let id = 56; // Number | As2 Partner ID.
apiInstance.deleteAs2PartnersId(id, (error, data, response) => {
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
 **id** | **Number**| As2 Partner ID. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getAs2Partners

> [As2PartnerEntity] getAs2Partners(opts)

List As2 Partners

List As2 Partners

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.As2PartnersApi();
let opts = {
  'cursor': "cursor_example", // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
  'perPage': 56 // Number | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
};
apiInstance.getAs2Partners(opts, (error, data, response) => {
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
 **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] 
 **perPage** | **Number**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] 

### Return type

[**[As2PartnerEntity]**](As2PartnerEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAs2PartnersId

> As2PartnerEntity getAs2PartnersId(id)

Show As2 Partner

Show As2 Partner

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.As2PartnersApi();
let id = 56; // Number | As2 Partner ID.
apiInstance.getAs2PartnersId(id, (error, data, response) => {
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
 **id** | **Number**| As2 Partner ID. | 

### Return type

[**As2PartnerEntity**](As2PartnerEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchAs2PartnersId

> As2PartnerEntity patchAs2PartnersId(id, opts)

Update As2 Partner

Update As2 Partner

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.As2PartnersApi();
let id = 56; // Number | As2 Partner ID.
let opts = {
  'enableDedicatedIps': true, // Boolean | 
  'name': "name_example", // String | AS2 Name
  'publicCertificate': "publicCertificate_example", // String | 
  'serverCertificate': "serverCertificate_example", // String | Remote server certificate security setting
  'uri': "uri_example" // String | URL base for AS2 responses
};
apiInstance.patchAs2PartnersId(id, opts, (error, data, response) => {
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
 **id** | **Number**| As2 Partner ID. | 
 **enableDedicatedIps** | **Boolean**|  | [optional] 
 **name** | **String**| AS2 Name | [optional] 
 **publicCertificate** | **String**|  | [optional] 
 **serverCertificate** | **String**| Remote server certificate security setting | [optional] 
 **uri** | **String**| URL base for AS2 responses | [optional] 

### Return type

[**As2PartnerEntity**](As2PartnerEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## postAs2Partners

> As2PartnerEntity postAs2Partners(as2StationId, name, publicCertificate, uri, opts)

Create As2 Partner

Create As2 Partner

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.As2PartnersApi();
let as2StationId = 56; // Number | Id of As2Station for this partner
let name = "name_example"; // String | AS2 Name
let publicCertificate = "publicCertificate_example"; // String | 
let uri = "uri_example"; // String | URL base for AS2 responses
let opts = {
  'enableDedicatedIps': true, // Boolean | 
  'serverCertificate': "serverCertificate_example" // String | Remote server certificate security setting
};
apiInstance.postAs2Partners(as2StationId, name, publicCertificate, uri, opts, (error, data, response) => {
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
 **as2StationId** | **Number**| Id of As2Station for this partner | 
 **name** | **String**| AS2 Name | 
 **publicCertificate** | **String**|  | 
 **uri** | **String**| URL base for AS2 responses | 
 **enableDedicatedIps** | **Boolean**|  | [optional] 
 **serverCertificate** | **String**| Remote server certificate security setting | [optional] 

### Return type

[**As2PartnerEntity**](As2PartnerEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

