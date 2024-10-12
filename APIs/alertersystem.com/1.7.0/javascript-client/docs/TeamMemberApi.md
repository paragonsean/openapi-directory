# AlerterSystemApi.TeamMemberApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTeamMemberGetCollection**](TeamMemberApi.md#apiTeamMemberGetCollection) | **GET** /api/team-member | Retrieves the collection of TeamMember resources.
[**apiTeamMemberIdDelete**](TeamMemberApi.md#apiTeamMemberIdDelete) | **DELETE** /api/team-member/{id} | Removes the TeamMember resource.
[**apiTeamMemberIdGet**](TeamMemberApi.md#apiTeamMemberIdGet) | **GET** /api/team-member/{id} | Retrieves a TeamMember resource.
[**apiTeamMemberIdPatch**](TeamMemberApi.md#apiTeamMemberIdPatch) | **PATCH** /api/team-member/{id} | Updates the TeamMember resource.
[**apiTeamMemberIdPut**](TeamMemberApi.md#apiTeamMemberIdPut) | **PUT** /api/team-member/{id} | Replaces the TeamMember resource.



## apiTeamMemberGetCollection

> [TeamMemberGet] apiTeamMemberGetCollection(opts)

Retrieves the collection of TeamMember resources.

Retrieves the collection of TeamMember resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TeamMemberApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'userAccount': "userAccount_example", // String | 
  'userAccount2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTeamMemberGetCollection(opts, (error, data, response) => {
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
 **userAccount** | **String**|  | [optional] 
 **userAccount2** | [**[String]**](String.md)|  | [optional] 
 **properties** | [**[String]**](String.md)| Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]&#x3D;{propertyName}&amp;properties[]&#x3D;{anotherPropertyName}&amp;properties[{nestedPropertyParent}][]&#x3D;{nestedProperty} | [optional] 

### Return type

[**[TeamMemberGet]**](TeamMemberGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTeamMemberIdDelete

> apiTeamMemberIdDelete(id)

Removes the TeamMember resource.

Removes the TeamMember resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TeamMemberApi();
let id = "id_example"; // String | TeamMember identifier
apiInstance.apiTeamMemberIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TeamMember identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTeamMemberIdGet

> TeamMemberGet apiTeamMemberIdGet(id)

Retrieves a TeamMember resource.

Retrieves a TeamMember resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TeamMemberApi();
let id = "id_example"; // String | TeamMember identifier
apiInstance.apiTeamMemberIdGet(id, (error, data, response) => {
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
 **id** | **String**| TeamMember identifier | 

### Return type

[**TeamMemberGet**](TeamMemberGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTeamMemberIdPatch

> TeamMemberGet apiTeamMemberIdPatch(id, teamMemberPatch)

Updates the TeamMember resource.

Updates the TeamMember resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TeamMemberApi();
let id = "id_example"; // String | TeamMember identifier
let teamMemberPatch = new AlerterSystemApi.TeamMemberPatch(); // TeamMemberPatch | The updated TeamMember resource
apiInstance.apiTeamMemberIdPatch(id, teamMemberPatch, (error, data, response) => {
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
 **id** | **String**| TeamMember identifier | 
 **teamMemberPatch** | [**TeamMemberPatch**](TeamMemberPatch.md)| The updated TeamMember resource | 

### Return type

[**TeamMemberGet**](TeamMemberGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTeamMemberIdPut

> TeamMemberGet apiTeamMemberIdPut(id, teamMemberPut)

Replaces the TeamMember resource.

Replaces the TeamMember resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TeamMemberApi();
let id = "id_example"; // String | TeamMember identifier
let teamMemberPut = new AlerterSystemApi.TeamMemberPut(); // TeamMemberPut | The updated TeamMember resource
apiInstance.apiTeamMemberIdPut(id, teamMemberPut, (error, data, response) => {
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
 **id** | **String**| TeamMember identifier | 
 **teamMemberPut** | [**TeamMemberPut**](TeamMemberPut.md)| The updated TeamMember resource | 

### Return type

[**TeamMemberGet**](TeamMemberGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

