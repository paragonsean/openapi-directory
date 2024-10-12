# VirtualizationApi

All URIs are relative to *https://netboxdemo.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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
> VirtualizationClusterGroupsList200Response virtualizationClusterGroupsList(id, name, slug, description, q, idN, idLte, idLt, idGte, idGt, nameN, nameIc, nameNic, nameIew, nameNiew, nameIsw, nameNisw, nameIe, nameNie, slugN, slugIc, slugNic, slugIew, slugNiew, slugIsw, slugNisw, slugIe, slugNie, descriptionN, descriptionIc, descriptionNic, descriptionIew, descriptionNiew, descriptionIsw, descriptionNisw, descriptionIe, descriptionNie, limit, offset)



Call to super to allow for caching

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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    VirtualizationApi apiInstance = new VirtualizationApi(defaultClient);
    String id = "id_example"; // String | 
    String name = "name_example"; // String | 
    String slug = "slug_example"; // String | 
    String description = "description_example"; // String | 
    String q = "q_example"; // String | 
    String idN = "idN_example"; // String | 
    String idLte = "idLte_example"; // String | 
    String idLt = "idLt_example"; // String | 
    String idGte = "idGte_example"; // String | 
    String idGt = "idGt_example"; // String | 
    String nameN = "nameN_example"; // String | 
    String nameIc = "nameIc_example"; // String | 
    String nameNic = "nameNic_example"; // String | 
    String nameIew = "nameIew_example"; // String | 
    String nameNiew = "nameNiew_example"; // String | 
    String nameIsw = "nameIsw_example"; // String | 
    String nameNisw = "nameNisw_example"; // String | 
    String nameIe = "nameIe_example"; // String | 
    String nameNie = "nameNie_example"; // String | 
    String slugN = "slugN_example"; // String | 
    String slugIc = "slugIc_example"; // String | 
    String slugNic = "slugNic_example"; // String | 
    String slugIew = "slugIew_example"; // String | 
    String slugNiew = "slugNiew_example"; // String | 
    String slugIsw = "slugIsw_example"; // String | 
    String slugNisw = "slugNisw_example"; // String | 
    String slugIe = "slugIe_example"; // String | 
    String slugNie = "slugNie_example"; // String | 
    String descriptionN = "descriptionN_example"; // String | 
    String descriptionIc = "descriptionIc_example"; // String | 
    String descriptionNic = "descriptionNic_example"; // String | 
    String descriptionIew = "descriptionIew_example"; // String | 
    String descriptionNiew = "descriptionNiew_example"; // String | 
    String descriptionIsw = "descriptionIsw_example"; // String | 
    String descriptionNisw = "descriptionNisw_example"; // String | 
    String descriptionIe = "descriptionIe_example"; // String | 
    String descriptionNie = "descriptionNie_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      VirtualizationClusterGroupsList200Response result = apiInstance.virtualizationClusterGroupsList(id, name, slug, description, q, idN, idLte, idLt, idGte, idGt, nameN, nameIc, nameNic, nameIew, nameNiew, nameIsw, nameNisw, nameIe, nameNie, slugN, slugIc, slugNic, slugIew, slugNiew, slugIsw, slugNisw, slugIe, slugNie, descriptionN, descriptionIc, descriptionNic, descriptionIew, descriptionNiew, descriptionIsw, descriptionNisw, descriptionIe, descriptionNie, limit, offset);
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
| **id** | **String**|  | [optional] |
| **name** | **String**|  | [optional] |
| **slug** | **String**|  | [optional] |
| **description** | **String**|  | [optional] |
| **q** | **String**|  | [optional] |
| **idN** | **String**|  | [optional] |
| **idLte** | **String**|  | [optional] |
| **idLt** | **String**|  | [optional] |
| **idGte** | **String**|  | [optional] |
| **idGt** | **String**|  | [optional] |
| **nameN** | **String**|  | [optional] |
| **nameIc** | **String**|  | [optional] |
| **nameNic** | **String**|  | [optional] |
| **nameIew** | **String**|  | [optional] |
| **nameNiew** | **String**|  | [optional] |
| **nameIsw** | **String**|  | [optional] |
| **nameNisw** | **String**|  | [optional] |
| **nameIe** | **String**|  | [optional] |
| **nameNie** | **String**|  | [optional] |
| **slugN** | **String**|  | [optional] |
| **slugIc** | **String**|  | [optional] |
| **slugNic** | **String**|  | [optional] |
| **slugIew** | **String**|  | [optional] |
| **slugNiew** | **String**|  | [optional] |
| **slugIsw** | **String**|  | [optional] |
| **slugNisw** | **String**|  | [optional] |
| **slugIe** | **String**|  | [optional] |
| **slugNie** | **String**|  | [optional] |
| **descriptionN** | **String**|  | [optional] |
| **descriptionIc** | **String**|  | [optional] |
| **descriptionNic** | **String**|  | [optional] |
| **descriptionIew** | **String**|  | [optional] |
| **descriptionNiew** | **String**|  | [optional] |
| **descriptionIsw** | **String**|  | [optional] |
| **descriptionNisw** | **String**|  | [optional] |
| **descriptionIe** | **String**|  | [optional] |
| **descriptionNie** | **String**|  | [optional] |
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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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



Call to super to allow for caching

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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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
> VirtualizationClusterTypesList200Response virtualizationClusterTypesList(id, name, slug, description, q, idN, idLte, idLt, idGte, idGt, nameN, nameIc, nameNic, nameIew, nameNiew, nameIsw, nameNisw, nameIe, nameNie, slugN, slugIc, slugNic, slugIew, slugNiew, slugIsw, slugNisw, slugIe, slugNie, descriptionN, descriptionIc, descriptionNic, descriptionIew, descriptionNiew, descriptionIsw, descriptionNisw, descriptionIe, descriptionNie, limit, offset)



Call to super to allow for caching

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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    VirtualizationApi apiInstance = new VirtualizationApi(defaultClient);
    String id = "id_example"; // String | 
    String name = "name_example"; // String | 
    String slug = "slug_example"; // String | 
    String description = "description_example"; // String | 
    String q = "q_example"; // String | 
    String idN = "idN_example"; // String | 
    String idLte = "idLte_example"; // String | 
    String idLt = "idLt_example"; // String | 
    String idGte = "idGte_example"; // String | 
    String idGt = "idGt_example"; // String | 
    String nameN = "nameN_example"; // String | 
    String nameIc = "nameIc_example"; // String | 
    String nameNic = "nameNic_example"; // String | 
    String nameIew = "nameIew_example"; // String | 
    String nameNiew = "nameNiew_example"; // String | 
    String nameIsw = "nameIsw_example"; // String | 
    String nameNisw = "nameNisw_example"; // String | 
    String nameIe = "nameIe_example"; // String | 
    String nameNie = "nameNie_example"; // String | 
    String slugN = "slugN_example"; // String | 
    String slugIc = "slugIc_example"; // String | 
    String slugNic = "slugNic_example"; // String | 
    String slugIew = "slugIew_example"; // String | 
    String slugNiew = "slugNiew_example"; // String | 
    String slugIsw = "slugIsw_example"; // String | 
    String slugNisw = "slugNisw_example"; // String | 
    String slugIe = "slugIe_example"; // String | 
    String slugNie = "slugNie_example"; // String | 
    String descriptionN = "descriptionN_example"; // String | 
    String descriptionIc = "descriptionIc_example"; // String | 
    String descriptionNic = "descriptionNic_example"; // String | 
    String descriptionIew = "descriptionIew_example"; // String | 
    String descriptionNiew = "descriptionNiew_example"; // String | 
    String descriptionIsw = "descriptionIsw_example"; // String | 
    String descriptionNisw = "descriptionNisw_example"; // String | 
    String descriptionIe = "descriptionIe_example"; // String | 
    String descriptionNie = "descriptionNie_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      VirtualizationClusterTypesList200Response result = apiInstance.virtualizationClusterTypesList(id, name, slug, description, q, idN, idLte, idLt, idGte, idGt, nameN, nameIc, nameNic, nameIew, nameNiew, nameIsw, nameNisw, nameIe, nameNie, slugN, slugIc, slugNic, slugIew, slugNiew, slugIsw, slugNisw, slugIe, slugNie, descriptionN, descriptionIc, descriptionNic, descriptionIew, descriptionNiew, descriptionIsw, descriptionNisw, descriptionIe, descriptionNie, limit, offset);
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
| **id** | **String**|  | [optional] |
| **name** | **String**|  | [optional] |
| **slug** | **String**|  | [optional] |
| **description** | **String**|  | [optional] |
| **q** | **String**|  | [optional] |
| **idN** | **String**|  | [optional] |
| **idLte** | **String**|  | [optional] |
| **idLt** | **String**|  | [optional] |
| **idGte** | **String**|  | [optional] |
| **idGt** | **String**|  | [optional] |
| **nameN** | **String**|  | [optional] |
| **nameIc** | **String**|  | [optional] |
| **nameNic** | **String**|  | [optional] |
| **nameIew** | **String**|  | [optional] |
| **nameNiew** | **String**|  | [optional] |
| **nameIsw** | **String**|  | [optional] |
| **nameNisw** | **String**|  | [optional] |
| **nameIe** | **String**|  | [optional] |
| **nameNie** | **String**|  | [optional] |
| **slugN** | **String**|  | [optional] |
| **slugIc** | **String**|  | [optional] |
| **slugNic** | **String**|  | [optional] |
| **slugIew** | **String**|  | [optional] |
| **slugNiew** | **String**|  | [optional] |
| **slugIsw** | **String**|  | [optional] |
| **slugNisw** | **String**|  | [optional] |
| **slugIe** | **String**|  | [optional] |
| **slugNie** | **String**|  | [optional] |
| **descriptionN** | **String**|  | [optional] |
| **descriptionIc** | **String**|  | [optional] |
| **descriptionNic** | **String**|  | [optional] |
| **descriptionIew** | **String**|  | [optional] |
| **descriptionNiew** | **String**|  | [optional] |
| **descriptionIsw** | **String**|  | [optional] |
| **descriptionNisw** | **String**|  | [optional] |
| **descriptionIe** | **String**|  | [optional] |
| **descriptionNie** | **String**|  | [optional] |
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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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



Call to super to allow for caching

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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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
> VirtualizationClustersList200Response virtualizationClustersList(id, name, tenantGroupId, tenantGroup, tenantId, tenant, created, createdGte, createdLte, lastUpdated, lastUpdatedGte, lastUpdatedLte, q, regionId, region, siteId, site, groupId, group, typeId, type, tag, idN, idLte, idLt, idGte, idGt, nameN, nameIc, nameNic, nameIew, nameNiew, nameIsw, nameNisw, nameIe, nameNie, tenantGroupIdN, tenantGroupN, tenantIdN, tenantN, regionIdN, regionN, siteIdN, siteN, groupIdN, groupN, typeIdN, typeN, tagN, limit, offset)



Call to super to allow for caching

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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    VirtualizationApi apiInstance = new VirtualizationApi(defaultClient);
    String id = "id_example"; // String | 
    String name = "name_example"; // String | 
    String tenantGroupId = "tenantGroupId_example"; // String | 
    String tenantGroup = "tenantGroup_example"; // String | 
    String tenantId = "tenantId_example"; // String | 
    String tenant = "tenant_example"; // String | 
    String created = "created_example"; // String | 
    String createdGte = "createdGte_example"; // String | 
    String createdLte = "createdLte_example"; // String | 
    String lastUpdated = "lastUpdated_example"; // String | 
    String lastUpdatedGte = "lastUpdatedGte_example"; // String | 
    String lastUpdatedLte = "lastUpdatedLte_example"; // String | 
    String q = "q_example"; // String | 
    String regionId = "regionId_example"; // String | 
    String region = "region_example"; // String | 
    String siteId = "siteId_example"; // String | 
    String site = "site_example"; // String | 
    String groupId = "groupId_example"; // String | 
    String group = "group_example"; // String | 
    String typeId = "typeId_example"; // String | 
    String type = "type_example"; // String | 
    String tag = "tag_example"; // String | 
    String idN = "idN_example"; // String | 
    String idLte = "idLte_example"; // String | 
    String idLt = "idLt_example"; // String | 
    String idGte = "idGte_example"; // String | 
    String idGt = "idGt_example"; // String | 
    String nameN = "nameN_example"; // String | 
    String nameIc = "nameIc_example"; // String | 
    String nameNic = "nameNic_example"; // String | 
    String nameIew = "nameIew_example"; // String | 
    String nameNiew = "nameNiew_example"; // String | 
    String nameIsw = "nameIsw_example"; // String | 
    String nameNisw = "nameNisw_example"; // String | 
    String nameIe = "nameIe_example"; // String | 
    String nameNie = "nameNie_example"; // String | 
    String tenantGroupIdN = "tenantGroupIdN_example"; // String | 
    String tenantGroupN = "tenantGroupN_example"; // String | 
    String tenantIdN = "tenantIdN_example"; // String | 
    String tenantN = "tenantN_example"; // String | 
    String regionIdN = "regionIdN_example"; // String | 
    String regionN = "regionN_example"; // String | 
    String siteIdN = "siteIdN_example"; // String | 
    String siteN = "siteN_example"; // String | 
    String groupIdN = "groupIdN_example"; // String | 
    String groupN = "groupN_example"; // String | 
    String typeIdN = "typeIdN_example"; // String | 
    String typeN = "typeN_example"; // String | 
    String tagN = "tagN_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      VirtualizationClustersList200Response result = apiInstance.virtualizationClustersList(id, name, tenantGroupId, tenantGroup, tenantId, tenant, created, createdGte, createdLte, lastUpdated, lastUpdatedGte, lastUpdatedLte, q, regionId, region, siteId, site, groupId, group, typeId, type, tag, idN, idLte, idLt, idGte, idGt, nameN, nameIc, nameNic, nameIew, nameNiew, nameIsw, nameNisw, nameIe, nameNie, tenantGroupIdN, tenantGroupN, tenantIdN, tenantN, regionIdN, regionN, siteIdN, siteN, groupIdN, groupN, typeIdN, typeN, tagN, limit, offset);
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
| **id** | **String**|  | [optional] |
| **name** | **String**|  | [optional] |
| **tenantGroupId** | **String**|  | [optional] |
| **tenantGroup** | **String**|  | [optional] |
| **tenantId** | **String**|  | [optional] |
| **tenant** | **String**|  | [optional] |
| **created** | **String**|  | [optional] |
| **createdGte** | **String**|  | [optional] |
| **createdLte** | **String**|  | [optional] |
| **lastUpdated** | **String**|  | [optional] |
| **lastUpdatedGte** | **String**|  | [optional] |
| **lastUpdatedLte** | **String**|  | [optional] |
| **q** | **String**|  | [optional] |
| **regionId** | **String**|  | [optional] |
| **region** | **String**|  | [optional] |
| **siteId** | **String**|  | [optional] |
| **site** | **String**|  | [optional] |
| **groupId** | **String**|  | [optional] |
| **group** | **String**|  | [optional] |
| **typeId** | **String**|  | [optional] |
| **type** | **String**|  | [optional] |
| **tag** | **String**|  | [optional] |
| **idN** | **String**|  | [optional] |
| **idLte** | **String**|  | [optional] |
| **idLt** | **String**|  | [optional] |
| **idGte** | **String**|  | [optional] |
| **idGt** | **String**|  | [optional] |
| **nameN** | **String**|  | [optional] |
| **nameIc** | **String**|  | [optional] |
| **nameNic** | **String**|  | [optional] |
| **nameIew** | **String**|  | [optional] |
| **nameNiew** | **String**|  | [optional] |
| **nameIsw** | **String**|  | [optional] |
| **nameNisw** | **String**|  | [optional] |
| **nameIe** | **String**|  | [optional] |
| **nameNie** | **String**|  | [optional] |
| **tenantGroupIdN** | **String**|  | [optional] |
| **tenantGroupN** | **String**|  | [optional] |
| **tenantIdN** | **String**|  | [optional] |
| **tenantN** | **String**|  | [optional] |
| **regionIdN** | **String**|  | [optional] |
| **regionN** | **String**|  | [optional] |
| **siteIdN** | **String**|  | [optional] |
| **siteN** | **String**|  | [optional] |
| **groupIdN** | **String**|  | [optional] |
| **groupN** | **String**|  | [optional] |
| **typeIdN** | **String**|  | [optional] |
| **typeN** | **String**|  | [optional] |
| **tagN** | **String**|  | [optional] |
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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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



Call to super to allow for caching

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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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
> VirtualMachineInterface virtualizationInterfacesCreate(writableVirtualMachineInterface)





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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    VirtualizationApi apiInstance = new VirtualizationApi(defaultClient);
    WritableVirtualMachineInterface writableVirtualMachineInterface = new WritableVirtualMachineInterface(); // WritableVirtualMachineInterface | 
    try {
      VirtualMachineInterface result = apiInstance.virtualizationInterfacesCreate(writableVirtualMachineInterface);
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
| **writableVirtualMachineInterface** | [**WritableVirtualMachineInterface**](WritableVirtualMachineInterface.md)|  | |

### Return type

[**VirtualMachineInterface**](VirtualMachineInterface.md)

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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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
> VirtualizationInterfacesList200Response virtualizationInterfacesList(id, name, enabled, mtu, q, virtualMachineId, virtualMachine, macAddress, idN, idLte, idLt, idGte, idGt, nameN, nameIc, nameNic, nameIew, nameNiew, nameIsw, nameNisw, nameIe, nameNie, mtuN, mtuLte, mtuLt, mtuGte, mtuGt, virtualMachineIdN, virtualMachineN, macAddressN, macAddressIc, macAddressNic, macAddressIew, macAddressNiew, macAddressIsw, macAddressNisw, macAddressIe, macAddressNie, limit, offset)



Call to super to allow for caching

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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    VirtualizationApi apiInstance = new VirtualizationApi(defaultClient);
    String id = "id_example"; // String | 
    String name = "name_example"; // String | 
    String enabled = "enabled_example"; // String | 
    String mtu = "mtu_example"; // String | 
    String q = "q_example"; // String | 
    String virtualMachineId = "virtualMachineId_example"; // String | 
    String virtualMachine = "virtualMachine_example"; // String | 
    String macAddress = "macAddress_example"; // String | 
    String idN = "idN_example"; // String | 
    String idLte = "idLte_example"; // String | 
    String idLt = "idLt_example"; // String | 
    String idGte = "idGte_example"; // String | 
    String idGt = "idGt_example"; // String | 
    String nameN = "nameN_example"; // String | 
    String nameIc = "nameIc_example"; // String | 
    String nameNic = "nameNic_example"; // String | 
    String nameIew = "nameIew_example"; // String | 
    String nameNiew = "nameNiew_example"; // String | 
    String nameIsw = "nameIsw_example"; // String | 
    String nameNisw = "nameNisw_example"; // String | 
    String nameIe = "nameIe_example"; // String | 
    String nameNie = "nameNie_example"; // String | 
    String mtuN = "mtuN_example"; // String | 
    String mtuLte = "mtuLte_example"; // String | 
    String mtuLt = "mtuLt_example"; // String | 
    String mtuGte = "mtuGte_example"; // String | 
    String mtuGt = "mtuGt_example"; // String | 
    String virtualMachineIdN = "virtualMachineIdN_example"; // String | 
    String virtualMachineN = "virtualMachineN_example"; // String | 
    String macAddressN = "macAddressN_example"; // String | 
    String macAddressIc = "macAddressIc_example"; // String | 
    String macAddressNic = "macAddressNic_example"; // String | 
    String macAddressIew = "macAddressIew_example"; // String | 
    String macAddressNiew = "macAddressNiew_example"; // String | 
    String macAddressIsw = "macAddressIsw_example"; // String | 
    String macAddressNisw = "macAddressNisw_example"; // String | 
    String macAddressIe = "macAddressIe_example"; // String | 
    String macAddressNie = "macAddressNie_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      VirtualizationInterfacesList200Response result = apiInstance.virtualizationInterfacesList(id, name, enabled, mtu, q, virtualMachineId, virtualMachine, macAddress, idN, idLte, idLt, idGte, idGt, nameN, nameIc, nameNic, nameIew, nameNiew, nameIsw, nameNisw, nameIe, nameNie, mtuN, mtuLte, mtuLt, mtuGte, mtuGt, virtualMachineIdN, virtualMachineN, macAddressN, macAddressIc, macAddressNic, macAddressIew, macAddressNiew, macAddressIsw, macAddressNisw, macAddressIe, macAddressNie, limit, offset);
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
| **id** | **String**|  | [optional] |
| **name** | **String**|  | [optional] |
| **enabled** | **String**|  | [optional] |
| **mtu** | **String**|  | [optional] |
| **q** | **String**|  | [optional] |
| **virtualMachineId** | **String**|  | [optional] |
| **virtualMachine** | **String**|  | [optional] |
| **macAddress** | **String**|  | [optional] |
| **idN** | **String**|  | [optional] |
| **idLte** | **String**|  | [optional] |
| **idLt** | **String**|  | [optional] |
| **idGte** | **String**|  | [optional] |
| **idGt** | **String**|  | [optional] |
| **nameN** | **String**|  | [optional] |
| **nameIc** | **String**|  | [optional] |
| **nameNic** | **String**|  | [optional] |
| **nameIew** | **String**|  | [optional] |
| **nameNiew** | **String**|  | [optional] |
| **nameIsw** | **String**|  | [optional] |
| **nameNisw** | **String**|  | [optional] |
| **nameIe** | **String**|  | [optional] |
| **nameNie** | **String**|  | [optional] |
| **mtuN** | **String**|  | [optional] |
| **mtuLte** | **String**|  | [optional] |
| **mtuLt** | **String**|  | [optional] |
| **mtuGte** | **String**|  | [optional] |
| **mtuGt** | **String**|  | [optional] |
| **virtualMachineIdN** | **String**|  | [optional] |
| **virtualMachineN** | **String**|  | [optional] |
| **macAddressN** | **String**|  | [optional] |
| **macAddressIc** | **String**|  | [optional] |
| **macAddressNic** | **String**|  | [optional] |
| **macAddressIew** | **String**|  | [optional] |
| **macAddressNiew** | **String**|  | [optional] |
| **macAddressIsw** | **String**|  | [optional] |
| **macAddressNisw** | **String**|  | [optional] |
| **macAddressIe** | **String**|  | [optional] |
| **macAddressNie** | **String**|  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**VirtualizationInterfacesList200Response**](VirtualizationInterfacesList200Response.md)

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
> VirtualMachineInterface virtualizationInterfacesPartialUpdate(id, writableVirtualMachineInterface)





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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    VirtualizationApi apiInstance = new VirtualizationApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this interface.
    WritableVirtualMachineInterface writableVirtualMachineInterface = new WritableVirtualMachineInterface(); // WritableVirtualMachineInterface | 
    try {
      VirtualMachineInterface result = apiInstance.virtualizationInterfacesPartialUpdate(id, writableVirtualMachineInterface);
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
| **writableVirtualMachineInterface** | [**WritableVirtualMachineInterface**](WritableVirtualMachineInterface.md)|  | |

### Return type

[**VirtualMachineInterface**](VirtualMachineInterface.md)

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
> VirtualMachineInterface virtualizationInterfacesRead(id)



Call to super to allow for caching

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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    VirtualizationApi apiInstance = new VirtualizationApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this interface.
    try {
      VirtualMachineInterface result = apiInstance.virtualizationInterfacesRead(id);
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

[**VirtualMachineInterface**](VirtualMachineInterface.md)

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
> VirtualMachineInterface virtualizationInterfacesUpdate(id, writableVirtualMachineInterface)





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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    VirtualizationApi apiInstance = new VirtualizationApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this interface.
    WritableVirtualMachineInterface writableVirtualMachineInterface = new WritableVirtualMachineInterface(); // WritableVirtualMachineInterface | 
    try {
      VirtualMachineInterface result = apiInstance.virtualizationInterfacesUpdate(id, writableVirtualMachineInterface);
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
| **writableVirtualMachineInterface** | [**WritableVirtualMachineInterface**](WritableVirtualMachineInterface.md)|  | |

### Return type

[**VirtualMachineInterface**](VirtualMachineInterface.md)

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
> VirtualMachineWithConfigContext virtualizationVirtualMachinesCreate(writableVirtualMachineWithConfigContext)





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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    VirtualizationApi apiInstance = new VirtualizationApi(defaultClient);
    WritableVirtualMachineWithConfigContext writableVirtualMachineWithConfigContext = new WritableVirtualMachineWithConfigContext(); // WritableVirtualMachineWithConfigContext | 
    try {
      VirtualMachineWithConfigContext result = apiInstance.virtualizationVirtualMachinesCreate(writableVirtualMachineWithConfigContext);
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
| **writableVirtualMachineWithConfigContext** | [**WritableVirtualMachineWithConfigContext**](WritableVirtualMachineWithConfigContext.md)|  | |

### Return type

[**VirtualMachineWithConfigContext**](VirtualMachineWithConfigContext.md)

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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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
> VirtualizationVirtualMachinesList200Response virtualizationVirtualMachinesList(id, name, cluster, vcpus, memory, disk, localContextData, tenantGroupId, tenantGroup, tenantId, tenant, created, createdGte, createdLte, lastUpdated, lastUpdatedGte, lastUpdatedLte, q, status, clusterGroupId, clusterGroup, clusterTypeId, clusterType, clusterId, regionId, region, siteId, site, roleId, role, platformId, platform, macAddress, tag, idN, idLte, idLt, idGte, idGt, nameN, nameIc, nameNic, nameIew, nameNiew, nameIsw, nameNisw, nameIe, nameNie, clusterN, vcpusN, vcpusLte, vcpusLt, vcpusGte, vcpusGt, memoryN, memoryLte, memoryLt, memoryGte, memoryGt, diskN, diskLte, diskLt, diskGte, diskGt, tenantGroupIdN, tenantGroupN, tenantIdN, tenantN, statusN, clusterGroupIdN, clusterGroupN, clusterTypeIdN, clusterTypeN, clusterIdN, regionIdN, regionN, siteIdN, siteN, roleIdN, roleN, platformIdN, platformN, macAddressN, macAddressIc, macAddressNic, macAddressIew, macAddressNiew, macAddressIsw, macAddressNisw, macAddressIe, macAddressNie, tagN, limit, offset)



Call to super to allow for caching

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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    VirtualizationApi apiInstance = new VirtualizationApi(defaultClient);
    String id = "id_example"; // String | 
    String name = "name_example"; // String | 
    String cluster = "cluster_example"; // String | 
    String vcpus = "vcpus_example"; // String | 
    String memory = "memory_example"; // String | 
    String disk = "disk_example"; // String | 
    String localContextData = "localContextData_example"; // String | 
    String tenantGroupId = "tenantGroupId_example"; // String | 
    String tenantGroup = "tenantGroup_example"; // String | 
    String tenantId = "tenantId_example"; // String | 
    String tenant = "tenant_example"; // String | 
    String created = "created_example"; // String | 
    String createdGte = "createdGte_example"; // String | 
    String createdLte = "createdLte_example"; // String | 
    String lastUpdated = "lastUpdated_example"; // String | 
    String lastUpdatedGte = "lastUpdatedGte_example"; // String | 
    String lastUpdatedLte = "lastUpdatedLte_example"; // String | 
    String q = "q_example"; // String | 
    String status = "status_example"; // String | 
    String clusterGroupId = "clusterGroupId_example"; // String | 
    String clusterGroup = "clusterGroup_example"; // String | 
    String clusterTypeId = "clusterTypeId_example"; // String | 
    String clusterType = "clusterType_example"; // String | 
    String clusterId = "clusterId_example"; // String | 
    String regionId = "regionId_example"; // String | 
    String region = "region_example"; // String | 
    String siteId = "siteId_example"; // String | 
    String site = "site_example"; // String | 
    String roleId = "roleId_example"; // String | 
    String role = "role_example"; // String | 
    String platformId = "platformId_example"; // String | 
    String platform = "platform_example"; // String | 
    String macAddress = "macAddress_example"; // String | 
    String tag = "tag_example"; // String | 
    String idN = "idN_example"; // String | 
    String idLte = "idLte_example"; // String | 
    String idLt = "idLt_example"; // String | 
    String idGte = "idGte_example"; // String | 
    String idGt = "idGt_example"; // String | 
    String nameN = "nameN_example"; // String | 
    String nameIc = "nameIc_example"; // String | 
    String nameNic = "nameNic_example"; // String | 
    String nameIew = "nameIew_example"; // String | 
    String nameNiew = "nameNiew_example"; // String | 
    String nameIsw = "nameIsw_example"; // String | 
    String nameNisw = "nameNisw_example"; // String | 
    String nameIe = "nameIe_example"; // String | 
    String nameNie = "nameNie_example"; // String | 
    String clusterN = "clusterN_example"; // String | 
    String vcpusN = "vcpusN_example"; // String | 
    String vcpusLte = "vcpusLte_example"; // String | 
    String vcpusLt = "vcpusLt_example"; // String | 
    String vcpusGte = "vcpusGte_example"; // String | 
    String vcpusGt = "vcpusGt_example"; // String | 
    String memoryN = "memoryN_example"; // String | 
    String memoryLte = "memoryLte_example"; // String | 
    String memoryLt = "memoryLt_example"; // String | 
    String memoryGte = "memoryGte_example"; // String | 
    String memoryGt = "memoryGt_example"; // String | 
    String diskN = "diskN_example"; // String | 
    String diskLte = "diskLte_example"; // String | 
    String diskLt = "diskLt_example"; // String | 
    String diskGte = "diskGte_example"; // String | 
    String diskGt = "diskGt_example"; // String | 
    String tenantGroupIdN = "tenantGroupIdN_example"; // String | 
    String tenantGroupN = "tenantGroupN_example"; // String | 
    String tenantIdN = "tenantIdN_example"; // String | 
    String tenantN = "tenantN_example"; // String | 
    String statusN = "statusN_example"; // String | 
    String clusterGroupIdN = "clusterGroupIdN_example"; // String | 
    String clusterGroupN = "clusterGroupN_example"; // String | 
    String clusterTypeIdN = "clusterTypeIdN_example"; // String | 
    String clusterTypeN = "clusterTypeN_example"; // String | 
    String clusterIdN = "clusterIdN_example"; // String | 
    String regionIdN = "regionIdN_example"; // String | 
    String regionN = "regionN_example"; // String | 
    String siteIdN = "siteIdN_example"; // String | 
    String siteN = "siteN_example"; // String | 
    String roleIdN = "roleIdN_example"; // String | 
    String roleN = "roleN_example"; // String | 
    String platformIdN = "platformIdN_example"; // String | 
    String platformN = "platformN_example"; // String | 
    String macAddressN = "macAddressN_example"; // String | 
    String macAddressIc = "macAddressIc_example"; // String | 
    String macAddressNic = "macAddressNic_example"; // String | 
    String macAddressIew = "macAddressIew_example"; // String | 
    String macAddressNiew = "macAddressNiew_example"; // String | 
    String macAddressIsw = "macAddressIsw_example"; // String | 
    String macAddressNisw = "macAddressNisw_example"; // String | 
    String macAddressIe = "macAddressIe_example"; // String | 
    String macAddressNie = "macAddressNie_example"; // String | 
    String tagN = "tagN_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      VirtualizationVirtualMachinesList200Response result = apiInstance.virtualizationVirtualMachinesList(id, name, cluster, vcpus, memory, disk, localContextData, tenantGroupId, tenantGroup, tenantId, tenant, created, createdGte, createdLte, lastUpdated, lastUpdatedGte, lastUpdatedLte, q, status, clusterGroupId, clusterGroup, clusterTypeId, clusterType, clusterId, regionId, region, siteId, site, roleId, role, platformId, platform, macAddress, tag, idN, idLte, idLt, idGte, idGt, nameN, nameIc, nameNic, nameIew, nameNiew, nameIsw, nameNisw, nameIe, nameNie, clusterN, vcpusN, vcpusLte, vcpusLt, vcpusGte, vcpusGt, memoryN, memoryLte, memoryLt, memoryGte, memoryGt, diskN, diskLte, diskLt, diskGte, diskGt, tenantGroupIdN, tenantGroupN, tenantIdN, tenantN, statusN, clusterGroupIdN, clusterGroupN, clusterTypeIdN, clusterTypeN, clusterIdN, regionIdN, regionN, siteIdN, siteN, roleIdN, roleN, platformIdN, platformN, macAddressN, macAddressIc, macAddressNic, macAddressIew, macAddressNiew, macAddressIsw, macAddressNisw, macAddressIe, macAddressNie, tagN, limit, offset);
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
| **id** | **String**|  | [optional] |
| **name** | **String**|  | [optional] |
| **cluster** | **String**|  | [optional] |
| **vcpus** | **String**|  | [optional] |
| **memory** | **String**|  | [optional] |
| **disk** | **String**|  | [optional] |
| **localContextData** | **String**|  | [optional] |
| **tenantGroupId** | **String**|  | [optional] |
| **tenantGroup** | **String**|  | [optional] |
| **tenantId** | **String**|  | [optional] |
| **tenant** | **String**|  | [optional] |
| **created** | **String**|  | [optional] |
| **createdGte** | **String**|  | [optional] |
| **createdLte** | **String**|  | [optional] |
| **lastUpdated** | **String**|  | [optional] |
| **lastUpdatedGte** | **String**|  | [optional] |
| **lastUpdatedLte** | **String**|  | [optional] |
| **q** | **String**|  | [optional] |
| **status** | **String**|  | [optional] |
| **clusterGroupId** | **String**|  | [optional] |
| **clusterGroup** | **String**|  | [optional] |
| **clusterTypeId** | **String**|  | [optional] |
| **clusterType** | **String**|  | [optional] |
| **clusterId** | **String**|  | [optional] |
| **regionId** | **String**|  | [optional] |
| **region** | **String**|  | [optional] |
| **siteId** | **String**|  | [optional] |
| **site** | **String**|  | [optional] |
| **roleId** | **String**|  | [optional] |
| **role** | **String**|  | [optional] |
| **platformId** | **String**|  | [optional] |
| **platform** | **String**|  | [optional] |
| **macAddress** | **String**|  | [optional] |
| **tag** | **String**|  | [optional] |
| **idN** | **String**|  | [optional] |
| **idLte** | **String**|  | [optional] |
| **idLt** | **String**|  | [optional] |
| **idGte** | **String**|  | [optional] |
| **idGt** | **String**|  | [optional] |
| **nameN** | **String**|  | [optional] |
| **nameIc** | **String**|  | [optional] |
| **nameNic** | **String**|  | [optional] |
| **nameIew** | **String**|  | [optional] |
| **nameNiew** | **String**|  | [optional] |
| **nameIsw** | **String**|  | [optional] |
| **nameNisw** | **String**|  | [optional] |
| **nameIe** | **String**|  | [optional] |
| **nameNie** | **String**|  | [optional] |
| **clusterN** | **String**|  | [optional] |
| **vcpusN** | **String**|  | [optional] |
| **vcpusLte** | **String**|  | [optional] |
| **vcpusLt** | **String**|  | [optional] |
| **vcpusGte** | **String**|  | [optional] |
| **vcpusGt** | **String**|  | [optional] |
| **memoryN** | **String**|  | [optional] |
| **memoryLte** | **String**|  | [optional] |
| **memoryLt** | **String**|  | [optional] |
| **memoryGte** | **String**|  | [optional] |
| **memoryGt** | **String**|  | [optional] |
| **diskN** | **String**|  | [optional] |
| **diskLte** | **String**|  | [optional] |
| **diskLt** | **String**|  | [optional] |
| **diskGte** | **String**|  | [optional] |
| **diskGt** | **String**|  | [optional] |
| **tenantGroupIdN** | **String**|  | [optional] |
| **tenantGroupN** | **String**|  | [optional] |
| **tenantIdN** | **String**|  | [optional] |
| **tenantN** | **String**|  | [optional] |
| **statusN** | **String**|  | [optional] |
| **clusterGroupIdN** | **String**|  | [optional] |
| **clusterGroupN** | **String**|  | [optional] |
| **clusterTypeIdN** | **String**|  | [optional] |
| **clusterTypeN** | **String**|  | [optional] |
| **clusterIdN** | **String**|  | [optional] |
| **regionIdN** | **String**|  | [optional] |
| **regionN** | **String**|  | [optional] |
| **siteIdN** | **String**|  | [optional] |
| **siteN** | **String**|  | [optional] |
| **roleIdN** | **String**|  | [optional] |
| **roleN** | **String**|  | [optional] |
| **platformIdN** | **String**|  | [optional] |
| **platformN** | **String**|  | [optional] |
| **macAddressN** | **String**|  | [optional] |
| **macAddressIc** | **String**|  | [optional] |
| **macAddressNic** | **String**|  | [optional] |
| **macAddressIew** | **String**|  | [optional] |
| **macAddressNiew** | **String**|  | [optional] |
| **macAddressIsw** | **String**|  | [optional] |
| **macAddressNisw** | **String**|  | [optional] |
| **macAddressIe** | **String**|  | [optional] |
| **macAddressNie** | **String**|  | [optional] |
| **tagN** | **String**|  | [optional] |
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
> VirtualMachineWithConfigContext virtualizationVirtualMachinesPartialUpdate(id, writableVirtualMachineWithConfigContext)





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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    VirtualizationApi apiInstance = new VirtualizationApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this virtual machine.
    WritableVirtualMachineWithConfigContext writableVirtualMachineWithConfigContext = new WritableVirtualMachineWithConfigContext(); // WritableVirtualMachineWithConfigContext | 
    try {
      VirtualMachineWithConfigContext result = apiInstance.virtualizationVirtualMachinesPartialUpdate(id, writableVirtualMachineWithConfigContext);
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
| **writableVirtualMachineWithConfigContext** | [**WritableVirtualMachineWithConfigContext**](WritableVirtualMachineWithConfigContext.md)|  | |

### Return type

[**VirtualMachineWithConfigContext**](VirtualMachineWithConfigContext.md)

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



Call to super to allow for caching

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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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
> VirtualMachineWithConfigContext virtualizationVirtualMachinesUpdate(id, writableVirtualMachineWithConfigContext)





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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    VirtualizationApi apiInstance = new VirtualizationApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this virtual machine.
    WritableVirtualMachineWithConfigContext writableVirtualMachineWithConfigContext = new WritableVirtualMachineWithConfigContext(); // WritableVirtualMachineWithConfigContext | 
    try {
      VirtualMachineWithConfigContext result = apiInstance.virtualizationVirtualMachinesUpdate(id, writableVirtualMachineWithConfigContext);
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
| **writableVirtualMachineWithConfigContext** | [**WritableVirtualMachineWithConfigContext**](WritableVirtualMachineWithConfigContext.md)|  | |

### Return type

[**VirtualMachineWithConfigContext**](VirtualMachineWithConfigContext.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

