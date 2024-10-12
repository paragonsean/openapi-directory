# PiiKeysApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNetworkPiiPiiKeys_2**](PiiKeysApi.md#getNetworkPiiPiiKeys_2) | **GET** /networks/{networkId}/pii/piiKeys | List the keys required to access Personally Identifiable Information (PII) for a given identifier |


<a id="getNetworkPiiPiiKeys_2"></a>
# **getNetworkPiiPiiKeys_2**
> Object getNetworkPiiPiiKeys_2(networkId, username, email, mac, serial, imei, bluetoothMac)

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
import org.openapitools.client.api.PiiKeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    PiiKeysApi apiInstance = new PiiKeysApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String username = "username_example"; // String | The username of a Systems Manager user
    String email = "email_example"; // String | The email of a network user account or a Systems Manager device
    String mac = "mac_example"; // String | The MAC of a network client device or a Systems Manager device
    String serial = "serial_example"; // String | The serial of a Systems Manager device
    String imei = "imei_example"; // String | The IMEI of a Systems Manager device
    String bluetoothMac = "bluetoothMac_example"; // String | The MAC of a Bluetooth client
    try {
      Object result = apiInstance.getNetworkPiiPiiKeys_2(networkId, username, email, mac, serial, imei, bluetoothMac);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PiiKeysApi#getNetworkPiiPiiKeys_2");
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

