# VirtualizationApi

All URIs are relative to *http://netboxdemo.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**virtualizationChoicesList**](VirtualizationApi.md#virtualizationChoicesList) | **GET** /virtualization/_choices/ |  |
| [**virtualizationChoicesRead**](VirtualizationApi.md#virtualizationChoicesRead) | **GET** /virtualization/_choices/{id}/ |  |
| [**virtualizationClusterGroupsCreate**](VirtualizationApi.md#virtualizationClusterGroupsCreate) | **POST** /virtualization/cluster-groups/ |  |
| [**virtualizationClusterGroupsDelete**](VirtualizationApi.md#virtualizationClusterGroupsDelete) | **DELETE** /virtualization/cluster-groups/{id}/ |  |
| [**virtualizationClusterGroupsList**](VirtualizationApi.md#virtualizationClusterGroupsList) | **GET** /virtualization/cluster-groups/ |  |
| [**virtualizationClusterGroupsPartialUpdate**](VirtualizationApi.md#virtualizationClusterGroupsPartialUpdate) | **PATCH** /virtualization/cluster-groups/{id}/ |  |
| [**virtualizationClusterGroupsRead**](VirtualizationApi.md#virtualizationClusterGroupsRead) | **GET** /virtualization/cluster-groups/{id}/ |  |
| [**virtualizationClusterGroupsUpdate**](VirtualizationApi.md#virtualizationClusterGroupsUpdate) | **PUT** /virtualization/cluster-groups/{id}/ |  |
| [**virtualizationClusterTypesCreate**](VirtualizationApi.md#virtualizationClusterTypesCreate) | **POST** /virtualization/cluster-types/ |  |
| [**virtualizationClusterTypesDelete**](VirtualizationApi.md#virtualizationClusterTypesDelete) | **DELETE** /virtualization/cluster-types/{id}/ |  |
| [**virtualizationClusterTypesList**](VirtualizationApi.md#virtualizationClusterTypesList) | **GET** /virtualization/cluster-types/ |  |
| [**virtualizationClusterTypesPartialUpdate**](VirtualizationApi.md#virtualizationClusterTypesPartialUpdate) | **PATCH** /virtualization/cluster-types/{id}/ |  |
| [**virtualizationClusterTypesRead**](VirtualizationApi.md#virtualizationClusterTypesRead) | **GET** /virtualization/cluster-types/{id}/ |  |
| [**virtualizationClusterTypesUpdate**](VirtualizationApi.md#virtualizationClusterTypesUpdate) | **PUT** /virtualization/cluster-types/{id}/ |  |
| [**virtualizationClustersCreate**](VirtualizationApi.md#virtualizationClustersCreate) | **POST** /virtualization/clusters/ |  |
| [**virtualizationClustersDelete**](VirtualizationApi.md#virtualizationClustersDelete) | **DELETE** /virtualization/clusters/{id}/ |  |
| [**virtualizationClustersList**](VirtualizationApi.md#virtualizationClustersList) | **GET** /virtualization/clusters/ |  |
| [**virtualizationClustersPartialUpdate**](VirtualizationApi.md#virtualizationClustersPartialUpdate) | **PATCH** /virtualization/clusters/{id}/ |  |
| [**virtualizationClustersRead**](VirtualizationApi.md#virtualizationClustersRead) | **GET** /virtualization/clusters/{id}/ |  |
| [**virtualizationClustersUpdate**](VirtualizationApi.md#virtualizationClustersUpdate) | **PUT** /virtualization/clusters/{id}/ |  |
| [**virtualizationInterfacesCreate**](VirtualizationApi.md#virtualizationInterfacesCreate) | **POST** /virtualization/interfaces/ |  |
| [**virtualizationInterfacesDelete**](VirtualizationApi.md#virtualizationInterfacesDelete) | **DELETE** /virtualization/interfaces/{id}/ |  |
| [**virtualizationInterfacesList**](VirtualizationApi.md#virtualizationInterfacesList) | **GET** /virtualization/interfaces/ |  |
| [**virtualizationInterfacesPartialUpdate**](VirtualizationApi.md#virtualizationInterfacesPartialUpdate) | **PATCH** /virtualization/interfaces/{id}/ |  |
| [**virtualizationInterfacesRead**](VirtualizationApi.md#virtualizationInterfacesRead) | **GET** /virtualization/interfaces/{id}/ |  |
| [**virtualizationInterfacesUpdate**](VirtualizationApi.md#virtualizationInterfacesUpdate) | **PUT** /virtualization/interfaces/{id}/ |  |
| [**virtualizationVirtualMachinesCreate**](VirtualizationApi.md#virtualizationVirtualMachinesCreate) | **POST** /virtualization/virtual-machines/ |  |
| [**virtualizationVirtualMachinesDelete**](VirtualizationApi.md#virtualizationVirtualMachinesDelete) | **DELETE** /virtualization/virtual-machines/{id}/ |  |
| [**virtualizationVirtualMachinesList**](VirtualizationApi.md#virtualizationVirtualMachinesList) | **GET** /virtualization/virtual-machines/ |  |
| [**virtualizationVirtualMachinesPartialUpdate**](VirtualizationApi.md#virtualizationVirtualMachinesPartialUpdate) | **PATCH** /virtualization/virtual-machines/{id}/ |  |
| [**virtualizationVirtualMachinesRead**](VirtualizationApi.md#virtualizationVirtualMachinesRead) | **GET** /virtualization/virtual-machines/{id}/ |  |
| [**virtualizationVirtualMachinesUpdate**](VirtualizationApi.md#virtualizationVirtualMachinesUpdate) | **PUT** /virtualization/virtual-machines/{id}/ |  |


<a id="virtualizationChoicesList"></a>
# **virtualizationChoicesList**
> virtualizationChoicesList()





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    VirtualizationApi apiInstance = new VirtualizationApi(defaultClient);
    try {
      apiInstance.virtualizationChoicesList();
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualizationApi#virtualizationChoicesList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="virtualizationChoicesRead"></a>
# **virtualizationChoicesRead**
> virtualizationChoicesRead(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    VirtualizationApi apiInstance = new VirtualizationApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.virtualizationChoicesRead(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualizationApi#virtualizationChoicesRead");
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
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="virtualizationClusterGroupsCreate"></a>
# **virtualizationClusterGroupsCreate**
> ClusterGroup virtualizationClusterGroupsCreate(clusterGroup)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    VirtualizationApi apiInstance = new VirtualizationApi(defaultClient);
    ClusterGroup clusterGroup = new ClusterGroup(); // ClusterGroup | 
    try {
      ClusterGroup result = apiInstance.virtualizationClusterGroupsCreate(clusterGroup);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualizationApi#virtualizationClusterGroupsCreate");
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
| **clusterGroup** | [**ClusterGroup**](ClusterGroup.md)|  | |

### Return type

[**ClusterGroup**](ClusterGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="virtualizationClusterGroupsDelete"></a>
# **virtualizationClusterGroupsDelete**
> virtualizationClusterGroupsDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    VirtualizationApi apiInstance = new VirtualizationApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this cluster group.
    try {
      apiInstance.virtualizationClusterGroupsDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualizationApi#virtualizationClusterGroupsDelete");
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
| **id** | **Integer**| A unique integer value identifying this cluster group. | |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |

<a id="virtualizationClusterGroupsList"></a>
# **virtualizationClusterGroupsList**
> VirtualizationClusterGroupsList200Response virtualizationClusterGroupsList(name, slug, limit, offset)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    VirtualizationApi apiInstance = new VirtualizationApi(defaultClient);
    String name = "name_example"; // String | 
    String slug = "slug_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      VirtualizationClusterGroupsList200Response result = apiInstance.virtualizationClusterGroupsList(name, slug, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualizationApi#virtualizationClusterGroupsList");
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
| **name** | **String**|  | [optional] |
| **slug** | **String**|  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**VirtualizationClusterGroupsList200Response**](VirtualizationClusterGroupsList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="virtualizationClusterGroupsPartialUpdate"></a>
# **virtualizationClusterGroupsPartialUpdate**
> ClusterGroup virtualizationClusterGroupsPartialUpdate(id, clusterGroup)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    VirtualizationApi apiInstance = new VirtualizationApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this cluster group.
    ClusterGroup clusterGroup = new ClusterGroup(); // ClusterGroup | 
    try {
      ClusterGroup result = apiInstance.virtualizationClusterGroupsPartialUpdate(id, clusterGroup);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualizationApi#virtualizationClusterGroupsPartialUpdate");
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
| **id** | **Integer**| A unique integer value identifying this cluster group. | |
| **clusterGroup** | [**ClusterGroup**](ClusterGroup.md)|  | |

### Return type

[**ClusterGroup**](ClusterGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="virtualizationClusterGroupsRead"></a>
# **virtualizationClusterGroupsRead**
> ClusterGroup virtualizationClusterGroupsRead(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    VirtualizationApi apiInstance = new VirtualizationApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this cluster group.
    try {
      ClusterGroup result = apiInstance.virtualizationClusterGroupsRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualizationApi#virtualizationClusterGroupsRead");
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
| **id** | **Integer**| A unique integer value identifying this cluster group. | |

### Return type

[**ClusterGroup**](ClusterGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="virtualizationClusterGroupsUpdate"></a>
# **virtualizationClusterGroupsUpdate**
> ClusterGroup virtualizationClusterGroupsUpdate(id, clusterGroup)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    VirtualizationApi apiInstance = new VirtualizationApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this cluster group.
    ClusterGroup clusterGroup = new ClusterGroup(); // ClusterGroup | 
    try {
      ClusterGroup result = apiInstance.virtualizationClusterGroupsUpdate(id, clusterGroup);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualizationApi#virtualizationClusterGroupsUpdate");
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
| **id** | **Integer**| A unique integer value identifying this cluster group. | |
| **clusterGroup** | [**ClusterGroup**](ClusterGroup.md)|  | |

### Return type

[**ClusterGroup**](ClusterGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="virtualizationClusterTypesCreate"></a>
# **virtualizationClusterTypesCreate**
> ClusterType virtualizationClusterTypesCreate(clusterType)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    VirtualizationApi apiInstance = new VirtualizationApi(defaultClient);
    ClusterType clusterType = new ClusterType(); // ClusterType | 
    try {
      ClusterType result = apiInstance.virtualizationClusterTypesCreate(clusterType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualizationApi#virtualizationClusterTypesCreate");
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
| **clusterType** | [**ClusterType**](ClusterType.md)|  | |

### Return type

[**ClusterType**](ClusterType.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="virtualizationClusterTypesDelete"></a>
# **virtualizationClusterTypesDelete**
> virtualizationClusterTypesDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    VirtualizationApi apiInstance = new VirtualizationApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this cluster type.
    try {
      apiInstance.virtualizationClusterTypesDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualizationApi#virtualizationClusterTypesDelete");
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
| **id** | **Integer**| A unique integer value identifying this cluster type. | |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |

<a id="virtualizationClusterTypesList"></a>
# **virtualizationClusterTypesList**
> VirtualizationClusterTypesList200Response virtualizationClusterTypesList(name, slug, limit, offset)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    VirtualizationApi apiInstance = new VirtualizationApi(defaultClient);
    String name = "name_example"; // String | 
    String slug = "slug_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      VirtualizationClusterTypesList200Response result = apiInstance.virtualizationClusterTypesList(name, slug, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualizationApi#virtualizationClusterTypesList");
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
| **name** | **String**|  | [optional] |
| **slug** | **String**|  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**VirtualizationClusterTypesList200Response**](VirtualizationClusterTypesList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="virtualizationClusterTypesPartialUpdate"></a>
# **virtualizationClusterTypesPartialUpdate**
> ClusterType virtualizationClusterTypesPartialUpdate(id, clusterType)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    VirtualizationApi apiInstance = new VirtualizationApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this cluster type.
    ClusterType clusterType = new ClusterType(); // ClusterType | 
    try {
      ClusterType result = apiInstance.virtualizationClusterTypesPartialUpdate(id, clusterType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualizationApi#virtualizationClusterTypesPartialUpdate");
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
| **id** | **Integer**| A unique integer value identifying this cluster type. | |
| **clusterType** | [**ClusterType**](ClusterType.md)|  | |

### Return type

[**ClusterType**](ClusterType.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="virtualizationClusterTypesRead"></a>
# **virtualizationClusterTypesRead**
> ClusterType virtualizationClusterTypesRead(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    VirtualizationApi apiInstance = new VirtualizationApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this cluster type.
    try {
      ClusterType result = apiInstance.virtualizationClusterTypesRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualizationApi#virtualizationClusterTypesRead");
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
| **id** | **Integer**| A unique integer value identifying this cluster type. | |

### Return type

[**ClusterType**](ClusterType.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="virtualizationClusterTypesUpdate"></a>
# **virtualizationClusterTypesUpdate**
> ClusterType virtualizationClusterTypesUpdate(id, clusterType)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    VirtualizationApi apiInstance = new VirtualizationApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this cluster type.
    ClusterType clusterType = new ClusterType(); // ClusterType | 
    try {
      ClusterType result = apiInstance.virtualizationClusterTypesUpdate(id, clusterType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualizationApi#virtualizationClusterTypesUpdate");
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
| **id** | **Integer**| A unique integer value identifying this cluster type. | |
| **clusterType** | [**ClusterType**](ClusterType.md)|  | |

### Return type

[**ClusterType**](ClusterType.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="virtualizationClustersCreate"></a>
# **virtualizationClustersCreate**
> Cluster virtualizationClustersCreate(writableCluster)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    VirtualizationApi apiInstance = new VirtualizationApi(defaultClient);
    WritableCluster writableCluster = new WritableCluster(); // WritableCluster | 
    try {
      Cluster result = apiInstance.virtualizationClustersCreate(writableCluster);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualizationApi#virtualizationClustersCreate");
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
| **writableCluster** | [**WritableCluster**](WritableCluster.md)|  | |

### Return type

[**Cluster**](Cluster.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="virtualizationClustersDelete"></a>
# **virtualizationClustersDelete**
> virtualizationClustersDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    VirtualizationApi apiInstance = new VirtualizationApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this cluster.
    try {
      apiInstance.virtualizationClustersDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualizationApi#virtualizationClustersDelete");
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
| **id** | **Integer**| A unique integer value identifying this cluster. | |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |

<a id="virtualizationClustersList"></a>
# **virtualizationClustersList**
> VirtualizationClustersList200Response virtualizationClustersList(name, idIn, q, groupId, group, typeId, type, siteId, site, tag, limit, offset)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    VirtualizationApi apiInstance = new VirtualizationApi(defaultClient);
    String name = "name_example"; // String | 
    String idIn = "idIn_example"; // String | Multiple values may be separated by commas.
    String q = "q_example"; // String | 
    String groupId = "groupId_example"; // String | 
    String group = "group_example"; // String | 
    String typeId = "typeId_example"; // String | 
    String type = "type_example"; // String | 
    String siteId = "siteId_example"; // String | 
    String site = "site_example"; // String | 
    String tag = "tag_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      VirtualizationClustersList200Response result = apiInstance.virtualizationClustersList(name, idIn, q, groupId, group, typeId, type, siteId, site, tag, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualizationApi#virtualizationClustersList");
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
| **name** | **String**|  | [optional] |
| **idIn** | **String**| Multiple values may be separated by commas. | [optional] |
| **q** | **String**|  | [optional] |
| **groupId** | **String**|  | [optional] |
| **group** | **String**|  | [optional] |
| **typeId** | **String**|  | [optional] |
| **type** | **String**|  | [optional] |
| **siteId** | **String**|  | [optional] |
| **site** | **String**|  | [optional] |
| **tag** | **String**|  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**VirtualizationClustersList200Response**](VirtualizationClustersList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="virtualizationClustersPartialUpdate"></a>
# **virtualizationClustersPartialUpdate**
> Cluster virtualizationClustersPartialUpdate(id, writableCluster)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    VirtualizationApi apiInstance = new VirtualizationApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this cluster.
    WritableCluster writableCluster = new WritableCluster(); // WritableCluster | 
    try {
      Cluster result = apiInstance.virtualizationClustersPartialUpdate(id, writableCluster);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualizationApi#virtualizationClustersPartialUpdate");
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
| **id** | **Integer**| A unique integer value identifying this cluster. | |
| **writableCluster** | [**WritableCluster**](WritableCluster.md)|  | |

### Return type

[**Cluster**](Cluster.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="virtualizationClustersRead"></a>
# **virtualizationClustersRead**
> Cluster virtualizationClustersRead(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    VirtualizationApi apiInstance = new VirtualizationApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this cluster.
    try {
      Cluster result = apiInstance.virtualizationClustersRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualizationApi#virtualizationClustersRead");
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
| **id** | **Integer**| A unique integer value identifying this cluster. | |

### Return type

[**Cluster**](Cluster.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="virtualizationClustersUpdate"></a>
# **virtualizationClustersUpdate**
> Cluster virtualizationClustersUpdate(id, writableCluster)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    VirtualizationApi apiInstance = new VirtualizationApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this cluster.
    WritableCluster writableCluster = new WritableCluster(); // WritableCluster | 
    try {
      Cluster result = apiInstance.virtualizationClustersUpdate(id, writableCluster);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualizationApi#virtualizationClustersUpdate");
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
| **id** | **Integer**| A unique integer value identifying this cluster. | |
| **writableCluster** | [**WritableCluster**](WritableCluster.md)|  | |

### Return type

[**Cluster**](Cluster.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="virtualizationInterfacesCreate"></a>
# **virtualizationInterfacesCreate**
> ModelInterface virtualizationInterfacesCreate(writableInterface)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    VirtualizationApi apiInstance = new VirtualizationApi(defaultClient);
    WritableInterface writableInterface = new WritableInterface(); // WritableInterface | 
    try {
      ModelInterface result = apiInstance.virtualizationInterfacesCreate(writableInterface);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualizationApi#virtualizationInterfacesCreate");
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
| **writableInterface** | [**WritableInterface**](WritableInterface.md)|  | |

### Return type

[**ModelInterface**](ModelInterface.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="virtualizationInterfacesDelete"></a>
# **virtualizationInterfacesDelete**
> virtualizationInterfacesDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    VirtualizationApi apiInstance = new VirtualizationApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this interface.
    try {
      apiInstance.virtualizationInterfacesDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualizationApi#virtualizationInterfacesDelete");
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
| **id** | **Integer**| A unique integer value identifying this interface. | |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |

<a id="virtualizationInterfacesList"></a>
# **virtualizationInterfacesList**
> DcimInterfacesList200Response virtualizationInterfacesList(name, enabled, mtu, virtualMachineId, virtualMachine, macAddress, limit, offset)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    VirtualizationApi apiInstance = new VirtualizationApi(defaultClient);
    String name = "name_example"; // String | 
    String enabled = "enabled_example"; // String | 
    BigDecimal mtu = new BigDecimal(78); // BigDecimal | 
    String virtualMachineId = "virtualMachineId_example"; // String | 
    String virtualMachine = "virtualMachine_example"; // String | 
    String macAddress = "macAddress_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      DcimInterfacesList200Response result = apiInstance.virtualizationInterfacesList(name, enabled, mtu, virtualMachineId, virtualMachine, macAddress, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualizationApi#virtualizationInterfacesList");
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
| **name** | **String**|  | [optional] |
| **enabled** | **String**|  | [optional] |
| **mtu** | **BigDecimal**|  | [optional] |
| **virtualMachineId** | **String**|  | [optional] |
| **virtualMachine** | **String**|  | [optional] |
| **macAddress** | **String**|  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**DcimInterfacesList200Response**](DcimInterfacesList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="virtualizationInterfacesPartialUpdate"></a>
# **virtualizationInterfacesPartialUpdate**
> ModelInterface virtualizationInterfacesPartialUpdate(id, writableInterface)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    VirtualizationApi apiInstance = new VirtualizationApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this interface.
    WritableInterface writableInterface = new WritableInterface(); // WritableInterface | 
    try {
      ModelInterface result = apiInstance.virtualizationInterfacesPartialUpdate(id, writableInterface);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualizationApi#virtualizationInterfacesPartialUpdate");
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
| **id** | **Integer**| A unique integer value identifying this interface. | |
| **writableInterface** | [**WritableInterface**](WritableInterface.md)|  | |

### Return type

[**ModelInterface**](ModelInterface.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="virtualizationInterfacesRead"></a>
# **virtualizationInterfacesRead**
> ModelInterface virtualizationInterfacesRead(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    VirtualizationApi apiInstance = new VirtualizationApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this interface.
    try {
      ModelInterface result = apiInstance.virtualizationInterfacesRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualizationApi#virtualizationInterfacesRead");
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
| **id** | **Integer**| A unique integer value identifying this interface. | |

### Return type

[**ModelInterface**](ModelInterface.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="virtualizationInterfacesUpdate"></a>
# **virtualizationInterfacesUpdate**
> ModelInterface virtualizationInterfacesUpdate(id, writableInterface)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    VirtualizationApi apiInstance = new VirtualizationApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this interface.
    WritableInterface writableInterface = new WritableInterface(); // WritableInterface | 
    try {
      ModelInterface result = apiInstance.virtualizationInterfacesUpdate(id, writableInterface);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualizationApi#virtualizationInterfacesUpdate");
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
| **id** | **Integer**| A unique integer value identifying this interface. | |
| **writableInterface** | [**WritableInterface**](WritableInterface.md)|  | |

### Return type

[**ModelInterface**](ModelInterface.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="virtualizationVirtualMachinesCreate"></a>
# **virtualizationVirtualMachinesCreate**
> VirtualMachine virtualizationVirtualMachinesCreate(writableVirtualMachine)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    VirtualizationApi apiInstance = new VirtualizationApi(defaultClient);
    WritableVirtualMachine writableVirtualMachine = new WritableVirtualMachine(); // WritableVirtualMachine | 
    try {
      VirtualMachine result = apiInstance.virtualizationVirtualMachinesCreate(writableVirtualMachine);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualizationApi#virtualizationVirtualMachinesCreate");
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
| **writableVirtualMachine** | [**WritableVirtualMachine**](WritableVirtualMachine.md)|  | |

### Return type

[**VirtualMachine**](VirtualMachine.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="virtualizationVirtualMachinesDelete"></a>
# **virtualizationVirtualMachinesDelete**
> virtualizationVirtualMachinesDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    VirtualizationApi apiInstance = new VirtualizationApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this virtual machine.
    try {
      apiInstance.virtualizationVirtualMachinesDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualizationApi#virtualizationVirtualMachinesDelete");
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
| **id** | **Integer**| A unique integer value identifying this virtual machine. | |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |

<a id="virtualizationVirtualMachinesList"></a>
# **virtualizationVirtualMachinesList**
> VirtualizationVirtualMachinesList200Response virtualizationVirtualMachinesList(name, cluster, idIn, q, status, clusterGroupId, clusterGroup, clusterTypeId, clusterType, clusterId, regionId, region, siteId, site, roleId, role, tenantId, tenant, platformId, platform, tag, limit, offset)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    VirtualizationApi apiInstance = new VirtualizationApi(defaultClient);
    String name = "name_example"; // String | 
    String cluster = "cluster_example"; // String | 
    String idIn = "idIn_example"; // String | Multiple values may be separated by commas.
    String q = "q_example"; // String | 
    String status = "status_example"; // String | 
    String clusterGroupId = "clusterGroupId_example"; // String | 
    String clusterGroup = "clusterGroup_example"; // String | 
    String clusterTypeId = "clusterTypeId_example"; // String | 
    String clusterType = "clusterType_example"; // String | 
    String clusterId = "clusterId_example"; // String | 
    BigDecimal regionId = new BigDecimal(78); // BigDecimal | 
    String region = "region_example"; // String | 
    String siteId = "siteId_example"; // String | 
    String site = "site_example"; // String | 
    String roleId = "roleId_example"; // String | 
    String role = "role_example"; // String | 
    String tenantId = "tenantId_example"; // String | 
    String tenant = "tenant_example"; // String | 
    String platformId = "platformId_example"; // String | 
    String platform = "platform_example"; // String | 
    String tag = "tag_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      VirtualizationVirtualMachinesList200Response result = apiInstance.virtualizationVirtualMachinesList(name, cluster, idIn, q, status, clusterGroupId, clusterGroup, clusterTypeId, clusterType, clusterId, regionId, region, siteId, site, roleId, role, tenantId, tenant, platformId, platform, tag, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualizationApi#virtualizationVirtualMachinesList");
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
| **name** | **String**|  | [optional] |
| **cluster** | **String**|  | [optional] |
| **idIn** | **String**| Multiple values may be separated by commas. | [optional] |
| **q** | **String**|  | [optional] |
| **status** | **String**|  | [optional] |
| **clusterGroupId** | **String**|  | [optional] |
| **clusterGroup** | **String**|  | [optional] |
| **clusterTypeId** | **String**|  | [optional] |
| **clusterType** | **String**|  | [optional] |
| **clusterId** | **String**|  | [optional] |
| **regionId** | **BigDecimal**|  | [optional] |
| **region** | **String**|  | [optional] |
| **siteId** | **String**|  | [optional] |
| **site** | **String**|  | [optional] |
| **roleId** | **String**|  | [optional] |
| **role** | **String**|  | [optional] |
| **tenantId** | **String**|  | [optional] |
| **tenant** | **String**|  | [optional] |
| **platformId** | **String**|  | [optional] |
| **platform** | **String**|  | [optional] |
| **tag** | **String**|  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**VirtualizationVirtualMachinesList200Response**](VirtualizationVirtualMachinesList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="virtualizationVirtualMachinesPartialUpdate"></a>
# **virtualizationVirtualMachinesPartialUpdate**
> VirtualMachine virtualizationVirtualMachinesPartialUpdate(id, writableVirtualMachine)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    VirtualizationApi apiInstance = new VirtualizationApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this virtual machine.
    WritableVirtualMachine writableVirtualMachine = new WritableVirtualMachine(); // WritableVirtualMachine | 
    try {
      VirtualMachine result = apiInstance.virtualizationVirtualMachinesPartialUpdate(id, writableVirtualMachine);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualizationApi#virtualizationVirtualMachinesPartialUpdate");
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
| **id** | **Integer**| A unique integer value identifying this virtual machine. | |
| **writableVirtualMachine** | [**WritableVirtualMachine**](WritableVirtualMachine.md)|  | |

### Return type

[**VirtualMachine**](VirtualMachine.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="virtualizationVirtualMachinesRead"></a>
# **virtualizationVirtualMachinesRead**
> VirtualMachineWithConfigContext virtualizationVirtualMachinesRead(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    VirtualizationApi apiInstance = new VirtualizationApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this virtual machine.
    try {
      VirtualMachineWithConfigContext result = apiInstance.virtualizationVirtualMachinesRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualizationApi#virtualizationVirtualMachinesRead");
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
| **id** | **Integer**| A unique integer value identifying this virtual machine. | |

### Return type

[**VirtualMachineWithConfigContext**](VirtualMachineWithConfigContext.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="virtualizationVirtualMachinesUpdate"></a>
# **virtualizationVirtualMachinesUpdate**
> VirtualMachine virtualizationVirtualMachinesUpdate(id, writableVirtualMachine)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    VirtualizationApi apiInstance = new VirtualizationApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this virtual machine.
    WritableVirtualMachine writableVirtualMachine = new WritableVirtualMachine(); // WritableVirtualMachine | 
    try {
      VirtualMachine result = apiInstance.virtualizationVirtualMachinesUpdate(id, writableVirtualMachine);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualizationApi#virtualizationVirtualMachinesUpdate");
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
| **id** | **Integer**| A unique integer value identifying this virtual machine. | |
| **writableVirtualMachine** | [**WritableVirtualMachine**](WritableVirtualMachine.md)|  | |

### Return type

[**VirtualMachine**](VirtualMachine.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

