# CapacitiesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**capacitiesCheckNameAvailability**](CapacitiesApi.md#capacitiesCheckNameAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.PowerBIDedicated/locations/{location}/checkNameAvailability |  |
| [**capacitiesCreate**](CapacitiesApi.md#capacitiesCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PowerBIDedicated/capacities/{dedicatedCapacityName} |  |
| [**capacitiesDelete**](CapacitiesApi.md#capacitiesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PowerBIDedicated/capacities/{dedicatedCapacityName} |  |
| [**capacitiesGetDetails**](CapacitiesApi.md#capacitiesGetDetails) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PowerBIDedicated/capacities/{dedicatedCapacityName} |  |
| [**capacitiesList**](CapacitiesApi.md#capacitiesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.PowerBIDedicated/capacities |  |
| [**capacitiesListByResourceGroup**](CapacitiesApi.md#capacitiesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PowerBIDedicated/capacities |  |
| [**capacitiesListSkusForCapacity**](CapacitiesApi.md#capacitiesListSkusForCapacity) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PowerBIDedicated/capacities/{dedicatedCapacityName}/skus |  |
| [**capacitiesResume**](CapacitiesApi.md#capacitiesResume) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PowerBIDedicated/capacities/{dedicatedCapacityName}/resume |  |
| [**capacitiesSuspend**](CapacitiesApi.md#capacitiesSuspend) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PowerBIDedicated/capacities/{dedicatedCapacityName}/suspend |  |
| [**capacitiesUpdate**](CapacitiesApi.md#capacitiesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PowerBIDedicated/capacities/{dedicatedCapacityName} |  |


<a id="capacitiesCheckNameAvailability"></a>
# **capacitiesCheckNameAvailability**
> CheckCapacityNameAvailabilityResult capacitiesCheckNameAvailability(location, apiVersion, subscriptionId, capacityParameters)



Check the name availability in the target location.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CapacitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CapacitiesApi apiInstance = new CapacitiesApi(defaultClient);
    String location = "location_example"; // String | The region name which the operation will lookup into.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String subscriptionId = "subscriptionId_example"; // String | A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    CheckCapacityNameAvailabilityParameters capacityParameters = new CheckCapacityNameAvailabilityParameters(); // CheckCapacityNameAvailabilityParameters | The name of the capacity.
    try {
      CheckCapacityNameAvailabilityResult result = apiInstance.capacitiesCheckNameAvailability(location, apiVersion, subscriptionId, capacityParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CapacitiesApi#capacitiesCheckNameAvailability");
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
| **location** | **String**| The region name which the operation will lookup into. | |
| **apiVersion** | **String**| The client API version. | |
| **subscriptionId** | **String**| A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **capacityParameters** | [**CheckCapacityNameAvailabilityParameters**](CheckCapacityNameAvailabilityParameters.md)| The name of the capacity. | |

### Return type

[**CheckCapacityNameAvailabilityResult**](CheckCapacityNameAvailabilityResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |

<a id="capacitiesCreate"></a>
# **capacitiesCreate**
> DedicatedCapacity capacitiesCreate(resourceGroupName, dedicatedCapacityName, apiVersion, subscriptionId, capacityParameters)



Provisions the specified Dedicated capacity based on the configuration specified in the request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CapacitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CapacitiesApi apiInstance = new CapacitiesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure Resource group of which a given PowerBIDedicated capacity is part. This name must be at least 1 character in length, and no more than 90.
    String dedicatedCapacityName = "dedicatedCapacityName_example"; // String | The name of the Dedicated capacity. It must be a minimum of 3 characters, and a maximum of 63.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String subscriptionId = "subscriptionId_example"; // String | A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    DedicatedCapacity capacityParameters = new DedicatedCapacity(); // DedicatedCapacity | Contains the information used to provision the Dedicated capacity.
    try {
      DedicatedCapacity result = apiInstance.capacitiesCreate(resourceGroupName, dedicatedCapacityName, apiVersion, subscriptionId, capacityParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CapacitiesApi#capacitiesCreate");
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
| **resourceGroupName** | **String**| The name of the Azure Resource group of which a given PowerBIDedicated capacity is part. This name must be at least 1 character in length, and no more than 90. | |
| **dedicatedCapacityName** | **String**| The name of the Dedicated capacity. It must be a minimum of 3 characters, and a maximum of 63. | |
| **apiVersion** | **String**| The client API version. | |
| **subscriptionId** | **String**| A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **capacityParameters** | [**DedicatedCapacity**](DedicatedCapacity.md)| Contains the information used to provision the Dedicated capacity. | |

### Return type

[**DedicatedCapacity**](DedicatedCapacity.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The operation completed successfully. |  -  |
| **201** | InProgress. The operation is still in progress. |  -  |

<a id="capacitiesDelete"></a>
# **capacitiesDelete**
> capacitiesDelete(resourceGroupName, dedicatedCapacityName, apiVersion, subscriptionId)



Deletes the specified Dedicated capacity.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CapacitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CapacitiesApi apiInstance = new CapacitiesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure Resource group of which a given PowerBIDedicated capacity is part. This name must be at least 1 character in length, and no more than 90.
    String dedicatedCapacityName = "dedicatedCapacityName_example"; // String | The name of the Dedicated capacity. It must be at least 3 characters in length, and no more than 63.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String subscriptionId = "subscriptionId_example"; // String | A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.capacitiesDelete(resourceGroupName, dedicatedCapacityName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling CapacitiesApi#capacitiesDelete");
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
| **resourceGroupName** | **String**| The name of the Azure Resource group of which a given PowerBIDedicated capacity is part. This name must be at least 1 character in length, and no more than 90. | |
| **dedicatedCapacityName** | **String**| The name of the Dedicated capacity. It must be at least 3 characters in length, and no more than 63. | |
| **apiVersion** | **String**| The client API version. | |
| **subscriptionId** | **String**| A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

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
| **200** | OK. |  -  |
| **202** | Accepted. |  -  |
| **204** | No Content. |  -  |

<a id="capacitiesGetDetails"></a>
# **capacitiesGetDetails**
> DedicatedCapacity capacitiesGetDetails(resourceGroupName, dedicatedCapacityName, apiVersion, subscriptionId)



Gets details about the specified dedicated capacity.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CapacitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CapacitiesApi apiInstance = new CapacitiesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure Resource group of which a given PowerBIDedicated capacity is part. This name must be at least 1 character in length, and no more than 90.
    String dedicatedCapacityName = "dedicatedCapacityName_example"; // String | The name of the dedicated capacity. It must be a minimum of 3 characters, and a maximum of 63.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String subscriptionId = "subscriptionId_example"; // String | A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      DedicatedCapacity result = apiInstance.capacitiesGetDetails(resourceGroupName, dedicatedCapacityName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CapacitiesApi#capacitiesGetDetails");
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
| **resourceGroupName** | **String**| The name of the Azure Resource group of which a given PowerBIDedicated capacity is part. This name must be at least 1 character in length, and no more than 90. | |
| **dedicatedCapacityName** | **String**| The name of the dedicated capacity. It must be a minimum of 3 characters, and a maximum of 63. | |
| **apiVersion** | **String**| The client API version. | |
| **subscriptionId** | **String**| A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**DedicatedCapacity**](DedicatedCapacity.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The operation was successful. |  -  |

<a id="capacitiesList"></a>
# **capacitiesList**
> DedicatedCapacities capacitiesList(apiVersion, subscriptionId)



Lists all the Dedicated capacities for the given subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CapacitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CapacitiesApi apiInstance = new CapacitiesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String subscriptionId = "subscriptionId_example"; // String | A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      DedicatedCapacities result = apiInstance.capacitiesList(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CapacitiesApi#capacitiesList");
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
| **apiVersion** | **String**| The client API version. | |
| **subscriptionId** | **String**| A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**DedicatedCapacities**](DedicatedCapacities.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="capacitiesListByResourceGroup"></a>
# **capacitiesListByResourceGroup**
> DedicatedCapacities capacitiesListByResourceGroup(resourceGroupName, apiVersion, subscriptionId)



Gets all the Dedicated capacities for the given resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CapacitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CapacitiesApi apiInstance = new CapacitiesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure Resource group of which a given PowerBIDedicated capacity is part. This name must be at least 1 character in length, and no more than 90.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String subscriptionId = "subscriptionId_example"; // String | A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      DedicatedCapacities result = apiInstance.capacitiesListByResourceGroup(resourceGroupName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CapacitiesApi#capacitiesListByResourceGroup");
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
| **resourceGroupName** | **String**| The name of the Azure Resource group of which a given PowerBIDedicated capacity is part. This name must be at least 1 character in length, and no more than 90. | |
| **apiVersion** | **String**| The client API version. | |
| **subscriptionId** | **String**| A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**DedicatedCapacities**](DedicatedCapacities.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="capacitiesListSkusForCapacity"></a>
# **capacitiesListSkusForCapacity**
> SkuEnumerationForExistingResourceResult capacitiesListSkusForCapacity(resourceGroupName, dedicatedCapacityName, apiVersion, subscriptionId)



Lists eligible SKUs for a PowerBI Dedicated resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CapacitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CapacitiesApi apiInstance = new CapacitiesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure Resource group of which a given PowerBIDedicated capacity is part. This name must be at least 1 character in length, and no more than 90.
    String dedicatedCapacityName = "dedicatedCapacityName_example"; // String | The name of the Dedicated capacity. It must be at least 3 characters in length, and no more than 63.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String subscriptionId = "subscriptionId_example"; // String | A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      SkuEnumerationForExistingResourceResult result = apiInstance.capacitiesListSkusForCapacity(resourceGroupName, dedicatedCapacityName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CapacitiesApi#capacitiesListSkusForCapacity");
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
| **resourceGroupName** | **String**| The name of the Azure Resource group of which a given PowerBIDedicated capacity is part. This name must be at least 1 character in length, and no more than 90. | |
| **dedicatedCapacityName** | **String**| The name of the Dedicated capacity. It must be at least 3 characters in length, and no more than 63. | |
| **apiVersion** | **String**| The client API version. | |
| **subscriptionId** | **String**| A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**SkuEnumerationForExistingResourceResult**](SkuEnumerationForExistingResourceResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="capacitiesResume"></a>
# **capacitiesResume**
> capacitiesResume(resourceGroupName, dedicatedCapacityName, apiVersion, subscriptionId)



Resumes operation of the specified Dedicated capacity instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CapacitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CapacitiesApi apiInstance = new CapacitiesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure Resource group of which a given PowerBIDedicated capacity is part. This name must be at least 1 character in length, and no more than 90.
    String dedicatedCapacityName = "dedicatedCapacityName_example"; // String | The name of the Dedicated capacity. It must be at least 3 characters in length, and no more than 63.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String subscriptionId = "subscriptionId_example"; // String | A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.capacitiesResume(resourceGroupName, dedicatedCapacityName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling CapacitiesApi#capacitiesResume");
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
| **resourceGroupName** | **String**| The name of the Azure Resource group of which a given PowerBIDedicated capacity is part. This name must be at least 1 character in length, and no more than 90. | |
| **dedicatedCapacityName** | **String**| The name of the Dedicated capacity. It must be at least 3 characters in length, and no more than 63. | |
| **apiVersion** | **String**| The client API version. | |
| **subscriptionId** | **String**| A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

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
| **200** | OK |  -  |
| **202** | Accepted |  -  |

<a id="capacitiesSuspend"></a>
# **capacitiesSuspend**
> capacitiesSuspend(resourceGroupName, dedicatedCapacityName, apiVersion, subscriptionId)



Suspends operation of the specified dedicated capacity instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CapacitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CapacitiesApi apiInstance = new CapacitiesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure Resource group of which a given PowerBIDedicated capacity is part. This name must be at least 1 character in length, and no more than 90.
    String dedicatedCapacityName = "dedicatedCapacityName_example"; // String | The name of the Dedicated capacity. It must be at least 3 characters in length, and no more than 63.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String subscriptionId = "subscriptionId_example"; // String | A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.capacitiesSuspend(resourceGroupName, dedicatedCapacityName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling CapacitiesApi#capacitiesSuspend");
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
| **resourceGroupName** | **String**| The name of the Azure Resource group of which a given PowerBIDedicated capacity is part. This name must be at least 1 character in length, and no more than 90. | |
| **dedicatedCapacityName** | **String**| The name of the Dedicated capacity. It must be at least 3 characters in length, and no more than 63. | |
| **apiVersion** | **String**| The client API version. | |
| **subscriptionId** | **String**| A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

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
| **200** | OK. |  -  |
| **202** | Accepted. |  -  |

<a id="capacitiesUpdate"></a>
# **capacitiesUpdate**
> DedicatedCapacity capacitiesUpdate(resourceGroupName, dedicatedCapacityName, apiVersion, subscriptionId, capacityUpdateParameters)



Updates the current state of the specified Dedicated capacity.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CapacitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CapacitiesApi apiInstance = new CapacitiesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure Resource group of which a given PowerBIDedicated capacity is part. This name must be at least 1 character in length, and no more than 90.
    String dedicatedCapacityName = "dedicatedCapacityName_example"; // String | The name of the Dedicated capacity. It must be at least 3 characters in length, and no more than 63.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String subscriptionId = "subscriptionId_example"; // String | A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    DedicatedCapacityUpdateParameters capacityUpdateParameters = new DedicatedCapacityUpdateParameters(); // DedicatedCapacityUpdateParameters | Request object that contains the updated information for the capacity.
    try {
      DedicatedCapacity result = apiInstance.capacitiesUpdate(resourceGroupName, dedicatedCapacityName, apiVersion, subscriptionId, capacityUpdateParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CapacitiesApi#capacitiesUpdate");
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
| **resourceGroupName** | **String**| The name of the Azure Resource group of which a given PowerBIDedicated capacity is part. This name must be at least 1 character in length, and no more than 90. | |
| **dedicatedCapacityName** | **String**| The name of the Dedicated capacity. It must be at least 3 characters in length, and no more than 63. | |
| **apiVersion** | **String**| The client API version. | |
| **subscriptionId** | **String**| A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **capacityUpdateParameters** | [**DedicatedCapacityUpdateParameters**](DedicatedCapacityUpdateParameters.md)| Request object that contains the updated information for the capacity. | |

### Return type

[**DedicatedCapacity**](DedicatedCapacity.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |

