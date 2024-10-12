# UpgradesApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getOrganizationFirmwareUpgradesByDevice_2**](UpgradesApi.md#getOrganizationFirmwareUpgradesByDevice_2) | **GET** /organizations/{organizationId}/firmware/upgrades/byDevice | Get firmware upgrade status for the filtered devices |
| [**getOrganizationFirmwareUpgrades_2**](UpgradesApi.md#getOrganizationFirmwareUpgrades_2) | **GET** /organizations/{organizationId}/firmware/upgrades | Get firmware upgrade information for an organization |


<a id="getOrganizationFirmwareUpgradesByDevice_2"></a>
# **getOrganizationFirmwareUpgradesByDevice_2**
> List&lt;GetOrganizationFirmwareUpgradesByDevice200ResponseInner&gt; getOrganizationFirmwareUpgradesByDevice_2(organizationId, perPage, startingAfter, endingBefore, networkIds, serials, macs, firmwareUpgradeIds, firmwareUpgradeBatchIds)

Get firmware upgrade status for the filtered devices

Get firmware upgrade status for the filtered devices

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UpgradesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    UpgradesApi apiInstance = new UpgradesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 50. Default is 50.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    List<String> networkIds = Arrays.asList(); // List<String> | Optional parameter to filter by network
    List<String> serials = Arrays.asList(); // List<String> | Optional parameter to filter by serial number.  All returned devices will have a serial number that is an exact match.
    List<String> macs = Arrays.asList(); // List<String> | Optional parameter to filter by one or more MAC addresses belonging to devices. All devices returned belong to MAC addresses that are an exact match.
    List<String> firmwareUpgradeIds = Arrays.asList(); // List<String> | Optional parameter to filter by firmware upgrade ids.
    List<String> firmwareUpgradeBatchIds = Arrays.asList(); // List<String> | Optional parameter to filter by firmware upgrade batch ids.
    try {
      List<GetOrganizationFirmwareUpgradesByDevice200ResponseInner> result = apiInstance.getOrganizationFirmwareUpgradesByDevice_2(organizationId, perPage, startingAfter, endingBefore, networkIds, serials, macs, firmwareUpgradeIds, firmwareUpgradeBatchIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UpgradesApi#getOrganizationFirmwareUpgradesByDevice_2");
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
| **perPage** | **Integer**| The number of entries per page returned. Acceptable range is 3 - 50. Default is 50. | [optional] |
| **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **networkIds** | [**List&lt;String&gt;**](String.md)| Optional parameter to filter by network | [optional] |
| **serials** | [**List&lt;String&gt;**](String.md)| Optional parameter to filter by serial number.  All returned devices will have a serial number that is an exact match. | [optional] |
| **macs** | [**List&lt;String&gt;**](String.md)| Optional parameter to filter by one or more MAC addresses belonging to devices. All devices returned belong to MAC addresses that are an exact match. | [optional] |
| **firmwareUpgradeIds** | [**List&lt;String&gt;**](String.md)| Optional parameter to filter by firmware upgrade ids. | [optional] |
| **firmwareUpgradeBatchIds** | [**List&lt;String&gt;**](String.md)| Optional parameter to filter by firmware upgrade batch ids. | [optional] |

### Return type

[**List&lt;GetOrganizationFirmwareUpgradesByDevice200ResponseInner&gt;**](GetOrganizationFirmwareUpgradesByDevice200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

<a id="getOrganizationFirmwareUpgrades_2"></a>
# **getOrganizationFirmwareUpgrades_2**
> List&lt;GetOrganizationFirmwareUpgrades200ResponseInner&gt; getOrganizationFirmwareUpgrades_2(organizationId, status, productType)

Get firmware upgrade information for an organization

Get firmware upgrade information for an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UpgradesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    UpgradesApi apiInstance = new UpgradesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    List<String> status = Arrays.asList(); // List<String> | The status of an upgrade 
    List<String> productType = Arrays.asList(); // List<String> | The product type in a given upgrade ID
    try {
      List<GetOrganizationFirmwareUpgrades200ResponseInner> result = apiInstance.getOrganizationFirmwareUpgrades_2(organizationId, status, productType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UpgradesApi#getOrganizationFirmwareUpgrades_2");
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
| **status** | [**List&lt;String&gt;**](String.md)| The status of an upgrade  | [optional] |
| **productType** | [**List&lt;String&gt;**](String.md)| The product type in a given upgrade ID | [optional] |

### Return type

[**List&lt;GetOrganizationFirmwareUpgrades200ResponseInner&gt;**](GetOrganizationFirmwareUpgrades200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

