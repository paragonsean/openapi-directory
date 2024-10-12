# HackathonWatch.HackathonsApi

All URIs are relative to *http://www.hackathonwatch.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gETHackathonsComingFormat**](HackathonsApi.md#gETHackathonsComingFormat) | **GET** /hackathons/coming.json | Return a list of coming hackathons
[**gETHackathonsIdFormat**](HackathonsApi.md#gETHackathonsIdFormat) | **GET** /hackathons/{id}.json | Return the detail of a given hackathon



## gETHackathonsComingFormat

> gETHackathonsComingFormat(opts)

Return a list of coming hackathons

### Example

```javascript
import HackathonWatch from 'hackathon_watch';

let apiInstance = new HackathonWatch.HackathonsApi();
let opts = {
  'page': 1 // Number | Specify the page of coming hackathons.
};
apiInstance.gETHackathonsComingFormat(opts, (error, data, response) => {
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
 **page** | **Number**| Specify the page of coming hackathons. | [optional] [default to 1]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## gETHackathonsIdFormat

> gETHackathonsIdFormat(id)

Return the detail of a given hackathon

### Example

```javascript
import HackathonWatch from 'hackathon_watch';

let apiInstance = new HackathonWatch.HackathonsApi();
let id = 56; // Number | ID of the hackathon for detail information
apiInstance.gETHackathonsIdFormat(id, (error, data, response) => {
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
 **id** | **Number**| ID of the hackathon for detail information | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

