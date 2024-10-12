# ScrollApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**scrolldocuments**](ScrollApi.md#scrolldocuments) | **GET** /api/dataentities/{acronym}/scroll | Scroll documents |


<a id="scrolldocuments"></a>
# **scrolldocuments**
> scrolldocuments(contentType, accept, acronym)

Scroll documents

Scrolls through documents according to the query parameter filters.    &gt; Avoid sending too many requests with wildcards (&#x60;*&#x60;) in the search parameters or that use the &#x60;keyword&#x60; parameter. This may lead to this endpoint being temporarily blocked for your account. If this happens you will receive an error with status code &#x60;429&#x60;.    Use all the features of &#x60;search&#x60; API to perform filters.    In the first request, the &#x60;X-VTEX-MD-TOKEN&#x60; token will be obtained in the header. This token must be passed to the next request in the query string &#x60;_token&#x60; parameter. The token has a timeout of 10 minutes, which refreshes after each request.    **ATTENTION:** To inform the number of documents per request, use the query string parameter &#x60;_size&#x60;, which has the maximum value of 1000.    After the token is obtained it is no longer necessary to send the filter or document size per page parameters. You only need to resend the token until the document collection is empty.    ### First request example:  &#x60;&#x60;&#x60;  /dataentities/CL/scroll?isCluster&#x3D;true&amp;_size&#x3D;250&amp;_fields&#x3D;email,firstName  &#x60;&#x60;&#x60;    After the first request, retrieve the token in the header &#x60;X-VTEX-MD-TOKEN&#x60; and make the next requests.    ### Example of subsequent requests:  &#x60;&#x60;&#x60;  /dataentities/CL/scroll?_token&#x3D;tokenvalueexample  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScrollApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    ScrollApi apiInstance = new ScrollApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent
    String accept = "application/vnd.vtex.ds.v10+json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
    String acronym = "{{acronym}}"; // String | Identifies the kind of data
    try {
      apiInstance.scrolldocuments(contentType, accept, acronym);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScrollApi#scrolldocuments");
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
| **contentType** | **String**| Type of the content being sent | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand  | [default to application/vnd.vtex.ds.v10+json] |
| **acronym** | **String**| Identifies the kind of data | [default to {{acronym}}] |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **429** | Too Many Requests |  -  |

