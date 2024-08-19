# ProxyApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**operationsList**](ProxyApi.md#operationsList) | **GET** /providers/Microsoft.HealthcareApis/operations |  |
| [**servicesCheckNameAvailability**](ProxyApi.md#servicesCheckNameAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.HealthcareApis/checkNameAvailability |  |


<a id="operationsList"></a>
# **operationsList**
> OperationListResult operationsList(apiVersion)



Lists all of the available Healthcare service REST API operations.

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
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
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
| **apiVersion** | **String**| Client Api Version. | |

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

<a id="servicesCheckNameAvailability"></a>
# **servicesCheckNameAvailability**
> ServicesNameAvailabilityInfo servicesCheckNameAvailability(apiVersion, subscriptionId, checkNameAvailabilityInputs)



Check if a service instance name is available.

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
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    CheckNameAvailabilityParameters checkNameAvailabilityInputs = new CheckNameAvailabilityParameters(); // CheckNameAvailabilityParameters | Set the name parameter in the CheckNameAvailabilityParameters structure to the name of the service instance to check.
    try {
      ServicesNameAvailabilityInfo result = apiInstance.servicesCheckNameAvailability(apiVersion, subscriptionId, checkNameAvailabilityInputs);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProxyApi#servicesCheckNameAvailability");
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| The subscription identifier. | |
| **checkNameAvailabilityInputs** | [**CheckNameAvailabilityParameters**](CheckNameAvailabilityParameters.md)| Set the name parameter in the CheckNameAvailabilityParameters structure to the name of the service instance to check. | |

### Return type

[**ServicesNameAvailabilityInfo**](ServicesNameAvailabilityInfo.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | This is a synchronous operation. The body contains a JSON-serialized response that specifies whether the service name is available. If the name is not available, the body contains the reason. |  -  |
| **0** | DefaultErrorResponse |  -  |

