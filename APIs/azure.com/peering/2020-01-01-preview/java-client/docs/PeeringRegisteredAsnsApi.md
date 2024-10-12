# PeeringRegisteredAsnsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**registeredAsnsCreateOrUpdate**](PeeringRegisteredAsnsApi.md#registeredAsnsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Peering/peerings/{peeringName}/registeredAsns/{registeredAsnName} |  |
| [**registeredAsnsDelete**](PeeringRegisteredAsnsApi.md#registeredAsnsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Peering/peerings/{peeringName}/registeredAsns/{registeredAsnName} |  |
| [**registeredAsnsGet**](PeeringRegisteredAsnsApi.md#registeredAsnsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Peering/peerings/{peeringName}/registeredAsns/{registeredAsnName} |  |
| [**registeredAsnsListByPeering**](PeeringRegisteredAsnsApi.md#registeredAsnsListByPeering) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Peering/peerings/{peeringName}/registeredAsns |  |


<a id="registeredAsnsCreateOrUpdate"></a>
# **registeredAsnsCreateOrUpdate**
> PeeringRegisteredAsn registeredAsnsCreateOrUpdate(resourceGroupName, peeringName, registeredAsnName, subscriptionId, apiVersion, registeredAsn)



Creates a new registered ASN with the specified name under the given subscription, resource group and peering.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeeringRegisteredAsnsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PeeringRegisteredAsnsApi apiInstance = new PeeringRegisteredAsnsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String peeringName = "peeringName_example"; // String | The name of the peering.
    String registeredAsnName = "registeredAsnName_example"; // String | The name of the ASN.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    PeeringRegisteredAsn registeredAsn = new PeeringRegisteredAsn(); // PeeringRegisteredAsn | The properties needed to create a registered ASN.
    try {
      PeeringRegisteredAsn result = apiInstance.registeredAsnsCreateOrUpdate(resourceGroupName, peeringName, registeredAsnName, subscriptionId, apiVersion, registeredAsn);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeeringRegisteredAsnsApi#registeredAsnsCreateOrUpdate");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **peeringName** | **String**| The name of the peering. | |
| **registeredAsnName** | **String**| The name of the ASN. | |
| **subscriptionId** | **String**| The Azure subscription ID. | |
| **apiVersion** | **String**| The client API version. | |
| **registeredAsn** | [**PeeringRegisteredAsn**](PeeringRegisteredAsn.md)| The properties needed to create a registered ASN. | |

### Return type

[**PeeringRegisteredAsn**](PeeringRegisteredAsn.md)

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

<a id="registeredAsnsDelete"></a>
# **registeredAsnsDelete**
> registeredAsnsDelete(resourceGroupName, peeringName, registeredAsnName, subscriptionId, apiVersion)



Deletes an existing registered ASN with the specified name under the given subscription, resource group and peering.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeeringRegisteredAsnsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PeeringRegisteredAsnsApi apiInstance = new PeeringRegisteredAsnsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String peeringName = "peeringName_example"; // String | The name of the peering.
    String registeredAsnName = "registeredAsnName_example"; // String | The name of the registered ASN.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    try {
      apiInstance.registeredAsnsDelete(resourceGroupName, peeringName, registeredAsnName, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeeringRegisteredAsnsApi#registeredAsnsDelete");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **peeringName** | **String**| The name of the peering. | |
| **registeredAsnName** | **String**| The name of the registered ASN. | |
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
| **204** | NoContent |  -  |
| **0** | Error response describing why the operation has failed. |  -  |

<a id="registeredAsnsGet"></a>
# **registeredAsnsGet**
> PeeringRegisteredAsn registeredAsnsGet(resourceGroupName, peeringName, registeredAsnName, subscriptionId, apiVersion)



Gets an existing registered ASN with the specified name under the given subscription, resource group and peering.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeeringRegisteredAsnsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PeeringRegisteredAsnsApi apiInstance = new PeeringRegisteredAsnsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String peeringName = "peeringName_example"; // String | The name of the peering.
    String registeredAsnName = "registeredAsnName_example"; // String | The name of the registered ASN.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    try {
      PeeringRegisteredAsn result = apiInstance.registeredAsnsGet(resourceGroupName, peeringName, registeredAsnName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeeringRegisteredAsnsApi#registeredAsnsGet");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **peeringName** | **String**| The name of the peering. | |
| **registeredAsnName** | **String**| The name of the registered ASN. | |
| **subscriptionId** | **String**| The Azure subscription ID. | |
| **apiVersion** | **String**| The client API version. | |

### Return type

[**PeeringRegisteredAsn**](PeeringRegisteredAsn.md)

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

<a id="registeredAsnsListByPeering"></a>
# **registeredAsnsListByPeering**
> PeeringRegisteredAsnListResult registeredAsnsListByPeering(resourceGroupName, peeringName, subscriptionId, apiVersion)



Lists all registered ASNs under the given subscription, resource group and peering.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeeringRegisteredAsnsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PeeringRegisteredAsnsApi apiInstance = new PeeringRegisteredAsnsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String peeringName = "peeringName_example"; // String | The name of the peering.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    try {
      PeeringRegisteredAsnListResult result = apiInstance.registeredAsnsListByPeering(resourceGroupName, peeringName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeeringRegisteredAsnsApi#registeredAsnsListByPeering");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **peeringName** | **String**| The name of the peering. | |
| **subscriptionId** | **String**| The Azure subscription ID. | |
| **apiVersion** | **String**| The client API version. | |

### Return type

[**PeeringRegisteredAsnListResult**](PeeringRegisteredAsnListResult.md)

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

