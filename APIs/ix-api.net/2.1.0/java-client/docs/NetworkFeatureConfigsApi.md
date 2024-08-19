# NetworkFeatureConfigsApi

All URIs are relative to */api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**networkFeatureConfigsCreate**](NetworkFeatureConfigsApi.md#networkFeatureConfigsCreate) | **POST** /network-feature-configs |  |
| [**networkFeatureConfigsDestroy**](NetworkFeatureConfigsApi.md#networkFeatureConfigsDestroy) | **DELETE** /network-feature-configs/{id} |  |
| [**networkFeatureConfigsList**](NetworkFeatureConfigsApi.md#networkFeatureConfigsList) | **GET** /network-feature-configs |  |
| [**networkFeatureConfigsPartialUpdate**](NetworkFeatureConfigsApi.md#networkFeatureConfigsPartialUpdate) | **PATCH** /network-feature-configs/{id} |  |
| [**networkFeatureConfigsRead**](NetworkFeatureConfigsApi.md#networkFeatureConfigsRead) | **GET** /network-feature-configs/{id} |  |
| [**networkFeatureConfigsUpdate**](NetworkFeatureConfigsApi.md#networkFeatureConfigsUpdate) | **PUT** /network-feature-configs/{id} |  |


<a id="networkFeatureConfigsCreate"></a>
# **networkFeatureConfigsCreate**
> NetworkFeatureConfig networkFeatureConfigsCreate(networkFeatureConfigRequest)



Create a configuration for a &#x60;NetworkFeature&#x60; defined in the &#x60;NetworkFeature&#x60;s collection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkFeatureConfigsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    NetworkFeatureConfigsApi apiInstance = new NetworkFeatureConfigsApi(defaultClient);
    NetworkFeatureConfigRequest networkFeatureConfigRequest = new NetworkFeatureConfigRequest(); // NetworkFeatureConfigRequest | Polymorphic Network Feature Config Request
    try {
      NetworkFeatureConfig result = apiInstance.networkFeatureConfigsCreate(networkFeatureConfigRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkFeatureConfigsApi#networkFeatureConfigsCreate");
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
| **networkFeatureConfigRequest** | [**NetworkFeatureConfigRequest**](NetworkFeatureConfigRequest.md)| Polymorphic Network Feature Config Request | [optional] |

### Return type

[**NetworkFeatureConfig**](NetworkFeatureConfig.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Polymorphic Network Feature Config |  -  |
| **400** | ValidationError |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |

<a id="networkFeatureConfigsDestroy"></a>
# **networkFeatureConfigsDestroy**
> NetworkFeatureConfig networkFeatureConfigsDestroy(id)



Remove a network feature config.  The network feature config will be marked as &#x60;decommission_requested&#x60;. Decommissioning a network feature config will not cascade to related services or service configs.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkFeatureConfigsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    NetworkFeatureConfigsApi apiInstance = new NetworkFeatureConfigsApi(defaultClient);
    String id = "id_example"; // String | Get by id
    try {
      NetworkFeatureConfig result = apiInstance.networkFeatureConfigsDestroy(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkFeatureConfigsApi#networkFeatureConfigsDestroy");
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

[**NetworkFeatureConfig**](NetworkFeatureConfig.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Polymorphic Network Feature Config |  -  |
| **400** | UnableToFulfill |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |
| **404** | NotFound |  -  |

<a id="networkFeatureConfigsList"></a>
# **networkFeatureConfigsList**
> List&lt;NetworkFeatureConfig&gt; networkFeatureConfigsList(id, state, stateIsNot, managingAccount, consumingAccount, externalRef, type, serviceConfig, networkFeature)



Get all network feature configs.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkFeatureConfigsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    NetworkFeatureConfigsApi apiInstance = new NetworkFeatureConfigsApi(defaultClient);
    List<String> id = Arrays.asList(); // List<String> | Filter by id
    String state = "state_example"; // String | Filter by state
    String stateIsNot = "stateIsNot_example"; // String | Filter by state__is_not
    String managingAccount = "managingAccount_example"; // String | Filter by managing_account
    String consumingAccount = "consumingAccount_example"; // String | Filter by consuming_account
    String externalRef = "externalRef_example"; // String | Filter by external_ref
    String type = "route_server"; // String | Filter by type
    String serviceConfig = "serviceConfig_example"; // String | Filter by service_config
    String networkFeature = "networkFeature_example"; // String | Filter by network_feature
    try {
      List<NetworkFeatureConfig> result = apiInstance.networkFeatureConfigsList(id, state, stateIsNot, managingAccount, consumingAccount, externalRef, type, serviceConfig, networkFeature);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkFeatureConfigsApi#networkFeatureConfigsList");
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
| **type** | **String**| Filter by type | [optional] [enum: route_server] |
| **serviceConfig** | **String**| Filter by service_config | [optional] |
| **networkFeature** | **String**| Filter by network_feature | [optional] |

### Return type

[**List&lt;NetworkFeatureConfig&gt;**](NetworkFeatureConfig.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of: Polymorphic Network Feature Config |  -  |
| **400** | ValidationError |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |

<a id="networkFeatureConfigsPartialUpdate"></a>
# **networkFeatureConfigsPartialUpdate**
> NetworkFeatureConfig networkFeatureConfigsPartialUpdate(id, networkFeatureConfigUpdatePartial)



Update parts of a network feature configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkFeatureConfigsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    NetworkFeatureConfigsApi apiInstance = new NetworkFeatureConfigsApi(defaultClient);
    String id = "id_example"; // String | Get by id
    NetworkFeatureConfigUpdatePartial networkFeatureConfigUpdatePartial = new NetworkFeatureConfigUpdatePartial(); // NetworkFeatureConfigUpdatePartial | Polymorphic Network Feauture Config Update
    try {
      NetworkFeatureConfig result = apiInstance.networkFeatureConfigsPartialUpdate(id, networkFeatureConfigUpdatePartial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkFeatureConfigsApi#networkFeatureConfigsPartialUpdate");
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
| **networkFeatureConfigUpdatePartial** | [**NetworkFeatureConfigUpdatePartial**](NetworkFeatureConfigUpdatePartial.md)| Polymorphic Network Feauture Config Update | [optional] |

### Return type

[**NetworkFeatureConfig**](NetworkFeatureConfig.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Polymorphic Network Feature Config |  -  |
| **400** | ValidationError |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |
| **404** | NotFound |  -  |

<a id="networkFeatureConfigsRead"></a>
# **networkFeatureConfigsRead**
> NetworkFeatureConfig networkFeatureConfigsRead(id)



Get a single network feature config.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkFeatureConfigsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    NetworkFeatureConfigsApi apiInstance = new NetworkFeatureConfigsApi(defaultClient);
    String id = "id_example"; // String | Get by id
    try {
      NetworkFeatureConfig result = apiInstance.networkFeatureConfigsRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkFeatureConfigsApi#networkFeatureConfigsRead");
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

[**NetworkFeatureConfig**](NetworkFeatureConfig.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Polymorphic Network Feature Config |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |
| **404** | NotFound |  -  |

<a id="networkFeatureConfigsUpdate"></a>
# **networkFeatureConfigsUpdate**
> NetworkFeatureConfig networkFeatureConfigsUpdate(id, networkFeatureConfigUpdate)



Update a network feature configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkFeatureConfigsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    NetworkFeatureConfigsApi apiInstance = new NetworkFeatureConfigsApi(defaultClient);
    String id = "id_example"; // String | Get by id
    NetworkFeatureConfigUpdate networkFeatureConfigUpdate = new NetworkFeatureConfigUpdate(); // NetworkFeatureConfigUpdate | Polymorphic Network Feauture Config Update
    try {
      NetworkFeatureConfig result = apiInstance.networkFeatureConfigsUpdate(id, networkFeatureConfigUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkFeatureConfigsApi#networkFeatureConfigsUpdate");
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
| **networkFeatureConfigUpdate** | [**NetworkFeatureConfigUpdate**](NetworkFeatureConfigUpdate.md)| Polymorphic Network Feauture Config Update | [optional] |

### Return type

[**NetworkFeatureConfig**](NetworkFeatureConfig.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Polymorphic Network Feature Config |  -  |
| **400** | ValidationError |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |
| **404** | NotFound |  -  |

