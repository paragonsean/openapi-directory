# PoolApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**poolCreate**](PoolApi.md#poolCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/pools/{poolName} |  |
| [**poolDelete**](PoolApi.md#poolDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/pools/{poolName} |  |
| [**poolDisableAutoScale**](PoolApi.md#poolDisableAutoScale) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/pools/{poolName}/disableAutoScale |  |
| [**poolGet**](PoolApi.md#poolGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/pools/{poolName} |  |
| [**poolListByBatchAccount**](PoolApi.md#poolListByBatchAccount) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/pools |  |
| [**poolStopResize**](PoolApi.md#poolStopResize) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/pools/{poolName}/stopResize | Stops an ongoing resize operation on the pool. |
| [**poolUpdate**](PoolApi.md#poolUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/pools/{poolName} |  |


<a id="poolCreate"></a>
# **poolCreate**
> Pool poolCreate(resourceGroupName, accountName, poolName, apiVersion, subscriptionId, parameters, ifMatch, ifNoneMatch)



Creates a new pool inside the specified account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PoolApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PoolApi apiInstance = new PoolApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
    String accountName = "accountName_example"; // String | The name of the Batch account.
    String poolName = "poolName_example"; // String | The pool name. This must be unique within the account.
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    Pool parameters = new Pool(); // Pool | Additional parameters for pool creation.
    String ifMatch = "ifMatch_example"; // String | The entity state (ETag) version of the pool to update. A value of \"*\" can be used to apply the operation only if the pool already exists. If omitted, this operation will always be applied.
    String ifNoneMatch = "ifNoneMatch_example"; // String | Set to '*' to allow a new pool to be created, but to prevent updating an existing pool. Other values will be ignored.
    try {
      Pool result = apiInstance.poolCreate(resourceGroupName, accountName, poolName, apiVersion, subscriptionId, parameters, ifMatch, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PoolApi#poolCreate");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the Batch account. | |
| **accountName** | **String**| The name of the Batch account. | |
| **poolName** | **String**| The pool name. This must be unique within the account. | |
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |
| **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | |
| **parameters** | [**Pool**](Pool.md)| Additional parameters for pool creation. | |
| **ifMatch** | **String**| The entity state (ETag) version of the pool to update. A value of \&quot;*\&quot; can be used to apply the operation only if the pool already exists. If omitted, this operation will always be applied. | [optional] |
| **ifNoneMatch** | **String**| Set to &#39;*&#39; to allow a new pool to be created, but to prevent updating an existing pool. Other values will be ignored. | [optional] |

### Return type

[**Pool**](Pool.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The operation was successful. The response contains the pool entity. |  * ETag - The ETag HTTP response header. This is an opaque string. You can use it to detect whether the resource has changed between requests. In particular, you can pass the ETag to one of the If-Match or If-None-Match headers. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="poolDelete"></a>
# **poolDelete**
> poolDelete(resourceGroupName, accountName, poolName, apiVersion, subscriptionId)



Deletes the specified pool.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PoolApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PoolApi apiInstance = new PoolApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
    String accountName = "accountName_example"; // String | The name of the Batch account.
    String poolName = "poolName_example"; // String | The pool name. This must be unique within the account.
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    try {
      apiInstance.poolDelete(resourceGroupName, accountName, poolName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling PoolApi#poolDelete");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the Batch account. | |
| **accountName** | **String**| The name of the Batch account. | |
| **poolName** | **String**| The pool name. This must be unique within the account. | |
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |
| **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | |

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
| **200** | The operation was successful. |  -  |
| **202** | The operation will be completed asynchronously. |  * Retry-After - Suggested delay to check the status of the asynchronous operation. The value is an integer that represents the seconds. <br>  * Location - The URL of the resource used to check the status of the asynchronous operation. <br>  |
| **204** | The operation was successful. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="poolDisableAutoScale"></a>
# **poolDisableAutoScale**
> Pool poolDisableAutoScale(resourceGroupName, accountName, poolName, apiVersion, subscriptionId)



Disables automatic scaling for a pool.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PoolApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PoolApi apiInstance = new PoolApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
    String accountName = "accountName_example"; // String | The name of the Batch account.
    String poolName = "poolName_example"; // String | The pool name. This must be unique within the account.
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    try {
      Pool result = apiInstance.poolDisableAutoScale(resourceGroupName, accountName, poolName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PoolApi#poolDisableAutoScale");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the Batch account. | |
| **accountName** | **String**| The name of the Batch account. | |
| **poolName** | **String**| The pool name. This must be unique within the account. | |
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |
| **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | |

### Return type

[**Pool**](Pool.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The operation was successful. The response contains the pool entity. |  * ETag - The ETag HTTP response header. This is an opaque string. You can use it to detect whether the resource has changed between requests. In particular, you can pass the ETag to one of the If-Match or If-None-Match headers. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="poolGet"></a>
# **poolGet**
> Pool poolGet(resourceGroupName, accountName, poolName, apiVersion, subscriptionId)



Gets information about the specified pool.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PoolApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PoolApi apiInstance = new PoolApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
    String accountName = "accountName_example"; // String | The name of the Batch account.
    String poolName = "poolName_example"; // String | The pool name. This must be unique within the account.
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    try {
      Pool result = apiInstance.poolGet(resourceGroupName, accountName, poolName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PoolApi#poolGet");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the Batch account. | |
| **accountName** | **String**| The name of the Batch account. | |
| **poolName** | **String**| The pool name. This must be unique within the account. | |
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |
| **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | |

### Return type

[**Pool**](Pool.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The operation was successful. The response contains the pool entity. |  * ETag - The ETag HTTP response header. This is an opaque string. You can use it to detect whether the resource has changed between requests. In particular, you can pass the ETag to one of the If-Match or If-None-Match headers. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="poolListByBatchAccount"></a>
# **poolListByBatchAccount**
> ListPoolsResult poolListByBatchAccount(resourceGroupName, accountName, apiVersion, subscriptionId, maxresults, $select, $filter)



Lists all of the pools in the specified account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PoolApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PoolApi apiInstance = new PoolApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
    String accountName = "accountName_example"; // String | The name of the Batch account.
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    Integer maxresults = 56; // Integer | The maximum number of items to return in the response.
    String $select = "$select_example"; // String | Comma separated list of properties that should be returned. e.g. \"properties/provisioningState\". Only top level properties under properties/ are valid for selection.
    String $filter = "$filter_example"; // String | OData filter expression. Valid properties for filtering are:   name  properties/allocationState  properties/allocationStateTransitionTime  properties/creationTime  properties/provisioningState  properties/provisioningStateTransitionTime  properties/lastModified  properties/vmSize  properties/interNodeCommunication  properties/scaleSettings/autoScale  properties/scaleSettings/fixedScale
    try {
      ListPoolsResult result = apiInstance.poolListByBatchAccount(resourceGroupName, accountName, apiVersion, subscriptionId, maxresults, $select, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PoolApi#poolListByBatchAccount");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the Batch account. | |
| **accountName** | **String**| The name of the Batch account. | |
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |
| **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | |
| **maxresults** | **Integer**| The maximum number of items to return in the response. | [optional] |
| **$select** | **String**| Comma separated list of properties that should be returned. e.g. \&quot;properties/provisioningState\&quot;. Only top level properties under properties/ are valid for selection. | [optional] |
| **$filter** | **String**| OData filter expression. Valid properties for filtering are:   name  properties/allocationState  properties/allocationStateTransitionTime  properties/creationTime  properties/provisioningState  properties/provisioningStateTransitionTime  properties/lastModified  properties/vmSize  properties/interNodeCommunication  properties/scaleSettings/autoScale  properties/scaleSettings/fixedScale | [optional] |

### Return type

[**ListPoolsResult**](ListPoolsResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The operation was successful. The response contains a list of certificates associated with the account. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="poolStopResize"></a>
# **poolStopResize**
> Pool poolStopResize(resourceGroupName, accountName, poolName, apiVersion, subscriptionId)

Stops an ongoing resize operation on the pool.

This does not restore the pool to its previous state before the resize operation: it only stops any further changes being made, and the pool maintains its current state. After stopping, the pool stabilizes at the number of nodes it was at when the stop operation was done. During the stop operation, the pool allocation state changes first to stopping and then to steady. A resize operation need not be an explicit resize pool request; this API can also be used to halt the initial sizing of the pool when it is created.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PoolApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PoolApi apiInstance = new PoolApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
    String accountName = "accountName_example"; // String | The name of the Batch account.
    String poolName = "poolName_example"; // String | The pool name. This must be unique within the account.
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    try {
      Pool result = apiInstance.poolStopResize(resourceGroupName, accountName, poolName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PoolApi#poolStopResize");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the Batch account. | |
| **accountName** | **String**| The name of the Batch account. | |
| **poolName** | **String**| The pool name. This must be unique within the account. | |
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |
| **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | |

### Return type

[**Pool**](Pool.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The operation was successful. The response contains the pool entity. |  * ETag - The ETag HTTP response header. This is an opaque string. You can use it to detect whether the resource has changed between requests. In particular, you can pass the ETag to one of the If-Match or If-None-Match headers. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="poolUpdate"></a>
# **poolUpdate**
> Pool poolUpdate(resourceGroupName, accountName, poolName, apiVersion, subscriptionId, parameters, ifMatch)



Updates the properties of an existing pool.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PoolApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PoolApi apiInstance = new PoolApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
    String accountName = "accountName_example"; // String | The name of the Batch account.
    String poolName = "poolName_example"; // String | The pool name. This must be unique within the account.
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    Pool parameters = new Pool(); // Pool | Pool properties that should be updated. Properties that are supplied will be updated, any property not supplied will be unchanged.
    String ifMatch = "ifMatch_example"; // String | The entity state (ETag) version of the pool to update. This value can be omitted or set to \"*\" to apply the operation unconditionally.
    try {
      Pool result = apiInstance.poolUpdate(resourceGroupName, accountName, poolName, apiVersion, subscriptionId, parameters, ifMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PoolApi#poolUpdate");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the Batch account. | |
| **accountName** | **String**| The name of the Batch account. | |
| **poolName** | **String**| The pool name. This must be unique within the account. | |
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |
| **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | |
| **parameters** | [**Pool**](Pool.md)| Pool properties that should be updated. Properties that are supplied will be updated, any property not supplied will be unchanged. | |
| **ifMatch** | **String**| The entity state (ETag) version of the pool to update. This value can be omitted or set to \&quot;*\&quot; to apply the operation unconditionally. | [optional] |

### Return type

[**Pool**](Pool.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The operation was successful. The response contains the pool entity. |  * ETag - The ETag HTTP response header. This is an opaque string. You can use it to detect whether the resource has changed between requests. In particular, you can pass the ETag to one of the If-Match or If-None-Match headers. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

