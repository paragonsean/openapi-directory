# DefaultApi

All URIs are relative to *https://api.stoplight.io/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**pOSTVersionsPublishAnon**](DefaultApi.md#pOSTVersionsPublishAnon) | **POST** /versions/publish/anon | Publish Anonymous |


<a id="pOSTVersionsPublishAnon"></a>
# **pOSTVersionsPublishAnon**
> POSTVersionsPublishAnon200Response pOSTVersionsPublishAnon(poSTVersionsPublishAnonRequest)

Publish Anonymous

Anonymously publish to API Docs.  This endpoint will take a JSON spec or a URL to a swagger or raml spec.  &#x60;&#x60;&#x60; {   \&quot;specData\&quot;: {...} } &#x60;&#x60;&#x60;  or  &#x60;&#x60;&#x60; {   \&quot;url\&quot;: \&quot;http://petstore.swagger.io/v2/swagger.json\&quot; } &#x60;&#x60;&#x60;  The spec will be published to api-docs.io anonymously, which means you will not be able to update or remove this documentation.  The response will contain a url to the published documentation.  &#x60;&#x60;&#x60; {   \&quot;url\&quot;: \&quot;https://swagger-petstore.api-docs.io/v1.0.0\&quot; } &#x60;&#x60;&#x60;   The limitations of anonymous publishing * Cannot update/remove the documentation * Cannot choose the subdomain * Cannot choose the version * Cannot add theming

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
    defaultClient.setBasePath("https://api.stoplight.io/v1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    POSTVersionsPublishAnonRequest poSTVersionsPublishAnonRequest = new POSTVersionsPublishAnonRequest(); // POSTVersionsPublishAnonRequest | 
    try {
      POSTVersionsPublishAnon200Response result = apiInstance.pOSTVersionsPublishAnon(poSTVersionsPublishAnonRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#pOSTVersionsPublishAnon");
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
| **poSTVersionsPublishAnonRequest** | [**POSTVersionsPublishAnonRequest**](POSTVersionsPublishAnonRequest.md)|  | [optional] |

### Return type

[**POSTVersionsPublishAnon200Response**](POSTVersionsPublishAnon200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** |  |  -  |
| **401** |  |  -  |
| **404** |  |  -  |
| **500** |  |  -  |

