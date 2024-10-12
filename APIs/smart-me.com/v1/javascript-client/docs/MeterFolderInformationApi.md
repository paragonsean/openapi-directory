# SmartMe.MeterFolderInformationApi

All URIs are relative to *https://smart-me.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**meterFolderInformationGet**](MeterFolderInformationApi.md#meterFolderInformationGet) | **GET** /api/MeterFolderInformation/{id} | Beta: Gets the General Information for a Meter or a Folder
[**meterFolderInformationPost**](MeterFolderInformationApi.md#meterFolderInformationPost) | **POST** /api/MeterFolderInformation | Sets the Name of a Meter or a Folder



## meterFolderInformationGet

> MeterFolderInformation meterFolderInformationGet(id)

Beta: Gets the General Information for a Meter or a Folder

Beta: Gets the General Information for a Meter or a Folder

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.MeterFolderInformationApi();
let id = "id_example"; // String | 
apiInstance.meterFolderInformationGet(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

[**MeterFolderInformation**](MeterFolderInformation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## meterFolderInformationPost

> meterFolderInformationPost(meterFolderInformationToPost)

Sets the Name of a Meter or a Folder

Sets the Name of a Meter or a Folder

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.MeterFolderInformationApi();
let meterFolderInformationToPost = new SmartMe.MeterFolderInformationToPost(); // MeterFolderInformationToPost | 
apiInstance.meterFolderInformationPost(meterFolderInformationToPost, (error, data, response) => {
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
 **meterFolderInformationToPost** | [**MeterFolderInformationToPost**](MeterFolderInformationToPost.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: Not defined

