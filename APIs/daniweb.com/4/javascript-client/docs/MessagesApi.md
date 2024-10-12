# DaniWebConnectApi.MessagesApi

All URIs are relative to *https://www.daniweb.com/connect/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**messagesIDGet**](MessagesApi.md#messagesIDGet) | **GET** /messages/{ID} | 
[**messagesIDMetadataCollectionsGet**](MessagesApi.md#messagesIDMetadataCollectionsGet) | **GET** /messages/{ID}/metadata/collections | 
[**messagesIDMetadataGet**](MessagesApi.md#messagesIDMetadataGet) | **GET** /messages/{ID}/metadata | 
[**messagesIDMetadataPost**](MessagesApi.md#messagesIDMetadataPost) | **POST** /messages/{ID}/metadata | 
[**messagesMetadataFiltersPost**](MessagesApi.md#messagesMetadataFiltersPost) | **POST** /messages/metadata/filters | 



## messagesIDGet

> EndpointGetMessagesID messagesIDGet(ID)



Fetch an array of messages. You can only retrieve messages authored by you or by users who exist within the current access token&#39;s bubble.

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.MessagesApi();
let ID = [null]; // [Number] | 
apiInstance.messagesIDGet(ID, (error, data, response) => {
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
 **ID** | [**[Number]**](Number.md)|  | 

### Return type

[**EndpointGetMessagesID**](EndpointGetMessagesID.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## messagesIDMetadataCollectionsGet

> EndpointGetMessagesIDMetadataCollections messagesIDMetadataCollectionsGet(ID)



Retrieve all key/value pairs attached to the current message that you have access to, so long as the user who authored the message exists within the current access token&#39;s bubble. This includes all public metadata, bubbled metadata that was created by an access token existing within the current bubble, user metadata that was created by you, or private metadata created by you from an access token existing within the current bubble. Metadata will be grouped by key.

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.MessagesApi();
let ID = 56; // Number | 
apiInstance.messagesIDMetadataCollectionsGet(ID, (error, data, response) => {
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
 **ID** | **Number**|  | 

### Return type

[**EndpointGetMessagesIDMetadataCollections**](EndpointGetMessagesIDMetadataCollections.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## messagesIDMetadataGet

> EndpointGetMessagesIDMetadata messagesIDMetadataGet(ID, opts)



Retrieve all key/value pairs attached to the current message that you have access to, so long as the user who authored the message exists within the current access token&#39;s bubble. This includes all public metadata, bubbled metadata that was created by an access token existing within the current bubble, user metadata that was created by you, or private metadata created by you from an access token existing within the current bubble.

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.MessagesApi();
let ID = 56; // Number | 
let opts = {
  'offset': 0, // Number | 
  'limit': 50 // Number | 
};
apiInstance.messagesIDMetadataGet(ID, opts, (error, data, response) => {
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
 **ID** | **Number**|  | 
 **offset** | **Number**|  | [optional] [default to 0]
 **limit** | **Number**|  | [optional] [default to 50]

### Return type

[**EndpointGetMessagesIDMetadata**](EndpointGetMessagesIDMetadata.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## messagesIDMetadataPost

> EndpointPostMessagesIDMetadata messagesIDMetadataPost(ID, opts)



Attach one-to-many key/value pairs of metadata to a message, so long as the user who authored the message exists within the current access token&#39;s bubble. A key is unique for each author/bubble combination. Attaching metadata with an existing key that was previously created by you, from within the same bubble, overwrites the key with the new value or set of values. The privacy setting allows you to specify who will have access to the metadata: Public metadata by you or the other user in the message&#39;s conversation, using an access token which grants you access to the user who authored the message, if it wasn&#39;t you; Bubbled metadata by you or the other user in the message&#39;s conversation, using an access token existing within the current bubble; User metadata by you, so long as you are using an access token which grants you access to the user who authored the message, if it wasn&#39;t you; Private metadata by you, so long as you are using an access token existing within the current bubble.

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.MessagesApi();
let ID = 56; // Number | 
let opts = {
  'metadata0Key': "metadata0Key_example", // String | 
  'metadata0Privacy': "metadata0Privacy_example", // String | 
  'metadata0Values': ["null"], // [String] | 
  'metadata1Key': "metadata1Key_example", // String | 
  'metadata1Privacy': "metadata1Privacy_example", // String | 
  'metadata1Values': ["null"], // [String] | 
  'metadata2Key': "metadata2Key_example", // String | 
  'metadata2Privacy': "metadata2Privacy_example", // String | 
  'metadata2Values': ["null"] // [String] | 
};
apiInstance.messagesIDMetadataPost(ID, opts, (error, data, response) => {
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
 **ID** | **Number**|  | 
 **metadata0Key** | **String**|  | [optional] 
 **metadata0Privacy** | **String**|  | [optional] 
 **metadata0Values** | [**[String]**](String.md)|  | [optional] 
 **metadata1Key** | **String**|  | [optional] 
 **metadata1Privacy** | **String**|  | [optional] 
 **metadata1Values** | [**[String]**](String.md)|  | [optional] 
 **metadata2Key** | **String**|  | [optional] 
 **metadata2Privacy** | **String**|  | [optional] 
 **metadata2Values** | [**[String]**](String.md)|  | [optional] 

### Return type

[**EndpointPostMessagesIDMetadata**](EndpointPostMessagesIDMetadata.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## messagesMetadataFiltersPost

> EndpointPostMessagesMetadataFilters messagesMetadataFiltersPost(opts)



Paginated listing of messages filtered by arbitrary metadata criteria. Messages must match on all key/value pairs passed in. Messages may only match on one value of an array passed in. However, messages are sorted based on how many distinct values they match on (most matches first).

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.MessagesApi();
let opts = {
  'limit': 50, // Number | 
  'metadata0Key': "metadata0Key_example", // String | 
  'metadata0Values': ["null"], // [String] | 
  'metadata1Key': "metadata1Key_example", // String | 
  'metadata1Values': ["null"], // [String] | 
  'metadata2Key': "metadata2Key_example", // String | 
  'metadata2Values': ["null"], // [String] | 
  'offset': 0 // Number | 
};
apiInstance.messagesMetadataFiltersPost(opts, (error, data, response) => {
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
 **limit** | **Number**|  | [optional] [default to 50]
 **metadata0Key** | **String**|  | [optional] 
 **metadata0Values** | [**[String]**](String.md)|  | [optional] 
 **metadata1Key** | **String**|  | [optional] 
 **metadata1Values** | [**[String]**](String.md)|  | [optional] 
 **metadata2Key** | **String**|  | [optional] 
 **metadata2Values** | [**[String]**](String.md)|  | [optional] 
 **offset** | **Number**|  | [optional] [default to 0]

### Return type

[**EndpointPostMessagesMetadataFilters**](EndpointPostMessagesMetadataFilters.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

