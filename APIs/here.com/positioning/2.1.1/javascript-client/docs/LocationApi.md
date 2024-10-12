# HereNetworkPositioningApiV2.LocationApi

All URIs are relative to *https://positioning.hereapi.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postLocate**](LocationApi.md#postLocate) | **POST** /locate | Location query



## postLocate

> PostLocate200Response postLocate(locate, opts)

Location query

Request WGS-84 compliant geocoordinates for a location based on 2G/3G/4G cell and/or WLAN measurements.

### Example

```javascript
import HereNetworkPositioningApiV2 from 'here_network_positioning_api_v2';
let defaultClient = HereNetworkPositioningApiV2.ApiClient.instance;
// Configure API key authorization: APIKey
let APIKey = defaultClient.authentications['APIKey'];
APIKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIKey.apiKeyPrefix = 'Token';
// Configure Bearer (JWT) access token for authorization: AccessToken
let AccessToken = defaultClient.authentications['AccessToken'];
AccessToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new HereNetworkPositioningApiV2.LocationApi();
let locate = new HereNetworkPositioningApiV2.Locate(); // Locate | Request body containing cell and/or WLAN measurement data. Cellular measurements are given in terms defined in 3GPP and 3GGP2 specifications, see the corresponsing documentation at http://www.3gpp.org. 
let opts = {
  'confidence': 68, // Number | Confidence level in percent for the accuracy/uncertainty in the location estimate response. If not specified, the default is 68 (this corresponds to a 68% probability that the true position is within the accuracy/uncertainty radius of the location estimate: the higher the number, the greater the confidence level). 
  'contentEncoding': "contentEncoding_example", // String | Indicates that the data in the body is gzip-encoded.
  'fallback': ["null"], // [String] | Acceptable fallback options for cell and WLAN positioning. Values `area` and `any` apply to cell based positioning, and value `singleWifi` applies to WLAN based positioning. Both cell and WLAN options may be specified in the same request. If both `area` and `any` are specified, then `area` is ignored.  By default, cell based positioning returns cell tower level location estimates only. If you allow a WGS-84 compliant geocoordinate location estimate based on LAC, RNC, TAC, NID, or RZ areas, use the `fallback=area` setting. If you use the `fallback=any` setting, the service uses all available cell fallback methods and therefore the location estimate in the response may be at the MNC, SID, or MCC level.  For privacy reasons, the precise positioning based on a single WLAN AP is not possible. You can use the `fallback=singleWifi` setting to allow less accurate positioning based on a single WLAN AP. In that case, the center location of the position estimate will be deviated and the reported accuracy radius will be larger. 
  'desired': ["null"], // [String] | Comma-separated list of additional data fields that the service should include in the response if data is available. The query parameter supports the value `altitude`. 
  'xRequestID': "xRequestID_example", // String | ID used for correlating customer requests within HERE services. Used for logging and error reporting. Can be any string, but UUID is recommended. It will be echoed in the response. 
  'required': ["null"] // [String] | Comma-separated list of additional data fields that the service should include in the response. If the data is not available, the response contains an error message. The query parameter supports the value `altitude`. 
};
apiInstance.postLocate(locate, opts, (error, data, response) => {
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
 **locate** | [**Locate**](Locate.md)| Request body containing cell and/or WLAN measurement data. Cellular measurements are given in terms defined in 3GPP and 3GGP2 specifications, see the corresponsing documentation at http://www.3gpp.org.  | 
 **confidence** | **Number**| Confidence level in percent for the accuracy/uncertainty in the location estimate response. If not specified, the default is 68 (this corresponds to a 68% probability that the true position is within the accuracy/uncertainty radius of the location estimate: the higher the number, the greater the confidence level).  | [optional] [default to 68]
 **contentEncoding** | **String**| Indicates that the data in the body is gzip-encoded. | [optional] 
 **fallback** | [**[String]**](String.md)| Acceptable fallback options for cell and WLAN positioning. Values &#x60;area&#x60; and &#x60;any&#x60; apply to cell based positioning, and value &#x60;singleWifi&#x60; applies to WLAN based positioning. Both cell and WLAN options may be specified in the same request. If both &#x60;area&#x60; and &#x60;any&#x60; are specified, then &#x60;area&#x60; is ignored.  By default, cell based positioning returns cell tower level location estimates only. If you allow a WGS-84 compliant geocoordinate location estimate based on LAC, RNC, TAC, NID, or RZ areas, use the &#x60;fallback&#x3D;area&#x60; setting. If you use the &#x60;fallback&#x3D;any&#x60; setting, the service uses all available cell fallback methods and therefore the location estimate in the response may be at the MNC, SID, or MCC level.  For privacy reasons, the precise positioning based on a single WLAN AP is not possible. You can use the &#x60;fallback&#x3D;singleWifi&#x60; setting to allow less accurate positioning based on a single WLAN AP. In that case, the center location of the position estimate will be deviated and the reported accuracy radius will be larger.  | [optional] 
 **desired** | [**[String]**](String.md)| Comma-separated list of additional data fields that the service should include in the response if data is available. The query parameter supports the value &#x60;altitude&#x60;.  | [optional] 
 **xRequestID** | **String**| ID used for correlating customer requests within HERE services. Used for logging and error reporting. Can be any string, but UUID is recommended. It will be echoed in the response.  | [optional] 
 **required** | [**[String]**](String.md)| Comma-separated list of additional data fields that the service should include in the response. If the data is not available, the response contains an error message. The query parameter supports the value &#x60;altitude&#x60;.  | [optional] 

### Return type

[**PostLocate200Response**](PostLocate200Response.md)

### Authorization

[APIKey](../README.md#APIKey), [AccessToken](../README.md#AccessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

