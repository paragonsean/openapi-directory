# DaymetSinglePixelExtractionToolApi.DefaultApi

All URIs are relative to *https://daymet.ornl.gov/single-pixel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiDataGet**](DefaultApi.md#apiDataGet) | **GET** /api/data | Download Daymet Data
[**previewGet**](DefaultApi.md#previewGet) | **GET** /preview | Preview Daymet Data in a web browser
[**sendSaveDataGet**](DefaultApi.md#sendSaveDataGet) | **GET** /send/saveData | Download Daymet Data
[**visualizeGet**](DefaultApi.md#visualizeGet) | **GET** /visualize | Visualize Daymet Data in a web browser



## apiDataGet

> apiDataGet(lat, lon, format, opts)

Download Daymet Data

Returns a csv or json of the requested data to local machine

### Example

```javascript
import DaymetSinglePixelExtractionToolApi from 'daymet_single_pixel_extraction_tool_api';

let apiInstance = new DaymetSinglePixelExtractionToolApi.DefaultApi();
let lat = 3.4; // Number | Latitude component of location.
let lon = 3.4; // Number | Longitude component of location.
let format = "format_example"; // String | Specify a format for data retrieval.
let opts = {
  'vars': ["null"], // [String] | Daymet Daily weather estimates.
  'years': ["null"], // [String] | Subset on years [1980..2019].
  'start': new Date("2013-10-20"), // Date | Subset on dates (start date).
  'end': new Date("2013-10-20") // Date | Subset on dates (end date).
};
apiInstance.apiDataGet(lat, lon, format, opts, (error, data, response) => {
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
 **lat** | **Number**| Latitude component of location. | 
 **lon** | **Number**| Longitude component of location. | 
 **format** | **String**| Specify a format for data retrieval. | 
 **vars** | [**[String]**](String.md)| Daymet Daily weather estimates. | [optional] 
 **years** | [**[String]**](String.md)| Subset on years [1980..2019]. | [optional] 
 **start** | **Date**| Subset on dates (start date). | [optional] 
 **end** | **Date**| Subset on dates (end date). | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## previewGet

> previewGet(lat, lon, format, opts)

Preview Daymet Data in a web browser

Returns a table to the browser displaying requested data

### Example

```javascript
import DaymetSinglePixelExtractionToolApi from 'daymet_single_pixel_extraction_tool_api';

let apiInstance = new DaymetSinglePixelExtractionToolApi.DefaultApi();
let lat = 3.4; // Number | Latitude component of location
let lon = 3.4; // Number | Longitude component of location.
let format = "format_example"; // String | Specify a format for data retrieval.
let opts = {
  'vars': ["null"], // [String] | Daymet Daily weather estimates.
  'years': ["null"], // [String] | Subset on years [1980..2019].
  'start': new Date("2013-10-20"), // Date | Subset on dates (start date).
  'end': new Date("2013-10-20") // Date | Subset on dates (end date).
};
apiInstance.previewGet(lat, lon, format, opts, (error, data, response) => {
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
 **lat** | **Number**| Latitude component of location | 
 **lon** | **Number**| Longitude component of location. | 
 **format** | **String**| Specify a format for data retrieval. | 
 **vars** | [**[String]**](String.md)| Daymet Daily weather estimates. | [optional] 
 **years** | [**[String]**](String.md)| Subset on years [1980..2019]. | [optional] 
 **start** | **Date**| Subset on dates (start date). | [optional] 
 **end** | **Date**| Subset on dates (end date). | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## sendSaveDataGet

> sendSaveDataGet(lat, lon, format, opts)

Download Daymet Data

Returns a csv or json of the requested data to local machine

### Example

```javascript
import DaymetSinglePixelExtractionToolApi from 'daymet_single_pixel_extraction_tool_api';

let apiInstance = new DaymetSinglePixelExtractionToolApi.DefaultApi();
let lat = 3.4; // Number | Latitude component of location.
let lon = 3.4; // Number | Longitude component of location.
let format = "format_example"; // String | Specify a format for data retrieval.
let opts = {
  'vars': ["null"], // [String] | Daymet Daily weather estimates.
  'years': ["null"], // [String] | Subset on years [1980..2019].
  'start': new Date("2013-10-20"), // Date | Subset on dates (start date).
  'end': new Date("2013-10-20") // Date | Subset on dates (end date).
};
apiInstance.sendSaveDataGet(lat, lon, format, opts, (error, data, response) => {
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
 **lat** | **Number**| Latitude component of location. | 
 **lon** | **Number**| Longitude component of location. | 
 **format** | **String**| Specify a format for data retrieval. | 
 **vars** | [**[String]**](String.md)| Daymet Daily weather estimates. | [optional] 
 **years** | [**[String]**](String.md)| Subset on years [1980..2019]. | [optional] 
 **start** | **Date**| Subset on dates (start date). | [optional] 
 **end** | **Date**| Subset on dates (end date). | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## visualizeGet

> visualizeGet(lat, lon, format, opts)

Visualize Daymet Data in a web browser

Returns plots to a web browser of requested data using Plotly

### Example

```javascript
import DaymetSinglePixelExtractionToolApi from 'daymet_single_pixel_extraction_tool_api';

let apiInstance = new DaymetSinglePixelExtractionToolApi.DefaultApi();
let lat = 3.4; // Number | Latitude component of location.
let lon = 3.4; // Number | Longitude component of location.
let format = "format_example"; // String | Specify a format for data retrieval.
let opts = {
  'vars': ["null"], // [String] | Daymet Daily weather estimates.
  'years': ["null"], // [String] | Subset on years [1980..2019].
  'start': new Date("2013-10-20"), // Date | Subset on dates (start date).
  'end': new Date("2013-10-20") // Date | Subset on dates (end date).
};
apiInstance.visualizeGet(lat, lon, format, opts, (error, data, response) => {
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
 **lat** | **Number**| Latitude component of location. | 
 **lon** | **Number**| Longitude component of location. | 
 **format** | **String**| Specify a format for data retrieval. | 
 **vars** | [**[String]**](String.md)| Daymet Daily weather estimates. | [optional] 
 **years** | [**[String]**](String.md)| Subset on years [1980..2019]. | [optional] 
 **start** | **Date**| Subset on dates (start date). | [optional] 
 **end** | **Date**| Subset on dates (end date). | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

