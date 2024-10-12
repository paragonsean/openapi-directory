# RoutingKeysApi

All URIs are relative to *https://api.victorops.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiPublicV1OrgRoutingKeysGet**](RoutingKeysApi.md#apiPublicV1OrgRoutingKeysGet) | **GET** /api-public/v1/org/routing-keys | List routing keys with associated teams |


<a id="apiPublicV1OrgRoutingKeysGet"></a>
# **apiPublicV1OrgRoutingKeysGet**
> ListRoutingKeysResponse apiPublicV1OrgRoutingKeysGet(xVOApiId, xVOApiKey)

List routing keys with associated teams

Retrieves a list of routing keys and associated teams. This API may be called a maximum of 60 times per minute.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoutingKeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    RoutingKeysApi apiInstance = new RoutingKeysApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    try {
      ListRoutingKeysResponse result = apiInstance.apiPublicV1OrgRoutingKeysGet(xVOApiId, xVOApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutingKeysApi#apiPublicV1OrgRoutingKeysGet");
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
| **xVOApiId** | **String**| Your API ID | |
| **xVOApiKey** | **String**| Your API Key | |

### Return type

[**ListRoutingKeysResponse**](ListRoutingKeysResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of routing keys and associated teams |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **404** | Path not found |  -  |
| **500** | Internal Server Error |  -  |

