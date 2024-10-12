# InsightsV1ConferenceApi

All URIs are relative to *https://insights.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchConference**](InsightsV1ConferenceApi.md#fetchConference) | **GET** /v1/Conferences/{ConferenceSid} |  |
| [**listConference**](InsightsV1ConferenceApi.md#listConference) | **GET** /v1/Conferences |  |


<a id="fetchConference"></a>
# **fetchConference**
> InsightsV1Conference fetchConference(conferenceSid)



Get a specific Conference Summary.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsightsV1ConferenceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://insights.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    InsightsV1ConferenceApi apiInstance = new InsightsV1ConferenceApi(defaultClient);
    String conferenceSid = "conferenceSid_example"; // String | The unique SID identifier of the Conference.
    try {
      InsightsV1Conference result = apiInstance.fetchConference(conferenceSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsightsV1ConferenceApi#fetchConference");
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
| **conferenceSid** | **String**| The unique SID identifier of the Conference. | |

### Return type

[**InsightsV1Conference**](InsightsV1Conference.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listConference"></a>
# **listConference**
> ListConferenceResponse listConference(conferenceSid, friendlyName, status, createdAfter, createdBefore, mixerRegion, tags, subaccount, detectedIssues, endReason, pageSize, page, pageToken)



Get a list of Conference Summaries.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsightsV1ConferenceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://insights.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    InsightsV1ConferenceApi apiInstance = new InsightsV1ConferenceApi(defaultClient);
    String conferenceSid = "conferenceSid_example"; // String | The SID of the conference.
    String friendlyName = "friendlyName_example"; // String | Custom label for the conference resource, up to 64 characters.
    String status = "status_example"; // String | Conference status.
    String createdAfter = "createdAfter_example"; // String | Conferences created after the provided timestamp specified in ISO 8601 format
    String createdBefore = "createdBefore_example"; // String | Conferences created before the provided timestamp specified in ISO 8601 format.
    String mixerRegion = "mixerRegion_example"; // String | Twilio region where the conference media was mixed.
    String tags = "tags_example"; // String | Tags applied by Twilio for common potential configuration, quality, or performance issues.
    String subaccount = "subaccount_example"; // String | Account SID for the subaccount whose resources you wish to retrieve.
    String detectedIssues = "detectedIssues_example"; // String | Potential configuration, behavior, or performance issues detected during the conference.
    String endReason = "endReason_example"; // String | Conference end reason; e.g. last participant left, modified by API, etc.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListConferenceResponse result = apiInstance.listConference(conferenceSid, friendlyName, status, createdAfter, createdBefore, mixerRegion, tags, subaccount, detectedIssues, endReason, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsightsV1ConferenceApi#listConference");
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
| **conferenceSid** | **String**| The SID of the conference. | [optional] |
| **friendlyName** | **String**| Custom label for the conference resource, up to 64 characters. | [optional] |
| **status** | **String**| Conference status. | [optional] |
| **createdAfter** | **String**| Conferences created after the provided timestamp specified in ISO 8601 format | [optional] |
| **createdBefore** | **String**| Conferences created before the provided timestamp specified in ISO 8601 format. | [optional] |
| **mixerRegion** | **String**| Twilio region where the conference media was mixed. | [optional] |
| **tags** | **String**| Tags applied by Twilio for common potential configuration, quality, or performance issues. | [optional] |
| **subaccount** | **String**| Account SID for the subaccount whose resources you wish to retrieve. | [optional] |
| **detectedIssues** | **String**| Potential configuration, behavior, or performance issues detected during the conference. | [optional] |
| **endReason** | **String**| Conference end reason; e.g. last participant left, modified by API, etc. | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListConferenceResponse**](ListConferenceResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

