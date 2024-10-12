# IssueTrackingApi.TicketsApi

All URIs are relative to *https://unify.apideck.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**collectionTicketsAdd**](TicketsApi.md#collectionTicketsAdd) | **POST** /issue-tracking/collections/{collection_id}/tickets | Create Ticket
[**collectionTicketsAll**](TicketsApi.md#collectionTicketsAll) | **GET** /issue-tracking/collections/{collection_id}/tickets | List Tickets
[**collectionTicketsDelete**](TicketsApi.md#collectionTicketsDelete) | **DELETE** /issue-tracking/collections/{collection_id}/tickets/{ticket_id} | Delete Ticket
[**collectionTicketsOne**](TicketsApi.md#collectionTicketsOne) | **GET** /issue-tracking/collections/{collection_id}/tickets/{ticket_id} | Get Ticket
[**collectionTicketsUpdate**](TicketsApi.md#collectionTicketsUpdate) | **PATCH** /issue-tracking/collections/{collection_id}/tickets/{ticket_id} | Update Ticket



## collectionTicketsAdd

> CreateTicketResponse collectionTicketsAdd(xApideckConsumerId, xApideckAppId, collectionId, ticket, opts)

Create Ticket

Create Ticket

### Example

```javascript
import IssueTrackingApi from 'issue_tracking_api';
let defaultClient = IssueTrackingApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new IssueTrackingApi.TicketsApi();
let xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
let xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
let collectionId = "apideck-io"; // String | The collection ID
let ticket = new IssueTrackingApi.Ticket(); // Ticket | 
let opts = {
  'raw': false, // Boolean | Include raw response. Mostly used for debugging purposes
  'xApideckServiceId': "xApideckServiceId_example" // String | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
};
apiInstance.collectionTicketsAdd(xApideckConsumerId, xApideckAppId, collectionId, ticket, opts, (error, data, response) => {
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
 **ticket** | [**Ticket**](Ticket.md)|  | 
 **raw** | **Boolean**| Include raw response. Mostly used for debugging purposes | [optional] [default to false]
 **xApideckServiceId** | **String**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional] 

### Return type

[**CreateTicketResponse**](CreateTicketResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## collectionTicketsAll

> GetTicketsResponse collectionTicketsAll(xApideckConsumerId, xApideckAppId, collectionId, opts)

List Tickets

List Tickets

### Example

```javascript
import IssueTrackingApi from 'issue_tracking_api';
let defaultClient = IssueTrackingApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new IssueTrackingApi.TicketsApi();
let xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
let xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
let collectionId = "apideck-io"; // String | The collection ID
let opts = {
  'raw': false, // Boolean | Include raw response. Mostly used for debugging purposes
  'xApideckServiceId': "xApideckServiceId_example", // String | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
  'cursor': "cursor_example", // String | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
  'limit': 20, // Number | Number of results to return. Minimum 1, Maximum 200, Default 20
  'sort': new IssueTrackingApi.TicketsSort(), // TicketsSort | Apply sorting
  'filter': new IssueTrackingApi.IssuesFilter(), // IssuesFilter | Apply filters
  'passThrough': {key: {"search":"San Francisco"}}, // PassThroughQuery | Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]=leads becomes ?search=leads
  'fields': "id,updated_at" // String | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded.
};
apiInstance.collectionTicketsAll(xApideckConsumerId, xApideckAppId, collectionId, opts, (error, data, response) => {
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
 **raw** | **Boolean**| Include raw response. Mostly used for debugging purposes | [optional] [default to false]
 **xApideckServiceId** | **String**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional] 
 **cursor** | **String**| Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. | [optional] 
 **limit** | **Number**| Number of results to return. Minimum 1, Maximum 200, Default 20 | [optional] [default to 20]
 **sort** | [**TicketsSort**](.md)| Apply sorting | [optional] 
 **filter** | [**IssuesFilter**](.md)| Apply filters | [optional] 
 **passThrough** | [**PassThroughQuery**](Object.md)| Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]&#x3D;leads becomes ?search&#x3D;leads | [optional] 
 **fields** | **String**| The &#39;fields&#39; parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. &lt;br /&gt;&lt;br /&gt;Example: &#x60;fields&#x3D;name,email,addresses.city&#x60;&lt;br /&gt;&lt;br /&gt;In the example above, the response will only include the fields \&quot;name\&quot;, \&quot;email\&quot; and \&quot;addresses.city\&quot;. If any other fields are available, they will be excluded. | [optional] 

### Return type

[**GetTicketsResponse**](GetTicketsResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## collectionTicketsDelete

> DeleteTicketResponse collectionTicketsDelete(ticketId, xApideckConsumerId, xApideckAppId, collectionId, opts)

Delete Ticket

Delete Ticket

### Example

```javascript
import IssueTrackingApi from 'issue_tracking_api';
let defaultClient = IssueTrackingApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new IssueTrackingApi.TicketsApi();
let ticketId = "ticketId_example"; // String | ID of the ticket you are acting upon.
let xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
let xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
let collectionId = "apideck-io"; // String | The collection ID
let opts = {
  'xApideckServiceId': "xApideckServiceId_example", // String | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
  'raw': false // Boolean | Include raw response. Mostly used for debugging purposes
};
apiInstance.collectionTicketsDelete(ticketId, xApideckConsumerId, xApideckAppId, collectionId, opts, (error, data, response) => {
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
 **ticketId** | **String**| ID of the ticket you are acting upon. | 
 **xApideckConsumerId** | **String**| ID of the consumer which you want to get or push data from | 
 **xApideckAppId** | **String**| The ID of your Unify application | 
 **collectionId** | **String**| The collection ID | 
 **xApideckServiceId** | **String**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional] 
 **raw** | **Boolean**| Include raw response. Mostly used for debugging purposes | [optional] [default to false]

### Return type

[**DeleteTicketResponse**](DeleteTicketResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## collectionTicketsOne

> GetTicketResponse collectionTicketsOne(ticketId, xApideckConsumerId, xApideckAppId, collectionId, opts)

Get Ticket

Get Ticket

### Example

```javascript
import IssueTrackingApi from 'issue_tracking_api';
let defaultClient = IssueTrackingApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new IssueTrackingApi.TicketsApi();
let ticketId = "ticketId_example"; // String | ID of the ticket you are acting upon.
let xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
let xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
let collectionId = "apideck-io"; // String | The collection ID
let opts = {
  'xApideckServiceId': "xApideckServiceId_example", // String | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
  'raw': false, // Boolean | Include raw response. Mostly used for debugging purposes
  'fields': "id,updated_at" // String | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded.
};
apiInstance.collectionTicketsOne(ticketId, xApideckConsumerId, xApideckAppId, collectionId, opts, (error, data, response) => {
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
 **ticketId** | **String**| ID of the ticket you are acting upon. | 
 **xApideckConsumerId** | **String**| ID of the consumer which you want to get or push data from | 
 **xApideckAppId** | **String**| The ID of your Unify application | 
 **collectionId** | **String**| The collection ID | 
 **xApideckServiceId** | **String**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional] 
 **raw** | **Boolean**| Include raw response. Mostly used for debugging purposes | [optional] [default to false]
 **fields** | **String**| The &#39;fields&#39; parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. &lt;br /&gt;&lt;br /&gt;Example: &#x60;fields&#x3D;name,email,addresses.city&#x60;&lt;br /&gt;&lt;br /&gt;In the example above, the response will only include the fields \&quot;name\&quot;, \&quot;email\&quot; and \&quot;addresses.city\&quot;. If any other fields are available, they will be excluded. | [optional] 

### Return type

[**GetTicketResponse**](GetTicketResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## collectionTicketsUpdate

> UpdateTicketResponse collectionTicketsUpdate(ticketId, xApideckConsumerId, xApideckAppId, collectionId, ticket, opts)

Update Ticket

Update Ticket

### Example

```javascript
import IssueTrackingApi from 'issue_tracking_api';
let defaultClient = IssueTrackingApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new IssueTrackingApi.TicketsApi();
let ticketId = "ticketId_example"; // String | ID of the ticket you are acting upon.
let xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
let xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
let collectionId = "apideck-io"; // String | The collection ID
let ticket = new IssueTrackingApi.Ticket(); // Ticket | 
let opts = {
  'xApideckServiceId': "xApideckServiceId_example", // String | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
  'raw': false // Boolean | Include raw response. Mostly used for debugging purposes
};
apiInstance.collectionTicketsUpdate(ticketId, xApideckConsumerId, xApideckAppId, collectionId, ticket, opts, (error, data, response) => {
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
 **ticketId** | **String**| ID of the ticket you are acting upon. | 
 **xApideckConsumerId** | **String**| ID of the consumer which you want to get or push data from | 
 **xApideckAppId** | **String**| The ID of your Unify application | 
 **collectionId** | **String**| The collection ID | 
 **ticket** | [**Ticket**](Ticket.md)|  | 
 **xApideckServiceId** | **String**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional] 
 **raw** | **Boolean**| Include raw response. Mostly used for debugging purposes | [optional] [default to false]

### Return type

[**UpdateTicketResponse**](UpdateTicketResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

