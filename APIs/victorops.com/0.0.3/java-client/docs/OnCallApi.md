# OnCallApi

All URIs are relative to *https://api.victorops.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiPublicV1OncallCurrentGet**](OnCallApi.md#apiPublicV1OncallCurrentGet) | **GET** /api-public/v1/oncall/current | Get an organization&#39;s on-call users |
| [**apiPublicV1PoliciesPolicyOncallUserPatch**](OnCallApi.md#apiPublicV1PoliciesPolicyOncallUserPatch) | **PATCH** /api-public/v1/policies/{policy}/oncall/user | Create an on-call override (take on-call) |
| [**apiPublicV1TeamTeamOncallScheduleGet**](OnCallApi.md#apiPublicV1TeamTeamOncallScheduleGet) | **GET** /api-public/v1/team/{team}/oncall/schedule | Get a team&#39;s on-call schedule |
| [**apiPublicV1TeamTeamOncallUserPatch**](OnCallApi.md#apiPublicV1TeamTeamOncallUserPatch) | **PATCH** /api-public/v1/team/{team}/oncall/user | Create an on-call override (take on-call) |
| [**apiPublicV1UserUserOncallScheduleGet**](OnCallApi.md#apiPublicV1UserUserOncallScheduleGet) | **GET** /api-public/v1/user/{user}/oncall/schedule | Get a user&#39;s on-call schedule |
| [**apiPublicV2TeamTeamOncallScheduleGet**](OnCallApi.md#apiPublicV2TeamTeamOncallScheduleGet) | **GET** /api-public/v2/team/{team}/oncall/schedule | Get a team&#39;s on-call schedule |
| [**apiPublicV2UserUserOncallScheduleGet**](OnCallApi.md#apiPublicV2UserUserOncallScheduleGet) | **GET** /api-public/v2/user/{user}/oncall/schedule | Get a user&#39;s on-call schedule |


<a id="apiPublicV1OncallCurrentGet"></a>
# **apiPublicV1OncallCurrentGet**
> ApiPublicV1OncallCurrentGet200Response apiPublicV1OncallCurrentGet(xVOApiId, xVOApiKey)

Get an organization&#39;s on-call users

Get all on-call users/teams for your organization.  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OnCallApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    OnCallApi apiInstance = new OnCallApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    try {
      ApiPublicV1OncallCurrentGet200Response result = apiInstance.apiPublicV1OncallCurrentGet(xVOApiId, xVOApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnCallApi#apiPublicV1OncallCurrentGet");
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

[**ApiPublicV1OncallCurrentGet200Response**](ApiPublicV1OncallCurrentGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All users and escalation policies currently on call |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiPublicV1PoliciesPolicyOncallUserPatch"></a>
# **apiPublicV1PoliciesPolicyOncallUserPatch**
> TakeResult apiPublicV1PoliciesPolicyOncallUserPatch(xVOApiId, xVOApiKey, policy, body)

Create an on-call override (take on-call)

Replaces a currently on-call user in the escalation policy with another.  In many cases, the policy slug will match the slug of the team that contains it.  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OnCallApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    OnCallApi apiInstance = new OnCallApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    String policy = "policy_example"; // String | The VictorOps policy 'slug'
    TakeRequest body = new TakeRequest(); // TakeRequest | The take on-call payload
    try {
      TakeResult result = apiInstance.apiPublicV1PoliciesPolicyOncallUserPatch(xVOApiId, xVOApiKey, policy, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnCallApi#apiPublicV1PoliciesPolicyOncallUserPatch");
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
| **policy** | **String**| The VictorOps policy &#39;slug&#39; | |
| **body** | [**TakeRequest**](TakeRequest.md)| The take on-call payload | |

### Return type

[**TakeResult**](TakeResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The result of the take request |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **404** | Team or user(s) not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiPublicV1TeamTeamOncallScheduleGet"></a>
# **apiPublicV1TeamTeamOncallScheduleGet**
> OnCallAndOverrides apiPublicV1TeamTeamOncallScheduleGet(xVOApiId, xVOApiKey, team, daysForward, daysSkip, step)

Get a team&#39;s on-call schedule

__NOTE: This call is deprecated. Please use &#x60;GET /api-public/v2/team/{team}/oncall/schedule&#x60;.__  Get the on-call schedule for a team, including on-call overrides.  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OnCallApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    OnCallApi apiInstance = new OnCallApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    String team = "team_example"; // String | The VictorOps team 'slug'
    BigDecimal daysForward = new BigDecimal("14.0"); // BigDecimal | Days to include in returned schedule (30 max)
    BigDecimal daysSkip = new BigDecimal("0.0"); // BigDecimal | Days to skip before computing schedule to return (90 max)
    BigDecimal step = new BigDecimal("0.0"); // BigDecimal | Step of escalation policy (3 max)
    try {
      OnCallAndOverrides result = apiInstance.apiPublicV1TeamTeamOncallScheduleGet(xVOApiId, xVOApiKey, team, daysForward, daysSkip, step);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnCallApi#apiPublicV1TeamTeamOncallScheduleGet");
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
| **team** | **String**| The VictorOps team &#39;slug&#39; | |
| **daysForward** | **BigDecimal**| Days to include in returned schedule (30 max) | [optional] [default to 14.0] |
| **daysSkip** | **BigDecimal**| Days to skip before computing schedule to return (90 max) | [optional] [default to 0.0] |
| **step** | **BigDecimal**| Step of escalation policy (3 max) | [optional] [default to 0.0] |

### Return type

[**OnCallAndOverrides**](OnCallAndOverrides.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The on-call schedule for the team |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **404** | Team not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiPublicV1TeamTeamOncallUserPatch"></a>
# **apiPublicV1TeamTeamOncallUserPatch**
> TakeResult apiPublicV1TeamTeamOncallUserPatch(xVOApiId, xVOApiKey, team, body)

Create an on-call override (take on-call)

__NOTE: This API call is deprecated. Please use &#x60;PATCH /api-public/v2/policies/{policy}/oncall/user&#x60;__  Replaces a currently on-call user on the team with another.  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OnCallApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    OnCallApi apiInstance = new OnCallApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    String team = "team_example"; // String | The VictorOps team 'slug'
    TakeRequest body = new TakeRequest(); // TakeRequest | The take on-call payload
    try {
      TakeResult result = apiInstance.apiPublicV1TeamTeamOncallUserPatch(xVOApiId, xVOApiKey, team, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnCallApi#apiPublicV1TeamTeamOncallUserPatch");
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
| **team** | **String**| The VictorOps team &#39;slug&#39; | |
| **body** | [**TakeRequest**](TakeRequest.md)| The take on-call payload | |

### Return type

[**TakeResult**](TakeResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The result of the take request |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **404** | Team or user(s) not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiPublicV1UserUserOncallScheduleGet"></a>
# **apiPublicV1UserUserOncallScheduleGet**
> List&lt;OnCallAndOverrides&gt; apiPublicV1UserUserOncallScheduleGet(xVOApiId, xVOApiKey, user, daysForward, daysSkip, step)

Get a user&#39;s on-call schedule

__NOTE: This call is deprecated. Please use &#x60;GET /api-public/v2/user/{user}/oncall/schedule&#x60;.__  Get the on-call schedule for a user for all teams, including on-call overrides.  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OnCallApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    OnCallApi apiInstance = new OnCallApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    String user = "user_example"; // String | The VictorOps user ID
    BigDecimal daysForward = new BigDecimal("14.0"); // BigDecimal | Days to include in returned schedule (30 max)
    BigDecimal daysSkip = new BigDecimal("0.0"); // BigDecimal | Days to skip before computing schedule to return (90 max)
    BigDecimal step = new BigDecimal("0.0"); // BigDecimal | Step of escalation policy (3 max)
    try {
      List<OnCallAndOverrides> result = apiInstance.apiPublicV1UserUserOncallScheduleGet(xVOApiId, xVOApiKey, user, daysForward, daysSkip, step);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnCallApi#apiPublicV1UserUserOncallScheduleGet");
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
| **user** | **String**| The VictorOps user ID | |
| **daysForward** | **BigDecimal**| Days to include in returned schedule (30 max) | [optional] [default to 14.0] |
| **daysSkip** | **BigDecimal**| Days to skip before computing schedule to return (90 max) | [optional] [default to 0.0] |
| **step** | **BigDecimal**| Step of escalation policy (3 max) | [optional] [default to 0.0] |

### Return type

[**List&lt;OnCallAndOverrides&gt;**](OnCallAndOverrides.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The on-call schedule for the user |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **404** | User not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiPublicV2TeamTeamOncallScheduleGet"></a>
# **apiPublicV2TeamTeamOncallScheduleGet**
> TeamSchedule apiPublicV2TeamTeamOncallScheduleGet(xVOApiId, xVOApiKey, team, daysForward, daysSkip, step)

Get a team&#39;s on-call schedule

Get the on-call schedule for a team, including on-call overrides.  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OnCallApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    OnCallApi apiInstance = new OnCallApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    String team = "team_example"; // String | The VictorOps team 'slug'
    BigDecimal daysForward = new BigDecimal("14.0"); // BigDecimal | Days to include in returned schedule (30 max)
    BigDecimal daysSkip = new BigDecimal("0.0"); // BigDecimal | Days to skip before computing schedule to return (90 max)
    BigDecimal step = new BigDecimal("0.0"); // BigDecimal | Step of escalation policy (3 max)
    try {
      TeamSchedule result = apiInstance.apiPublicV2TeamTeamOncallScheduleGet(xVOApiId, xVOApiKey, team, daysForward, daysSkip, step);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnCallApi#apiPublicV2TeamTeamOncallScheduleGet");
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
| **team** | **String**| The VictorOps team &#39;slug&#39; | |
| **daysForward** | **BigDecimal**| Days to include in returned schedule (30 max) | [optional] [default to 14.0] |
| **daysSkip** | **BigDecimal**| Days to skip before computing schedule to return (90 max) | [optional] [default to 0.0] |
| **step** | **BigDecimal**| Step of escalation policy (3 max) | [optional] [default to 0.0] |

### Return type

[**TeamSchedule**](TeamSchedule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The on-call schedule for the team |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **404** | Team not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiPublicV2UserUserOncallScheduleGet"></a>
# **apiPublicV2UserUserOncallScheduleGet**
> UserSchedule apiPublicV2UserUserOncallScheduleGet(xVOApiId, xVOApiKey, user, daysForward, daysSkip, step)

Get a user&#39;s on-call schedule

Get the on-call schedule for a user for all teams the user is on, including on-call overrides.  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OnCallApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    OnCallApi apiInstance = new OnCallApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    String user = "user_example"; // String | The VictorOps user ID
    BigDecimal daysForward = new BigDecimal("14.0"); // BigDecimal | Days to include in returned schedule (30 max)
    BigDecimal daysSkip = new BigDecimal("0.0"); // BigDecimal | Days to skip before computing schedule to return (90 max)
    BigDecimal step = new BigDecimal("0.0"); // BigDecimal | Step of escalation policy (3 max)
    try {
      UserSchedule result = apiInstance.apiPublicV2UserUserOncallScheduleGet(xVOApiId, xVOApiKey, user, daysForward, daysSkip, step);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnCallApi#apiPublicV2UserUserOncallScheduleGet");
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
| **user** | **String**| The VictorOps user ID | |
| **daysForward** | **BigDecimal**| Days to include in returned schedule (30 max) | [optional] [default to 14.0] |
| **daysSkip** | **BigDecimal**| Days to skip before computing schedule to return (90 max) | [optional] [default to 0.0] |
| **step** | **BigDecimal**| Step of escalation policy (3 max) | [optional] [default to 0.0] |

### Return type

[**UserSchedule**](UserSchedule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The on-call schedule for the user |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **404** | User not found |  -  |
| **500** | Internal Server Error |  -  |

