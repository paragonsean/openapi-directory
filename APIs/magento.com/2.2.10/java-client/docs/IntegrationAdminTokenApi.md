# IntegrationAdminTokenApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**integrationAdminTokenServiceV1CreateAdminAccessTokenPost**](IntegrationAdminTokenApi.md#integrationAdminTokenServiceV1CreateAdminAccessTokenPost) | **POST** /V1/integration/admin/token | integration/admin/token |


<a id="integrationAdminTokenServiceV1CreateAdminAccessTokenPost"></a>
# **integrationAdminTokenServiceV1CreateAdminAccessTokenPost**
> String integrationAdminTokenServiceV1CreateAdminAccessTokenPost(integrationAdminTokenServiceV1CreateAdminAccessTokenPostRequest)

integration/admin/token

Create access token for admin given the admin credentials.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationAdminTokenApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    IntegrationAdminTokenApi apiInstance = new IntegrationAdminTokenApi(defaultClient);
    IntegrationAdminTokenServiceV1CreateAdminAccessTokenPostRequest integrationAdminTokenServiceV1CreateAdminAccessTokenPostRequest = new IntegrationAdminTokenServiceV1CreateAdminAccessTokenPostRequest(); // IntegrationAdminTokenServiceV1CreateAdminAccessTokenPostRequest | 
    try {
      String result = apiInstance.integrationAdminTokenServiceV1CreateAdminAccessTokenPost(integrationAdminTokenServiceV1CreateAdminAccessTokenPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationAdminTokenApi#integrationAdminTokenServiceV1CreateAdminAccessTokenPost");
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
| **integrationAdminTokenServiceV1CreateAdminAccessTokenPostRequest** | [**IntegrationAdminTokenServiceV1CreateAdminAccessTokenPostRequest**](IntegrationAdminTokenServiceV1CreateAdminAccessTokenPostRequest.md)|  | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **500** | Internal Server error |  -  |
| **0** | Unexpected error |  -  |

