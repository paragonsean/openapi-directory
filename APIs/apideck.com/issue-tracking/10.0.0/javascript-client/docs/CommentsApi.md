# IssueTrackingApi.CommentsApi

All URIs are relative to *https://unify.apideck.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**collectionTicketCommentsAdd**](CommentsApi.md#collectionTicketCommentsAdd) | **POST** /issue-tracking/collections/{collection_id}/tickets/{ticket_id}/comments | Create Comment
[**collectionTicketCommentsAll**](CommentsApi.md#collectionTicketCommentsAll) | **GET** /issue-tracking/collections/{collection_id}/tickets/{ticket_id}/comments | List Comments
[**collectionTicketCommentsDelete**](CommentsApi.md#collectionTicketCommentsDelete) | **DELETE** /issue-tracking/collections/{collection_id}/tickets/{ticket_id}/comments/{id} | Delete Comment
[**collectionTicketCommentsOne**](CommentsApi.md#collectionTicketCommentsOne) | **GET** /issue-tracking/collections/{collection_id}/tickets/{ticket_id}/comments/{id} | Get Comment
[**collectionTicketCommentsUpdate**](CommentsApi.md#collectionTicketCommentsUpdate) | **PATCH** /issue-tracking/collections/{collection_id}/tickets/{ticket_id}/comments/{id} | Update Comment



## collectionTicketCommentsAdd

> CreateCommentResponse collectionTicketCommentsAdd(xApideckConsumerId, xApideckAppId, collectionId, ticketId, collectionTicketComment, opts)

Create Comment

Create Comment

### Example

```javascript
import IssueTrackingApi from 'issue_tracking_api';
let defaultClient = IssueTrackingApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new IssueTrackingApi.CommentsApi();
let xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
let xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
let collectionId = "apideck-io"; // String | The collection ID
let ticketId = "ticketId_example"; // String | ID of the ticket you are acting upon.
let collectionTicketComment = new IssueTrackingApi.CollectionTicketComment(); // CollectionTicketComment | 
let opts = {
  'raw': false, // Boolean | Include raw response. Mostly used for debugging purposes
  'xApideckServiceId': "xApideckServiceId_example" // String | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
};
apiInstance.collectionTicketCommentsAdd(xApideckConsumerId, xApideckAppId, collectionId, ticketId, collectionTicketComment, opts, (error, data, response) => {
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
 **xApideckConsumerId** | **String**| ID of the consumer which you want to get or push data from | 
 **xApideckAppId** | **String**| The ID of your Unify application | 
 **collectionId** | **String**| The collection ID | 
 **ticketId** | **String**| ID of the ticket you are acting upon. | 
 **collectionTicketComment** | [**CollectionTicketComment**](CollectionTicketComment.md)|  | 
 **raw** | **Boolean**| Include raw response. Mostly used for debugging purposes | [optional] [default to false]
 **xApideckServiceId** | **String**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional] 

### Return type

[**CreateCommentResponse**](CreateCommentResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## collectionTicketCommentsAll

> GetCommentsResponse collectionTicketCommentsAll(xApideckConsumerId, xApideckAppId, collectionId, ticketId, opts)

List Comments

List Comments

### Example

```javascript
import IssueTrackingApi from 'issue_tracking_api';
let defaultClient = IssueTrackingApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new IssueTrackingApi.CommentsApi();
let xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
let xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
let collectionId = "apideck-io"; // String | The collection ID
let ticketId = "ticketId_example"; // String | ID of the ticket you are acting upon.
let opts = {
  'raw': false, // Boolean | Include raw response. Mostly used for debugging purposes
  'xApideckServiceId': "xApideckServiceId_example", // String | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
  'cursor': "cursor_example", // String | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
  'limit': 20, // Number | Number of results to return. Minimum 1, Maximum 200, Default 20
  'sort': new IssueTrackingApi.CommentsSort(), // CommentsSort | Apply sorting
  'passThrough': {key: {"search":"San Francisco"}}, // PassThroughQuery | Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]=leads becomes ?search=leads
  'fields': "id,updated_at" // String | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded.
};
apiInstance.collectionTicketCommentsAll(xApideckConsumerId, xApideckAppId, collectionId, ticketId, opts, (error, data, response) => {
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
 **xApideckConsumerId** | **String**| ID of the consumer which you want to get or push data from | 
 **xApideckAppId** | **String**| The ID of your Unify application | 
 **collectionId** | **String**| The collection ID | 
 **ticketId** | **String**| ID of the ticket you are acting upon. | 
 **raw** | **Boolean**| Include raw response. Mostly used for debugging purposes | [optional] [default to false]
 **xApideckServiceId** | **String**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional] 
 **cursor** | **String**| Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. | [optional] 
 **limit** | **Number**| Number of results to return. Minimum 1, Maximum 200, Default 20 | [optional] [default to 20]
 **sort** | [**CommentsSort**](.md)| Apply sorting | [optional] 
 **passThrough** | [**PassThroughQuery**](Object.md)| Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]&#x3D;leads becomes ?search&#x3D;leads | [optional] 
 **fields** | **String**| The &#39;fields&#39; parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. &lt;br /&gt;&lt;br /&gt;Example: &#x60;fields&#x3D;name,email,addresses.city&#x60;&lt;br /&gt;&lt;br /&gt;In the example above, the response will only include the fields \&quot;name\&quot;, \&quot;email\&quot; and \&quot;addresses.city\&quot;. If any other fields are available, they will be excluded. | [optional] 

### Return type

[**GetCommentsResponse**](GetCommentsResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## collectionTicketCommentsDelete

> DeleteCommentResponse collectionTicketCommentsDelete(id, xApideckConsumerId, xApideckAppId, collectionId, ticketId, opts)

Delete Comment

Delete Comment

### Example

```javascript
import IssueTrackingApi from 'issue_tracking_api';
let defaultClient = IssueTrackingApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new IssueTrackingApi.CommentsApi();
let id = "id_example"; // String | ID of the record you are acting upon.
let xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
let xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
let collectionId = "apideck-io"; // String | The collection ID
let ticketId = "ticketId_example"; // String | ID of the ticket you are acting upon.
let opts = {
  'xApideckServiceId': "xApideckServiceId_example", // String | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
  'raw': false // Boolean | Include raw response. Mostly used for debugging purposes
};
apiInstance.collectionTicketCommentsDelete(id, xApideckConsumerId, xApideckAppId, collectionId, ticketId, opts, (error, data, response) => {
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
 **id** | **String**| ID of the record you are acting upon. | 
 **xApideckConsumerId** | **String**| ID of the consumer which you want to get or push data from | 
 **xApideckAppId** | **String**| The ID of your Unify application | 
 **collectionId** | **String**| The collection ID | 
 **ticketId** | **String**| ID of the ticket you are acting upon. | 
 **xApideckServiceId** | **String**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional] 
 **raw** | **Boolean**| Include raw response. Mostly used for debugging purposes | [optional] [default to false]

### Return type

[**DeleteCommentResponse**](DeleteCommentResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## collectionTicketCommentsOne

> GetCommentResponse collectionTicketCommentsOne(id, xApideckConsumerId, xApideckAppId, collectionId, ticketId, opts)

Get Comment

Get Comment

### Example

```javascript
import IssueTrackingApi from 'issue_tracking_api';
let defaultClient = IssueTrackingApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new IssueTrackingApi.CommentsApi();
let id = "id_example"; // String | ID of the record you are acting upon.
let xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
let xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
let collectionId = "apideck-io"; // String | The collection ID
let ticketId = "ticketId_example"; // String | ID of the ticket you are acting upon.
let opts = {
  'raw': false, // Boolean | Include raw response. Mostly used for debugging purposes
  'xApideckServiceId': "xApideckServiceId_example", // String | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
  'cursor': "cursor_example", // String | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
  'limit': 20, // Number | Number of results to return. Minimum 1, Maximum 200, Default 20
  'fields': "id,updated_at" // String | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded.
};
apiInstance.collectionTicketCommentsOne(id, xApideckConsumerId, xApideckAppId, collectionId, ticketId, opts, (error, data, response) => {
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
 **id** | **String**| ID of the record you are acting upon. | 
 **xApideckConsumerId** | **String**| ID of the consumer which you want to get or push data from | 
 **xApideckAppId** | **String**| The ID of your Unify application | 
 **collectionId** | **String**| The collection ID | 
 **ticketId** | **String**| ID of the ticket you are acting upon. | 
 **raw** | **Boolean**| Include raw response. Mostly used for debugging purposes | [optional] [default to false]
 **xApideckServiceId** | **String**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional] 
 **cursor** | **String**| Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. | [optional] 
 **limit** | **Number**| Number of results to return. Minimum 1, Maximum 200, Default 20 | [optional] [default to 20]
 **fields** | **String**| The &#39;fields&#39; parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. &lt;br /&gt;&lt;br /&gt;Example: &#x60;fields&#x3D;name,email,addresses.city&#x60;&lt;br /&gt;&lt;br /&gt;In the example above, the response will only include the fields \&quot;name\&quot;, \&quot;email\&quot; and \&quot;addresses.city\&quot;. If any other fields are available, they will be excluded. | [optional] 

### Return type

[**GetCommentResponse**](GetCommentResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## collectionTicketCommentsUpdate

> UpdateCommentResponse collectionTicketCommentsUpdate(id, xApideckConsumerId, xApideckAppId, collectionId, ticketId, collectionTicketComment, opts)

Update Comment

Update Comment

### Example

```javascript
import IssueTrackingApi from 'issue_tracking_api';
let defaultClient = IssueTrackingApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new IssueTrackingApi.CommentsApi();
let id = "id_example"; // String | ID of the record you are acting upon.
let xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
let xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
let collectionId = "apideck-io"; // String | The collection ID
let ticketId = "ticketId_example"; // String | ID of the ticket you are acting upon.
let collectionTicketComment = new IssueTrackingApi.CollectionTicketComment(); // CollectionTicketComment | 
let opts = {
  'xApideckServiceId': "xApideckServiceId_example", // String | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
  'raw': false // Boolean | Include raw response. Mostly used for debugging purposes
};
apiInstance.collectionTicketCommentsUpdate(id, xApideckConsumerId, xApideckAppId, collectionId, ticketId, collectionTicketComment, opts, (error, data, response) => {
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
 **id** | **String**| ID of the record you are acting upon. | 
 **xApideckConsumerId** | **String**| ID of the consumer which you want to get or push data from | 
 **xApideckAppId** | **String**| The ID of your Unify application | 
 **collectionId** | **String**| The collection ID | 
 **ticketId** | **String**| ID of the ticket you are acting upon. | 
 **collectionTicketComment** | [**CollectionTicketComment**](CollectionTicketComment.md)|  | 
 **xApideckServiceId** | **String**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional] 
 **raw** | **Boolean**| Include raw response. Mostly used for debugging purposes | [optional] [default to false]

### Return type

[**UpdateCommentResponse**](UpdateCommentResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

