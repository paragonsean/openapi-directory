# LocationApi

All URIs are relative to *https://positioning.hereapi.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postLocate**](LocationApi.md#postLocate) | **POST** /locate | Location query |


<a id="postLocate"></a>
# **postLocate**
> PostLocate200Response postLocate(locate, confidence, contentEncoding, fallback, desired, xRequestID, required)

Location query

Request WGS-84 compliant geocoordinates for a location based on 2G/3G/4G cell and/or WLAN measurements.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://positioning.hereapi.com/v2");
    
    // Configure API key authorization: APIKey
    ApiKeyAuth APIKey = (ApiKeyAuth) defaultClient.getAuthentication("APIKey");
    APIKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIKey.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: AccessToken
    HttpBearerAuth AccessToken = (HttpBearerAuth) defaultClient.getAuthentication("AccessToken");
    AccessToken.setBearerToken("BEARER TOKEN");

    LocationApi apiInstance = new LocationApi(defaultClient);
    Locate locate = new Locate(); // Locate | Request body containing cell and/or WLAN measurement data. Cellular measurements are given in terms defined in 3GPP and 3GGP2 specifications, see the corresponsing documentation at http://www.3gpp.org. 
    Integer confidence = 68; // Integer | Confidence level in percent for the accuracy/uncertainty in the location estimate response. If not specified, the default is 68 (this corresponds to a 68% probability that the true position is within the accuracy/uncertainty radius of the location estimate: the higher the number, the greater the confidence level). 
    String contentEncoding = "gzip"; // String | Indicates that the data in the body is gzip-encoded.
    List<String> fallback = Arrays.asList(); // List<String> | Acceptable fallback options for cell and WLAN positioning. Values `area` and `any` apply to cell based positioning, and value `singleWifi` applies to WLAN based positioning. Both cell and WLAN options may be specified in the same request. If both `area` and `any` are specified, then `area` is ignored.  By default, cell based positioning returns cell tower level location estimates only. If you allow a WGS-84 compliant geocoordinate location estimate based on LAC, RNC, TAC, NID, or RZ areas, use the `fallback=area` setting. If you use the `fallback=any` setting, the service uses all available cell fallback methods and therefore the location estimate in the response may be at the MNC, SID, or MCC level.  For privacy reasons, the precise positioning based on a single WLAN AP is not possible. You can use the `fallback=singleWifi` setting to allow less accurate positioning based on a single WLAN AP. In that case, the center location of the position estimate will be deviated and the reported accuracy radius will be larger. 
    List<String> desired = Arrays.asList(); // List<String> | Comma-separated list of additional data fields that the service should include in the response if data is available. The query parameter supports the value `altitude`. 
    String xRequestID = "xRequestID_example"; // String | ID used for correlating customer requests within HERE services. Used for logging and error reporting. Can be any string, but UUID is recommended. It will be echoed in the response. 
    List<String> required = Arrays.asList(); // List<String> | Comma-separated list of additional data fields that the service should include in the response. If the data is not available, the response contains an error message. The query parameter supports the value `altitude`. 
    try {
      PostLocate200Response result = apiInstance.postLocate(locate, confidence, contentEncoding, fallback, desired, xRequestID, required);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationApi#postLocate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **locate** | [**Locate**](Locate.md)| Request body containing cell and/or WLAN measurement data. Cellular measurements are given in terms defined in 3GPP and 3GGP2 specifications, see the corresponsing documentation at http://www.3gpp.org.  | |
| **confidence** | **Integer**| Confidence level in percent for the accuracy/uncertainty in the location estimate response. If not specified, the default is 68 (this corresponds to a 68% probability that the true position is within the accuracy/uncertainty radius of the location estimate: the higher the number, the greater the confidence level).  | [optional] [default to 68] |
| **contentEncoding** | **String**| Indicates that the data in the body is gzip-encoded. | [optional] [enum: gzip] |
| **fallback** | [**List&lt;String&gt;**](String.md)| Acceptable fallback options for cell and WLAN positioning. Values &#x60;area&#x60; and &#x60;any&#x60; apply to cell based positioning, and value &#x60;singleWifi&#x60; applies to WLAN based positioning. Both cell and WLAN options may be specified in the same request. If both &#x60;area&#x60; and &#x60;any&#x60; are specified, then &#x60;area&#x60; is ignored.  By default, cell based positioning returns cell tower level location estimates only. If you allow a WGS-84 compliant geocoordinate location estimate based on LAC, RNC, TAC, NID, or RZ areas, use the &#x60;fallback&#x3D;area&#x60; setting. If you use the &#x60;fallback&#x3D;any&#x60; setting, the service uses all available cell fallback methods and therefore the location estimate in the response may be at the MNC, SID, or MCC level.  For privacy reasons, the precise positioning based on a single WLAN AP is not possible. You can use the &#x60;fallback&#x3D;singleWifi&#x60; setting to allow less accurate positioning based on a single WLAN AP. In that case, the center location of the position estimate will be deviated and the reported accuracy radius will be larger.  | [optional] [enum: any, area, singleWifi] |
| **desired** | [**List&lt;String&gt;**](String.md)| Comma-separated list of additional data fields that the service should include in the response if data is available. The query parameter supports the value &#x60;altitude&#x60;.  | [optional] [enum: altitude] |
| **xRequestID** | **String**| ID used for correlating customer requests within HERE services. Used for logging and error reporting. Can be any string, but UUID is recommended. It will be echoed in the response.  | [optional] |
| **required** | [**List&lt;String&gt;**](String.md)| Comma-separated list of additional data fields that the service should include in the response. If the data is not available, the response contains an error message. The query parameter supports the value &#x60;altitude&#x60;.  | [optional] [enum: altitude] |

### Return type

[**PostLocate200Response**](PostLocate200Response.md)

### Authorization

[APIKey](../README.md#APIKey), [AccessToken](../README.md#AccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request processed successfully and a WGS-84 compliant geocoordinate location estimate was included in the response. |  * X-Correlation-ID -  <br>  * X-Request-ID -  <br>  |
| **400** | The request is malformed. The URL query parameters or the JSON POST body in the request is invalid. Check the message in the response for additional troubleshooting information.  |  * X-Correlation-ID -  <br>  * X-Request-ID -  <br>  |
| **401** | Authentication failed. |  -  |
| **403** | Access denied. |  -  |
| **404** | The values provided in the request cannot produce any content for the response. The location of the WLANs and cells in the request is unknown or the locations of the radio measurements are so widely scattered that the location cannot be determined. Make sure that the network measurements are correct and consistent. Try allowing fallbacks &#x60;area&#x60; or &#x60;any&#x60; for cell positioning and &#x60;singleWifi&#x60; for WLAN positioning.  |  * X-Correlation-ID -  <br>  * X-Request-ID -  <br>  |
| **405** | Method not allowed. Only POST is supported. |  * X-Correlation-ID -  <br>  * X-Request-ID -  <br>  |
| **413** | Too large request. |  * X-Correlation-ID -  <br>  * X-Request-ID -  <br>  |
| **414** | Too long URI. |  * X-Correlation-ID -  <br>  * X-Request-ID -  <br>  |
| **415** | Invalid request content type. |  * X-Correlation-ID -  <br>  * X-Request-ID -  <br>  |
| **500** | An unexpected server error has occurred, try again later. |  * X-Correlation-ID -  <br>  * X-Request-ID -  <br>  |
| **503** | Service is unavailable, try again later. |  * X-Correlation-ID -  <br>  * X-Request-ID -  <br>  |

