# ScheduledOverridesApi

All URIs are relative to *https://api.victorops.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiPublicV1OverridesGet**](ScheduledOverridesApi.md#apiPublicV1OverridesGet) | **GET** /api-public/v1/overrides | List the scheduled overrides |
| [**apiPublicV1OverridesPost**](ScheduledOverridesApi.md#apiPublicV1OverridesPost) | **POST** /api-public/v1/overrides | Creates a new scheduled override |
| [**apiPublicV1OverridesPublicIdAssignmentsGet**](ScheduledOverridesApi.md#apiPublicV1OverridesPublicIdAssignmentsGet) | **GET** /api-public/v1/overrides/{publicId}/assignments | Get the specified scheduled override |
| [**apiPublicV1OverridesPublicIdAssignmentsPolicySlugDelete**](ScheduledOverridesApi.md#apiPublicV1OverridesPublicIdAssignmentsPolicySlugDelete) | **DELETE** /api-public/v1/overrides/{publicId}/assignments/{policySlug} | Delete the scheduled override assignment |
| [**apiPublicV1OverridesPublicIdAssignmentsPolicySlugGet**](ScheduledOverridesApi.md#apiPublicV1OverridesPublicIdAssignmentsPolicySlugGet) | **GET** /api-public/v1/overrides/{publicId}/assignments/{policySlug} | Get the specified scheduled override assignment |
| [**apiPublicV1OverridesPublicIdAssignmentsPolicySlugPut**](ScheduledOverridesApi.md#apiPublicV1OverridesPublicIdAssignmentsPolicySlugPut) | **PUT** /api-public/v1/overrides/{publicId}/assignments/{policySlug} | Update the scheduled override assignment |
| [**apiPublicV1OverridesPublicIdDelete**](ScheduledOverridesApi.md#apiPublicV1OverridesPublicIdDelete) | **DELETE** /api-public/v1/overrides/{publicId} | Deletes a scheduled override |
| [**apiPublicV1OverridesPublicIdGet**](ScheduledOverridesApi.md#apiPublicV1OverridesPublicIdGet) | **GET** /api-public/v1/overrides/{publicId} | Get the specified scheduled override |


<a id="apiPublicV1OverridesGet"></a>
# **apiPublicV1OverridesGet**
> ApiPublicV1OverridesGet200Response apiPublicV1OverridesGet(xVOApiId, xVOApiKey)

List the scheduled overrides

List all the scheduled overrides on the organization  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScheduledOverridesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    ScheduledOverridesApi apiInstance = new ScheduledOverridesApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    try {
      ApiPublicV1OverridesGet200Response result = apiInstance.apiPublicV1OverridesGet(xVOApiId, xVOApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScheduledOverridesApi#apiPublicV1OverridesGet");
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

[**ApiPublicV1OverridesGet200Response**](ApiPublicV1OverridesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of scheduled overrides for your organization |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **404** | Path not found |  -  |
| **422** | You have reached your user limit.  |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiPublicV1OverridesPost"></a>
# **apiPublicV1OverridesPost**
> ApiPublicV1OverridesPost200Response apiPublicV1OverridesPost(xVOApiId, xVOApiKey, body)

Creates a new scheduled override

Creates a new scheduled override. Start and end dates are in ISO8601 format. E.g. &#x60;2018-09-28&#39;T&#39;05:00:00Z&#x60;  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScheduledOverridesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    ScheduledOverridesApi apiInstance = new ScheduledOverridesApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    ScheduledOverridePayload body = new ScheduledOverridePayload(); // ScheduledOverridePayload | 
    try {
      ApiPublicV1OverridesPost200Response result = apiInstance.apiPublicV1OverridesPost(xVOApiId, xVOApiKey, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScheduledOverridesApi#apiPublicV1OverridesPost");
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
| **body** | [**ScheduledOverridePayload**](ScheduledOverridePayload.md)|  | |

### Return type

[**ApiPublicV1OverridesPost200Response**](ApiPublicV1OverridesPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The created scheduled override |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **404** | Path not found |  -  |
| **422** | You have reached your user limit.  |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiPublicV1OverridesPublicIdAssignmentsGet"></a>
# **apiPublicV1OverridesPublicIdAssignmentsGet**
> List&lt;Assignment&gt; apiPublicV1OverridesPublicIdAssignmentsGet(xVOApiId, xVOApiKey, publicId)

Get the specified scheduled override

Get the specified scheduled override assignments  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScheduledOverridesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    ScheduledOverridesApi apiInstance = new ScheduledOverridesApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    String publicId = "publicId_example"; // String | The publicId of the scheduled override
    try {
      List<Assignment> result = apiInstance.apiPublicV1OverridesPublicIdAssignmentsGet(xVOApiId, xVOApiKey, publicId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScheduledOverridesApi#apiPublicV1OverridesPublicIdAssignmentsGet");
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
| **publicId** | **String**| The publicId of the scheduled override | |

### Return type

[**List&lt;Assignment&gt;**](Assignment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The assignments for a given scheduled override |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **404** | Path not found |  -  |
| **422** | You have reached your user limit.  |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiPublicV1OverridesPublicIdAssignmentsPolicySlugDelete"></a>
# **apiPublicV1OverridesPublicIdAssignmentsPolicySlugDelete**
> Assignment apiPublicV1OverridesPublicIdAssignmentsPolicySlugDelete(xVOApiId, xVOApiKey, publicId, policySlug)

Delete the scheduled override assignment

Delete the scheduled override assignment  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScheduledOverridesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    ScheduledOverridesApi apiInstance = new ScheduledOverridesApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    String publicId = "publicId_example"; // String | The publicId of the scheduled override
    String policySlug = "policySlug_example"; // String | The policySlug of the assignment
    try {
      Assignment result = apiInstance.apiPublicV1OverridesPublicIdAssignmentsPolicySlugDelete(xVOApiId, xVOApiKey, publicId, policySlug);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScheduledOverridesApi#apiPublicV1OverridesPublicIdAssignmentsPolicySlugDelete");
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
| **publicId** | **String**| The publicId of the scheduled override | |
| **policySlug** | **String**| The policySlug of the assignment | |

### Return type

[**Assignment**](Assignment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The assignment that was deleted for the given scheduled override and policySlug |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **404** | Path not found |  -  |
| **422** | You have reached your user limit.  |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiPublicV1OverridesPublicIdAssignmentsPolicySlugGet"></a>
# **apiPublicV1OverridesPublicIdAssignmentsPolicySlugGet**
> Assignment apiPublicV1OverridesPublicIdAssignmentsPolicySlugGet(xVOApiId, xVOApiKey, publicId, policySlug)

Get the specified scheduled override assignment

Get the specified scheduled override assignments  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScheduledOverridesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    ScheduledOverridesApi apiInstance = new ScheduledOverridesApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    String publicId = "publicId_example"; // String | The publicId of the scheduled override
    String policySlug = "policySlug_example"; // String | The policySlug of the assignment
    try {
      Assignment result = apiInstance.apiPublicV1OverridesPublicIdAssignmentsPolicySlugGet(xVOApiId, xVOApiKey, publicId, policySlug);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScheduledOverridesApi#apiPublicV1OverridesPublicIdAssignmentsPolicySlugGet");
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
| **publicId** | **String**| The publicId of the scheduled override | |
| **policySlug** | **String**| The policySlug of the assignment | |

### Return type

[**Assignment**](Assignment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The assignment for the given publicId |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **404** | Path not found |  -  |
| **422** | You have reached your user limit.  |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiPublicV1OverridesPublicIdAssignmentsPolicySlugPut"></a>
# **apiPublicV1OverridesPublicIdAssignmentsPolicySlugPut**
> Assignment apiPublicV1OverridesPublicIdAssignmentsPolicySlugPut(xVOApiId, xVOApiKey, publicId, policySlug, body)

Update the scheduled override assignment

Update the scheduled override assignment  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScheduledOverridesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    ScheduledOverridesApi apiInstance = new ScheduledOverridesApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    String publicId = "publicId_example"; // String | The publicId of the scheduled override
    String policySlug = "policySlug_example"; // String | The policySlug of the assignment
    UpdateAssignment body = new UpdateAssignment(); // UpdateAssignment | The policy and username we are assigning
    try {
      Assignment result = apiInstance.apiPublicV1OverridesPublicIdAssignmentsPolicySlugPut(xVOApiId, xVOApiKey, publicId, policySlug, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScheduledOverridesApi#apiPublicV1OverridesPublicIdAssignmentsPolicySlugPut");
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
| **publicId** | **String**| The publicId of the scheduled override | |
| **policySlug** | **String**| The policySlug of the assignment | |
| **body** | [**UpdateAssignment**](UpdateAssignment.md)| The policy and username we are assigning | |

### Return type

[**Assignment**](Assignment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The assignment for the given policySlug |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **404** | Path not found |  -  |
| **422** | You have reached your user limit.  |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiPublicV1OverridesPublicIdDelete"></a>
# **apiPublicV1OverridesPublicIdDelete**
> apiPublicV1OverridesPublicIdDelete(xVOApiId, xVOApiKey, publicId)

Deletes a scheduled override

Deletes a scheduled override  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScheduledOverridesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    ScheduledOverridesApi apiInstance = new ScheduledOverridesApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    String publicId = "publicId_example"; // String | The publicId of the scheduled override
    try {
      apiInstance.apiPublicV1OverridesPublicIdDelete(xVOApiId, xVOApiKey, publicId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScheduledOverridesApi#apiPublicV1OverridesPublicIdDelete");
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
| **publicId** | **String**| The publicId of the scheduled override | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Whether or not the delete was successful |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **404** | Path not found |  -  |
| **422** | You have reached your user limit.  |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiPublicV1OverridesPublicIdGet"></a>
# **apiPublicV1OverridesPublicIdGet**
> ApiPublicV1OverridesPublicIdGet200Response apiPublicV1OverridesPublicIdGet(xVOApiId, xVOApiKey, publicId)

Get the specified scheduled override

Get the specified scheduled override  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScheduledOverridesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    ScheduledOverridesApi apiInstance = new ScheduledOverridesApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    String publicId = "publicId_example"; // String | The publicId of the scheduled override
    try {
      ApiPublicV1OverridesPublicIdGet200Response result = apiInstance.apiPublicV1OverridesPublicIdGet(xVOApiId, xVOApiKey, publicId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScheduledOverridesApi#apiPublicV1OverridesPublicIdGet");
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
| **publicId** | **String**| The publicId of the scheduled override | |

### Return type

[**ApiPublicV1OverridesPublicIdGet200Response**](ApiPublicV1OverridesPublicIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The scheduled override |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **404** | Path not found |  -  |
| **422** | You have reached your user limit.  |  -  |
| **500** | Internal Server Error |  -  |

