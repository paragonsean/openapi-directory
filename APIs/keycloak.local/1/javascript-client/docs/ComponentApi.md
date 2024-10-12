# KeycloakAdminRestApi.ComponentApi

All URIs are relative to *http://keycloak.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**realmComponentsGet**](ComponentApi.md#realmComponentsGet) | **GET** /{realm}/components | 
[**realmComponentsIdDelete**](ComponentApi.md#realmComponentsIdDelete) | **DELETE** /{realm}/components/{id} | 
[**realmComponentsIdGet**](ComponentApi.md#realmComponentsIdGet) | **GET** /{realm}/components/{id} | 
[**realmComponentsIdPut**](ComponentApi.md#realmComponentsIdPut) | **PUT** /{realm}/components/{id} | 
[**realmComponentsIdSubComponentTypesGet**](ComponentApi.md#realmComponentsIdSubComponentTypesGet) | **GET** /{realm}/components/{id}/sub-component-types | List of subcomponent types that are available to configure for a particular parent component.
[**realmComponentsPost**](ComponentApi.md#realmComponentsPost) | **POST** /{realm}/components | 



## realmComponentsGet

> [ComponentRepresentation] realmComponentsGet(realm, opts)



### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ComponentApi();
let realm = "realm_example"; // String | realm name (not id!)
let opts = {
  'name': "name_example", // String | 
  'parent': "parent_example", // String | 
  'type': "type_example" // String | 
};
apiInstance.realmComponentsGet(realm, opts, (error, data, response) => {
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
 **realm** | **String**| realm name (not id!) | 
 **name** | **String**|  | [optional] 
 **parent** | **String**|  | [optional] 
 **type** | **String**|  | [optional] 

### Return type

[**[ComponentRepresentation]**](ComponentRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmComponentsIdDelete

> realmComponentsIdDelete(realm, id)



### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ComponentApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | 
apiInstance.realmComponentsIdDelete(realm, id, (error, data, response) => {
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
 **realm** | **String**| realm name (not id!) | 
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realmComponentsIdGet

> ComponentRepresentation realmComponentsIdGet(realm, id)



### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ComponentApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | 
apiInstance.realmComponentsIdGet(realm, id, (error, data, response) => {
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
 **realm** | **String**| realm name (not id!) | 
 **id** | **String**|  | 

### Return type

[**ComponentRepresentation**](ComponentRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmComponentsIdPut

> realmComponentsIdPut(realm, id, componentRepresentation)



### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ComponentApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | 
let componentRepresentation = new KeycloakAdminRestApi.ComponentRepresentation(); // ComponentRepresentation | 
apiInstance.realmComponentsIdPut(realm, id, componentRepresentation, (error, data, response) => {
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
 **realm** | **String**| realm name (not id!) | 
 **id** | **String**|  | 
 **componentRepresentation** | [**ComponentRepresentation**](ComponentRepresentation.md)|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmComponentsIdSubComponentTypesGet

> [ComponentTypeRepresentation] realmComponentsIdSubComponentTypesGet(realm, id, opts)

List of subcomponent types that are available to configure for a particular parent component.

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ComponentApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | 
let opts = {
  'type': "type_example" // String | 
};
apiInstance.realmComponentsIdSubComponentTypesGet(realm, id, opts, (error, data, response) => {
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
 **realm** | **String**| realm name (not id!) | 
 **id** | **String**|  | 
 **type** | **String**|  | [optional] 

### Return type

[**[ComponentTypeRepresentation]**](ComponentTypeRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmComponentsPost

> realmComponentsPost(realm, componentRepresentation)



### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ComponentApi();
let realm = "realm_example"; // String | realm name (not id!)
let componentRepresentation = new KeycloakAdminRestApi.ComponentRepresentation(); // ComponentRepresentation | 
apiInstance.realmComponentsPost(realm, componentRepresentation, (error, data, response) => {
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
 **realm** | **String**| realm name (not id!) | 
 **componentRepresentation** | [**ComponentRepresentation**](ComponentRepresentation.md)|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

