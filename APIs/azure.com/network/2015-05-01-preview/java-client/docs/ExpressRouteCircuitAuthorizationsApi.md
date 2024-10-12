# ExpressRouteCircuitAuthorizationsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**expressRouteCircuitAuthorizationsCreateOrUpdate**](ExpressRouteCircuitAuthorizationsApi.md#expressRouteCircuitAuthorizationsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCircuits/{circuitName}/authorizations/{authorizationName} |  |
| [**expressRouteCircuitAuthorizationsDelete**](ExpressRouteCircuitAuthorizationsApi.md#expressRouteCircuitAuthorizationsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCircuits/{circuitName}/authorizations/{authorizationName} |  |
| [**expressRouteCircuitAuthorizationsGet**](ExpressRouteCircuitAuthorizationsApi.md#expressRouteCircuitAuthorizationsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCircuits/{circuitName}/authorizations/{authorizationName} |  |
| [**expressRouteCircuitAuthorizationsList**](ExpressRouteCircuitAuthorizationsApi.md#expressRouteCircuitAuthorizationsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCircuits/{circuitName}/authorizations |  |


<a id="expressRouteCircuitAuthorizationsCreateOrUpdate"></a>
# **expressRouteCircuitAuthorizationsCreateOrUpdate**
> ExpressRouteCircuitAuthorization expressRouteCircuitAuthorizationsCreateOrUpdate(resourceGroupName, circuitName, authorizationName, apiVersion, subscriptionId, authorizationParameters)



The Put Authorization operation creates/updates an authorization in the specified ExpressRouteCircuits

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpressRouteCircuitAuthorizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExpressRouteCircuitAuthorizationsApi apiInstance = new ExpressRouteCircuitAuthorizationsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String circuitName = "circuitName_example"; // String | The name of the express route circuit.
    String authorizationName = "authorizationName_example"; // String | The name of the authorization.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    ExpressRouteCircuitAuthorization authorizationParameters = new ExpressRouteCircuitAuthorization(); // ExpressRouteCircuitAuthorization | Parameters supplied to the create/update ExpressRouteCircuitAuthorization operation
    try {
      ExpressRouteCircuitAuthorization result = apiInstance.expressRouteCircuitAuthorizationsCreateOrUpdate(resourceGroupName, circuitName, authorizationName, apiVersion, subscriptionId, authorizationParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpressRouteCircuitAuthorizationsApi#expressRouteCircuitAuthorizationsCreateOrUpdate");
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
| **circuitName** | **String**| The name of the express route circuit. | |
| **authorizationName** | **String**| The name of the authorization. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **authorizationParameters** | [**ExpressRouteCircuitAuthorization**](ExpressRouteCircuitAuthorization.md)| Parameters supplied to the create/update ExpressRouteCircuitAuthorization operation | |

### Return type

[**ExpressRouteCircuitAuthorization**](ExpressRouteCircuitAuthorization.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **201** |  |  -  |

<a id="expressRouteCircuitAuthorizationsDelete"></a>
# **expressRouteCircuitAuthorizationsDelete**
> expressRouteCircuitAuthorizationsDelete(resourceGroupName, circuitName, authorizationName, apiVersion, subscriptionId)



The delete authorization operation deletes the specified authorization from the specified ExpressRouteCircuit.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpressRouteCircuitAuthorizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExpressRouteCircuitAuthorizationsApi apiInstance = new ExpressRouteCircuitAuthorizationsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String circuitName = "circuitName_example"; // String | The name of the express route circuit.
    String authorizationName = "authorizationName_example"; // String | The name of the authorization.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.expressRouteCircuitAuthorizationsDelete(resourceGroupName, circuitName, authorizationName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpressRouteCircuitAuthorizationsApi#expressRouteCircuitAuthorizationsDelete");
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
| **circuitName** | **String**| The name of the express route circuit. | |
| **authorizationName** | **String**| The name of the authorization. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **202** |  |  -  |
| **204** |  |  -  |

<a id="expressRouteCircuitAuthorizationsGet"></a>
# **expressRouteCircuitAuthorizationsGet**
> ExpressRouteCircuitAuthorization expressRouteCircuitAuthorizationsGet(resourceGroupName, circuitName, authorizationName, apiVersion, subscriptionId)



The GET authorization operation retrieves the specified authorization from the specified ExpressRouteCircuit.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpressRouteCircuitAuthorizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExpressRouteCircuitAuthorizationsApi apiInstance = new ExpressRouteCircuitAuthorizationsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String circuitName = "circuitName_example"; // String | The name of the express route circuit.
    String authorizationName = "authorizationName_example"; // String | The name of the authorization.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      ExpressRouteCircuitAuthorization result = apiInstance.expressRouteCircuitAuthorizationsGet(resourceGroupName, circuitName, authorizationName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpressRouteCircuitAuthorizationsApi#expressRouteCircuitAuthorizationsGet");
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
| **circuitName** | **String**| The name of the express route circuit. | |
| **authorizationName** | **String**| The name of the authorization. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**ExpressRouteCircuitAuthorization**](ExpressRouteCircuitAuthorization.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="expressRouteCircuitAuthorizationsList"></a>
# **expressRouteCircuitAuthorizationsList**
> AuthorizationListResult expressRouteCircuitAuthorizationsList(resourceGroupName, circuitName, apiVersion, subscriptionId)



The List authorization operation retrieves all the authorizations in an ExpressRouteCircuit.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpressRouteCircuitAuthorizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExpressRouteCircuitAuthorizationsApi apiInstance = new ExpressRouteCircuitAuthorizationsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String circuitName = "circuitName_example"; // String | The name of the circuit.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      AuthorizationListResult result = apiInstance.expressRouteCircuitAuthorizationsList(resourceGroupName, circuitName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpressRouteCircuitAuthorizationsApi#expressRouteCircuitAuthorizationsList");
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
| **circuitName** | **String**| The name of the circuit. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**AuthorizationListResult**](AuthorizationListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

