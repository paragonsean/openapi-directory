# BrandLoversMarketplaceApiV1.TicketsApi

All URIs are relative to *https://api.brandlovers.com/marketplace/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ticketPost**](TicketsApi.md#ticketPost) | **POST** /ticket | Creates a new trouble ticket
[**ticketTicketIdMessagePost**](TicketsApi.md#ticketTicketIdMessagePost) | **POST** /ticket/{ticketId}/message | Add new message to trouble ticket
[**ticketTicketIdMessagesGet**](TicketsApi.md#ticketTicketIdMessagesGet) | **GET** /ticket/{ticketId}/messages | Get trouble ticket messages
[**ticketTicketIdStatusPut**](TicketsApi.md#ticketTicketIdStatusPut) | **PUT** /ticket/{ticketId}/status | Update trouble ticket status
[**ticketsGet**](TicketsApi.md#ticketsGet) | **GET** /tickets | Get customers trouble tickets



## ticketPost

> ticketPost(authorization, newTicket)

Creates a new trouble ticket

Use this service to create a new trouble ticket. Use this to include relevant information about the order, comunicate with the customer or marketplace team. Whenever possible message will be pushed to Mobile first. This is the primary mean of comunicaiton with the customer regarding orders, shippments, shippments status. New tickets will be automatically be set to &#39;OPEN&#39;. Trouble tickets need to be associated with a orderId or customer. New tickets can optionally include a new message.

### Example

```javascript
import BrandLoversMarketplaceApiV1 from 'brand_lovers_marketplace_api_v1';

let apiInstance = new BrandLoversMarketplaceApiV1.TicketsApi();
let authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
let newTicket = new BrandLoversMarketplaceApiV1.NewTicket(); // NewTicket | JSON object with new trouble ticket
apiInstance.ticketPost(authorization, newTicket, (error, data, response) => {
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
 **authorization** | **String**| Authorization token. The Authorization token can be found in your Admin console. | 
 **newTicket** | [**NewTicket**](NewTicket.md)| JSON object with new trouble ticket | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## ticketTicketIdMessagePost

> ticketTicketIdMessagePost(authorization, ticketId, message)

Add new message to trouble ticket

Add a new message to this trouble ticket. Messages can be &#x60;CUSTOMER&#x60; (customer will be able to see it) or &#x60;INTERNAL&#x60;.

### Example

```javascript
import BrandLoversMarketplaceApiV1 from 'brand_lovers_marketplace_api_v1';

let apiInstance = new BrandLoversMarketplaceApiV1.TicketsApi();
let authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
let ticketId = "ticketId_example"; // String | Trouble ticket ID.
let message = new BrandLoversMarketplaceApiV1.NewTicketMessage(); // NewTicketMessage | New message object to append to trouble ticket.
apiInstance.ticketTicketIdMessagePost(authorization, ticketId, message, (error, data, response) => {
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
 **authorization** | **String**| Authorization token. The Authorization token can be found in your Admin console. | 
 **ticketId** | **String**| Trouble ticket ID. | 
 **message** | [**NewTicketMessage**](NewTicketMessage.md)| New message object to append to trouble ticket. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## ticketTicketIdMessagesGet

> GetTicketMessages ticketTicketIdMessagesGet(authorization, ticketId, opts)

Get trouble ticket messages

Returns trouble ticket history with all messages exchanged. Only tickets related to your seller will be returned. Attempt to read other tickets will return 403 (acess denied).

### Example

```javascript
import BrandLoversMarketplaceApiV1 from 'brand_lovers_marketplace_api_v1';

let apiInstance = new BrandLoversMarketplaceApiV1.TicketsApi();
let authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
let ticketId = "ticketId_example"; // String | Trouble ticket ID.
let opts = {
  'offset': 56, // Number | Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with `limit` to paginate across the results.
  'limit': 56 // Number | Number or items to return when executing query. Defaults to 10. Use this conjuction with `offset` to paginate across the results.
};
apiInstance.ticketTicketIdMessagesGet(authorization, ticketId, opts, (error, data, response) => {
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
 **authorization** | **String**| Authorization token. The Authorization token can be found in your Admin console. | 
 **ticketId** | **String**| Trouble ticket ID. | 
 **offset** | **Number**| Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with &#x60;limit&#x60; to paginate across the results. | [optional] 
 **limit** | **Number**| Number or items to return when executing query. Defaults to 10. Use this conjuction with &#x60;offset&#x60; to paginate across the results. | [optional] 

### Return type

[**GetTicketMessages**](GetTicketMessages.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ticketTicketIdStatusPut

> ticketTicketIdStatusPut(authorization, ticketId, body)

Update trouble ticket status

Alows the seller to update the status of a trouble ticket

### Example

```javascript
import BrandLoversMarketplaceApiV1 from 'brand_lovers_marketplace_api_v1';

let apiInstance = new BrandLoversMarketplaceApiV1.TicketsApi();
let authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
let ticketId = "ticketId_example"; // String | Trouble ticket unique identification
let body = new BrandLoversMarketplaceApiV1.TicketStatus(); // TicketStatus | New trouble ticket status
apiInstance.ticketTicketIdStatusPut(authorization, ticketId, body, (error, data, response) => {
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
 **authorization** | **String**| Authorization token. The Authorization token can be found in your Admin console. | 
 **ticketId** | **String**| Trouble ticket unique identification | 
 **body** | [**TicketStatus**](TicketStatus.md)| New trouble ticket status | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## ticketsGet

> GetTickets ticketsGet(authorization, opts)

Get customers trouble tickets

Allows seller to receive and status, queries, requests and complaints from customers. As well related messages

### Example

```javascript
import BrandLoversMarketplaceApiV1 from 'brand_lovers_marketplace_api_v1';

let apiInstance = new BrandLoversMarketplaceApiV1.TicketsApi();
let authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
let opts = {
  'status': "status_example", // String | Query by trouble ticket status
  'offset': 56, // Number | Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with `limit` to paginate across the results.
  'limit': 56 // Number | Number or items to return when executing query. Defaults to 10. Use this conjuction with `offset` to paginate across the results.
};
apiInstance.ticketsGet(authorization, opts, (error, data, response) => {
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
 **authorization** | **String**| Authorization token. The Authorization token can be found in your Admin console. | 
 **status** | **String**| Query by trouble ticket status | [optional] 
 **offset** | **Number**| Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with &#x60;limit&#x60; to paginate across the results. | [optional] 
 **limit** | **Number**| Number or items to return when executing query. Defaults to 10. Use this conjuction with &#x60;offset&#x60; to paginate across the results. | [optional] 

### Return type

[**GetTickets**](GetTickets.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

