# ActivitiesApi

All URIs are relative to *https://app.apacta.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**activitiesActivityIdDelete**](ActivitiesApi.md#activitiesActivityIdDelete) | **DELETE** /activities/{activity_id} | Delete an activity |
| [**activitiesActivityIdPut**](ActivitiesApi.md#activitiesActivityIdPut) | **PUT** /activities/{activity_id} | Edit an activity |
| [**activitiesBulkDeleteDelete**](ActivitiesApi.md#activitiesBulkDeleteDelete) | **DELETE** /activities/bulkDelete | Bulk delete activities |
| [**activitiesGet**](ActivitiesApi.md#activitiesGet) | **GET** /activities | Get a list of activities |
| [**activitiesPost**](ActivitiesApi.md#activitiesPost) | **POST** /activities | Create an activity |


<a id="activitiesActivityIdDelete"></a>
# **activitiesActivityIdDelete**
> EmptySuccessResponse activitiesActivityIdDelete(activityId)

Delete an activity

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");

    ActivitiesApi apiInstance = new ActivitiesApi(defaultClient);
    UUID activityId = UUID.randomUUID(); // UUID | 
    try {
      EmptySuccessResponse result = apiInstance.activitiesActivityIdDelete(activityId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivitiesApi#activitiesActivityIdDelete");
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
| **activityId** | **UUID**|  | |

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **403** | Forbidden |  -  |
| **404** | Record not found |  -  |
| **422** | Validation error |  -  |

<a id="activitiesActivityIdPut"></a>
# **activitiesActivityIdPut**
> EmptySuccessResponse activitiesActivityIdPut(activityId, activitiesPostRequest)

Edit an activity

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");

    ActivitiesApi apiInstance = new ActivitiesApi(defaultClient);
    UUID activityId = UUID.randomUUID(); // UUID | 
    ActivitiesPostRequest activitiesPostRequest = new ActivitiesPostRequest(); // ActivitiesPostRequest | 
    try {
      EmptySuccessResponse result = apiInstance.activitiesActivityIdPut(activityId, activitiesPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivitiesApi#activitiesActivityIdPut");
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
| **activityId** | **UUID**|  | |
| **activitiesPostRequest** | [**ActivitiesPostRequest**](ActivitiesPostRequest.md)|  | |

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **403** | Forbidden |  -  |
| **404** | Record not found |  -  |
| **422** | Validation error |  -  |

<a id="activitiesBulkDeleteDelete"></a>
# **activitiesBulkDeleteDelete**
> EmptySuccessResponse activitiesBulkDeleteDelete(bulkActionRequestBody)

Bulk delete activities

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");

    ActivitiesApi apiInstance = new ActivitiesApi(defaultClient);
    BulkActionRequestBody bulkActionRequestBody = new BulkActionRequestBody(); // BulkActionRequestBody | Activities ids
    try {
      EmptySuccessResponse result = apiInstance.activitiesBulkDeleteDelete(bulkActionRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivitiesApi#activitiesBulkDeleteDelete");
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
| **bulkActionRequestBody** | [**BulkActionRequestBody**](BulkActionRequestBody.md)| Activities ids | |

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |

<a id="activitiesGet"></a>
# **activitiesGet**
> ActivitiesGet200Response activitiesGet()

Get a list of activities

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");

    ActivitiesApi apiInstance = new ActivitiesApi(defaultClient);
    try {
      ActivitiesGet200Response result = apiInstance.activitiesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivitiesApi#activitiesGet");
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

[**ActivitiesGet200Response**](ActivitiesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="activitiesPost"></a>
# **activitiesPost**
> EmptySuccessResponse activitiesPost(activitiesPostRequest)

Create an activity

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");

    ActivitiesApi apiInstance = new ActivitiesApi(defaultClient);
    ActivitiesPostRequest activitiesPostRequest = new ActivitiesPostRequest(); // ActivitiesPostRequest | 
    try {
      EmptySuccessResponse result = apiInstance.activitiesPost(activitiesPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivitiesApi#activitiesPost");
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
| **activitiesPostRequest** | [**ActivitiesPostRequest**](ActivitiesPostRequest.md)|  | |

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **403** | Forbidden |  -  |
| **422** | Validation error |  -  |

