# 1PasswordConnect.ItemsApi

All URIs are relative to *http://1password.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createVaultItem**](ItemsApi.md#createVaultItem) | **POST** /vaults/{vaultUuid}/items | Create a new Item
[**deleteVaultItem**](ItemsApi.md#deleteVaultItem) | **DELETE** /vaults/{vaultUuid}/items/{itemUuid} | Delete an Item
[**getVaultItemById**](ItemsApi.md#getVaultItemById) | **GET** /vaults/{vaultUuid}/items/{itemUuid} | Get the details of an Item
[**getVaultItems**](ItemsApi.md#getVaultItems) | **GET** /vaults/{vaultUuid}/items | Get all items for inside a Vault
[**patchVaultItem**](ItemsApi.md#patchVaultItem) | **PATCH** /vaults/{vaultUuid}/items/{itemUuid} | Update a subset of Item attributes
[**updateVaultItem**](ItemsApi.md#updateVaultItem) | **PUT** /vaults/{vaultUuid}/items/{itemUuid} | Update an Item



## createVaultItem

> FullItem createVaultItem(vaultUuid, opts)

Create a new Item

### Example

```javascript
import 1PasswordConnect from '1_password_connect';
let defaultClient = 1PasswordConnect.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: ConnectToken
let ConnectToken = defaultClient.authentications['ConnectToken'];
ConnectToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new 1PasswordConnect.ItemsApi();
let vaultUuid = "vaultUuid_example"; // String | The UUID of the Vault to create an Item in
let opts = {
  'fullItem': new 1PasswordConnect.FullItem() // FullItem | 
};
apiInstance.createVaultItem(vaultUuid, opts, (error, data, response) => {
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
 **vaultUuid** | **String**| The UUID of the Vault to create an Item in | 
 **fullItem** | [**FullItem**](FullItem.md)|  | [optional] 

### Return type

[**FullItem**](FullItem.md)

### Authorization

[ConnectToken](../README.md#ConnectToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteVaultItem

> deleteVaultItem(vaultUuid, itemUuid)

Delete an Item

### Example

```javascript
import 1PasswordConnect from '1_password_connect';
let defaultClient = 1PasswordConnect.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: ConnectToken
let ConnectToken = defaultClient.authentications['ConnectToken'];
ConnectToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new 1PasswordConnect.ItemsApi();
let vaultUuid = "vaultUuid_example"; // String | The UUID of the Vault the item is in
let itemUuid = "itemUuid_example"; // String | The UUID of the Item to update
apiInstance.deleteVaultItem(vaultUuid, itemUuid, (error, data, response) => {
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
 **vaultUuid** | **String**| The UUID of the Vault the item is in | 
 **itemUuid** | **String**| The UUID of the Item to update | 

### Return type

null (empty response body)

### Authorization

[ConnectToken](../README.md#ConnectToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVaultItemById

> FullItem getVaultItemById(vaultUuid, itemUuid)

Get the details of an Item

### Example

```javascript
import 1PasswordConnect from '1_password_connect';
let defaultClient = 1PasswordConnect.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: ConnectToken
let ConnectToken = defaultClient.authentications['ConnectToken'];
ConnectToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new 1PasswordConnect.ItemsApi();
let vaultUuid = "vaultUuid_example"; // String | The UUID of the Vault to fetch Item from
let itemUuid = "itemUuid_example"; // String | The UUID of the Item to fetch
apiInstance.getVaultItemById(vaultUuid, itemUuid, (error, data, response) => {
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
 **vaultUuid** | **String**| The UUID of the Vault to fetch Item from | 
 **itemUuid** | **String**| The UUID of the Item to fetch | 

### Return type

[**FullItem**](FullItem.md)

### Authorization

[ConnectToken](../README.md#ConnectToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVaultItems

> [Item] getVaultItems(vaultUuid, opts)

Get all items for inside a Vault

### Example

```javascript
import 1PasswordConnect from '1_password_connect';
let defaultClient = 1PasswordConnect.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: ConnectToken
let ConnectToken = defaultClient.authentications['ConnectToken'];
ConnectToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new 1PasswordConnect.ItemsApi();
let vaultUuid = "vaultUuid_example"; // String | The UUID of the Vault to fetch Items from
let opts = {
  'filter': "title eq \"Some Item Name\"" // String | Filter the Item collection based on Item name using SCIM eq filter
};
apiInstance.getVaultItems(vaultUuid, opts, (error, data, response) => {
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
 **filter** | **String**| Filter the Item collection based on Item name using SCIM eq filter | [optional] 

### Return type

[**[Item]**](Item.md)

### Authorization

[ConnectToken](../README.md#ConnectToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchVaultItem

> FullItem patchVaultItem(vaultUuid, itemUuid, opts)

Update a subset of Item attributes

Applies a modified [RFC6902 JSON Patch](https://tools.ietf.org/html/rfc6902) document to an Item or ItemField. This endpoint only supports &#x60;add&#x60;, &#x60;remove&#x60; and &#x60;replace&#x60; operations.  When modifying a specific ItemField, the ItemField&#39;s ID in the &#x60;path&#x60; attribute of the operation object: &#x60;/fields/{fieldId}&#x60; 

### Example

```javascript
import 1PasswordConnect from '1_password_connect';
let defaultClient = 1PasswordConnect.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: ConnectToken
let ConnectToken = defaultClient.authentications['ConnectToken'];
ConnectToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new 1PasswordConnect.ItemsApi();
let vaultUuid = "vaultUuid_example"; // String | The UUID of the Vault the item is in
let itemUuid = "itemUuid_example"; // String | The UUID of the Item to update
let opts = {
  'patchInner': [{"op":"replace","path":"/favorite","value":true},{"op":"remove","path":"/tags/1"}] // [PatchInner] | 
};
apiInstance.patchVaultItem(vaultUuid, itemUuid, opts, (error, data, response) => {
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
 **vaultUuid** | **String**| The UUID of the Vault the item is in | 
 **itemUuid** | **String**| The UUID of the Item to update | 
 **patchInner** | [**[PatchInner]**](PatchInner.md)|  | [optional] 

### Return type

[**FullItem**](FullItem.md)

### Authorization

[ConnectToken](../README.md#ConnectToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateVaultItem

> FullItem updateVaultItem(vaultUuid, itemUuid, opts)

Update an Item

### Example

```javascript
import 1PasswordConnect from '1_password_connect';
let defaultClient = 1PasswordConnect.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: ConnectToken
let ConnectToken = defaultClient.authentications['ConnectToken'];
ConnectToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new 1PasswordConnect.ItemsApi();
let vaultUuid = "vaultUuid_example"; // String | The UUID of the Item's Vault
let itemUuid = "itemUuid_example"; // String | The UUID of the Item to update
let opts = {
  'fullItem': new 1PasswordConnect.FullItem() // FullItem | 
};
apiInstance.updateVaultItem(vaultUuid, itemUuid, opts, (error, data, response) => {
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
 **vaultUuid** | **String**| The UUID of the Item&#39;s Vault | 
 **itemUuid** | **String**| The UUID of the Item to update | 
 **fullItem** | [**FullItem**](FullItem.md)|  | [optional] 

### Return type

[**FullItem**](FullItem.md)

### Authorization

[ConnectToken](../README.md#ConnectToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

