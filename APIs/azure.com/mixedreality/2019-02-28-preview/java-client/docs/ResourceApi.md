# ResourceApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**spatialAnchorsAccountsCreate**](ResourceApi.md#spatialAnchorsAccountsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MixedReality/spatialAnchorsAccounts/{spatialAnchorsAccountName} |  |
| [**spatialAnchorsAccountsDelete**](ResourceApi.md#spatialAnchorsAccountsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MixedReality/spatialAnchorsAccounts/{spatialAnchorsAccountName} |  |
| [**spatialAnchorsAccountsGet**](ResourceApi.md#spatialAnchorsAccountsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MixedReality/spatialAnchorsAccounts/{spatialAnchorsAccountName} |  |
| [**spatialAnchorsAccountsListByResourceGroup**](ResourceApi.md#spatialAnchorsAccountsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MixedReality/spatialAnchorsAccounts |  |
| [**spatialAnchorsAccountsListBySubscription**](ResourceApi.md#spatialAnchorsAccountsListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.MixedReality/spatialAnchorsAccounts |  |
| [**spatialAnchorsAccountsUpdate**](ResourceApi.md#spatialAnchorsAccountsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MixedReality/spatialAnchorsAccounts/{spatialAnchorsAccountName} |  |


<a id="spatialAnchorsAccountsCreate"></a>
# **spatialAnchorsAccountsCreate**
> SpatialAnchorsAccount spatialAnchorsAccountsCreate(subscriptionId, resourceGroupName, spatialAnchorsAccountName, apiVersion, spatialAnchorsAccount)



Creating or Updating a Spatial Anchors Account.

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
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String spatialAnchorsAccountName = "spatialAnchorsAccountName_example"; // String | Name of an Mixed Reality Spatial Anchors Account.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    SpatialAnchorsAccount spatialAnchorsAccount = new SpatialAnchorsAccount(); // SpatialAnchorsAccount | Spatial Anchors Account parameter.
    try {
      SpatialAnchorsAccount result = apiInstance.spatialAnchorsAccountsCreate(subscriptionId, resourceGroupName, spatialAnchorsAccountName, apiVersion, spatialAnchorsAccount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceApi#spatialAnchorsAccountsCreate");
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
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **spatialAnchorsAccountName** | **String**| Name of an Mixed Reality Spatial Anchors Account. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **spatialAnchorsAccount** | [**SpatialAnchorsAccount**](SpatialAnchorsAccount.md)| Spatial Anchors Account parameter. | |

### Return type

[**SpatialAnchorsAccount**](SpatialAnchorsAccount.md)

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

<a id="spatialAnchorsAccountsDelete"></a>
# **spatialAnchorsAccountsDelete**
> spatialAnchorsAccountsDelete(subscriptionId, resourceGroupName, spatialAnchorsAccountName, apiVersion)



Delete a Spatial Anchors Account.

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
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String spatialAnchorsAccountName = "spatialAnchorsAccountName_example"; // String | Name of an Mixed Reality Spatial Anchors Account.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    try {
      apiInstance.spatialAnchorsAccountsDelete(subscriptionId, resourceGroupName, spatialAnchorsAccountName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceApi#spatialAnchorsAccountsDelete");
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
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **spatialAnchorsAccountName** | **String**| Name of an Mixed Reality Spatial Anchors Account. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |

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
| **204** | NoContent |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="spatialAnchorsAccountsGet"></a>
# **spatialAnchorsAccountsGet**
> SpatialAnchorsAccount spatialAnchorsAccountsGet(subscriptionId, resourceGroupName, spatialAnchorsAccountName, apiVersion)



Retrieve a Spatial Anchors Account.

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
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String spatialAnchorsAccountName = "spatialAnchorsAccountName_example"; // String | Name of an Mixed Reality Spatial Anchors Account.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    try {
      SpatialAnchorsAccount result = apiInstance.spatialAnchorsAccountsGet(subscriptionId, resourceGroupName, spatialAnchorsAccountName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceApi#spatialAnchorsAccountsGet");
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
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **spatialAnchorsAccountName** | **String**| Name of an Mixed Reality Spatial Anchors Account. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |

### Return type

[**SpatialAnchorsAccount**](SpatialAnchorsAccount.md)

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

<a id="spatialAnchorsAccountsListByResourceGroup"></a>
# **spatialAnchorsAccountsListByResourceGroup**
> SpatialAnchorsAccountList spatialAnchorsAccountsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion)



List Resources by Resource Group

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
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    try {
      SpatialAnchorsAccountList result = apiInstance.spatialAnchorsAccountsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceApi#spatialAnchorsAccountsListByResourceGroup");
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
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |

### Return type

[**SpatialAnchorsAccountList**](SpatialAnchorsAccountList.md)

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

<a id="spatialAnchorsAccountsListBySubscription"></a>
# **spatialAnchorsAccountsListBySubscription**
> SpatialAnchorsAccountList spatialAnchorsAccountsListBySubscription(subscriptionId, apiVersion)



List Spatial Anchors Accounts by Subscription

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
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    try {
      SpatialAnchorsAccountList result = apiInstance.spatialAnchorsAccountsListBySubscription(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceApi#spatialAnchorsAccountsListBySubscription");
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
| **subscriptionId** | **String**| Azure subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |

### Return type

[**SpatialAnchorsAccountList**](SpatialAnchorsAccountList.md)

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

<a id="spatialAnchorsAccountsUpdate"></a>
# **spatialAnchorsAccountsUpdate**
> SpatialAnchorsAccount spatialAnchorsAccountsUpdate(subscriptionId, resourceGroupName, spatialAnchorsAccountName, apiVersion, spatialAnchorsAccount)



Updating a Spatial Anchors Account

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
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String spatialAnchorsAccountName = "spatialAnchorsAccountName_example"; // String | Name of an Mixed Reality Spatial Anchors Account.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    SpatialAnchorsAccount spatialAnchorsAccount = new SpatialAnchorsAccount(); // SpatialAnchorsAccount | Spatial Anchors Account parameter.
    try {
      SpatialAnchorsAccount result = apiInstance.spatialAnchorsAccountsUpdate(subscriptionId, resourceGroupName, spatialAnchorsAccountName, apiVersion, spatialAnchorsAccount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceApi#spatialAnchorsAccountsUpdate");
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
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **spatialAnchorsAccountName** | **String**| Name of an Mixed Reality Spatial Anchors Account. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **spatialAnchorsAccount** | [**SpatialAnchorsAccount**](SpatialAnchorsAccount.md)| Spatial Anchors Account parameter. | |

### Return type

[**SpatialAnchorsAccount**](SpatialAnchorsAccount.md)

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

