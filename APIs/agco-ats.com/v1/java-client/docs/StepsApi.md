# StepsApi

All URIs are relative to *https://secure.agco-ats.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**stepsGetStep**](StepsApi.md#stepsGetStep) | **GET** /api/v2/steps/{stepID} | Get a Step by ID |
| [**stepsGetSteps**](StepsApi.md#stepsGetSteps) | **GET** /api/v2/steps | Get Steps |
| [**stepsPostStep**](StepsApi.md#stepsPostStep) | **POST** /api/v2/steps | Create a Step |
| [**stepsPutStep**](StepsApi.md#stepsPutStep) | **PUT** /api/v2/steps/{stepID} | Update a Step |


<a id="stepsGetStep"></a>
# **stepsGetStep**
> BuildSystemSharedDTOStep stepsGetStep(stepID, isIncludeDeleted)

Get a Step by ID

Gets a Step by ID. When successful, the response is the requested Step.              If unsuccessful, an appropriate ApiError is returned.  Steps.Read permission is required.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StepsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    StepsApi apiInstance = new StepsApi(defaultClient);
    Integer stepID = 56; // Integer | The ID of the Step to get.
    Boolean isIncludeDeleted = true; // Boolean | Does it include deleted step, or not
    try {
      BuildSystemSharedDTOStep result = apiInstance.stepsGetStep(stepID, isIncludeDeleted);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StepsApi#stepsGetStep");
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
| **stepID** | **Integer**| The ID of the Step to get. | |
| **isIncludeDeleted** | **Boolean**| Does it include deleted step, or not | [optional] |

### Return type

[**BuildSystemSharedDTOStep**](BuildSystemSharedDTOStep.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="stepsGetSteps"></a>
# **stepsGetSteps**
> APIPagedResponseBuildSystemSharedDTOStep stepsGetSteps(limit, offset, includeDeleted)

Get Steps

Gets a collection of Steps. When successful, the response is a PagedResponse of Steps.              If unsuccessful, an appropriate ApiError is returned.  Steps.Read permission is required.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StepsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    StepsApi apiInstance = new StepsApi(defaultClient);
    Integer limit = 56; // Integer | Optional. The page limit.  If not specified, the default page limit is 10.
    Integer offset = 56; // Integer | Optional. The page offset.  If not specified, the default page offset is 0.
    Boolean includeDeleted = true; // Boolean | Does it include deleted step, or not
    try {
      APIPagedResponseBuildSystemSharedDTOStep result = apiInstance.stepsGetSteps(limit, offset, includeDeleted);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StepsApi#stepsGetSteps");
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
| **limit** | **Integer**| Optional. The page limit.  If not specified, the default page limit is 10. | [optional] |
| **offset** | **Integer**| Optional. The page offset.  If not specified, the default page offset is 0. | [optional] |
| **includeDeleted** | **Boolean**| Does it include deleted step, or not | [optional] |

### Return type

[**APIPagedResponseBuildSystemSharedDTOStep**](APIPagedResponseBuildSystemSharedDTOStep.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="stepsPostStep"></a>
# **stepsPostStep**
> Integer stepsPostStep(buildSystemSharedDTOStep)

Create a Step

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StepsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    StepsApi apiInstance = new StepsApi(defaultClient);
    BuildSystemSharedDTOStep buildSystemSharedDTOStep = new BuildSystemSharedDTOStep(); // BuildSystemSharedDTOStep | The step to create
    try {
      Integer result = apiInstance.stepsPostStep(buildSystemSharedDTOStep);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StepsApi#stepsPostStep");
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
| **buildSystemSharedDTOStep** | [**BuildSystemSharedDTOStep**](BuildSystemSharedDTOStep.md)| The step to create | |

### Return type

**Integer**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="stepsPutStep"></a>
# **stepsPutStep**
> stepsPutStep(stepID, buildSystemSharedDTOStep)

Update a Step

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StepsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    StepsApi apiInstance = new StepsApi(defaultClient);
    Integer stepID = 56; // Integer | The step ID of the step to update
    BuildSystemSharedDTOStep buildSystemSharedDTOStep = new BuildSystemSharedDTOStep(); // BuildSystemSharedDTOStep | The updated step
    try {
      apiInstance.stepsPutStep(stepID, buildSystemSharedDTOStep);
    } catch (ApiException e) {
      System.err.println("Exception when calling StepsApi#stepsPutStep");
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
| **stepID** | **Integer**| The step ID of the step to update | |
| **buildSystemSharedDTOStep** | [**BuildSystemSharedDTOStep**](BuildSystemSharedDTOStep.md)| The updated step | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | API Error Response |  -  |

