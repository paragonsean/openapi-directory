# AppsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**appsCheckNameAvailability**](AppsApi.md#appsCheckNameAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.IoTCentral/checkNameAvailability |  |
| [**appsCreateOrUpdate**](AppsApi.md#appsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.IoTCentral/IoTApps/{resourceName} |  |
| [**appsDelete**](AppsApi.md#appsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.IoTCentral/IoTApps/{resourceName} |  |
| [**appsGet**](AppsApi.md#appsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.IoTCentral/IoTApps/{resourceName} |  |
| [**appsListByResourceGroup**](AppsApi.md#appsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.IoTCentral/IoTApps |  |
| [**appsListBySubscription**](AppsApi.md#appsListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.IoTCentral/IoTApps |  |
| [**appsUpdate**](AppsApi.md#appsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.IoTCentral/IoTApps/{resourceName} |  |


<a id="appsCheckNameAvailability"></a>
# **appsCheckNameAvailability**
> AppNameAvailabilityInfo appsCheckNameAvailability(apiVersion, subscriptionId, operationInputs)



Check if an IoT Central application name is available.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    OperationInputs operationInputs = new OperationInputs(); // OperationInputs | Set the name parameter in the OperationInputs structure to the name of the IoT Central application to check.
    try {
      AppNameAvailabilityInfo result = apiInstance.appsCheckNameAvailability(apiVersion, subscriptionId, operationInputs);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#appsCheckNameAvailability");
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
| **apiVersion** | **String**| The version of the API. | |
| **subscriptionId** | **String**| The subscription identifier. | |
| **operationInputs** | [**OperationInputs**](OperationInputs.md)| Set the name parameter in the OperationInputs structure to the name of the IoT Central application to check. | |

### Return type

[**AppNameAvailabilityInfo**](AppNameAvailabilityInfo.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | This is a synchronous operation. The body contains a JSON-serialized response that specifies whether the IoT Central application name is available. If the name is not available, the body contains the reason. |  -  |
| **0** | DefaultErrorResponse |  -  |

<a id="appsCreateOrUpdate"></a>
# **appsCreateOrUpdate**
> App appsCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, app)



Create or update the metadata of an IoT Central application. The usual pattern to modify a property is to retrieve the IoT Central application metadata and security metadata, and then combine them with the modified values in a new body to update the IoT Central application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoT Central application.
    String resourceName = "resourceName_example"; // String | The ARM resource name of the IoT Central application.
    App app = new App(); // App | The IoT Central application metadata and security metadata.
    try {
      App result = apiInstance.appsCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, app);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#appsCreateOrUpdate");
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
| **apiVersion** | **String**| The version of the API. | |
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the IoT Central application. | |
| **resourceName** | **String**| The ARM resource name of the IoT Central application. | |
| **app** | [**App**](App.md)| The IoT Central application metadata and security metadata. | |

### Return type

[**App**](App.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | This is returned as a response to the status polling request for the create or update operation. The body contains the resource representation that indicates a transitional provisioning state. |  -  |
| **201** | This is returned as a response to the status polling request for the create or update operation. The body contains the resource representation that indicates a transitional provisioning state. |  -  |
| **202** | Accepted - Put request accepted; the operation will complete asynchronously. |  -  |
| **0** | DefaultErrorResponse |  -  |

<a id="appsDelete"></a>
# **appsDelete**
> appsDelete(apiVersion, subscriptionId, resourceGroupName, resourceName)



Delete an IoT Central application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoT Central application.
    String resourceName = "resourceName_example"; // String | The ARM resource name of the IoT Central application.
    try {
      apiInstance.appsDelete(apiVersion, subscriptionId, resourceGroupName, resourceName);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#appsDelete");
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
| **apiVersion** | **String**| The version of the API. | |
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the IoT Central application. | |
| **resourceName** | **String**| The ARM resource name of the IoT Central application. | |

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
| **200** | This is returned as a response to the status polling request for the delete operation. The body contains the resource representation that indicates a transitional provisioning state. |  -  |
| **202** | Accepted - Delete request accepted; the operation will complete asynchronously. |  -  |
| **204** | Once the long running delete operation completes successfully, a 204 No Content status code is returned when the status polling request finds the IoT Central application metadata in the service and the status of the delete operation is set to a completed state. |  -  |
| **0** | DefaultErrorResponse |  -  |

<a id="appsGet"></a>
# **appsGet**
> App appsGet(apiVersion, subscriptionId, resourceGroupName, resourceName)



Get the metadata of an IoT Central application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoT Central application.
    String resourceName = "resourceName_example"; // String | The ARM resource name of the IoT Central application.
    try {
      App result = apiInstance.appsGet(apiVersion, subscriptionId, resourceGroupName, resourceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#appsGet");
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
| **apiVersion** | **String**| The version of the API. | |
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the IoT Central application. | |
| **resourceName** | **String**| The ARM resource name of the IoT Central application. | |

### Return type

[**App**](App.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The body contains all the non-security properties of the IoT Central application. Security-related properties are set to null. |  -  |
| **0** | Default error response |  -  |

<a id="appsListByResourceGroup"></a>
# **appsListByResourceGroup**
> AppListResult appsListByResourceGroup(apiVersion, subscriptionId, resourceGroupName)



Get all the IoT Central Applications in a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoT Central application.
    try {
      AppListResult result = apiInstance.appsListByResourceGroup(apiVersion, subscriptionId, resourceGroupName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#appsListByResourceGroup");
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
| **apiVersion** | **String**| The version of the API. | |
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the IoT Central application. | |

### Return type

[**AppListResult**](AppListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | This is a synchronous operation. The body contains a JSON-serialized array of the metadata from all the IoT Central Applications in the resource group. |  -  |
| **0** | DefaultErrorResponse |  -  |

<a id="appsListBySubscription"></a>
# **appsListBySubscription**
> AppListResult appsListBySubscription(apiVersion, subscriptionId)



Get all IoT Central Applications in a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    try {
      AppListResult result = apiInstance.appsListBySubscription(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#appsListBySubscription");
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
| **apiVersion** | **String**| The version of the API. | |
| **subscriptionId** | **String**| The subscription identifier. | |

### Return type

[**AppListResult**](AppListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | This is a synchronous operation. The body contains a JSON-serialized array of the metadata from all the IoT Central Applications in the subscription. |  -  |
| **0** | DefaultErrorResponse |  -  |

<a id="appsUpdate"></a>
# **appsUpdate**
> App appsUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, appPatch)



Update the metadata of an IoT Central application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoT Central application.
    String resourceName = "resourceName_example"; // String | The ARM resource name of the IoT Central application.
    AppPatch appPatch = new AppPatch(); // AppPatch | The IoT Central application metadata and security metadata.
    try {
      App result = apiInstance.appsUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, appPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#appsUpdate");
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
| **apiVersion** | **String**| The version of the API. | |
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the IoT Central application. | |
| **resourceName** | **String**| The ARM resource name of the IoT Central application. | |
| **appPatch** | [**AppPatch**](AppPatch.md)| The IoT Central application metadata and security metadata. | |

### Return type

[**App**](App.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | This is returned as a response to the status polling request for the create or update operation. The body contains the resource representation that indicates a transitional provisioning state. |  -  |
| **202** | Accepted - Put request accepted; the operation will complete asynchronously. |  -  |
| **0** | DefaultErrorResponse |  -  |

