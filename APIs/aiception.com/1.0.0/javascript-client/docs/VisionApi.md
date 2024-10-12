# AIceptionInteractive.VisionApi

All URIs are relative to *https://aiception.com/api/v2.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adultContentPost**](VisionApi.md#adultContentPost) | **POST** /adult_content | Image contains nudity or sexually explicit content? [ image_url -&gt; id ]
[**adultContentTaskIdGet**](VisionApi.md#adultContentTaskIdGet) | **GET** /adult_content/{taskId} | Gets the adult_content task [ id -&gt; adult content task ]
[**detectObjectPost**](VisionApi.md#detectObjectPost) | **POST** /detect_object | What is that object? [ image_url -&gt; id ]
[**detectObjectTaskIdGet**](VisionApi.md#detectObjectTaskIdGet) | **GET** /detect_object/{taskId} | Gets the detect_object task [ id -&gt; detect object task]
[**faceAgePost**](VisionApi.md#faceAgePost) | **POST** /face_age | How old is the person in the image? [ image_url -&gt; id ]
[**faceAgeTaskIdGet**](VisionApi.md#faceAgeTaskIdGet) | **GET** /face_age/{taskId} | Gets the face_age task [ id -&gt; face age task ]
[**facePost**](VisionApi.md#facePost) | **POST** /face | Find all faces in the image [ image_url -&gt; id ]
[**faceTaskIdGet**](VisionApi.md#faceTaskIdGet) | **GET** /face/{taskId} | Gets the face task [ id -&gt; face task ]



## adultContentPost

> Task adultContentPost(body)

Image contains nudity or sexually explicit content? [ image_url -&gt; id ]

Creates a new adult_content task that tells the if the image has nudity or sexual content.

### Example

```javascript
import AIceptionInteractive from 'a_iception_interactive';
let defaultClient = AIceptionInteractive.ApiClient.instance;
// Configure HTTP basic authorization: UserSecurity
let UserSecurity = defaultClient.authentications['UserSecurity'];
UserSecurity.username = 'YOUR USERNAME';
UserSecurity.password = 'YOUR PASSWORD';

let apiInstance = new AIceptionInteractive.VisionApi();
let body = new AIceptionInteractive.AdultContentPostRequest(); // AdultContentPostRequest | The image to analyze
apiInstance.adultContentPost(body, (error, data, response) => {
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
 **body** | [**AdultContentPostRequest**](AdultContentPostRequest.md)| The image to analyze | 

### Return type

[**Task**](Task.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## adultContentTaskIdGet

> Task adultContentTaskIdGet(taskId)

Gets the adult_content task [ id -&gt; adult content task ]

Gets the adult_content task.

### Example

```javascript
import AIceptionInteractive from 'a_iception_interactive';
let defaultClient = AIceptionInteractive.ApiClient.instance;
// Configure HTTP basic authorization: UserSecurity
let UserSecurity = defaultClient.authentications['UserSecurity'];
UserSecurity.username = 'YOUR USERNAME';
UserSecurity.password = 'YOUR PASSWORD';

let apiInstance = new AIceptionInteractive.VisionApi();
let taskId = "taskId_example"; // String | An internal id for the task
apiInstance.adultContentTaskIdGet(taskId, (error, data, response) => {
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


## detectObjectPost

> Task detectObjectPost(body)

What is that object? [ image_url -&gt; id ]

Creates a new detect object task that recognizes the object in the image.

### Example

```javascript
import AIceptionInteractive from 'a_iception_interactive';
let defaultClient = AIceptionInteractive.ApiClient.instance;
// Configure HTTP basic authorization: UserSecurity
let UserSecurity = defaultClient.authentications['UserSecurity'];
UserSecurity.username = 'YOUR USERNAME';
UserSecurity.password = 'YOUR PASSWORD';

let apiInstance = new AIceptionInteractive.VisionApi();
let body = new AIceptionInteractive.AdultContentPostRequest(); // AdultContentPostRequest | The image to analyze
apiInstance.detectObjectPost(body, (error, data, response) => {
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
 **body** | [**AdultContentPostRequest**](AdultContentPostRequest.md)| The image to analyze | 

### Return type

[**Task**](Task.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## detectObjectTaskIdGet

> Task detectObjectTaskIdGet(taskId)

Gets the detect_object task [ id -&gt; detect object task]

Gets the detect_object task.

### Example

```javascript
import AIceptionInteractive from 'a_iception_interactive';
let defaultClient = AIceptionInteractive.ApiClient.instance;
// Configure HTTP basic authorization: UserSecurity
let UserSecurity = defaultClient.authentications['UserSecurity'];
UserSecurity.username = 'YOUR USERNAME';
UserSecurity.password = 'YOUR PASSWORD';

let apiInstance = new AIceptionInteractive.VisionApi();
let taskId = "taskId_example"; // String | An internal id for the task
apiInstance.detectObjectTaskIdGet(taskId, (error, data, response) => {
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


## faceAgePost

> Task faceAgePost(body)

How old is the person in the image? [ image_url -&gt; id ]

Creates a new face age task that approximates the age of the person in the image.

### Example

```javascript
import AIceptionInteractive from 'a_iception_interactive';
let defaultClient = AIceptionInteractive.ApiClient.instance;
// Configure HTTP basic authorization: UserSecurity
let UserSecurity = defaultClient.authentications['UserSecurity'];
UserSecurity.username = 'YOUR USERNAME';
UserSecurity.password = 'YOUR PASSWORD';

let apiInstance = new AIceptionInteractive.VisionApi();
let body = new AIceptionInteractive.AdultContentPostRequest(); // AdultContentPostRequest | The image to analyze
apiInstance.faceAgePost(body, (error, data, response) => {
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
 **body** | [**AdultContentPostRequest**](AdultContentPostRequest.md)| The image to analyze | 

### Return type

[**Task**](Task.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## faceAgeTaskIdGet

> Task faceAgeTaskIdGet(taskId)

Gets the face_age task [ id -&gt; face age task ]

Gets the face_age task.

### Example

```javascript
import AIceptionInteractive from 'a_iception_interactive';
let defaultClient = AIceptionInteractive.ApiClient.instance;
// Configure HTTP basic authorization: UserSecurity
let UserSecurity = defaultClient.authentications['UserSecurity'];
UserSecurity.username = 'YOUR USERNAME';
UserSecurity.password = 'YOUR PASSWORD';

let apiInstance = new AIceptionInteractive.VisionApi();
let taskId = "taskId_example"; // String | An internal id for the task
apiInstance.faceAgeTaskIdGet(taskId, (error, data, response) => {
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


## facePost

> Task facePost(body)

Find all faces in the image [ image_url -&gt; id ]

Get a list of all the locations of the faces in the image.

### Example

```javascript
import AIceptionInteractive from 'a_iception_interactive';
let defaultClient = AIceptionInteractive.ApiClient.instance;
// Configure HTTP basic authorization: UserSecurity
let UserSecurity = defaultClient.authentications['UserSecurity'];
UserSecurity.username = 'YOUR USERNAME';
UserSecurity.password = 'YOUR PASSWORD';

let apiInstance = new AIceptionInteractive.VisionApi();
let body = new AIceptionInteractive.AdultContentPostRequest(); // AdultContentPostRequest | The image to analyze
apiInstance.facePost(body, (error, data, response) => {
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
 **body** | [**AdultContentPostRequest**](AdultContentPostRequest.md)| The image to analyze | 

### Return type

[**Task**](Task.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## faceTaskIdGet

> Task faceTaskIdGet(taskId)

Gets the face task [ id -&gt; face task ]

Gets the face task.

### Example

```javascript
import AIceptionInteractive from 'a_iception_interactive';
let defaultClient = AIceptionInteractive.ApiClient.instance;
// Configure HTTP basic authorization: UserSecurity
let UserSecurity = defaultClient.authentications['UserSecurity'];
UserSecurity.username = 'YOUR USERNAME';
UserSecurity.password = 'YOUR PASSWORD';

let apiInstance = new AIceptionInteractive.VisionApi();
let taskId = "taskId_example"; // String | An internal id for the task
apiInstance.faceTaskIdGet(taskId, (error, data, response) => {
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

