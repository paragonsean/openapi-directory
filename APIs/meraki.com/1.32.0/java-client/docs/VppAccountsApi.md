# VppAccountsApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getOrganizationSmVppAccount_1**](VppAccountsApi.md#getOrganizationSmVppAccount_1) | **GET** /organizations/{organizationId}/sm/vppAccounts/{vppAccountId} | Get a hash containing the unparsed token of the VPP account with the given ID |
| [**getOrganizationSmVppAccounts_1**](VppAccountsApi.md#getOrganizationSmVppAccounts_1) | **GET** /organizations/{organizationId}/sm/vppAccounts | List the VPP accounts in the organization |


<a id="getOrganizationSmVppAccount_1"></a>
# **getOrganizationSmVppAccount_1**
> GetOrganizationSmVppAccounts200ResponseInner getOrganizationSmVppAccount_1(organizationId, vppAccountId)

Get a hash containing the unparsed token of the VPP account with the given ID

Get a hash containing the unparsed token of the VPP account with the given ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VppAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    VppAccountsApi apiInstance = new VppAccountsApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String vppAccountId = "vppAccountId_example"; // String | 
    try {
      GetOrganizationSmVppAccounts200ResponseInner result = apiInstance.getOrganizationSmVppAccount_1(organizationId, vppAccountId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VppAccountsApi#getOrganizationSmVppAccount_1");
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
| **vppAccountId** | **String**|  | |

### Return type

[**GetOrganizationSmVppAccounts200ResponseInner**](GetOrganizationSmVppAccounts200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getOrganizationSmVppAccounts_1"></a>
# **getOrganizationSmVppAccounts_1**
> List&lt;GetOrganizationSmVppAccounts200ResponseInner&gt; getOrganizationSmVppAccounts_1(organizationId)

List the VPP accounts in the organization

List the VPP accounts in the organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VppAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    VppAccountsApi apiInstance = new VppAccountsApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    try {
      List<GetOrganizationSmVppAccounts200ResponseInner> result = apiInstance.getOrganizationSmVppAccounts_1(organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VppAccountsApi#getOrganizationSmVppAccounts_1");
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

[**List&lt;GetOrganizationSmVppAccounts200ResponseInner&gt;**](GetOrganizationSmVppAccounts200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

