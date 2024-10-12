# 1PasswordConnect.VaultsApi

All URIs are relative to *http://1password.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getVaultById**](VaultsApi.md#getVaultById) | **GET** /vaults/{vaultUuid} | Get Vault details and metadata
[**getVaults**](VaultsApi.md#getVaults) | **GET** /vaults | Get all Vaults



## getVaultById

> Vault getVaultById(vaultUuid)

Get Vault details and metadata

### Example

```javascript
import 1PasswordConnect from '1_password_connect';
let defaultClient = 1PasswordConnect.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: ConnectToken
let ConnectToken = defaultClient.authentications['ConnectToken'];
ConnectToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new 1PasswordConnect.VaultsApi();
let vaultUuid = "vaultUuid_example"; // String | The UUID of the Vault to fetch Items from
apiInstance.getVaultById(vaultUuid, (error, data, response) => {
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
 **vaultUuid** | **String**| The UUID of the Vault to fetch Items from | 

### Return type

[**Vault**](Vault.md)

### Authorization

[ConnectToken](../README.md#ConnectToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVaults

> [Vault] getVaults(opts)

Get all Vaults

### Example

```javascript
import 1PasswordConnect from '1_password_connect';
let defaultClient = 1PasswordConnect.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: ConnectToken
let ConnectToken = defaultClient.authentications['ConnectToken'];
ConnectToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new 1PasswordConnect.VaultsApi();
let opts = {
  'filter': "name eq \"Some Vault Name\"" // String | Filter the Vault collection based on Vault name using SCIM eq filter
};
apiInstance.getVaults(opts, (error, data, response) => {
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
 **filter** | **String**| Filter the Vault collection based on Vault name using SCIM eq filter | [optional] 

### Return type

[**[Vault]**](Vault.md)

### Authorization

[ConnectToken](../README.md#ConnectToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

