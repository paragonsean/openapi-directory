# ImageCharts.ChartApi

All URIs are relative to *https://image-charts.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getChart**](ChartApi.md#getChart) | **GET** /chart | Image-Charts API



## getChart

> String getChart(cht, chl, opts)

Image-Charts API

Image-charts

### Example

```javascript
import ImageCharts from 'image_charts';

let apiInstance = new ImageCharts.ChartApi();
let cht = "cht_example"; // String | Chart type
let chl = "chl_example"; // String | bar, pie slice, doughnut slice and polar slice chart labels
let opts = {
  'chd': "chd_example", // String | chart data
  'chds': "chds_example", // String | data format with custom scaling
  'choe': "choe_example", // String | QRCode data encoding
  'chld': "'L|4'", // String | QRCode error correction level and optional margin
  'chxr': "chxr_example", // String | Axis data-range
  'chxp': "chxp_example", // String | axis label positions
  'chof': "'.png'", // String | Image output format
  'chs': "chs_example", // String | Chart size (<width>x<height>)
  'chdl': "chdl_example", // String | Text for each series, to display in the legend
  'chdls': "'000000'", // String | Chart legend text and style
  'chg': "chg_example", // String | Solid or dotted grid lines
  'chco': "'F56991,FF9F80,FFC48C,D1F2A5,EFFAB4'", // String | series colors
  'chtt': "chtt_example", // String | chart title
  'chts': "chts_example", // String | chart title colors and font size
  'chxt': "chxt_example", // String | Display values on your axis lines or change which axes are shown
  'chxl': "chxl_example", // String | Custom string axis labels on any axis
  'chxs': "chxs_example", // String | Font size, color for axis labels, both custom labels and default label values
  'chm': "chm_example", // String | compound charts and line fills
  'chls': "chls_example", // String | line thickness and solid/dashed style
  'chlps': "chlps_example", // String | Position and style of labels on data
  'chma': "chma_example", // String | chart margins
  'chdlp': "'r'", // String | Position of the legend and order of the legend entries
  'chf': "'bg,s,FFFFFF'", // String | Background Fills
  'chbh': "'10'", // String | Bar Width and Spacing. (not supported)  You can optionally specify custom values for bar widths and spacing between bars and groups. You can only specify one set of width values for all bars. If you don't specify chbh, all bars will be 23 pixels wide, which means that the end bars can be clipped if the total bar + space width is wider than the chart width.
  'chbr': "'0'", // String | Bar corner radius. Display bars with rounded corner.
  'chan': "chan_example", // String | gif configuration
  'chli': "chli_example", // String | doughnut chart inside label
  'icac': "icac_example", // String | image-charts enterprise `account_id`
  'ichm': "ichm_example", // String | HMAC-SHA256 signature required to activate paid features
  'icff': "icff_example", // String | Default font family for all text from Google Fonts. Use same syntax as Google Font CSS API
  'icfs': "icfs_example", // String | Default font style for all text
  'iclocale': "iclocale_example", // String | localization (ISO 639-1)
  'icwt': false, // Boolean | (Private) Force to display the watermark EVEN IF the chart was signed with an enterprise account
  'icretina': "icretina_example", // String | retina mode
  'icqrb': "'FFFFFF'", // String | Background color for QR Codes
  'icqrf': "'000000'" // String | Foreground color for QR Codes
};
apiInstance.getChart(cht, chl, opts, (error, data, response) => {
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
 **cht** | **String**| Chart type | 
 **chl** | **String**| bar, pie slice, doughnut slice and polar slice chart labels | 
 **chd** | **String**| chart data | [optional] 
 **chds** | **String**| data format with custom scaling | [optional] 
 **choe** | **String**| QRCode data encoding | [optional] 
 **chld** | **String**| QRCode error correction level and optional margin | [optional] [default to &#39;L|4&#39;]
 **chxr** | **String**| Axis data-range | [optional] 
 **chxp** | **String**| axis label positions | [optional] 
 **chof** | **String**| Image output format | [optional] [default to &#39;.png&#39;]
 **chs** | **String**| Chart size (&lt;width&gt;x&lt;height&gt;) | [optional] 
 **chdl** | **String**| Text for each series, to display in the legend | [optional] 
 **chdls** | **String**| Chart legend text and style | [optional] [default to &#39;000000&#39;]
 **chg** | **String**| Solid or dotted grid lines | [optional] 
 **chco** | **String**| series colors | [optional] [default to &#39;F56991,FF9F80,FFC48C,D1F2A5,EFFAB4&#39;]
 **chtt** | **String**| chart title | [optional] 
 **chts** | **String**| chart title colors and font size | [optional] 
 **chxt** | **String**| Display values on your axis lines or change which axes are shown | [optional] 
 **chxl** | **String**| Custom string axis labels on any axis | [optional] 
 **chxs** | **String**| Font size, color for axis labels, both custom labels and default label values | [optional] 
 **chm** | **String**| compound charts and line fills | [optional] 
 **chls** | **String**| line thickness and solid/dashed style | [optional] 
 **chlps** | **String**| Position and style of labels on data | [optional] 
 **chma** | **String**| chart margins | [optional] 
 **chdlp** | **String**| Position of the legend and order of the legend entries | [optional] [default to &#39;r&#39;]
 **chf** | **String**| Background Fills | [optional] [default to &#39;bg,s,FFFFFF&#39;]
 **chbh** | **String**| Bar Width and Spacing. (not supported)  You can optionally specify custom values for bar widths and spacing between bars and groups. You can only specify one set of width values for all bars. If you don&#39;t specify chbh, all bars will be 23 pixels wide, which means that the end bars can be clipped if the total bar + space width is wider than the chart width. | [optional] [default to &#39;10&#39;]
 **chbr** | **String**| Bar corner radius. Display bars with rounded corner. | [optional] [default to &#39;0&#39;]
 **chan** | **String**| gif configuration | [optional] 
 **chli** | **String**| doughnut chart inside label | [optional] 
 **icac** | **String**| image-charts enterprise &#x60;account_id&#x60; | [optional] 
 **ichm** | **String**| HMAC-SHA256 signature required to activate paid features | [optional] 
 **icff** | **String**| Default font family for all text from Google Fonts. Use same syntax as Google Font CSS API | [optional] 
 **icfs** | **String**| Default font style for all text | [optional] 
 **iclocale** | **String**| localization (ISO 639-1) | [optional] 
 **icwt** | **Boolean**| (Private) Force to display the watermark EVEN IF the chart was signed with an enterprise account | [optional] [default to false]
 **icretina** | **String**| retina mode | [optional] 
 **icqrb** | **String**| Background color for QR Codes | [optional] [default to &#39;FFFFFF&#39;]
 **icqrf** | **String**| Foreground color for QR Codes | [optional] [default to &#39;000000&#39;]

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/png, application/gif, image/svg+xml

