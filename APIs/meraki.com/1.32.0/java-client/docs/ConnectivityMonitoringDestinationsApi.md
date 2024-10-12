# ConnectivityMonitoringDestinationsApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNetworkApplianceConnectivityMonitoringDestinations_1**](ConnectivityMonitoringDestinationsApi.md#getNetworkApplianceConnectivityMonitoringDestinations_1) | **GET** /networks/{networkId}/appliance/connectivityMonitoringDestinations | Return the connectivity testing destinations for an MX network |
| [**getNetworkCellularGatewayConnectivityMonitoringDestinations_1**](ConnectivityMonitoringDestinationsApi.md#getNetworkCellularGatewayConnectivityMonitoringDestinations_1) | **GET** /networks/{networkId}/cellularGateway/connectivityMonitoringDestinations | Return the connectivity testing destinations for an MG network |
| [**updateNetworkApplianceConnectivityMonitoringDestinations_1**](ConnectivityMonitoringDestinationsApi.md#updateNetworkApplianceConnectivityMonitoringDestinations_1) | **PUT** /networks/{networkId}/appliance/connectivityMonitoringDestinations | Update the connectivity testing destinations for an MX network |
| [**updateNetworkCellularGatewayConnectivityMonitoringDestinations_1**](ConnectivityMonitoringDestinationsApi.md#updateNetworkCellularGatewayConnectivityMonitoringDestinations_1) | **PUT** /networks/{networkId}/cellularGateway/connectivityMonitoringDestinations | Update the connectivity testing destinations for an MG network |


<a id="getNetworkApplianceConnectivityMonitoringDestinations_1"></a>
# **getNetworkApplianceConnectivityMonitoringDestinations_1**
> Object getNetworkApplianceConnectivityMonitoringDestinations_1(networkId)

Return the connectivity testing destinations for an MX network

Return the connectivity testing destinations for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConnectivityMonitoringDestinationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ConnectivityMonitoringDestinationsApi apiInstance = new ConnectivityMonitoringDestinationsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkApplianceConnectivityMonitoringDestinations_1(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConnectivityMonitoringDestinationsApi#getNetworkApplianceConnectivityMonitoringDestinations_1");
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
| **networkId** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkCellularGatewayConnectivityMonitoringDestinations_1"></a>
# **getNetworkCellularGatewayConnectivityMonitoringDestinations_1**
> Object getNetworkCellularGatewayConnectivityMonitoringDestinations_1(networkId)

Return the connectivity testing destinations for an MG network

Return the connectivity testing destinations for an MG network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConnectivityMonitoringDestinationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ConnectivityMonitoringDestinationsApi apiInstance = new ConnectivityMonitoringDestinationsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkCellularGatewayConnectivityMonitoringDestinations_1(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConnectivityMonitoringDestinationsApi#getNetworkCellularGatewayConnectivityMonitoringDestinations_1");
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
| **networkId** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkApplianceConnectivityMonitoringDestinations_1"></a>
# **updateNetworkApplianceConnectivityMonitoringDestinations_1**
> Object updateNetworkApplianceConnectivityMonitoringDestinations_1(networkId, updateNetworkApplianceConnectivityMonitoringDestinationsRequest)

Update the connectivity testing destinations for an MX network

Update the connectivity testing destinations for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConnectivityMonitoringDestinationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ConnectivityMonitoringDestinationsApi apiInstance = new ConnectivityMonitoringDestinationsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkApplianceConnectivityMonitoringDestinationsRequest updateNetworkApplianceConnectivityMonitoringDestinationsRequest = new UpdateNetworkApplianceConnectivityMonitoringDestinationsRequest(); // UpdateNetworkApplianceConnectivityMonitoringDestinationsRequest | 
    try {
      Object result = apiInstance.updateNetworkApplianceConnectivityMonitoringDestinations_1(networkId, updateNetworkApplianceConnectivityMonitoringDestinationsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConnectivityMonitoringDestinationsApi#updateNetworkApplianceConnectivityMonitoringDestinations_1");
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
| **networkId** | **String**|  | |
| **updateNetworkApplianceConnectivityMonitoringDestinationsRequest** | [**UpdateNetworkApplianceConnectivityMonitoringDestinationsRequest**](UpdateNetworkApplianceConnectivityMonitoringDestinationsRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkCellularGatewayConnectivityMonitoringDestinations_1"></a>
# **updateNetworkCellularGatewayConnectivityMonitoringDestinations_1**
> Object updateNetworkCellularGatewayConnectivityMonitoringDestinations_1(networkId, updateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest)

Update the connectivity testing destinations for an MG network

Update the connectivity testing destinations for an MG network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConnectivityMonitoringDestinationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ConnectivityMonitoringDestinationsApi apiInstance = new ConnectivityMonitoringDestinationsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest updateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest = new UpdateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest(); // UpdateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest | 
    try {
      Object result = apiInstance.updateNetworkCellularGatewayConnectivityMonitoringDestinations_1(networkId, updateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConnectivityMonitoringDestinationsApi#updateNetworkCellularGatewayConnectivityMonitoringDestinations_1");
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
| **networkId** | **String**|  | |
| **updateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest** | [**UpdateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest**](UpdateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

