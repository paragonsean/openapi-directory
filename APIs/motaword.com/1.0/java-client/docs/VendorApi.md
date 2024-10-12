# VendorApi

All URIs are relative to *https://api.motaword.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAvailableVendors**](VendorApi.md#getAvailableVendors) | **POST** /users/available-vendors | Get a list of vendors available for the criteria given |


<a id="getAvailableVendors"></a>
# **getAvailableVendors**
> UserList getAvailableVendors(with, availableVendorsFilter)

Get a list of vendors available for the criteria given

Get a list of vendors available for the criteria given

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VendorApi;

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

    VendorApi apiInstance = new VendorApi(defaultClient);
    List<String> with = Arrays.asList(); // List<String> | Include detailed information. Possible values 'user'. Requesting user info enrichment takes much longer.
    AvailableVendorsFilter availableVendorsFilter = new AvailableVendorsFilter(); // AvailableVendorsFilter | 
    try {
      UserList result = apiInstance.getAvailableVendors(with, availableVendorsFilter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VendorApi#getAvailableVendors");
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
| **with** | [**List&lt;String&gt;**](String.md)| Include detailed information. Possible values &#39;user&#39;. Requesting user info enrichment takes much longer. | [optional] [enum: user] |
| **availableVendorsFilter** | [**AvailableVendorsFilter**](AvailableVendorsFilter.md)|  | [optional] |

### Return type

[**UserList**](UserList.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User list |  -  |

