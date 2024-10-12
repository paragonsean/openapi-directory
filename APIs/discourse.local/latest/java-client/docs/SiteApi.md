# SiteApi

All URIs are relative to *http://discourse.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getSite**](SiteApi.md#getSite) | **GET** /site.json | Get site info |


<a id="getSite"></a>
# **getSite**
> GetSite200Response getSite()

Get site info

Can be used to fetch all categories and subcategories

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SiteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://discourse.local");

    SiteApi apiInstance = new SiteApi(defaultClient);
    try {
      GetSite200Response result = apiInstance.getSite();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SiteApi#getSite");
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

[**GetSite200Response**](GetSite200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success response |  -  |

