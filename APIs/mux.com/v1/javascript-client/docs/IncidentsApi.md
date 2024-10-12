# MuxApi.IncidentsApi

All URIs are relative to *https://api.mux.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getIncident**](IncidentsApi.md#getIncident) | **GET** /data/v1/incidents/{INCIDENT_ID} | Get an Incident
[**listIncidents**](IncidentsApi.md#listIncidents) | **GET** /data/v1/incidents | List Incidents
[**listRelatedIncidents**](IncidentsApi.md#listRelatedIncidents) | **GET** /data/v1/incidents/{INCIDENT_ID}/related | List Related Incidents



## getIncident

> IncidentResponse getIncident(INCIDENT_ID)

Get an Incident

Returns the details of an incident.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.IncidentsApi();
let INCIDENT_ID = "abcd1234"; // String | ID of the Incident
apiInstance.getIncident(INCIDENT_ID, (error, data, response) => {
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
 **INCIDENT_ID** | **String**| ID of the Incident | 

### Return type

[**IncidentResponse**](IncidentResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listIncidents

> ListIncidentsResponse listIncidents(opts)

List Incidents

Returns a list of incidents.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.IncidentsApi();
let opts = {
  'limit': 25, // Number | Number of items to include in the response
  'page': 1, // Number | Offset by this many pages, of the size of `limit`
  'orderBy': "orderBy_example", // String | Value to order the results by
  'orderDirection': "orderDirection_example", // String | Sort order.
  'status': "status_example", // String | Status to filter incidents by
  'severity': "severity_example" // String | Severity to filter incidents by
};
apiInstance.listIncidents(opts, (error, data, response) => {
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
 **limit** | **Number**| Number of items to include in the response | [optional] [default to 25]
 **page** | **Number**| Offset by this many pages, of the size of &#x60;limit&#x60; | [optional] [default to 1]
 **orderBy** | **String**| Value to order the results by | [optional] 
 **orderDirection** | **String**| Sort order. | [optional] 
 **status** | **String**| Status to filter incidents by | [optional] 
 **severity** | **String**| Severity to filter incidents by | [optional] 

### Return type

[**ListIncidentsResponse**](ListIncidentsResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listRelatedIncidents

> ListRelatedIncidentsResponse listRelatedIncidents(INCIDENT_ID, opts)

List Related Incidents

Returns all the incidents that seem related to a specific incident.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.IncidentsApi();
let INCIDENT_ID = "abcd1234"; // String | ID of the Incident
let opts = {
  'limit': 25, // Number | Number of items to include in the response
  'page': 1, // Number | Offset by this many pages, of the size of `limit`
  'orderBy': "orderBy_example", // String | Value to order the results by
  'orderDirection': "orderDirection_example" // String | Sort order.
};
apiInstance.listRelatedIncidents(INCIDENT_ID, opts, (error, data, response) => {
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
 **INCIDENT_ID** | **String**| ID of the Incident | 
 **limit** | **Number**| Number of items to include in the response | [optional] [default to 25]
 **page** | **Number**| Offset by this many pages, of the size of &#x60;limit&#x60; | [optional] [default to 1]
 **orderBy** | **String**| Value to order the results by | [optional] 
 **orderDirection** | **String**| Sort order. | [optional] 

### Return type

[**ListRelatedIncidentsResponse**](ListRelatedIncidentsResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

