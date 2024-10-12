# ImageCharts.ChartJsApi

All URIs are relative to *https://image-charts.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getChartjs280**](ChartJsApi.md#getChartjs280) | **GET** /chart.js/2.8.0 | Chart.js as image API



## getChartjs280

> String getChartjs280(opts)

Chart.js as image API

Image-charts

### Example

```javascript
import ImageCharts from 'image_charts';

let apiInstance = new ImageCharts.ChartJsApi();
let opts = {
  'c': "c_example", // String | Javascript/JSON definition of the chart. Use a Chart.js configuration object.
  'chart': "chart_example", // String | Javascript/JSON definition of the chart. Use a Chart.js configuration object.
  'width': 500, // Number | Width of the chart
  'height': 300, // Number | Height of the chart
  'backgroundColor': "backgroundColor_example", // String | Background of the chart canvas. Accepts rgb (rgb(255,255,120)), colors (red), and url-encoded hex values (%23ff00ff). Abbreviated as \"bkg\"
  'bkg': "bkg_example", // String | Background of the chart canvas. Accepts rgb (rgb(255,255,120)), colors (red), and url-encoded hex values (%23ff00ff). Abbreviated as \"bkg\"
  'encoding': "'url'", // String | Encoding of your \"chart\" parameter. Accepted values are url and base64.
  'icac': "icac_example", // String | image-charts enterprise `account_id`
  'ichm': "ichm_example", // String | HMAC-SHA256 signature required to activate paid features
  'icretina': "icretina_example" // String | retina mode
};
apiInstance.getChartjs280(opts, (error, data, response) => {
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
 **c** | **String**| Javascript/JSON definition of the chart. Use a Chart.js configuration object. | [optional] 
 **chart** | **String**| Javascript/JSON definition of the chart. Use a Chart.js configuration object. | [optional] 
 **width** | **Number**| Width of the chart | [optional] [default to 500]
 **height** | **Number**| Height of the chart | [optional] [default to 300]
 **backgroundColor** | **String**| Background of the chart canvas. Accepts rgb (rgb(255,255,120)), colors (red), and url-encoded hex values (%23ff00ff). Abbreviated as \&quot;bkg\&quot; | [optional] 
 **bkg** | **String**| Background of the chart canvas. Accepts rgb (rgb(255,255,120)), colors (red), and url-encoded hex values (%23ff00ff). Abbreviated as \&quot;bkg\&quot; | [optional] 
 **encoding** | **String**| Encoding of your \&quot;chart\&quot; parameter. Accepted values are url and base64. | [optional] [default to &#39;url&#39;]
 **icac** | **String**| image-charts enterprise &#x60;account_id&#x60; | [optional] 
 **ichm** | **String**| HMAC-SHA256 signature required to activate paid features | [optional] 
 **icretina** | **String**| retina mode | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/png, application/gif, image/svg+xml

