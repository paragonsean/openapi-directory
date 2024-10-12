# HealthCheckApi

All URIs are relative to *https://products.api.telstra.com/messaging/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**healthCheck**](HealthCheckApi.md#healthCheck) | **GET** /health-check | health check |


<a id="healthCheck"></a>
# **healthCheck**
> HealthCheck200Response healthCheck(authorization, telstraApiVersion)

health check

Use this endpoint to check the operational status of the messaging service. A 200 OK response means the service is up. If you receive a 504 response, the service is temporarily down. Check the [API Live Status page] (https://dev.telstra.com/api/status) to see if there&#39;s an active incident.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HealthCheckApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://products.api.telstra.com/messaging/v3");
    
    // Configure OAuth2 access token for authorization: bearer_auth
    OAuth bearer_auth = (OAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setAccessToken("YOUR ACCESS TOKEN");

    HealthCheckApi apiInstance = new HealthCheckApi(defaultClient);
    String authorization = "Bearer <access_token>"; // String | 
    String telstraApiVersion = "3.1.0"; // String | 
    try {
      HealthCheck200Response result = apiInstance.healthCheck(authorization, telstraApiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HealthCheckApi#healthCheck");
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
| **authorization** | **String**|  | |
| **telstraApiVersion** | **String**|  | [optional] |

### Return type

[**HealthCheck200Response**](HealthCheck200Response.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A 200 OK response means the messaging service is up. |  * Content-Language -  <br>  |
| **401** | Unauthorized  | code | suggested_action | | :--- | :--- | | TOKEN_INVALID | Check the access token. | | TOKEN_EXPIRED | Please refresh the token. |  |  * Content-Language -  <br>  |
| **402** | Payment Required  | code | suggested_action | | :--- | :--- | | ACCOUNT_ERR | Contact [support](mailto:telstradev@team.telstra.com) for help with your account. | | ACCOUNT_NOT_LINKED | Check you&#39;ve registered for the Messaging API [here](https://dev.telstra.com). |  |  * Content-Language -  <br>  |
| **403** | Forbidden  | code | suggested_action | | :--- | :--- | | RESOURCE_AUTH_ERR | Check the permissions associated with your account. | | INSUFFICIENT_SCOPE | The access token you generated does not have sufficient permissions for this request. |  |  * Content-Language -  <br>  |
| **404** | Not Found  | code | suggested_action | | :--- | :--- | | RESOURCE_TEMP_ERR | Check the API status page to see if an active incident is causing a temporary issue with the resource. | | RESOURCE_NOT_FOUND | Check the endpoint is correct. |  |  * Content-Language -  <br>  |
| **405** | Method Not Allowed  | code | suggested_action | | :--- | :--- | | METHOD_INVALID | Ensure the method is GET. |  |  * Content-Language -  <br>  |
| **429** | Too Many Requests  | code | suggested_action | | :--- | :--- | | TOO_MANY_REQUESTS | Reduce the number of concurrent calls. |  |  * Content-Language -  <br>  * Retry-After -  <br>  |
| **500** | Internal Server Error  | code | suggested_action | | :--- | :--- | | INTERNAL_TIMEOUT | Try the call again. If the issue persists, check the API [status page](https://dev.telstra.com/api/status) to see if there&#39;s an active incident. | | INTERNAL_SERVER_ERR | Check the API [status page](https://dev.telstra.com/api/status) to see if an active incident is causing the internal error. | | NETWORK_ERR | Please try again later. |  |  * Content-Language -  <br>  |
| **504** | Gateway timeout  | code | suggested_action | | :--- | :--- | | GATEWAY_TIMEOUT | The service is temporarily down. Check the [API Live Status page] (https://dev.telstra.com/api/status) or [contact support](mailto:telstradev@team.telstra.com). |  |  * Content-Language -  <br>  |
| **0** | Unexpected  |  * Content-Language -  <br>  |

