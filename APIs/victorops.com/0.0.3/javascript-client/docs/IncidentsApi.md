# VictorOps.IncidentsApi

All URIs are relative to *https://api.victorops.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiPublicV1IncidentsAckPatch**](IncidentsApi.md#apiPublicV1IncidentsAckPatch) | **PATCH** /api-public/v1/incidents/ack | Acknowledge an incident or list of incidents
[**apiPublicV1IncidentsByUserAckPatch**](IncidentsApi.md#apiPublicV1IncidentsByUserAckPatch) | **PATCH** /api-public/v1/incidents/byUser/ack | Acknowledge all incidents for which a user was paged.
[**apiPublicV1IncidentsByUserResolvePatch**](IncidentsApi.md#apiPublicV1IncidentsByUserResolvePatch) | **PATCH** /api-public/v1/incidents/byUser/resolve | Resolve all incidents for which a user was paged.
[**apiPublicV1IncidentsGet**](IncidentsApi.md#apiPublicV1IncidentsGet) | **GET** /api-public/v1/incidents | Get current incident information
[**apiPublicV1IncidentsPost**](IncidentsApi.md#apiPublicV1IncidentsPost) | **POST** /api-public/v1/incidents | Create a new incident
[**apiPublicV1IncidentsReroutePost**](IncidentsApi.md#apiPublicV1IncidentsReroutePost) | **POST** /api-public/v1/incidents/reroute | Reroute one or more incidents to one or more new routable destinations.
[**apiPublicV1IncidentsResolvePatch**](IncidentsApi.md#apiPublicV1IncidentsResolvePatch) | **PATCH** /api-public/v1/incidents/resolve | Resolve an incident or list of incidents



## apiPublicV1IncidentsAckPatch

> AckOrResolveResponse apiPublicV1IncidentsAckPatch(xVOApiId, xVOApiKey, body)

Acknowledge an incident or list of incidents

The incident(s) must be currently open.  The user supplied must be a valid VictorOps user and a member of your organization.  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.IncidentsApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
let body = new VictorOps.AckOrResolveRequest(); // AckOrResolveRequest | Ack/Resolve payload
apiInstance.apiPublicV1IncidentsAckPatch(xVOApiId, xVOApiKey, body, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 
 **body** | [**AckOrResolveRequest**](AckOrResolveRequest.md)| Ack/Resolve payload | 

### Return type

[**AckOrResolveResponse**](AckOrResolveResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiPublicV1IncidentsByUserAckPatch

> AckOrResolveResponse apiPublicV1IncidentsByUserAckPatch(xVOApiId, xVOApiKey, body)

Acknowledge all incidents for which a user was paged.

The incident(s) must be currently open.  The user supplied must be a valid VictorOps user and a member of your organization.  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.IncidentsApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
let body = new VictorOps.AckOrResolveByUserRequest(); // AckOrResolveByUserRequest | Ack/Resolve payload
apiInstance.apiPublicV1IncidentsByUserAckPatch(xVOApiId, xVOApiKey, body, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 
 **body** | [**AckOrResolveByUserRequest**](AckOrResolveByUserRequest.md)| Ack/Resolve payload | 

### Return type

[**AckOrResolveResponse**](AckOrResolveResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiPublicV1IncidentsByUserResolvePatch

> AckOrResolveResponse apiPublicV1IncidentsByUserResolvePatch(xVOApiId, xVOApiKey, body)

Resolve all incidents for which a user was paged.

The incident(s) must be currently open.  The user supplied must be a valid VictorOps user and a member of your organization.  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.IncidentsApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
let body = new VictorOps.AckOrResolveByUserRequest(); // AckOrResolveByUserRequest | Ack/Resolve payload
apiInstance.apiPublicV1IncidentsByUserResolvePatch(xVOApiId, xVOApiKey, body, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 
 **body** | [**AckOrResolveByUserRequest**](AckOrResolveByUserRequest.md)| Ack/Resolve payload | 

### Return type

[**AckOrResolveResponse**](AckOrResolveResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiPublicV1IncidentsGet

> ActiveIncidentList apiPublicV1IncidentsGet(xVOApiId, xVOApiKey)

Get current incident information

Get a list of the currently open, acknowledged and recently resolved incidents.  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.IncidentsApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
apiInstance.apiPublicV1IncidentsGet(xVOApiId, xVOApiKey, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 

### Return type

[**ActiveIncidentList**](ActiveIncidentList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiPublicV1IncidentsPost

> CreatedIncident apiPublicV1IncidentsPost(xVOApiId, xVOApiKey, body)

Create a new incident

Create a new incident.  This call replicates the function of our &lt;a href&#x3D;\&quot;https://help.victorops.com/knowledge-base/manual-incident-creation/\&quot;&gt;manual incident creation process&lt;/a&gt;. Monitoring tools and custom integrations should be configured using our &lt;a href&#x3D;\&quot;https://help.victorops.com/knowledge-base/victorops-restendpoint-integration/\&quot;&gt;REST Endpoint&lt;/a&gt;.  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.IncidentsApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
let body = new VictorOps.CreateIncidentRequest(); // CreateIncidentRequest | The incident details
apiInstance.apiPublicV1IncidentsPost(xVOApiId, xVOApiKey, body, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 
 **body** | [**CreateIncidentRequest**](CreateIncidentRequest.md)| The incident details | 

### Return type

[**CreatedIncident**](CreatedIncident.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiPublicV1IncidentsReroutePost

> RerouteStatusResponse apiPublicV1IncidentsReroutePost(xVOApiId, xVOApiKey, body)

Reroute one or more incidents to one or more new routable destinations.

Reroute one or more incidents to one or more users and/or escalation policies  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.IncidentsApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
let body = new VictorOps.RerouteCollection(); // RerouteCollection | The reroute rules
apiInstance.apiPublicV1IncidentsReroutePost(xVOApiId, xVOApiKey, body, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 
 **body** | [**RerouteCollection**](RerouteCollection.md)| The reroute rules | 

### Return type

[**RerouteStatusResponse**](RerouteStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiPublicV1IncidentsResolvePatch

> AckOrResolveResponse apiPublicV1IncidentsResolvePatch(xVOApiId, xVOApiKey, body)

Resolve an incident or list of incidents

The incident(s) must be currently open.  The user supplied must be a valid VictorOps user and a member of your organization.  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.IncidentsApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
let body = new VictorOps.AckOrResolveRequest(); // AckOrResolveRequest | Ack/Resolve payload
apiInstance.apiPublicV1IncidentsResolvePatch(xVOApiId, xVOApiKey, body, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 
 **body** | [**AckOrResolveRequest**](AckOrResolveRequest.md)| Ack/Resolve payload | 

### Return type

[**AckOrResolveResponse**](AckOrResolveResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

