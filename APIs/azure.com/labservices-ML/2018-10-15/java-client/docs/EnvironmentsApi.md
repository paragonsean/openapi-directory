# EnvironmentsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**environmentsClaim**](EnvironmentsApi.md#environmentsClaim) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/environmentsettings/{environmentSettingName}/environments/{environmentName}/claim |  |
| [**environmentsCreateOrUpdate**](EnvironmentsApi.md#environmentsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/environmentsettings/{environmentSettingName}/environments/{environmentName} |  |
| [**environmentsDelete**](EnvironmentsApi.md#environmentsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/environmentsettings/{environmentSettingName}/environments/{environmentName} |  |
| [**environmentsGet**](EnvironmentsApi.md#environmentsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/environmentsettings/{environmentSettingName}/environments/{environmentName} |  |
| [**environmentsList**](EnvironmentsApi.md#environmentsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/environmentsettings/{environmentSettingName}/environments |  |
| [**environmentsResetPassword**](EnvironmentsApi.md#environmentsResetPassword) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/environmentsettings/{environmentSettingName}/environments/{environmentName}/resetPassword |  |
| [**environmentsStart**](EnvironmentsApi.md#environmentsStart) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/environmentsettings/{environmentSettingName}/environments/{environmentName}/start |  |
| [**environmentsStop**](EnvironmentsApi.md#environmentsStop) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/environmentsettings/{environmentSettingName}/environments/{environmentName}/stop |  |
| [**environmentsUpdate**](EnvironmentsApi.md#environmentsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/environmentsettings/{environmentSettingName}/environments/{environmentName} |  |


<a id="environmentsClaim"></a>
# **environmentsClaim**
> environmentsClaim(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, environmentName, apiVersion)



Claims the environment and assigns it to the user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EnvironmentsApi apiInstance = new EnvironmentsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labAccountName = "labAccountName_example"; // String | The name of the lab Account.
    String labName = "labName_example"; // String | The name of the lab.
    String environmentSettingName = "environmentSettingName_example"; // String | The name of the environment Setting.
    String environmentName = "environmentName_example"; // String | The name of the environment.
    String apiVersion = "2018-10-15"; // String | Client API version.
    try {
      apiInstance.environmentsClaim(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, environmentName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnvironmentsApi#environmentsClaim");
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
| **labAccountName** | **String**| The name of the lab Account. | |
| **labName** | **String**| The name of the lab. | |
| **environmentSettingName** | **String**| The name of the environment Setting. | |
| **environmentName** | **String**| The name of the environment. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-10-15] |

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
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

<a id="environmentsCreateOrUpdate"></a>
# **environmentsCreateOrUpdate**
> Environment environmentsCreateOrUpdate(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, environmentName, apiVersion, environment)



Create or replace an existing Environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EnvironmentsApi apiInstance = new EnvironmentsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labAccountName = "labAccountName_example"; // String | The name of the lab Account.
    String labName = "labName_example"; // String | The name of the lab.
    String environmentSettingName = "environmentSettingName_example"; // String | The name of the environment Setting.
    String environmentName = "environmentName_example"; // String | The name of the environment.
    String apiVersion = "2018-10-15"; // String | Client API version.
    Environment environment = new Environment(); // Environment | Represents an environment instance
    try {
      Environment result = apiInstance.environmentsCreateOrUpdate(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, environmentName, apiVersion, environment);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnvironmentsApi#environmentsCreateOrUpdate");
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
| **labAccountName** | **String**| The name of the lab Account. | |
| **labName** | **String**| The name of the lab. | |
| **environmentSettingName** | **String**| The name of the environment Setting. | |
| **environmentName** | **String**| The name of the environment. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-10-15] |
| **environment** | [**Environment**](Environment.md)| Represents an environment instance | |

### Return type

[**Environment**](Environment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **0** | BadRequest |  -  |

<a id="environmentsDelete"></a>
# **environmentsDelete**
> environmentsDelete(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, environmentName, apiVersion)



Delete environment. This operation can take a while to complete

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EnvironmentsApi apiInstance = new EnvironmentsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labAccountName = "labAccountName_example"; // String | The name of the lab Account.
    String labName = "labName_example"; // String | The name of the lab.
    String environmentSettingName = "environmentSettingName_example"; // String | The name of the environment Setting.
    String environmentName = "environmentName_example"; // String | The name of the environment.
    String apiVersion = "2018-10-15"; // String | Client API version.
    try {
      apiInstance.environmentsDelete(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, environmentName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnvironmentsApi#environmentsDelete");
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
| **labAccountName** | **String**| The name of the lab Account. | |
| **labName** | **String**| The name of the lab. | |
| **environmentSettingName** | **String**| The name of the environment Setting. | |
| **environmentName** | **String**| The name of the environment. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-10-15] |

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
| **202** | Accepted |  -  |
| **204** | No Content |  -  |
| **0** | BadRequest |  -  |

<a id="environmentsGet"></a>
# **environmentsGet**
> Environment environmentsGet(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, environmentName, apiVersion, $expand)



Get environment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EnvironmentsApi apiInstance = new EnvironmentsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labAccountName = "labAccountName_example"; // String | The name of the lab Account.
    String labName = "labName_example"; // String | The name of the lab.
    String environmentSettingName = "environmentSettingName_example"; // String | The name of the environment Setting.
    String environmentName = "environmentName_example"; // String | The name of the environment.
    String apiVersion = "2018-10-15"; // String | Client API version.
    String $expand = "$expand_example"; // String | Specify the $expand query. Example: 'properties($expand=networkInterface)'
    try {
      Environment result = apiInstance.environmentsGet(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, environmentName, apiVersion, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnvironmentsApi#environmentsGet");
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
| **labAccountName** | **String**| The name of the lab Account. | |
| **labName** | **String**| The name of the lab. | |
| **environmentSettingName** | **String**| The name of the environment Setting. | |
| **environmentName** | **String**| The name of the environment. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-10-15] |
| **$expand** | **String**| Specify the $expand query. Example: &#39;properties($expand&#x3D;networkInterface)&#39; | [optional] |

### Return type

[**Environment**](Environment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

<a id="environmentsList"></a>
# **environmentsList**
> ResponseWithContinuationEnvironment environmentsList(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, apiVersion, $expand, $filter, $top, $orderby)



List environments in a given environment setting.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EnvironmentsApi apiInstance = new EnvironmentsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labAccountName = "labAccountName_example"; // String | The name of the lab Account.
    String labName = "labName_example"; // String | The name of the lab.
    String environmentSettingName = "environmentSettingName_example"; // String | The name of the environment Setting.
    String apiVersion = "2018-10-15"; // String | Client API version.
    String $expand = "$expand_example"; // String | Specify the $expand query. Example: 'properties($expand=networkInterface)'
    String $filter = "$filter_example"; // String | The filter to apply to the operation.
    Integer $top = 56; // Integer | The maximum number of resources to return from the operation.
    String $orderby = "$orderby_example"; // String | The ordering expression for the results, using OData notation.
    try {
      ResponseWithContinuationEnvironment result = apiInstance.environmentsList(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, apiVersion, $expand, $filter, $top, $orderby);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnvironmentsApi#environmentsList");
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
| **labAccountName** | **String**| The name of the lab Account. | |
| **labName** | **String**| The name of the lab. | |
| **environmentSettingName** | **String**| The name of the environment Setting. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-10-15] |
| **$expand** | **String**| Specify the $expand query. Example: &#39;properties($expand&#x3D;networkInterface)&#39; | [optional] |
| **$filter** | **String**| The filter to apply to the operation. | [optional] |
| **$top** | **Integer**| The maximum number of resources to return from the operation. | [optional] |
| **$orderby** | **String**| The ordering expression for the results, using OData notation. | [optional] |

### Return type

[**ResponseWithContinuationEnvironment**](ResponseWithContinuationEnvironment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

<a id="environmentsResetPassword"></a>
# **environmentsResetPassword**
> environmentsResetPassword(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, environmentName, apiVersion, resetPasswordPayload)



Resets the user password on an environment This operation can take a while to complete

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EnvironmentsApi apiInstance = new EnvironmentsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labAccountName = "labAccountName_example"; // String | The name of the lab Account.
    String labName = "labName_example"; // String | The name of the lab.
    String environmentSettingName = "environmentSettingName_example"; // String | The name of the environment Setting.
    String environmentName = "environmentName_example"; // String | The name of the environment.
    String apiVersion = "2018-10-15"; // String | Client API version.
    ResetPasswordPayload resetPasswordPayload = new ResetPasswordPayload(); // ResetPasswordPayload | Represents the payload for resetting passwords.
    try {
      apiInstance.environmentsResetPassword(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, environmentName, apiVersion, resetPasswordPayload);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnvironmentsApi#environmentsResetPassword");
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
| **labAccountName** | **String**| The name of the lab Account. | |
| **labName** | **String**| The name of the lab. | |
| **environmentSettingName** | **String**| The name of the environment Setting. | |
| **environmentName** | **String**| The name of the environment. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-10-15] |
| **resetPasswordPayload** | [**ResetPasswordPayload**](ResetPasswordPayload.md)| Represents the payload for resetting passwords. | |

### Return type

null (empty response body)

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
| **0** | BadRequest |  -  |

<a id="environmentsStart"></a>
# **environmentsStart**
> environmentsStart(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, environmentName, apiVersion)



Starts an environment by starting all resources inside the environment. This operation can take a while to complete

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EnvironmentsApi apiInstance = new EnvironmentsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labAccountName = "labAccountName_example"; // String | The name of the lab Account.
    String labName = "labName_example"; // String | The name of the lab.
    String environmentSettingName = "environmentSettingName_example"; // String | The name of the environment Setting.
    String environmentName = "environmentName_example"; // String | The name of the environment.
    String apiVersion = "2018-10-15"; // String | Client API version.
    try {
      apiInstance.environmentsStart(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, environmentName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnvironmentsApi#environmentsStart");
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
| **labAccountName** | **String**| The name of the lab Account. | |
| **labName** | **String**| The name of the lab. | |
| **environmentSettingName** | **String**| The name of the environment Setting. | |
| **environmentName** | **String**| The name of the environment. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-10-15] |

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
| **200** | OK |  -  |
| **202** | Accepted |  -  |
| **0** | BadRequest |  -  |

<a id="environmentsStop"></a>
# **environmentsStop**
> environmentsStop(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, environmentName, apiVersion)



Stops an environment by stopping all resources inside the environment This operation can take a while to complete

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EnvironmentsApi apiInstance = new EnvironmentsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labAccountName = "labAccountName_example"; // String | The name of the lab Account.
    String labName = "labName_example"; // String | The name of the lab.
    String environmentSettingName = "environmentSettingName_example"; // String | The name of the environment Setting.
    String environmentName = "environmentName_example"; // String | The name of the environment.
    String apiVersion = "2018-10-15"; // String | Client API version.
    try {
      apiInstance.environmentsStop(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, environmentName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnvironmentsApi#environmentsStop");
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
| **labAccountName** | **String**| The name of the lab Account. | |
| **labName** | **String**| The name of the lab. | |
| **environmentSettingName** | **String**| The name of the environment Setting. | |
| **environmentName** | **String**| The name of the environment. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-10-15] |

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
| **200** | OK |  -  |
| **202** | Accepted |  -  |
| **0** | BadRequest |  -  |

<a id="environmentsUpdate"></a>
# **environmentsUpdate**
> Environment environmentsUpdate(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, environmentName, apiVersion, environment)



Modify properties of environments.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EnvironmentsApi apiInstance = new EnvironmentsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labAccountName = "labAccountName_example"; // String | The name of the lab Account.
    String labName = "labName_example"; // String | The name of the lab.
    String environmentSettingName = "environmentSettingName_example"; // String | The name of the environment Setting.
    String environmentName = "environmentName_example"; // String | The name of the environment.
    String apiVersion = "2018-10-15"; // String | Client API version.
    EnvironmentFragment environment = new EnvironmentFragment(); // EnvironmentFragment | Represents an environment instance
    try {
      Environment result = apiInstance.environmentsUpdate(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, environmentName, apiVersion, environment);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnvironmentsApi#environmentsUpdate");
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
| **labAccountName** | **String**| The name of the lab Account. | |
| **labName** | **String**| The name of the lab. | |
| **environmentSettingName** | **String**| The name of the environment Setting. | |
| **environmentName** | **String**| The name of the environment. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-10-15] |
| **environment** | [**EnvironmentFragment**](EnvironmentFragment.md)| Represents an environment instance | |

### Return type

[**Environment**](Environment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

