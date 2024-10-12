# AIceptionInteractive.CreativeApi

All URIs are relative to *https://aiception.com/api/v2.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**artisticImagePost**](CreativeApi.md#artisticImagePost) | **POST** /artistic_image | Create an artistic image [ image_url, style_url -&gt; id ]
[**artisticImageTaskIdGet**](CreativeApi.md#artisticImageTaskIdGet) | **GET** /artistic_image/{taskId} | Gets a artistic image by task id [ id -&gt; artistic image task ]



## artisticImagePost

> Task artisticImagePost(body)

Create an artistic image [ image_url, style_url -&gt; id ]

Given an image content and a style image create a new stylized image of the content.

### Example

```javascript
import AIceptionInteractive from 'a_iception_interactive';
let defaultClient = AIceptionInteractive.ApiClient.instance;
// Configure HTTP basic authorization: UserSecurity
let UserSecurity = defaultClient.authentications['UserSecurity'];
UserSecurity.username = 'YOUR USERNAME';
UserSecurity.password = 'YOUR PASSWORD';

let apiInstance = new AIceptionInteractive.CreativeApi();
let body = new AIceptionInteractive.ArtisticImagePostRequest(); // ArtisticImagePostRequest | The content image and the style image
apiInstance.artisticImagePost(body, (error, data, response) => {
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
 **body** | [**ArtisticImagePostRequest**](ArtisticImagePostRequest.md)| The content image and the style image | 

### Return type

[**Task**](Task.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## artisticImageTaskIdGet

> Task artisticImageTaskIdGet(taskId)

Gets a artistic image by task id [ id -&gt; artistic image task ]

The artistic_image will have the urls of the stylized images.

### Example

```javascript
import AIceptionInteractive from 'a_iception_interactive';
let defaultClient = AIceptionInteractive.ApiClient.instance;
// Configure HTTP basic authorization: UserSecurity
let UserSecurity = defaultClient.authentications['UserSecurity'];
UserSecurity.username = 'YOUR USERNAME';
UserSecurity.password = 'YOUR PASSWORD';

let apiInstance = new AIceptionInteractive.CreativeApi();
let taskId = "taskId_example"; // String | An internal id for the task
apiInstance.artisticImageTaskIdGet(taskId, (error, data, response) => {
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
 **taskId** | **String**| An internal id for the task | 

### Return type

[**Task**](Task.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

