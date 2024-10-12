# MeApi

All URIs are relative to *https://api.test.enode.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**disconnectVendor**](MeApi.md#disconnectVendor) | **DELETE** /me/vendors/{vendor} | Disconnect Vendor |
| [**getMe**](MeApi.md#getMe) | **GET** /me | Get My User |


<a id="disconnectVendor"></a>
# **disconnectVendor**
> disconnectVendor(vendor)

Disconnect Vendor

Disconnect a single Vendor from the User&#39;s account.  All stored data about their Vendor account will be deleted, and any vehicles that were provided by that Vendor will disappear from the system.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.enode.io");
    
    // Configure OAuth2 access token for authorization: UserAccessToken
    OAuth UserAccessToken = (OAuth) defaultClient.getAuthentication("UserAccessToken");
    UserAccessToken.setAccessToken("YOUR ACCESS TOKEN");

    MeApi apiInstance = new MeApi(defaultClient);
    String vendor = "TESLA"; // String | Vendor to be unlinked
    try {
      apiInstance.disconnectVendor(vendor);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeApi#disconnectVendor");
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
| **vendor** | **String**| Vendor to be unlinked | [enum: TESLA, BMW, AUDI, VOLKSWAGEN, HYUNDAI, PEUGEOT, NISSAN] |

### Return type

null (empty response body)

### Authorization

[UserAccessToken](../README.md#UserAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

<a id="getMe"></a>
# **getMe**
> GetMe200Response getMe()

Get My User

Returns metadata about the authenticated User, including a list of vendors for which the user has provided credentials.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.enode.io");
    
    // Configure OAuth2 access token for authorization: UserAccessToken
    OAuth UserAccessToken = (OAuth) defaultClient.getAuthentication("UserAccessToken");
    UserAccessToken.setAccessToken("YOUR ACCESS TOKEN");

    MeApi apiInstance = new MeApi(defaultClient);
    try {
      GetMe200Response result = apiInstance.getMe();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeApi#getMe");
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

[**GetMe200Response**](GetMe200Response.md)

### Authorization

[UserAccessToken](../README.md#UserAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful |  -  |

