# LetMcApiV2FreeTier1.PhotoControllerApi

All URIs are relative to *https://live-api.letmc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**photoControllerGetPhotoDownload**](PhotoControllerApi.md#photoControllerGetPhotoDownload) | **GET** /v2/tier1/{shortName}/photos/photo/{photoID}/download | Downloads the photo of a property given the property and photo ID.
[**v2Tier1ShortNamePhotoPhotosGet**](PhotoControllerApi.md#v2Tier1ShortNamePhotoPhotosGet) | **GET** /v2/tier1/{shortName}/photo/photos | A collection of all photos in the company
[**v2Tier1ShortNamePhotoPhotosPhotoIDGet**](PhotoControllerApi.md#v2Tier1ShortNamePhotoPhotosPhotoIDGet) | **GET** /v2/tier1/{shortName}/photo/photos/{photoID} | Get a specific photo given its unique Object ID (OID)



## photoControllerGetPhotoDownload

> Object photoControllerGetPhotoDownload(shortName, photoID, opts)

Downloads the photo of a property given the property and photo ID.

### Example

```javascript
import LetMcApiV2FreeTier1 from 'let_mc_api_v2_free__tier_1';

let apiInstance = new LetMcApiV2FreeTier1.PhotoControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let photoID = "photoID_example"; // String | The unique ID of the photo on the property
let opts = {
  'width': 56, // Number | An optional parameter specifying the image width
  'height': 56 // Number | An optional parameter specifying the image height
};
apiInstance.photoControllerGetPhotoDownload(shortName, photoID, opts, (error, data, response) => {
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
 **shortName** | **String**| The unique client short-name | 
 **photoID** | **String**| The unique ID of the photo on the property | 
 **width** | **Number**| An optional parameter specifying the image width | [optional] 
 **height** | **Number**| An optional parameter specifying the image height | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## v2Tier1ShortNamePhotoPhotosGet

> PhotoModelResults v2Tier1ShortNamePhotoPhotosGet(shortName, offset, count)

A collection of all photos in the company

### Example

```javascript
import LetMcApiV2FreeTier1 from 'let_mc_api_v2_free__tier_1';

let apiInstance = new LetMcApiV2FreeTier1.PhotoControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let offset = 56; // Number | The index of the first item to return
let count = 56; // Number | The maximum number of items to return (up to 1000 per request)
apiInstance.v2Tier1ShortNamePhotoPhotosGet(shortName, offset, count, (error, data, response) => {
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
 **shortName** | **String**| The unique client short-name | 
 **offset** | **Number**| The index of the first item to return | 
 **count** | **Number**| The maximum number of items to return (up to 1000 per request) | 

### Return type

[**PhotoModelResults**](PhotoModelResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## v2Tier1ShortNamePhotoPhotosPhotoIDGet

> PhotoModel v2Tier1ShortNamePhotoPhotosPhotoIDGet(shortName, photoID)

Get a specific photo given its unique Object ID (OID)

### Example

```javascript
import LetMcApiV2FreeTier1 from 'let_mc_api_v2_free__tier_1';

let apiInstance = new LetMcApiV2FreeTier1.PhotoControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let photoID = "photoID_example"; // String | The unique ID of the Photo
apiInstance.v2Tier1ShortNamePhotoPhotosPhotoIDGet(shortName, photoID, (error, data, response) => {
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
 **shortName** | **String**| The unique client short-name | 
 **photoID** | **String**| The unique ID of the Photo | 

### Return type

[**PhotoModel**](PhotoModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml

