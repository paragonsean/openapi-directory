# GameSparksGameDetailsApi.CredentialsApi

All URIs are relative to *http://config2.gamesparks.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**updateCredentialSecretUsingPOST**](CredentialsApi.md#updateCredentialSecretUsingPOST) | **POST** /restv2/game/{apiKey}/config/~credentials/{credentialName}/resetSecret | Resets the secret of a credential



## updateCredentialSecretUsingPOST

> updateCredentialSecretUsingPOST(apiKey, credentialName)

Resets the secret of a credential

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.CredentialsApi();
let apiKey = "apiKey_example"; // String | apiKey
let credentialName = "credentialName_example"; // String | credentialName
apiInstance.updateCredentialSecretUsingPOST(apiKey, credentialName, (error, data, response) => {
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
 **apiKey** | **String**| apiKey | 
 **credentialName** | **String**| credentialName | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8

