# TheySaidSoQuotesApi.QuoteImagesApi

All URIs are relative to *https://quotes.rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quoteImageBackgroundDelete**](QuoteImagesApi.md#quoteImageBackgroundDelete) | **DELETE** /quote/image/background | 
[**quoteImageBackgroundListGet**](QuoteImagesApi.md#quoteImageBackgroundListGet) | **GET** /quote/image/background/list | 
[**quoteImageBackgroundPost**](QuoteImagesApi.md#quoteImageBackgroundPost) | **POST** /quote/image/background | 
[**quoteImageBackgroundSearchGet**](QuoteImagesApi.md#quoteImageBackgroundSearchGet) | **GET** /quote/image/background/search | 
[**quoteImageBackgroundTagsAddPost**](QuoteImagesApi.md#quoteImageBackgroundTagsAddPost) | **POST** /quote/image/background/tags/add | 
[**quoteImageBackgroundTagsRemovePost**](QuoteImagesApi.md#quoteImageBackgroundTagsRemovePost) | **POST** /quote/image/background/tags/remove | 
[**quoteImageDelete**](QuoteImagesApi.md#quoteImageDelete) | **DELETE** /quote/image | 
[**quoteImageFontDelete**](QuoteImagesApi.md#quoteImageFontDelete) | **DELETE** /quote/image/font | 
[**quoteImageFontListGet**](QuoteImagesApi.md#quoteImageFontListGet) | **GET** /quote/image/font/list | 
[**quoteImageFontPost**](QuoteImagesApi.md#quoteImageFontPost) | **POST** /quote/image/font | 
[**quoteImageFontSearchGet**](QuoteImagesApi.md#quoteImageFontSearchGet) | **GET** /quote/image/font/search | 
[**quoteImageFontTagsAddPost**](QuoteImagesApi.md#quoteImageFontTagsAddPost) | **POST** /quote/image/font/tags/add | 
[**quoteImageFontTagsRemovePost**](QuoteImagesApi.md#quoteImageFontTagsRemovePost) | **POST** /quote/image/font/tags/remove | 
[**quoteImageGet**](QuoteImagesApi.md#quoteImageGet) | **GET** /quote/image | 
[**quoteImagePut**](QuoteImagesApi.md#quoteImagePut) | **PUT** /quote/image | 
[**quoteImageSearchGet**](QuoteImagesApi.md#quoteImageSearchGet) | **GET** /quote/image/search | 



## quoteImageBackgroundDelete

> quoteImageBackgroundDelete(id)



Delete a background image file. The user needs to be the owner of the background image to be able to delete it. 

### Example

```javascript
import TheySaidSoQuotesApi from 'they_said_so_quotes_api';
let defaultClient = TheySaidSoQuotesApi.ApiClient.instance;
// Configure Bearer (bearer token) access token for authorization: BearerAuth
let BearerAuth = defaultClient.authentications['BearerAuth'];
BearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TheySaidSoQuotesApi.QuoteImagesApi();
let id = "id_example"; // String | Font ID
apiInstance.quoteImageBackgroundDelete(id, (error, data, response) => {
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
 **id** | **String**| Font ID | 

### Return type

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/xml, application/json


## quoteImageBackgroundListGet

> quoteImageBackgroundListGet(opts)



Lists background images in your private collection.  

### Example

```javascript
import TheySaidSoQuotesApi from 'they_said_so_quotes_api';
let defaultClient = TheySaidSoQuotesApi.ApiClient.instance;
// Configure Bearer (bearer token) access token for authorization: BearerAuth
let BearerAuth = defaultClient.authentications['BearerAuth'];
BearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TheySaidSoQuotesApi.QuoteImagesApi();
let opts = {
  'start': 56 // Number | Response is paged. This parameter determines where the response should start.
};
apiInstance.quoteImageBackgroundListGet(opts, (error, data, response) => {
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
 **start** | **Number**| Response is paged. This parameter determines where the response should start. | [optional] 

### Return type

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## quoteImageBackgroundPost

> quoteImageBackgroundPost(image, opts)



Add an image for use later as a quote background image.

### Example

```javascript
import TheySaidSoQuotesApi from 'they_said_so_quotes_api';
let defaultClient = TheySaidSoQuotesApi.ApiClient.instance;
// Configure Bearer (bearer token) access token for authorization: BearerAuth
let BearerAuth = defaultClient.authentications['BearerAuth'];
BearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TheySaidSoQuotesApi.QuoteImagesApi();
let image = "/path/to/file"; // File | Image file to add to your collection (png/jpg/gif are supported)
let opts = {
  'tags': "tags_example" // String | Optional comma separated tags
};
apiInstance.quoteImageBackgroundPost(image, opts, (error, data, response) => {
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
 **image** | **File**| Image file to add to your collection (png/jpg/gif are supported) | 
 **tags** | **String**| Optional comma separated tags | [optional] 

### Return type

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## quoteImageBackgroundSearchGet

> quoteImageBackgroundSearchGet(opts)



Searches for a background image with a given tag.  

### Example

```javascript
import TheySaidSoQuotesApi from 'they_said_so_quotes_api';
let defaultClient = TheySaidSoQuotesApi.ApiClient.instance;
// Configure Bearer (bearer token) access token for authorization: BearerAuth
let BearerAuth = defaultClient.authentications['BearerAuth'];
BearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TheySaidSoQuotesApi.QuoteImagesApi();
let opts = {
  'query': "query_example" // String | Tag string
};
apiInstance.quoteImageBackgroundSearchGet(opts, (error, data, response) => {
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
 **query** | **String**| Tag string | [optional] 

### Return type

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## quoteImageBackgroundTagsAddPost

> quoteImageBackgroundTagsAddPost(id, tags)



Add a tag to a given Image.

### Example

```javascript
import TheySaidSoQuotesApi from 'they_said_so_quotes_api';
let defaultClient = TheySaidSoQuotesApi.ApiClient.instance;
// Configure Bearer (bearer token) access token for authorization: BearerAuth
let BearerAuth = defaultClient.authentications['BearerAuth'];
BearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TheySaidSoQuotesApi.QuoteImagesApi();
let id = "id_example"; // String | Image ID
let tags = "tags_example"; // String | Comma Separated tags
apiInstance.quoteImageBackgroundTagsAddPost(id, tags, (error, data, response) => {
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
 **id** | **String**| Image ID | 
 **tags** | **String**| Comma Separated tags | 

### Return type

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## quoteImageBackgroundTagsRemovePost

> quoteImageBackgroundTagsRemovePost(id, tags)



Remove a tag from a given Image.

### Example

```javascript
import TheySaidSoQuotesApi from 'they_said_so_quotes_api';
let defaultClient = TheySaidSoQuotesApi.ApiClient.instance;
// Configure Bearer (bearer token) access token for authorization: BearerAuth
let BearerAuth = defaultClient.authentications['BearerAuth'];
BearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TheySaidSoQuotesApi.QuoteImagesApi();
let id = "id_example"; // String | Image ID
let tags = "tags_example"; // String | Comma Separated tags
apiInstance.quoteImageBackgroundTagsRemovePost(id, tags, (error, data, response) => {
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
 **id** | **String**| Image ID | 
 **tags** | **String**| Comma Separated tags | 

### Return type

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## quoteImageDelete

> quoteImageDelete(id)



Delete a quote image. The user needs to be the owner of the quote image to be able to delete it. 

### Example

```javascript
import TheySaidSoQuotesApi from 'they_said_so_quotes_api';
let defaultClient = TheySaidSoQuotesApi.ApiClient.instance;
// Configure Bearer (bearer token) access token for authorization: BearerAuth
let BearerAuth = defaultClient.authentications['BearerAuth'];
BearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TheySaidSoQuotesApi.QuoteImagesApi();
let id = "id_example"; // String | Quote Image ID
apiInstance.quoteImageDelete(id, (error, data, response) => {
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
 **id** | **String**| Quote Image ID | 

### Return type

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/xml, application/json


## quoteImageFontDelete

> quoteImageFontDelete(id)



Delete a font file. The user needs to be the owner of the font to be able to delete it. 

### Example

```javascript
import TheySaidSoQuotesApi from 'they_said_so_quotes_api';
let defaultClient = TheySaidSoQuotesApi.ApiClient.instance;
// Configure Bearer (bearer token) access token for authorization: BearerAuth
let BearerAuth = defaultClient.authentications['BearerAuth'];
BearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TheySaidSoQuotesApi.QuoteImagesApi();
let id = "id_example"; // String | Font ID
apiInstance.quoteImageFontDelete(id, (error, data, response) => {
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
 **id** | **String**| Font ID | 

### Return type

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/xml, application/json


## quoteImageFontListGet

> quoteImageFontListGet(opts)



Lists background images in your private collection.  

### Example

```javascript
import TheySaidSoQuotesApi from 'they_said_so_quotes_api';
let defaultClient = TheySaidSoQuotesApi.ApiClient.instance;
// Configure Bearer (bearer token) access token for authorization: BearerAuth
let BearerAuth = defaultClient.authentications['BearerAuth'];
BearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TheySaidSoQuotesApi.QuoteImagesApi();
let opts = {
  'start': 56 // Number | Response is paged. This parameter determines where the response should start.
};
apiInstance.quoteImageFontListGet(opts, (error, data, response) => {
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
 **start** | **Number**| Response is paged. This parameter determines where the response should start. | [optional] 

### Return type

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## quoteImageFontPost

> quoteImageFontPost(font, opts)



Add a font file for use later in creating a quote image. This is essentially a &#x60;PUT&#x60; but not many clients handle PUT with binary stream i.e. a file, gracefully.

### Example

```javascript
import TheySaidSoQuotesApi from 'they_said_so_quotes_api';
let defaultClient = TheySaidSoQuotesApi.ApiClient.instance;
// Configure Bearer (bearer token) access token for authorization: BearerAuth
let BearerAuth = defaultClient.authentications['BearerAuth'];
BearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TheySaidSoQuotesApi.QuoteImagesApi();
let font = "/path/to/file"; // File | Font file to add to your collection (ttf/otf are supported)
let opts = {
  'tags': "tags_example" // String | Optional comma separated tags
};
apiInstance.quoteImageFontPost(font, opts, (error, data, response) => {
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
 **font** | **File**| Font file to add to your collection (ttf/otf are supported) | 
 **tags** | **String**| Optional comma separated tags | [optional] 

### Return type

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## quoteImageFontSearchGet

> quoteImageFontSearchGet(opts)



Searches for a font with a given tag.  

### Example

```javascript
import TheySaidSoQuotesApi from 'they_said_so_quotes_api';
let defaultClient = TheySaidSoQuotesApi.ApiClient.instance;
// Configure Bearer (bearer token) access token for authorization: BearerAuth
let BearerAuth = defaultClient.authentications['BearerAuth'];
BearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TheySaidSoQuotesApi.QuoteImagesApi();
let opts = {
  'query': "query_example" // String | Tag string
};
apiInstance.quoteImageFontSearchGet(opts, (error, data, response) => {
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
 **query** | **String**| Tag string | [optional] 

### Return type

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## quoteImageFontTagsAddPost

> quoteImageFontTagsAddPost(id, tags)



Add a tag to a given font.

### Example

```javascript
import TheySaidSoQuotesApi from 'they_said_so_quotes_api';
let defaultClient = TheySaidSoQuotesApi.ApiClient.instance;
// Configure Bearer (bearer token) access token for authorization: BearerAuth
let BearerAuth = defaultClient.authentications['BearerAuth'];
BearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TheySaidSoQuotesApi.QuoteImagesApi();
let id = "id_example"; // String | Font ID
let tags = "tags_example"; // String | Comma Separated tags
apiInstance.quoteImageFontTagsAddPost(id, tags, (error, data, response) => {
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
 **id** | **String**| Font ID | 
 **tags** | **String**| Comma Separated tags | 

### Return type

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## quoteImageFontTagsRemovePost

> quoteImageFontTagsRemovePost(id, tags)



Remove a tag from a given Font.

### Example

```javascript
import TheySaidSoQuotesApi from 'they_said_so_quotes_api';
let defaultClient = TheySaidSoQuotesApi.ApiClient.instance;
// Configure Bearer (bearer token) access token for authorization: BearerAuth
let BearerAuth = defaultClient.authentications['BearerAuth'];
BearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TheySaidSoQuotesApi.QuoteImagesApi();
let id = "id_example"; // String | Font ID
let tags = "tags_example"; // String | Comma Separated tags
apiInstance.quoteImageFontTagsRemovePost(id, tags, (error, data, response) => {
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
 **id** | **String**| Font ID | 
 **tags** | **String**| Comma Separated tags | 

### Return type

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## quoteImageGet

> quoteImageGet(id, opts)



Gets a Quote image for a given id. Response can be an image file as a binary or a base64 encoded contents wrapped in json. &#x60;TODO&#x60; 

### Example

```javascript
import TheySaidSoQuotesApi from 'they_said_so_quotes_api';
let defaultClient = TheySaidSoQuotesApi.ApiClient.instance;
// Configure Bearer (bearer token) access token for authorization: BearerAuth
let BearerAuth = defaultClient.authentications['BearerAuth'];
BearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TheySaidSoQuotesApi.QuoteImagesApi();
let id = "id_example"; // String | Quote Image id
let opts = {
  'binary': true // Boolean | Should the response be a direct file download of the image or a base64 encoded image file wrapped in json?
};
apiInstance.quoteImageGet(id, opts, (error, data, response) => {
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
 **id** | **String**| Quote Image id | 
 **binary** | **Boolean**| Should the response be a direct file download of the image or a base64 encoded image file wrapped in json? | [optional] [default to true]

### Return type

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## quoteImagePut

> quoteImagePut(quoteId, opts)



Create a new quote image for a given quote. Choose background colors/images , choose different font styles and generate a beautiful quote image. Did you just had a feeling of being a god or what?! 

### Example

```javascript
import TheySaidSoQuotesApi from 'they_said_so_quotes_api';
let defaultClient = TheySaidSoQuotesApi.ApiClient.instance;
// Configure Bearer (bearer token) access token for authorization: BearerAuth
let BearerAuth = defaultClient.authentications['BearerAuth'];
BearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TheySaidSoQuotesApi.QuoteImagesApi();
let quoteId = "quoteId_example"; // String | Quote id
let opts = {
  'bgimageId': "'theysaidso_default_background_image'", // String | Background Image id ( Will override bgcolor if supplied)
  'bgColor': "bgColor_example", // String | Background Color(if background image id is not supplied)
  'fontId': "'theysaidso_default_font'", // String | Font id
  'textColor': "textColor_example", // String | Text Color
  'textSize': "textSize_example", // String | Text/font size
  'halign': "'center'", // String | Horizontal text Alignment Value
  'valign': "'center'", // String | Vertical text Alignment Value
  'width': 56, // Number | Image Width(By default this takes the width of the background image)
  'height': 56, // Number | Image Height(By default this takes the height of the background image)
  'branding': false, // Boolean | Disable They Said So branding (Only available in certain subscription levels. Ignored in other levels)
  'includeTransparentLayer': true // Boolean | Should include a transparent layer between the text and the background image? This helps when the background image is bright and obscures the text.
};
apiInstance.quoteImagePut(quoteId, opts, (error, data, response) => {
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
 **quoteId** | **String**| Quote id | 
 **bgimageId** | **String**| Background Image id ( Will override bgcolor if supplied) | [optional] [default to &#39;theysaidso_default_background_image&#39;]
 **bgColor** | **String**| Background Color(if background image id is not supplied) | [optional] 
 **fontId** | **String**| Font id | [optional] [default to &#39;theysaidso_default_font&#39;]
 **textColor** | **String**| Text Color | [optional] 
 **textSize** | **String**| Text/font size | [optional] 
 **halign** | **String**| Horizontal text Alignment Value | [optional] [default to &#39;center&#39;]
 **valign** | **String**| Vertical text Alignment Value | [optional] [default to &#39;center&#39;]
 **width** | **Number**| Image Width(By default this takes the width of the background image) | [optional] 
 **height** | **Number**| Image Height(By default this takes the height of the background image) | [optional] 
 **branding** | **Boolean**| Disable They Said So branding (Only available in certain subscription levels. Ignored in other levels) | [optional] [default to false]
 **includeTransparentLayer** | **Boolean**| Should include a transparent layer between the text and the background image? This helps when the background image is bright and obscures the text. | [optional] [default to true]

### Return type

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## quoteImageSearchGet

> quoteImageSearchGet(opts)



Gets a Random Quote image. Optional &#x60;category&#x60; param determines the category of quote used in the image. Optional &#x60;author&#x60; param gets the quote image of a given author.  

### Example

```javascript
import TheySaidSoQuotesApi from 'they_said_so_quotes_api';
let defaultClient = TheySaidSoQuotesApi.ApiClient.instance;
// Configure Bearer (bearer token) access token for authorization: BearerAuth
let BearerAuth = defaultClient.authentications['BearerAuth'];
BearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TheySaidSoQuotesApi.QuoteImagesApi();
let opts = {
  'category': "category_example", // String | Quote Category
  'author': "author_example", // String | Quote Author
  '_private': false // Boolean | Should search private collection. Default searches public image collection.
};
apiInstance.quoteImageSearchGet(opts, (error, data, response) => {
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
 **category** | **String**| Quote Category | [optional] 
 **author** | **String**| Quote Author | [optional] 
 **_private** | **Boolean**| Should search private collection. Default searches public image collection. | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

