# AdvisorsApi

All URIs are relative to *https://staging.vestorly.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**findAdvisorByID**](AdvisorsApi.md#findAdvisorByID) | **GET** /advisors/{id} |  |


<a id="findAdvisorByID"></a>
# **findAdvisorByID**
> Advisor findAdvisorByID(vestorlyAuth, id, accessToken)



Returns a single advisor given their ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdvisorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging.vestorly.com/api/v2");
    
    // Configure OAuth2 access token for authorization: access_token
    OAuth access_token = (OAuth) defaultClient.getAuthentication("access_token");
    access_token.setAccessToken("YOUR ACCESS TOKEN");

    AdvisorsApi apiInstance = new AdvisorsApi(defaultClient);
    String vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
    String id = "id_example"; // String | Advisor Id to fetch
    String accessToken = "accessToken_example"; // String | OAuth Token
    try {
      Advisor result = apiInstance.findAdvisorByID(vestorlyAuth, id, accessToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdvisorsApi#findAdvisorByID");
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
| **id** | **String**| Advisor Id to fetch | |
| **accessToken** | **String**| OAuth Token | [optional] |

### Return type

[**Advisor**](Advisor.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Advisor response |  -  |

