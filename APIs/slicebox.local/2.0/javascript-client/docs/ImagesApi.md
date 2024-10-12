# SliceboxApi.ImagesApi

All URIs are relative to *http://slicebox.local/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**imagesDeletePost**](ImagesApi.md#imagesDeletePost) | **POST** /images/delete | 
[**imagesExportGet**](ImagesApi.md#imagesExportGet) | **GET** /images/export | 
[**imagesExportPost**](ImagesApi.md#imagesExportPost) | **POST** /images/export | 
[**imagesIdAnonymizePut_0**](ImagesApi.md#imagesIdAnonymizePut_0) | **PUT** /images/{id}/anonymize | 
[**imagesIdAnonymizedPost_0**](ImagesApi.md#imagesIdAnonymizedPost_0) | **POST** /images/{id}/anonymized | 
[**imagesIdAttributesGet**](ImagesApi.md#imagesIdAttributesGet) | **GET** /images/{id}/attributes | 
[**imagesIdDelete**](ImagesApi.md#imagesIdDelete) | **DELETE** /images/{id} | 
[**imagesIdGet**](ImagesApi.md#imagesIdGet) | **GET** /images/{id} | 
[**imagesIdImageinformationGet**](ImagesApi.md#imagesIdImageinformationGet) | **GET** /images/{id}/imageinformation | 
[**imagesIdModifyPut**](ImagesApi.md#imagesIdModifyPut) | **PUT** /images/{id}/modify | 
[**imagesIdPngGet**](ImagesApi.md#imagesIdPngGet) | **GET** /images/{id}/png | 
[**imagesJpegPost**](ImagesApi.md#imagesJpegPost) | **POST** /images/jpeg | 
[**imagesPost**](ImagesApi.md#imagesPost) | **POST** /images | 



## imagesDeletePost

> imagesDeletePost(imageIDs)



bulk delete a sequence of images according to the supplied image IDs. This is the same as a sequence of DELETE requests to /images/{id}

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.ImagesApi();
let imageIDs = [null]; // [Number] | IDs of images to delete
apiInstance.imagesDeletePost(imageIDs, (error, data, response) => {
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
 **imageIDs** | [**[Number]**](Number.md)| IDs of images to delete | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/octet-stream, multipart/form-data
- **Accept**: Not defined


## imagesExportGet

> imagesExportGet(id)



download the export set with the supplied export set ID as a zip archive

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.ImagesApi();
let id = 789; // Number | ID of export set to download
apiInstance.imagesExportGet(id, (error, data, response) => {
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
 **id** | **Number**| ID of export set to download | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## imagesExportPost

> ExportSetId imagesExportPost(imageIds)



create an export set, a group of image IDs of images to export. The export set will contain the selected images. The export set is available for download 12 hours before it is automatically deleted.

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.ImagesApi();
let imageIds = [null]; // [Number] | ids of images to export
apiInstance.imagesExportPost(imageIds, (error, data, response) => {
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
 **imageIds** | [**[Number]**](Number.md)| ids of images to export | 

### Return type

[**ExportSetId**](ExportSetId.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/octet-stream, multipart/form-data
- **Accept**: application/json, application/octet-stream


## imagesIdAnonymizePut_0

> Image imagesIdAnonymizePut_0(id, tagValues)



delete the selected image and replace it with an anonymized version

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.ImagesApi();
let id = 789; // Number | ID of image to anonymize
let tagValues = new SliceboxApi.AnonymizationData(); // AnonymizationData | specification of values for anonymous DICOM attributes
apiInstance.imagesIdAnonymizePut_0(id, tagValues, (error, data, response) => {
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
 **id** | **Number**| ID of image to anonymize | 
 **tagValues** | [**AnonymizationData**](AnonymizationData.md)| specification of values for anonymous DICOM attributes | 

### Return type

[**Image**](Image.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/octet-stream, multipart/form-data
- **Accept**: application/json, application/octet-stream


## imagesIdAnonymizedPost_0

> imagesIdAnonymizedPost_0(id, tagValues)



get an anonymized version of the image with the supplied ID

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.ImagesApi();
let id = 789; // Number | ID of image for which to get anonymized dataset
let tagValues = new SliceboxApi.AnonymizationData(); // AnonymizationData | specification of values for anonymous DICOM attributes
apiInstance.imagesIdAnonymizedPost_0(id, tagValues, (error, data, response) => {
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
 **id** | **Number**| ID of image for which to get anonymized dataset | 
 **tagValues** | [**AnonymizationData**](AnonymizationData.md)| specification of values for anonymous DICOM attributes | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/octet-stream, multipart/form-data
- **Accept**: Not defined


## imagesIdAttributesGet

> [ImageAttribute] imagesIdAttributesGet(id)



list all DICOM attributes of the dataset corresponding to the supplied image ID

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.ImagesApi();
let id = 789; // Number | ID of image
apiInstance.imagesIdAttributesGet(id, (error, data, response) => {
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
 **id** | **Number**| ID of image | 

### Return type

[**[ImageAttribute]**](ImageAttribute.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/octet-stream


## imagesIdDelete

> imagesIdDelete(id)



Delete the image with the supplied ID

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.ImagesApi();
let id = 789; // Number | ID of image
apiInstance.imagesIdDelete(id, (error, data, response) => {
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
 **id** | **Number**| ID of image | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## imagesIdGet

> imagesIdGet(id)



fetch dataset corresponding to the supplied image ID

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.ImagesApi();
let id = 789; // Number | ID of image
apiInstance.imagesIdGet(id, (error, data, response) => {
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
 **id** | **Number**| ID of image | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## imagesIdImageinformationGet

> ImageInformation imagesIdImageinformationGet(id)



get basic information about the pixel data of an image

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.ImagesApi();
let id = 789; // Number | ID of image
apiInstance.imagesIdImageinformationGet(id, (error, data, response) => {
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
 **id** | **Number**| ID of image | 

### Return type

[**ImageInformation**](ImageInformation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/octet-stream


## imagesIdModifyPut

> imagesIdModifyPut(id, tagPathValueMappings)



modify and/or insert image attributes according to the input tagpath-value mappings

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.ImagesApi();
let id = 789; // Number | ID of image to modify
let tagPathValueMappings = [new SliceboxApi.TagMapping()]; // [TagMapping] | specification of tag paths and corresponding values to insert or modify
apiInstance.imagesIdModifyPut(id, tagPathValueMappings, (error, data, response) => {
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
 **id** | **Number**| ID of image to modify | 
 **tagPathValueMappings** | [**[TagMapping]**](TagMapping.md)| specification of tag paths and corresponding values to insert or modify | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/octet-stream, multipart/form-data
- **Accept**: Not defined


## imagesIdPngGet

> imagesIdPngGet(id, opts)



get a PNG image representation of the image corresponding to the supplied ID

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.ImagesApi();
let id = 789; // Number | ID of image
let opts = {
  'framenumber': 1, // Number | frame/slice to show
  'windowmin': 0, // Number | intensity window minimum value. If not specified or set to zero, windowing will be selected from relevant DICOM attributes
  'windowmax': 0, // Number | intensity window maximum value. If not specified or set to zero, windowing will be selected from relevant DICOM attributes
  'imageheight': 0 // Number | height of PNG image. If not specified or set to zero, the image height will equal that of the data
};
apiInstance.imagesIdPngGet(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of image | 
 **framenumber** | **Number**| frame/slice to show | [optional] [default to 1]
 **windowmin** | **Number**| intensity window minimum value. If not specified or set to zero, windowing will be selected from relevant DICOM attributes | [optional] [default to 0]
 **windowmax** | **Number**| intensity window maximum value. If not specified or set to zero, windowing will be selected from relevant DICOM attributes | [optional] [default to 0]
 **imageheight** | **Number**| height of PNG image. If not specified or set to zero, the image height will equal that of the data | [optional] [default to 0]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## imagesJpegPost

> Image imagesJpegPost(studyid, jpegBytes, opts)



add a JPEG image to slicebox. The image data will be wrapped in a DICOM file and added as a new series belonging to the study with the supplied ID

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.ImagesApi();
let studyid = 789; // Number | ID of study to add new series to
let jpegBytes = {key: null}; // Object | The jpeg image data
let opts = {
  'description': "description_example" // String | DICOM series description of the resulting secondary capture series
};
apiInstance.imagesJpegPost(studyid, jpegBytes, opts, (error, data, response) => {
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
 **studyid** | **Number**| ID of study to add new series to | 
 **jpegBytes** | **Object**| The jpeg image data | 
 **description** | **String**| DICOM series description of the resulting secondary capture series | [optional] 

### Return type

[**Image**](Image.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/octet-stream, multipart/form-data
- **Accept**: application/json, application/octet-stream


## imagesPost

> Image imagesPost(imagesPostRequest)



add a DICOM dataset to slicebox

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.ImagesApi();
let imagesPostRequest = new SliceboxApi.ImagesPostRequest(); // ImagesPostRequest | 
apiInstance.imagesPost(imagesPostRequest, (error, data, response) => {
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
 **imagesPostRequest** | [**ImagesPostRequest**](ImagesPostRequest.md)|  | 

### Return type

[**Image**](Image.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/octet-stream, multipart/form-data
- **Accept**: application/json, application/octet-stream

