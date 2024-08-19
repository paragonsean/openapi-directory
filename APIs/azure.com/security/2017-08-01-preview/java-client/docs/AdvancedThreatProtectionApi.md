# AdvancedThreatProtectionApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**advancedThreatProtectionCreate**](AdvancedThreatProtectionApi.md#advancedThreatProtectionCreate) | **PUT** /{resourceId}/providers/Microsoft.Security/advancedThreatProtectionSettings/{settingName} |  |
| [**advancedThreatProtectionGet**](AdvancedThreatProtectionApi.md#advancedThreatProtectionGet) | **GET** /{resourceId}/providers/Microsoft.Security/advancedThreatProtectionSettings/{settingName} |  |


<a id="advancedThreatProtectionCreate"></a>
# **advancedThreatProtectionCreate**
> AdvancedThreatProtectionSetting advancedThreatProtectionCreate(apiVersion, resourceId, settingName, advancedThreatProtectionSetting)



Creates or updates the Advanced Threat Protection settings on a specified resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdvancedThreatProtectionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AdvancedThreatProtectionApi apiInstance = new AdvancedThreatProtectionApi(defaultClient);
    String apiVersion = "2017-08-01-preview"; // String | API version for the operation
    String resourceId = "resourceId_example"; // String | The identifier of the resource.
    String settingName = "current"; // String | Advanced Threat Protection setting name.
    AdvancedThreatProtectionSetting advancedThreatProtectionSetting = new AdvancedThreatProtectionSetting(); // AdvancedThreatProtectionSetting | Advanced Threat Protection Settings
    try {
      AdvancedThreatProtectionSetting result = apiInstance.advancedThreatProtectionCreate(apiVersion, resourceId, settingName, advancedThreatProtectionSetting);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdvancedThreatProtectionApi#advancedThreatProtectionCreate");
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
| **apiVersion** | **String**| API version for the operation | [enum: 2017-08-01-preview] |
| **resourceId** | **String**| The identifier of the resource. | |
| **settingName** | **String**| Advanced Threat Protection setting name. | [enum: current] |
| **advancedThreatProtectionSetting** | [**AdvancedThreatProtectionSetting**](AdvancedThreatProtectionSetting.md)| Advanced Threat Protection Settings | |

### Return type

[**AdvancedThreatProtectionSetting**](AdvancedThreatProtectionSetting.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request to put Advanced Threat Protection settings. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="advancedThreatProtectionGet"></a>
# **advancedThreatProtectionGet**
> AdvancedThreatProtectionSetting advancedThreatProtectionGet(apiVersion, resourceId, settingName)



Gets the Advanced Threat Protection settings for the specified resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdvancedThreatProtectionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AdvancedThreatProtectionApi apiInstance = new AdvancedThreatProtectionApi(defaultClient);
    String apiVersion = "2017-08-01-preview"; // String | API version for the operation
    String resourceId = "resourceId_example"; // String | The identifier of the resource.
    String settingName = "current"; // String | Advanced Threat Protection setting name.
    try {
      AdvancedThreatProtectionSetting result = apiInstance.advancedThreatProtectionGet(apiVersion, resourceId, settingName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdvancedThreatProtectionApi#advancedThreatProtectionGet");
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
| **apiVersion** | **String**| API version for the operation | [enum: 2017-08-01-preview] |
| **resourceId** | **String**| The identifier of the resource. | |
| **settingName** | **String**| Advanced Threat Protection setting name. | [enum: current] |

### Return type

[**AdvancedThreatProtectionSetting**](AdvancedThreatProtectionSetting.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request to get Advanced Threat Protection settings. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

