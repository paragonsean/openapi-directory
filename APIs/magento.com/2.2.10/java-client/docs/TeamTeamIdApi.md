# TeamTeamIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**companyTeamRepositoryV1DeleteByIdDelete**](TeamTeamIdApi.md#companyTeamRepositoryV1DeleteByIdDelete) | **DELETE** /V1/team/{teamId} | team/{teamId} |
| [**companyTeamRepositoryV1GetGet**](TeamTeamIdApi.md#companyTeamRepositoryV1GetGet) | **GET** /V1/team/{teamId} | team/{teamId} |
| [**companyTeamRepositoryV1SavePut**](TeamTeamIdApi.md#companyTeamRepositoryV1SavePut) | **PUT** /V1/team/{teamId} | team/{teamId} |


<a id="companyTeamRepositoryV1DeleteByIdDelete"></a>
# **companyTeamRepositoryV1DeleteByIdDelete**
> ErrorResponse companyTeamRepositoryV1DeleteByIdDelete(teamId)

team/{teamId}

Delete a team from the company structure.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamTeamIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    TeamTeamIdApi apiInstance = new TeamTeamIdApi(defaultClient);
    Integer teamId = 56; // Integer | 
    try {
      ErrorResponse result = apiInstance.companyTeamRepositoryV1DeleteByIdDelete(teamId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamTeamIdApi#companyTeamRepositoryV1DeleteByIdDelete");
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
| **teamId** | **Integer**|  | |

### Return type

[**ErrorResponse**](ErrorResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

<a id="companyTeamRepositoryV1GetGet"></a>
# **companyTeamRepositoryV1GetGet**
> CompanyDataTeamInterface companyTeamRepositoryV1GetGet(teamId)

team/{teamId}

Returns data for a team in the company, by entity id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamTeamIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    TeamTeamIdApi apiInstance = new TeamTeamIdApi(defaultClient);
    Integer teamId = 56; // Integer | 
    try {
      CompanyDataTeamInterface result = apiInstance.companyTeamRepositoryV1GetGet(teamId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamTeamIdApi#companyTeamRepositoryV1GetGet");
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
| **teamId** | **Integer**|  | |

### Return type

[**CompanyDataTeamInterface**](CompanyDataTeamInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

<a id="companyTeamRepositoryV1SavePut"></a>
# **companyTeamRepositoryV1SavePut**
> Boolean companyTeamRepositoryV1SavePut(teamId, companyTeamRepositoryV1CreatePostRequest)

team/{teamId}

Update a team in the company structure.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamTeamIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    TeamTeamIdApi apiInstance = new TeamTeamIdApi(defaultClient);
    String teamId = "teamId_example"; // String | 
    CompanyTeamRepositoryV1CreatePostRequest companyTeamRepositoryV1CreatePostRequest = new CompanyTeamRepositoryV1CreatePostRequest(); // CompanyTeamRepositoryV1CreatePostRequest | 
    try {
      Boolean result = apiInstance.companyTeamRepositoryV1SavePut(teamId, companyTeamRepositoryV1CreatePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamTeamIdApi#companyTeamRepositoryV1SavePut");
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
| **teamId** | **String**|  | |
| **companyTeamRepositoryV1CreatePostRequest** | [**CompanyTeamRepositoryV1CreatePostRequest**](CompanyTeamRepositoryV1CreatePostRequest.md)|  | [optional] |

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

