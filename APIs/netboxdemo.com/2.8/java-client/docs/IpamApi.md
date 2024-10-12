# IpamApi

All URIs are relative to *https://netboxdemo.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**ipamAggregatesCreate**](IpamApi.md#ipamAggregatesCreate) | **POST** /ipam/aggregates/ |  |
| [**ipamAggregatesDelete**](IpamApi.md#ipamAggregatesDelete) | **DELETE** /ipam/aggregates/{id}/ |  |
| [**ipamAggregatesList**](IpamApi.md#ipamAggregatesList) | **GET** /ipam/aggregates/ |  |
| [**ipamAggregatesPartialUpdate**](IpamApi.md#ipamAggregatesPartialUpdate) | **PATCH** /ipam/aggregates/{id}/ |  |
| [**ipamAggregatesRead**](IpamApi.md#ipamAggregatesRead) | **GET** /ipam/aggregates/{id}/ |  |
| [**ipamAggregatesUpdate**](IpamApi.md#ipamAggregatesUpdate) | **PUT** /ipam/aggregates/{id}/ |  |
| [**ipamIpAddressesCreate**](IpamApi.md#ipamIpAddressesCreate) | **POST** /ipam/ip-addresses/ |  |
| [**ipamIpAddressesDelete**](IpamApi.md#ipamIpAddressesDelete) | **DELETE** /ipam/ip-addresses/{id}/ |  |
| [**ipamIpAddressesList**](IpamApi.md#ipamIpAddressesList) | **GET** /ipam/ip-addresses/ |  |
| [**ipamIpAddressesPartialUpdate**](IpamApi.md#ipamIpAddressesPartialUpdate) | **PATCH** /ipam/ip-addresses/{id}/ |  |
| [**ipamIpAddressesRead**](IpamApi.md#ipamIpAddressesRead) | **GET** /ipam/ip-addresses/{id}/ |  |
| [**ipamIpAddressesUpdate**](IpamApi.md#ipamIpAddressesUpdate) | **PUT** /ipam/ip-addresses/{id}/ |  |
| [**ipamPrefixesAvailableIpsCreate**](IpamApi.md#ipamPrefixesAvailableIpsCreate) | **POST** /ipam/prefixes/{id}/available-ips/ |  |
| [**ipamPrefixesAvailableIpsRead**](IpamApi.md#ipamPrefixesAvailableIpsRead) | **GET** /ipam/prefixes/{id}/available-ips/ |  |
| [**ipamPrefixesAvailablePrefixesCreate**](IpamApi.md#ipamPrefixesAvailablePrefixesCreate) | **POST** /ipam/prefixes/{id}/available-prefixes/ | A convenience method for returning available child prefixes within a parent. |
| [**ipamPrefixesAvailablePrefixesRead**](IpamApi.md#ipamPrefixesAvailablePrefixesRead) | **GET** /ipam/prefixes/{id}/available-prefixes/ | A convenience method for returning available child prefixes within a parent. |
| [**ipamPrefixesCreate**](IpamApi.md#ipamPrefixesCreate) | **POST** /ipam/prefixes/ |  |
| [**ipamPrefixesDelete**](IpamApi.md#ipamPrefixesDelete) | **DELETE** /ipam/prefixes/{id}/ |  |
| [**ipamPrefixesList**](IpamApi.md#ipamPrefixesList) | **GET** /ipam/prefixes/ |  |
| [**ipamPrefixesPartialUpdate**](IpamApi.md#ipamPrefixesPartialUpdate) | **PATCH** /ipam/prefixes/{id}/ |  |
| [**ipamPrefixesRead**](IpamApi.md#ipamPrefixesRead) | **GET** /ipam/prefixes/{id}/ |  |
| [**ipamPrefixesUpdate**](IpamApi.md#ipamPrefixesUpdate) | **PUT** /ipam/prefixes/{id}/ |  |
| [**ipamRirsCreate**](IpamApi.md#ipamRirsCreate) | **POST** /ipam/rirs/ |  |
| [**ipamRirsDelete**](IpamApi.md#ipamRirsDelete) | **DELETE** /ipam/rirs/{id}/ |  |
| [**ipamRirsList**](IpamApi.md#ipamRirsList) | **GET** /ipam/rirs/ |  |
| [**ipamRirsPartialUpdate**](IpamApi.md#ipamRirsPartialUpdate) | **PATCH** /ipam/rirs/{id}/ |  |
| [**ipamRirsRead**](IpamApi.md#ipamRirsRead) | **GET** /ipam/rirs/{id}/ |  |
| [**ipamRirsUpdate**](IpamApi.md#ipamRirsUpdate) | **PUT** /ipam/rirs/{id}/ |  |
| [**ipamRolesCreate**](IpamApi.md#ipamRolesCreate) | **POST** /ipam/roles/ |  |
| [**ipamRolesDelete**](IpamApi.md#ipamRolesDelete) | **DELETE** /ipam/roles/{id}/ |  |
| [**ipamRolesList**](IpamApi.md#ipamRolesList) | **GET** /ipam/roles/ |  |
| [**ipamRolesPartialUpdate**](IpamApi.md#ipamRolesPartialUpdate) | **PATCH** /ipam/roles/{id}/ |  |
| [**ipamRolesRead**](IpamApi.md#ipamRolesRead) | **GET** /ipam/roles/{id}/ |  |
| [**ipamRolesUpdate**](IpamApi.md#ipamRolesUpdate) | **PUT** /ipam/roles/{id}/ |  |
| [**ipamServicesCreate**](IpamApi.md#ipamServicesCreate) | **POST** /ipam/services/ |  |
| [**ipamServicesDelete**](IpamApi.md#ipamServicesDelete) | **DELETE** /ipam/services/{id}/ |  |
| [**ipamServicesList**](IpamApi.md#ipamServicesList) | **GET** /ipam/services/ |  |
| [**ipamServicesPartialUpdate**](IpamApi.md#ipamServicesPartialUpdate) | **PATCH** /ipam/services/{id}/ |  |
| [**ipamServicesRead**](IpamApi.md#ipamServicesRead) | **GET** /ipam/services/{id}/ |  |
| [**ipamServicesUpdate**](IpamApi.md#ipamServicesUpdate) | **PUT** /ipam/services/{id}/ |  |
| [**ipamVlanGroupsCreate**](IpamApi.md#ipamVlanGroupsCreate) | **POST** /ipam/vlan-groups/ |  |
| [**ipamVlanGroupsDelete**](IpamApi.md#ipamVlanGroupsDelete) | **DELETE** /ipam/vlan-groups/{id}/ |  |
| [**ipamVlanGroupsList**](IpamApi.md#ipamVlanGroupsList) | **GET** /ipam/vlan-groups/ |  |
| [**ipamVlanGroupsPartialUpdate**](IpamApi.md#ipamVlanGroupsPartialUpdate) | **PATCH** /ipam/vlan-groups/{id}/ |  |
| [**ipamVlanGroupsRead**](IpamApi.md#ipamVlanGroupsRead) | **GET** /ipam/vlan-groups/{id}/ |  |
| [**ipamVlanGroupsUpdate**](IpamApi.md#ipamVlanGroupsUpdate) | **PUT** /ipam/vlan-groups/{id}/ |  |
| [**ipamVlansCreate**](IpamApi.md#ipamVlansCreate) | **POST** /ipam/vlans/ |  |
| [**ipamVlansDelete**](IpamApi.md#ipamVlansDelete) | **DELETE** /ipam/vlans/{id}/ |  |
| [**ipamVlansList**](IpamApi.md#ipamVlansList) | **GET** /ipam/vlans/ |  |
| [**ipamVlansPartialUpdate**](IpamApi.md#ipamVlansPartialUpdate) | **PATCH** /ipam/vlans/{id}/ |  |
| [**ipamVlansRead**](IpamApi.md#ipamVlansRead) | **GET** /ipam/vlans/{id}/ |  |
| [**ipamVlansUpdate**](IpamApi.md#ipamVlansUpdate) | **PUT** /ipam/vlans/{id}/ |  |
| [**ipamVrfsCreate**](IpamApi.md#ipamVrfsCreate) | **POST** /ipam/vrfs/ |  |
| [**ipamVrfsDelete**](IpamApi.md#ipamVrfsDelete) | **DELETE** /ipam/vrfs/{id}/ |  |
| [**ipamVrfsList**](IpamApi.md#ipamVrfsList) | **GET** /ipam/vrfs/ |  |
| [**ipamVrfsPartialUpdate**](IpamApi.md#ipamVrfsPartialUpdate) | **PATCH** /ipam/vrfs/{id}/ |  |
| [**ipamVrfsRead**](IpamApi.md#ipamVrfsRead) | **GET** /ipam/vrfs/{id}/ |  |
| [**ipamVrfsUpdate**](IpamApi.md#ipamVrfsUpdate) | **PUT** /ipam/vrfs/{id}/ |  |


<a id="ipamAggregatesCreate"></a>
# **ipamAggregatesCreate**
> Aggregate ipamAggregatesCreate(writableAggregate)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    WritableAggregate writableAggregate = new WritableAggregate(); // WritableAggregate | 
    try {
      Aggregate result = apiInstance.ipamAggregatesCreate(writableAggregate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamAggregatesCreate");
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
| **writableAggregate** | [**WritableAggregate**](WritableAggregate.md)|  | |

### Return type

[**Aggregate**](Aggregate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="ipamAggregatesDelete"></a>
# **ipamAggregatesDelete**
> ipamAggregatesDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this aggregate.
    try {
      apiInstance.ipamAggregatesDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamAggregatesDelete");
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
| **id** | **Integer**| A unique integer value identifying this aggregate. | |

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

<a id="ipamAggregatesList"></a>
# **ipamAggregatesList**
> IpamAggregatesList200Response ipamAggregatesList(id, dateAdded, created, createdGte, createdLte, lastUpdated, lastUpdatedGte, lastUpdatedLte, q, family, prefix, rirId, rir, tag, idN, idLte, idLt, idGte, idGt, dateAddedN, dateAddedLte, dateAddedLt, dateAddedGte, dateAddedGt, rirIdN, rirN, tagN, limit, offset)



Call to super to allow for caching

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    String id = "id_example"; // String | 
    String dateAdded = "dateAdded_example"; // String | 
    String created = "created_example"; // String | 
    String createdGte = "createdGte_example"; // String | 
    String createdLte = "createdLte_example"; // String | 
    String lastUpdated = "lastUpdated_example"; // String | 
    String lastUpdatedGte = "lastUpdatedGte_example"; // String | 
    String lastUpdatedLte = "lastUpdatedLte_example"; // String | 
    String q = "q_example"; // String | 
    BigDecimal family = new BigDecimal(78); // BigDecimal | 
    String prefix = "prefix_example"; // String | 
    String rirId = "rirId_example"; // String | 
    String rir = "rir_example"; // String | 
    String tag = "tag_example"; // String | 
    String idN = "idN_example"; // String | 
    String idLte = "idLte_example"; // String | 
    String idLt = "idLt_example"; // String | 
    String idGte = "idGte_example"; // String | 
    String idGt = "idGt_example"; // String | 
    String dateAddedN = "dateAddedN_example"; // String | 
    String dateAddedLte = "dateAddedLte_example"; // String | 
    String dateAddedLt = "dateAddedLt_example"; // String | 
    String dateAddedGte = "dateAddedGte_example"; // String | 
    String dateAddedGt = "dateAddedGt_example"; // String | 
    String rirIdN = "rirIdN_example"; // String | 
    String rirN = "rirN_example"; // String | 
    String tagN = "tagN_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      IpamAggregatesList200Response result = apiInstance.ipamAggregatesList(id, dateAdded, created, createdGte, createdLte, lastUpdated, lastUpdatedGte, lastUpdatedLte, q, family, prefix, rirId, rir, tag, idN, idLte, idLt, idGte, idGt, dateAddedN, dateAddedLte, dateAddedLt, dateAddedGte, dateAddedGt, rirIdN, rirN, tagN, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamAggregatesList");
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
| **dateAdded** | **String**|  | [optional] |
| **created** | **String**|  | [optional] |
| **createdGte** | **String**|  | [optional] |
| **createdLte** | **String**|  | [optional] |
| **lastUpdated** | **String**|  | [optional] |
| **lastUpdatedGte** | **String**|  | [optional] |
| **lastUpdatedLte** | **String**|  | [optional] |
| **q** | **String**|  | [optional] |
| **family** | **BigDecimal**|  | [optional] |
| **prefix** | **String**|  | [optional] |
| **rirId** | **String**|  | [optional] |
| **rir** | **String**|  | [optional] |
| **tag** | **String**|  | [optional] |
| **idN** | **String**|  | [optional] |
| **idLte** | **String**|  | [optional] |
| **idLt** | **String**|  | [optional] |
| **idGte** | **String**|  | [optional] |
| **idGt** | **String**|  | [optional] |
| **dateAddedN** | **String**|  | [optional] |
| **dateAddedLte** | **String**|  | [optional] |
| **dateAddedLt** | **String**|  | [optional] |
| **dateAddedGte** | **String**|  | [optional] |
| **dateAddedGt** | **String**|  | [optional] |
| **rirIdN** | **String**|  | [optional] |
| **rirN** | **String**|  | [optional] |
| **tagN** | **String**|  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**IpamAggregatesList200Response**](IpamAggregatesList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="ipamAggregatesPartialUpdate"></a>
# **ipamAggregatesPartialUpdate**
> Aggregate ipamAggregatesPartialUpdate(id, writableAggregate)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this aggregate.
    WritableAggregate writableAggregate = new WritableAggregate(); // WritableAggregate | 
    try {
      Aggregate result = apiInstance.ipamAggregatesPartialUpdate(id, writableAggregate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamAggregatesPartialUpdate");
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
| **id** | **Integer**| A unique integer value identifying this aggregate. | |
| **writableAggregate** | [**WritableAggregate**](WritableAggregate.md)|  | |

### Return type

[**Aggregate**](Aggregate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="ipamAggregatesRead"></a>
# **ipamAggregatesRead**
> Aggregate ipamAggregatesRead(id)



Call to super to allow for caching

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this aggregate.
    try {
      Aggregate result = apiInstance.ipamAggregatesRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamAggregatesRead");
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
| **id** | **Integer**| A unique integer value identifying this aggregate. | |

### Return type

[**Aggregate**](Aggregate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="ipamAggregatesUpdate"></a>
# **ipamAggregatesUpdate**
> Aggregate ipamAggregatesUpdate(id, writableAggregate)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this aggregate.
    WritableAggregate writableAggregate = new WritableAggregate(); // WritableAggregate | 
    try {
      Aggregate result = apiInstance.ipamAggregatesUpdate(id, writableAggregate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamAggregatesUpdate");
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
| **id** | **Integer**| A unique integer value identifying this aggregate. | |
| **writableAggregate** | [**WritableAggregate**](WritableAggregate.md)|  | |

### Return type

[**Aggregate**](Aggregate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="ipamIpAddressesCreate"></a>
# **ipamIpAddressesCreate**
> IPAddress ipamIpAddressesCreate(writableIPAddress)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    WritableIPAddress writableIPAddress = new WritableIPAddress(); // WritableIPAddress | 
    try {
      IPAddress result = apiInstance.ipamIpAddressesCreate(writableIPAddress);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamIpAddressesCreate");
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
| **writableIPAddress** | [**WritableIPAddress**](WritableIPAddress.md)|  | |

### Return type

[**IPAddress**](IPAddress.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="ipamIpAddressesDelete"></a>
# **ipamIpAddressesDelete**
> ipamIpAddressesDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this IP address.
    try {
      apiInstance.ipamIpAddressesDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamIpAddressesDelete");
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
| **id** | **Integer**| A unique integer value identifying this IP address. | |

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

<a id="ipamIpAddressesList"></a>
# **ipamIpAddressesList**
> IpamIpAddressesList200Response ipamIpAddressesList(id, dnsName, tenantGroupId, tenantGroup, tenantId, tenant, created, createdGte, createdLte, lastUpdated, lastUpdatedGte, lastUpdatedLte, q, family, parent, address, maskLength, vrfId, vrf, device, deviceId, virtualMachineId, virtualMachine, _interface, interfaceId, assignedToInterface, status, role, tag, idN, idLte, idLt, idGte, idGt, dnsNameN, dnsNameIc, dnsNameNic, dnsNameIew, dnsNameNiew, dnsNameIsw, dnsNameNisw, dnsNameIe, dnsNameNie, tenantGroupIdN, tenantGroupN, tenantIdN, tenantN, vrfIdN, vrfN, virtualMachineIdN, virtualMachineN, interfaceN, interfaceIdN, statusN, roleN, tagN, limit, offset)



Call to super to allow for caching

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    String id = "id_example"; // String | 
    String dnsName = "dnsName_example"; // String | 
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
    BigDecimal family = new BigDecimal(78); // BigDecimal | 
    String parent = "parent_example"; // String | 
    String address = "address_example"; // String | 
    BigDecimal maskLength = new BigDecimal(78); // BigDecimal | 
    String vrfId = "vrfId_example"; // String | 
    String vrf = "vrf_example"; // String | 
    String device = "device_example"; // String | 
    String deviceId = "deviceId_example"; // String | 
    String virtualMachineId = "virtualMachineId_example"; // String | 
    String virtualMachine = "virtualMachine_example"; // String | 
    String _interface = "_interface_example"; // String | 
    String interfaceId = "interfaceId_example"; // String | 
    String assignedToInterface = "assignedToInterface_example"; // String | 
    String status = "status_example"; // String | 
    String role = "role_example"; // String | 
    String tag = "tag_example"; // String | 
    String idN = "idN_example"; // String | 
    String idLte = "idLte_example"; // String | 
    String idLt = "idLt_example"; // String | 
    String idGte = "idGte_example"; // String | 
    String idGt = "idGt_example"; // String | 
    String dnsNameN = "dnsNameN_example"; // String | 
    String dnsNameIc = "dnsNameIc_example"; // String | 
    String dnsNameNic = "dnsNameNic_example"; // String | 
    String dnsNameIew = "dnsNameIew_example"; // String | 
    String dnsNameNiew = "dnsNameNiew_example"; // String | 
    String dnsNameIsw = "dnsNameIsw_example"; // String | 
    String dnsNameNisw = "dnsNameNisw_example"; // String | 
    String dnsNameIe = "dnsNameIe_example"; // String | 
    String dnsNameNie = "dnsNameNie_example"; // String | 
    String tenantGroupIdN = "tenantGroupIdN_example"; // String | 
    String tenantGroupN = "tenantGroupN_example"; // String | 
    String tenantIdN = "tenantIdN_example"; // String | 
    String tenantN = "tenantN_example"; // String | 
    String vrfIdN = "vrfIdN_example"; // String | 
    String vrfN = "vrfN_example"; // String | 
    String virtualMachineIdN = "virtualMachineIdN_example"; // String | 
    String virtualMachineN = "virtualMachineN_example"; // String | 
    String interfaceN = "interfaceN_example"; // String | 
    String interfaceIdN = "interfaceIdN_example"; // String | 
    String statusN = "statusN_example"; // String | 
    String roleN = "roleN_example"; // String | 
    String tagN = "tagN_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      IpamIpAddressesList200Response result = apiInstance.ipamIpAddressesList(id, dnsName, tenantGroupId, tenantGroup, tenantId, tenant, created, createdGte, createdLte, lastUpdated, lastUpdatedGte, lastUpdatedLte, q, family, parent, address, maskLength, vrfId, vrf, device, deviceId, virtualMachineId, virtualMachine, _interface, interfaceId, assignedToInterface, status, role, tag, idN, idLte, idLt, idGte, idGt, dnsNameN, dnsNameIc, dnsNameNic, dnsNameIew, dnsNameNiew, dnsNameIsw, dnsNameNisw, dnsNameIe, dnsNameNie, tenantGroupIdN, tenantGroupN, tenantIdN, tenantN, vrfIdN, vrfN, virtualMachineIdN, virtualMachineN, interfaceN, interfaceIdN, statusN, roleN, tagN, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamIpAddressesList");
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
| **dnsName** | **String**|  | [optional] |
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
| **family** | **BigDecimal**|  | [optional] |
| **parent** | **String**|  | [optional] |
| **address** | **String**|  | [optional] |
| **maskLength** | **BigDecimal**|  | [optional] |
| **vrfId** | **String**|  | [optional] |
| **vrf** | **String**|  | [optional] |
| **device** | **String**|  | [optional] |
| **deviceId** | **String**|  | [optional] |
| **virtualMachineId** | **String**|  | [optional] |
| **virtualMachine** | **String**|  | [optional] |
| **_interface** | **String**|  | [optional] |
| **interfaceId** | **String**|  | [optional] |
| **assignedToInterface** | **String**|  | [optional] |
| **status** | **String**|  | [optional] |
| **role** | **String**|  | [optional] |
| **tag** | **String**|  | [optional] |
| **idN** | **String**|  | [optional] |
| **idLte** | **String**|  | [optional] |
| **idLt** | **String**|  | [optional] |
| **idGte** | **String**|  | [optional] |
| **idGt** | **String**|  | [optional] |
| **dnsNameN** | **String**|  | [optional] |
| **dnsNameIc** | **String**|  | [optional] |
| **dnsNameNic** | **String**|  | [optional] |
| **dnsNameIew** | **String**|  | [optional] |
| **dnsNameNiew** | **String**|  | [optional] |
| **dnsNameIsw** | **String**|  | [optional] |
| **dnsNameNisw** | **String**|  | [optional] |
| **dnsNameIe** | **String**|  | [optional] |
| **dnsNameNie** | **String**|  | [optional] |
| **tenantGroupIdN** | **String**|  | [optional] |
| **tenantGroupN** | **String**|  | [optional] |
| **tenantIdN** | **String**|  | [optional] |
| **tenantN** | **String**|  | [optional] |
| **vrfIdN** | **String**|  | [optional] |
| **vrfN** | **String**|  | [optional] |
| **virtualMachineIdN** | **String**|  | [optional] |
| **virtualMachineN** | **String**|  | [optional] |
| **interfaceN** | **String**|  | [optional] |
| **interfaceIdN** | **String**|  | [optional] |
| **statusN** | **String**|  | [optional] |
| **roleN** | **String**|  | [optional] |
| **tagN** | **String**|  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**IpamIpAddressesList200Response**](IpamIpAddressesList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="ipamIpAddressesPartialUpdate"></a>
# **ipamIpAddressesPartialUpdate**
> IPAddress ipamIpAddressesPartialUpdate(id, writableIPAddress)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this IP address.
    WritableIPAddress writableIPAddress = new WritableIPAddress(); // WritableIPAddress | 
    try {
      IPAddress result = apiInstance.ipamIpAddressesPartialUpdate(id, writableIPAddress);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamIpAddressesPartialUpdate");
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
| **id** | **Integer**| A unique integer value identifying this IP address. | |
| **writableIPAddress** | [**WritableIPAddress**](WritableIPAddress.md)|  | |

### Return type

[**IPAddress**](IPAddress.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="ipamIpAddressesRead"></a>
# **ipamIpAddressesRead**
> IPAddress ipamIpAddressesRead(id)



Call to super to allow for caching

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this IP address.
    try {
      IPAddress result = apiInstance.ipamIpAddressesRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamIpAddressesRead");
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
| **id** | **Integer**| A unique integer value identifying this IP address. | |

### Return type

[**IPAddress**](IPAddress.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="ipamIpAddressesUpdate"></a>
# **ipamIpAddressesUpdate**
> IPAddress ipamIpAddressesUpdate(id, writableIPAddress)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this IP address.
    WritableIPAddress writableIPAddress = new WritableIPAddress(); // WritableIPAddress | 
    try {
      IPAddress result = apiInstance.ipamIpAddressesUpdate(id, writableIPAddress);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamIpAddressesUpdate");
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
| **id** | **Integer**| A unique integer value identifying this IP address. | |
| **writableIPAddress** | [**WritableIPAddress**](WritableIPAddress.md)|  | |

### Return type

[**IPAddress**](IPAddress.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="ipamPrefixesAvailableIpsCreate"></a>
# **ipamPrefixesAvailableIpsCreate**
> List&lt;AvailableIP&gt; ipamPrefixesAvailableIpsCreate(id, writableAvailableIP)



A convenience method for returning available IP addresses within a prefix. By default, the number of IPs returned will be equivalent to PAGINATE_COUNT. An arbitrary limit (up to MAX_PAGE_SIZE, if set) may be passed, however results will not be paginated.  The advisory lock decorator uses a PostgreSQL advisory lock to prevent this API from being invoked in parallel, which results in a race condition where multiple insertions can occur.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this prefix.
    WritableAvailableIP writableAvailableIP = new WritableAvailableIP(); // WritableAvailableIP | 
    try {
      List<AvailableIP> result = apiInstance.ipamPrefixesAvailableIpsCreate(id, writableAvailableIP);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamPrefixesAvailableIpsCreate");
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
| **id** | **Integer**| A unique integer value identifying this prefix. | |
| **writableAvailableIP** | [**WritableAvailableIP**](WritableAvailableIP.md)|  | |

### Return type

[**List&lt;AvailableIP&gt;**](AvailableIP.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="ipamPrefixesAvailableIpsRead"></a>
# **ipamPrefixesAvailableIpsRead**
> List&lt;AvailableIP&gt; ipamPrefixesAvailableIpsRead(id)



A convenience method for returning available IP addresses within a prefix. By default, the number of IPs returned will be equivalent to PAGINATE_COUNT. An arbitrary limit (up to MAX_PAGE_SIZE, if set) may be passed, however results will not be paginated.  The advisory lock decorator uses a PostgreSQL advisory lock to prevent this API from being invoked in parallel, which results in a race condition where multiple insertions can occur.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this prefix.
    try {
      List<AvailableIP> result = apiInstance.ipamPrefixesAvailableIpsRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamPrefixesAvailableIpsRead");
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
| **id** | **Integer**| A unique integer value identifying this prefix. | |

### Return type

[**List&lt;AvailableIP&gt;**](AvailableIP.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="ipamPrefixesAvailablePrefixesCreate"></a>
# **ipamPrefixesAvailablePrefixesCreate**
> List&lt;AvailablePrefix&gt; ipamPrefixesAvailablePrefixesCreate(id, writablePrefix)

A convenience method for returning available child prefixes within a parent.

The advisory lock decorator uses a PostgreSQL advisory lock to prevent this API from being invoked in parallel, which results in a race condition where multiple insertions can occur.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this prefix.
    WritablePrefix writablePrefix = new WritablePrefix(); // WritablePrefix | 
    try {
      List<AvailablePrefix> result = apiInstance.ipamPrefixesAvailablePrefixesCreate(id, writablePrefix);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamPrefixesAvailablePrefixesCreate");
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
| **id** | **Integer**| A unique integer value identifying this prefix. | |
| **writablePrefix** | [**WritablePrefix**](WritablePrefix.md)|  | |

### Return type

[**List&lt;AvailablePrefix&gt;**](AvailablePrefix.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="ipamPrefixesAvailablePrefixesRead"></a>
# **ipamPrefixesAvailablePrefixesRead**
> List&lt;AvailablePrefix&gt; ipamPrefixesAvailablePrefixesRead(id)

A convenience method for returning available child prefixes within a parent.

The advisory lock decorator uses a PostgreSQL advisory lock to prevent this API from being invoked in parallel, which results in a race condition where multiple insertions can occur.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this prefix.
    try {
      List<AvailablePrefix> result = apiInstance.ipamPrefixesAvailablePrefixesRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamPrefixesAvailablePrefixesRead");
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
| **id** | **Integer**| A unique integer value identifying this prefix. | |

### Return type

[**List&lt;AvailablePrefix&gt;**](AvailablePrefix.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="ipamPrefixesCreate"></a>
# **ipamPrefixesCreate**
> Prefix ipamPrefixesCreate(writablePrefix)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    WritablePrefix writablePrefix = new WritablePrefix(); // WritablePrefix | 
    try {
      Prefix result = apiInstance.ipamPrefixesCreate(writablePrefix);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamPrefixesCreate");
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
| **writablePrefix** | [**WritablePrefix**](WritablePrefix.md)|  | |

### Return type

[**Prefix**](Prefix.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="ipamPrefixesDelete"></a>
# **ipamPrefixesDelete**
> ipamPrefixesDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this prefix.
    try {
      apiInstance.ipamPrefixesDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamPrefixesDelete");
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
| **id** | **Integer**| A unique integer value identifying this prefix. | |

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

<a id="ipamPrefixesList"></a>
# **ipamPrefixesList**
> IpamPrefixesList200Response ipamPrefixesList(id, isPool, tenantGroupId, tenantGroup, tenantId, tenant, created, createdGte, createdLte, lastUpdated, lastUpdatedGte, lastUpdatedLte, q, family, prefix, within, withinInclude, contains, maskLength, vrfId, vrf, regionId, region, siteId, site, vlanId, vlanVid, roleId, role, status, tag, idN, idLte, idLt, idGte, idGt, tenantGroupIdN, tenantGroupN, tenantIdN, tenantN, vrfIdN, vrfN, regionIdN, regionN, siteIdN, siteN, vlanIdN, roleIdN, roleN, statusN, tagN, limit, offset)



Call to super to allow for caching

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    String id = "id_example"; // String | 
    String isPool = "isPool_example"; // String | 
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
    BigDecimal family = new BigDecimal(78); // BigDecimal | 
    String prefix = "prefix_example"; // String | 
    String within = "within_example"; // String | 
    String withinInclude = "withinInclude_example"; // String | 
    String contains = "contains_example"; // String | 
    BigDecimal maskLength = new BigDecimal(78); // BigDecimal | 
    String vrfId = "vrfId_example"; // String | 
    String vrf = "vrf_example"; // String | 
    String regionId = "regionId_example"; // String | 
    String region = "region_example"; // String | 
    String siteId = "siteId_example"; // String | 
    String site = "site_example"; // String | 
    String vlanId = "vlanId_example"; // String | 
    BigDecimal vlanVid = new BigDecimal(78); // BigDecimal | 
    String roleId = "roleId_example"; // String | 
    String role = "role_example"; // String | 
    String status = "status_example"; // String | 
    String tag = "tag_example"; // String | 
    String idN = "idN_example"; // String | 
    String idLte = "idLte_example"; // String | 
    String idLt = "idLt_example"; // String | 
    String idGte = "idGte_example"; // String | 
    String idGt = "idGt_example"; // String | 
    String tenantGroupIdN = "tenantGroupIdN_example"; // String | 
    String tenantGroupN = "tenantGroupN_example"; // String | 
    String tenantIdN = "tenantIdN_example"; // String | 
    String tenantN = "tenantN_example"; // String | 
    String vrfIdN = "vrfIdN_example"; // String | 
    String vrfN = "vrfN_example"; // String | 
    String regionIdN = "regionIdN_example"; // String | 
    String regionN = "regionN_example"; // String | 
    String siteIdN = "siteIdN_example"; // String | 
    String siteN = "siteN_example"; // String | 
    String vlanIdN = "vlanIdN_example"; // String | 
    String roleIdN = "roleIdN_example"; // String | 
    String roleN = "roleN_example"; // String | 
    String statusN = "statusN_example"; // String | 
    String tagN = "tagN_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      IpamPrefixesList200Response result = apiInstance.ipamPrefixesList(id, isPool, tenantGroupId, tenantGroup, tenantId, tenant, created, createdGte, createdLte, lastUpdated, lastUpdatedGte, lastUpdatedLte, q, family, prefix, within, withinInclude, contains, maskLength, vrfId, vrf, regionId, region, siteId, site, vlanId, vlanVid, roleId, role, status, tag, idN, idLte, idLt, idGte, idGt, tenantGroupIdN, tenantGroupN, tenantIdN, tenantN, vrfIdN, vrfN, regionIdN, regionN, siteIdN, siteN, vlanIdN, roleIdN, roleN, statusN, tagN, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamPrefixesList");
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
| **isPool** | **String**|  | [optional] |
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
| **family** | **BigDecimal**|  | [optional] |
| **prefix** | **String**|  | [optional] |
| **within** | **String**|  | [optional] |
| **withinInclude** | **String**|  | [optional] |
| **contains** | **String**|  | [optional] |
| **maskLength** | **BigDecimal**|  | [optional] |
| **vrfId** | **String**|  | [optional] |
| **vrf** | **String**|  | [optional] |
| **regionId** | **String**|  | [optional] |
| **region** | **String**|  | [optional] |
| **siteId** | **String**|  | [optional] |
| **site** | **String**|  | [optional] |
| **vlanId** | **String**|  | [optional] |
| **vlanVid** | **BigDecimal**|  | [optional] |
| **roleId** | **String**|  | [optional] |
| **role** | **String**|  | [optional] |
| **status** | **String**|  | [optional] |
| **tag** | **String**|  | [optional] |
| **idN** | **String**|  | [optional] |
| **idLte** | **String**|  | [optional] |
| **idLt** | **String**|  | [optional] |
| **idGte** | **String**|  | [optional] |
| **idGt** | **String**|  | [optional] |
| **tenantGroupIdN** | **String**|  | [optional] |
| **tenantGroupN** | **String**|  | [optional] |
| **tenantIdN** | **String**|  | [optional] |
| **tenantN** | **String**|  | [optional] |
| **vrfIdN** | **String**|  | [optional] |
| **vrfN** | **String**|  | [optional] |
| **regionIdN** | **String**|  | [optional] |
| **regionN** | **String**|  | [optional] |
| **siteIdN** | **String**|  | [optional] |
| **siteN** | **String**|  | [optional] |
| **vlanIdN** | **String**|  | [optional] |
| **roleIdN** | **String**|  | [optional] |
| **roleN** | **String**|  | [optional] |
| **statusN** | **String**|  | [optional] |
| **tagN** | **String**|  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**IpamPrefixesList200Response**](IpamPrefixesList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="ipamPrefixesPartialUpdate"></a>
# **ipamPrefixesPartialUpdate**
> Prefix ipamPrefixesPartialUpdate(id, writablePrefix)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this prefix.
    WritablePrefix writablePrefix = new WritablePrefix(); // WritablePrefix | 
    try {
      Prefix result = apiInstance.ipamPrefixesPartialUpdate(id, writablePrefix);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamPrefixesPartialUpdate");
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
| **id** | **Integer**| A unique integer value identifying this prefix. | |
| **writablePrefix** | [**WritablePrefix**](WritablePrefix.md)|  | |

### Return type

[**Prefix**](Prefix.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="ipamPrefixesRead"></a>
# **ipamPrefixesRead**
> Prefix ipamPrefixesRead(id)



Call to super to allow for caching

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this prefix.
    try {
      Prefix result = apiInstance.ipamPrefixesRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamPrefixesRead");
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
| **id** | **Integer**| A unique integer value identifying this prefix. | |

### Return type

[**Prefix**](Prefix.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="ipamPrefixesUpdate"></a>
# **ipamPrefixesUpdate**
> Prefix ipamPrefixesUpdate(id, writablePrefix)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this prefix.
    WritablePrefix writablePrefix = new WritablePrefix(); // WritablePrefix | 
    try {
      Prefix result = apiInstance.ipamPrefixesUpdate(id, writablePrefix);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamPrefixesUpdate");
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
| **id** | **Integer**| A unique integer value identifying this prefix. | |
| **writablePrefix** | [**WritablePrefix**](WritablePrefix.md)|  | |

### Return type

[**Prefix**](Prefix.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="ipamRirsCreate"></a>
# **ipamRirsCreate**
> RIR ipamRirsCreate(RIR)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    RIR RIR = new RIR(); // RIR | 
    try {
      RIR result = apiInstance.ipamRirsCreate(RIR);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamRirsCreate");
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
| **RIR** | [**RIR**](RIR.md)|  | |

### Return type

[**RIR**](RIR.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="ipamRirsDelete"></a>
# **ipamRirsDelete**
> ipamRirsDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this RIR.
    try {
      apiInstance.ipamRirsDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamRirsDelete");
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
| **id** | **Integer**| A unique integer value identifying this RIR. | |

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

<a id="ipamRirsList"></a>
# **ipamRirsList**
> IpamRirsList200Response ipamRirsList(id, name, slug, isPrivate, description, q, idN, idLte, idLt, idGte, idGt, nameN, nameIc, nameNic, nameIew, nameNiew, nameIsw, nameNisw, nameIe, nameNie, slugN, slugIc, slugNic, slugIew, slugNiew, slugIsw, slugNisw, slugIe, slugNie, descriptionN, descriptionIc, descriptionNic, descriptionIew, descriptionNiew, descriptionIsw, descriptionNisw, descriptionIe, descriptionNie, limit, offset)



Call to super to allow for caching

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    String id = "id_example"; // String | 
    String name = "name_example"; // String | 
    String slug = "slug_example"; // String | 
    String isPrivate = "isPrivate_example"; // String | 
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
      IpamRirsList200Response result = apiInstance.ipamRirsList(id, name, slug, isPrivate, description, q, idN, idLte, idLt, idGte, idGt, nameN, nameIc, nameNic, nameIew, nameNiew, nameIsw, nameNisw, nameIe, nameNie, slugN, slugIc, slugNic, slugIew, slugNiew, slugIsw, slugNisw, slugIe, slugNie, descriptionN, descriptionIc, descriptionNic, descriptionIew, descriptionNiew, descriptionIsw, descriptionNisw, descriptionIe, descriptionNie, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamRirsList");
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
| **isPrivate** | **String**|  | [optional] |
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

[**IpamRirsList200Response**](IpamRirsList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="ipamRirsPartialUpdate"></a>
# **ipamRirsPartialUpdate**
> RIR ipamRirsPartialUpdate(id, RIR)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this RIR.
    RIR RIR = new RIR(); // RIR | 
    try {
      RIR result = apiInstance.ipamRirsPartialUpdate(id, RIR);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamRirsPartialUpdate");
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
| **id** | **Integer**| A unique integer value identifying this RIR. | |
| **RIR** | [**RIR**](RIR.md)|  | |

### Return type

[**RIR**](RIR.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="ipamRirsRead"></a>
# **ipamRirsRead**
> RIR ipamRirsRead(id)



Call to super to allow for caching

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this RIR.
    try {
      RIR result = apiInstance.ipamRirsRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamRirsRead");
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
| **id** | **Integer**| A unique integer value identifying this RIR. | |

### Return type

[**RIR**](RIR.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="ipamRirsUpdate"></a>
# **ipamRirsUpdate**
> RIR ipamRirsUpdate(id, RIR)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this RIR.
    RIR RIR = new RIR(); // RIR | 
    try {
      RIR result = apiInstance.ipamRirsUpdate(id, RIR);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamRirsUpdate");
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
| **id** | **Integer**| A unique integer value identifying this RIR. | |
| **RIR** | [**RIR**](RIR.md)|  | |

### Return type

[**RIR**](RIR.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="ipamRolesCreate"></a>
# **ipamRolesCreate**
> Role ipamRolesCreate(role)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    Role role = new Role(); // Role | 
    try {
      Role result = apiInstance.ipamRolesCreate(role);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamRolesCreate");
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
| **role** | [**Role**](Role.md)|  | |

### Return type

[**Role**](Role.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="ipamRolesDelete"></a>
# **ipamRolesDelete**
> ipamRolesDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this role.
    try {
      apiInstance.ipamRolesDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamRolesDelete");
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
| **id** | **Integer**| A unique integer value identifying this role. | |

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

<a id="ipamRolesList"></a>
# **ipamRolesList**
> IpamRolesList200Response ipamRolesList(id, name, slug, q, idN, idLte, idLt, idGte, idGt, nameN, nameIc, nameNic, nameIew, nameNiew, nameIsw, nameNisw, nameIe, nameNie, slugN, slugIc, slugNic, slugIew, slugNiew, slugIsw, slugNisw, slugIe, slugNie, limit, offset)



Call to super to allow for caching

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    String id = "id_example"; // String | 
    String name = "name_example"; // String | 
    String slug = "slug_example"; // String | 
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
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      IpamRolesList200Response result = apiInstance.ipamRolesList(id, name, slug, q, idN, idLte, idLt, idGte, idGt, nameN, nameIc, nameNic, nameIew, nameNiew, nameIsw, nameNisw, nameIe, nameNie, slugN, slugIc, slugNic, slugIew, slugNiew, slugIsw, slugNisw, slugIe, slugNie, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamRolesList");
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
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**IpamRolesList200Response**](IpamRolesList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="ipamRolesPartialUpdate"></a>
# **ipamRolesPartialUpdate**
> Role ipamRolesPartialUpdate(id, role)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this role.
    Role role = new Role(); // Role | 
    try {
      Role result = apiInstance.ipamRolesPartialUpdate(id, role);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamRolesPartialUpdate");
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
| **id** | **Integer**| A unique integer value identifying this role. | |
| **role** | [**Role**](Role.md)|  | |

### Return type

[**Role**](Role.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="ipamRolesRead"></a>
# **ipamRolesRead**
> Role ipamRolesRead(id)



Call to super to allow for caching

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this role.
    try {
      Role result = apiInstance.ipamRolesRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamRolesRead");
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
| **id** | **Integer**| A unique integer value identifying this role. | |

### Return type

[**Role**](Role.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="ipamRolesUpdate"></a>
# **ipamRolesUpdate**
> Role ipamRolesUpdate(id, role)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this role.
    Role role = new Role(); // Role | 
    try {
      Role result = apiInstance.ipamRolesUpdate(id, role);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamRolesUpdate");
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
| **id** | **Integer**| A unique integer value identifying this role. | |
| **role** | [**Role**](Role.md)|  | |

### Return type

[**Role**](Role.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="ipamServicesCreate"></a>
# **ipamServicesCreate**
> Service ipamServicesCreate(writableService)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    WritableService writableService = new WritableService(); // WritableService | 
    try {
      Service result = apiInstance.ipamServicesCreate(writableService);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamServicesCreate");
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
| **writableService** | [**WritableService**](WritableService.md)|  | |

### Return type

[**Service**](Service.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="ipamServicesDelete"></a>
# **ipamServicesDelete**
> ipamServicesDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this service.
    try {
      apiInstance.ipamServicesDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamServicesDelete");
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
| **id** | **Integer**| A unique integer value identifying this service. | |

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

<a id="ipamServicesList"></a>
# **ipamServicesList**
> IpamServicesList200Response ipamServicesList(id, name, protocol, port, created, createdGte, createdLte, lastUpdated, lastUpdatedGte, lastUpdatedLte, q, deviceId, device, virtualMachineId, virtualMachine, tag, idN, idLte, idLt, idGte, idGt, nameN, nameIc, nameNic, nameIew, nameNiew, nameIsw, nameNisw, nameIe, nameNie, protocolN, portN, portLte, portLt, portGte, portGt, deviceIdN, deviceN, virtualMachineIdN, virtualMachineN, tagN, limit, offset)



Call to super to allow for caching

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    String id = "id_example"; // String | 
    String name = "name_example"; // String | 
    String protocol = "protocol_example"; // String | 
    String port = "port_example"; // String | 
    String created = "created_example"; // String | 
    String createdGte = "createdGte_example"; // String | 
    String createdLte = "createdLte_example"; // String | 
    String lastUpdated = "lastUpdated_example"; // String | 
    String lastUpdatedGte = "lastUpdatedGte_example"; // String | 
    String lastUpdatedLte = "lastUpdatedLte_example"; // String | 
    String q = "q_example"; // String | 
    String deviceId = "deviceId_example"; // String | 
    String device = "device_example"; // String | 
    String virtualMachineId = "virtualMachineId_example"; // String | 
    String virtualMachine = "virtualMachine_example"; // String | 
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
    String protocolN = "protocolN_example"; // String | 
    String portN = "portN_example"; // String | 
    String portLte = "portLte_example"; // String | 
    String portLt = "portLt_example"; // String | 
    String portGte = "portGte_example"; // String | 
    String portGt = "portGt_example"; // String | 
    String deviceIdN = "deviceIdN_example"; // String | 
    String deviceN = "deviceN_example"; // String | 
    String virtualMachineIdN = "virtualMachineIdN_example"; // String | 
    String virtualMachineN = "virtualMachineN_example"; // String | 
    String tagN = "tagN_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      IpamServicesList200Response result = apiInstance.ipamServicesList(id, name, protocol, port, created, createdGte, createdLte, lastUpdated, lastUpdatedGte, lastUpdatedLte, q, deviceId, device, virtualMachineId, virtualMachine, tag, idN, idLte, idLt, idGte, idGt, nameN, nameIc, nameNic, nameIew, nameNiew, nameIsw, nameNisw, nameIe, nameNie, protocolN, portN, portLte, portLt, portGte, portGt, deviceIdN, deviceN, virtualMachineIdN, virtualMachineN, tagN, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamServicesList");
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
| **protocol** | **String**|  | [optional] |
| **port** | **String**|  | [optional] |
| **created** | **String**|  | [optional] |
| **createdGte** | **String**|  | [optional] |
| **createdLte** | **String**|  | [optional] |
| **lastUpdated** | **String**|  | [optional] |
| **lastUpdatedGte** | **String**|  | [optional] |
| **lastUpdatedLte** | **String**|  | [optional] |
| **q** | **String**|  | [optional] |
| **deviceId** | **String**|  | [optional] |
| **device** | **String**|  | [optional] |
| **virtualMachineId** | **String**|  | [optional] |
| **virtualMachine** | **String**|  | [optional] |
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
| **protocolN** | **String**|  | [optional] |
| **portN** | **String**|  | [optional] |
| **portLte** | **String**|  | [optional] |
| **portLt** | **String**|  | [optional] |
| **portGte** | **String**|  | [optional] |
| **portGt** | **String**|  | [optional] |
| **deviceIdN** | **String**|  | [optional] |
| **deviceN** | **String**|  | [optional] |
| **virtualMachineIdN** | **String**|  | [optional] |
| **virtualMachineN** | **String**|  | [optional] |
| **tagN** | **String**|  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**IpamServicesList200Response**](IpamServicesList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="ipamServicesPartialUpdate"></a>
# **ipamServicesPartialUpdate**
> Service ipamServicesPartialUpdate(id, writableService)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this service.
    WritableService writableService = new WritableService(); // WritableService | 
    try {
      Service result = apiInstance.ipamServicesPartialUpdate(id, writableService);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamServicesPartialUpdate");
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
| **id** | **Integer**| A unique integer value identifying this service. | |
| **writableService** | [**WritableService**](WritableService.md)|  | |

### Return type

[**Service**](Service.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="ipamServicesRead"></a>
# **ipamServicesRead**
> Service ipamServicesRead(id)



Call to super to allow for caching

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this service.
    try {
      Service result = apiInstance.ipamServicesRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamServicesRead");
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
| **id** | **Integer**| A unique integer value identifying this service. | |

### Return type

[**Service**](Service.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="ipamServicesUpdate"></a>
# **ipamServicesUpdate**
> Service ipamServicesUpdate(id, writableService)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this service.
    WritableService writableService = new WritableService(); // WritableService | 
    try {
      Service result = apiInstance.ipamServicesUpdate(id, writableService);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamServicesUpdate");
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
| **id** | **Integer**| A unique integer value identifying this service. | |
| **writableService** | [**WritableService**](WritableService.md)|  | |

### Return type

[**Service**](Service.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="ipamVlanGroupsCreate"></a>
# **ipamVlanGroupsCreate**
> VLANGroup ipamVlanGroupsCreate(writableVLANGroup)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    WritableVLANGroup writableVLANGroup = new WritableVLANGroup(); // WritableVLANGroup | 
    try {
      VLANGroup result = apiInstance.ipamVlanGroupsCreate(writableVLANGroup);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamVlanGroupsCreate");
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
| **writableVLANGroup** | [**WritableVLANGroup**](WritableVLANGroup.md)|  | |

### Return type

[**VLANGroup**](VLANGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="ipamVlanGroupsDelete"></a>
# **ipamVlanGroupsDelete**
> ipamVlanGroupsDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this VLAN group.
    try {
      apiInstance.ipamVlanGroupsDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamVlanGroupsDelete");
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
| **id** | **Integer**| A unique integer value identifying this VLAN group. | |

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

<a id="ipamVlanGroupsList"></a>
# **ipamVlanGroupsList**
> IpamVlanGroupsList200Response ipamVlanGroupsList(id, name, slug, description, q, regionId, region, siteId, site, idN, idLte, idLt, idGte, idGt, nameN, nameIc, nameNic, nameIew, nameNiew, nameIsw, nameNisw, nameIe, nameNie, slugN, slugIc, slugNic, slugIew, slugNiew, slugIsw, slugNisw, slugIe, slugNie, descriptionN, descriptionIc, descriptionNic, descriptionIew, descriptionNiew, descriptionIsw, descriptionNisw, descriptionIe, descriptionNie, regionIdN, regionN, siteIdN, siteN, limit, offset)



Call to super to allow for caching

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    String id = "id_example"; // String | 
    String name = "name_example"; // String | 
    String slug = "slug_example"; // String | 
    String description = "description_example"; // String | 
    String q = "q_example"; // String | 
    String regionId = "regionId_example"; // String | 
    String region = "region_example"; // String | 
    String siteId = "siteId_example"; // String | 
    String site = "site_example"; // String | 
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
    String regionIdN = "regionIdN_example"; // String | 
    String regionN = "regionN_example"; // String | 
    String siteIdN = "siteIdN_example"; // String | 
    String siteN = "siteN_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      IpamVlanGroupsList200Response result = apiInstance.ipamVlanGroupsList(id, name, slug, description, q, regionId, region, siteId, site, idN, idLte, idLt, idGte, idGt, nameN, nameIc, nameNic, nameIew, nameNiew, nameIsw, nameNisw, nameIe, nameNie, slugN, slugIc, slugNic, slugIew, slugNiew, slugIsw, slugNisw, slugIe, slugNie, descriptionN, descriptionIc, descriptionNic, descriptionIew, descriptionNiew, descriptionIsw, descriptionNisw, descriptionIe, descriptionNie, regionIdN, regionN, siteIdN, siteN, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamVlanGroupsList");
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
| **regionId** | **String**|  | [optional] |
| **region** | **String**|  | [optional] |
| **siteId** | **String**|  | [optional] |
| **site** | **String**|  | [optional] |
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
| **regionIdN** | **String**|  | [optional] |
| **regionN** | **String**|  | [optional] |
| **siteIdN** | **String**|  | [optional] |
| **siteN** | **String**|  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**IpamVlanGroupsList200Response**](IpamVlanGroupsList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="ipamVlanGroupsPartialUpdate"></a>
# **ipamVlanGroupsPartialUpdate**
> VLANGroup ipamVlanGroupsPartialUpdate(id, writableVLANGroup)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this VLAN group.
    WritableVLANGroup writableVLANGroup = new WritableVLANGroup(); // WritableVLANGroup | 
    try {
      VLANGroup result = apiInstance.ipamVlanGroupsPartialUpdate(id, writableVLANGroup);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamVlanGroupsPartialUpdate");
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
| **id** | **Integer**| A unique integer value identifying this VLAN group. | |
| **writableVLANGroup** | [**WritableVLANGroup**](WritableVLANGroup.md)|  | |

### Return type

[**VLANGroup**](VLANGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="ipamVlanGroupsRead"></a>
# **ipamVlanGroupsRead**
> VLANGroup ipamVlanGroupsRead(id)



Call to super to allow for caching

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this VLAN group.
    try {
      VLANGroup result = apiInstance.ipamVlanGroupsRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamVlanGroupsRead");
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
| **id** | **Integer**| A unique integer value identifying this VLAN group. | |

### Return type

[**VLANGroup**](VLANGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="ipamVlanGroupsUpdate"></a>
# **ipamVlanGroupsUpdate**
> VLANGroup ipamVlanGroupsUpdate(id, writableVLANGroup)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this VLAN group.
    WritableVLANGroup writableVLANGroup = new WritableVLANGroup(); // WritableVLANGroup | 
    try {
      VLANGroup result = apiInstance.ipamVlanGroupsUpdate(id, writableVLANGroup);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamVlanGroupsUpdate");
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
| **id** | **Integer**| A unique integer value identifying this VLAN group. | |
| **writableVLANGroup** | [**WritableVLANGroup**](WritableVLANGroup.md)|  | |

### Return type

[**VLANGroup**](VLANGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="ipamVlansCreate"></a>
# **ipamVlansCreate**
> VLAN ipamVlansCreate(writableVLAN)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    WritableVLAN writableVLAN = new WritableVLAN(); // WritableVLAN | 
    try {
      VLAN result = apiInstance.ipamVlansCreate(writableVLAN);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamVlansCreate");
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
| **writableVLAN** | [**WritableVLAN**](WritableVLAN.md)|  | |

### Return type

[**VLAN**](VLAN.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="ipamVlansDelete"></a>
# **ipamVlansDelete**
> ipamVlansDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this VLAN.
    try {
      apiInstance.ipamVlansDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamVlansDelete");
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
| **id** | **Integer**| A unique integer value identifying this VLAN. | |

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

<a id="ipamVlansList"></a>
# **ipamVlansList**
> IpamVlansList200Response ipamVlansList(id, vid, name, tenantGroupId, tenantGroup, tenantId, tenant, created, createdGte, createdLte, lastUpdated, lastUpdatedGte, lastUpdatedLte, q, regionId, region, siteId, site, groupId, group, roleId, role, status, tag, idN, idLte, idLt, idGte, idGt, vidN, vidLte, vidLt, vidGte, vidGt, nameN, nameIc, nameNic, nameIew, nameNiew, nameIsw, nameNisw, nameIe, nameNie, tenantGroupIdN, tenantGroupN, tenantIdN, tenantN, regionIdN, regionN, siteIdN, siteN, groupIdN, groupN, roleIdN, roleN, statusN, tagN, limit, offset)



Call to super to allow for caching

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    String id = "id_example"; // String | 
    String vid = "vid_example"; // String | 
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
    String roleId = "roleId_example"; // String | 
    String role = "role_example"; // String | 
    String status = "status_example"; // String | 
    String tag = "tag_example"; // String | 
    String idN = "idN_example"; // String | 
    String idLte = "idLte_example"; // String | 
    String idLt = "idLt_example"; // String | 
    String idGte = "idGte_example"; // String | 
    String idGt = "idGt_example"; // String | 
    String vidN = "vidN_example"; // String | 
    String vidLte = "vidLte_example"; // String | 
    String vidLt = "vidLt_example"; // String | 
    String vidGte = "vidGte_example"; // String | 
    String vidGt = "vidGt_example"; // String | 
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
    String roleIdN = "roleIdN_example"; // String | 
    String roleN = "roleN_example"; // String | 
    String statusN = "statusN_example"; // String | 
    String tagN = "tagN_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      IpamVlansList200Response result = apiInstance.ipamVlansList(id, vid, name, tenantGroupId, tenantGroup, tenantId, tenant, created, createdGte, createdLte, lastUpdated, lastUpdatedGte, lastUpdatedLte, q, regionId, region, siteId, site, groupId, group, roleId, role, status, tag, idN, idLte, idLt, idGte, idGt, vidN, vidLte, vidLt, vidGte, vidGt, nameN, nameIc, nameNic, nameIew, nameNiew, nameIsw, nameNisw, nameIe, nameNie, tenantGroupIdN, tenantGroupN, tenantIdN, tenantN, regionIdN, regionN, siteIdN, siteN, groupIdN, groupN, roleIdN, roleN, statusN, tagN, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamVlansList");
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
| **vid** | **String**|  | [optional] |
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
| **roleId** | **String**|  | [optional] |
| **role** | **String**|  | [optional] |
| **status** | **String**|  | [optional] |
| **tag** | **String**|  | [optional] |
| **idN** | **String**|  | [optional] |
| **idLte** | **String**|  | [optional] |
| **idLt** | **String**|  | [optional] |
| **idGte** | **String**|  | [optional] |
| **idGt** | **String**|  | [optional] |
| **vidN** | **String**|  | [optional] |
| **vidLte** | **String**|  | [optional] |
| **vidLt** | **String**|  | [optional] |
| **vidGte** | **String**|  | [optional] |
| **vidGt** | **String**|  | [optional] |
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
| **roleIdN** | **String**|  | [optional] |
| **roleN** | **String**|  | [optional] |
| **statusN** | **String**|  | [optional] |
| **tagN** | **String**|  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**IpamVlansList200Response**](IpamVlansList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="ipamVlansPartialUpdate"></a>
# **ipamVlansPartialUpdate**
> VLAN ipamVlansPartialUpdate(id, writableVLAN)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this VLAN.
    WritableVLAN writableVLAN = new WritableVLAN(); // WritableVLAN | 
    try {
      VLAN result = apiInstance.ipamVlansPartialUpdate(id, writableVLAN);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamVlansPartialUpdate");
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
| **id** | **Integer**| A unique integer value identifying this VLAN. | |
| **writableVLAN** | [**WritableVLAN**](WritableVLAN.md)|  | |

### Return type

[**VLAN**](VLAN.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="ipamVlansRead"></a>
# **ipamVlansRead**
> VLAN ipamVlansRead(id)



Call to super to allow for caching

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this VLAN.
    try {
      VLAN result = apiInstance.ipamVlansRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamVlansRead");
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
| **id** | **Integer**| A unique integer value identifying this VLAN. | |

### Return type

[**VLAN**](VLAN.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="ipamVlansUpdate"></a>
# **ipamVlansUpdate**
> VLAN ipamVlansUpdate(id, writableVLAN)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this VLAN.
    WritableVLAN writableVLAN = new WritableVLAN(); // WritableVLAN | 
    try {
      VLAN result = apiInstance.ipamVlansUpdate(id, writableVLAN);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamVlansUpdate");
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
| **id** | **Integer**| A unique integer value identifying this VLAN. | |
| **writableVLAN** | [**WritableVLAN**](WritableVLAN.md)|  | |

### Return type

[**VLAN**](VLAN.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="ipamVrfsCreate"></a>
# **ipamVrfsCreate**
> VRF ipamVrfsCreate(writableVRF)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    WritableVRF writableVRF = new WritableVRF(); // WritableVRF | 
    try {
      VRF result = apiInstance.ipamVrfsCreate(writableVRF);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamVrfsCreate");
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
| **writableVRF** | [**WritableVRF**](WritableVRF.md)|  | |

### Return type

[**VRF**](VRF.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="ipamVrfsDelete"></a>
# **ipamVrfsDelete**
> ipamVrfsDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this VRF.
    try {
      apiInstance.ipamVrfsDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamVrfsDelete");
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
| **id** | **Integer**| A unique integer value identifying this VRF. | |

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

<a id="ipamVrfsList"></a>
# **ipamVrfsList**
> IpamVrfsList200Response ipamVrfsList(id, name, rd, enforceUnique, tenantGroupId, tenantGroup, tenantId, tenant, created, createdGte, createdLte, lastUpdated, lastUpdatedGte, lastUpdatedLte, q, tag, idN, idLte, idLt, idGte, idGt, nameN, nameIc, nameNic, nameIew, nameNiew, nameIsw, nameNisw, nameIe, nameNie, rdN, rdIc, rdNic, rdIew, rdNiew, rdIsw, rdNisw, rdIe, rdNie, tenantGroupIdN, tenantGroupN, tenantIdN, tenantN, tagN, limit, offset)



Call to super to allow for caching

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    String id = "id_example"; // String | 
    String name = "name_example"; // String | 
    String rd = "rd_example"; // String | 
    String enforceUnique = "enforceUnique_example"; // String | 
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
    String rdN = "rdN_example"; // String | 
    String rdIc = "rdIc_example"; // String | 
    String rdNic = "rdNic_example"; // String | 
    String rdIew = "rdIew_example"; // String | 
    String rdNiew = "rdNiew_example"; // String | 
    String rdIsw = "rdIsw_example"; // String | 
    String rdNisw = "rdNisw_example"; // String | 
    String rdIe = "rdIe_example"; // String | 
    String rdNie = "rdNie_example"; // String | 
    String tenantGroupIdN = "tenantGroupIdN_example"; // String | 
    String tenantGroupN = "tenantGroupN_example"; // String | 
    String tenantIdN = "tenantIdN_example"; // String | 
    String tenantN = "tenantN_example"; // String | 
    String tagN = "tagN_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      IpamVrfsList200Response result = apiInstance.ipamVrfsList(id, name, rd, enforceUnique, tenantGroupId, tenantGroup, tenantId, tenant, created, createdGte, createdLte, lastUpdated, lastUpdatedGte, lastUpdatedLte, q, tag, idN, idLte, idLt, idGte, idGt, nameN, nameIc, nameNic, nameIew, nameNiew, nameIsw, nameNisw, nameIe, nameNie, rdN, rdIc, rdNic, rdIew, rdNiew, rdIsw, rdNisw, rdIe, rdNie, tenantGroupIdN, tenantGroupN, tenantIdN, tenantN, tagN, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamVrfsList");
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
| **rd** | **String**|  | [optional] |
| **enforceUnique** | **String**|  | [optional] |
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
| **rdN** | **String**|  | [optional] |
| **rdIc** | **String**|  | [optional] |
| **rdNic** | **String**|  | [optional] |
| **rdIew** | **String**|  | [optional] |
| **rdNiew** | **String**|  | [optional] |
| **rdIsw** | **String**|  | [optional] |
| **rdNisw** | **String**|  | [optional] |
| **rdIe** | **String**|  | [optional] |
| **rdNie** | **String**|  | [optional] |
| **tenantGroupIdN** | **String**|  | [optional] |
| **tenantGroupN** | **String**|  | [optional] |
| **tenantIdN** | **String**|  | [optional] |
| **tenantN** | **String**|  | [optional] |
| **tagN** | **String**|  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**IpamVrfsList200Response**](IpamVrfsList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="ipamVrfsPartialUpdate"></a>
# **ipamVrfsPartialUpdate**
> VRF ipamVrfsPartialUpdate(id, writableVRF)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this VRF.
    WritableVRF writableVRF = new WritableVRF(); // WritableVRF | 
    try {
      VRF result = apiInstance.ipamVrfsPartialUpdate(id, writableVRF);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamVrfsPartialUpdate");
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
| **id** | **Integer**| A unique integer value identifying this VRF. | |
| **writableVRF** | [**WritableVRF**](WritableVRF.md)|  | |

### Return type

[**VRF**](VRF.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="ipamVrfsRead"></a>
# **ipamVrfsRead**
> VRF ipamVrfsRead(id)



Call to super to allow for caching

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this VRF.
    try {
      VRF result = apiInstance.ipamVrfsRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamVrfsRead");
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
| **id** | **Integer**| A unique integer value identifying this VRF. | |

### Return type

[**VRF**](VRF.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="ipamVrfsUpdate"></a>
# **ipamVrfsUpdate**
> VRF ipamVrfsUpdate(id, writableVRF)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this VRF.
    WritableVRF writableVRF = new WritableVRF(); // WritableVRF | 
    try {
      VRF result = apiInstance.ipamVrfsUpdate(id, writableVRF);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamVrfsUpdate");
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
| **id** | **Integer**| A unique integer value identifying this VRF. | |
| **writableVRF** | [**WritableVRF**](WritableVRF.md)|  | |

### Return type

[**VRF**](VRF.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

