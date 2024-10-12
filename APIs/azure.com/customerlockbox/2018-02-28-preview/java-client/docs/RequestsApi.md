# RequestsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**requestsGet**](RequestsApi.md#requestsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.CustomerLockbox/requests/{requestId} |  |
| [**requestsList**](RequestsApi.md#requestsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.CustomerLockbox/requests |  |
| [**requestsUpdateStatus**](RequestsApi.md#requestsUpdateStatus) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.CustomerLockbox/requests/{requestId}/UpdateApproval |  |


<a id="requestsGet"></a>
# **requestsGet**
> LockboxRequestResponse requestsGet(requestId, subscriptionId, apiVersion)



Get Customer Lockbox request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RequestsApi apiInstance = new RequestsApi(defaultClient);
    String requestId = "requestId_example"; // String | The Lockbox request ID.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    try {
      LockboxRequestResponse result = apiInstance.requestsGet(requestId, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RequestsApi#requestsGet");
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
| **requestId** | **String**| The Lockbox request ID. | |
| **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | |
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |

### Return type

[**LockboxRequestResponse**](LockboxRequestResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Retrieval of Customer Lockbox request successful. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="requestsList"></a>
# **requestsList**
> RequestListResult requestsList(subscriptionId, $filter)



Lists all of the Lockbox requests in the given subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RequestsApi apiInstance = new RequestsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    String $filter = "$filter_example"; // String | The $filter OData query parameter. Only filter by request status is supported, e.g $filter=properties/status eq 'Pending'
    try {
      RequestListResult result = apiInstance.requestsList(subscriptionId, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RequestsApi#requestsList");
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
| **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | |
| **$filter** | **String**| The $filter OData query parameter. Only filter by request status is supported, e.g $filter&#x3D;properties/status eq &#39;Pending&#39; | [optional] |

### Return type

[**RequestListResult**](RequestListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully listed the Lockbox requests under the given subscription. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="requestsUpdateStatus"></a>
# **requestsUpdateStatus**
> Approval requestsUpdateStatus(subscriptionId, requestId, apiVersion, approval)



Update Customer Lockbox request approval status API

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RequestsApi apiInstance = new RequestsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    String requestId = "requestId_example"; // String | The Lockbox request ID.
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    Approval approval = new Approval(); // Approval | The approval object to update request status.
    try {
      Approval result = apiInstance.requestsUpdateStatus(subscriptionId, requestId, apiVersion, approval);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RequestsApi#requestsUpdateStatus");
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
| **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | |
| **requestId** | **String**| The Lockbox request ID. | |
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |
| **approval** | [**Approval**](Approval.md)| The approval object to update request status. | |

### Return type

[**Approval**](Approval.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update of Request Status successful |  -  |
| **0** | Error response describing why the operation failed. |  -  |

