# RadioMusicServices.ExperienceApi

All URIs are relative to *https://rms.api.bbc.co.uk*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getExperienceHomepage**](ExperienceApi.md#getExperienceHomepage) | **GET** /experience/homepage | Homepage Experience



## getExperienceHomepage

> ExperienceResponse getExperienceHomepage(xAPIKey)

Homepage Experience

Homepage Experience 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.ExperienceApi();
let xAPIKey = "xAPIKey_example"; // String | API_KEY
apiInstance.getExperienceHomepage(xAPIKey, (error, data, response) => {
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
 **xAPIKey** | **String**| API_KEY | 

### Return type

[**ExperienceResponse**](ExperienceResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

