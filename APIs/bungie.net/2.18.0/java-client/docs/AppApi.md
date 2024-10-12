# AppApi

All URIs are relative to *https://www.bungie.net/Platform*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**appGetApplicationApiUsage**](AppApi.md#appGetApplicationApiUsage) | **GET** /App/ApiUsage/{applicationId}/ |  |
| [**appGetBungieApplications**](AppApi.md#appGetBungieApplications) | **GET** /App/FirstParty/ |  |


<a id="appGetApplicationApiUsage"></a>
# **appGetApplicationApiUsage**
> AppGetApplicationApiUsage200Response appGetApplicationApiUsage(applicationId, end, start)



Get API usage by application for time frame specified. You can go as far back as 30 days ago, and can ask for up to a 48 hour window of time in a single request. You must be authenticated with at least the ReadUserData permission to access this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AppApi apiInstance = new AppApi(defaultClient);
    Integer applicationId = 56; // Integer | ID of the application to get usage statistics.
    OffsetDateTime end = OffsetDateTime.now(); // OffsetDateTime | End time for query. Goes to now if not specified.
    OffsetDateTime start = OffsetDateTime.now(); // OffsetDateTime | Start time for query. Goes to 24 hours ago if not specified.
    try {
      AppGetApplicationApiUsage200Response result = apiInstance.appGetApplicationApiUsage(applicationId, end, start);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppApi#appGetApplicationApiUsage");
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
| **applicationId** | **Integer**| ID of the application to get usage statistics. | |
| **end** | **OffsetDateTime**| End time for query. Goes to now if not specified. | [optional] |
| **start** | **OffsetDateTime**| Start time for query. Goes to 24 hours ago if not specified. | [optional] |

### Return type

[**AppGetApplicationApiUsage200Response**](AppGetApplicationApiUsage200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="appGetBungieApplications"></a>
# **appGetBungieApplications**
> AppGetBungieApplications200Response appGetBungieApplications()



Get list of applications created by Bungie.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    AppApi apiInstance = new AppApi(defaultClient);
    try {
      AppGetBungieApplications200Response result = apiInstance.appGetBungieApplications();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppApi#appGetBungieApplications");
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

[**AppGetBungieApplications200Response**](AppGetBungieApplications200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

