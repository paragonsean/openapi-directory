# ProxyApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**ioTSpacesCheckNameAvailability**](ProxyApi.md#ioTSpacesCheckNameAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.IoTSpaces/checkNameAvailability |  |
| [**operationsList**](ProxyApi.md#operationsList) | **GET** /providers/Microsoft.IoTSpaces/operations |  |


<a id="ioTSpacesCheckNameAvailability"></a>
# **ioTSpacesCheckNameAvailability**
> IoTSpacesNameAvailabilityInfo ioTSpacesCheckNameAvailability(apiVersion, subscriptionId, operationInputs)



Check if an IoTSpaces instance name is available.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProxyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProxyApi apiInstance = new ProxyApi(defaultClient);
    String apiVersion = "2017-10-01-preview"; // String | The version of the API.
    UUID subscriptionId = UUID.randomUUID(); // UUID | The subscription identifier.
    OperationInputs operationInputs = new OperationInputs(); // OperationInputs | Set the name parameter in the OperationInputs structure to the name of the IoTSpaces instance to check.
    try {
      IoTSpacesNameAvailabilityInfo result = apiInstance.ioTSpacesCheckNameAvailability(apiVersion, subscriptionId, operationInputs);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProxyApi#ioTSpacesCheckNameAvailability");
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
| **apiVersion** | **String**| The version of the API. | [enum: 2017-10-01-preview] |
| **subscriptionId** | **UUID**| The subscription identifier. | |
| **operationInputs** | [**OperationInputs**](OperationInputs.md)| Set the name parameter in the OperationInputs structure to the name of the IoTSpaces instance to check. | |

### Return type

[**IoTSpacesNameAvailabilityInfo**](IoTSpacesNameAvailabilityInfo.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | This is a synchronous operation. The body contains a JSON-serialized response that specifies whether the IoTSpaces service name is available. If the name is not available, the body contains the reason. |  -  |
| **0** | DefaultErrorResponse |  -  |

<a id="operationsList"></a>
# **operationsList**
> OperationListResult operationsList(apiVersion)



Lists all of the available IoTSpaces service REST API operations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProxyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProxyApi apiInstance = new ProxyApi(defaultClient);
    String apiVersion = "2017-10-01-preview"; // String | The version of the API.
    try {
      OperationListResult result = apiInstance.operationsList(apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProxyApi#operationsList");
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
| **apiVersion** | **String**| The version of the API. | [enum: 2017-10-01-preview] |

### Return type

[**OperationListResult**](OperationListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | DefaultErrorResponse |  -  |

