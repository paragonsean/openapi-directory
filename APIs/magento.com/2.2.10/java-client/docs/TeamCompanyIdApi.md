# TeamCompanyIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**companyTeamRepositoryV1CreatePost**](TeamCompanyIdApi.md#companyTeamRepositoryV1CreatePost) | **POST** /V1/team/{companyId} | team/{companyId} |


<a id="companyTeamRepositoryV1CreatePost"></a>
# **companyTeamRepositoryV1CreatePost**
> ErrorResponse companyTeamRepositoryV1CreatePost(companyId, companyTeamRepositoryV1CreatePostRequest)

team/{companyId}

Create a team in the company structure.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamCompanyIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    TeamCompanyIdApi apiInstance = new TeamCompanyIdApi(defaultClient);
    Integer companyId = 56; // Integer | 
    CompanyTeamRepositoryV1CreatePostRequest companyTeamRepositoryV1CreatePostRequest = new CompanyTeamRepositoryV1CreatePostRequest(); // CompanyTeamRepositoryV1CreatePostRequest | 
    try {
      ErrorResponse result = apiInstance.companyTeamRepositoryV1CreatePost(companyId, companyTeamRepositoryV1CreatePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamCompanyIdApi#companyTeamRepositoryV1CreatePost");
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
| **companyId** | **Integer**|  | |
| **companyTeamRepositoryV1CreatePostRequest** | [**CompanyTeamRepositoryV1CreatePostRequest**](CompanyTeamRepositoryV1CreatePostRequest.md)|  | [optional] |

### Return type

[**ErrorResponse**](ErrorResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

