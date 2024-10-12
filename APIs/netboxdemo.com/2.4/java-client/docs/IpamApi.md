# IpamApi

All URIs are relative to *http://netboxdemo.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**ipamAggregatesCreate**](IpamApi.md#ipamAggregatesCreate) | **POST** /ipam/aggregates/ |  |
| [**ipamAggregatesDelete**](IpamApi.md#ipamAggregatesDelete) | **DELETE** /ipam/aggregates/{id}/ |  |
| [**ipamAggregatesList**](IpamApi.md#ipamAggregatesList) | **GET** /ipam/aggregates/ |  |
| [**ipamAggregatesPartialUpdate**](IpamApi.md#ipamAggregatesPartialUpdate) | **PATCH** /ipam/aggregates/{id}/ |  |
| [**ipamAggregatesRead**](IpamApi.md#ipamAggregatesRead) | **GET** /ipam/aggregates/{id}/ |  |
| [**ipamAggregatesUpdate**](IpamApi.md#ipamAggregatesUpdate) | **PUT** /ipam/aggregates/{id}/ |  |
| [**ipamChoicesList**](IpamApi.md#ipamChoicesList) | **GET** /ipam/_choices/ |  |
| [**ipamChoicesRead**](IpamApi.md#ipamChoicesRead) | **GET** /ipam/_choices/{id}/ |  |
| [**ipamIpAddressesCreate**](IpamApi.md#ipamIpAddressesCreate) | **POST** /ipam/ip-addresses/ |  |
| [**ipamIpAddressesDelete**](IpamApi.md#ipamIpAddressesDelete) | **DELETE** /ipam/ip-addresses/{id}/ |  |
| [**ipamIpAddressesList**](IpamApi.md#ipamIpAddressesList) | **GET** /ipam/ip-addresses/ |  |
| [**ipamIpAddressesPartialUpdate**](IpamApi.md#ipamIpAddressesPartialUpdate) | **PATCH** /ipam/ip-addresses/{id}/ |  |
| [**ipamIpAddressesRead**](IpamApi.md#ipamIpAddressesRead) | **GET** /ipam/ip-addresses/{id}/ |  |
| [**ipamIpAddressesUpdate**](IpamApi.md#ipamIpAddressesUpdate) | **PUT** /ipam/ip-addresses/{id}/ |  |
| [**ipamPrefixesAvailableIpsCreate**](IpamApi.md#ipamPrefixesAvailableIpsCreate) | **POST** /ipam/prefixes/{id}/available-ips/ |  |
| [**ipamPrefixesAvailableIpsRead**](IpamApi.md#ipamPrefixesAvailableIpsRead) | **GET** /ipam/prefixes/{id}/available-ips/ |  |
| [**ipamPrefixesAvailablePrefixesCreate**](IpamApi.md#ipamPrefixesAvailablePrefixesCreate) | **POST** /ipam/prefixes/{id}/available-prefixes/ |  |
| [**ipamPrefixesAvailablePrefixesRead**](IpamApi.md#ipamPrefixesAvailablePrefixesRead) | **GET** /ipam/prefixes/{id}/available-prefixes/ |  |
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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
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
> IpamAggregatesList200Response ipamAggregatesList(family, dateAdded, idIn, q, rirId, rir, tag, limit, offset)





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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    String family = "family_example"; // String | 
    String dateAdded = "dateAdded_example"; // String | 
    String idIn = "idIn_example"; // String | Multiple values may be separated by commas.
    String q = "q_example"; // String | 
    String rirId = "rirId_example"; // String | 
    String rir = "rir_example"; // String | 
    String tag = "tag_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      IpamAggregatesList200Response result = apiInstance.ipamAggregatesList(family, dateAdded, idIn, q, rirId, rir, tag, limit, offset);
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
| **family** | **String**|  | [optional] |
| **dateAdded** | **String**|  | [optional] |
| **idIn** | **String**| Multiple values may be separated by commas. | [optional] |
| **q** | **String**|  | [optional] |
| **rirId** | **String**|  | [optional] |
| **rir** | **String**|  | [optional] |
| **tag** | **String**|  | [optional] |
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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
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

<a id="ipamChoicesList"></a>
# **ipamChoicesList**
> ipamChoicesList()





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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    try {
      apiInstance.ipamChoicesList();
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamChoicesList");
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

<a id="ipamChoicesRead"></a>
# **ipamChoicesRead**
> ipamChoicesRead(id)





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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.ipamChoicesRead(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpamApi#ipamChoicesRead");
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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
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
> IpamIpAddressesList200Response ipamIpAddressesList(family, idIn, q, parent, address, maskLength, vrfId, vrf, tenantId, tenant, device, deviceId, virtualMachineId, virtualMachine, interfaceId, status, role, tag, limit, offset)





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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    String family = "family_example"; // String | 
    String idIn = "idIn_example"; // String | Multiple values may be separated by commas.
    String q = "q_example"; // String | 
    String parent = "parent_example"; // String | 
    String address = "address_example"; // String | 
    BigDecimal maskLength = new BigDecimal(78); // BigDecimal | 
    String vrfId = "vrfId_example"; // String | 
    String vrf = "vrf_example"; // String | 
    String tenantId = "tenantId_example"; // String | 
    String tenant = "tenant_example"; // String | 
    String device = "device_example"; // String | 
    BigDecimal deviceId = new BigDecimal(78); // BigDecimal | 
    String virtualMachineId = "virtualMachineId_example"; // String | 
    String virtualMachine = "virtualMachine_example"; // String | 
    String interfaceId = "interfaceId_example"; // String | 
    String status = "status_example"; // String | 
    String role = "role_example"; // String | 
    String tag = "tag_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      IpamIpAddressesList200Response result = apiInstance.ipamIpAddressesList(family, idIn, q, parent, address, maskLength, vrfId, vrf, tenantId, tenant, device, deviceId, virtualMachineId, virtualMachine, interfaceId, status, role, tag, limit, offset);
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
| **family** | **String**|  | [optional] |
| **idIn** | **String**| Multiple values may be separated by commas. | [optional] |
| **q** | **String**|  | [optional] |
| **parent** | **String**|  | [optional] |
| **address** | **String**|  | [optional] |
| **maskLength** | **BigDecimal**|  | [optional] |
| **vrfId** | **String**|  | [optional] |
| **vrf** | **String**|  | [optional] |
| **tenantId** | **String**|  | [optional] |
| **tenant** | **String**|  | [optional] |
| **device** | **String**|  | [optional] |
| **deviceId** | **BigDecimal**|  | [optional] |
| **virtualMachineId** | **String**|  | [optional] |
| **virtualMachine** | **String**|  | [optional] |
| **interfaceId** | **String**|  | [optional] |
| **status** | **String**|  | [optional] |
| **role** | **String**|  | [optional] |
| **tag** | **String**|  | [optional] |
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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
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
> Prefix ipamPrefixesAvailableIpsCreate(id, writablePrefix)



A convenience method for returning available IP addresses within a prefix. By default, the number of IPs returned will be equivalent to PAGINATE_COUNT. An arbitrary limit (up to MAX_PAGE_SIZE, if set) may be passed, however results will not be paginated.

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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this prefix.
    WritablePrefix writablePrefix = new WritablePrefix(); // WritablePrefix | 
    try {
      Prefix result = apiInstance.ipamPrefixesAvailableIpsCreate(id, writablePrefix);
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

<a id="ipamPrefixesAvailableIpsRead"></a>
# **ipamPrefixesAvailableIpsRead**
> Prefix ipamPrefixesAvailableIpsRead(id)



A convenience method for returning available IP addresses within a prefix. By default, the number of IPs returned will be equivalent to PAGINATE_COUNT. An arbitrary limit (up to MAX_PAGE_SIZE, if set) may be passed, however results will not be paginated.

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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this prefix.
    try {
      Prefix result = apiInstance.ipamPrefixesAvailableIpsRead(id);
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

<a id="ipamPrefixesAvailablePrefixesCreate"></a>
# **ipamPrefixesAvailablePrefixesCreate**
> Prefix ipamPrefixesAvailablePrefixesCreate(id, writablePrefix)



A convenience method for returning available child prefixes within a parent.

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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this prefix.
    WritablePrefix writablePrefix = new WritablePrefix(); // WritablePrefix | 
    try {
      Prefix result = apiInstance.ipamPrefixesAvailablePrefixesCreate(id, writablePrefix);
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

<a id="ipamPrefixesAvailablePrefixesRead"></a>
# **ipamPrefixesAvailablePrefixesRead**
> Prefix ipamPrefixesAvailablePrefixesRead(id)



A convenience method for returning available child prefixes within a parent.

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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this prefix.
    try {
      Prefix result = apiInstance.ipamPrefixesAvailablePrefixesRead(id);
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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
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
> IpamPrefixesList200Response ipamPrefixesList(family, isPool, idIn, q, within, withinInclude, contains, maskLength, vrfId, vrf, tenantId, tenant, siteId, site, vlanId, vlanVid, roleId, role, status, tag, limit, offset)





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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    String family = "family_example"; // String | 
    String isPool = "isPool_example"; // String | 
    String idIn = "idIn_example"; // String | Multiple values may be separated by commas.
    String q = "q_example"; // String | 
    String within = "within_example"; // String | 
    String withinInclude = "withinInclude_example"; // String | 
    String contains = "contains_example"; // String | 
    BigDecimal maskLength = new BigDecimal(78); // BigDecimal | 
    String vrfId = "vrfId_example"; // String | 
    String vrf = "vrf_example"; // String | 
    String tenantId = "tenantId_example"; // String | 
    String tenant = "tenant_example"; // String | 
    String siteId = "siteId_example"; // String | 
    String site = "site_example"; // String | 
    String vlanId = "vlanId_example"; // String | 
    BigDecimal vlanVid = new BigDecimal(78); // BigDecimal | 
    String roleId = "roleId_example"; // String | 
    String role = "role_example"; // String | 
    String status = "status_example"; // String | 
    String tag = "tag_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      IpamPrefixesList200Response result = apiInstance.ipamPrefixesList(family, isPool, idIn, q, within, withinInclude, contains, maskLength, vrfId, vrf, tenantId, tenant, siteId, site, vlanId, vlanVid, roleId, role, status, tag, limit, offset);
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
| **family** | **String**|  | [optional] |
| **isPool** | **String**|  | [optional] |
| **idIn** | **String**| Multiple values may be separated by commas. | [optional] |
| **q** | **String**|  | [optional] |
| **within** | **String**|  | [optional] |
| **withinInclude** | **String**|  | [optional] |
| **contains** | **String**|  | [optional] |
| **maskLength** | **BigDecimal**|  | [optional] |
| **vrfId** | **String**|  | [optional] |
| **vrf** | **String**|  | [optional] |
| **tenantId** | **String**|  | [optional] |
| **tenant** | **String**|  | [optional] |
| **siteId** | **String**|  | [optional] |
| **site** | **String**|  | [optional] |
| **vlanId** | **String**|  | [optional] |
| **vlanVid** | **BigDecimal**|  | [optional] |
| **roleId** | **String**|  | [optional] |
| **role** | **String**|  | [optional] |
| **status** | **String**|  | [optional] |
| **tag** | **String**|  | [optional] |
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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
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
> IpamRirsList200Response ipamRirsList(name, slug, isPrivate, idIn, limit, offset)





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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    String name = "name_example"; // String | 
    String slug = "slug_example"; // String | 
    String isPrivate = "isPrivate_example"; // String | 
    String idIn = "idIn_example"; // String | Multiple values may be separated by commas.
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      IpamRirsList200Response result = apiInstance.ipamRirsList(name, slug, isPrivate, idIn, limit, offset);
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
| **name** | **String**|  | [optional] |
| **slug** | **String**|  | [optional] |
| **isPrivate** | **String**|  | [optional] |
| **idIn** | **String**| Multiple values may be separated by commas. | [optional] |
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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
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
> IpamRolesList200Response ipamRolesList(name, slug, limit, offset)





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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    String name = "name_example"; // String | 
    String slug = "slug_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      IpamRolesList200Response result = apiInstance.ipamRolesList(name, slug, limit, offset);
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
| **name** | **String**|  | [optional] |
| **slug** | **String**|  | [optional] |
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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
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
> IpamServicesList200Response ipamServicesList(name, protocol, port, q, deviceId, device, virtualMachineId, virtualMachine, tag, limit, offset)





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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    String name = "name_example"; // String | 
    String protocol = "protocol_example"; // String | 
    BigDecimal port = new BigDecimal(78); // BigDecimal | 
    String q = "q_example"; // String | 
    String deviceId = "deviceId_example"; // String | 
    String device = "device_example"; // String | 
    String virtualMachineId = "virtualMachineId_example"; // String | 
    String virtualMachine = "virtualMachine_example"; // String | 
    String tag = "tag_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      IpamServicesList200Response result = apiInstance.ipamServicesList(name, protocol, port, q, deviceId, device, virtualMachineId, virtualMachine, tag, limit, offset);
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
| **name** | **String**|  | [optional] |
| **protocol** | **String**|  | [optional] |
| **port** | **BigDecimal**|  | [optional] |
| **q** | **String**|  | [optional] |
| **deviceId** | **String**|  | [optional] |
| **device** | **String**|  | [optional] |
| **virtualMachineId** | **String**|  | [optional] |
| **virtualMachine** | **String**|  | [optional] |
| **tag** | **String**|  | [optional] |
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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
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
> IpamVlanGroupsList200Response ipamVlanGroupsList(name, slug, siteId, site, limit, offset)





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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    String name = "name_example"; // String | 
    String slug = "slug_example"; // String | 
    String siteId = "siteId_example"; // String | 
    String site = "site_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      IpamVlanGroupsList200Response result = apiInstance.ipamVlanGroupsList(name, slug, siteId, site, limit, offset);
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
| **name** | **String**|  | [optional] |
| **slug** | **String**|  | [optional] |
| **siteId** | **String**|  | [optional] |
| **site** | **String**|  | [optional] |
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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
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
> IpamVlansList200Response ipamVlansList(vid, name, idIn, q, siteId, site, groupId, group, tenantId, tenant, roleId, role, status, tag, limit, offset)





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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    BigDecimal vid = new BigDecimal(78); // BigDecimal | 
    String name = "name_example"; // String | 
    String idIn = "idIn_example"; // String | Multiple values may be separated by commas.
    String q = "q_example"; // String | 
    String siteId = "siteId_example"; // String | 
    String site = "site_example"; // String | 
    String groupId = "groupId_example"; // String | 
    String group = "group_example"; // String | 
    String tenantId = "tenantId_example"; // String | 
    String tenant = "tenant_example"; // String | 
    String roleId = "roleId_example"; // String | 
    String role = "role_example"; // String | 
    String status = "status_example"; // String | 
    String tag = "tag_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      IpamVlansList200Response result = apiInstance.ipamVlansList(vid, name, idIn, q, siteId, site, groupId, group, tenantId, tenant, roleId, role, status, tag, limit, offset);
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
| **vid** | **BigDecimal**|  | [optional] |
| **name** | **String**|  | [optional] |
| **idIn** | **String**| Multiple values may be separated by commas. | [optional] |
| **q** | **String**|  | [optional] |
| **siteId** | **String**|  | [optional] |
| **site** | **String**|  | [optional] |
| **groupId** | **String**|  | [optional] |
| **group** | **String**|  | [optional] |
| **tenantId** | **String**|  | [optional] |
| **tenant** | **String**|  | [optional] |
| **roleId** | **String**|  | [optional] |
| **role** | **String**|  | [optional] |
| **status** | **String**|  | [optional] |
| **tag** | **String**|  | [optional] |
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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
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
> IpamVrfsList200Response ipamVrfsList(name, rd, enforceUnique, idIn, q, tenantId, tenant, tag, limit, offset)





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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IpamApi apiInstance = new IpamApi(defaultClient);
    String name = "name_example"; // String | 
    String rd = "rd_example"; // String | 
    String enforceUnique = "enforceUnique_example"; // String | 
    String idIn = "idIn_example"; // String | Multiple values may be separated by commas.
    String q = "q_example"; // String | 
    String tenantId = "tenantId_example"; // String | 
    String tenant = "tenant_example"; // String | 
    String tag = "tag_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      IpamVrfsList200Response result = apiInstance.ipamVrfsList(name, rd, enforceUnique, idIn, q, tenantId, tenant, tag, limit, offset);
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
| **name** | **String**|  | [optional] |
| **rd** | **String**|  | [optional] |
| **enforceUnique** | **String**|  | [optional] |
| **idIn** | **String**| Multiple values may be separated by commas. | [optional] |
| **q** | **String**|  | [optional] |
| **tenantId** | **String**|  | [optional] |
| **tenant** | **String**|  | [optional] |
| **tag** | **String**|  | [optional] |
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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
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

