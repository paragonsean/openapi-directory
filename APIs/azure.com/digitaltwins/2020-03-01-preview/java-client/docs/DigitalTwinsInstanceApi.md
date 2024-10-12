# DigitalTwinsInstanceApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**digitalTwinsCreateOrUpdate**](DigitalTwinsInstanceApi.md#digitalTwinsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DigitalTwins/digitalTwinsInstances/{resourceName} |  |
| [**digitalTwinsDelete**](DigitalTwinsInstanceApi.md#digitalTwinsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DigitalTwins/digitalTwinsInstances/{resourceName} |  |
| [**digitalTwinsGet**](DigitalTwinsInstanceApi.md#digitalTwinsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DigitalTwins/digitalTwinsInstances/{resourceName} |  |
| [**digitalTwinsList**](DigitalTwinsInstanceApi.md#digitalTwinsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.DigitalTwins/digitalTwinsInstances |  |
| [**digitalTwinsListByResourceGroup**](DigitalTwinsInstanceApi.md#digitalTwinsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DigitalTwins/digitalTwinsInstances |  |
| [**digitalTwinsUpdate**](DigitalTwinsInstanceApi.md#digitalTwinsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DigitalTwins/digitalTwinsInstances/{resourceName} |  |


<a id="digitalTwinsCreateOrUpdate"></a>
# **digitalTwinsCreateOrUpdate**
> DigitalTwinsDescription digitalTwinsCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, digitalTwinsCreate)



Create or update the metadata of a DigitalTwinsInstance. The usual pattern to modify a property is to retrieve the DigitalTwinsInstance and security metadata, and then combine them with the modified values in a new body to update the DigitalTwinsInstance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DigitalTwinsInstanceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DigitalTwinsInstanceApi apiInstance = new DigitalTwinsInstanceApi(defaultClient);
    String apiVersion = "2020-03-01-preview"; // String | Version of the DigitalTwinsInstance Management API.
    UUID subscriptionId = UUID.randomUUID(); // UUID | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the DigitalTwinsInstance.
    String resourceName = "resourceName_example"; // String | The name of the DigitalTwinsInstance.
    DigitalTwinsDescription digitalTwinsCreate = new DigitalTwinsDescription(); // DigitalTwinsDescription | The DigitalTwinsInstance and security metadata.
    try {
      DigitalTwinsDescription result = apiInstance.digitalTwinsCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, digitalTwinsCreate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DigitalTwinsInstanceApi#digitalTwinsCreateOrUpdate");
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
| **apiVersion** | **String**| Version of the DigitalTwinsInstance Management API. | [enum: 2020-03-01-preview] |
| **subscriptionId** | **UUID**| The subscription identifier. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the DigitalTwinsInstance. | |
| **resourceName** | **String**| The name of the DigitalTwinsInstance. | |
| **digitalTwinsCreate** | [**DigitalTwinsDescription**](DigitalTwinsDescription.md)| The DigitalTwinsInstance and security metadata. | |

### Return type

[**DigitalTwinsDescription**](DigitalTwinsDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | This is returned as a response to the status polling request for the create or update operation. The body contains the resource representation that indicates a transitional provisioning state. |  -  |
| **201** | Created - Put request accepted; the operation will complete asynchronously. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="digitalTwinsDelete"></a>
# **digitalTwinsDelete**
> digitalTwinsDelete(apiVersion, subscriptionId, resourceGroupName, resourceName)



Delete a DigitalTwinsInstance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DigitalTwinsInstanceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DigitalTwinsInstanceApi apiInstance = new DigitalTwinsInstanceApi(defaultClient);
    String apiVersion = "2020-03-01-preview"; // String | Version of the DigitalTwinsInstance Management API.
    UUID subscriptionId = UUID.randomUUID(); // UUID | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the DigitalTwinsInstance.
    String resourceName = "resourceName_example"; // String | The name of the DigitalTwinsInstance.
    try {
      apiInstance.digitalTwinsDelete(apiVersion, subscriptionId, resourceGroupName, resourceName);
    } catch (ApiException e) {
      System.err.println("Exception when calling DigitalTwinsInstanceApi#digitalTwinsDelete");
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
| **apiVersion** | **String**| Version of the DigitalTwinsInstance Management API. | [enum: 2020-03-01-preview] |
| **subscriptionId** | **UUID**| The subscription identifier. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the DigitalTwinsInstance. | |
| **resourceName** | **String**| The name of the DigitalTwinsInstance. | |

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
| **204** | Once the long running delete operation completes successfully, a 204 No Content status code is returned when the status polling request finds the DigitalTwins service metadata in the service and the status of the delete operation is set to a completed state. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="digitalTwinsGet"></a>
# **digitalTwinsGet**
> DigitalTwinsDescription digitalTwinsGet(apiVersion, subscriptionId, resourceGroupName, resourceName)



Get DigitalTwinsInstances resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DigitalTwinsInstanceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DigitalTwinsInstanceApi apiInstance = new DigitalTwinsInstanceApi(defaultClient);
    String apiVersion = "2020-03-01-preview"; // String | Version of the DigitalTwinsInstance Management API.
    UUID subscriptionId = UUID.randomUUID(); // UUID | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the DigitalTwinsInstance.
    String resourceName = "resourceName_example"; // String | The name of the DigitalTwinsInstance.
    try {
      DigitalTwinsDescription result = apiInstance.digitalTwinsGet(apiVersion, subscriptionId, resourceGroupName, resourceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DigitalTwinsInstanceApi#digitalTwinsGet");
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
| **apiVersion** | **String**| Version of the DigitalTwinsInstance Management API. | [enum: 2020-03-01-preview] |
| **subscriptionId** | **UUID**| The subscription identifier. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the DigitalTwinsInstance. | |
| **resourceName** | **String**| The name of the DigitalTwinsInstance. | |

### Return type

[**DigitalTwinsDescription**](DigitalTwinsDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The body contains all the non-security properties of the DigitalTwinsInstance. Security-related properties are set to null. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="digitalTwinsList"></a>
# **digitalTwinsList**
> DigitalTwinsDescriptionListResult digitalTwinsList(apiVersion, subscriptionId)



Get all the DigitalTwinsInstances in a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DigitalTwinsInstanceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DigitalTwinsInstanceApi apiInstance = new DigitalTwinsInstanceApi(defaultClient);
    String apiVersion = "2020-03-01-preview"; // String | Version of the DigitalTwinsInstance Management API.
    UUID subscriptionId = UUID.randomUUID(); // UUID | The subscription identifier.
    try {
      DigitalTwinsDescriptionListResult result = apiInstance.digitalTwinsList(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DigitalTwinsInstanceApi#digitalTwinsList");
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
| **apiVersion** | **String**| Version of the DigitalTwinsInstance Management API. | [enum: 2020-03-01-preview] |
| **subscriptionId** | **UUID**| The subscription identifier. | |

### Return type

[**DigitalTwinsDescriptionListResult**](DigitalTwinsDescriptionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | This is a synchronous operation. The body contains a JSON-serialized array of the metadata from all the DigitalTwinsInstances in the subscription. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="digitalTwinsListByResourceGroup"></a>
# **digitalTwinsListByResourceGroup**
> DigitalTwinsDescriptionListResult digitalTwinsListByResourceGroup(apiVersion, subscriptionId, resourceGroupName)



Get all the DigitalTwinsInstances in a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DigitalTwinsInstanceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DigitalTwinsInstanceApi apiInstance = new DigitalTwinsInstanceApi(defaultClient);
    String apiVersion = "2020-03-01-preview"; // String | Version of the DigitalTwinsInstance Management API.
    UUID subscriptionId = UUID.randomUUID(); // UUID | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the DigitalTwinsInstance.
    try {
      DigitalTwinsDescriptionListResult result = apiInstance.digitalTwinsListByResourceGroup(apiVersion, subscriptionId, resourceGroupName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DigitalTwinsInstanceApi#digitalTwinsListByResourceGroup");
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
| **apiVersion** | **String**| Version of the DigitalTwinsInstance Management API. | [enum: 2020-03-01-preview] |
| **subscriptionId** | **UUID**| The subscription identifier. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the DigitalTwinsInstance. | |

### Return type

[**DigitalTwinsDescriptionListResult**](DigitalTwinsDescriptionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | This is a synchronous operation. The body contains a JSON-serialized array of the metadata from all the DigitalTwinsInstances in the resource group. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="digitalTwinsUpdate"></a>
# **digitalTwinsUpdate**
> DigitalTwinsDescription digitalTwinsUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, digitalTwinsPatchDescription)



Update metadata of DigitalTwinsInstance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DigitalTwinsInstanceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DigitalTwinsInstanceApi apiInstance = new DigitalTwinsInstanceApi(defaultClient);
    String apiVersion = "2020-03-01-preview"; // String | Version of the DigitalTwinsInstance Management API.
    UUID subscriptionId = UUID.randomUUID(); // UUID | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the DigitalTwinsInstance.
    String resourceName = "resourceName_example"; // String | The name of the DigitalTwinsInstance.
    DigitalTwinsPatchDescription digitalTwinsPatchDescription = new DigitalTwinsPatchDescription(); // DigitalTwinsPatchDescription | The DigitalTwinsInstance and security metadata.
    try {
      DigitalTwinsDescription result = apiInstance.digitalTwinsUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, digitalTwinsPatchDescription);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DigitalTwinsInstanceApi#digitalTwinsUpdate");
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
| **apiVersion** | **String**| Version of the DigitalTwinsInstance Management API. | [enum: 2020-03-01-preview] |
| **subscriptionId** | **UUID**| The subscription identifier. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the DigitalTwinsInstance. | |
| **resourceName** | **String**| The name of the DigitalTwinsInstance. | |
| **digitalTwinsPatchDescription** | [**DigitalTwinsPatchDescription**](DigitalTwinsPatchDescription.md)| The DigitalTwinsInstance and security metadata. | |

### Return type

[**DigitalTwinsDescription**](DigitalTwinsDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | This is returned as a response to the status polling request for the create or update operation. The body contains the resource representation that indicates a transitional provisioning state. |  -  |
| **201** | Accepted - Put request accepted; the operation will complete asynchronously. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

