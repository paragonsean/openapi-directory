# SnmpSettingsApi

All URIs are relative to *https://api.meraki.com/api/v0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNetworkSnmpSettings**](SnmpSettingsApi.md#getNetworkSnmpSettings) | **GET** /networks/{networkId}/snmpSettings | Return the SNMP settings for a network |
| [**getOrganizationSnmp**](SnmpSettingsApi.md#getOrganizationSnmp) | **GET** /organizations/{organizationId}/snmp | Return the SNMP settings for an organization |


<a id="getNetworkSnmpSettings"></a>
# **getNetworkSnmpSettings**
> Object getNetworkSnmpSettings(networkId)

Return the SNMP settings for a network

Return the SNMP settings for a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnmpSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SnmpSettingsApi apiInstance = new SnmpSettingsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkSnmpSettings(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnmpSettingsApi#getNetworkSnmpSettings");
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

<a id="getOrganizationSnmp"></a>
# **getOrganizationSnmp**
> Object getOrganizationSnmp(organizationId)

Return the SNMP settings for an organization

Return the SNMP settings for an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnmpSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SnmpSettingsApi apiInstance = new SnmpSettingsApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    try {
      Object result = apiInstance.getOrganizationSnmp(organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnmpSettingsApi#getOrganizationSnmp");
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
| **organizationId** | **String**|  | |

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

