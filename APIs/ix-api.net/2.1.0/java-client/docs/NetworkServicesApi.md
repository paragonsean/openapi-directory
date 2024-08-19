# NetworkServicesApi

All URIs are relative to */api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**networkServiceCancellationPolicyRead**](NetworkServicesApi.md#networkServiceCancellationPolicyRead) | **GET** /network-services/{id}/cancellation-policy |  |
| [**networkServiceChangeRequestCreate**](NetworkServicesApi.md#networkServiceChangeRequestCreate) | **POST** /network-services/{id}/change-request |  |
| [**networkServiceChangeRequestDestroy**](NetworkServicesApi.md#networkServiceChangeRequestDestroy) | **DELETE** /network-services/{id}/change-request |  |
| [**networkServiceChangeRequestRead**](NetworkServicesApi.md#networkServiceChangeRequestRead) | **GET** /network-services/{id}/change-request |  |
| [**networkServicesCreate**](NetworkServicesApi.md#networkServicesCreate) | **POST** /network-services |  |
| [**networkServicesDestroy**](NetworkServicesApi.md#networkServicesDestroy) | **DELETE** /network-services/{id} |  |
| [**networkServicesList**](NetworkServicesApi.md#networkServicesList) | **GET** /network-services |  |
| [**networkServicesPartialUpdate**](NetworkServicesApi.md#networkServicesPartialUpdate) | **PATCH** /network-services/{id} |  |
| [**networkServicesRead**](NetworkServicesApi.md#networkServicesRead) | **GET** /network-services/{id} |  |
| [**networkServicesUpdate**](NetworkServicesApi.md#networkServicesUpdate) | **PUT** /network-services/{id} |  |


<a id="networkServiceCancellationPolicyRead"></a>
# **networkServiceCancellationPolicyRead**
> CancellationPolicy networkServiceCancellationPolicyRead(id, decommissionAt)



The cancellation-policy can be queried to answer the questions:  If I cancel my service, *when will it be technically decommissioned*? If I cancel my service, *until what date will I be charged*?  When the query parameter &#x60;decommision_at&#x60; is not provided it will provide the first possible cancellation date and charge period if cancelled at above date.  The granularity of the date field is a day, the start and end of which are to be interpreted by the IXP (some may use UTC, some may use their local time zone).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    NetworkServicesApi apiInstance = new NetworkServicesApi(defaultClient);
    String id = "id_example"; // String | Get by id
    String decommissionAt = "decommissionAt_example"; // String | By providing a date in the format `YYYY-MM-DD` you can query the policy what would happen if you request a decommissioning on this date.
    try {
      CancellationPolicy result = apiInstance.networkServiceCancellationPolicyRead(id, decommissionAt);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkServicesApi#networkServiceCancellationPolicyRead");
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

<a id="networkServiceChangeRequestCreate"></a>
# **networkServiceChangeRequestCreate**
> NetworkServiceChangeRequest networkServiceChangeRequestCreate(id, networkServiceChangeRequest)



Request a change to the network service.  A participant in a network service of type &#x60;p2p_vc&#x60; can issue a change request, expressing a desired change in the capacity. The change is accepted when all sides have configured the network service configs with the new bandwidth. These changes can sometimes require a change of the product offering. The product offering may only differ in regards to bandwidth.  The network service will change it&#39;s state from &#x60;production&#x60; into &#x60;production_change_pending&#x60;.  Only one change request may be issued at a time.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    NetworkServicesApi apiInstance = new NetworkServicesApi(defaultClient);
    String id = "id_example"; // String | Get by id
    NetworkServiceChangeRequest networkServiceChangeRequest = new NetworkServiceChangeRequest(); // NetworkServiceChangeRequest | NetworkServiceChangeRequest
    try {
      NetworkServiceChangeRequest result = apiInstance.networkServiceChangeRequestCreate(id, networkServiceChangeRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkServicesApi#networkServiceChangeRequestCreate");
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
| **networkServiceChangeRequest** | [**NetworkServiceChangeRequest**](NetworkServiceChangeRequest.md)| NetworkServiceChangeRequest | [optional] |

### Return type

[**NetworkServiceChangeRequest**](NetworkServiceChangeRequest.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | NetworkServiceChangeRequest |  -  |
| **400** | ValidationError |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |

<a id="networkServiceChangeRequestDestroy"></a>
# **networkServiceChangeRequestDestroy**
> NetworkServiceChangeRequest networkServiceChangeRequestDestroy(id)



Retract or reject a change to the network service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    NetworkServicesApi apiInstance = new NetworkServicesApi(defaultClient);
    String id = "id_example"; // String | Get by id
    try {
      NetworkServiceChangeRequest result = apiInstance.networkServiceChangeRequestDestroy(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkServicesApi#networkServiceChangeRequestDestroy");
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

[**NetworkServiceChangeRequest**](NetworkServiceChangeRequest.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | NetworkServiceChangeRequest |  -  |
| **400** | UnableToFulfill |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |
| **404** | NotFound |  -  |

<a id="networkServiceChangeRequestRead"></a>
# **networkServiceChangeRequestRead**
> NetworkServiceChangeRequest networkServiceChangeRequestRead(id)



Get the change request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    NetworkServicesApi apiInstance = new NetworkServicesApi(defaultClient);
    String id = "id_example"; // String | Get by id
    try {
      NetworkServiceChangeRequest result = apiInstance.networkServiceChangeRequestRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkServicesApi#networkServiceChangeRequestRead");
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

[**NetworkServiceChangeRequest**](NetworkServiceChangeRequest.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | NetworkServiceChangeRequest |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |
| **404** | NotFound |  -  |

<a id="networkServicesCreate"></a>
# **networkServicesCreate**
> NetworkService networkServicesCreate(networkServiceRequest)



Create a new network service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    NetworkServicesApi apiInstance = new NetworkServicesApi(defaultClient);
    NetworkServiceRequest networkServiceRequest = new NetworkServiceRequest(); // NetworkServiceRequest | Polymorphic Network Service Request
    try {
      NetworkService result = apiInstance.networkServicesCreate(networkServiceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkServicesApi#networkServicesCreate");
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
| **networkServiceRequest** | [**NetworkServiceRequest**](NetworkServiceRequest.md)| Polymorphic Network Service Request | [optional] |

### Return type

[**NetworkService**](NetworkService.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Polymorphic Network Services |  -  |
| **400** | ValidationError |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |

<a id="networkServicesDestroy"></a>
# **networkServicesDestroy**
> NetworkService networkServicesDestroy(id, cancellationRequest)



Request decomissioning of the network service.  The network service will enter the state of &#x60;decommission_requested&#x60;. The request will cascade to related network service and feature configs.  An *optional request body* can be provided to request a specific service termination date.  If no date is given in the request body, it is assumed to be the earliest possible date.  Possible values for &#x60;decommission_at&#x60; can be queried through the &#x60;network_service_cancellation_policy_read&#x60; operation.  The response will contain the dates on which the changes will be effected.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    NetworkServicesApi apiInstance = new NetworkServicesApi(defaultClient);
    String id = "id_example"; // String | Get by id
    CancellationRequest cancellationRequest = new CancellationRequest(); // CancellationRequest | Service Cancellation Request
    try {
      NetworkService result = apiInstance.networkServicesDestroy(id, cancellationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkServicesApi#networkServicesDestroy");
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

[**NetworkService**](NetworkService.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Polymorphic Network Services |  -  |
| **400** | CancellationPolicyError |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |
| **404** | NotFound |  -  |

<a id="networkServicesList"></a>
# **networkServicesList**
> List&lt;NetworkService&gt; networkServicesList(id, state, stateIsNot, managingAccount, consumingAccount, externalRef, type, pop, productOffering)



List available &#x60;NetworkService&#x60;s.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    NetworkServicesApi apiInstance = new NetworkServicesApi(defaultClient);
    List<String> id = Arrays.asList(); // List<String> | Filter by id
    String state = "state_example"; // String | Filter by state
    String stateIsNot = "stateIsNot_example"; // String | Filter by state__is_not
    String managingAccount = "managingAccount_example"; // String | Filter by managing_account
    String consumingAccount = "consumingAccount_example"; // String | Filter by consuming_account
    String externalRef = "externalRef_example"; // String | Filter by external_ref
    String type = "exchange_lan"; // String | Filter by type
    String pop = "pop_example"; // String | Filter by pop
    String productOffering = "productOffering_example"; // String | Filter by product_offering
    try {
      List<NetworkService> result = apiInstance.networkServicesList(id, state, stateIsNot, managingAccount, consumingAccount, externalRef, type, pop, productOffering);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkServicesApi#networkServicesList");
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
| **pop** | **String**| Filter by pop | [optional] |
| **productOffering** | **String**| Filter by product_offering | [optional] |

### Return type

[**List&lt;NetworkService&gt;**](NetworkService.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of: Polymorphic Network Services |  -  |
| **400** | ValidationError |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |

<a id="networkServicesPartialUpdate"></a>
# **networkServicesPartialUpdate**
> NetworkService networkServicesPartialUpdate(id, networkServiceRequestPartial)



Partially update a network service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    NetworkServicesApi apiInstance = new NetworkServicesApi(defaultClient);
    String id = "id_example"; // String | Get by id
    NetworkServiceRequestPartial networkServiceRequestPartial = new NetworkServiceRequestPartial(); // NetworkServiceRequestPartial | Polymorphic Network Service Request
    try {
      NetworkService result = apiInstance.networkServicesPartialUpdate(id, networkServiceRequestPartial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkServicesApi#networkServicesPartialUpdate");
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
| **networkServiceRequestPartial** | [**NetworkServiceRequestPartial**](NetworkServiceRequestPartial.md)| Polymorphic Network Service Request | [optional] |

### Return type

[**NetworkService**](NetworkService.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Polymorphic Network Services |  -  |
| **400** | ValidationError |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |
| **404** | NotFound |  -  |

<a id="networkServicesRead"></a>
# **networkServicesRead**
> NetworkService networkServicesRead(id)



Get a specific &#x60;network-service&#x60; by id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    NetworkServicesApi apiInstance = new NetworkServicesApi(defaultClient);
    String id = "id_example"; // String | Get by id
    try {
      NetworkService result = apiInstance.networkServicesRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkServicesApi#networkServicesRead");
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

[**NetworkService**](NetworkService.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Polymorphic Network Services |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |
| **404** | NotFound |  -  |

<a id="networkServicesUpdate"></a>
# **networkServicesUpdate**
> NetworkService networkServicesUpdate(id, networkServiceRequest)



Update a network service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    NetworkServicesApi apiInstance = new NetworkServicesApi(defaultClient);
    String id = "id_example"; // String | Get by id
    NetworkServiceRequest networkServiceRequest = new NetworkServiceRequest(); // NetworkServiceRequest | Polymorphic Network Service Request
    try {
      NetworkService result = apiInstance.networkServicesUpdate(id, networkServiceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkServicesApi#networkServicesUpdate");
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
| **networkServiceRequest** | [**NetworkServiceRequest**](NetworkServiceRequest.md)| Polymorphic Network Service Request | [optional] |

### Return type

[**NetworkService**](NetworkService.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Polymorphic Network Services |  -  |
| **400** | ValidationError |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |
| **404** | NotFound |  -  |

