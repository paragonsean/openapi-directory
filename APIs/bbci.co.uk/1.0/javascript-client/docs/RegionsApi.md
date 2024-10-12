# BbcIPlayerBusinessLayer.RegionsApi

All URIs are relative to *https://ibl.api.bbci.co.uk/ibl/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getRegions**](RegionsApi.md#getRegions) | **GET** /regions | List all regions



## getRegions

> Object getRegions(lang)

List all regions

Get the list of all the regions TV &amp; iPlayer.

### Example

```javascript
import BbcIPlayerBusinessLayer from 'bbc_i_player_business_layer';

let apiInstance = new BbcIPlayerBusinessLayer.RegionsApi();
let lang = "lang_example"; // String | The language for any applicable localised strings.
apiInstance.getRegions(lang, (error, data, response) => {
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
 **lang** | **String**| The language for any applicable localised strings. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

