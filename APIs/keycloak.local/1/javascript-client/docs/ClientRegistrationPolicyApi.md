# KeycloakAdminRestApi.ClientRegistrationPolicyApi

All URIs are relative to *http://keycloak.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**realmClientRegistrationPolicyProvidersGet**](ClientRegistrationPolicyApi.md#realmClientRegistrationPolicyProvidersGet) | **GET** /{realm}/client-registration-policy/providers | Base path for retrieve providers with the configProperties properly filled



## realmClientRegistrationPolicyProvidersGet

> [ComponentTypeRepresentation] realmClientRegistrationPolicyProvidersGet(realm)

Base path for retrieve providers with the configProperties properly filled

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ClientRegistrationPolicyApi();
let realm = "realm_example"; // String | realm name (not id!)
apiInstance.realmClientRegistrationPolicyProvidersGet(realm, (error, data, response) => {
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

[**[ComponentTypeRepresentation]**](ComponentTypeRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

