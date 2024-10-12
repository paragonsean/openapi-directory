# OrganizationReadApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**organizationDetailsGetOrganizationDetails**](OrganizationReadApi.md#organizationDetailsGetOrganizationDetails) | **GET** /v1/organizationdetails | Get the details of organization. |
| [**organizationSettingsGetOrganizationSettings**](OrganizationReadApi.md#organizationSettingsGetOrganizationSettings) | **GET** /v1/organizationsettings | Get the settings of organization. |
| [**organizationsGetVismaFinancialsCompanyInfo**](OrganizationReadApi.md#organizationsGetVismaFinancialsCompanyInfo) | **GET** /v1/integrations/vismafinancials/companyinformation | Get Visma.net Financials integration company information. |


<a id="organizationDetailsGetOrganizationDetails"></a>
# **organizationDetailsGetOrganizationDetails**
> OrganizationDetailsOutputModel organizationDetailsGetOrganizationDetails()

Get the details of organization.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationReadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    OrganizationReadApi apiInstance = new OrganizationReadApi(defaultClient);
    try {
      OrganizationDetailsOutputModel result = apiInstance.organizationDetailsGetOrganizationDetails();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationReadApi#organizationDetailsGetOrganizationDetails");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OrganizationDetailsOutputModel**](OrganizationDetailsOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Organization |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="organizationSettingsGetOrganizationSettings"></a>
# **organizationSettingsGetOrganizationSettings**
> OrganizationSettingsModel organizationSettingsGetOrganizationSettings()

Get the settings of organization.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationReadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    OrganizationReadApi apiInstance = new OrganizationReadApi(defaultClient);
    try {
      OrganizationSettingsModel result = apiInstance.organizationSettingsGetOrganizationSettings();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationReadApi#organizationSettingsGetOrganizationSettings");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OrganizationSettingsModel**](OrganizationSettingsModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Organization. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="organizationsGetVismaFinancialsCompanyInfo"></a>
# **organizationsGetVismaFinancialsCompanyInfo**
> VismaFinancialsCompanyModel organizationsGetVismaFinancialsCompanyInfo()

Get Visma.net Financials integration company information.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationReadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    OrganizationReadApi apiInstance = new OrganizationReadApi(defaultClient);
    try {
      VismaFinancialsCompanyModel result = apiInstance.organizationsGetVismaFinancialsCompanyInfo();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationReadApi#organizationsGetVismaFinancialsCompanyInfo");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**VismaFinancialsCompanyModel**](VismaFinancialsCompanyModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | VismaFinancialsCompanyModel. |  -  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

