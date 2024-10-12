# HypervVmApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getHypervVirtualMachineForceFullSpec**](HypervVmApi.md#getHypervVirtualMachineForceFullSpec) | **GET** /hyperv/vm/{id}/request/force_full_snapshot | Retrieve the configuration which has been set for forcing a full snapshot for a Hyper-V Virtual Machine |
| [**requestHypervVirtualMachineForceFullSnapshot**](HypervVmApi.md#requestHypervVirtualMachineForceFullSnapshot) | **POST** /hyperv/vm/{id}/request/force_full_snapshot | Request a full snapshot during next backup job of a Hyper-V virtual machine |


<a id="getHypervVirtualMachineForceFullSpec"></a>
# **getHypervVirtualMachineForceFullSpec**
> HypervVirtualMachineForceFullResponse getHypervVirtualMachineForceFullSpec(id)

Retrieve the configuration which has been set for forcing a full snapshot for a Hyper-V Virtual Machine

Retrieve the configuration created to force a full snapshot for a Hyper-V Virtual Machine.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HypervVmApi;

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

    HypervVmApi apiInstance = new HypervVmApi(defaultClient);
    String id = "id_example"; // String | The ID of the Hyper-V virtual machine.
    try {
      HypervVirtualMachineForceFullResponse result = apiInstance.getHypervVirtualMachineForceFullSpec(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HypervVmApi#getHypervVirtualMachineForceFullSpec");
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
| **id** | **String**| The ID of the Hyper-V virtual machine. | |

### Return type

[**HypervVirtualMachineForceFullResponse**](HypervVirtualMachineForceFullResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return the configuration created to force a full snapshot on the Hyper-V virtual machine. |  -  |

<a id="requestHypervVirtualMachineForceFullSnapshot"></a>
# **requestHypervVirtualMachineForceFullSnapshot**
> HypervVirtualMachineForceFullResponse requestHypervVirtualMachineForceFullSnapshot(id, hypervVirtualMachineForceFullRequest)

Request a full snapshot during next backup job of a Hyper-V virtual machine

Request a full snapshot during the next backup job of a Hyper-V virtual machine.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HypervVmApi;

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

    HypervVmApi apiInstance = new HypervVmApi(defaultClient);
    String id = "id_example"; // String | ID of the Hyper-V virtual machine.
    HypervVirtualMachineForceFullRequest hypervVirtualMachineForceFullRequest = new HypervVirtualMachineForceFullRequest(); // HypervVirtualMachineForceFullRequest | Configuration created to force a full snapshot on the Hyper-V virtual machine.
    try {
      HypervVirtualMachineForceFullResponse result = apiInstance.requestHypervVirtualMachineForceFullSnapshot(id, hypervVirtualMachineForceFullRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HypervVmApi#requestHypervVirtualMachineForceFullSnapshot");
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
| **id** | **String**| ID of the Hyper-V virtual machine. | |
| **hypervVirtualMachineForceFullRequest** | [**HypervVirtualMachineForceFullRequest**](HypervVirtualMachineForceFullRequest.md)| Configuration created to force a full snapshot on the Hyper-V virtual machine. | |

### Return type

[**HypervVirtualMachineForceFullResponse**](HypervVirtualMachineForceFullResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Returns the Hyper-V virtual machine force full response containing the configuration for each virtual disk that requested a forced full snapshot. |  -  |

