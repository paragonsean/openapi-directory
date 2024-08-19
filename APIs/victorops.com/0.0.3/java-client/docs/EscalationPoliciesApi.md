# EscalationPoliciesApi

All URIs are relative to *https://api.victorops.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiPublicV1PoliciesGet**](EscalationPoliciesApi.md#apiPublicV1PoliciesGet) | **GET** /api-public/v1/policies | Get escalation policy info |
| [**apiPublicV1TeamTeamPoliciesGet**](EscalationPoliciesApi.md#apiPublicV1TeamTeamPoliciesGet) | **GET** /api-public/v1/team/{team}/policies | Retrieve a list of escalation policies for a team |


<a id="apiPublicV1PoliciesGet"></a>
# **apiPublicV1PoliciesGet**
> EscalationPolicyInfoList apiPublicV1PoliciesGet(xVOApiId, xVOApiKey)

Get escalation policy info

Retrieves a list of escalation policy information. This API may be called a maximum of once a minute.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EscalationPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    EscalationPoliciesApi apiInstance = new EscalationPoliciesApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    try {
      EscalationPolicyInfoList result = apiInstance.apiPublicV1PoliciesGet(xVOApiId, xVOApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EscalationPoliciesApi#apiPublicV1PoliciesGet");
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
| **xVOApiId** | **String**| Your API ID | |
| **xVOApiKey** | **String**| Your API Key | |

### Return type

[**EscalationPolicyInfoList**](EscalationPolicyInfoList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of escalation policies |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **404** | Path not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiPublicV1TeamTeamPoliciesGet"></a>
# **apiPublicV1TeamTeamPoliciesGet**
> EscalationPolicyList apiPublicV1TeamTeamPoliciesGet(xVOApiId, xVOApiKey, team)

Retrieve a list of escalation policies for a team

Get the escalation policies for the specified team.  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EscalationPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    EscalationPoliciesApi apiInstance = new EscalationPoliciesApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    String team = "team_example"; // String | The VictorOps team to fetch
    try {
      EscalationPolicyList result = apiInstance.apiPublicV1TeamTeamPoliciesGet(xVOApiId, xVOApiKey, team);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EscalationPoliciesApi#apiPublicV1TeamTeamPoliciesGet");
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
| **xVOApiId** | **String**| Your API ID | |
| **xVOApiKey** | **String**| Your API Key | |
| **team** | **String**| The VictorOps team to fetch | |

### Return type

[**EscalationPolicyList**](EscalationPolicyList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The escalation policy list. This does not include details about the actual notification steps of the policy. |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **404** | Team not found |  -  |
| **422** | Team name or email is unavailable, or you have reached your team limit.  |  -  |
| **500** | Internal Server Error |  -  |

