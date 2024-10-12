# LoginSecurityApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getOrganizationLoginSecurity_1**](LoginSecurityApi.md#getOrganizationLoginSecurity_1) | **GET** /organizations/{organizationId}/loginSecurity | Returns the login security settings for an organization. |
| [**updateOrganizationLoginSecurity_1**](LoginSecurityApi.md#updateOrganizationLoginSecurity_1) | **PUT** /organizations/{organizationId}/loginSecurity | Update the login security settings for an organization |


<a id="getOrganizationLoginSecurity_1"></a>
# **getOrganizationLoginSecurity_1**
> GetOrganizationLoginSecurity200Response getOrganizationLoginSecurity_1(organizationId)

Returns the login security settings for an organization.

Returns the login security settings for an organization.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LoginSecurityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    LoginSecurityApi apiInstance = new LoginSecurityApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    try {
      GetOrganizationLoginSecurity200Response result = apiInstance.getOrganizationLoginSecurity_1(organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LoginSecurityApi#getOrganizationLoginSecurity_1");
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

[**GetOrganizationLoginSecurity200Response**](GetOrganizationLoginSecurity200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateOrganizationLoginSecurity_1"></a>
# **updateOrganizationLoginSecurity_1**
> GetOrganizationLoginSecurity200Response updateOrganizationLoginSecurity_1(organizationId, updateOrganizationLoginSecurityRequest)

Update the login security settings for an organization

Update the login security settings for an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LoginSecurityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    LoginSecurityApi apiInstance = new LoginSecurityApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    UpdateOrganizationLoginSecurityRequest updateOrganizationLoginSecurityRequest = new UpdateOrganizationLoginSecurityRequest(); // UpdateOrganizationLoginSecurityRequest | 
    try {
      GetOrganizationLoginSecurity200Response result = apiInstance.updateOrganizationLoginSecurity_1(organizationId, updateOrganizationLoginSecurityRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LoginSecurityApi#updateOrganizationLoginSecurity_1");
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
| **updateOrganizationLoginSecurityRequest** | [**UpdateOrganizationLoginSecurityRequest**](UpdateOrganizationLoginSecurityRequest.md)|  | [optional] |

### Return type

[**GetOrganizationLoginSecurity200Response**](GetOrganizationLoginSecurity200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

