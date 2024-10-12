# Semantria.BlacklistApi

All URIs are relative to *https://api.semantria.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addBlacklist**](BlacklistApi.md#addBlacklist) | **POST** /blacklist.{content_type} | Add items to blacklist
[**deleteBlacklistItems**](BlacklistApi.md#deleteBlacklistItems) | **DELETE** /blacklist.{content_type} | Remove items from blacklist
[**getBlacklist**](BlacklistApi.md#getBlacklist) | **GET** /blacklist.{content_type} | Retrieve blacklisted items
[**updateBlacklist**](BlacklistApi.md#updateBlacklist) | **PUT** /blacklist.{content_type} | Update items in blacklist



## addBlacklist

> [BlacklistItemResponseVersion] addBlacklist(contentType, blacklistedItems, opts)

Add items to blacklist

This method adds new unique items to the backlist on Semantria side.

### Example

```javascript
import Semantria from 'semantria';

let apiInstance = new Semantria.BlacklistApi();
let contentType = "contentType_example"; // String | 
let blacklistedItems = {key: null}; // Object | List of parametrized JSON or XML objects.
let opts = {
  'configId': "configId_example" // String | Identifier of configuration blacklist linked to.
};
apiInstance.addBlacklist(contentType, blacklistedItems, opts, (error, data, response) => {
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
 **contentType** | **String**|  | 
 **blacklistedItems** | **Object**| List of parametrized JSON or XML objects. | 
 **configId** | **String**| Identifier of configuration blacklist linked to. | [optional] 

### Return type

[**[BlacklistItemResponseVersion]**](BlacklistItemResponseVersion.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## deleteBlacklistItems

> deleteBlacklistItems(contentType, blacklistedItemIDs, opts)

Remove items from blacklist

This method removes certain blacklisted items by their values on Semantria side.

### Example

```javascript
import Semantria from 'semantria';

let apiInstance = new Semantria.BlacklistApi();
let contentType = "contentType_example"; // String | 
let blacklistedItemIDs = ["null"]; // [String] | List of unique blacklisted item identifiers (string).
let opts = {
  'configId': "configId_example" // String | Identifier of configuration blacklist items linked to.
};
apiInstance.deleteBlacklistItems(contentType, blacklistedItemIDs, opts, (error, data, response) => {
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
 **contentType** | **String**|  | 
 **blacklistedItemIDs** | [**[String]**](String.md)| List of unique blacklisted item identifiers (string). | 
 **configId** | **String**| Identifier of configuration blacklist items linked to. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getBlacklist

> [BlacklistItemResponseVersion] getBlacklist(contentType, opts)

Retrieve blacklisted items

This method retrieves all backlisted items available on Semantria side.

### Example

```javascript
import Semantria from 'semantria';

let apiInstance = new Semantria.BlacklistApi();
let contentType = "contentType_example"; // String | 
let opts = {
  'configId': "configId_example" // String | Identifier of configuration blacklist linked to.
};
apiInstance.getBlacklist(contentType, opts, (error, data, response) => {
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
 **contentType** | **String**|  | 
 **configId** | **String**| Identifier of configuration blacklist linked to. | [optional] 

### Return type

[**[BlacklistItemResponseVersion]**](BlacklistItemResponseVersion.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## updateBlacklist

> [BlacklistItemResponseVersion] updateBlacklist(contentType, blacklistedItems, opts)

Update items in blacklist

This method updates existing items by unique IDs in the backlist on Semantria side.

### Example

```javascript
import Semantria from 'semantria';

let apiInstance = new Semantria.BlacklistApi();
let contentType = "contentType_example"; // String | 
let blacklistedItems = {key: null}; // Object | List of parametrized JSON or XML objects.
let opts = {
  'configId': "configId_example" // String | Identifier of configuration blacklist linked to.
};
apiInstance.updateBlacklist(contentType, blacklistedItems, opts, (error, data, response) => {
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
 **contentType** | **String**|  | 
 **blacklistedItems** | **Object**| List of parametrized JSON or XML objects. | 
 **configId** | **String**| Identifier of configuration blacklist linked to. | [optional] 

### Return type

[**[BlacklistItemResponseVersion]**](BlacklistItemResponseVersion.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

