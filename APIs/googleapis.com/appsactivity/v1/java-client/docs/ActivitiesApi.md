# ActivitiesApi

All URIs are relative to *https://www.googleapis.com/appsactivity/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**appsactivityActivitiesList**](ActivitiesApi.md#appsactivityActivitiesList) | **GET** /activities |  |


<a id="appsactivityActivitiesList"></a>
# **appsactivityActivitiesList**
> ListActivitiesResponse appsactivityActivitiesList(alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, driveAncestorId, driveFileId, groupingStrategy, pageSize, pageToken, source, userId)



Returns a list of activities visible to the current logged in user. Visible activities are determined by the visibility settings of the object that was acted on, e.g. Drive files a user can see. An activity is a record of past events. Multiple events may be merged if they are similar. A request is scoped to activities from a given Google service using the source parameter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/appsactivity/v1");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ActivitiesApi apiInstance = new ActivitiesApi(defaultClient);
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    String driveAncestorId = "driveAncestorId_example"; // String | Identifies the Drive folder containing the items for which to return activities.
    String driveFileId = "driveFileId_example"; // String | Identifies the Drive item to return activities for.
    String groupingStrategy = "driveUi"; // String | Indicates the strategy to use when grouping singleEvents items in the associated combinedEvent object.
    Integer pageSize = 56; // Integer | The maximum number of events to return on a page. The response includes a continuation token if there are more events.
    String pageToken = "pageToken_example"; // String | A token to retrieve a specific page of results.
    String source = "source_example"; // String | The Google service from which to return activities. Possible values of source are:  - drive.google.com
    String userId = "userId_example"; // String | The ID used for ACL checks (does not filter the resulting event list by the assigned value). Use the special value me to indicate the currently authenticated user.
    try {
      ListActivitiesResponse result = apiInstance.appsactivityActivitiesList(alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, driveAncestorId, driveFileId, groupingStrategy, pageSize, pageToken, source, userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivitiesApi#appsactivityActivitiesList");
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
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **driveAncestorId** | **String**| Identifies the Drive folder containing the items for which to return activities. | [optional] |
| **driveFileId** | **String**| Identifies the Drive item to return activities for. | [optional] |
| **groupingStrategy** | **String**| Indicates the strategy to use when grouping singleEvents items in the associated combinedEvent object. | [optional] [enum: driveUi, none] |
| **pageSize** | **Integer**| The maximum number of events to return on a page. The response includes a continuation token if there are more events. | [optional] |
| **pageToken** | **String**| A token to retrieve a specific page of results. | [optional] |
| **source** | **String**| The Google service from which to return activities. Possible values of source are:  - drive.google.com | [optional] |
| **userId** | **String**| The ID used for ACL checks (does not filter the resulting event list by the assigned value). Use the special value me to indicate the currently authenticated user. | [optional] |

### Return type

[**ListActivitiesResponse**](ListActivitiesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

