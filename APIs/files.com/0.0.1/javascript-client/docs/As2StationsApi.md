# FilesComApi.As2StationsApi

All URIs are relative to *http://app.files.com/api/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteAs2StationsId**](As2StationsApi.md#deleteAs2StationsId) | **DELETE** /as2_stations/{id} | Delete As2 Station
[**getAs2Stations**](As2StationsApi.md#getAs2Stations) | **GET** /as2_stations | List As2 Stations
[**getAs2StationsId**](As2StationsApi.md#getAs2StationsId) | **GET** /as2_stations/{id} | Show As2 Station
[**patchAs2StationsId**](As2StationsApi.md#patchAs2StationsId) | **PATCH** /as2_stations/{id} | Update As2 Station
[**postAs2Stations**](As2StationsApi.md#postAs2Stations) | **POST** /as2_stations | Create As2 Station



## deleteAs2StationsId

> deleteAs2StationsId(id)

Delete As2 Station

Delete As2 Station

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.As2StationsApi();
let id = 56; // Number | As2 Station ID.
apiInstance.deleteAs2StationsId(id, (error, data, response) => {
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
 **id** | **Number**| As2 Station ID. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getAs2Stations

> [As2StationEntity] getAs2Stations(opts)

List As2 Stations

List As2 Stations

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.As2StationsApi();
let opts = {
  'cursor': "cursor_example", // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
  'perPage': 56 // Number | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
};
apiInstance.getAs2Stations(opts, (error, data, response) => {
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

[**[As2StationEntity]**](As2StationEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAs2StationsId

> As2StationEntity getAs2StationsId(id)

Show As2 Station

Show As2 Station

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.As2StationsApi();
let id = 56; // Number | As2 Station ID.
apiInstance.getAs2StationsId(id, (error, data, response) => {
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
 **id** | **Number**| As2 Station ID. | 

### Return type

[**As2StationEntity**](As2StationEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchAs2StationsId

> As2StationEntity patchAs2StationsId(id, opts)

Update As2 Station

Update As2 Station

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.As2StationsApi();
let id = 56; // Number | As2 Station ID.
let opts = {
  'name': "name_example", // String | AS2 Name
  'privateKey': "privateKey_example", // String | 
  'privateKeyPassword': "privateKeyPassword_example", // String | 
  'publicCertificate': "publicCertificate_example" // String | 
};
apiInstance.patchAs2StationsId(id, opts, (error, data, response) => {
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
 **id** | **Number**| As2 Station ID. | 
 **name** | **String**| AS2 Name | [optional] 
 **privateKey** | **String**|  | [optional] 
 **privateKeyPassword** | **String**|  | [optional] 
 **publicCertificate** | **String**|  | [optional] 

### Return type

[**As2StationEntity**](As2StationEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## postAs2Stations

> As2StationEntity postAs2Stations(name, privateKey, publicCertificate, opts)

Create As2 Station

Create As2 Station

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.As2StationsApi();
let name = "name_example"; // String | AS2 Name
let privateKey = "privateKey_example"; // String | 
let publicCertificate = "publicCertificate_example"; // String | 
let opts = {
  'privateKeyPassword': "privateKeyPassword_example" // String | 
};
apiInstance.postAs2Stations(name, privateKey, publicCertificate, opts, (error, data, response) => {
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
 **name** | **String**| AS2 Name | 
 **privateKey** | **String**|  | 
 **publicCertificate** | **String**|  | 
 **privateKeyPassword** | **String**|  | [optional] 

### Return type

[**As2StationEntity**](As2StationEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

