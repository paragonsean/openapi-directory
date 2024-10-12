# PiiApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createNetworkPiiRequest_1**](PiiApi.md#createNetworkPiiRequest_1) | **POST** /networks/{networkId}/pii/requests | Submit a new delete or restrict processing PII request |
| [**deleteNetworkPiiRequest_1**](PiiApi.md#deleteNetworkPiiRequest_1) | **DELETE** /networks/{networkId}/pii/requests/{requestId} | Delete a restrict processing PII request |
| [**getNetworkPiiPiiKeys_1**](PiiApi.md#getNetworkPiiPiiKeys_1) | **GET** /networks/{networkId}/pii/piiKeys | List the keys required to access Personally Identifiable Information (PII) for a given identifier |
| [**getNetworkPiiRequest_1**](PiiApi.md#getNetworkPiiRequest_1) | **GET** /networks/{networkId}/pii/requests/{requestId} | Return a PII request |
| [**getNetworkPiiRequests_1**](PiiApi.md#getNetworkPiiRequests_1) | **GET** /networks/{networkId}/pii/requests | List the PII requests for this network or organization |
| [**getNetworkPiiSmDevicesForKey_1**](PiiApi.md#getNetworkPiiSmDevicesForKey_1) | **GET** /networks/{networkId}/pii/smDevicesForKey | Given a piece of Personally Identifiable Information (PII), return the Systems Manager device ID(s) associated with that identifier |
| [**getNetworkPiiSmOwnersForKey_1**](PiiApi.md#getNetworkPiiSmOwnersForKey_1) | **GET** /networks/{networkId}/pii/smOwnersForKey | Given a piece of Personally Identifiable Information (PII), return the Systems Manager owner ID(s) associated with that identifier |


<a id="createNetworkPiiRequest_1"></a>
# **createNetworkPiiRequest_1**
> Object createNetworkPiiRequest_1(networkId, createNetworkPiiRequestRequest)

Submit a new delete or restrict processing PII request

Submit a new delete or restrict processing PII request  ## ALTERNATE PATH  &#x60;&#x60;&#x60; /organizations/{organizationId}/pii/requests &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PiiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    PiiApi apiInstance = new PiiApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkPiiRequestRequest createNetworkPiiRequestRequest = new CreateNetworkPiiRequestRequest(); // CreateNetworkPiiRequestRequest | 
    try {
      Object result = apiInstance.createNetworkPiiRequest_1(networkId, createNetworkPiiRequestRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PiiApi#createNetworkPiiRequest_1");
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
| **networkId** | **String**|  | |
| **createNetworkPiiRequestRequest** | [**CreateNetworkPiiRequestRequest**](CreateNetworkPiiRequestRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |

<a id="deleteNetworkPiiRequest_1"></a>
# **deleteNetworkPiiRequest_1**
> deleteNetworkPiiRequest_1(networkId, requestId)

Delete a restrict processing PII request

Delete a restrict processing PII request  ## ALTERNATE PATH  &#x60;&#x60;&#x60; /organizations/{organizationId}/pii/requests/{requestId} &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PiiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    PiiApi apiInstance = new PiiApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String requestId = "requestId_example"; // String | 
    try {
      apiInstance.deleteNetworkPiiRequest_1(networkId, requestId);
    } catch (ApiException e) {
      System.err.println("Exception when calling PiiApi#deleteNetworkPiiRequest_1");
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
| **networkId** | **String**|  | |
| **requestId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful operation |  -  |

<a id="getNetworkPiiPiiKeys_1"></a>
# **getNetworkPiiPiiKeys_1**
> Object getNetworkPiiPiiKeys_1(networkId, username, email, mac, serial, imei, bluetoothMac)

List the keys required to access Personally Identifiable Information (PII) for a given identifier

List the keys required to access Personally Identifiable Information (PII) for a given identifier. Exactly one identifier will be accepted. If the organization contains org-wide Systems Manager users matching the key provided then there will be an entry with the key \&quot;0\&quot; containing the applicable keys.  ## ALTERNATE PATH  &#x60;&#x60;&#x60; /organizations/{organizationId}/pii/piiKeys &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PiiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    PiiApi apiInstance = new PiiApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String username = "username_example"; // String | The username of a Systems Manager user
    String email = "email_example"; // String | The email of a network user account or a Systems Manager device
    String mac = "mac_example"; // String | The MAC of a network client device or a Systems Manager device
    String serial = "serial_example"; // String | The serial of a Systems Manager device
    String imei = "imei_example"; // String | The IMEI of a Systems Manager device
    String bluetoothMac = "bluetoothMac_example"; // String | The MAC of a Bluetooth client
    try {
      Object result = apiInstance.getNetworkPiiPiiKeys_1(networkId, username, email, mac, serial, imei, bluetoothMac);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PiiApi#getNetworkPiiPiiKeys_1");
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
| **networkId** | **String**|  | |
| **username** | **String**| The username of a Systems Manager user | [optional] |
| **email** | **String**| The email of a network user account or a Systems Manager device | [optional] |
| **mac** | **String**| The MAC of a network client device or a Systems Manager device | [optional] |
| **serial** | **String**| The serial of a Systems Manager device | [optional] |
| **imei** | **String**| The IMEI of a Systems Manager device | [optional] |
| **bluetoothMac** | **String**| The MAC of a Bluetooth client | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkPiiRequest_1"></a>
# **getNetworkPiiRequest_1**
> Object getNetworkPiiRequest_1(networkId, requestId)

Return a PII request

Return a PII request  ## ALTERNATE PATH  &#x60;&#x60;&#x60; /organizations/{organizationId}/pii/requests/{requestId} &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PiiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    PiiApi apiInstance = new PiiApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String requestId = "requestId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkPiiRequest_1(networkId, requestId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PiiApi#getNetworkPiiRequest_1");
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
| **networkId** | **String**|  | |
| **requestId** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkPiiRequests_1"></a>
# **getNetworkPiiRequests_1**
> List&lt;Object&gt; getNetworkPiiRequests_1(networkId)

List the PII requests for this network or organization

List the PII requests for this network or organization  ## ALTERNATE PATH  &#x60;&#x60;&#x60; /organizations/{organizationId}/pii/requests &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PiiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    PiiApi apiInstance = new PiiApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<Object> result = apiInstance.getNetworkPiiRequests_1(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PiiApi#getNetworkPiiRequests_1");
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
| **networkId** | **String**|  | |

### Return type

**List&lt;Object&gt;**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkPiiSmDevicesForKey_1"></a>
# **getNetworkPiiSmDevicesForKey_1**
> Object getNetworkPiiSmDevicesForKey_1(networkId, username, email, mac, serial, imei, bluetoothMac)

Given a piece of Personally Identifiable Information (PII), return the Systems Manager device ID(s) associated with that identifier

Given a piece of Personally Identifiable Information (PII), return the Systems Manager device ID(s) associated with that identifier. These device IDs can be used with the Systems Manager API endpoints to retrieve device details. Exactly one identifier will be accepted.  ## ALTERNATE PATH  &#x60;&#x60;&#x60; /organizations/{organizationId}/pii/smDevicesForKey &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PiiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    PiiApi apiInstance = new PiiApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String username = "username_example"; // String | The username of a Systems Manager user
    String email = "email_example"; // String | The email of a network user account or a Systems Manager device
    String mac = "mac_example"; // String | The MAC of a network client device or a Systems Manager device
    String serial = "serial_example"; // String | The serial of a Systems Manager device
    String imei = "imei_example"; // String | The IMEI of a Systems Manager device
    String bluetoothMac = "bluetoothMac_example"; // String | The MAC of a Bluetooth client
    try {
      Object result = apiInstance.getNetworkPiiSmDevicesForKey_1(networkId, username, email, mac, serial, imei, bluetoothMac);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PiiApi#getNetworkPiiSmDevicesForKey_1");
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
| **networkId** | **String**|  | |
| **username** | **String**| The username of a Systems Manager user | [optional] |
| **email** | **String**| The email of a network user account or a Systems Manager device | [optional] |
| **mac** | **String**| The MAC of a network client device or a Systems Manager device | [optional] |
| **serial** | **String**| The serial of a Systems Manager device | [optional] |
| **imei** | **String**| The IMEI of a Systems Manager device | [optional] |
| **bluetoothMac** | **String**| The MAC of a Bluetooth client | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkPiiSmOwnersForKey_1"></a>
# **getNetworkPiiSmOwnersForKey_1**
> Object getNetworkPiiSmOwnersForKey_1(networkId, username, email, mac, serial, imei, bluetoothMac)

Given a piece of Personally Identifiable Information (PII), return the Systems Manager owner ID(s) associated with that identifier

Given a piece of Personally Identifiable Information (PII), return the Systems Manager owner ID(s) associated with that identifier. These owner IDs can be used with the Systems Manager API endpoints to retrieve owner details. Exactly one identifier will be accepted.  ## ALTERNATE PATH  &#x60;&#x60;&#x60; /organizations/{organizationId}/pii/smOwnersForKey &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PiiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    PiiApi apiInstance = new PiiApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String username = "username_example"; // String | The username of a Systems Manager user
    String email = "email_example"; // String | The email of a network user account or a Systems Manager device
    String mac = "mac_example"; // String | The MAC of a network client device or a Systems Manager device
    String serial = "serial_example"; // String | The serial of a Systems Manager device
    String imei = "imei_example"; // String | The IMEI of a Systems Manager device
    String bluetoothMac = "bluetoothMac_example"; // String | The MAC of a Bluetooth client
    try {
      Object result = apiInstance.getNetworkPiiSmOwnersForKey_1(networkId, username, email, mac, serial, imei, bluetoothMac);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PiiApi#getNetworkPiiSmOwnersForKey_1");
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
| **networkId** | **String**|  | |
| **username** | **String**| The username of a Systems Manager user | [optional] |
| **email** | **String**| The email of a network user account or a Systems Manager device | [optional] |
| **mac** | **String**| The MAC of a network client device or a Systems Manager device | [optional] |
| **serial** | **String**| The serial of a Systems Manager device | [optional] |
| **imei** | **String**| The IMEI of a Systems Manager device | [optional] |
| **bluetoothMac** | **String**| The MAC of a Bluetooth client | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

