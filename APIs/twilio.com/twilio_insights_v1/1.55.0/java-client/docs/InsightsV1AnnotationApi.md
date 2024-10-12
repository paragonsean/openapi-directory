# InsightsV1AnnotationApi

All URIs are relative to *https://insights.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchAnnotation**](InsightsV1AnnotationApi.md#fetchAnnotation) | **GET** /v1/Voice/{CallSid}/Annotation |  |
| [**updateAnnotation**](InsightsV1AnnotationApi.md#updateAnnotation) | **POST** /v1/Voice/{CallSid}/Annotation |  |


<a id="fetchAnnotation"></a>
# **fetchAnnotation**
> InsightsV1CallAnnotation fetchAnnotation(callSid)



Get the Annotation for a specific Call.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsightsV1AnnotationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://insights.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    InsightsV1AnnotationApi apiInstance = new InsightsV1AnnotationApi(defaultClient);
    String callSid = "callSid_example"; // String | The unique SID identifier of the Call.
    try {
      InsightsV1CallAnnotation result = apiInstance.fetchAnnotation(callSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsightsV1AnnotationApi#fetchAnnotation");
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
| **callSid** | **String**| The unique SID identifier of the Call. | |

### Return type

[**InsightsV1CallAnnotation**](InsightsV1CallAnnotation.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateAnnotation"></a>
# **updateAnnotation**
> InsightsV1CallAnnotation updateAnnotation(callSid, answeredBy, callScore, comment, connectivityIssue, incident, qualityIssues, spam)



Update an Annotation for a specific Call.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsightsV1AnnotationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://insights.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    InsightsV1AnnotationApi apiInstance = new InsightsV1AnnotationApi(defaultClient);
    String callSid = "callSid_example"; // String | The unique string that Twilio created to identify this Call resource. It always starts with a CA.
    AnnotationEnumAnsweredBy answeredBy = AnnotationEnumAnsweredBy.fromValue("unknown_answered_by"); // AnnotationEnumAnsweredBy | 
    Integer callScore = 56; // Integer | Specify the call score. This is of type integer. Use a range of 1-5 to indicate the call experience score, with the following mapping as a reference for rating the call [5: Excellent, 4: Good, 3 : Fair, 2 : Poor, 1: Bad].
    String comment = "comment_example"; // String | Specify any comments pertaining to the call. `comment` has a maximum character limit of 100. Twilio does not treat this field as PII, so no PII should be included in the `comment`.
    AnnotationEnumConnectivityIssue connectivityIssue = AnnotationEnumConnectivityIssue.fromValue("unknown_connectivity_issue"); // AnnotationEnumConnectivityIssue | 
    String incident = "incident_example"; // String | Associate this call with an incident or support ticket. The `incident` parameter is of type string with a maximum character limit of 100. Twilio does not treat this field as PII, so no PII should be included in `incident`.
    String qualityIssues = "qualityIssues_example"; // String | Specify if the call had any subjective quality issues. Possible values, one or more of `no_quality_issue`, `low_volume`, `choppy_robotic`, `echo`, `dtmf`, `latency`, `owa`, `static_noise`. Use comma separated values to indicate multiple quality issues for the same call.
    Boolean spam = true; // Boolean | A boolean flag to indicate if the call was a spam call. Use this to provide feedback on whether calls placed from your account were marked as spam, or if inbound calls received by your account were unwanted spam. Use `true` if the call was a spam call.
    try {
      InsightsV1CallAnnotation result = apiInstance.updateAnnotation(callSid, answeredBy, callScore, comment, connectivityIssue, incident, qualityIssues, spam);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsightsV1AnnotationApi#updateAnnotation");
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
| **callSid** | **String**| The unique string that Twilio created to identify this Call resource. It always starts with a CA. | |
| **answeredBy** | **AnnotationEnumAnsweredBy**|  | [optional] [enum: unknown_answered_by, human, machine] |
| **callScore** | **Integer**| Specify the call score. This is of type integer. Use a range of 1-5 to indicate the call experience score, with the following mapping as a reference for rating the call [5: Excellent, 4: Good, 3 : Fair, 2 : Poor, 1: Bad]. | [optional] |
| **comment** | **String**| Specify any comments pertaining to the call. &#x60;comment&#x60; has a maximum character limit of 100. Twilio does not treat this field as PII, so no PII should be included in the &#x60;comment&#x60;. | [optional] |
| **connectivityIssue** | **AnnotationEnumConnectivityIssue**|  | [optional] [enum: unknown_connectivity_issue, no_connectivity_issue, invalid_number, caller_id, dropped_call, number_reachability] |
| **incident** | **String**| Associate this call with an incident or support ticket. The &#x60;incident&#x60; parameter is of type string with a maximum character limit of 100. Twilio does not treat this field as PII, so no PII should be included in &#x60;incident&#x60;. | [optional] |
| **qualityIssues** | **String**| Specify if the call had any subjective quality issues. Possible values, one or more of &#x60;no_quality_issue&#x60;, &#x60;low_volume&#x60;, &#x60;choppy_robotic&#x60;, &#x60;echo&#x60;, &#x60;dtmf&#x60;, &#x60;latency&#x60;, &#x60;owa&#x60;, &#x60;static_noise&#x60;. Use comma separated values to indicate multiple quality issues for the same call. | [optional] |
| **spam** | **Boolean**| A boolean flag to indicate if the call was a spam call. Use this to provide feedback on whether calls placed from your account were marked as spam, or if inbound calls received by your account were unwanted spam. Use &#x60;true&#x60; if the call was a spam call. | [optional] |

### Return type

[**InsightsV1CallAnnotation**](InsightsV1CallAnnotation.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

