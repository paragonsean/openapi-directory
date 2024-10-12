# ProfilesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**profilesCreate**](ProfilesApi.md#profilesCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName} | Creates a new CDN profile with the specified parameters. |
| [**profilesDeleteIfExists**](ProfilesApi.md#profilesDeleteIfExists) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName} | Deletes an existing CDN profile with the specified parameters. Deleting a profile will result in the deletion of all subresources including endpoints, origins and custom domains. |
| [**profilesGenerateSsoUri**](ProfilesApi.md#profilesGenerateSsoUri) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/generateSsoUri | Generates a dynamic SSO URI used to sign in to the CDN Supplemental Portal used for advanced management tasks, such as Country Filtering, Advanced HTTP Reports, and Real-time Stats and Alerts. The SSO URI changes approximately every 10 minutes. |
| [**profilesGet**](ProfilesApi.md#profilesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName} | Gets a CDN profile with the specified parameters. |
| [**profilesListByResourceGroup**](ProfilesApi.md#profilesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles | Lists the CDN profiles within a resource group. |
| [**profilesListBySubscriptionId**](ProfilesApi.md#profilesListBySubscriptionId) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Cdn/profiles | Lists the CDN profiles within an Azure subscription. |
| [**profilesUpdate**](ProfilesApi.md#profilesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName} | Updates an existing CDN profile with the specified parameters. |


<a id="profilesCreate"></a>
# **profilesCreate**
> Profile profilesCreate(profileName, resourceGroupName, subscriptionId, apiVersion, profileProperties)

Creates a new CDN profile with the specified parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProfilesApi apiInstance = new ProfilesApi(defaultClient);
    String profileName = "profileName_example"; // String | Name of the CDN profile within the resource group.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2015-06-01
    ProfileCreateParameters profileProperties = new ProfileCreateParameters(); // ProfileCreateParameters | Profile properties needed for creation.
    try {
      Profile result = apiInstance.profilesCreate(profileName, resourceGroupName, subscriptionId, apiVersion, profileProperties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfilesApi#profilesCreate");
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
| **profileName** | **String**| Name of the CDN profile within the resource group. | |
| **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2015-06-01 | |
| **profileProperties** | [**ProfileCreateParameters**](ProfileCreateParameters.md)| Profile properties needed for creation. | |

### Return type

[**Profile**](Profile.md)

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
| **202** | Accepted and  the operation will complete asynchronously. |  -  |
| **0** | CDN error response describing why the operation failed. |  -  |

<a id="profilesDeleteIfExists"></a>
# **profilesDeleteIfExists**
> profilesDeleteIfExists(profileName, resourceGroupName, subscriptionId, apiVersion)

Deletes an existing CDN profile with the specified parameters. Deleting a profile will result in the deletion of all subresources including endpoints, origins and custom domains.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProfilesApi apiInstance = new ProfilesApi(defaultClient);
    String profileName = "profileName_example"; // String | Name of the CDN profile within the resource group.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2015-06-01
    try {
      apiInstance.profilesDeleteIfExists(profileName, resourceGroupName, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfilesApi#profilesDeleteIfExists");
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
| **profileName** | **String**| Name of the CDN profile within the resource group. | |
| **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2015-06-01 | |

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
| **202** | Accepted and the operation will complete asynchronously. |  -  |
| **204** | No Content. |  -  |
| **0** | CDN error response describing why the operation failed. |  -  |

<a id="profilesGenerateSsoUri"></a>
# **profilesGenerateSsoUri**
> SsoUri profilesGenerateSsoUri(profileName, resourceGroupName, subscriptionId, apiVersion)

Generates a dynamic SSO URI used to sign in to the CDN Supplemental Portal used for advanced management tasks, such as Country Filtering, Advanced HTTP Reports, and Real-time Stats and Alerts. The SSO URI changes approximately every 10 minutes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProfilesApi apiInstance = new ProfilesApi(defaultClient);
    String profileName = "profileName_example"; // String | Name of the CDN profile within the resource group.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2015-06-01
    try {
      SsoUri result = apiInstance.profilesGenerateSsoUri(profileName, resourceGroupName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfilesApi#profilesGenerateSsoUri");
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
| **profileName** | **String**| Name of the CDN profile within the resource group. | |
| **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2015-06-01 | |

### Return type

[**SsoUri**](SsoUri.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | CDN error response describing why the operation failed. |  -  |

<a id="profilesGet"></a>
# **profilesGet**
> Profile profilesGet(profileName, resourceGroupName, subscriptionId, apiVersion)

Gets a CDN profile with the specified parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProfilesApi apiInstance = new ProfilesApi(defaultClient);
    String profileName = "profileName_example"; // String | Name of the CDN profile within the resource group.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2015-06-01
    try {
      Profile result = apiInstance.profilesGet(profileName, resourceGroupName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfilesApi#profilesGet");
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
| **profileName** | **String**| Name of the CDN profile within the resource group. | |
| **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2015-06-01 | |

### Return type

[**Profile**](Profile.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | CDN error response describing why the operation failed. |  -  |

<a id="profilesListByResourceGroup"></a>
# **profilesListByResourceGroup**
> ProfileListResult profilesListByResourceGroup(resourceGroupName, subscriptionId, apiVersion)

Lists the CDN profiles within a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProfilesApi apiInstance = new ProfilesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2015-06-01
    try {
      ProfileListResult result = apiInstance.profilesListByResourceGroup(resourceGroupName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfilesApi#profilesListByResourceGroup");
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
| **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2015-06-01 | |

### Return type

[**ProfileListResult**](ProfileListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | CDN error response describing why the operation failed. |  -  |

<a id="profilesListBySubscriptionId"></a>
# **profilesListBySubscriptionId**
> ProfileListResult profilesListBySubscriptionId(subscriptionId, apiVersion)

Lists the CDN profiles within an Azure subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProfilesApi apiInstance = new ProfilesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2015-06-01
    try {
      ProfileListResult result = apiInstance.profilesListBySubscriptionId(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfilesApi#profilesListBySubscriptionId");
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
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2015-06-01 | |

### Return type

[**ProfileListResult**](ProfileListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | CDN error response describing why the operation failed. |  -  |

<a id="profilesUpdate"></a>
# **profilesUpdate**
> Profile profilesUpdate(profileName, resourceGroupName, subscriptionId, apiVersion, profileProperties)

Updates an existing CDN profile with the specified parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProfilesApi apiInstance = new ProfilesApi(defaultClient);
    String profileName = "profileName_example"; // String | Name of the CDN profile within the resource group.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2015-06-01
    ProfileUpdateParameters profileProperties = new ProfileUpdateParameters(); // ProfileUpdateParameters | Profile properties needed for update.
    try {
      Profile result = apiInstance.profilesUpdate(profileName, resourceGroupName, subscriptionId, apiVersion, profileProperties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfilesApi#profilesUpdate");
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
| **profileName** | **String**| Name of the CDN profile within the resource group. | |
| **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2015-06-01 | |
| **profileProperties** | [**ProfileUpdateParameters**](ProfileUpdateParameters.md)| Profile properties needed for update. | |

### Return type

[**Profile**](Profile.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |
| **0** | CDN error response describing why the operation failed. |  -  |

