# NetworkServiceConfigsApi

All URIs are relative to */api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**networkServiceConfigCancellationPolicyRead**](NetworkServiceConfigsApi.md#networkServiceConfigCancellationPolicyRead) | **GET** /network-service-configs/{id}/cancellation-policy |  |
| [**networkServiceConfigsCreate**](NetworkServiceConfigsApi.md#networkServiceConfigsCreate) | **POST** /network-service-configs |  |
| [**networkServiceConfigsDestroy**](NetworkServiceConfigsApi.md#networkServiceConfigsDestroy) | **DELETE** /network-service-configs/{id} |  |
| [**networkServiceConfigsList**](NetworkServiceConfigsApi.md#networkServiceConfigsList) | **GET** /network-service-configs |  |
| [**networkServiceConfigsPartialUpdate**](NetworkServiceConfigsApi.md#networkServiceConfigsPartialUpdate) | **PATCH** /network-service-configs/{id} |  |
| [**networkServiceConfigsRead**](NetworkServiceConfigsApi.md#networkServiceConfigsRead) | **GET** /network-service-configs/{id} |  |
| [**networkServiceConfigsUpdate**](NetworkServiceConfigsApi.md#networkServiceConfigsUpdate) | **PUT** /network-service-configs/{id} |  |


<a id="networkServiceConfigCancellationPolicyRead"></a>
# **networkServiceConfigCancellationPolicyRead**
> CancellationPolicy networkServiceConfigCancellationPolicyRead(id, decommissionAt)



The cancellation-policy can be queried to answer the questions:  If I cancel my subscription, *when will it be technically decommissioned*? If I cancel my subscription, *until what date will I be charged*?  When the query parameter &#x60;decommision_at&#x60; is not provided it will provide the first possible cancellation date and charge period if cancelled at above date.  The granularity of the date field is a day, the start and end of which are to be interpreted by the IXP (some may use UTC, some may use their local time zone).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkServiceConfigsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    NetworkServiceConfigsApi apiInstance = new NetworkServiceConfigsApi(defaultClient);
    String id = "id_example"; // String | Get by id
    String decommissionAt = "decommissionAt_example"; // String | By providing a date in the format `YYYY-MM-DD` you can query the policy what would happen if you request a decommissioning on this date.
    try {
      CancellationPolicy result = apiInstance.networkServiceConfigCancellationPolicyRead(id, decommissionAt);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkServiceConfigsApi#networkServiceConfigCancellationPolicyRead");
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
| **id** | **String**| Get by id | |
| **decommissionAt** | **String**| By providing a date in the format &#x60;YYYY-MM-DD&#x60; you can query the policy what would happen if you request a decommissioning on this date. | [optional] |

### Return type

[**CancellationPolicy**](CancellationPolicy.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Cancellation Policy |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |
| **404** | NotFound |  -  |

<a id="networkServiceConfigsCreate"></a>
# **networkServiceConfigsCreate**
> NetworkServiceConfig networkServiceConfigsCreate(networkServiceConfigRequest)



Create a &#x60;network-service-config&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkServiceConfigsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    NetworkServiceConfigsApi apiInstance = new NetworkServiceConfigsApi(defaultClient);
    NetworkServiceConfigRequest networkServiceConfigRequest = new NetworkServiceConfigRequest(); // NetworkServiceConfigRequest | Polymorhic Network Service Config Request
    try {
      NetworkServiceConfig result = apiInstance.networkServiceConfigsCreate(networkServiceConfigRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkServiceConfigsApi#networkServiceConfigsCreate");
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
| **networkServiceConfigRequest** | [**NetworkServiceConfigRequest**](NetworkServiceConfigRequest.md)| Polymorhic Network Service Config Request | [optional] |

### Return type

[**NetworkServiceConfig**](NetworkServiceConfig.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Polymorphic Network Service Config |  -  |
| **400** | ValidationError |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |

<a id="networkServiceConfigsDestroy"></a>
# **networkServiceConfigsDestroy**
> NetworkServiceConfig networkServiceConfigsDestroy(id, cancellationRequest)



Request decommissioning the network service configuration.  The network service config will assume the state &#x60;decommission_requested&#x60;. This will cascade to related resources like &#x60;network-feature-configs&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkServiceConfigsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    NetworkServiceConfigsApi apiInstance = new NetworkServiceConfigsApi(defaultClient);
    String id = "id_example"; // String | Get by id
    CancellationRequest cancellationRequest = new CancellationRequest(); // CancellationRequest | Service Cancellation Request
    try {
      NetworkServiceConfig result = apiInstance.networkServiceConfigsDestroy(id, cancellationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkServiceConfigsApi#networkServiceConfigsDestroy");
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
| **id** | **String**| Get by id | |
| **cancellationRequest** | [**CancellationRequest**](CancellationRequest.md)| Service Cancellation Request | [optional] |

### Return type

[**NetworkServiceConfig**](NetworkServiceConfig.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Polymorphic Network Service Config |  -  |
| **400** | CancellationPolicyError |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |
| **404** | NotFound |  -  |

<a id="networkServiceConfigsList"></a>
# **networkServiceConfigsList**
> List&lt;NetworkServiceConfig&gt; networkServiceConfigsList(id, state, stateIsNot, managingAccount, consumingAccount, externalRef, type, innerVlan, outerVlan, capacity, networkService, connection, productOffering)



Get all &#x60;network-service-config&#x60;s.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkServiceConfigsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    NetworkServiceConfigsApi apiInstance = new NetworkServiceConfigsApi(defaultClient);
    List<String> id = Arrays.asList(); // List<String> | Filter by id
    String state = "state_example"; // String | Filter by state
    String stateIsNot = "stateIsNot_example"; // String | Filter by state__is_not
    String managingAccount = "managingAccount_example"; // String | Filter by managing_account
    String consumingAccount = "consumingAccount_example"; // String | Filter by consuming_account
    String externalRef = "externalRef_example"; // String | Filter by external_ref
    String type = "exchange_lan"; // String | Filter by type
    Integer innerVlan = 56; // Integer | Filter by inner_vlan
    Integer outerVlan = 56; // Integer | Filter by outer_vlan
    Integer capacity = 56; // Integer | Filter by capacity
    String networkService = "networkService_example"; // String | Filter by network_service
    String connection = "connection_example"; // String | Filter by connection
    String productOffering = "productOffering_example"; // String | Filter by product_offering
    try {
      List<NetworkServiceConfig> result = apiInstance.networkServiceConfigsList(id, state, stateIsNot, managingAccount, consumingAccount, externalRef, type, innerVlan, outerVlan, capacity, networkService, connection, productOffering);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkServiceConfigsApi#networkServiceConfigsList");
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
| **id** | [**List&lt;String&gt;**](String.md)| Filter by id | [optional] |
| **state** | **String**| Filter by state | [optional] |
| **stateIsNot** | **String**| Filter by state__is_not | [optional] |
| **managingAccount** | **String**| Filter by managing_account | [optional] |
| **consumingAccount** | **String**| Filter by consuming_account | [optional] |
| **externalRef** | **String**| Filter by external_ref | [optional] |
| **type** | **String**| Filter by type | [optional] [enum: exchange_lan, p2p_vc, p2mp_vc, mp2mp_vc, cloud_vc] |
| **innerVlan** | **Integer**| Filter by inner_vlan | [optional] |
| **outerVlan** | **Integer**| Filter by outer_vlan | [optional] |
| **capacity** | **Integer**| Filter by capacity | [optional] |
| **networkService** | **String**| Filter by network_service | [optional] |
| **connection** | **String**| Filter by connection | [optional] |
| **productOffering** | **String**| Filter by product_offering | [optional] |

### Return type

[**List&lt;NetworkServiceConfig&gt;**](NetworkServiceConfig.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of: Polymorphic Network Service Config |  -  |
| **400** | ValidationError |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |

<a id="networkServiceConfigsPartialUpdate"></a>
# **networkServiceConfigsPartialUpdate**
> NetworkServiceConfig networkServiceConfigsPartialUpdate(id, networkServiceConfigUpdatePartial)



Update parts of an exisiting &#x60;network-service-config&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkServiceConfigsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    NetworkServiceConfigsApi apiInstance = new NetworkServiceConfigsApi(defaultClient);
    String id = "id_example"; // String | Get by id
    NetworkServiceConfigUpdatePartial networkServiceConfigUpdatePartial = new NetworkServiceConfigUpdatePartial(); // NetworkServiceConfigUpdatePartial | Polymorphic Network Service Config
    try {
      NetworkServiceConfig result = apiInstance.networkServiceConfigsPartialUpdate(id, networkServiceConfigUpdatePartial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkServiceConfigsApi#networkServiceConfigsPartialUpdate");
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
| **id** | **String**| Get by id | |
| **networkServiceConfigUpdatePartial** | [**NetworkServiceConfigUpdatePartial**](NetworkServiceConfigUpdatePartial.md)| Polymorphic Network Service Config | [optional] |

### Return type

[**NetworkServiceConfig**](NetworkServiceConfig.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Polymorphic Network Service Config |  -  |
| **400** | ValidationError |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |
| **404** | NotFound |  -  |

<a id="networkServiceConfigsRead"></a>
# **networkServiceConfigsRead**
> NetworkServiceConfig networkServiceConfigsRead(id)



Get a &#x60;network-service-config&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkServiceConfigsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    NetworkServiceConfigsApi apiInstance = new NetworkServiceConfigsApi(defaultClient);
    String id = "id_example"; // String | Get by id
    try {
      NetworkServiceConfig result = apiInstance.networkServiceConfigsRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkServiceConfigsApi#networkServiceConfigsRead");
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
| **id** | **String**| Get by id | |

### Return type

[**NetworkServiceConfig**](NetworkServiceConfig.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Polymorphic Network Service Config |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |
| **404** | NotFound |  -  |

<a id="networkServiceConfigsUpdate"></a>
# **networkServiceConfigsUpdate**
> NetworkServiceConfig networkServiceConfigsUpdate(id, networkServiceConfigUpdate)



Update an exisiting &#x60;network-service-config&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkServiceConfigsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    NetworkServiceConfigsApi apiInstance = new NetworkServiceConfigsApi(defaultClient);
    String id = "id_example"; // String | Get by id
    NetworkServiceConfigUpdate networkServiceConfigUpdate = new NetworkServiceConfigUpdate(); // NetworkServiceConfigUpdate | Polymorphic Network Service Config
    try {
      NetworkServiceConfig result = apiInstance.networkServiceConfigsUpdate(id, networkServiceConfigUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkServiceConfigsApi#networkServiceConfigsUpdate");
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
| **id** | **String**| Get by id | |
| **networkServiceConfigUpdate** | [**NetworkServiceConfigUpdate**](NetworkServiceConfigUpdate.md)| Polymorphic Network Service Config | [optional] |

### Return type

[**NetworkServiceConfig**](NetworkServiceConfig.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Polymorphic Network Service Config |  -  |
| **400** | ValidationError |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |
| **404** | NotFound |  -  |

