# DefaultApi

All URIs are relative to *https://api.opencagedata.com/geocode*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**vversionFormatGet**](DefaultApi.md#vversionFormatGet) | **GET** /v{version}/{format} |  |


<a id="vversionFormatGet"></a>
# **vversionFormatGet**
> Response vversionFormatGet(version, format, q, key, abbrv, addressOnly, addRequest, bounds, countrycode, jsonp, language, limit, minConfidence, noAnnotations, noDedupe, noRecord, pretty, proximity, roadinfo)



geocode a query

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.opencagedata.com/geocode");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Integer version = 56; // Integer | API version.
    String format = "format_example"; // String | format of the response. One of 'json', 'xml' or 'map'.
    String q = "q_example"; // String | string or lat,lng to be geocoded.
    String key = "key_example"; // String | an application key.
    Boolean abbrv = true; // Boolean | when true we attempt to abbreviate the formatted field of results.
    Boolean addressOnly = true; // Boolean | when true we include only address details in the formatted field of results.
    Boolean addRequest = true; // Boolean | if true the request is included in the response.
    String bounds = "bounds_example"; // String | four coordinate points forming the south-west and north-east corners of a bounding box (min long, min lat, max long, max lat).
    String countrycode = "countrycode_example"; // String | two letter code ISO 3166-1 Alpha 2 code to limit results to that country.
    String jsonp = "jsonp_example"; // String | wraps the returned JSON with a function name.
    String language = "language_example"; // String | an IETF format language code (ex: 'es' or 'pt-BR').
    Integer limit = 56; // Integer | maximum number of results to return. Default is 10. Maximum is 100.
    Integer minConfidence = 56; // Integer | integer from 1-10. Only results with at least this confidence are returned.
    Boolean noAnnotations = true; // Boolean | when true annotations are not added to results.
    Boolean noDedupe = true; // Boolean | when true results are not deduplicated.
    Boolean noRecord = true; // Boolean | when true query content is not logged.
    Boolean pretty = true; // Boolean | when true results are pretty printed. Useful for debugging.
    String proximity = "proximity_example"; // String | lat,lng to bias results.
    Boolean roadinfo = true; // Boolean | match nearest road, include roadinfo annotation
    try {
      Response result = apiInstance.vversionFormatGet(version, format, q, key, abbrv, addressOnly, addRequest, bounds, countrycode, jsonp, language, limit, minConfidence, noAnnotations, noDedupe, noRecord, pretty, proximity, roadinfo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#vversionFormatGet");
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
| **version** | **Integer**| API version. | |
| **format** | **String**| format of the response. One of &#39;json&#39;, &#39;xml&#39; or &#39;map&#39;. | |
| **q** | **String**| string or lat,lng to be geocoded. | |
| **key** | **String**| an application key. | |
| **abbrv** | **Boolean**| when true we attempt to abbreviate the formatted field of results. | [optional] |
| **addressOnly** | **Boolean**| when true we include only address details in the formatted field of results. | [optional] |
| **addRequest** | **Boolean**| if true the request is included in the response. | [optional] |
| **bounds** | **String**| four coordinate points forming the south-west and north-east corners of a bounding box (min long, min lat, max long, max lat). | [optional] |
| **countrycode** | **String**| two letter code ISO 3166-1 Alpha 2 code to limit results to that country. | [optional] |
| **jsonp** | **String**| wraps the returned JSON with a function name. | [optional] |
| **language** | **String**| an IETF format language code (ex: &#39;es&#39; or &#39;pt-BR&#39;). | [optional] |
| **limit** | **Integer**| maximum number of results to return. Default is 10. Maximum is 100. | [optional] |
| **minConfidence** | **Integer**| integer from 1-10. Only results with at least this confidence are returned. | [optional] |
| **noAnnotations** | **Boolean**| when true annotations are not added to results. | [optional] |
| **noDedupe** | **Boolean**| when true results are not deduplicated. | [optional] |
| **noRecord** | **Boolean**| when true query content is not logged. | [optional] |
| **pretty** | **Boolean**| when true results are pretty printed. Useful for debugging. | [optional] |
| **proximity** | **String**| lat,lng to bias results. | [optional] |
| **roadinfo** | **Boolean**| match nearest road, include roadinfo annotation | [optional] |

### Return type

[**Response**](Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |
| **400** | Invalid request |  -  |
| **401** | Unable to authenticate |  -  |
| **402** | Valid request but quota exceeded |  -  |
| **403** | Forbidden |  -  |
| **404** | Invalid API endpoint |  -  |
| **405** | Method not allowed |  -  |
| **408** | Timeout; you can try again |  -  |
| **410** | Request too long |  -  |
| **426** | Upgrade required |  -  |
| **429** | Too many requests |  -  |
| **503** | Internal server error |  -  |

