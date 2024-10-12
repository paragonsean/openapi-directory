# LinodeApi.ImagesApi

All URIs are relative to *https://api.linode.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createImage**](ImagesApi.md#createImage) | **POST** /images | Image Create
[**deleteImage**](ImagesApi.md#deleteImage) | **DELETE** /images/{imageId} | Image Delete
[**getImage**](ImagesApi.md#getImage) | **GET** /images/{imageId} | Image View
[**getImages**](ImagesApi.md#getImages) | **GET** /images | Images List
[**imagesUploadPost**](ImagesApi.md#imagesUploadPost) | **POST** /images/upload | Image Upload
[**updateImage**](ImagesApi.md#updateImage) | **PUT** /images/{imageId} | Image Update



## createImage

> Image createImage(opts)

Image Create

Captures a private gold-master Image from a Linode Disk. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ImagesApi();
let opts = {
  'createImageRequest': new LinodeApi.CreateImageRequest() // CreateImageRequest | Information about the Image to create.
};
apiInstance.createImage(opts, (error, data, response) => {
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
 **createImageRequest** | [**CreateImageRequest**](CreateImageRequest.md)| Information about the Image to create. | [optional] 

### Return type

[**Image**](Image.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteImage

> Object deleteImage(imageId)

Image Delete

Deletes a private Image you have permission to &#x60;read_write&#x60;.   **Deleting an Image is a destructive action and cannot be undone.** 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ImagesApi();
let imageId = "imageId_example"; // String | ID of the Image to look up.
apiInstance.deleteImage(imageId, (error, data, response) => {
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
 **imageId** | **String**| ID of the Image to look up. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getImage

> Image getImage(imageId)

Image View

Get information about a single Image.  * **Public** Images have IDs that begin with \&quot;linode/\&quot;. These distribution images are generally available to all users.  * **Private** Images have IDs that begin with \&quot;private/\&quot;. These Images are Account-specific and only accessible to Users with appropriate [Grants](/docs/api/account/#users-grants-view).  * To view a public Image, call this endpoint with or without authentication. To view a private Image, call this endpoint with authentication. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ImagesApi();
let imageId = "imageId_example"; // String | ID of the Image to look up.
apiInstance.getImage(imageId, (error, data, response) => {
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
 **imageId** | **String**| ID of the Image to look up. | 

### Return type

[**Image**](Image.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getImages

> GetImages200Response getImages(opts)

Images List

Returns a paginated list of Images.  * **Public** Images have IDs that begin with \&quot;linode/\&quot;. These distribution images are generally available to all users.  * **Private** Images have IDs that begin with \&quot;private/\&quot;. These Images are Account-specific and only accessible to Users with appropriate [Grants](/docs/api/account/#users-grants-view).  * To view only public Images, call this endpoint with or without authentication. To view private Images as well, call this endpoint with authentication. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ImagesApi();
let opts = {
  'page': 1, // Number | The page of a collection to return.
  'pageSize': 100 // Number | The number of items to return per page.
};
apiInstance.getImages(opts, (error, data, response) => {
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
 **page** | **Number**| The page of a collection to return. | [optional] [default to 1]
 **pageSize** | **Number**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetImages200Response**](GetImages200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## imagesUploadPost

> ImagesUploadPost200Response imagesUploadPost(opts)

Image Upload

Initiates an Image upload.  This endpoint creates a new private Image object and returns it along with the URL to which image data can be uploaded.  - Image data must be uploaded within 24 hours of creation or the upload will be cancelled and the image deleted.  - Image uploads should be made as an HTTP PUT request to the URL returned in the &#x60;upload_to&#x60; response parameter, with a &#x60;Content-type: application/octet-stream&#x60; header included in the request. For example:        curl -v \\         -H \&quot;Content-Type: application/octet-stream\&quot; \\         --upload-file example.img.gz \\         $UPLOAD_URL \\         --progress-bar \\         --output /dev/null  - Uploaded image data should be compressed in gzip (&#x60;.gz&#x60;) format. The uncompressed disk should be in raw disk image (&#x60;.img&#x60;) format. A maximum compressed file size of 5GB is supported for upload at this time.  **Note:** To initiate and complete an Image upload in a single step, see our guide on how to [Upload an Image](/docs/products/tools/images/guides/upload-an-image/) using Cloud Manager or the Linode CLI &#x60;image-upload&#x60; plugin. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ImagesApi();
let opts = {
  'imagesUploadPostRequest': new LinodeApi.ImagesUploadPostRequest() // ImagesUploadPostRequest | The uploaded Image details.
};
apiInstance.imagesUploadPost(opts, (error, data, response) => {
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
 **imagesUploadPostRequest** | [**ImagesUploadPostRequest**](ImagesUploadPostRequest.md)| The uploaded Image details. | [optional] 

### Return type

[**ImagesUploadPost200Response**](ImagesUploadPost200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateImage

> Image updateImage(imageId, image)

Image Update

Updates a private Image that you have permission to &#x60;read_write&#x60;. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ImagesApi();
let imageId = "imageId_example"; // String | ID of the Image to look up.
let image = new LinodeApi.Image(); // Image | The fields to update. 
apiInstance.updateImage(imageId, image, (error, data, response) => {
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
 **imageId** | **String**| ID of the Image to look up. | 
 **image** | [**Image**](Image.md)| The fields to update.  | 

### Return type

[**Image**](Image.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

