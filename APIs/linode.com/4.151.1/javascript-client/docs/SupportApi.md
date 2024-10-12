# LinodeApi.SupportApi

All URIs are relative to *https://api.linode.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**closeTicket**](SupportApi.md#closeTicket) | **POST** /support/tickets/{ticketId}/close | Support Ticket Close
[**createTicket**](SupportApi.md#createTicket) | **POST** /support/tickets | Support Ticket Open
[**createTicketAttachment**](SupportApi.md#createTicketAttachment) | **POST** /support/tickets/{ticketId}/attachments | Support Ticket Attachment Create
[**createTicketReply**](SupportApi.md#createTicketReply) | **POST** /support/tickets/{ticketId}/replies | Reply Create
[**getTicket**](SupportApi.md#getTicket) | **GET** /support/tickets/{ticketId} | Support Ticket View
[**getTicketReplies**](SupportApi.md#getTicketReplies) | **GET** /support/tickets/{ticketId}/replies | Replies List
[**getTickets**](SupportApi.md#getTickets) | **GET** /support/tickets | Support Tickets List



## closeTicket

> Object closeTicket(ticketId)

Support Ticket Close

Closes a Support Ticket you have access to modify. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.SupportApi();
let ticketId = 56; // Number | The ID of the Support Ticket.
apiInstance.closeTicket(ticketId, (error, data, response) => {
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
 **ticketId** | **Number**| The ID of the Support Ticket. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createTicket

> SupportTicket createTicket(opts)

Support Ticket Open

Open a Support Ticket. Only one of the ID attributes (&#x60;linode_id&#x60;, &#x60;domain_id&#x60;, etc.) can be set on a single Support Ticket. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.SupportApi();
let opts = {
  'supportTicketRequest': new LinodeApi.SupportTicketRequest() // SupportTicketRequest | Open a Support Ticket.
};
apiInstance.createTicket(opts, (error, data, response) => {
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
 **supportTicketRequest** | [**SupportTicketRequest**](SupportTicketRequest.md)| Open a Support Ticket. | [optional] 

### Return type

[**SupportTicket**](SupportTicket.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createTicketAttachment

> Object createTicketAttachment(ticketId, file)

Support Ticket Attachment Create

Adds a file attachment to an existing Support Ticket on your Account. File attachments are used to assist our Support team in resolving your Ticket. Examples of attachments are screen shots and text files that provide additional information.  The file attachment is submitted in the request as multipart/form-data.  **Note**: Accepted file extensions include: .gif, .jpg, .jpeg, .pjpg, .pjpeg, .tif, .tiff, .png, .pdf, or .txt. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.SupportApi();
let ticketId = 56; // Number | The ID of the Support Ticket.
let file = "file_example"; // String | The local, absolute path to the file you want to attach to your Support Ticket. 
apiInstance.createTicketAttachment(ticketId, file, (error, data, response) => {
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
 **ticketId** | **Number**| The ID of the Support Ticket. | 
 **file** | **String**| The local, absolute path to the file you want to attach to your Support Ticket.  | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## createTicketReply

> SupportTicketReply createTicketReply(ticketId, createTicketReplyRequest)

Reply Create

Adds a reply to an existing Support Ticket. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.SupportApi();
let ticketId = 56; // Number | The ID of the Support Ticket.
let createTicketReplyRequest = new LinodeApi.CreateTicketReplyRequest(); // CreateTicketReplyRequest | Add a reply.
apiInstance.createTicketReply(ticketId, createTicketReplyRequest, (error, data, response) => {
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
 **ticketId** | **Number**| The ID of the Support Ticket. | 
 **createTicketReplyRequest** | [**CreateTicketReplyRequest**](CreateTicketReplyRequest.md)| Add a reply. | 

### Return type

[**SupportTicketReply**](SupportTicketReply.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getTicket

> SupportTicket getTicket(ticketId)

Support Ticket View

Returns a Support Ticket under your Account. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.SupportApi();
let ticketId = 56; // Number | The ID of the Support Ticket.
apiInstance.getTicket(ticketId, (error, data, response) => {
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
 **ticketId** | **Number**| The ID of the Support Ticket. | 

### Return type

[**SupportTicket**](SupportTicket.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTicketReplies

> GetTicketReplies200Response getTicketReplies(ticketId, opts)

Replies List

Returns a collection of replies to a Support Ticket on your Account. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.SupportApi();
let ticketId = 56; // Number | The ID of the Support Ticket.
let opts = {
  'page': 1, // Number | The page of a collection to return.
  'pageSize': 100 // Number | The number of items to return per page.
};
apiInstance.getTicketReplies(ticketId, opts, (error, data, response) => {
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
 **ticketId** | **Number**| The ID of the Support Ticket. | 
 **page** | **Number**| The page of a collection to return. | [optional] [default to 1]
 **pageSize** | **Number**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetTicketReplies200Response**](GetTicketReplies200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTickets

> GetTickets200Response getTickets(opts)

Support Tickets List

Returns a collection of Support Tickets on your Account. Support Tickets can be both tickets you open with Linode for support, as well as tickets generated by Linode regarding your Account. This collection includes all Support Tickets generated on your Account, with open tickets returned first. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.SupportApi();
let opts = {
  'page': 1, // Number | The page of a collection to return.
  'pageSize': 100 // Number | The number of items to return per page.
};
apiInstance.getTickets(opts, (error, data, response) => {
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
 **page** | **Number**| The page of a collection to return. | [optional] [default to 1]
 **pageSize** | **Number**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetTickets200Response**](GetTickets200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

