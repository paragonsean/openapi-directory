# ActivationsApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**activationsCreateOrUpdate**](ActivationsApi.md#activationsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroup}/providers/Microsoft.AzureBridge.Admin/activations/{activationName} |  |
| [**activationsDelete**](ActivationsApi.md#activationsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroup}/providers/Microsoft.AzureBridge.Admin/activations/{activationName} |  |
| [**activationsGet**](ActivationsApi.md#activationsGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroup}/providers/Microsoft.AzureBridge.Admin/activations/{activationName} |  |
| [**activationsList**](ActivationsApi.md#activationsList) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroup}/providers/Microsoft.AzureBridge.Admin/activations |  |


<a id="activationsCreateOrUpdate"></a>
# **activationsCreateOrUpdate**
> ActivationResource activationsCreateOrUpdate(subscriptionId, resourceGroup, activationName, apiVersion, activation)



Create a new activation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ActivationsApi apiInstance = new ActivationsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    String resourceGroup = "resourceGroup_example"; // String | The resource group the resource is located under.
    String activationName = "activationName_example"; // String | Name of the activation.
    String apiVersion = "2016-01-01"; // String | Client Api Version.
    Activation activation = new Activation(); // Activation | new activation.
    try {
      ActivationResource result = apiInstance.activationsCreateOrUpdate(subscriptionId, resourceGroup, activationName, apiVersion, activation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivationsApi#activationsCreateOrUpdate");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call. | |
| **resourceGroup** | **String**| The resource group the resource is located under. | |
| **activationName** | **String**| Name of the activation. | |
| **apiVersion** | **String**| Client Api Version. | [default to 2016-01-01] |
| **activation** | [**Activation**](Activation.md)| new activation. | |

### Return type

[**ActivationResource**](ActivationResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="activationsDelete"></a>
# **activationsDelete**
> ActivationResource activationsDelete(subscriptionId, resourceGroup, activationName, apiVersion)



Delete an activation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ActivationsApi apiInstance = new ActivationsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    String resourceGroup = "resourceGroup_example"; // String | The resource group the resource is located under.
    String activationName = "activationName_example"; // String | Name of the activation.
    String apiVersion = "2016-01-01"; // String | Client Api Version.
    try {
      ActivationResource result = apiInstance.activationsDelete(subscriptionId, resourceGroup, activationName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivationsApi#activationsDelete");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call. | |
| **resourceGroup** | **String**| The resource group the resource is located under. | |
| **activationName** | **String**| Name of the activation. | |
| **apiVersion** | **String**| Client Api Version. | [default to 2016-01-01] |

### Return type

[**ActivationResource**](ActivationResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="activationsGet"></a>
# **activationsGet**
> ActivationResource activationsGet(subscriptionId, resourceGroup, activationName, apiVersion)



Returns activation name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ActivationsApi apiInstance = new ActivationsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    String resourceGroup = "resourceGroup_example"; // String | The resource group the resource is located under.
    String activationName = "activationName_example"; // String | Name of the activation.
    String apiVersion = "2016-01-01"; // String | Client Api Version.
    try {
      ActivationResource result = apiInstance.activationsGet(subscriptionId, resourceGroup, activationName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivationsApi#activationsGet");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call. | |
| **resourceGroup** | **String**| The resource group the resource is located under. | |
| **activationName** | **String**| Name of the activation. | |
| **apiVersion** | **String**| Client Api Version. | [default to 2016-01-01] |

### Return type

[**ActivationResource**](ActivationResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not Found |  -  |

<a id="activationsList"></a>
# **activationsList**
> ActivationResourcesPage activationsList(subscriptionId, resourceGroup, apiVersion)



Returns the list of activations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ActivationsApi apiInstance = new ActivationsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    String resourceGroup = "resourceGroup_example"; // String | The resource group the resource is located under.
    String apiVersion = "2016-01-01"; // String | Client Api Version.
    try {
      ActivationResourcesPage result = apiInstance.activationsList(subscriptionId, resourceGroup, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivationsApi#activationsList");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call. | |
| **resourceGroup** | **String**| The resource group the resource is located under. | |
| **apiVersion** | **String**| Client Api Version. | [default to 2016-01-01] |

### Return type

[**ActivationResourcesPage**](ActivationResourcesPage.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

