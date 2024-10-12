# TenantBackfillApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**startTenantBackfill**](TenantBackfillApi.md#startTenantBackfill) | **POST** /providers/Microsoft.Management/startTenantBackfill |  |
| [**tenantBackfillStatus**](TenantBackfillApi.md#tenantBackfillStatus) | **POST** /providers/Microsoft.Management/tenantBackfillStatus |  |


<a id="startTenantBackfill"></a>
# **startTenantBackfill**
> TenantBackfillStatusResult startTenantBackfill(apiVersion)



Starts backfilling subscriptions for the Tenant.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TenantBackfillApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TenantBackfillApi apiInstance = new TenantBackfillApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-01-01-preview.
    try {
      TenantBackfillStatusResult result = apiInstance.startTenantBackfill(apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TenantBackfillApi#startTenantBackfill");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-01-01-preview. | |

### Return type

[**TenantBackfillStatusResult**](TenantBackfillStatusResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="tenantBackfillStatus"></a>
# **tenantBackfillStatus**
> TenantBackfillStatusResult tenantBackfillStatus(apiVersion)



Gets tenant backfill status

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TenantBackfillApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TenantBackfillApi apiInstance = new TenantBackfillApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-01-01-preview.
    try {
      TenantBackfillStatusResult result = apiInstance.tenantBackfillStatus(apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TenantBackfillApi#tenantBackfillStatus");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-01-01-preview. | |

### Return type

[**TenantBackfillStatusResult**](TenantBackfillStatusResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

