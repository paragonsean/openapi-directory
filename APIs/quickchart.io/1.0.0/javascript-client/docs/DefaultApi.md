# QuickChartApi.DefaultApi

All URIs are relative to *https://quickchart.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chartGet**](DefaultApi.md#chartGet) | **GET** /chart | Generate a chart (GET)
[**chartPost**](DefaultApi.md#chartPost) | **POST** /chart | Generate a chart (POST)
[**qrGet**](DefaultApi.md#qrGet) | **GET** /qr | Generate a QR code (GET)
[**qrPost**](DefaultApi.md#qrPost) | **POST** /qr | Generate a QR code (POST)



## chartGet

> File chartGet(opts)

Generate a chart (GET)

Generate a chart based on the provided parameters.

### Example

```javascript
import QuickChartApi from 'quick_chart_api';

let apiInstance = new QuickChartApi.DefaultApi();
let opts = {
  'chart': "chart_example", // String | The chart configuration in Chart.js format (JSON or Javascript).
  'width': 56, // Number | The width of the chart in pixels.
  'height': 56, // Number | The height of the chart in pixels.
  'format': "format_example", // String | The output format of the chart, 'png', 'jpg', 'svg', or 'webp'.
  'backgroundColor': "backgroundColor_example" // String | The background color of the chart.
};
apiInstance.chartGet(opts, (error, data, response) => {
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
 **chart** | **String**| The chart configuration in Chart.js format (JSON or Javascript). | [optional] 
 **width** | **Number**| The width of the chart in pixels. | [optional] 
 **height** | **Number**| The height of the chart in pixels. | [optional] 
 **format** | **String**| The output format of the chart, &#39;png&#39;, &#39;jpg&#39;, &#39;svg&#39;, or &#39;webp&#39;. | [optional] 
 **backgroundColor** | **String**| The background color of the chart. | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/jpeg, image/png, image/svg+xml, image/webp


## chartPost

> File chartPost(chartPostRequest)

Generate a chart (POST)

Generate a chart based on the provided configuration in the request body.

### Example

```javascript
import QuickChartApi from 'quick_chart_api';

let apiInstance = new QuickChartApi.DefaultApi();
let chartPostRequest = new QuickChartApi.ChartPostRequest(); // ChartPostRequest | 
apiInstance.chartPost(chartPostRequest, (error, data, response) => {
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
 **chartPostRequest** | [**ChartPostRequest**](ChartPostRequest.md)|  | 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: image/jpeg, image/png, image/svg+xml, image/webp


## qrGet

> File qrGet(opts)

Generate a QR code (GET)

Generate a QR code based on the provided parameters.

### Example

```javascript
import QuickChartApi from 'quick_chart_api';

let apiInstance = new QuickChartApi.DefaultApi();
let opts = {
  'text': "text_example", // String | The text to be encoded in the QR code.
  'width': 56, // Number | The width of the QR code in pixels.
  'height': 56, // Number | The height of the QR code in pixels.
  'format': "format_example", // String | The output format of the QR code, e.g., 'png' or 'svg'.
  'margin': 56 // Number | The margin around the QR code in pixels.
};
apiInstance.qrGet(opts, (error, data, response) => {
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
 **text** | **String**| The text to be encoded in the QR code. | [optional] 
 **width** | **Number**| The width of the QR code in pixels. | [optional] 
 **height** | **Number**| The height of the QR code in pixels. | [optional] 
 **format** | **String**| The output format of the QR code, e.g., &#39;png&#39; or &#39;svg&#39;. | [optional] 
 **margin** | **Number**| The margin around the QR code in pixels. | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/png, image/svg+xml


## qrPost

> File qrPost(qrPostRequest)

Generate a QR code (POST)

Generate a QR code based on the provided configuration in the request body.

### Example

```javascript
import QuickChartApi from 'quick_chart_api';

let apiInstance = new QuickChartApi.DefaultApi();
let qrPostRequest = new QuickChartApi.QrPostRequest(); // QrPostRequest | 
apiInstance.qrPost(qrPostRequest, (error, data, response) => {
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
 **qrPostRequest** | [**QrPostRequest**](QrPostRequest.md)|  | 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: image/png, image/svg+xml

