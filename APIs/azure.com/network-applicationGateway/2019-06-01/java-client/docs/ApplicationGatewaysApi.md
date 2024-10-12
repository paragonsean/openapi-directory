# ApplicationGatewaysApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**applicationGatewaysBackendHealth**](ApplicationGatewaysApi.md#applicationGatewaysBackendHealth) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/applicationGateways/{applicationGatewayName}/backendhealth |  |
| [**applicationGatewaysBackendHealthOnDemand**](ApplicationGatewaysApi.md#applicationGatewaysBackendHealthOnDemand) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/applicationGateways/{applicationGatewayName}/getBackendHealthOnDemand |  |
| [**applicationGatewaysCreateOrUpdate**](ApplicationGatewaysApi.md#applicationGatewaysCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/applicationGateways/{applicationGatewayName} |  |
| [**applicationGatewaysDelete**](ApplicationGatewaysApi.md#applicationGatewaysDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/applicationGateways/{applicationGatewayName} |  |
| [**applicationGatewaysGet**](ApplicationGatewaysApi.md#applicationGatewaysGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/applicationGateways/{applicationGatewayName} |  |
| [**applicationGatewaysGetSslPredefinedPolicy**](ApplicationGatewaysApi.md#applicationGatewaysGetSslPredefinedPolicy) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/applicationGatewayAvailableSslOptions/default/predefinedPolicies/{predefinedPolicyName} |  |
| [**applicationGatewaysList**](ApplicationGatewaysApi.md#applicationGatewaysList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/applicationGateways |  |
| [**applicationGatewaysListAll**](ApplicationGatewaysApi.md#applicationGatewaysListAll) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/applicationGateways |  |
| [**applicationGatewaysListAvailableRequestHeaders**](ApplicationGatewaysApi.md#applicationGatewaysListAvailableRequestHeaders) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/applicationGatewayAvailableRequestHeaders |  |
| [**applicationGatewaysListAvailableResponseHeaders**](ApplicationGatewaysApi.md#applicationGatewaysListAvailableResponseHeaders) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/applicationGatewayAvailableResponseHeaders |  |
| [**applicationGatewaysListAvailableServerVariables**](ApplicationGatewaysApi.md#applicationGatewaysListAvailableServerVariables) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/applicationGatewayAvailableServerVariables |  |
| [**applicationGatewaysListAvailableSslOptions**](ApplicationGatewaysApi.md#applicationGatewaysListAvailableSslOptions) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/applicationGatewayAvailableSslOptions/default |  |
| [**applicationGatewaysListAvailableSslPredefinedPolicies**](ApplicationGatewaysApi.md#applicationGatewaysListAvailableSslPredefinedPolicies) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/applicationGatewayAvailableSslOptions/default/predefinedPolicies |  |
| [**applicationGatewaysListAvailableWafRuleSets**](ApplicationGatewaysApi.md#applicationGatewaysListAvailableWafRuleSets) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/applicationGatewayAvailableWafRuleSets |  |
| [**applicationGatewaysStart**](ApplicationGatewaysApi.md#applicationGatewaysStart) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/applicationGateways/{applicationGatewayName}/start |  |
| [**applicationGatewaysStop**](ApplicationGatewaysApi.md#applicationGatewaysStop) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/applicationGateways/{applicationGatewayName}/stop |  |
| [**applicationGatewaysUpdateTags**](ApplicationGatewaysApi.md#applicationGatewaysUpdateTags) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/applicationGateways/{applicationGatewayName} |  |


<a id="applicationGatewaysBackendHealth"></a>
# **applicationGatewaysBackendHealth**
> ApplicationGatewayBackendHealth applicationGatewaysBackendHealth(resourceGroupName, applicationGatewayName, apiVersion, subscriptionId, $expand)



Gets the backend health of the specified application gateway in a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationGatewaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationGatewaysApi apiInstance = new ApplicationGatewaysApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String applicationGatewayName = "applicationGatewayName_example"; // String | The name of the application gateway.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String $expand = "$expand_example"; // String | Expands BackendAddressPool and BackendHttpSettings referenced in backend health.
    try {
      ApplicationGatewayBackendHealth result = apiInstance.applicationGatewaysBackendHealth(resourceGroupName, applicationGatewayName, apiVersion, subscriptionId, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationGatewaysApi#applicationGatewaysBackendHealth");
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
| **applicationGatewayName** | **String**| The name of the application gateway. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **$expand** | **String**| Expands BackendAddressPool and BackendHttpSettings referenced in backend health. | [optional] |

### Return type

[**ApplicationGatewayBackendHealth**](ApplicationGatewayBackendHealth.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |

<a id="applicationGatewaysBackendHealthOnDemand"></a>
# **applicationGatewaysBackendHealthOnDemand**
> ApplicationGatewayBackendHealthOnDemand applicationGatewaysBackendHealthOnDemand(resourceGroupName, applicationGatewayName, probeRequest, UNKNOWN_PARAMETER_NAME, UNKNOWN_PARAMETER_NAME2, $expand)



Gets the backend health for given combination of backend pool and http setting of the specified application gateway in a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationGatewaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationGatewaysApi apiInstance = new ApplicationGatewaysApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String applicationGatewayName = "applicationGatewayName_example"; // String | The name of the application gateway.
    ApplicationGatewayOnDemandProbe probeRequest = new ApplicationGatewayOnDemandProbe(); // ApplicationGatewayOnDemandProbe | Request body for on-demand test probe operation.
     UNKNOWN_PARAMETER_NAME = new null(); //  | 
     UNKNOWN_PARAMETER_NAME2 = new null(); //  | 
    String $expand = "$expand_example"; // String | Expands BackendAddressPool and BackendHttpSettings referenced in backend health.
    try {
      ApplicationGatewayBackendHealthOnDemand result = apiInstance.applicationGatewaysBackendHealthOnDemand(resourceGroupName, applicationGatewayName, probeRequest, UNKNOWN_PARAMETER_NAME, UNKNOWN_PARAMETER_NAME2, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationGatewaysApi#applicationGatewaysBackendHealthOnDemand");
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
| **applicationGatewayName** | **String**| The name of the application gateway. | |
| **probeRequest** | [**ApplicationGatewayOnDemandProbe**](ApplicationGatewayOnDemandProbe.md)| Request body for on-demand test probe operation. | |
| **UNKNOWN_PARAMETER_NAME** | [****](.md)|  | [optional] |
| **UNKNOWN_PARAMETER_NAME2** | [****](.md)|  | [optional] |
| **$expand** | **String**| Expands BackendAddressPool and BackendHttpSettings referenced in backend health. | [optional] |

### Return type

[**ApplicationGatewayBackendHealthOnDemand**](ApplicationGatewayBackendHealthOnDemand.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |

<a id="applicationGatewaysCreateOrUpdate"></a>
# **applicationGatewaysCreateOrUpdate**
> ApplicationGateway applicationGatewaysCreateOrUpdate(resourceGroupName, applicationGatewayName, parameters, UNKNOWN_PARAMETER_NAME, UNKNOWN_PARAMETER_NAME2)



Creates or updates the specified application gateway.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationGatewaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationGatewaysApi apiInstance = new ApplicationGatewaysApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String applicationGatewayName = "applicationGatewayName_example"; // String | The name of the application gateway.
    ApplicationGateway parameters = new ApplicationGateway(); // ApplicationGateway | Parameters supplied to the create or update application gateway operation.
     UNKNOWN_PARAMETER_NAME = new null(); //  | 
     UNKNOWN_PARAMETER_NAME2 = new null(); //  | 
    try {
      ApplicationGateway result = apiInstance.applicationGatewaysCreateOrUpdate(resourceGroupName, applicationGatewayName, parameters, UNKNOWN_PARAMETER_NAME, UNKNOWN_PARAMETER_NAME2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationGatewaysApi#applicationGatewaysCreateOrUpdate");
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
| **applicationGatewayName** | **String**| The name of the application gateway. | |
| **parameters** | [**ApplicationGateway**](ApplicationGateway.md)| Parameters supplied to the create or update application gateway operation. | |
| **UNKNOWN_PARAMETER_NAME** | [****](.md)|  | [optional] |
| **UNKNOWN_PARAMETER_NAME2** | [****](.md)|  | [optional] |

### Return type

[**ApplicationGateway**](ApplicationGateway.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update successful. The operation returns the resulting ApplicationGateway resource. |  -  |
| **201** | Create successful. The operation returns the resulting ApplicationGateway resource. |  -  |

<a id="applicationGatewaysDelete"></a>
# **applicationGatewaysDelete**
> applicationGatewaysDelete(resourceGroupName, applicationGatewayName, UNKNOWN_PARAMETER_NAME, UNKNOWN_PARAMETER_NAME2)



Deletes the specified application gateway.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationGatewaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationGatewaysApi apiInstance = new ApplicationGatewaysApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String applicationGatewayName = "applicationGatewayName_example"; // String | The name of the application gateway.
     UNKNOWN_PARAMETER_NAME = new null(); //  | 
     UNKNOWN_PARAMETER_NAME2 = new null(); //  | 
    try {
      apiInstance.applicationGatewaysDelete(resourceGroupName, applicationGatewayName, UNKNOWN_PARAMETER_NAME, UNKNOWN_PARAMETER_NAME2);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationGatewaysApi#applicationGatewaysDelete");
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
| **applicationGatewayName** | **String**| The name of the application gateway. | |
| **UNKNOWN_PARAMETER_NAME** | [****](.md)|  | [optional] |
| **UNKNOWN_PARAMETER_NAME2** | [****](.md)|  | [optional] |

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
| **200** | Delete successful. |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |
| **204** | Request successful. Resource with the specified name does not exist. |  -  |

<a id="applicationGatewaysGet"></a>
# **applicationGatewaysGet**
> ApplicationGateway applicationGatewaysGet(resourceGroupName, applicationGatewayName, UNKNOWN_PARAMETER_NAME, UNKNOWN_PARAMETER_NAME2)



Gets the specified application gateway.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationGatewaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationGatewaysApi apiInstance = new ApplicationGatewaysApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String applicationGatewayName = "applicationGatewayName_example"; // String | The name of the application gateway.
     UNKNOWN_PARAMETER_NAME = new null(); //  | 
     UNKNOWN_PARAMETER_NAME2 = new null(); //  | 
    try {
      ApplicationGateway result = apiInstance.applicationGatewaysGet(resourceGroupName, applicationGatewayName, UNKNOWN_PARAMETER_NAME, UNKNOWN_PARAMETER_NAME2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationGatewaysApi#applicationGatewaysGet");
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
| **applicationGatewayName** | **String**| The name of the application gateway. | |
| **UNKNOWN_PARAMETER_NAME** | [****](.md)|  | [optional] |
| **UNKNOWN_PARAMETER_NAME2** | [****](.md)|  | [optional] |

### Return type

[**ApplicationGateway**](ApplicationGateway.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns an ApplicationGateway resource. |  -  |

<a id="applicationGatewaysGetSslPredefinedPolicy"></a>
# **applicationGatewaysGetSslPredefinedPolicy**
> Object applicationGatewaysGetSslPredefinedPolicy(predefinedPolicyName, UNKNOWN_PARAMETER_NAME, UNKNOWN_PARAMETER_NAME2)



Gets Ssl predefined policy with the specified policy name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationGatewaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationGatewaysApi apiInstance = new ApplicationGatewaysApi(defaultClient);
    String predefinedPolicyName = "predefinedPolicyName_example"; // String | Name of Ssl predefined policy.
     UNKNOWN_PARAMETER_NAME = new null(); //  | 
     UNKNOWN_PARAMETER_NAME2 = new null(); //  | 
    try {
      Object result = apiInstance.applicationGatewaysGetSslPredefinedPolicy(predefinedPolicyName, UNKNOWN_PARAMETER_NAME, UNKNOWN_PARAMETER_NAME2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationGatewaysApi#applicationGatewaysGetSslPredefinedPolicy");
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
| **predefinedPolicyName** | **String**| Name of Ssl predefined policy. | |
| **UNKNOWN_PARAMETER_NAME** | [****](.md)|  | [optional] |
| **UNKNOWN_PARAMETER_NAME2** | [****](.md)|  | [optional] |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. The operation returns a Ssl predefined policy with the specified policy name. |  -  |

<a id="applicationGatewaysList"></a>
# **applicationGatewaysList**
> ApplicationGatewayListResult applicationGatewaysList(resourceGroupName, UNKNOWN_PARAMETER_NAME, UNKNOWN_PARAMETER_NAME2)



Lists all application gateways in a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationGatewaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationGatewaysApi apiInstance = new ApplicationGatewaysApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
     UNKNOWN_PARAMETER_NAME = new null(); //  | 
     UNKNOWN_PARAMETER_NAME2 = new null(); //  | 
    try {
      ApplicationGatewayListResult result = apiInstance.applicationGatewaysList(resourceGroupName, UNKNOWN_PARAMETER_NAME, UNKNOWN_PARAMETER_NAME2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationGatewaysApi#applicationGatewaysList");
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
| **UNKNOWN_PARAMETER_NAME** | [****](.md)|  | [optional] |
| **UNKNOWN_PARAMETER_NAME2** | [****](.md)|  | [optional] |

### Return type

[**ApplicationGatewayListResult**](ApplicationGatewayListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. The operation returns a list of ApplicationGateway resources. |  -  |

<a id="applicationGatewaysListAll"></a>
# **applicationGatewaysListAll**
> ApplicationGatewayListResult applicationGatewaysListAll(UNKNOWN_PARAMETER_NAME, UNKNOWN_PARAMETER_NAME2)



Gets all the application gateways in a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationGatewaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationGatewaysApi apiInstance = new ApplicationGatewaysApi(defaultClient);
     UNKNOWN_PARAMETER_NAME = new null(); //  | 
     UNKNOWN_PARAMETER_NAME2 = new null(); //  | 
    try {
      ApplicationGatewayListResult result = apiInstance.applicationGatewaysListAll(UNKNOWN_PARAMETER_NAME, UNKNOWN_PARAMETER_NAME2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationGatewaysApi#applicationGatewaysListAll");
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
| **UNKNOWN_PARAMETER_NAME** | [****](.md)|  | [optional] |
| **UNKNOWN_PARAMETER_NAME2** | [****](.md)|  | [optional] |

### Return type

[**ApplicationGatewayListResult**](ApplicationGatewayListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. The operation returns a list of ApplicationGateway resources. |  -  |

<a id="applicationGatewaysListAvailableRequestHeaders"></a>
# **applicationGatewaysListAvailableRequestHeaders**
> List&lt;String&gt; applicationGatewaysListAvailableRequestHeaders(UNKNOWN_PARAMETER_NAME, UNKNOWN_PARAMETER_NAME2)



Lists all available request headers.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationGatewaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationGatewaysApi apiInstance = new ApplicationGatewaysApi(defaultClient);
     UNKNOWN_PARAMETER_NAME = new null(); //  | 
     UNKNOWN_PARAMETER_NAME2 = new null(); //  | 
    try {
      List<String> result = apiInstance.applicationGatewaysListAvailableRequestHeaders(UNKNOWN_PARAMETER_NAME, UNKNOWN_PARAMETER_NAME2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationGatewaysApi#applicationGatewaysListAvailableRequestHeaders");
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
| **UNKNOWN_PARAMETER_NAME** | [****](.md)|  | [optional] |
| **UNKNOWN_PARAMETER_NAME2** | [****](.md)|  | [optional] |

### Return type

**List&lt;String&gt;**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. The operation returns a list of all available request headers. |  -  |
| **0** | Unexpected error. |  -  |

<a id="applicationGatewaysListAvailableResponseHeaders"></a>
# **applicationGatewaysListAvailableResponseHeaders**
> List&lt;String&gt; applicationGatewaysListAvailableResponseHeaders(UNKNOWN_PARAMETER_NAME, UNKNOWN_PARAMETER_NAME2)



Lists all available response headers.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationGatewaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationGatewaysApi apiInstance = new ApplicationGatewaysApi(defaultClient);
     UNKNOWN_PARAMETER_NAME = new null(); //  | 
     UNKNOWN_PARAMETER_NAME2 = new null(); //  | 
    try {
      List<String> result = apiInstance.applicationGatewaysListAvailableResponseHeaders(UNKNOWN_PARAMETER_NAME, UNKNOWN_PARAMETER_NAME2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationGatewaysApi#applicationGatewaysListAvailableResponseHeaders");
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
| **UNKNOWN_PARAMETER_NAME** | [****](.md)|  | [optional] |
| **UNKNOWN_PARAMETER_NAME2** | [****](.md)|  | [optional] |

### Return type

**List&lt;String&gt;**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. The operation returns a list of all available response headers. |  -  |
| **0** | Unexpected error. |  -  |

<a id="applicationGatewaysListAvailableServerVariables"></a>
# **applicationGatewaysListAvailableServerVariables**
> List&lt;String&gt; applicationGatewaysListAvailableServerVariables(UNKNOWN_PARAMETER_NAME, UNKNOWN_PARAMETER_NAME2)



Lists all available server variables.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationGatewaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationGatewaysApi apiInstance = new ApplicationGatewaysApi(defaultClient);
     UNKNOWN_PARAMETER_NAME = new null(); //  | 
     UNKNOWN_PARAMETER_NAME2 = new null(); //  | 
    try {
      List<String> result = apiInstance.applicationGatewaysListAvailableServerVariables(UNKNOWN_PARAMETER_NAME, UNKNOWN_PARAMETER_NAME2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationGatewaysApi#applicationGatewaysListAvailableServerVariables");
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
| **UNKNOWN_PARAMETER_NAME** | [****](.md)|  | [optional] |
| **UNKNOWN_PARAMETER_NAME2** | [****](.md)|  | [optional] |

### Return type

**List&lt;String&gt;**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. The operation returns a list of all available server variables. |  -  |
| **0** | Unexpected error. |  -  |

<a id="applicationGatewaysListAvailableSslOptions"></a>
# **applicationGatewaysListAvailableSslOptions**
> Object applicationGatewaysListAvailableSslOptions(UNKNOWN_PARAMETER_NAME, UNKNOWN_PARAMETER_NAME2)



Lists available Ssl options for configuring Ssl policy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationGatewaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationGatewaysApi apiInstance = new ApplicationGatewaysApi(defaultClient);
     UNKNOWN_PARAMETER_NAME = new null(); //  | 
     UNKNOWN_PARAMETER_NAME2 = new null(); //  | 
    try {
      Object result = apiInstance.applicationGatewaysListAvailableSslOptions(UNKNOWN_PARAMETER_NAME, UNKNOWN_PARAMETER_NAME2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationGatewaysApi#applicationGatewaysListAvailableSslOptions");
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
| **UNKNOWN_PARAMETER_NAME** | [****](.md)|  | [optional] |
| **UNKNOWN_PARAMETER_NAME2** | [****](.md)|  | [optional] |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. The operation returns all available Ssl options for configuring Ssl policy. |  -  |

<a id="applicationGatewaysListAvailableSslPredefinedPolicies"></a>
# **applicationGatewaysListAvailableSslPredefinedPolicies**
> ApplicationGatewayAvailableSslPredefinedPolicies applicationGatewaysListAvailableSslPredefinedPolicies(UNKNOWN_PARAMETER_NAME, UNKNOWN_PARAMETER_NAME2)



Lists all SSL predefined policies for configuring Ssl policy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationGatewaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationGatewaysApi apiInstance = new ApplicationGatewaysApi(defaultClient);
     UNKNOWN_PARAMETER_NAME = new null(); //  | 
     UNKNOWN_PARAMETER_NAME2 = new null(); //  | 
    try {
      ApplicationGatewayAvailableSslPredefinedPolicies result = apiInstance.applicationGatewaysListAvailableSslPredefinedPolicies(UNKNOWN_PARAMETER_NAME, UNKNOWN_PARAMETER_NAME2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationGatewaysApi#applicationGatewaysListAvailableSslPredefinedPolicies");
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
| **UNKNOWN_PARAMETER_NAME** | [****](.md)|  | [optional] |
| **UNKNOWN_PARAMETER_NAME2** | [****](.md)|  | [optional] |

### Return type

[**ApplicationGatewayAvailableSslPredefinedPolicies**](ApplicationGatewayAvailableSslPredefinedPolicies.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. The operation returns a lists of all Ssl predefined policies for configuring Ssl policy. |  -  |

<a id="applicationGatewaysListAvailableWafRuleSets"></a>
# **applicationGatewaysListAvailableWafRuleSets**
> ApplicationGatewayAvailableWafRuleSetsResult applicationGatewaysListAvailableWafRuleSets(UNKNOWN_PARAMETER_NAME, UNKNOWN_PARAMETER_NAME2)



Lists all available web application firewall rule sets.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationGatewaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationGatewaysApi apiInstance = new ApplicationGatewaysApi(defaultClient);
     UNKNOWN_PARAMETER_NAME = new null(); //  | 
     UNKNOWN_PARAMETER_NAME2 = new null(); //  | 
    try {
      ApplicationGatewayAvailableWafRuleSetsResult result = apiInstance.applicationGatewaysListAvailableWafRuleSets(UNKNOWN_PARAMETER_NAME, UNKNOWN_PARAMETER_NAME2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationGatewaysApi#applicationGatewaysListAvailableWafRuleSets");
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
| **UNKNOWN_PARAMETER_NAME** | [****](.md)|  | [optional] |
| **UNKNOWN_PARAMETER_NAME2** | [****](.md)|  | [optional] |

### Return type

[**ApplicationGatewayAvailableWafRuleSetsResult**](ApplicationGatewayAvailableWafRuleSetsResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. The operation returns a list of all available web application firewall rule sets. |  -  |

<a id="applicationGatewaysStart"></a>
# **applicationGatewaysStart**
> applicationGatewaysStart(resourceGroupName, applicationGatewayName, UNKNOWN_PARAMETER_NAME, UNKNOWN_PARAMETER_NAME2)



Starts the specified application gateway.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationGatewaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationGatewaysApi apiInstance = new ApplicationGatewaysApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String applicationGatewayName = "applicationGatewayName_example"; // String | The name of the application gateway.
     UNKNOWN_PARAMETER_NAME = new null(); //  | 
     UNKNOWN_PARAMETER_NAME2 = new null(); //  | 
    try {
      apiInstance.applicationGatewaysStart(resourceGroupName, applicationGatewayName, UNKNOWN_PARAMETER_NAME, UNKNOWN_PARAMETER_NAME2);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationGatewaysApi#applicationGatewaysStart");
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
| **applicationGatewayName** | **String**| The name of the application gateway. | |
| **UNKNOWN_PARAMETER_NAME** | [****](.md)|  | [optional] |
| **UNKNOWN_PARAMETER_NAME2** | [****](.md)|  | [optional] |

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
| **200** | Request successful. The operation starts the ApplicationGateway resource. |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |

<a id="applicationGatewaysStop"></a>
# **applicationGatewaysStop**
> applicationGatewaysStop(resourceGroupName, applicationGatewayName, UNKNOWN_PARAMETER_NAME, UNKNOWN_PARAMETER_NAME2)



Stops the specified application gateway in a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationGatewaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationGatewaysApi apiInstance = new ApplicationGatewaysApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String applicationGatewayName = "applicationGatewayName_example"; // String | The name of the application gateway.
     UNKNOWN_PARAMETER_NAME = new null(); //  | 
     UNKNOWN_PARAMETER_NAME2 = new null(); //  | 
    try {
      apiInstance.applicationGatewaysStop(resourceGroupName, applicationGatewayName, UNKNOWN_PARAMETER_NAME, UNKNOWN_PARAMETER_NAME2);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationGatewaysApi#applicationGatewaysStop");
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
| **applicationGatewayName** | **String**| The name of the application gateway. | |
| **UNKNOWN_PARAMETER_NAME** | [****](.md)|  | [optional] |
| **UNKNOWN_PARAMETER_NAME2** | [****](.md)|  | [optional] |

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
| **200** | Request successful. The operation stops the ApplicationGateway resource. |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |

<a id="applicationGatewaysUpdateTags"></a>
# **applicationGatewaysUpdateTags**
> ApplicationGateway applicationGatewaysUpdateTags(resourceGroupName, applicationGatewayName, parameters, UNKNOWN_PARAMETER_NAME, UNKNOWN_PARAMETER_NAME2)



Updates the specified application gateway tags.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationGatewaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationGatewaysApi apiInstance = new ApplicationGatewaysApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String applicationGatewayName = "applicationGatewayName_example"; // String | The name of the application gateway.
    ApplicationGatewaysUpdateTagsRequest parameters = new ApplicationGatewaysUpdateTagsRequest(); // ApplicationGatewaysUpdateTagsRequest | Parameters supplied to update application gateway tags.
     UNKNOWN_PARAMETER_NAME = new null(); //  | 
     UNKNOWN_PARAMETER_NAME2 = new null(); //  | 
    try {
      ApplicationGateway result = apiInstance.applicationGatewaysUpdateTags(resourceGroupName, applicationGatewayName, parameters, UNKNOWN_PARAMETER_NAME, UNKNOWN_PARAMETER_NAME2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationGatewaysApi#applicationGatewaysUpdateTags");
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
| **applicationGatewayName** | **String**| The name of the application gateway. | |
| **parameters** | [**ApplicationGatewaysUpdateTagsRequest**](ApplicationGatewaysUpdateTagsRequest.md)| Parameters supplied to update application gateway tags. | |
| **UNKNOWN_PARAMETER_NAME** | [****](.md)|  | [optional] |
| **UNKNOWN_PARAMETER_NAME2** | [****](.md)|  | [optional] |

### Return type

[**ApplicationGateway**](ApplicationGateway.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update successful. The operation returns the resulting ApplicationGateway resource. |  -  |

