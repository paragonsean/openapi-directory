# BetaTesterInvitationsApi

All URIs are relative to *https://api.appstoreconnect.apple.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**betaTesterInvitationsCreateInstance**](BetaTesterInvitationsApi.md#betaTesterInvitationsCreateInstance) | **POST** /v1/betaTesterInvitations |  |


<a id="betaTesterInvitationsCreateInstance"></a>
# **betaTesterInvitationsCreateInstance**
> BetaTesterInvitationResponse betaTesterInvitationsCreateInstance(betaTesterInvitationCreateRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BetaTesterInvitationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BetaTesterInvitationsApi apiInstance = new BetaTesterInvitationsApi(defaultClient);
    BetaTesterInvitationCreateRequest betaTesterInvitationCreateRequest = new BetaTesterInvitationCreateRequest(); // BetaTesterInvitationCreateRequest | BetaTesterInvitation representation
    try {
      BetaTesterInvitationResponse result = apiInstance.betaTesterInvitationsCreateInstance(betaTesterInvitationCreateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BetaTesterInvitationsApi#betaTesterInvitationsCreateInstance");
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
| **betaTesterInvitationCreateRequest** | [**BetaTesterInvitationCreateRequest**](BetaTesterInvitationCreateRequest.md)| BetaTesterInvitation representation | |

### Return type

[**BetaTesterInvitationResponse**](BetaTesterInvitationResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Single BetaTesterInvitation |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **409** | Request entity error(s) |  -  |

