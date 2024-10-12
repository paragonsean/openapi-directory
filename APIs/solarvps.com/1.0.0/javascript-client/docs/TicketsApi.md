# SolarVps.TicketsApi

All URIs are relative to *http://api.ss.solarvps.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ticketsDepartmentAddPost**](TicketsApi.md#ticketsDepartmentAddPost) | **POST** /tickets/{department}/add | Open ticket with desired department
[**ticketsGet**](TicketsApi.md#ticketsGet) | **GET** /tickets | View all your tickets
[**ticketsTicketIdGet**](TicketsApi.md#ticketsTicketIdGet) | **GET** /tickets/{ticketId} | View details on a specific ticket
[**ticketsTicketidUpdatePost**](TicketsApi.md#ticketsTicketidUpdatePost) | **POST** /tickets/{ticketid}/update | Post a reply to a ticket



## ticketsDepartmentAddPost

> ticketsDepartmentAddPost(department, subject, contents)

Open ticket with desired department

Available departments are support, billing, sales

### Example

```javascript
import SolarVps from 'solar_vps';
let defaultClient = SolarVps.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new SolarVps.TicketsApi();
let department = "department_example"; // String | Department you want to open a ticket with
let subject = "subject_example"; // String | Subject of the ticket you are opening
let contents = "contents_example"; // String | Message reply being sent
apiInstance.ticketsDepartmentAddPost(department, subject, contents, (error, data, response) => {
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
 **department** | **String**| Department you want to open a ticket with | 
 **subject** | **String**| Subject of the ticket you are opening | 
 **contents** | **String**| Message reply being sent | 

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## ticketsGet

> ticketsGet()

View all your tickets

Shows all your tickets

### Example

```javascript
import SolarVps from 'solar_vps';
let defaultClient = SolarVps.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new SolarVps.TicketsApi();
apiInstance.ticketsGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## ticketsTicketIdGet

> ticketsTicketIdGet(ticketId)

View details on a specific ticket

Shows all information of a specific ticketId

### Example

```javascript
import SolarVps from 'solar_vps';
let defaultClient = SolarVps.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new SolarVps.TicketsApi();
let ticketId = 3.4; // Number | TicketId you want to see
apiInstance.ticketsTicketIdGet(ticketId, (error, data, response) => {
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
 **ticketId** | **Number**| TicketId you want to see | 

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## ticketsTicketidUpdatePost

> ticketsTicketidUpdatePost(ticketid, contents)

Post a reply to a ticket

### Example

```javascript
import SolarVps from 'solar_vps';
let defaultClient = SolarVps.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new SolarVps.TicketsApi();
let ticketid = 3.4; // Number | TicketId of the ticket you want to post an update to
let contents = "contents_example"; // String | Message reply being sent
apiInstance.ticketsTicketidUpdatePost(ticketid, contents, (error, data, response) => {
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
 **ticketid** | **Number**| TicketId of the ticket you want to post an update to | 
 **contents** | **String**| Message reply being sent | 

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

