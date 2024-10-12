# IdentityPsksApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createNetworkWirelessSsidIdentityPsk_2**](IdentityPsksApi.md#createNetworkWirelessSsidIdentityPsk_2) | **POST** /networks/{networkId}/wireless/ssids/{number}/identityPsks | Create an Identity PSK |
| [**deleteNetworkWirelessSsidIdentityPsk_2**](IdentityPsksApi.md#deleteNetworkWirelessSsidIdentityPsk_2) | **DELETE** /networks/{networkId}/wireless/ssids/{number}/identityPsks/{identityPskId} | Delete an Identity PSK |
| [**getNetworkWirelessSsidIdentityPsk_2**](IdentityPsksApi.md#getNetworkWirelessSsidIdentityPsk_2) | **GET** /networks/{networkId}/wireless/ssids/{number}/identityPsks/{identityPskId} | Return an Identity PSK |
| [**getNetworkWirelessSsidIdentityPsks_2**](IdentityPsksApi.md#getNetworkWirelessSsidIdentityPsks_2) | **GET** /networks/{networkId}/wireless/ssids/{number}/identityPsks | List all Identity PSKs in a wireless network |
| [**updateNetworkWirelessSsidIdentityPsk_2**](IdentityPsksApi.md#updateNetworkWirelessSsidIdentityPsk_2) | **PUT** /networks/{networkId}/wireless/ssids/{number}/identityPsks/{identityPskId} | Update an Identity PSK |


<a id="createNetworkWirelessSsidIdentityPsk_2"></a>
# **createNetworkWirelessSsidIdentityPsk_2**
> Object createNetworkWirelessSsidIdentityPsk_2(networkId, number, createNetworkWirelessSsidIdentityPskRequest)

Create an Identity PSK

Create an Identity PSK

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdentityPsksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    IdentityPsksApi apiInstance = new IdentityPsksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    CreateNetworkWirelessSsidIdentityPskRequest createNetworkWirelessSsidIdentityPskRequest = new CreateNetworkWirelessSsidIdentityPskRequest(); // CreateNetworkWirelessSsidIdentityPskRequest | 
    try {
      Object result = apiInstance.createNetworkWirelessSsidIdentityPsk_2(networkId, number, createNetworkWirelessSsidIdentityPskRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdentityPsksApi#createNetworkWirelessSsidIdentityPsk_2");
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
| **number** | **String**|  | |
| **createNetworkWirelessSsidIdentityPskRequest** | [**CreateNetworkWirelessSsidIdentityPskRequest**](CreateNetworkWirelessSsidIdentityPskRequest.md)|  | |

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

<a id="deleteNetworkWirelessSsidIdentityPsk_2"></a>
# **deleteNetworkWirelessSsidIdentityPsk_2**
> deleteNetworkWirelessSsidIdentityPsk_2(networkId, number, identityPskId)

Delete an Identity PSK

Delete an Identity PSK

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdentityPsksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    IdentityPsksApi apiInstance = new IdentityPsksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    String identityPskId = "identityPskId_example"; // String | 
    try {
      apiInstance.deleteNetworkWirelessSsidIdentityPsk_2(networkId, number, identityPskId);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdentityPsksApi#deleteNetworkWirelessSsidIdentityPsk_2");
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
| **number** | **String**|  | |
| **identityPskId** | **String**|  | |

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

<a id="getNetworkWirelessSsidIdentityPsk_2"></a>
# **getNetworkWirelessSsidIdentityPsk_2**
> GetNetworkWirelessSsidIdentityPsks200ResponseInner getNetworkWirelessSsidIdentityPsk_2(networkId, number, identityPskId)

Return an Identity PSK

Return an Identity PSK

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdentityPsksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    IdentityPsksApi apiInstance = new IdentityPsksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    String identityPskId = "identityPskId_example"; // String | 
    try {
      GetNetworkWirelessSsidIdentityPsks200ResponseInner result = apiInstance.getNetworkWirelessSsidIdentityPsk_2(networkId, number, identityPskId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdentityPsksApi#getNetworkWirelessSsidIdentityPsk_2");
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
| **number** | **String**|  | |
| **identityPskId** | **String**|  | |

### Return type

[**GetNetworkWirelessSsidIdentityPsks200ResponseInner**](GetNetworkWirelessSsidIdentityPsks200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkWirelessSsidIdentityPsks_2"></a>
# **getNetworkWirelessSsidIdentityPsks_2**
> List&lt;GetNetworkWirelessSsidIdentityPsks200ResponseInner&gt; getNetworkWirelessSsidIdentityPsks_2(networkId, number)

List all Identity PSKs in a wireless network

List all Identity PSKs in a wireless network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdentityPsksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    IdentityPsksApi apiInstance = new IdentityPsksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    try {
      List<GetNetworkWirelessSsidIdentityPsks200ResponseInner> result = apiInstance.getNetworkWirelessSsidIdentityPsks_2(networkId, number);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdentityPsksApi#getNetworkWirelessSsidIdentityPsks_2");
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
| **number** | **String**|  | |

### Return type

[**List&lt;GetNetworkWirelessSsidIdentityPsks200ResponseInner&gt;**](GetNetworkWirelessSsidIdentityPsks200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkWirelessSsidIdentityPsk_2"></a>
# **updateNetworkWirelessSsidIdentityPsk_2**
> Object updateNetworkWirelessSsidIdentityPsk_2(networkId, number, identityPskId, updateNetworkWirelessSsidIdentityPskRequest)

Update an Identity PSK

Update an Identity PSK

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdentityPsksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    IdentityPsksApi apiInstance = new IdentityPsksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    String identityPskId = "identityPskId_example"; // String | 
    UpdateNetworkWirelessSsidIdentityPskRequest updateNetworkWirelessSsidIdentityPskRequest = new UpdateNetworkWirelessSsidIdentityPskRequest(); // UpdateNetworkWirelessSsidIdentityPskRequest | 
    try {
      Object result = apiInstance.updateNetworkWirelessSsidIdentityPsk_2(networkId, number, identityPskId, updateNetworkWirelessSsidIdentityPskRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdentityPsksApi#updateNetworkWirelessSsidIdentityPsk_2");
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
| **number** | **String**|  | |
| **identityPskId** | **String**|  | |
| **updateNetworkWirelessSsidIdentityPskRequest** | [**UpdateNetworkWirelessSsidIdentityPskRequest**](UpdateNetworkWirelessSsidIdentityPskRequest.md)|  | [optional] |

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
| **200** | Successful operation |  -  |

