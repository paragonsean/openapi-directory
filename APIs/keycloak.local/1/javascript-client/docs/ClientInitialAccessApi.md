# KeycloakAdminRestApi.ClientInitialAccessApi

All URIs are relative to *http://keycloak.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**realmClientsInitialAccessGet**](ClientInitialAccessApi.md#realmClientsInitialAccessGet) | **GET** /{realm}/clients-initial-access | 
[**realmClientsInitialAccessIdDelete**](ClientInitialAccessApi.md#realmClientsInitialAccessIdDelete) | **DELETE** /{realm}/clients-initial-access/{id} | 
[**realmClientsInitialAccessPost**](ClientInitialAccessApi.md#realmClientsInitialAccessPost) | **POST** /{realm}/clients-initial-access | Create a new initial access token.



## realmClientsInitialAccessGet

> [ClientInitialAccessPresentation] realmClientsInitialAccessGet(realm)



### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ClientInitialAccessApi();
let realm = "realm_example"; // String | realm name (not id!)
apiInstance.realmClientsInitialAccessGet(realm, (error, data, response) => {
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

### Return type

[**[ClientInitialAccessPresentation]**](ClientInitialAccessPresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmClientsInitialAccessIdDelete

> realmClientsInitialAccessIdDelete(realm, id)



### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ClientInitialAccessApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | 
apiInstance.realmClientsInitialAccessIdDelete(realm, id, (error, data, response) => {
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


## realmClientsInitialAccessPost

> ClientInitialAccessPresentation realmClientsInitialAccessPost(realm, clientInitialAccessCreatePresentation)

Create a new initial access token.

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ClientInitialAccessApi();
let realm = "realm_example"; // String | realm name (not id!)
let clientInitialAccessCreatePresentation = new KeycloakAdminRestApi.ClientInitialAccessCreatePresentation(); // ClientInitialAccessCreatePresentation | 
apiInstance.realmClientsInitialAccessPost(realm, clientInitialAccessCreatePresentation, (error, data, response) => {
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
 **clientInitialAccessCreatePresentation** | [**ClientInitialAccessCreatePresentation**](ClientInitialAccessCreatePresentation.md)|  | 

### Return type

[**ClientInitialAccessPresentation**](ClientInitialAccessPresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

