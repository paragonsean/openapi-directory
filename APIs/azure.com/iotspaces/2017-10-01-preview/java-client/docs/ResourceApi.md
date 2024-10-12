# ResourceApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**ioTSpacesCreateOrUpdate**](ResourceApi.md#ioTSpacesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.IoTSpaces/Graph/{resourceName} |  |
| [**ioTSpacesDelete**](ResourceApi.md#ioTSpacesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.IoTSpaces/Graph/{resourceName} |  |
| [**ioTSpacesGet**](ResourceApi.md#ioTSpacesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.IoTSpaces/Graph/{resourceName} |  |
| [**ioTSpacesUpdate**](ResourceApi.md#ioTSpacesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.IoTSpaces/Graph/{resourceName} |  |


<a id="ioTSpacesCreateOrUpdate"></a>
# **ioTSpacesCreateOrUpdate**
> IoTSpacesDescription ioTSpacesCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, iotSpaceDescription)



Create or update the metadata of an IoTSpaces instance. The usual pattern to modify a property is to retrieve the IoTSpaces instance metadata and security metadata, and then combine them with the modified values in a new body to update the IoTSpaces instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ResourceApi apiInstance = new ResourceApi(defaultClient);
    String apiVersion = "2017-10-01-preview"; // String | The version of the API.
    UUID subscriptionId = UUID.randomUUID(); // UUID | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoTSpaces instance.
    String resourceName = "resourceName_example"; // String | The name of the IoTSpaces instance.
    IoTSpacesDescription iotSpaceDescription = new IoTSpacesDescription(); // IoTSpacesDescription | The IoTSpaces instance metadata and security metadata.
    try {
      IoTSpacesDescription result = apiInstance.ioTSpacesCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, iotSpaceDescription);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceApi#ioTSpacesCreateOrUpdate");
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
| **apiVersion** | **String**| The version of the API. | [enum: 2017-10-01-preview] |
| **subscriptionId** | **UUID**| The subscription identifier. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the IoTSpaces instance. | |
| **resourceName** | **String**| The name of the IoTSpaces instance. | |
| **iotSpaceDescription** | [**IoTSpacesDescription**](IoTSpacesDescription.md)| The IoTSpaces instance metadata and security metadata. | |

### Return type

[**IoTSpacesDescription**](IoTSpacesDescription.md)

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

<a id="ioTSpacesDelete"></a>
# **ioTSpacesDelete**
> IoTSpacesDescription ioTSpacesDelete(apiVersion, subscriptionId, resourceGroupName, resourceName)



Delete an IoTSpaces instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ResourceApi apiInstance = new ResourceApi(defaultClient);
    String apiVersion = "2017-10-01-preview"; // String | The version of the API.
    UUID subscriptionId = UUID.randomUUID(); // UUID | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoTSpaces instance.
    String resourceName = "resourceName_example"; // String | The name of the IoTSpaces instance.
    try {
      IoTSpacesDescription result = apiInstance.ioTSpacesDelete(apiVersion, subscriptionId, resourceGroupName, resourceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceApi#ioTSpacesDelete");
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
| **apiVersion** | **String**| The version of the API. | [enum: 2017-10-01-preview] |
| **subscriptionId** | **UUID**| The subscription identifier. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the IoTSpaces instance. | |
| **resourceName** | **String**| The name of the IoTSpaces instance. | |

### Return type

[**IoTSpacesDescription**](IoTSpacesDescription.md)

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
| **204** | Once the long running delete operation completes successfully, a 204 No Content status code is returned when the status polling request finds the IoTSpaces service metadata in the service and the status of the delete operation is set to a completed state. |  -  |
| **0** | DefaultErrorResponse |  -  |

<a id="ioTSpacesGet"></a>
# **ioTSpacesGet**
> IoTSpacesDescription ioTSpacesGet(apiVersion, subscriptionId, resourceGroupName, resourceName)



Get the metadata of a IoTSpaces instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ResourceApi apiInstance = new ResourceApi(defaultClient);
    String apiVersion = "2017-10-01-preview"; // String | The version of the API.
    UUID subscriptionId = UUID.randomUUID(); // UUID | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoTSpaces instance.
    String resourceName = "resourceName_example"; // String | The name of the IoTSpaces instance.
    try {
      IoTSpacesDescription result = apiInstance.ioTSpacesGet(apiVersion, subscriptionId, resourceGroupName, resourceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceApi#ioTSpacesGet");
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
| **apiVersion** | **String**| The version of the API. | [enum: 2017-10-01-preview] |
| **subscriptionId** | **UUID**| The subscription identifier. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the IoTSpaces instance. | |
| **resourceName** | **String**| The name of the IoTSpaces instance. | |

### Return type

[**IoTSpacesDescription**](IoTSpacesDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The body contains all the non-security properties of the IoTSpaces instance. Security-related properties are set to null. |  -  |
| **0** | Default error response |  -  |

<a id="ioTSpacesUpdate"></a>
# **ioTSpacesUpdate**
> IoTSpacesDescription ioTSpacesUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, iotSpacePatchDescription)



Update the metadata of a IoTSpaces instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ResourceApi apiInstance = new ResourceApi(defaultClient);
    String apiVersion = "2017-10-01-preview"; // String | The version of the API.
    UUID subscriptionId = UUID.randomUUID(); // UUID | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoTSpaces instance.
    String resourceName = "resourceName_example"; // String | The name of the IoTSpaces instance.
    IoTSpacesPatchDescription iotSpacePatchDescription = new IoTSpacesPatchDescription(); // IoTSpacesPatchDescription | The IoTSpaces instance metadata and security metadata.
    try {
      IoTSpacesDescription result = apiInstance.ioTSpacesUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, iotSpacePatchDescription);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceApi#ioTSpacesUpdate");
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
| **apiVersion** | **String**| The version of the API. | [enum: 2017-10-01-preview] |
| **subscriptionId** | **UUID**| The subscription identifier. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the IoTSpaces instance. | |
| **resourceName** | **String**| The name of the IoTSpaces instance. | |
| **iotSpacePatchDescription** | [**IoTSpacesPatchDescription**](IoTSpacesPatchDescription.md)| The IoTSpaces instance metadata and security metadata. | |

### Return type

[**IoTSpacesDescription**](IoTSpacesDescription.md)

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

