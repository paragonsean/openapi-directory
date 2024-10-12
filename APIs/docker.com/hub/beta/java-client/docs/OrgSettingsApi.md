# OrgSettingsApi

All URIs are relative to *https://hub.docker.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v2OrgsNameSettingsGet**](OrgSettingsApi.md#v2OrgsNameSettingsGet) | **GET** /v2/orgs/{name}/settings | Get organization settings |
| [**v2OrgsNameSettingsPut**](OrgSettingsApi.md#v2OrgsNameSettingsPut) | **PUT** /v2/orgs/{name}/settings | Update organization settings |


<a id="v2OrgsNameSettingsGet"></a>
# **v2OrgsNameSettingsGet**
> OrgSettings v2OrgsNameSettingsGet(name)

Get organization settings

Returns organization settings by name. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrgSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://hub.docker.com");

    OrgSettingsApi apiInstance = new OrgSettingsApi(defaultClient);
    String name = "name_example"; // String | Name of the organization.
    try {
      OrgSettings result = apiInstance.v2OrgsNameSettingsGet(name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrgSettingsApi#v2OrgsNameSettingsGet");
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
| **name** | **String**| Name of the organization. | |

### Return type

[**OrgSettings**](OrgSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="v2OrgsNameSettingsPut"></a>
# **v2OrgsNameSettingsPut**
> OrgSettings v2OrgsNameSettingsPut(name, v2OrgsNameSettingsPutRequest)

Update organization settings

Updates an organization&#39;s settings. Some settings are only used when the organization is on a business plan.  ***Only users in the \&quot;owners\&quot; group of the organization can use this endpoint.***  The following settings are only used on a business plan: - &#x60;restricted_images&#x60; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrgSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://hub.docker.com");

    OrgSettingsApi apiInstance = new OrgSettingsApi(defaultClient);
    String name = "name_example"; // String | Name of the organization.
    V2OrgsNameSettingsPutRequest v2OrgsNameSettingsPutRequest = new V2OrgsNameSettingsPutRequest(); // V2OrgsNameSettingsPutRequest | 
    try {
      OrgSettings result = apiInstance.v2OrgsNameSettingsPut(name, v2OrgsNameSettingsPutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrgSettingsApi#v2OrgsNameSettingsPut");
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
| **name** | **String**| Name of the organization. | |
| **v2OrgsNameSettingsPutRequest** | [**V2OrgsNameSettingsPutRequest**](V2OrgsNameSettingsPutRequest.md)|  | |

### Return type

[**OrgSettings**](OrgSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

