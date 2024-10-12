# SliceboxApi.TransactionsApi

All URIs are relative to *http://slicebox.local/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transactionsTokenImagePost**](TransactionsApi.md#transactionsTokenImagePost) | **POST** /transactions/{token}/image | 
[**transactionsTokenOutgoingDonePost**](TransactionsApi.md#transactionsTokenOutgoingDonePost) | **POST** /transactions/{token}/outgoing/done | 
[**transactionsTokenOutgoingFailedPost**](TransactionsApi.md#transactionsTokenOutgoingFailedPost) | **POST** /transactions/{token}/outgoing/failed | 
[**transactionsTokenOutgoingGet**](TransactionsApi.md#transactionsTokenOutgoingGet) | **GET** /transactions/{token}/outgoing | 
[**transactionsTokenOutgoingPollGet**](TransactionsApi.md#transactionsTokenOutgoingPollGet) | **GET** /transactions/{token}/outgoing/poll | 
[**transactionsTokenStatusGet**](TransactionsApi.md#transactionsTokenStatusGet) | **GET** /transactions/{token}/status | 
[**transactionsTokenStatusPut**](TransactionsApi.md#transactionsTokenStatusPut) | **PUT** /transactions/{token}/status | 



## transactionsTokenImagePost

> transactionsTokenImagePost(token, transactionid, sequencenumber, totalimagecount, dataset)



add an image (dataset) as part of a transaction. This method is used when sending images using the push method to a public slicebox.

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.TransactionsApi();
let token = "token_example"; // String | authentication token identifying the current box-to-box connection
let transactionid = 789; // Number | the ID of the client's outgoing transaction
let sequencenumber = 789; // Number | the index of this image in the transaction
let totalimagecount = 789; // Number | the total number of images in this transaction
let dataset = {key: null}; // Object | the dataset byte array
apiInstance.transactionsTokenImagePost(token, transactionid, sequencenumber, totalimagecount, dataset, (error, data, response) => {
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
 **token** | **String**| authentication token identifying the current box-to-box connection | 
 **transactionid** | **Number**| the ID of the client&#39;s outgoing transaction | 
 **sequencenumber** | **Number**| the index of this image in the transaction | 
 **totalimagecount** | **Number**| the total number of images in this transaction | 
 **dataset** | **Object**| the dataset byte array | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/octet-stream
- **Accept**: Not defined


## transactionsTokenOutgoingDonePost

> transactionsTokenOutgoingDonePost(token, outgoingEntryAndImageInformationBlock)



signal that the supplied outgoing transaction and image was successfully received and can be marked as sent. This method is used when sending images using the poll method from a public slicebox.

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.TransactionsApi();
let token = "token_example"; // String | authentication token identifying the current box-to-box connection
let outgoingEntryAndImageInformationBlock = new SliceboxApi.OutgoingTransactionImage(); // OutgoingTransactionImage | outgoing transaction and image that has been successfully received
apiInstance.transactionsTokenOutgoingDonePost(token, outgoingEntryAndImageInformationBlock, (error, data, response) => {
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
 **token** | **String**| authentication token identifying the current box-to-box connection | 
 **outgoingEntryAndImageInformationBlock** | [**OutgoingTransactionImage**](OutgoingTransactionImage.md)| outgoing transaction and image that has been successfully received | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/octet-stream, multipart/form-data
- **Accept**: Not defined


## transactionsTokenOutgoingFailedPost

> transactionsTokenOutgoingFailedPost(token, outgoingTransactionAndImageAndErrorMessage)



signal that the image corresponding to the supplied outgoing transaction and image could not be read or stored properly on the receiving side, and that the transaction should be marked as failed.

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.TransactionsApi();
let token = "token_example"; // String | authentication token identifying the current box-to-box connection
let outgoingTransactionAndImageAndErrorMessage = new SliceboxApi.FailedOutgoingTransactionImage(); // FailedOutgoingTransactionImage | the outgoing transaction and image information block corresponding to the failed image transfer, along with the associated error message
apiInstance.transactionsTokenOutgoingFailedPost(token, outgoingTransactionAndImageAndErrorMessage, (error, data, response) => {
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
 **token** | **String**| authentication token identifying the current box-to-box connection | 
 **outgoingTransactionAndImageAndErrorMessage** | [**FailedOutgoingTransactionImage**](FailedOutgoingTransactionImage.md)| the outgoing transaction and image information block corresponding to the failed image transfer, along with the associated error message | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/octet-stream, multipart/form-data
- **Accept**: Not defined


## transactionsTokenOutgoingGet

> transactionsTokenOutgoingGet(token, transactionid, imageid)



fetch an image from the connected box as part of a transaction. This method is used when sending images using the poll method from a public slicebox.

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.TransactionsApi();
let token = "token_example"; // String | authentication token identifying the current box-to-box connection
let transactionid = 789; // Number | the ID of the outgoing transaction
let imageid = 789; // Number | the ID of the outgoing transaction image
apiInstance.transactionsTokenOutgoingGet(token, transactionid, imageid, (error, data, response) => {
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
 **token** | **String**| authentication token identifying the current box-to-box connection | 
 **transactionid** | **Number**| the ID of the outgoing transaction | 
 **imageid** | **Number**| the ID of the outgoing transaction image | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## transactionsTokenOutgoingPollGet

> [OutgoingTransactionImage] transactionsTokenOutgoingPollGet(token)



get next outgoing transaction and image (information on the next image that the connected box wishes to send to you), if any. This method is used when sending images using the poll method from a public slicebox.

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.TransactionsApi();
let token = "token_example"; // String | authentication token identifying the current box-to-box connection
apiInstance.transactionsTokenOutgoingPollGet(token, (error, data, response) => {
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
 **token** | **String**| authentication token identifying the current box-to-box connection | 

### Return type

[**[OutgoingTransactionImage]**](OutgoingTransactionImage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/octet-stream


## transactionsTokenStatusGet

> transactionsTokenStatusGet(token, transactionid)



get the status of the remote incoming transaction with the supplied transaction ID

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.TransactionsApi();
let token = "token_example"; // String | authentication token identifying the current box-to-box connection
let transactionid = 789; // Number | the ID of the client's outgoing transaction
apiInstance.transactionsTokenStatusGet(token, transactionid, (error, data, response) => {
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
 **token** | **String**| authentication token identifying the current box-to-box connection | 
 **transactionid** | **Number**| the ID of the client&#39;s outgoing transaction | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## transactionsTokenStatusPut

> transactionsTokenStatusPut(token, transactionid, transactionStatus)



update the status of the transaction with the supplied ID

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.TransactionsApi();
let token = "token_example"; // String | authentication token identifying the current box-to-box connection
let transactionid = 789; // Number | the ID of the client's outgoing transaction
let transactionStatus = "transactionStatus_example"; // String | the updated status of the transaction
apiInstance.transactionsTokenStatusPut(token, transactionid, transactionStatus, (error, data, response) => {
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
 **token** | **String**| authentication token identifying the current box-to-box connection | 
 **transactionid** | **Number**| the ID of the client&#39;s outgoing transaction | 
 **transactionStatus** | **String**| the updated status of the transaction | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/octet-stream, multipart/form-data
- **Accept**: Not defined

