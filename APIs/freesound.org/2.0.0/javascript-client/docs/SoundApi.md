# Freesound.SoundApi

All URIs are relative to *http://www.freesound.org/apiv2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSoundById**](SoundApi.md#getSoundById) | **GET** /sounds/{soundId} | Details of a sound



## getSoundById

> Sound getSoundById(soundId)

Details of a sound

This resource allows the retrieval of detailed information about a sound.

### Example

```javascript
import Freesound from 'freesound';

let apiInstance = new Freesound.SoundApi();
let soundId = 789; // Number | ID of the sound that needs to be fetched
apiInstance.getSoundById(soundId, (error, data, response) => {
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
 **soundId** | **Number**| ID of the sound that needs to be fetched | 

### Return type

[**Sound**](Sound.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/xml, application/json

