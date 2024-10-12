# OpenAlprCarCheckApi.DefaultApi

All URIs are relative to *https://api.openalpr.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getConfig**](DefaultApi.md#getConfig) | **GET** /config | 
[**recognizeBytes**](DefaultApi.md#recognizeBytes) | **POST** /recognize_bytes | 
[**recognizeFile**](DefaultApi.md#recognizeFile) | **POST** /recognize | 
[**recognizeUrl**](DefaultApi.md#recognizeUrl) | **POST** /recognize_url | 



## getConfig

> GetConfig200Response getConfig()



Get a list of available results for plate and vehicle recognition 

### Example

```javascript
import OpenAlprCarCheckApi from 'open_alpr_car_check_api';

let apiInstance = new OpenAlprCarCheckApi.DefaultApi();
apiInstance.getConfig((error, data, response) => {
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

[**GetConfig200Response**](GetConfig200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## recognizeBytes

> RecognizeFile200Response recognizeBytes(secretKey, country, imageBytes, opts)



Send an image for OpenALPR to analyze and provide metadata back The image is sent as base64 encoded bytes. 

### Example

```javascript
import OpenAlprCarCheckApi from 'open_alpr_car_check_api';

let apiInstance = new OpenAlprCarCheckApi.DefaultApi();
let secretKey = "secretKey_example"; // String | The secret key used to authenticate your account.  You can view your  secret key by visiting  https://cloud.openalpr.com/ 
let country = "country_example"; // String | Defines the training data used by OpenALPR.  \"us\" analyzes  North-American style plates.  \"eu\" analyzes European-style plates.  This field is required if using the \"plate\" task 
let imageBytes = "imageBytes_example"; // String | The image file that you wish to analyze encoded in base64 
let opts = {
  'recognizeVehicle': 0, // Number | If set to 1, the vehicle will also be recognized in the image This requires an additional credit per request 
  'returnImage': 0, // Number | If set to 1, the image you uploaded will be encoded in base64 and  sent back along with the response 
  'topn': 10 // Number | The number of results you would like to be returned for plate  candidates and vehicle classifications 
};
apiInstance.recognizeBytes(secretKey, country, imageBytes, opts, (error, data, response) => {
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
 **secretKey** | **String**| The secret key used to authenticate your account.  You can view your  secret key by visiting  https://cloud.openalpr.com/  | 
 **country** | **String**| Defines the training data used by OpenALPR.  \&quot;us\&quot; analyzes  North-American style plates.  \&quot;eu\&quot; analyzes European-style plates.  This field is required if using the \&quot;plate\&quot; task  | 
 **imageBytes** | **String**| The image file that you wish to analyze encoded in base64  | 
 **recognizeVehicle** | **Number**| If set to 1, the vehicle will also be recognized in the image This requires an additional credit per request  | [optional] [default to 0]
 **returnImage** | **Number**| If set to 1, the image you uploaded will be encoded in base64 and  sent back along with the response  | [optional] [default to 0]
 **topn** | **Number**| The number of results you would like to be returned for plate  candidates and vehicle classifications  | [optional] [default to 10]

### Return type

[**RecognizeFile200Response**](RecognizeFile200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## recognizeFile

> RecognizeFile200Response recognizeFile(secretKey, country, image, opts)



Send an image for OpenALPR to analyze and provide metadata back The image is sent as a file using a form data POST 

### Example

```javascript
import OpenAlprCarCheckApi from 'open_alpr_car_check_api';

let apiInstance = new OpenAlprCarCheckApi.DefaultApi();
let secretKey = "secretKey_example"; // String | The secret key used to authenticate your account.  You can view your  secret key by visiting  https://cloud.openalpr.com/ 
let country = "country_example"; // String | Defines the training data used by OpenALPR.  \"us\" analyzes  North-American style plates.  \"eu\" analyzes European-style plates.  This field is required if using the \"plate\" task 
let image = "/path/to/file"; // File | The image file that you wish to analyze 
let opts = {
  'recognizeVehicle': 0, // Number | If set to 1, the vehicle will also be recognized in the image This requires an additional credit per request 
  'returnImage': 0, // Number | If set to 1, the image you uploaded will be encoded in base64 and  sent back along with the response 
  'topn': 10, // Number | The number of results you would like to be returned for plate  candidates and vehicle classifications 
  'isCropped': 0 // Number | When providing a plate or vehicle that is already cropped,   this performs a recognition against the full crop and does not  attempt to localize the plate/vehicle 
};
apiInstance.recognizeFile(secretKey, country, image, opts, (error, data, response) => {
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
 **secretKey** | **String**| The secret key used to authenticate your account.  You can view your  secret key by visiting  https://cloud.openalpr.com/  | 
 **country** | **String**| Defines the training data used by OpenALPR.  \&quot;us\&quot; analyzes  North-American style plates.  \&quot;eu\&quot; analyzes European-style plates.  This field is required if using the \&quot;plate\&quot; task  | 
 **image** | **File**| The image file that you wish to analyze  | 
 **recognizeVehicle** | **Number**| If set to 1, the vehicle will also be recognized in the image This requires an additional credit per request  | [optional] [default to 0]
 **returnImage** | **Number**| If set to 1, the image you uploaded will be encoded in base64 and  sent back along with the response  | [optional] [default to 0]
 **topn** | **Number**| The number of results you would like to be returned for plate  candidates and vehicle classifications  | [optional] [default to 10]
 **isCropped** | **Number**| When providing a plate or vehicle that is already cropped,   this performs a recognition against the full crop and does not  attempt to localize the plate/vehicle  | [optional] [default to 0]

### Return type

[**RecognizeFile200Response**](RecognizeFile200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## recognizeUrl

> RecognizeFile200Response recognizeUrl(imageUrl, secretKey, country, opts)



Send an image for OpenALPR to analyze and provide metadata back The image is sent as a URL.  The OpenALPR service will download the image  and process it 

### Example

```javascript
import OpenAlprCarCheckApi from 'open_alpr_car_check_api';

let apiInstance = new OpenAlprCarCheckApi.DefaultApi();
let imageUrl = "imageUrl_example"; // String | A URL to an image that you wish to analyze 
let secretKey = "secretKey_example"; // String | The secret key used to authenticate your account.  You can view your  secret key by visiting  https://cloud.openalpr.com/ 
let country = "country_example"; // String | Defines the training data used by OpenALPR.  \"us\" analyzes  North-American style plates.  \"eu\" analyzes European-style plates.  This field is required if using the \"plate\" task 
let opts = {
  'recognizeVehicle': 0, // Number | If set to 1, the vehicle will also be recognized in the image This requires an additional credit per request 
  'returnImage': 0, // Number | If set to 1, the image you uploaded will be encoded in base64 and  sent back along with the response 
  'topn': 10 // Number | The number of results you would like to be returned for plate  candidates and vehicle classifications 
};
apiInstance.recognizeUrl(imageUrl, secretKey, country, opts, (error, data, response) => {
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
 **imageUrl** | **String**| A URL to an image that you wish to analyze  | 
 **secretKey** | **String**| The secret key used to authenticate your account.  You can view your  secret key by visiting  https://cloud.openalpr.com/  | 
 **country** | **String**| Defines the training data used by OpenALPR.  \&quot;us\&quot; analyzes  North-American style plates.  \&quot;eu\&quot; analyzes European-style plates.  This field is required if using the \&quot;plate\&quot; task  | 
 **recognizeVehicle** | **Number**| If set to 1, the vehicle will also be recognized in the image This requires an additional credit per request  | [optional] [default to 0]
 **returnImage** | **Number**| If set to 1, the image you uploaded will be encoded in base64 and  sent back along with the response  | [optional] [default to 0]
 **topn** | **Number**| The number of results you would like to be returned for plate  candidates and vehicle classifications  | [optional] [default to 10]

### Return type

[**RecognizeFile200Response**](RecognizeFile200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

