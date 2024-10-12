# AlerterSystemApi.TeamInvitationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTeamInvitationGetCollection**](TeamInvitationApi.md#apiTeamInvitationGetCollection) | **GET** /api/team-invitation | Retrieves the collection of TeamInvitation resources.
[**apiTeamInvitationIdDelete**](TeamInvitationApi.md#apiTeamInvitationIdDelete) | **DELETE** /api/team-invitation/{id} | Removes the TeamInvitation resource.
[**apiTeamInvitationIdGet**](TeamInvitationApi.md#apiTeamInvitationIdGet) | **GET** /api/team-invitation/{id} | Retrieves a TeamInvitation resource.
[**apiTeamInvitationPost**](TeamInvitationApi.md#apiTeamInvitationPost) | **POST** /api/team-invitation | Creates a TeamInvitation resource.



## apiTeamInvitationGetCollection

> [TeamInvitationGet] apiTeamInvitationGetCollection(opts)

Retrieves the collection of TeamInvitation resources.

Retrieves the collection of TeamInvitation resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TeamInvitationApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'inviteeEmail': "inviteeEmail_example", // String | 
  'inviteeEmail2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTeamInvitationGetCollection(opts, (error, data, response) => {
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
 **page** | **Number**| The collection page number | [optional] [default to 1]
 **dataSegmentCode** | **String**|  | [optional] 
 **dataSegmentCode2** | [**[String]**](String.md)|  | [optional] 
 **partition** | **String**|  | [optional] 
 **partition2** | [**[String]**](String.md)|  | [optional] 
 **inviteeEmail** | **String**|  | [optional] 
 **inviteeEmail2** | [**[String]**](String.md)|  | [optional] 
 **properties** | [**[String]**](String.md)| Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]&#x3D;{propertyName}&amp;properties[]&#x3D;{anotherPropertyName}&amp;properties[{nestedPropertyParent}][]&#x3D;{nestedProperty} | [optional] 

### Return type

[**[TeamInvitationGet]**](TeamInvitationGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTeamInvitationIdDelete

> apiTeamInvitationIdDelete(id)

Removes the TeamInvitation resource.

Removes the TeamInvitation resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TeamInvitationApi();
let id = "id_example"; // String | TeamInvitation identifier
apiInstance.apiTeamInvitationIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TeamInvitation identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTeamInvitationIdGet

> TeamInvitationGet apiTeamInvitationIdGet(id)

Retrieves a TeamInvitation resource.

Retrieves a TeamInvitation resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TeamInvitationApi();
let id = "id_example"; // String | TeamInvitation identifier
apiInstance.apiTeamInvitationIdGet(id, (error, data, response) => {
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
 **id** | **String**| TeamInvitation identifier | 

### Return type

[**TeamInvitationGet**](TeamInvitationGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTeamInvitationPost

> TeamInvitationGet apiTeamInvitationPost(teamInvitationPost)

Creates a TeamInvitation resource.

Creates a TeamInvitation resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TeamInvitationApi();
let teamInvitationPost = new AlerterSystemApi.TeamInvitationPost(); // TeamInvitationPost | The new TeamInvitation resource
apiInstance.apiTeamInvitationPost(teamInvitationPost, (error, data, response) => {
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
 **teamInvitationPost** | [**TeamInvitationPost**](TeamInvitationPost.md)| The new TeamInvitation resource | 

### Return type

[**TeamInvitationGet**](TeamInvitationGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

