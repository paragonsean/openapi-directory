# VisageCloud.AnalysisApi

All URIs are relative to *https://visagecloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**compareFacesUsingGET**](AnalysisApi.md#compareFacesUsingGET) | **GET** /rest/v1.1/analysis/compare | Compare several faces identified by faceHash, without depending on mapping faces to profiles
[**performAnalysisUsingPOST**](AnalysisApi.md#performAnalysisUsingPOST) | **POST** /rest/v1.1/analysis/detection | Perform detection on a given picture or picture URL
[**performRecognitionUsingPOST**](AnalysisApi.md#performRecognitionUsingPOST) | **POST** /rest/v1.1/analysis/recognition | Perform labeled recognition on a given picture or picture URL
[**retrieveAnalysisUsingGET**](AnalysisApi.md#retrieveAnalysisUsingGET) | **GET** /rest/v1.1/analysis/retrieve | Retrieve a complete analysis object including both detection and recognition information
[**retriveLatestUsingGET**](AnalysisApi.md#retriveLatestUsingGET) | **GET** /rest/v1.1/analysis/listLatest | Retrieve the last *count* operations per current account



## compareFacesUsingGET

> RestResponse compareFacesUsingGET(accessKey, secretKey, faceHashes, opts)

Compare several faces identified by faceHash, without depending on mapping faces to profiles

### Example

```javascript
import VisageCloud from 'visage_cloud';

let apiInstance = new VisageCloud.AnalysisApi();
let accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
let secretKey = "secretKey_example"; // String | The secretKey or readOnlyKey provided by VisageCloud
let faceHashes = ["null"]; // [String] | The IDs of the faces which you want compared, comma-separated
let opts = {
  'showDetails': false // Boolean | Show details
};
apiInstance.compareFacesUsingGET(accessKey, secretKey, faceHashes, opts, (error, data, response) => {
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
 **accessKey** | **String**| The accessKey provided by VisageCloud | 
 **secretKey** | **String**| The secretKey or readOnlyKey provided by VisageCloud | 
 **faceHashes** | [**[String]**](String.md)| The IDs of the faces which you want compared, comma-separated | 
 **showDetails** | **Boolean**| Show details | [optional] [default to false]

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## performAnalysisUsingPOST

> RestResponse performAnalysisUsingPOST(accessKey, secretKey, opts)

Perform detection on a given picture or picture URL

### Example

```javascript
import VisageCloud from 'visage_cloud';

let apiInstance = new VisageCloud.AnalysisApi();
let accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
let secretKey = "secretKey_example"; // String | The secretKey or readOnlyKey provided by VisageCloud
let opts = {
  'storeAnalysisPicture': true, // Boolean | Boolean value indicating whether you want the picture of the analysis to be stored for later retrieval
  'storeFacePictures': true, // Boolean | Boolean value indicating whether you want the faces inside the picture to be stored for later retrieval
  'storeResult': true, // Boolean | Boolean value indicating whether you want the result of the analysis to be stored
  'retentionTime': 56, // Number | How many seconds the results should be retained in stoarage?
  'pictureURL': "pictureURL_example", // String | The URL of the picture, assuming it is served by a third party server. Server should be accesible from the Internet or through another netwoek by VisageCloud infrastructure
  'algorithmVersion': "'V2'", // String | Algorithm version (V2 is more performant but not backward compatible)
  'autoRotate': false, // Boolean | Auto-rotate to find flipped or rotate faces
  'skipEXIF': false, // Boolean | Skip EXIF rotation procesing
  'waitForPictureUpload': false, // Boolean | Waits until the picture is successfully uploaded, before returning the response back the the client
  'filters': ["null"], // [String] | [For advanced users only] Change feature filters for robustness of feature extraction. Tweaking this parameter may affect per
  'options': "options_example", // String | [For advanced users only] Options for preprocessing of image.
  'picture': "picture_example" // String | The multipart/form-data version of the image, in case a direct upload is used. At least one of picture or pictureURL must be present
};
apiInstance.performAnalysisUsingPOST(accessKey, secretKey, opts, (error, data, response) => {
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
 **accessKey** | **String**| The accessKey provided by VisageCloud | 
 **secretKey** | **String**| The secretKey or readOnlyKey provided by VisageCloud | 
 **storeAnalysisPicture** | **Boolean**| Boolean value indicating whether you want the picture of the analysis to be stored for later retrieval | [optional] [default to true]
 **storeFacePictures** | **Boolean**| Boolean value indicating whether you want the faces inside the picture to be stored for later retrieval | [optional] [default to true]
 **storeResult** | **Boolean**| Boolean value indicating whether you want the result of the analysis to be stored | [optional] [default to true]
 **retentionTime** | **Number**| How many seconds the results should be retained in stoarage? | [optional] 
 **pictureURL** | **String**| The URL of the picture, assuming it is served by a third party server. Server should be accesible from the Internet or through another netwoek by VisageCloud infrastructure | [optional] 
 **algorithmVersion** | **String**| Algorithm version (V2 is more performant but not backward compatible) | [optional] [default to &#39;V2&#39;]
 **autoRotate** | **Boolean**| Auto-rotate to find flipped or rotate faces | [optional] [default to false]
 **skipEXIF** | **Boolean**| Skip EXIF rotation procesing | [optional] [default to false]
 **waitForPictureUpload** | **Boolean**| Waits until the picture is successfully uploaded, before returning the response back the the client | [optional] [default to false]
 **filters** | [**[String]**](String.md)| [For advanced users only] Change feature filters for robustness of feature extraction. Tweaking this parameter may affect per | [optional] 
 **options** | **String**| [For advanced users only] Options for preprocessing of image. | [optional] 
 **picture** | **String**| The multipart/form-data version of the image, in case a direct upload is used. At least one of picture or pictureURL must be present | [optional] 

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## performRecognitionUsingPOST

> RestResponse performRecognitionUsingPOST(accessKey, secretKey, collectionId, opts)

Perform labeled recognition on a given picture or picture URL

### Example

```javascript
import VisageCloud from 'visage_cloud';

let apiInstance = new VisageCloud.AnalysisApi();
let accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
let secretKey = "secretKey_example"; // String | The secretKey or readOnlyKey provided by VisageCloud
let collectionId = "collectionId_example"; // String | Uniquely identified collection that can store multiple profiles
let opts = {
  'storeAnalysisPicture': true, // Boolean | Boolean value indicating whether you want the picture of the analysis to be stored for later retrieval
  'storeFacePictures': true, // Boolean | Boolean value indicating whether you want the faces inside the picture to be stored for later retrieval
  'storeResult': true, // Boolean | Boolean value indicating whether you want the result of the analysis to be stored
  'retentionTime': 56, // Number | How many seconds the results should be retained in stoarage?
  'labels': ["null"], // [String] | Labels associated with the given picture or picture URL
  'attributeFilters': ["null"], // [String] | Filters that will be applied on the recognition operation
  'pictureURL': "pictureURL_example", // String | The URL of the picture
  'algorithmVersion': "'V2'", // String | Algorithm version (V2 is more performant but not backward compatible)
  'autoRotate': false, // Boolean | Auto-rotate to find flipped or rotate faces
  'skipEXIFRotationProcessing': false, // Boolean | Skip EXIF rotation procesing
  'waitForPictureUpload': false, // Boolean | Waits until the picture is successfully uploaded, before returning the response back the the client
  'filters': ["null"], // [String] | [For advanced users only] Change feature filters for robustness of feature extraction. Tweaking this parameter may affect per
  'options': "options_example", // String | [For advanced users only] Options for preprocessing of image.
  'picture': "picture_example" // String | The picture itself
};
apiInstance.performRecognitionUsingPOST(accessKey, secretKey, collectionId, opts, (error, data, response) => {
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
 **accessKey** | **String**| The accessKey provided by VisageCloud | 
 **secretKey** | **String**| The secretKey or readOnlyKey provided by VisageCloud | 
 **collectionId** | **String**| Uniquely identified collection that can store multiple profiles | 
 **storeAnalysisPicture** | **Boolean**| Boolean value indicating whether you want the picture of the analysis to be stored for later retrieval | [optional] [default to true]
 **storeFacePictures** | **Boolean**| Boolean value indicating whether you want the faces inside the picture to be stored for later retrieval | [optional] [default to true]
 **storeResult** | **Boolean**| Boolean value indicating whether you want the result of the analysis to be stored | [optional] [default to true]
 **retentionTime** | **Number**| How many seconds the results should be retained in stoarage? | [optional] 
 **labels** | [**[String]**](String.md)| Labels associated with the given picture or picture URL | [optional] 
 **attributeFilters** | [**[String]**](String.md)| Filters that will be applied on the recognition operation | [optional] 
 **pictureURL** | **String**| The URL of the picture | [optional] 
 **algorithmVersion** | **String**| Algorithm version (V2 is more performant but not backward compatible) | [optional] [default to &#39;V2&#39;]
 **autoRotate** | **Boolean**| Auto-rotate to find flipped or rotate faces | [optional] [default to false]
 **skipEXIFRotationProcessing** | **Boolean**| Skip EXIF rotation procesing | [optional] [default to false]
 **waitForPictureUpload** | **Boolean**| Waits until the picture is successfully uploaded, before returning the response back the the client | [optional] [default to false]
 **filters** | [**[String]**](String.md)| [For advanced users only] Change feature filters for robustness of feature extraction. Tweaking this parameter may affect per | [optional] 
 **options** | **String**| [For advanced users only] Options for preprocessing of image. | [optional] 
 **picture** | **String**| The picture itself | [optional] 

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## retrieveAnalysisUsingGET

> RestResponse retrieveAnalysisUsingGET(accessKey, secretKey, analysisId)

Retrieve a complete analysis object including both detection and recognition information

### Example

```javascript
import VisageCloud from 'visage_cloud';

let apiInstance = new VisageCloud.AnalysisApi();
let accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
let secretKey = "secretKey_example"; // String | The secretKey or readOnlyKey provided by VisageCloud
let analysisId = "analysisId_example"; // String | The ID of the analysis for which the data will be retrieved
apiInstance.retrieveAnalysisUsingGET(accessKey, secretKey, analysisId, (error, data, response) => {
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
 **accessKey** | **String**| The accessKey provided by VisageCloud | 
 **secretKey** | **String**| The secretKey or readOnlyKey provided by VisageCloud | 
 **analysisId** | **String**| The ID of the analysis for which the data will be retrieved | 

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retriveLatestUsingGET

> RestResponse retriveLatestUsingGET(accessKey, secretKey, opts)

Retrieve the last *count* operations per current account

### Example

```javascript
import VisageCloud from 'visage_cloud';

let apiInstance = new VisageCloud.AnalysisApi();
let accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
let secretKey = "secretKey_example"; // String | The secretKey or readOnlyKey provided by VisageCloud
let opts = {
  'count': 100 // Number | How many records to retrieve at a time
};
apiInstance.retriveLatestUsingGET(accessKey, secretKey, opts, (error, data, response) => {
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
 **accessKey** | **String**| The accessKey provided by VisageCloud | 
 **secretKey** | **String**| The secretKey or readOnlyKey provided by VisageCloud | 
 **count** | **Number**| How many records to retrieve at a time | [optional] [default to 100]

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

