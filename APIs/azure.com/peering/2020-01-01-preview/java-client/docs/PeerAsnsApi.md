# PeerAsnsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**peerAsnsCreateOrUpdate**](PeerAsnsApi.md#peerAsnsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Peering/peerAsns/{peerAsnName} |  |
| [**peerAsnsDelete**](PeerAsnsApi.md#peerAsnsDelete) | **DELETE** /subscriptions/{subscriptionId}/providers/Microsoft.Peering/peerAsns/{peerAsnName} |  |
| [**peerAsnsGet**](PeerAsnsApi.md#peerAsnsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Peering/peerAsns/{peerAsnName} |  |
| [**peerAsnsListBySubscription**](PeerAsnsApi.md#peerAsnsListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Peering/peerAsns |  |


<a id="peerAsnsCreateOrUpdate"></a>
# **peerAsnsCreateOrUpdate**
> PeerAsn peerAsnsCreateOrUpdate(peerAsnName, subscriptionId, apiVersion, peerAsn)



Creates a new peer ASN or updates an existing peer ASN with the specified name under the given subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeerAsnsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PeerAsnsApi apiInstance = new PeerAsnsApi(defaultClient);
    String peerAsnName = "peerAsnName_example"; // String | The peer ASN name.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    PeerAsn peerAsn = new PeerAsn(); // PeerAsn | The peer ASN.
    try {
      PeerAsn result = apiInstance.peerAsnsCreateOrUpdate(peerAsnName, subscriptionId, apiVersion, peerAsn);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeerAsnsApi#peerAsnsCreateOrUpdate");
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
| **peerAsnName** | **String**| The peer ASN name. | |
| **subscriptionId** | **String**| The Azure subscription ID. | |
| **apiVersion** | **String**| The client API version. | |
| **peerAsn** | [**PeerAsn**](PeerAsn.md)| The peer ASN. | |

### Return type

[**PeerAsn**](PeerAsn.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **0** | Error response describing why the operation has failed. |  -  |

<a id="peerAsnsDelete"></a>
# **peerAsnsDelete**
> peerAsnsDelete(peerAsnName, subscriptionId, apiVersion)



Deletes an existing peer ASN with the specified name under the given subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeerAsnsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PeerAsnsApi apiInstance = new PeerAsnsApi(defaultClient);
    String peerAsnName = "peerAsnName_example"; // String | The peer ASN name.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    try {
      apiInstance.peerAsnsDelete(peerAsnName, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeerAsnsApi#peerAsnsDelete");
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
| **peerAsnName** | **String**| The peer ASN name. | |
| **subscriptionId** | **String**| The Azure subscription ID. | |
| **apiVersion** | **String**| The client API version. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **204** | No Content |  -  |
| **0** | Error response describing why the operation has failed. |  -  |

<a id="peerAsnsGet"></a>
# **peerAsnsGet**
> PeerAsn peerAsnsGet(peerAsnName, subscriptionId, apiVersion)



Gets the peer ASN with the specified name under the given subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeerAsnsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PeerAsnsApi apiInstance = new PeerAsnsApi(defaultClient);
    String peerAsnName = "peerAsnName_example"; // String | The peer ASN name.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    try {
      PeerAsn result = apiInstance.peerAsnsGet(peerAsnName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeerAsnsApi#peerAsnsGet");
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
| **peerAsnName** | **String**| The peer ASN name. | |
| **subscriptionId** | **String**| The Azure subscription ID. | |
| **apiVersion** | **String**| The client API version. | |

### Return type

[**PeerAsn**](PeerAsn.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation has failed. |  -  |

<a id="peerAsnsListBySubscription"></a>
# **peerAsnsListBySubscription**
> PeerAsnListResult peerAsnsListBySubscription(subscriptionId, apiVersion)



Lists all of the peer ASNs under the given subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeerAsnsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PeerAsnsApi apiInstance = new PeerAsnsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    try {
      PeerAsnListResult result = apiInstance.peerAsnsListBySubscription(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeerAsnsApi#peerAsnsListBySubscription");
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
| **subscriptionId** | **String**| The Azure subscription ID. | |
| **apiVersion** | **String**| The client API version. | |

### Return type

[**PeerAsnListResult**](PeerAsnListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation has failed. |  -  |

