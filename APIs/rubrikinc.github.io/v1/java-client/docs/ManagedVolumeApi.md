# ManagedVolumeApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createManagedVolumeGenerateScriptJob**](ManagedVolumeApi.md#createManagedVolumeGenerateScriptJob) | **POST** /managed_volume/snapshot/export/{id}/script | Generate and download unified view script |


<a id="createManagedVolumeGenerateScriptJob"></a>
# **createManagedVolumeGenerateScriptJob**
> AsyncRequestStatus createManagedVolumeGenerateScriptJob(id)

Generate and download unified view script

Start an asynchronous job to generate and download a script to unify export paths across channels in managed volume export.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedVolumeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ManagedVolumeApi apiInstance = new ManagedVolumeApi(defaultClient);
    String id = "id_example"; // String | ID of snapshot export.
    try {
      AsyncRequestStatus result = apiInstance.createManagedVolumeGenerateScriptJob(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedVolumeApi#createManagedVolumeGenerateScriptJob");
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
| **id** | **String**| ID of snapshot export. | |

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Status of an asynchronous job to generate unified view script. |  -  |

