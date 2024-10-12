# AlertTypesApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getOrganizationWebhooksAlertTypes_2**](AlertTypesApi.md#getOrganizationWebhooksAlertTypes_2) | **GET** /organizations/{organizationId}/webhooks/alertTypes | Return a list of alert types to be used with managing webhook alerts |


<a id="getOrganizationWebhooksAlertTypes_2"></a>
# **getOrganizationWebhooksAlertTypes_2**
> List&lt;Object&gt; getOrganizationWebhooksAlertTypes_2(organizationId, productType)

Return a list of alert types to be used with managing webhook alerts

Return a list of alert types to be used with managing webhook alerts

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    AlertTypesApi apiInstance = new AlertTypesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String productType = "appliance"; // String | Filter sample alerts to a specific product type
    try {
      List<Object> result = apiInstance.getOrganizationWebhooksAlertTypes_2(organizationId, productType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertTypesApi#getOrganizationWebhooksAlertTypes_2");
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
| **organizationId** | **String**|  | |
| **productType** | **String**| Filter sample alerts to a specific product type | [optional] [enum: appliance, camera, cellularGateway, health, platform, sensor, sm, switch, wireless] |

### Return type

**List&lt;Object&gt;**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

