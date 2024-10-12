# PolicyApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**policyCreateOrUpdateResource**](PolicyApi.md#policyCreateOrUpdateResource) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/policysets/{policySetName}/policies/{name} |  |
| [**policyDeleteResource**](PolicyApi.md#policyDeleteResource) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/policysets/{policySetName}/policies/{name} |  |
| [**policyGetResource**](PolicyApi.md#policyGetResource) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/policysets/{policySetName}/policies/{name} |  |
| [**policyList**](PolicyApi.md#policyList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/policysets/{policySetName}/policies |  |
| [**policyPatchResource**](PolicyApi.md#policyPatchResource) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/policysets/{policySetName}/policies/{name} |  |


<a id="policyCreateOrUpdateResource"></a>
# **policyCreateOrUpdateResource**
> Policy policyCreateOrUpdateResource(subscriptionId, resourceGroupName, labName, policySetName, name, apiVersion, policy)



Create or replace an existing policy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PolicyApi apiInstance = new PolicyApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labName = "labName_example"; // String | The name of the lab.
    String policySetName = "policySetName_example"; // String | The name of the policy set.
    String name = "name_example"; // String | The name of the policy.
    String apiVersion = "2015-05-21-preview"; // String | Client API version.
    Policy policy = new Policy(); // Policy | 
    try {
      Policy result = apiInstance.policyCreateOrUpdateResource(subscriptionId, resourceGroupName, labName, policySetName, name, apiVersion, policy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicyApi#policyCreateOrUpdateResource");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labName** | **String**| The name of the lab. | |
| **policySetName** | **String**| The name of the policy set. | |
| **name** | **String**| The name of the policy. | |
| **apiVersion** | **String**| Client API version. | [default to 2015-05-21-preview] |
| **policy** | [**Policy**](Policy.md)|  | |

### Return type

[**Policy**](Policy.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **0** | BadRequest |  -  |

<a id="policyDeleteResource"></a>
# **policyDeleteResource**
> policyDeleteResource(subscriptionId, resourceGroupName, labName, policySetName, name, apiVersion)



Delete policy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PolicyApi apiInstance = new PolicyApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labName = "labName_example"; // String | The name of the lab.
    String policySetName = "policySetName_example"; // String | The name of the policy set.
    String name = "name_example"; // String | The name of the policy.
    String apiVersion = "2015-05-21-preview"; // String | Client API version.
    try {
      apiInstance.policyDeleteResource(subscriptionId, resourceGroupName, labName, policySetName, name, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicyApi#policyDeleteResource");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labName** | **String**| The name of the lab. | |
| **policySetName** | **String**| The name of the policy set. | |
| **name** | **String**| The name of the policy. | |
| **apiVersion** | **String**| Client API version. | [default to 2015-05-21-preview] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **204** | No Content |  -  |
| **0** | BadRequest |  -  |

<a id="policyGetResource"></a>
# **policyGetResource**
> Policy policyGetResource(subscriptionId, resourceGroupName, labName, policySetName, name, apiVersion)



Get policy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PolicyApi apiInstance = new PolicyApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labName = "labName_example"; // String | The name of the lab.
    String policySetName = "policySetName_example"; // String | The name of the policy set.
    String name = "name_example"; // String | The name of the policy.
    String apiVersion = "2015-05-21-preview"; // String | Client API version.
    try {
      Policy result = apiInstance.policyGetResource(subscriptionId, resourceGroupName, labName, policySetName, name, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicyApi#policyGetResource");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labName** | **String**| The name of the lab. | |
| **policySetName** | **String**| The name of the policy set. | |
| **name** | **String**| The name of the policy. | |
| **apiVersion** | **String**| Client API version. | [default to 2015-05-21-preview] |

### Return type

[**Policy**](Policy.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

<a id="policyList"></a>
# **policyList**
> ResponseWithContinuationPolicy policyList(subscriptionId, resourceGroupName, labName, policySetName, apiVersion, $filter, $top, $orderBy)



List policies.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PolicyApi apiInstance = new PolicyApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labName = "labName_example"; // String | The name of the lab.
    String policySetName = "policySetName_example"; // String | The name of the policy set.
    String apiVersion = "2015-05-21-preview"; // String | Client API version.
    String $filter = "$filter_example"; // String | The filter to apply on the operation.
    Integer $top = 56; // Integer | 
    String $orderBy = "$orderBy_example"; // String | 
    try {
      ResponseWithContinuationPolicy result = apiInstance.policyList(subscriptionId, resourceGroupName, labName, policySetName, apiVersion, $filter, $top, $orderBy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicyApi#policyList");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labName** | **String**| The name of the lab. | |
| **policySetName** | **String**| The name of the policy set. | |
| **apiVersion** | **String**| Client API version. | [default to 2015-05-21-preview] |
| **$filter** | **String**| The filter to apply on the operation. | [optional] |
| **$top** | **Integer**|  | [optional] |
| **$orderBy** | **String**|  | [optional] |

### Return type

[**ResponseWithContinuationPolicy**](ResponseWithContinuationPolicy.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

<a id="policyPatchResource"></a>
# **policyPatchResource**
> Policy policyPatchResource(subscriptionId, resourceGroupName, labName, policySetName, name, apiVersion, policy)



Modify properties of policies.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PolicyApi apiInstance = new PolicyApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labName = "labName_example"; // String | The name of the lab.
    String policySetName = "policySetName_example"; // String | The name of the policy set.
    String name = "name_example"; // String | The name of the policy.
    String apiVersion = "2015-05-21-preview"; // String | Client API version.
    Policy policy = new Policy(); // Policy | 
    try {
      Policy result = apiInstance.policyPatchResource(subscriptionId, resourceGroupName, labName, policySetName, name, apiVersion, policy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicyApi#policyPatchResource");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labName** | **String**| The name of the lab. | |
| **policySetName** | **String**| The name of the policy set. | |
| **name** | **String**| The name of the policy. | |
| **apiVersion** | **String**| Client API version. | [default to 2015-05-21-preview] |
| **policy** | [**Policy**](Policy.md)|  | |

### Return type

[**Policy**](Policy.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

