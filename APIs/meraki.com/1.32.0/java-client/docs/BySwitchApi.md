# BySwitchApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getOrganizationSwitchPortsBySwitch_2**](BySwitchApi.md#getOrganizationSwitchPortsBySwitch_2) | **GET** /organizations/{organizationId}/switch/ports/bySwitch | List the switchports in an organization by switch |


<a id="getOrganizationSwitchPortsBySwitch_2"></a>
# **getOrganizationSwitchPortsBySwitch_2**
> List&lt;GetOrganizationSwitchPortsBySwitch200ResponseInner&gt; getOrganizationSwitchPortsBySwitch_2(organizationId, perPage, startingAfter, endingBefore, networkIds, portProfileIds, name, mac, macs, serial, serials, configurationUpdatedAfter)

List the switchports in an organization by switch

List the switchports in an organization by switch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BySwitchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    BySwitchApi apiInstance = new BySwitchApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 50. Default is 50.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    List<String> networkIds = Arrays.asList(); // List<String> | Optional parameter to filter switchports by network.
    List<String> portProfileIds = Arrays.asList(); // List<String> | Optional parameter to filter switchports belonging to the specified switchport profiles.
    String name = "name_example"; // String | Optional parameter to filter switchports belonging to switches by name. All returned switches will have a name that contains the search term or is an exact match.
    String mac = "mac_example"; // String | Optional parameter to filter switchports belonging to switches by MAC address. All returned switches will have a MAC address that contains the search term or is an exact match.
    List<String> macs = Arrays.asList(); // List<String> | Optional parameter to filter switchports by one or more MAC addresses belonging to devices. All switchports returned belong to MAC addresses of switches that are an exact match.
    String serial = "serial_example"; // String | Optional parameter to filter switchports belonging to switches by serial number. All returned switches will have a serial number that contains the search term or is an exact match.
    List<String> serials = Arrays.asList(); // List<String> | Optional parameter to filter switchports belonging to switches with one or more serial numbers. All switchports returned belong to serial numbers of switches that are an exact match.
    String configurationUpdatedAfter = "configurationUpdatedAfter_example"; // String | Optional parameter to filter results by switches where the configuration has been updated after the given timestamp.
    try {
      List<GetOrganizationSwitchPortsBySwitch200ResponseInner> result = apiInstance.getOrganizationSwitchPortsBySwitch_2(organizationId, perPage, startingAfter, endingBefore, networkIds, portProfileIds, name, mac, macs, serial, serials, configurationUpdatedAfter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BySwitchApi#getOrganizationSwitchPortsBySwitch_2");
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
| **networkIds** | [**List&lt;String&gt;**](String.md)| Optional parameter to filter switchports by network. | [optional] |
| **portProfileIds** | [**List&lt;String&gt;**](String.md)| Optional parameter to filter switchports belonging to the specified switchport profiles. | [optional] |
| **name** | **String**| Optional parameter to filter switchports belonging to switches by name. All returned switches will have a name that contains the search term or is an exact match. | [optional] |
| **mac** | **String**| Optional parameter to filter switchports belonging to switches by MAC address. All returned switches will have a MAC address that contains the search term or is an exact match. | [optional] |
| **macs** | [**List&lt;String&gt;**](String.md)| Optional parameter to filter switchports by one or more MAC addresses belonging to devices. All switchports returned belong to MAC addresses of switches that are an exact match. | [optional] |
| **serial** | **String**| Optional parameter to filter switchports belonging to switches by serial number. All returned switches will have a serial number that contains the search term or is an exact match. | [optional] |
| **serials** | [**List&lt;String&gt;**](String.md)| Optional parameter to filter switchports belonging to switches with one or more serial numbers. All switchports returned belong to serial numbers of switches that are an exact match. | [optional] |
| **configurationUpdatedAfter** | **String**| Optional parameter to filter results by switches where the configuration has been updated after the given timestamp. | [optional] |

### Return type

[**List&lt;GetOrganizationSwitchPortsBySwitch200ResponseInner&gt;**](GetOrganizationSwitchPortsBySwitch200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

