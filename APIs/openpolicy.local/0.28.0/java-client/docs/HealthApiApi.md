# HealthApiApi

All URIs are relative to *http://openpolicy.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getHealth**](HealthApiApi.md#getHealth) | **GET** /health | Health |


<a id="getHealth"></a>
# **getHealth**
> getHealth(bundles, plugins)

Health

This API endpoint verifies that the server is operational.  The response from the server is either 200 or 500: - **200** - OPA service is healthy. If &#x60;bundles&#x60; is true, then all configured bundles have been activated. If &#x60;plugins&#x60; is true, then all plugins are in an &#39;OK&#39; state. - **500** - OPA service is *not* healthy. If &#x60;bundles&#x60; is true, at least one of configured bundles has not yet been activated. If &#x60;plugins&#x60; is true, at least one plugins is in a &#39;not OK&#39; state.  --- **Note** This check is only for initial bundle activation. Subsequent downloads will not affect the health check.  Use the **status** endpoint (in the (management API)[management.html]) for more fine-grained bundle status monitoring.  ---

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HealthApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://openpolicy.local");

    HealthApiApi apiInstance = new HealthApiApi(defaultClient);
    Boolean bundles = true; // Boolean | Reports on bundle activation status (useful for 'ready' checks at startup).  This includes any discovery bundles or bundles defined in the loaded discovery configuration.
    Boolean plugins = false; // Boolean | Reports on plugin status
    try {
      apiInstance.getHealth(bundles, plugins);
    } catch (ApiException e) {
      System.err.println("Exception when calling HealthApiApi#getHealth");
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
| **bundles** | **Boolean**| Reports on bundle activation status (useful for &#39;ready&#39; checks at startup).  This includes any discovery bundles or bundles defined in the loaded discovery configuration. | [optional] |
| **plugins** | **Boolean**| Reports on plugin status | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OPA service is healthy |  -  |
| **500** | OPA service is not healthy |  -  |

