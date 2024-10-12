# InvitationApi

All URIs are relative to *https://api.motaword.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getInvitationVendors**](InvitationApi.md#getInvitationVendors) | **POST** /invitation/vendors | Get vendor list for compiled invitation needs |


<a id="getInvitationVendors"></a>
# **getInvitationVendors**
> VendorInvitationList getInvitationVendors(fileNeedsVendor)

Get vendor list for compiled invitation needs

Get vendor list for compiled invitation needs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvitationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    InvitationApi apiInstance = new InvitationApi(defaultClient);
    List<FileNeedsVendor> fileNeedsVendor = Arrays.asList(); // List<FileNeedsVendor> | 
    try {
      VendorInvitationList result = apiInstance.getInvitationVendors(fileNeedsVendor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvitationApi#getInvitationVendors");
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
| **fileNeedsVendor** | [**List&lt;FileNeedsVendor&gt;**](FileNeedsVendor.md)|  | [optional] |

### Return type

[**VendorInvitationList**](VendorInvitationList.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Invitation need grouped by vendor |  -  |
| **400** | FileTooLarge FileTooSmall NoFileUploaded |  -  |
| **405** | UnsupportedGlossaryFormat |  -  |

