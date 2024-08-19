# IpsApi

All URIs are relative to */api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**ipsCreate**](IpsApi.md#ipsCreate) | **POST** /ips |  |
| [**ipsList**](IpsApi.md#ipsList) | **GET** /ips |  |
| [**ipsPartialUpdate**](IpsApi.md#ipsPartialUpdate) | **PATCH** /ips/{id} |  |
| [**ipsRead**](IpsApi.md#ipsRead) | **GET** /ips/{id} |  |
| [**ipsUpdate**](IpsApi.md#ipsUpdate) | **PUT** /ips/{id} |  |


<a id="ipsCreate"></a>
# **ipsCreate**
> IpAddress ipsCreate(ipAddressRequest)



Add an ip host address or network prefix.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    IpsApi apiInstance = new IpsApi(defaultClient);
    IpAddressRequest ipAddressRequest = new IpAddressRequest(); // IpAddressRequest | IP-Address / Prefix allocation Request
    try {
      IpAddress result = apiInstance.ipsCreate(ipAddressRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpsApi#ipsCreate");
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
| **ipAddressRequest** | [**IpAddressRequest**](IpAddressRequest.md)| IP-Address / Prefix allocation Request | [optional] |

### Return type

[**IpAddress**](IpAddress.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | IP-Address |  -  |

<a id="ipsList"></a>
# **ipsList**
> List&lt;IpAddress&gt; ipsList(id, managingAccount, consumingAccount, externalRef, networkService, networkServiceConfig, networkFeature, networkFeatureConfig, version, fqdn, prefixLength, validNotBefore, validNotAfter)



List all ip addresses (and prefixes).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    IpsApi apiInstance = new IpsApi(defaultClient);
    List<String> id = Arrays.asList(); // List<String> | Filter by id
    String managingAccount = "managingAccount_example"; // String | Filter by managing_account
    String consumingAccount = "consumingAccount_example"; // String | Filter by consuming_account
    String externalRef = "externalRef_example"; // String | Filter by external_ref
    String networkService = "networkService_example"; // String | Filter by network_service
    String networkServiceConfig = "networkServiceConfig_example"; // String | Filter by network_service_config
    String networkFeature = "networkFeature_example"; // String | Filter by network_feature
    String networkFeatureConfig = "networkFeatureConfig_example"; // String | Filter by network_feature_config
    Integer version = 56; // Integer | Filter by version
    String fqdn = "fqdn_example"; // String | Filter by fqdn
    Integer prefixLength = 56; // Integer | Filter by prefix_length
    String validNotBefore = "validNotBefore_example"; // String | Filter by valid_not_before
    String validNotAfter = "validNotAfter_example"; // String | Filter by valid_not_after
    try {
      List<IpAddress> result = apiInstance.ipsList(id, managingAccount, consumingAccount, externalRef, networkService, networkServiceConfig, networkFeature, networkFeatureConfig, version, fqdn, prefixLength, validNotBefore, validNotAfter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpsApi#ipsList");
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
| **networkService** | **String**| Filter by network_service | [optional] |
| **networkServiceConfig** | **String**| Filter by network_service_config | [optional] |
| **networkFeature** | **String**| Filter by network_feature | [optional] |
| **networkFeatureConfig** | **String**| Filter by network_feature_config | [optional] |
| **version** | **Integer**| Filter by version | [optional] |
| **fqdn** | **String**| Filter by fqdn | [optional] |
| **prefixLength** | **Integer**| Filter by prefix_length | [optional] |
| **validNotBefore** | **String**| Filter by valid_not_before | [optional] |
| **validNotAfter** | **String**| Filter by valid_not_after | [optional] |

### Return type

[**List&lt;IpAddress&gt;**](IpAddress.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of: IP-Address |  -  |
| **400** | ValidationError |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |

<a id="ipsPartialUpdate"></a>
# **ipsPartialUpdate**
> IpAddress ipsPartialUpdate(id, ipAddressUpdatePartial)



Update parts of an ip address.   As with the &#x60;PUT&#x60; opertaion, IP addresses, where you don&#39;t have update rights, will yield a &#x60;resource access denied&#x60; error when attempting an update.  If the ip address was allocated for you, you might not be able to change anything but the &#x60;fqdn&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    IpsApi apiInstance = new IpsApi(defaultClient);
    String id = "id_example"; // String | Get by id
    IpAddressUpdatePartial ipAddressUpdatePartial = new IpAddressUpdatePartial(); // IpAddressUpdatePartial | IP-Address Update
    try {
      IpAddress result = apiInstance.ipsPartialUpdate(id, ipAddressUpdatePartial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpsApi#ipsPartialUpdate");
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
| **ipAddressUpdatePartial** | [**IpAddressUpdatePartial**](IpAddressUpdatePartial.md)| IP-Address Update | [optional] |

### Return type

[**IpAddress**](IpAddress.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | IP-Address |  -  |
| **400** | ValidationError |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |
| **404** | NotFound |  -  |

<a id="ipsRead"></a>
# **ipsRead**
> IpAddress ipsRead(id)



Get a single ip addresses by it&#39;s id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    IpsApi apiInstance = new IpsApi(defaultClient);
    String id = "id_example"; // String | Get by id
    try {
      IpAddress result = apiInstance.ipsRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpsApi#ipsRead");
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

[**IpAddress**](IpAddress.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | IP-Address |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |
| **404** | NotFound |  -  |

<a id="ipsUpdate"></a>
# **ipsUpdate**
> IpAddress ipsUpdate(id, ipAddressUpdate)



Update an ip address object.  You can only update IP addresses within your current scope. Not all addresses you can read you can update.  If the ip address was allocated for you, you might not be able to change anything but the &#x60;fqdn&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    IpsApi apiInstance = new IpsApi(defaultClient);
    String id = "id_example"; // String | Get by id
    IpAddressUpdate ipAddressUpdate = new IpAddressUpdate(); // IpAddressUpdate | IP-Address Update
    try {
      IpAddress result = apiInstance.ipsUpdate(id, ipAddressUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpsApi#ipsUpdate");
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
| **ipAddressUpdate** | [**IpAddressUpdate**](IpAddressUpdate.md)| IP-Address Update | [optional] |

### Return type

[**IpAddress**](IpAddress.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | IP-Address |  -  |
| **400** | ValidationError |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |
| **404** | NotFound |  -  |

