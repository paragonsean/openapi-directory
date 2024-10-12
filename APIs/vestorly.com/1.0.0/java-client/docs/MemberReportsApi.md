# MemberReportsApi

All URIs are relative to *https://staging.vestorly.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**findMemberReports**](MemberReportsApi.md#findMemberReports) | **GET** /member_reports |  |


<a id="findMemberReports"></a>
# **findMemberReports**
> MemberReports findMemberReports(vestorlyAuth, accessToken)



Returns all member reports

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging.vestorly.com/api/v2");
    
    // Configure OAuth2 access token for authorization: access_token
    OAuth access_token = (OAuth) defaultClient.getAuthentication("access_token");
    access_token.setAccessToken("YOUR ACCESS TOKEN");

    MemberReportsApi apiInstance = new MemberReportsApi(defaultClient);
    String vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
    String accessToken = "accessToken_example"; // String | OAuth Token
    try {
      MemberReports result = apiInstance.findMemberReports(vestorlyAuth, accessToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberReportsApi#findMemberReports");
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
| **vestorlyAuth** | **String**| Vestorly Auth Token | |
| **accessToken** | **String**| OAuth Token | [optional] |

### Return type

[**MemberReports**](MemberReports.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | member reports response |  -  |

