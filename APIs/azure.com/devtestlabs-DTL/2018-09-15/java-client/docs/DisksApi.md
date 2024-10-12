# DisksApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**disksAttach**](DisksApi.md#disksAttach) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{userName}/disks/{name}/attach |  |
| [**disksCreateOrUpdate**](DisksApi.md#disksCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{userName}/disks/{name} |  |
| [**disksDelete**](DisksApi.md#disksDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{userName}/disks/{name} |  |
| [**disksDetach**](DisksApi.md#disksDetach) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{userName}/disks/{name}/detach |  |
| [**disksGet**](DisksApi.md#disksGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{userName}/disks/{name} |  |
| [**disksList**](DisksApi.md#disksList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{userName}/disks |  |
| [**disksUpdate**](DisksApi.md#disksUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{userName}/disks/{name} |  |


<a id="disksAttach"></a>
# **disksAttach**
> disksAttach(subscriptionId, resourceGroupName, labName, userName, name, apiVersion, attachDiskProperties)



Attach and create the lease of the disk to the virtual machine. This operation can take a while to complete.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DisksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DisksApi apiInstance = new DisksApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labName = "labName_example"; // String | The name of the lab.
    String userName = "userName_example"; // String | The name of the user profile.
    String name = "name_example"; // String | The name of the disk.
    String apiVersion = "2018-09-15"; // String | Client API version.
    AttachDiskProperties attachDiskProperties = new AttachDiskProperties(); // AttachDiskProperties | Properties of the disk to attach.
    try {
      apiInstance.disksAttach(subscriptionId, resourceGroupName, labName, userName, name, apiVersion, attachDiskProperties);
    } catch (ApiException e) {
      System.err.println("Exception when calling DisksApi#disksAttach");
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
| **userName** | **String**| The name of the user profile. | |
| **name** | **String**| The name of the disk. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-09-15] |
| **attachDiskProperties** | [**AttachDiskProperties**](AttachDiskProperties.md)| Properties of the disk to attach. | |

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

<a id="disksCreateOrUpdate"></a>
# **disksCreateOrUpdate**
> Disk disksCreateOrUpdate(subscriptionId, resourceGroupName, labName, userName, name, apiVersion, disk)



Create or replace an existing disk. This operation can take a while to complete.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DisksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DisksApi apiInstance = new DisksApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labName = "labName_example"; // String | The name of the lab.
    String userName = "userName_example"; // String | The name of the user profile.
    String name = "name_example"; // String | The name of the disk.
    String apiVersion = "2018-09-15"; // String | Client API version.
    Disk disk = new Disk(); // Disk | A Disk.
    try {
      Disk result = apiInstance.disksCreateOrUpdate(subscriptionId, resourceGroupName, labName, userName, name, apiVersion, disk);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DisksApi#disksCreateOrUpdate");
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
| **userName** | **String**| The name of the user profile. | |
| **name** | **String**| The name of the disk. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-09-15] |
| **disk** | [**Disk**](Disk.md)| A Disk. | |

### Return type

[**Disk**](Disk.md)

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

<a id="disksDelete"></a>
# **disksDelete**
> disksDelete(subscriptionId, resourceGroupName, labName, userName, name, apiVersion)



Delete disk. This operation can take a while to complete.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DisksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DisksApi apiInstance = new DisksApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labName = "labName_example"; // String | The name of the lab.
    String userName = "userName_example"; // String | The name of the user profile.
    String name = "name_example"; // String | The name of the disk.
    String apiVersion = "2018-09-15"; // String | Client API version.
    try {
      apiInstance.disksDelete(subscriptionId, resourceGroupName, labName, userName, name, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DisksApi#disksDelete");
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
| **userName** | **String**| The name of the user profile. | |
| **name** | **String**| The name of the disk. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-09-15] |

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
| **204** | No Content |  -  |
| **0** | BadRequest |  -  |

<a id="disksDetach"></a>
# **disksDetach**
> disksDetach(subscriptionId, resourceGroupName, labName, userName, name, apiVersion, detachDiskProperties)



Detach and break the lease of the disk attached to the virtual machine. This operation can take a while to complete.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DisksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DisksApi apiInstance = new DisksApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labName = "labName_example"; // String | The name of the lab.
    String userName = "userName_example"; // String | The name of the user profile.
    String name = "name_example"; // String | The name of the disk.
    String apiVersion = "2018-09-15"; // String | Client API version.
    DetachDiskProperties detachDiskProperties = new DetachDiskProperties(); // DetachDiskProperties | Properties of the disk to detach.
    try {
      apiInstance.disksDetach(subscriptionId, resourceGroupName, labName, userName, name, apiVersion, detachDiskProperties);
    } catch (ApiException e) {
      System.err.println("Exception when calling DisksApi#disksDetach");
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
| **userName** | **String**| The name of the user profile. | |
| **name** | **String**| The name of the disk. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-09-15] |
| **detachDiskProperties** | [**DetachDiskProperties**](DetachDiskProperties.md)| Properties of the disk to detach. | |

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

<a id="disksGet"></a>
# **disksGet**
> Disk disksGet(subscriptionId, resourceGroupName, labName, userName, name, apiVersion, $expand)



Get disk.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DisksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DisksApi apiInstance = new DisksApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labName = "labName_example"; // String | The name of the lab.
    String userName = "userName_example"; // String | The name of the user profile.
    String name = "name_example"; // String | The name of the disk.
    String apiVersion = "2018-09-15"; // String | Client API version.
    String $expand = "$expand_example"; // String | Specify the $expand query. Example: 'properties($select=diskType)'
    try {
      Disk result = apiInstance.disksGet(subscriptionId, resourceGroupName, labName, userName, name, apiVersion, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DisksApi#disksGet");
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
| **userName** | **String**| The name of the user profile. | |
| **name** | **String**| The name of the disk. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-09-15] |
| **$expand** | **String**| Specify the $expand query. Example: &#39;properties($select&#x3D;diskType)&#39; | [optional] |

### Return type

[**Disk**](Disk.md)

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

<a id="disksList"></a>
# **disksList**
> DiskList disksList(subscriptionId, resourceGroupName, labName, userName, apiVersion, $expand, $filter, $top, $orderby)



List disks in a given user profile.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DisksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DisksApi apiInstance = new DisksApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labName = "labName_example"; // String | The name of the lab.
    String userName = "userName_example"; // String | The name of the user profile.
    String apiVersion = "2018-09-15"; // String | Client API version.
    String $expand = "$expand_example"; // String | Specify the $expand query. Example: 'properties($select=diskType)'
    String $filter = "$filter_example"; // String | The filter to apply to the operation. Example: '$filter=contains(name,'myName')
    Integer $top = 56; // Integer | The maximum number of resources to return from the operation. Example: '$top=10'
    String $orderby = "$orderby_example"; // String | The ordering expression for the results, using OData notation. Example: '$orderby=name desc'
    try {
      DiskList result = apiInstance.disksList(subscriptionId, resourceGroupName, labName, userName, apiVersion, $expand, $filter, $top, $orderby);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DisksApi#disksList");
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
| **userName** | **String**| The name of the user profile. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-09-15] |
| **$expand** | **String**| Specify the $expand query. Example: &#39;properties($select&#x3D;diskType)&#39; | [optional] |
| **$filter** | **String**| The filter to apply to the operation. Example: &#39;$filter&#x3D;contains(name,&#39;myName&#39;) | [optional] |
| **$top** | **Integer**| The maximum number of resources to return from the operation. Example: &#39;$top&#x3D;10&#39; | [optional] |
| **$orderby** | **String**| The ordering expression for the results, using OData notation. Example: &#39;$orderby&#x3D;name desc&#39; | [optional] |

### Return type

[**DiskList**](DiskList.md)

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

<a id="disksUpdate"></a>
# **disksUpdate**
> Disk disksUpdate(subscriptionId, resourceGroupName, labName, userName, name, apiVersion, disk)



Allows modifying tags of disks. All other properties will be ignored.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DisksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DisksApi apiInstance = new DisksApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labName = "labName_example"; // String | The name of the lab.
    String userName = "userName_example"; // String | The name of the user profile.
    String name = "name_example"; // String | The name of the disk.
    String apiVersion = "2018-09-15"; // String | Client API version.
    DiskFragment disk = new DiskFragment(); // DiskFragment | A Disk.
    try {
      Disk result = apiInstance.disksUpdate(subscriptionId, resourceGroupName, labName, userName, name, apiVersion, disk);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DisksApi#disksUpdate");
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
| **userName** | **String**| The name of the user profile. | |
| **name** | **String**| The name of the disk. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-09-15] |
| **disk** | [**DiskFragment**](DiskFragment.md)| A Disk. | |

### Return type

[**Disk**](Disk.md)

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

