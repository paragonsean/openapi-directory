# AccessTokenApi

All URIs are relative to *https://smart-me.com:443*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**accessTokenPut**](AccessTokenApi.md#accessTokenPut) | **PUT** /api/AccessToken | Creates a Access Token to write on a Card (e.g. NFC) |


<a id="accessTokenPut"></a>
# **accessTokenPut**
> String accessTokenPut(accessTokenToPut)

Creates a Access Token to write on a Card (e.g. NFC)

Creates a Access Token to write on a Card (e.g. NFC)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccessTokenApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    AccessTokenApi apiInstance = new AccessTokenApi(defaultClient);
    AccessTokenToPut accessTokenToPut = new AccessTokenToPut(); // AccessTokenToPut | 
    try {
      String result = apiInstance.accessTokenPut(accessTokenToPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccessTokenApi#accessTokenPut");
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
| **accessTokenToPut** | [**AccessTokenToPut**](AccessTokenToPut.md)|  | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

