# EndpointsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**endpointsCreateOrUpdate**](EndpointsApi.md#endpointsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/trafficmanagerprofiles/{profileName}/{endpointType}/{endpointName} |  |
| [**endpointsDelete**](EndpointsApi.md#endpointsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/trafficmanagerprofiles/{profileName}/{endpointType}/{endpointName} |  |
| [**endpointsGet**](EndpointsApi.md#endpointsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/trafficmanagerprofiles/{profileName}/{endpointType}/{endpointName} |  |
| [**endpointsUpdate**](EndpointsApi.md#endpointsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/trafficmanagerprofiles/{profileName}/{endpointType}/{endpointName} |  |


<a id="endpointsCreateOrUpdate"></a>
# **endpointsCreateOrUpdate**
> Endpoint endpointsCreateOrUpdate(resourceGroupName, profileName, endpointType, endpointName, apiVersion, subscriptionId, parameters)



Create or update a Traffic Manager endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EndpointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    EndpointsApi apiInstance = new EndpointsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Traffic Manager endpoint to be created or updated.
    String profileName = "profileName_example"; // String | The name of the Traffic Manager profile.
    String endpointType = "endpointType_example"; // String | The type of the Traffic Manager endpoint to be created or updated.
    String endpointName = "endpointName_example"; // String | The name of the Traffic Manager endpoint to be created or updated.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    Endpoint parameters = new Endpoint(); // Endpoint | The Traffic Manager endpoint parameters supplied to the CreateOrUpdate operation.
    try {
      Endpoint result = apiInstance.endpointsCreateOrUpdate(resourceGroupName, profileName, endpointType, endpointName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EndpointsApi#endpointsCreateOrUpdate");
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
| **resourceGroupName** | **String**| The name of the resource group containing the Traffic Manager endpoint to be created or updated. | |
| **profileName** | **String**| The name of the Traffic Manager profile. | |
| **endpointType** | **String**| The type of the Traffic Manager endpoint to be created or updated. | |
| **endpointName** | **String**| The name of the Traffic Manager endpoint to be created or updated. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**Endpoint**](Endpoint.md)| The Traffic Manager endpoint parameters supplied to the CreateOrUpdate operation. | |

### Return type

[**Endpoint**](Endpoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The created or updated Endpoint. |  -  |
| **201** | The created or updated Endpoint. |  -  |

<a id="endpointsDelete"></a>
# **endpointsDelete**
> endpointsDelete(resourceGroupName, profileName, endpointType, endpointName, apiVersion, subscriptionId)



Deletes a Traffic Manager endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EndpointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    EndpointsApi apiInstance = new EndpointsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Traffic Manager endpoint to be deleted.
    String profileName = "profileName_example"; // String | The name of the Traffic Manager profile.
    String endpointType = "endpointType_example"; // String | The type of the Traffic Manager endpoint to be deleted.
    String endpointName = "endpointName_example"; // String | The name of the Traffic Manager endpoint to be deleted.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.endpointsDelete(resourceGroupName, profileName, endpointType, endpointName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling EndpointsApi#endpointsDelete");
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
| **resourceGroupName** | **String**| The name of the resource group containing the Traffic Manager endpoint to be deleted. | |
| **profileName** | **String**| The name of the Traffic Manager profile. | |
| **endpointType** | **String**| The type of the Traffic Manager endpoint to be deleted. | |
| **endpointName** | **String**| The name of the Traffic Manager endpoint to be deleted. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

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
| **200** |  |  -  |
| **204** |  |  -  |

<a id="endpointsGet"></a>
# **endpointsGet**
> Endpoint endpointsGet(resourceGroupName, profileName, endpointType, endpointName, apiVersion, subscriptionId)



Gets a Traffic Manager endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EndpointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    EndpointsApi apiInstance = new EndpointsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Traffic Manager endpoint.
    String profileName = "profileName_example"; // String | The name of the Traffic Manager profile.
    String endpointType = "endpointType_example"; // String | The type of the Traffic Manager endpoint.
    String endpointName = "endpointName_example"; // String | The name of the Traffic Manager endpoint.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      Endpoint result = apiInstance.endpointsGet(resourceGroupName, profileName, endpointType, endpointName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EndpointsApi#endpointsGet");
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
| **resourceGroupName** | **String**| The name of the resource group containing the Traffic Manager endpoint. | |
| **profileName** | **String**| The name of the Traffic Manager profile. | |
| **endpointType** | **String**| The type of the Traffic Manager endpoint. | |
| **endpointName** | **String**| The name of the Traffic Manager endpoint. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**Endpoint**](Endpoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Traffic Manager endpoint. |  -  |

<a id="endpointsUpdate"></a>
# **endpointsUpdate**
> Endpoint endpointsUpdate(resourceGroupName, profileName, endpointType, endpointName, apiVersion, subscriptionId, parameters)



Update a Traffic Manager endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EndpointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    EndpointsApi apiInstance = new EndpointsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Traffic Manager endpoint to be updated.
    String profileName = "profileName_example"; // String | The name of the Traffic Manager profile.
    String endpointType = "endpointType_example"; // String | The type of the Traffic Manager endpoint to be updated.
    String endpointName = "endpointName_example"; // String | The name of the Traffic Manager endpoint to be updated.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    Endpoint parameters = new Endpoint(); // Endpoint | The Traffic Manager endpoint parameters supplied to the Update operation.
    try {
      Endpoint result = apiInstance.endpointsUpdate(resourceGroupName, profileName, endpointType, endpointName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EndpointsApi#endpointsUpdate");
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
| **resourceGroupName** | **String**| The name of the resource group containing the Traffic Manager endpoint to be updated. | |
| **profileName** | **String**| The name of the Traffic Manager profile. | |
| **endpointType** | **String**| The type of the Traffic Manager endpoint to be updated. | |
| **endpointName** | **String**| The name of the Traffic Manager endpoint to be updated. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**Endpoint**](Endpoint.md)| The Traffic Manager endpoint parameters supplied to the Update operation. | |

### Return type

[**Endpoint**](Endpoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated Traffic Manager endpoint. |  -  |

