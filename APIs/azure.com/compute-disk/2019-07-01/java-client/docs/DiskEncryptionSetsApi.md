# DiskEncryptionSetsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**diskEncryptionSetsCreateOrUpdate**](DiskEncryptionSetsApi.md#diskEncryptionSetsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/diskEncryptionSets/{diskEncryptionSetName} |  |
| [**diskEncryptionSetsDelete**](DiskEncryptionSetsApi.md#diskEncryptionSetsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/diskEncryptionSets/{diskEncryptionSetName} |  |
| [**diskEncryptionSetsGet**](DiskEncryptionSetsApi.md#diskEncryptionSetsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/diskEncryptionSets/{diskEncryptionSetName} |  |
| [**diskEncryptionSetsList**](DiskEncryptionSetsApi.md#diskEncryptionSetsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Compute/diskEncryptionSets |  |
| [**diskEncryptionSetsListByResourceGroup**](DiskEncryptionSetsApi.md#diskEncryptionSetsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/diskEncryptionSets |  |
| [**diskEncryptionSetsUpdate**](DiskEncryptionSetsApi.md#diskEncryptionSetsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/diskEncryptionSets/{diskEncryptionSetName} |  |


<a id="diskEncryptionSetsCreateOrUpdate"></a>
# **diskEncryptionSetsCreateOrUpdate**
> DiskEncryptionSet diskEncryptionSetsCreateOrUpdate(subscriptionId, resourceGroupName, diskEncryptionSetName, apiVersion, diskEncryptionSet)



Creates or updates a disk encryption set

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiskEncryptionSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DiskEncryptionSetsApi apiInstance = new DiskEncryptionSetsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String diskEncryptionSetName = "diskEncryptionSetName_example"; // String | The name of the disk encryption set that is being created. The name can't be changed after the disk encryption set is created. Supported characters for the name are a-z, A-Z, 0-9 and _. The maximum name length is 80 characters.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    DiskEncryptionSet diskEncryptionSet = new DiskEncryptionSet(); // DiskEncryptionSet | disk encryption set object supplied in the body of the Put disk encryption set operation.
    try {
      DiskEncryptionSet result = apiInstance.diskEncryptionSetsCreateOrUpdate(subscriptionId, resourceGroupName, diskEncryptionSetName, apiVersion, diskEncryptionSet);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiskEncryptionSetsApi#diskEncryptionSetsCreateOrUpdate");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **diskEncryptionSetName** | **String**| The name of the disk encryption set that is being created. The name can&#39;t be changed after the disk encryption set is created. Supported characters for the name are a-z, A-Z, 0-9 and _. The maximum name length is 80 characters. | |
| **apiVersion** | **String**| Client Api Version. | |
| **diskEncryptionSet** | [**DiskEncryptionSet**](DiskEncryptionSet.md)| disk encryption set object supplied in the body of the Put disk encryption set operation. | |

### Return type

[**DiskEncryptionSet**](DiskEncryptionSet.md)

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
| **0** | Error response describing why the operation failed. |  -  |

<a id="diskEncryptionSetsDelete"></a>
# **diskEncryptionSetsDelete**
> diskEncryptionSetsDelete(subscriptionId, resourceGroupName, diskEncryptionSetName, apiVersion)



Deletes a disk encryption set.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiskEncryptionSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DiskEncryptionSetsApi apiInstance = new DiskEncryptionSetsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String diskEncryptionSetName = "diskEncryptionSetName_example"; // String | The name of the disk encryption set that is being created. The name can't be changed after the disk encryption set is created. Supported characters for the name are a-z, A-Z, 0-9 and _. The maximum name length is 80 characters.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      apiInstance.diskEncryptionSetsDelete(subscriptionId, resourceGroupName, diskEncryptionSetName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiskEncryptionSetsApi#diskEncryptionSetsDelete");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **diskEncryptionSetName** | **String**| The name of the disk encryption set that is being created. The name can&#39;t be changed after the disk encryption set is created. Supported characters for the name are a-z, A-Z, 0-9 and _. The maximum name length is 80 characters. | |
| **apiVersion** | **String**| Client Api Version. | |

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
| **204** | If the disk encryption set is already deleted, this is an expected error code. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="diskEncryptionSetsGet"></a>
# **diskEncryptionSetsGet**
> DiskEncryptionSet diskEncryptionSetsGet(subscriptionId, resourceGroupName, diskEncryptionSetName, apiVersion)



Gets information about a disk encryption set.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiskEncryptionSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DiskEncryptionSetsApi apiInstance = new DiskEncryptionSetsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String diskEncryptionSetName = "diskEncryptionSetName_example"; // String | The name of the disk encryption set that is being created. The name can't be changed after the disk encryption set is created. Supported characters for the name are a-z, A-Z, 0-9 and _. The maximum name length is 80 characters.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      DiskEncryptionSet result = apiInstance.diskEncryptionSetsGet(subscriptionId, resourceGroupName, diskEncryptionSetName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiskEncryptionSetsApi#diskEncryptionSetsGet");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **diskEncryptionSetName** | **String**| The name of the disk encryption set that is being created. The name can&#39;t be changed after the disk encryption set is created. Supported characters for the name are a-z, A-Z, 0-9 and _. The maximum name length is 80 characters. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**DiskEncryptionSet**](DiskEncryptionSet.md)

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

<a id="diskEncryptionSetsList"></a>
# **diskEncryptionSetsList**
> DiskEncryptionSetList diskEncryptionSetsList(subscriptionId, apiVersion)



Lists all the disk encryption sets under a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiskEncryptionSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DiskEncryptionSetsApi apiInstance = new DiskEncryptionSetsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      DiskEncryptionSetList result = apiInstance.diskEncryptionSetsList(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiskEncryptionSetsApi#diskEncryptionSetsList");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**DiskEncryptionSetList**](DiskEncryptionSetList.md)

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

<a id="diskEncryptionSetsListByResourceGroup"></a>
# **diskEncryptionSetsListByResourceGroup**
> DiskEncryptionSetList diskEncryptionSetsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion)



Lists all the disk encryption sets under a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiskEncryptionSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DiskEncryptionSetsApi apiInstance = new DiskEncryptionSetsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      DiskEncryptionSetList result = apiInstance.diskEncryptionSetsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiskEncryptionSetsApi#diskEncryptionSetsListByResourceGroup");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**DiskEncryptionSetList**](DiskEncryptionSetList.md)

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

<a id="diskEncryptionSetsUpdate"></a>
# **diskEncryptionSetsUpdate**
> DiskEncryptionSet diskEncryptionSetsUpdate(subscriptionId, resourceGroupName, diskEncryptionSetName, apiVersion, diskEncryptionSet)



Updates (patches) a disk encryption set.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiskEncryptionSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DiskEncryptionSetsApi apiInstance = new DiskEncryptionSetsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String diskEncryptionSetName = "diskEncryptionSetName_example"; // String | The name of the disk encryption set that is being created. The name can't be changed after the disk encryption set is created. Supported characters for the name are a-z, A-Z, 0-9 and _. The maximum name length is 80 characters.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    DiskEncryptionSetUpdate diskEncryptionSet = new DiskEncryptionSetUpdate(); // DiskEncryptionSetUpdate | disk encryption set object supplied in the body of the Patch disk encryption set operation.
    try {
      DiskEncryptionSet result = apiInstance.diskEncryptionSetsUpdate(subscriptionId, resourceGroupName, diskEncryptionSetName, apiVersion, diskEncryptionSet);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiskEncryptionSetsApi#diskEncryptionSetsUpdate");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **diskEncryptionSetName** | **String**| The name of the disk encryption set that is being created. The name can&#39;t be changed after the disk encryption set is created. Supported characters for the name are a-z, A-Z, 0-9 and _. The maximum name length is 80 characters. | |
| **apiVersion** | **String**| Client Api Version. | |
| **diskEncryptionSet** | [**DiskEncryptionSetUpdate**](DiskEncryptionSetUpdate.md)| disk encryption set object supplied in the body of the Patch disk encryption set operation. | |

### Return type

[**DiskEncryptionSet**](DiskEncryptionSet.md)

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
| **0** | Error response describing why the operation failed. |  -  |

