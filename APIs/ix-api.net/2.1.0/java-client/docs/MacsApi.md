# MacsApi

All URIs are relative to */api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**macsCreate**](MacsApi.md#macsCreate) | **POST** /macs |  |
| [**macsDestroy**](MacsApi.md#macsDestroy) | **DELETE** /macs/{id} |  |
| [**macsList**](MacsApi.md#macsList) | **GET** /macs |  |
| [**macsRead**](MacsApi.md#macsRead) | **GET** /macs/{id} |  |


<a id="macsCreate"></a>
# **macsCreate**
> MacAddress macsCreate(macAddressRequest)



Register a mac address.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MacsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    MacsApi apiInstance = new MacsApi(defaultClient);
    MacAddressRequest macAddressRequest = new MacAddressRequest(); // MacAddressRequest | MAC-Address Request
    try {
      MacAddress result = apiInstance.macsCreate(macAddressRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MacsApi#macsCreate");
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
| **macAddressRequest** | [**MacAddressRequest**](MacAddressRequest.md)| MAC-Address Request | [optional] |

### Return type

[**MacAddress**](MacAddress.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | MAC-Address |  -  |
| **400** | ValidationError |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |

<a id="macsDestroy"></a>
# **macsDestroy**
> MacAddress macsDestroy(id)



Remove a mac address.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MacsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    MacsApi apiInstance = new MacsApi(defaultClient);
    String id = "id_example"; // String | Get by id
    try {
      MacAddress result = apiInstance.macsDestroy(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MacsApi#macsDestroy");
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

[**MacAddress**](MacAddress.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | MAC-Address |  -  |
| **400** | UnableToFulfill |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |
| **404** | NotFound |  -  |

<a id="macsList"></a>
# **macsList**
> List&lt;MacAddress&gt; macsList(id, managingAccount, consumingAccount, externalRef, networkServiceConfig, address, assignedAt, validNotBefore, validNotAfter)



List all mac addresses managed by the authorized customer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MacsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    MacsApi apiInstance = new MacsApi(defaultClient);
    List<String> id = Arrays.asList(); // List<String> | Filter by id
    String managingAccount = "managingAccount_example"; // String | Filter by managing_account
    String consumingAccount = "consumingAccount_example"; // String | Filter by consuming_account
    String externalRef = "externalRef_example"; // String | Filter by external_ref
    String networkServiceConfig = "networkServiceConfig_example"; // String | Filter by network_service_config
    String address = "address_example"; // String | Filter by address
    String assignedAt = "assignedAt_example"; // String | Filter by assigned_at
    String validNotBefore = "validNotBefore_example"; // String | Filter by valid_not_before
    String validNotAfter = "validNotAfter_example"; // String | Filter by valid_not_after
    try {
      List<MacAddress> result = apiInstance.macsList(id, managingAccount, consumingAccount, externalRef, networkServiceConfig, address, assignedAt, validNotBefore, validNotAfter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MacsApi#macsList");
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
| **managingAccount** | **String**| Filter by managing_account | [optional] |
| **consumingAccount** | **String**| Filter by consuming_account | [optional] |
| **externalRef** | **String**| Filter by external_ref | [optional] |
| **networkServiceConfig** | **String**| Filter by network_service_config | [optional] |
| **address** | **String**| Filter by address | [optional] |
| **assignedAt** | **String**| Filter by assigned_at | [optional] |
| **validNotBefore** | **String**| Filter by valid_not_before | [optional] |
| **validNotAfter** | **String**| Filter by valid_not_after | [optional] |

### Return type

[**List&lt;MacAddress&gt;**](MacAddress.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of: MAC-Address |  -  |
| **400** | ValidationError |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |

<a id="macsRead"></a>
# **macsRead**
> MacAddress macsRead(id)



Get a single mac address by it&#39;s id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MacsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    MacsApi apiInstance = new MacsApi(defaultClient);
    String id = "id_example"; // String | Get by id
    try {
      MacAddress result = apiInstance.macsRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MacsApi#macsRead");
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

[**MacAddress**](MacAddress.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | MAC-Address |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |
| **404** | NotFound |  -  |

