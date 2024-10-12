# OpenapiJsClient.V1Api

All URIs are relative to *http://api.ote-godaddy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createTicket**](V1Api.md#createTicket) | **POST** /v1/abuse/tickets | Create a new abuse ticket
[**getTicketInfo**](V1Api.md#getTicketInfo) | **GET** /v1/abuse/tickets/{ticketId} | Return the abuse ticket data for a given ticket id
[**getTickets**](V1Api.md#getTickets) | **GET** /v1/abuse/tickets | List all abuse tickets ids that match user provided filters



## createTicket

> createTicket(abuseTicketCreate)

Create a new abuse ticket

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';

let apiInstance = new OpenapiJsClient.V1Api();
let abuseTicketCreate = new OpenapiJsClient.AbuseTicketCreate(); // AbuseTicketCreate | The endpoint which allows the Reporter to create a new abuse ticket
apiInstance.createTicket(abuseTicketCreate, (error, data, response) => {
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
 **abuseTicketCreate** | [**AbuseTicketCreate**](AbuseTicketCreate.md)| The endpoint which allows the Reporter to create a new abuse ticket | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## getTicketInfo

> AbuseTicket getTicketInfo(ticketId)

Return the abuse ticket data for a given ticket id

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';

let apiInstance = new OpenapiJsClient.V1Api();
let ticketId = "ticketId_example"; // String | A unique abuse ticket identifier
apiInstance.getTicketInfo(ticketId, (error, data, response) => {
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
 **ticketId** | **String**| A unique abuse ticket identifier | 

### Return type

[**AbuseTicket**](AbuseTicket.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getTickets

> AbuseTicketList getTickets(opts)

List all abuse tickets ids that match user provided filters

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';

let apiInstance = new OpenapiJsClient.V1Api();
let opts = {
  'type': "type_example", // String | The type of abuse.
  'closed': false, // Boolean | Is this abuse ticket closed?
  'sourceDomainOrIp': "sourceDomainOrIp_example", // String | The domain name or ip address the abuse originated from
  'target': "target_example", // String | The brand/company the abuse is targeting. ie: brand name/bank name
  'createdStart': "createdStart_example", // String | The earliest abuse ticket creation date to pull abuse tickets for
  'createdEnd': "createdEnd_example", // String | The latest abuse ticket creation date to pull abuse tickets for
  'limit': 100, // Number | Number of abuse ticket numbers to return.
  'offset': 0 // Number | The earliest result set record number to pull abuse tickets for
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
 **type** | **String**| The type of abuse. | [optional] 
 **closed** | **Boolean**| Is this abuse ticket closed? | [optional] [default to false]
 **sourceDomainOrIp** | **String**| The domain name or ip address the abuse originated from | [optional] 
 **target** | **String**| The brand/company the abuse is targeting. ie: brand name/bank name | [optional] 
 **createdStart** | **String**| The earliest abuse ticket creation date to pull abuse tickets for | [optional] 
 **createdEnd** | **String**| The latest abuse ticket creation date to pull abuse tickets for | [optional] 
 **limit** | **Number**| Number of abuse ticket numbers to return. | [optional] [default to 100]
 **offset** | **Number**| The earliest result set record number to pull abuse tickets for | [optional] [default to 0]

### Return type

[**AbuseTicketList**](AbuseTicketList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

