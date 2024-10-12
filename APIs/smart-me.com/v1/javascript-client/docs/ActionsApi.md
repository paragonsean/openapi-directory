# SmartMe.ActionsApi

All URIs are relative to *https://smart-me.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**actionsGet**](ActionsApi.md#actionsGet) | **GET** /api/Actions/{id} | Gets all available Actions of a Device
[**actionsPost**](ActionsApi.md#actionsPost) | **POST** /api/Actions | Set an action for the specified device.



## actionsGet

> [ActionInformation] actionsGet(id)

Gets all available Actions of a Device

Gets all available Actions of a Device

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.ActionsApi();
let id = "id_example"; // String | The ID of the device
apiInstance.actionsGet(id, (error, data, response) => {
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
 **id** | **String**| The ID of the device | 

### Return type

[**[ActionInformation]**](ActionInformation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## actionsPost

> actionsPost(actionToPost)

Set an action for the specified device.

Set an action for the specified device.

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.ActionsApi();
let actionToPost = new SmartMe.ActionToPost(); // ActionToPost | The Action Data
apiInstance.actionsPost(actionToPost, (error, data, response) => {
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
 **actionToPost** | [**ActionToPost**](ActionToPost.md)| The Action Data | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: Not defined

