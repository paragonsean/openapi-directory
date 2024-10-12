# AlerterSystemApi.TeamMemberRoleCodeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTeamMemberRoleCodeGetCollection**](TeamMemberRoleCodeApi.md#apiTeamMemberRoleCodeGetCollection) | **GET** /api/team-member-role-code | Retrieves the collection of TeamMemberRoleCode resources.
[**apiTeamMemberRoleCodeIdGet**](TeamMemberRoleCodeApi.md#apiTeamMemberRoleCodeIdGet) | **GET** /api/team-member-role-code/{id} | Retrieves a TeamMemberRoleCode resource.



## apiTeamMemberRoleCodeGetCollection

> [TeamMemberRoleCodeGet] apiTeamMemberRoleCodeGetCollection(opts)

Retrieves the collection of TeamMemberRoleCode resources.

Retrieves the collection of TeamMemberRoleCode resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TeamMemberRoleCodeApi();
let opts = {
  'page': 1, // Number | The collection page number
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTeamMemberRoleCodeGetCollection(opts, (error, data, response) => {
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
 **properties** | [**[String]**](String.md)| Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]&#x3D;{propertyName}&amp;properties[]&#x3D;{anotherPropertyName}&amp;properties[{nestedPropertyParent}][]&#x3D;{nestedProperty} | [optional] 

### Return type

[**[TeamMemberRoleCodeGet]**](TeamMemberRoleCodeGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTeamMemberRoleCodeIdGet

> TeamMemberRoleCodeGet apiTeamMemberRoleCodeIdGet(id)

Retrieves a TeamMemberRoleCode resource.

Retrieves a TeamMemberRoleCode resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TeamMemberRoleCodeApi();
let id = "id_example"; // String | TeamMemberRoleCode identifier
apiInstance.apiTeamMemberRoleCodeIdGet(id, (error, data, response) => {
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
 **id** | **String**| TeamMemberRoleCode identifier | 

### Return type

[**TeamMemberRoleCodeGet**](TeamMemberRoleCodeGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html

