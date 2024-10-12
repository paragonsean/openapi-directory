# BbcIPlayerBusinessLayer.ProgrammesTLEOsApi

All URIs are relative to *https://ibl.api.bbci.co.uk/ibl/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getBroadcastsByChannel**](ProgrammesTLEOsApi.md#getBroadcastsByChannel) | **GET** /channels/{channel}/broadcasts | Get broadcasts by channel
[**getHighlightsByCategory**](ProgrammesTLEOsApi.md#getHighlightsByCategory) | **GET** /categories/{category}/highlights | List the highlights for a category.
[**getProgrammeHighlights**](ProgrammesTLEOsApi.md#getProgrammeHighlights) | **GET** /home/highlights | Get programme highlights
[**getProgrammesByCategory**](ProgrammesTLEOsApi.md#getProgrammesByCategory) | **GET** /categories/{category}/programmes | List all the programmes for a category.
[**getProgrammesByChannel**](ProgrammesTLEOsApi.md#getProgrammesByChannel) | **GET** /channels/{channel}/programmes | Get programmes by channel
[**getProgrammesByParentPID**](ProgrammesTLEOsApi.md#getProgrammesByParentPID) | **GET** /programmes/{pid} | Programme for a given pid.



## getBroadcastsByChannel

> Object getBroadcastsByChannel(channel, lang, rights, availability, perPage, opts)

Get broadcasts by channel

Get broadcasts by channel

### Example

```javascript
import BbcIPlayerBusinessLayer from 'bbc_i_player_business_layer';

let apiInstance = new BbcIPlayerBusinessLayer.ProgrammesTLEOsApi();
let channel = "channel_example"; // String | The channel identifier to limit results to.
let lang = "lang_example"; // String | The language for any applicable localised strings.
let rights = "'web'"; // String | The rights group to limit results to.
let availability = "'available'"; // String | Whether to return all, or available programmes
let perPage = 789; // Number | The number of results to return.
let opts = {
  'mixin': ["null"], // [String] | Request additional data in the output
  'from': "from_example" // String | Time to return results from, e.g. -3h
};
apiInstance.getBroadcastsByChannel(channel, lang, rights, availability, perPage, opts, (error, data, response) => {
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
 **channel** | **String**| The channel identifier to limit results to. | 
 **lang** | **String**| The language for any applicable localised strings. | 
 **rights** | **String**| The rights group to limit results to. | [default to &#39;web&#39;]
 **availability** | **String**| Whether to return all, or available programmes | [default to &#39;available&#39;]
 **perPage** | **Number**| The number of results to return. | 
 **mixin** | [**[String]**](String.md)| Request additional data in the output | [optional] 
 **from** | **String**| Time to return results from, e.g. -3h | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getHighlightsByCategory

> Object getHighlightsByCategory(category, lang, rights, availability, opts)

List the highlights for a category.

Get the editorial highlights of a given category in TV &amp; iPlayer.

### Example

```javascript
import BbcIPlayerBusinessLayer from 'bbc_i_player_business_layer';

let apiInstance = new BbcIPlayerBusinessLayer.ProgrammesTLEOsApi();
let category = "category_example"; // String | The category identifier to return results from.
let lang = "lang_example"; // String | The language for any applicable localised strings.
let rights = "'web'"; // String | The rights group to limit results to.
let availability = "'available'"; // String | Whether to return all, or available programmes
let opts = {
  'mixin': ["null"] // [String] | Request additional data in the output
};
apiInstance.getHighlightsByCategory(category, lang, rights, availability, opts, (error, data, response) => {
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
 **category** | **String**| The category identifier to return results from. | 
 **lang** | **String**| The language for any applicable localised strings. | 
 **rights** | **String**| The rights group to limit results to. | [default to &#39;web&#39;]
 **availability** | **String**| Whether to return all, or available programmes | [default to &#39;available&#39;]
 **mixin** | [**[String]**](String.md)| Request additional data in the output | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProgrammeHighlights

> Object getProgrammeHighlights(lang, rights, availability, opts)

Get programme highlights

Get programme highlights

### Example

```javascript
import BbcIPlayerBusinessLayer from 'bbc_i_player_business_layer';

let apiInstance = new BbcIPlayerBusinessLayer.ProgrammesTLEOsApi();
let lang = "lang_example"; // String | The language for any applicable localised strings.
let rights = "'web'"; // String | The rights group to limit results to.
let availability = "'available'"; // String | Whether to return all, or available programmes
let opts = {
  'mixin': ["null"] // [String] | Request additional data in the output
};
apiInstance.getProgrammeHighlights(lang, rights, availability, opts, (error, data, response) => {
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
 **rights** | **String**| The rights group to limit results to. | [default to &#39;web&#39;]
 **availability** | **String**| Whether to return all, or available programmes | [default to &#39;available&#39;]
 **mixin** | [**[String]**](String.md)| Request additional data in the output | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProgrammesByCategory

> Object getProgrammesByCategory(category, lang, rights, availability, page, perPage)

List all the programmes for a category.

Get the list of all the Programmes (TLEOs) for a given category in TV &amp; iPlayer.

### Example

```javascript
import BbcIPlayerBusinessLayer from 'bbc_i_player_business_layer';

let apiInstance = new BbcIPlayerBusinessLayer.ProgrammesTLEOsApi();
let category = "category_example"; // String | The category identifier to return results from.
let lang = "lang_example"; // String | The language for any applicable localised strings.
let rights = "'web'"; // String | The rights group to limit results to.
let availability = "'available'"; // String | Whether to return all, or available programmes
let page = 789; // Number | The page index.
let perPage = 789; // Number | The number of results to return.
apiInstance.getProgrammesByCategory(category, lang, rights, availability, page, perPage, (error, data, response) => {
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
 **category** | **String**| The category identifier to return results from. | 
 **lang** | **String**| The language for any applicable localised strings. | 
 **rights** | **String**| The rights group to limit results to. | [default to &#39;web&#39;]
 **availability** | **String**| Whether to return all, or available programmes | [default to &#39;available&#39;]
 **page** | **Number**| The page index. | 
 **perPage** | **Number**| The number of results to return. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProgrammesByChannel

> Object getProgrammesByChannel(channel, lang, rights, availability, page, perPage)

Get programmes by channel

Get programmes by channel

### Example

```javascript
import BbcIPlayerBusinessLayer from 'bbc_i_player_business_layer';

let apiInstance = new BbcIPlayerBusinessLayer.ProgrammesTLEOsApi();
let channel = "channel_example"; // String | The channel identifier to limit results to.
let lang = "lang_example"; // String | The language for any applicable localised strings.
let rights = "'web'"; // String | The rights group to limit results to.
let availability = "'available'"; // String | Whether to return all, or available programmes
let page = 789; // Number | The page index.
let perPage = 789; // Number | The number of results to return.
apiInstance.getProgrammesByChannel(channel, lang, rights, availability, page, perPage, (error, data, response) => {
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
 **channel** | **String**| The channel identifier to limit results to. | 
 **lang** | **String**| The language for any applicable localised strings. | 
 **rights** | **String**| The rights group to limit results to. | [default to &#39;web&#39;]
 **availability** | **String**| Whether to return all, or available programmes | [default to &#39;available&#39;]
 **page** | **Number**| The page index. | 
 **perPage** | **Number**| The number of results to return. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProgrammesByParentPID

> Object getProgrammesByParentPID(pid, rights, availability, initialChildCount)

Programme for a given pid.

Get the programme for a given programme identifier.

### Example

```javascript
import BbcIPlayerBusinessLayer from 'bbc_i_player_business_layer';

let apiInstance = new BbcIPlayerBusinessLayer.ProgrammesTLEOsApi();
let pid = "pid_example"; // String | The programme identifier.
let rights = "'web'"; // String | The rights group to limit results to.
let availability = "'available'"; // String | Whether to return all, or available programmes
let initialChildCount = 4; // Number | The depth to return child entities.
apiInstance.getProgrammesByParentPID(pid, rights, availability, initialChildCount, (error, data, response) => {
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
 **pid** | **String**| The programme identifier. | 
 **rights** | **String**| The rights group to limit results to. | [default to &#39;web&#39;]
 **availability** | **String**| Whether to return all, or available programmes | [default to &#39;available&#39;]
 **initialChildCount** | **Number**| The depth to return child entities. | [default to 4]

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

