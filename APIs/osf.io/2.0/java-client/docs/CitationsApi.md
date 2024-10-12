# CitationsApi

All URIs are relative to *https://api.test.osf.io/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**citationsStylesList**](CitationsApi.md#citationsStylesList) | **GET** /citations/styles/ | List all citation styles |
| [**citationsStylesRead**](CitationsApi.md#citationsStylesRead) | **GET** /citations/styles/{style_id}/ | Retrieve a citation style |


<a id="citationsStylesList"></a>
# **citationsStylesList**
> List&lt;CitationStyle&gt; citationsStylesList()

List all citation styles

 A paginated list of all standard citation styles available for rendering citations. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of 10 citation styles. Each resource in the array is a separate citation syle and contains the full representation of the citation style object.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  This request should never return an error. #### Filtering You can optionally request that the response only include citation styles that match your filters by utilizing the &#x60;filter&#x60; query parameter, e.g. https://api.osf.io/v2/citations/styles/?filter[title]&#x3D;open.  Citation styles may be filtered by their &#x60;id&#x60;, &#x60;title&#x60;, &#x60;short-title&#x60;, and &#x60;summary&#x60;. #### Errors This request should never return an error.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CitationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    CitationsApi apiInstance = new CitationsApi(defaultClient);
    try {
      List<CitationStyle> result = apiInstance.citationsStylesList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CitationsApi#citationsStylesList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;CitationStyle&gt;**](CitationStyle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="citationsStylesRead"></a>
# **citationsStylesRead**
> CitationStyle citationsStylesRead(styleId)

Retrieve a citation style

Retrieves the details of a citation style. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the requested citation style, if the request is successful. #### Errors If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CitationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    CitationsApi apiInstance = new CitationsApi(defaultClient);
    String styleId = "styleId_example"; // String | The unique identifier of the citation style.
    try {
      CitationStyle result = apiInstance.citationsStylesRead(styleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CitationsApi#citationsStylesRead");
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
| **styleId** | **String**| The unique identifier of the citation style. | |

### Return type

[**CitationStyle**](CitationStyle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

