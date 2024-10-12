# UebermapsApiEndpoints.AttachmentsApi

All URIs are relative to *http://uebermaps.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attachmentsIdDelete**](AttachmentsApi.md#attachmentsIdDelete) | **DELETE** /attachments/{id} | Delete attachment
[**mapsIdAttachmentsGet**](AttachmentsApi.md#mapsIdAttachmentsGet) | **GET** /maps/{id}/attachments | List attachments for a given map
[**mapsIdAttachmentsPost**](AttachmentsApi.md#mapsIdAttachmentsPost) | **POST** /maps/{id}/attachments | Upload map attachment
[**spotsIdAttachmentsGet**](AttachmentsApi.md#spotsIdAttachmentsGet) | **GET** /spots/{id}/attachments | List attachments for a given spot
[**spotsIdAttachmentsPost**](AttachmentsApi.md#spotsIdAttachmentsPost) | **POST** /spots/{id}/attachments | Upload spot attachment



## attachmentsIdDelete

> Attachment attachmentsIdDelete(id)

Delete attachment

Delete attachment.

### Example

```javascript
import UebermapsApiEndpoints from 'uebermaps_api_endpoints';

let apiInstance = new UebermapsApiEndpoints.AttachmentsApi();
let id = 56; // Number | Attachment id
apiInstance.attachmentsIdDelete(id, (error, data, response) => {
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
 **id** | **Number**| Attachment id | 

### Return type

[**Attachment**](Attachment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mapsIdAttachmentsGet

> [Attachment] mapsIdAttachmentsGet(id)

List attachments for a given map

List attachments for a given map.

### Example

```javascript
import UebermapsApiEndpoints from 'uebermaps_api_endpoints';

let apiInstance = new UebermapsApiEndpoints.AttachmentsApi();
let id = 56; // Number | Map id
apiInstance.mapsIdAttachmentsGet(id, (error, data, response) => {
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
 **id** | **Number**| Map id | 

### Return type

[**[Attachment]**](Attachment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mapsIdAttachmentsPost

> Attachment mapsIdAttachmentsPost(id, image)

Upload map attachment

Upload map attachment. Wrap attachment parameters in [attachment]

### Example

```javascript
import UebermapsApiEndpoints from 'uebermaps_api_endpoints';

let apiInstance = new UebermapsApiEndpoints.AttachmentsApi();
let id = 56; // Number | Map id
let image = "image_example"; // String | Base64 encoded image
apiInstance.mapsIdAttachmentsPost(id, image, (error, data, response) => {
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
 **id** | **Number**| Map id | 
 **image** | **String**| Base64 encoded image | 

### Return type

[**Attachment**](Attachment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## spotsIdAttachmentsGet

> [Attachment] spotsIdAttachmentsGet(id)

List attachments for a given spot

List attachments for a given spot.

### Example

```javascript
import UebermapsApiEndpoints from 'uebermaps_api_endpoints';

let apiInstance = new UebermapsApiEndpoints.AttachmentsApi();
let id = 56; // Number | Spot id
apiInstance.spotsIdAttachmentsGet(id, (error, data, response) => {
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
 **id** | **Number**| Spot id | 

### Return type

[**[Attachment]**](Attachment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## spotsIdAttachmentsPost

> Attachment spotsIdAttachmentsPost(id, image)

Upload spot attachment

Upload spot attachment. Wrap attachment parameters in [attachment]

### Example

```javascript
import UebermapsApiEndpoints from 'uebermaps_api_endpoints';

let apiInstance = new UebermapsApiEndpoints.AttachmentsApi();
let id = 56; // Number | Spot id
let image = "image_example"; // String | Base64 encoded image
apiInstance.spotsIdAttachmentsPost(id, image, (error, data, response) => {
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
 **id** | **Number**| Spot id | 
 **image** | **String**| Base64 encoded image | 

### Return type

[**Attachment**](Attachment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

