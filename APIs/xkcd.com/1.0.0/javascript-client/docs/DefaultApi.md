# Xkcd.DefaultApi

All URIs are relative to *http://xkcd.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**comicIdInfo0JsonGet**](DefaultApi.md#comicIdInfo0JsonGet) | **GET** /{comicId}/info.0.json | 
[**info0JsonGet**](DefaultApi.md#info0JsonGet) | **GET** /info.0.json | 



## comicIdInfo0JsonGet

> Comic comicIdInfo0JsonGet(comicId)



Fetch comics and metadata  by comic id. 

### Example

```javascript
import Xkcd from 'xkcd';

let apiInstance = new Xkcd.DefaultApi();
let comicId = 3.4; // Number | 
apiInstance.comicIdInfo0JsonGet(comicId, (error, data, response) => {
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
 **comicId** | **Number**|  | 

### Return type

[**Comic**](Comic.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## info0JsonGet

> Comic info0JsonGet()



Fetch current comic and metadata. 

### Example

```javascript
import Xkcd from 'xkcd';

let apiInstance = new Xkcd.DefaultApi();
apiInstance.info0JsonGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**Comic**](Comic.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

