# MembershipApi

All URIs are relative to *https://tl-api.azurewebsites.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**membershipGet**](MembershipApi.md#membershipGet) | **GET** /api/Membership | Get all of the members details This will return all properties related to member entity              |
| [**membershipPost**](MembershipApi.md#membershipPost) | **POST** /api/Membership | Add new Member              |


<a id="membershipGet"></a>
# **membershipGet**
> List&lt;MemberDTO&gt; membershipGet()

Get all of the members details This will return all properties related to member entity             

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MembershipApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tl-api.azurewebsites.net");
    
    // Configure OAuth2 access token for authorization: bearer
    OAuth bearer = (OAuth) defaultClient.getAuthentication("bearer");
    bearer.setAccessToken("YOUR ACCESS TOKEN");

    MembershipApi apiInstance = new MembershipApi(defaultClient);
    try {
      List<MemberDTO> result = apiInstance.membershipGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MembershipApi#membershipGet");
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

[**List&lt;MemberDTO&gt;**](MemberDTO.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | API Response with all Members entity as a list. |  -  |
| **404** |  |  -  |

<a id="membershipPost"></a>
# **membershipPost**
> Boolean membershipPost(memberDTO)

Add new Member             

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MembershipApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tl-api.azurewebsites.net");
    
    // Configure OAuth2 access token for authorization: bearer
    OAuth bearer = (OAuth) defaultClient.getAuthentication("bearer");
    bearer.setAccessToken("YOUR ACCESS TOKEN");

    MembershipApi apiInstance = new MembershipApi(defaultClient);
    MemberDTO memberDTO = new MemberDTO(); // MemberDTO | member object
    try {
      Boolean result = apiInstance.membershipPost(memberDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MembershipApi#membershipPost");
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
| **memberDTO** | [**MemberDTO**](MemberDTO.md)| member object | |

### Return type

**Boolean**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | newly created member entity |  -  |
| **404** |  |  -  |

