# JitNetworkAccessPoliciesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**jitNetworkAccessPoliciesCreateOrUpdate**](JitNetworkAccessPoliciesApi.md#jitNetworkAccessPoliciesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/locations/{ascLocation}/jitNetworkAccessPolicies/{jitNetworkAccessPolicyName} |  |
| [**jitNetworkAccessPoliciesDelete**](JitNetworkAccessPoliciesApi.md#jitNetworkAccessPoliciesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/locations/{ascLocation}/jitNetworkAccessPolicies/{jitNetworkAccessPolicyName} |  |
| [**jitNetworkAccessPoliciesGet**](JitNetworkAccessPoliciesApi.md#jitNetworkAccessPoliciesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/locations/{ascLocation}/jitNetworkAccessPolicies/{jitNetworkAccessPolicyName} |  |
| [**jitNetworkAccessPoliciesInitiate**](JitNetworkAccessPoliciesApi.md#jitNetworkAccessPoliciesInitiate) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/locations/{ascLocation}/jitNetworkAccessPolicies/{jitNetworkAccessPolicyName}/{jitNetworkAccessPolicyInitiateType} |  |
| [**jitNetworkAccessPoliciesList**](JitNetworkAccessPoliciesApi.md#jitNetworkAccessPoliciesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/jitNetworkAccessPolicies |  |
| [**jitNetworkAccessPoliciesListByRegion**](JitNetworkAccessPoliciesApi.md#jitNetworkAccessPoliciesListByRegion) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/locations/{ascLocation}/jitNetworkAccessPolicies |  |
| [**jitNetworkAccessPoliciesListByResourceGroup**](JitNetworkAccessPoliciesApi.md#jitNetworkAccessPoliciesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/jitNetworkAccessPolicies |  |
| [**jitNetworkAccessPoliciesListByResourceGroupAndRegion**](JitNetworkAccessPoliciesApi.md#jitNetworkAccessPoliciesListByResourceGroupAndRegion) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/locations/{ascLocation}/jitNetworkAccessPolicies |  |


<a id="jitNetworkAccessPoliciesCreateOrUpdate"></a>
# **jitNetworkAccessPoliciesCreateOrUpdate**
> JitNetworkAccessPolicy jitNetworkAccessPoliciesCreateOrUpdate(subscriptionId, resourceGroupName, ascLocation, jitNetworkAccessPolicyName, apiVersion, body)



Create a policy for protecting resources using Just-in-Time access control

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JitNetworkAccessPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    JitNetworkAccessPoliciesApi apiInstance = new JitNetworkAccessPoliciesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
    String jitNetworkAccessPolicyName = "jitNetworkAccessPolicyName_example"; // String | Name of a Just-in-Time access configuration policy.
    String apiVersion = "2015-06-01-preview"; // String | API version for the operation
    JitNetworkAccessPolicy body = new JitNetworkAccessPolicy(); // JitNetworkAccessPolicy | 
    try {
      JitNetworkAccessPolicy result = apiInstance.jitNetworkAccessPoliciesCreateOrUpdate(subscriptionId, resourceGroupName, ascLocation, jitNetworkAccessPolicyName, apiVersion, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JitNetworkAccessPoliciesApi#jitNetworkAccessPoliciesCreateOrUpdate");
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
| **subscriptionId** | **String**| Azure subscription ID | |
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | |
| **ascLocation** | **String**| The location where ASC stores the data of the subscription. can be retrieved from Get locations | |
| **jitNetworkAccessPolicyName** | **String**| Name of a Just-in-Time access configuration policy. | |
| **apiVersion** | **String**| API version for the operation | [enum: 2015-06-01-preview] |
| **body** | [**JitNetworkAccessPolicy**](JitNetworkAccessPolicy.md)|  | |

### Return type

[**JitNetworkAccessPolicy**](JitNetworkAccessPolicy.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="jitNetworkAccessPoliciesDelete"></a>
# **jitNetworkAccessPoliciesDelete**
> jitNetworkAccessPoliciesDelete(subscriptionId, resourceGroupName, ascLocation, jitNetworkAccessPolicyName, apiVersion)



Delete a Just-in-Time access control policy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JitNetworkAccessPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    JitNetworkAccessPoliciesApi apiInstance = new JitNetworkAccessPoliciesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
    String jitNetworkAccessPolicyName = "jitNetworkAccessPolicyName_example"; // String | Name of a Just-in-Time access configuration policy.
    String apiVersion = "2015-06-01-preview"; // String | API version for the operation
    try {
      apiInstance.jitNetworkAccessPoliciesDelete(subscriptionId, resourceGroupName, ascLocation, jitNetworkAccessPolicyName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling JitNetworkAccessPoliciesApi#jitNetworkAccessPoliciesDelete");
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
| **subscriptionId** | **String**| Azure subscription ID | |
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | |
| **ascLocation** | **String**| The location where ASC stores the data of the subscription. can be retrieved from Get locations | |
| **jitNetworkAccessPolicyName** | **String**| Name of a Just-in-Time access configuration policy. | |
| **apiVersion** | **String**| API version for the operation | [enum: 2015-06-01-preview] |

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
| **200** | OK - Resource was deleted |  -  |
| **204** | No Content - Resource does not exist |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="jitNetworkAccessPoliciesGet"></a>
# **jitNetworkAccessPoliciesGet**
> JitNetworkAccessPolicy jitNetworkAccessPoliciesGet(subscriptionId, resourceGroupName, ascLocation, jitNetworkAccessPolicyName, apiVersion)



Policies for protecting resources using Just-in-Time access control for the subscription, location

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JitNetworkAccessPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    JitNetworkAccessPoliciesApi apiInstance = new JitNetworkAccessPoliciesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
    String jitNetworkAccessPolicyName = "jitNetworkAccessPolicyName_example"; // String | Name of a Just-in-Time access configuration policy.
    String apiVersion = "2015-06-01-preview"; // String | API version for the operation
    try {
      JitNetworkAccessPolicy result = apiInstance.jitNetworkAccessPoliciesGet(subscriptionId, resourceGroupName, ascLocation, jitNetworkAccessPolicyName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JitNetworkAccessPoliciesApi#jitNetworkAccessPoliciesGet");
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
| **subscriptionId** | **String**| Azure subscription ID | |
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | |
| **ascLocation** | **String**| The location where ASC stores the data of the subscription. can be retrieved from Get locations | |
| **jitNetworkAccessPolicyName** | **String**| Name of a Just-in-Time access configuration policy. | |
| **apiVersion** | **String**| API version for the operation | [enum: 2015-06-01-preview] |

### Return type

[**JitNetworkAccessPolicy**](JitNetworkAccessPolicy.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="jitNetworkAccessPoliciesInitiate"></a>
# **jitNetworkAccessPoliciesInitiate**
> JitNetworkAccessRequest jitNetworkAccessPoliciesInitiate(subscriptionId, resourceGroupName, ascLocation, jitNetworkAccessPolicyName, jitNetworkAccessPolicyInitiateType, apiVersion, body)



Initiate a JIT access from a specific Just-in-Time policy configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JitNetworkAccessPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    JitNetworkAccessPoliciesApi apiInstance = new JitNetworkAccessPoliciesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
    String jitNetworkAccessPolicyName = "jitNetworkAccessPolicyName_example"; // String | Name of a Just-in-Time access configuration policy.
    String jitNetworkAccessPolicyInitiateType = "initiate"; // String | Type of the action to do on the Just-in-Time access policy.
    String apiVersion = "2015-06-01-preview"; // String | API version for the operation
    JitNetworkAccessPolicyInitiateRequest body = new JitNetworkAccessPolicyInitiateRequest(); // JitNetworkAccessPolicyInitiateRequest | 
    try {
      JitNetworkAccessRequest result = apiInstance.jitNetworkAccessPoliciesInitiate(subscriptionId, resourceGroupName, ascLocation, jitNetworkAccessPolicyName, jitNetworkAccessPolicyInitiateType, apiVersion, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JitNetworkAccessPoliciesApi#jitNetworkAccessPoliciesInitiate");
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
| **subscriptionId** | **String**| Azure subscription ID | |
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | |
| **ascLocation** | **String**| The location where ASC stores the data of the subscription. can be retrieved from Get locations | |
| **jitNetworkAccessPolicyName** | **String**| Name of a Just-in-Time access configuration policy. | |
| **jitNetworkAccessPolicyInitiateType** | **String**| Type of the action to do on the Just-in-Time access policy. | [enum: initiate] |
| **apiVersion** | **String**| API version for the operation | [enum: 2015-06-01-preview] |
| **body** | [**JitNetworkAccessPolicyInitiateRequest**](JitNetworkAccessPolicyInitiateRequest.md)|  | |

### Return type

[**JitNetworkAccessRequest**](JitNetworkAccessRequest.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="jitNetworkAccessPoliciesList"></a>
# **jitNetworkAccessPoliciesList**
> JitNetworkAccessPoliciesList jitNetworkAccessPoliciesList(subscriptionId, apiVersion)



Policies for protecting resources using Just-in-Time access control.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JitNetworkAccessPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    JitNetworkAccessPoliciesApi apiInstance = new JitNetworkAccessPoliciesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String apiVersion = "2015-06-01-preview"; // String | API version for the operation
    try {
      JitNetworkAccessPoliciesList result = apiInstance.jitNetworkAccessPoliciesList(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JitNetworkAccessPoliciesApi#jitNetworkAccessPoliciesList");
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
| **subscriptionId** | **String**| Azure subscription ID | |
| **apiVersion** | **String**| API version for the operation | [enum: 2015-06-01-preview] |

### Return type

[**JitNetworkAccessPoliciesList**](JitNetworkAccessPoliciesList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="jitNetworkAccessPoliciesListByRegion"></a>
# **jitNetworkAccessPoliciesListByRegion**
> JitNetworkAccessPoliciesList jitNetworkAccessPoliciesListByRegion(subscriptionId, ascLocation, apiVersion)



Policies for protecting resources using Just-in-Time access control for the subscription, location

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JitNetworkAccessPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    JitNetworkAccessPoliciesApi apiInstance = new JitNetworkAccessPoliciesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
    String apiVersion = "2015-06-01-preview"; // String | API version for the operation
    try {
      JitNetworkAccessPoliciesList result = apiInstance.jitNetworkAccessPoliciesListByRegion(subscriptionId, ascLocation, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JitNetworkAccessPoliciesApi#jitNetworkAccessPoliciesListByRegion");
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
| **subscriptionId** | **String**| Azure subscription ID | |
| **ascLocation** | **String**| The location where ASC stores the data of the subscription. can be retrieved from Get locations | |
| **apiVersion** | **String**| API version for the operation | [enum: 2015-06-01-preview] |

### Return type

[**JitNetworkAccessPoliciesList**](JitNetworkAccessPoliciesList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="jitNetworkAccessPoliciesListByResourceGroup"></a>
# **jitNetworkAccessPoliciesListByResourceGroup**
> JitNetworkAccessPoliciesList jitNetworkAccessPoliciesListByResourceGroup(subscriptionId, resourceGroupName, apiVersion)



Policies for protecting resources using Just-in-Time access control for the subscription, location

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JitNetworkAccessPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    JitNetworkAccessPoliciesApi apiInstance = new JitNetworkAccessPoliciesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String apiVersion = "2015-06-01-preview"; // String | API version for the operation
    try {
      JitNetworkAccessPoliciesList result = apiInstance.jitNetworkAccessPoliciesListByResourceGroup(subscriptionId, resourceGroupName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JitNetworkAccessPoliciesApi#jitNetworkAccessPoliciesListByResourceGroup");
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
| **subscriptionId** | **String**| Azure subscription ID | |
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | |
| **apiVersion** | **String**| API version for the operation | [enum: 2015-06-01-preview] |

### Return type

[**JitNetworkAccessPoliciesList**](JitNetworkAccessPoliciesList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="jitNetworkAccessPoliciesListByResourceGroupAndRegion"></a>
# **jitNetworkAccessPoliciesListByResourceGroupAndRegion**
> JitNetworkAccessPoliciesList jitNetworkAccessPoliciesListByResourceGroupAndRegion(subscriptionId, resourceGroupName, ascLocation, apiVersion)



Policies for protecting resources using Just-in-Time access control for the subscription, location

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JitNetworkAccessPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    JitNetworkAccessPoliciesApi apiInstance = new JitNetworkAccessPoliciesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
    String apiVersion = "2015-06-01-preview"; // String | API version for the operation
    try {
      JitNetworkAccessPoliciesList result = apiInstance.jitNetworkAccessPoliciesListByResourceGroupAndRegion(subscriptionId, resourceGroupName, ascLocation, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JitNetworkAccessPoliciesApi#jitNetworkAccessPoliciesListByResourceGroupAndRegion");
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
| **subscriptionId** | **String**| Azure subscription ID | |
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | |
| **ascLocation** | **String**| The location where ASC stores the data of the subscription. can be retrieved from Get locations | |
| **apiVersion** | **String**| API version for the operation | [enum: 2015-06-01-preview] |

### Return type

[**JitNetworkAccessPoliciesList**](JitNetworkAccessPoliciesList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

