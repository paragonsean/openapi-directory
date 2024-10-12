# IntegrationCustomerTokenApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**integrationCustomerTokenServiceV1CreateCustomerAccessTokenPost**](IntegrationCustomerTokenApi.md#integrationCustomerTokenServiceV1CreateCustomerAccessTokenPost) | **POST** /V1/integration/customer/token | integration/customer/token |


<a id="integrationCustomerTokenServiceV1CreateCustomerAccessTokenPost"></a>
# **integrationCustomerTokenServiceV1CreateCustomerAccessTokenPost**
> String integrationCustomerTokenServiceV1CreateCustomerAccessTokenPost(integrationAdminTokenServiceV1CreateAdminAccessTokenPostRequest)

integration/customer/token

Create access token for admin given the customer credentials.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationCustomerTokenApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    IntegrationCustomerTokenApi apiInstance = new IntegrationCustomerTokenApi(defaultClient);
    IntegrationAdminTokenServiceV1CreateAdminAccessTokenPostRequest integrationAdminTokenServiceV1CreateAdminAccessTokenPostRequest = new IntegrationAdminTokenServiceV1CreateAdminAccessTokenPostRequest(); // IntegrationAdminTokenServiceV1CreateAdminAccessTokenPostRequest | 
    try {
      String result = apiInstance.integrationCustomerTokenServiceV1CreateCustomerAccessTokenPost(integrationAdminTokenServiceV1CreateAdminAccessTokenPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationCustomerTokenApi#integrationCustomerTokenServiceV1CreateCustomerAccessTokenPost");
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
| **0** | Unexpected error |  -  |

