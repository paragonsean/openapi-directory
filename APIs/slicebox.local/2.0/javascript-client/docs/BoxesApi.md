# SliceboxApi.BoxesApi

All URIs are relative to *http://slicebox.local/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**boxesConnectPost**](BoxesApi.md#boxesConnectPost) | **POST** /boxes/connect | 
[**boxesCreateconnectionPost**](BoxesApi.md#boxesCreateconnectionPost) | **POST** /boxes/createconnection | 
[**boxesGet**](BoxesApi.md#boxesGet) | **GET** /boxes | 
[**boxesIdDelete**](BoxesApi.md#boxesIdDelete) | **DELETE** /boxes/{id} | 
[**boxesIdSendPost**](BoxesApi.md#boxesIdSendPost) | **POST** /boxes/{id}/send | 
[**boxesIncomingGet**](BoxesApi.md#boxesIncomingGet) | **GET** /boxes/incoming | 
[**boxesIncomingIdDelete**](BoxesApi.md#boxesIncomingIdDelete) | **DELETE** /boxes/incoming/{id} | 
[**boxesIncomingIdImagesGet**](BoxesApi.md#boxesIncomingIdImagesGet) | **GET** /boxes/incoming/{id}/images | 
[**boxesOutgoingGet**](BoxesApi.md#boxesOutgoingGet) | **GET** /boxes/outgoing | 
[**boxesOutgoingIdDelete**](BoxesApi.md#boxesOutgoingIdDelete) | **DELETE** /boxes/outgoing/{id} | 
[**boxesOutgoingIdImagesGet**](BoxesApi.md#boxesOutgoingIdImagesGet) | **GET** /boxes/outgoing/{id}/images | 



## boxesConnectPost

> Box boxesConnectPost(remoteBox)



connect to another box using a received URL. Used to connect to a public box.

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.BoxesApi();
let remoteBox = new SliceboxApi.RemoteBox(); // RemoteBox | remote box to connect with
apiInstance.boxesConnectPost(remoteBox, (error, data, response) => {
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
 **remoteBox** | [**RemoteBox**](RemoteBox.md)| remote box to connect with | 

### Return type

[**Box**](Box.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/octet-stream, multipart/form-data
- **Accept**: application/json, application/octet-stream


## boxesCreateconnectionPost

> Box boxesCreateconnectionPost(remoteBoxConnectionData)



create a new box connection where the supplied entity holds the remote box name. Used by publicly available boxes.

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.BoxesApi();
let remoteBoxConnectionData = new SliceboxApi.RemoteBoxConnectionData(); // RemoteBoxConnectionData | name of box to connect (and send URL) to
apiInstance.boxesCreateconnectionPost(remoteBoxConnectionData, (error, data, response) => {
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
 **remoteBoxConnectionData** | [**RemoteBoxConnectionData**](RemoteBoxConnectionData.md)| name of box to connect (and send URL) to | 

### Return type

[**Box**](Box.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/octet-stream, multipart/form-data
- **Accept**: application/json, application/octet-stream


## boxesGet

> [Box] boxesGet(opts)



get a list of box connections

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.BoxesApi();
let opts = {
  'startindex': 0, // Number | start index of returned slice of boxes
  'count': 20 // Number | size of returned slice of boxes
};
apiInstance.boxesGet(opts, (error, data, response) => {
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
 **startindex** | **Number**| start index of returned slice of boxes | [optional] [default to 0]
 **count** | **Number**| size of returned slice of boxes | [optional] [default to 20]

### Return type

[**[Box]**](Box.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/octet-stream


## boxesIdDelete

> boxesIdDelete(id)



Delete the remote box with the supplied ID

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.BoxesApi();
let id = 789; // Number | ID of box to remove
apiInstance.boxesIdDelete(id, (error, data, response) => {
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
 **id** | **Number**| ID of box to remove | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## boxesIdSendPost

> boxesIdSendPost(id, sequenceOfImageTagValues)



send images corresponding to the supplied image ids to the remote box with the supplied ID

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.BoxesApi();
let id = 789; // Number | ID of box to send images to
let sequenceOfImageTagValues = new SliceboxApi.BulkAnonymizationData(); // BulkAnonymizationData | specification of which images to send and list of DICOM attribute values to use in anonymized datasets
apiInstance.boxesIdSendPost(id, sequenceOfImageTagValues, (error, data, response) => {
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
 **id** | **Number**| ID of box to send images to | 
 **sequenceOfImageTagValues** | [**BulkAnonymizationData**](BulkAnonymizationData.md)| specification of which images to send and list of DICOM attribute values to use in anonymized datasets | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/octet-stream, multipart/form-data
- **Accept**: Not defined


## boxesIncomingGet

> [IncomingTransaction] boxesIncomingGet(opts)



get incoming transactions (finished, currently receiving, waiting or failed)

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.BoxesApi();
let opts = {
  'startindex': 0, // Number | start index of returned slice of transactions
  'count': 20 // Number | size of returned slice of transactions
};
apiInstance.boxesIncomingGet(opts, (error, data, response) => {
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
 **startindex** | **Number**| start index of returned slice of transactions | [optional] [default to 0]
 **count** | **Number**| size of returned slice of transactions | [optional] [default to 20]

### Return type

[**[IncomingTransaction]**](IncomingTransaction.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/octet-stream


## boxesIncomingIdDelete

> boxesIncomingIdDelete(id)



delete an incoming transaction. If a currently active transaction is deleted, a new transaction with the remainder of the images is created when receiving the next incoming image.

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.BoxesApi();
let id = 789; // Number | ID of incoming transaction
apiInstance.boxesIncomingIdDelete(id, (error, data, response) => {
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
 **id** | **Number**| ID of incoming transaction | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## boxesIncomingIdImagesGet

> [Image] boxesIncomingIdImagesGet(id)



get the received images corresponding to the incoming transaction with the supplied ID

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.BoxesApi();
let id = 789; // Number | ID of incoming transaction
apiInstance.boxesIncomingIdImagesGet(id, (error, data, response) => {
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
 **id** | **Number**| ID of incoming transaction | 

### Return type

[**[Image]**](Image.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/octet-stream


## boxesOutgoingGet

> [OutgoingTransaction] boxesOutgoingGet(opts)



get outgoing transactions (finished, currently sending, waiting or failed)

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.BoxesApi();
let opts = {
  'startindex': 0, // Number | start index of returned slice of transactions
  'count': 20 // Number | size of returned slice of transactions
};
apiInstance.boxesOutgoingGet(opts, (error, data, response) => {
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
 **startindex** | **Number**| start index of returned slice of transactions | [optional] [default to 0]
 **count** | **Number**| size of returned slice of transactions | [optional] [default to 20]

### Return type

[**[OutgoingTransaction]**](OutgoingTransaction.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/octet-stream


## boxesOutgoingIdDelete

> boxesOutgoingIdDelete(id)



delete an outgoing transaction. This will stop ongoing transactions.

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.BoxesApi();
let id = 789; // Number | ID of outgoing transaction
apiInstance.boxesOutgoingIdDelete(id, (error, data, response) => {
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
 **id** | **Number**| ID of outgoing transaction | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## boxesOutgoingIdImagesGet

> [Image] boxesOutgoingIdImagesGet(id)



get the sent images corresponding to the outgoing transaction with the supplied ID

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.BoxesApi();
let id = 789; // Number | ID of outgoing transaction
apiInstance.boxesOutgoingIdImagesGet(id, (error, data, response) => {
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
 **id** | **Number**| ID of outgoing transaction | 

### Return type

[**[Image]**](Image.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/octet-stream

