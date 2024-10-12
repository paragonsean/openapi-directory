# NetworkExperimentProfilesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**networkExperimentProfilesCreateOrUpdate**](NetworkExperimentProfilesApi.md#networkExperimentProfilesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/NetworkExperimentProfiles/{profileName} | Creates an NetworkExperiment Profile |
| [**networkExperimentProfilesDelete**](NetworkExperimentProfilesApi.md#networkExperimentProfilesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/NetworkExperimentProfiles/{profileName} | Deletes an NetworkExperiment Profile by ProfileName |
| [**networkExperimentProfilesGet**](NetworkExperimentProfilesApi.md#networkExperimentProfilesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/NetworkExperimentProfiles/{profileName} | Gets an NetworkExperiment Profile by ProfileName |
| [**networkExperimentProfilesList**](NetworkExperimentProfilesApi.md#networkExperimentProfilesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/NetworkExperimentProfiles | Gets a list of Network Experiment Profiles under a subscription |
| [**networkExperimentProfilesListByResourceGroup**](NetworkExperimentProfilesApi.md#networkExperimentProfilesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/NetworkExperimentProfiles | Gets a list of Network Experiment Profiles within a resource group under a subscription |
| [**networkExperimentProfilesUpdate**](NetworkExperimentProfilesApi.md#networkExperimentProfilesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/NetworkExperimentProfiles/{profileName} | Updates an NetworkExperimentProfiles by NetworkExperimentProfile name |


<a id="networkExperimentProfilesCreateOrUpdate"></a>
# **networkExperimentProfilesCreateOrUpdate**
> Profile networkExperimentProfilesCreateOrUpdate(profileName, subscriptionId, apiVersion, resourceGroupName, parameters)

Creates an NetworkExperiment Profile

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkExperimentProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NetworkExperimentProfilesApi apiInstance = new NetworkExperimentProfilesApi(defaultClient);
    String profileName = "profileName_example"; // String | The Profile identifier associated with the Tenant and Partner
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    Profile parameters = new Profile(); // Profile | An Network Experiment Profile
    try {
      Profile result = apiInstance.networkExperimentProfilesCreateOrUpdate(profileName, subscriptionId, apiVersion, resourceGroupName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkExperimentProfilesApi#networkExperimentProfilesCreateOrUpdate");
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
| **profileName** | **String**| The Profile identifier associated with the Tenant and Partner | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API version. | |
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **parameters** | [**Profile**](Profile.md)| An Network Experiment Profile | |

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
| **200** | OK. The request has succeeded. |  -  |
| **201** | Created. The request has been fulfilled and a new protection policy has been created. |  -  |
| **202** | Accepted. The request has been accepted for processing and the operation will complete asynchronously. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="networkExperimentProfilesDelete"></a>
# **networkExperimentProfilesDelete**
> networkExperimentProfilesDelete(subscriptionId, apiVersion, resourceGroupName, profileName)

Deletes an NetworkExperiment Profile by ProfileName

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkExperimentProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NetworkExperimentProfilesApi apiInstance = new NetworkExperimentProfilesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String profileName = "profileName_example"; // String | The Profile identifier associated with the Tenant and Partner
    try {
      apiInstance.networkExperimentProfilesDelete(subscriptionId, apiVersion, resourceGroupName, profileName);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkExperimentProfilesApi#networkExperimentProfilesDelete");
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
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API version. | |
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **profileName** | **String**| The Profile identifier associated with the Tenant and Partner | |

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
| **200** | Delete successful. |  -  |
| **202** | Accepted. The request has been accepted for processing and the operation will complete asynchronously. |  -  |
| **204** | No Content. The request has been accepted but the profile was not found. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="networkExperimentProfilesGet"></a>
# **networkExperimentProfilesGet**
> Profile networkExperimentProfilesGet(subscriptionId, apiVersion, resourceGroupName, profileName)

Gets an NetworkExperiment Profile by ProfileName

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkExperimentProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NetworkExperimentProfilesApi apiInstance = new NetworkExperimentProfilesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String profileName = "profileName_example"; // String | The Profile identifier associated with the Tenant and Partner
    try {
      Profile result = apiInstance.networkExperimentProfilesGet(subscriptionId, apiVersion, resourceGroupName, profileName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkExperimentProfilesApi#networkExperimentProfilesGet");
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
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API version. | |
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **profileName** | **String**| The Profile identifier associated with the Tenant and Partner | |

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
| **200** | successful operation |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="networkExperimentProfilesList"></a>
# **networkExperimentProfilesList**
> ProfileList networkExperimentProfilesList(subscriptionId, apiVersion)

Gets a list of Network Experiment Profiles under a subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkExperimentProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NetworkExperimentProfilesApi apiInstance = new NetworkExperimentProfilesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      ProfileList result = apiInstance.networkExperimentProfilesList(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkExperimentProfilesApi#networkExperimentProfilesList");
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
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API version. | |

### Return type

[**ProfileList**](ProfileList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="networkExperimentProfilesListByResourceGroup"></a>
# **networkExperimentProfilesListByResourceGroup**
> ProfileList networkExperimentProfilesListByResourceGroup(subscriptionId, apiVersion, resourceGroupName)

Gets a list of Network Experiment Profiles within a resource group under a subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkExperimentProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NetworkExperimentProfilesApi apiInstance = new NetworkExperimentProfilesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    try {
      ProfileList result = apiInstance.networkExperimentProfilesListByResourceGroup(subscriptionId, apiVersion, resourceGroupName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkExperimentProfilesApi#networkExperimentProfilesListByResourceGroup");
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
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API version. | |
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |

### Return type

[**ProfileList**](ProfileList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="networkExperimentProfilesUpdate"></a>
# **networkExperimentProfilesUpdate**
> Profile networkExperimentProfilesUpdate(subscriptionId, apiVersion, resourceGroupName, profileName, parameters)

Updates an NetworkExperimentProfiles by NetworkExperimentProfile name

Updates an NetworkExperimentProfiles

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkExperimentProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NetworkExperimentProfilesApi apiInstance = new NetworkExperimentProfilesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String profileName = "profileName_example"; // String | The Profile identifier associated with the Tenant and Partner
    ProfileUpdateModel parameters = new ProfileUpdateModel(); // ProfileUpdateModel | The Profile Update Model
    try {
      Profile result = apiInstance.networkExperimentProfilesUpdate(subscriptionId, apiVersion, resourceGroupName, profileName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkExperimentProfilesApi#networkExperimentProfilesUpdate");
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
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API version. | |
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **profileName** | **String**| The Profile identifier associated with the Tenant and Partner | |
| **parameters** | [**ProfileUpdateModel**](ProfileUpdateModel.md)| The Profile Update Model | |

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
| **200** | OK. successful operation |  -  |
| **202** | Accepted. The request has been accepted for processing and the operation will complete asynchronously. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

