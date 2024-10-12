# LabelsApi

All URIs are relative to */api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteLabelsID**](LabelsApi.md#deleteLabelsID) | **DELETE** /labels/{labelID} | Delete a label |
| [**getLabels**](LabelsApi.md#getLabels) | **GET** /labels | List all labels |
| [**getLabelsID**](LabelsApi.md#getLabelsID) | **GET** /labels/{labelID} | Retrieve a label |
| [**patchLabelsID**](LabelsApi.md#patchLabelsID) | **PATCH** /labels/{labelID} | Update a label |
| [**postLabels**](LabelsApi.md#postLabels) | **POST** /labels | Create a label |


<a id="deleteLabelsID"></a>
# **deleteLabelsID**
> deleteLabelsID(labelID, zapTraceSpan)

Delete a label

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LabelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    LabelsApi apiInstance = new LabelsApi(defaultClient);
    String labelID = "labelID_example"; // String | The ID of the label to delete.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      apiInstance.deleteLabelsID(labelID, zapTraceSpan);
    } catch (ApiException e) {
      System.err.println("Exception when calling LabelsApi#deleteLabelsID");
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
| **labelID** | **String**| The ID of the label to delete. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Delete has been accepted |  -  |
| **404** | Label not found |  -  |
| **0** | Unexpected error |  -  |

<a id="getLabels"></a>
# **getLabels**
> LabelsResponse getLabels(zapTraceSpan, orgID)

List all labels

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LabelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    LabelsApi apiInstance = new LabelsApi(defaultClient);
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    String orgID = "orgID_example"; // String | The organization ID.
    try {
      LabelsResponse result = apiInstance.getLabels(zapTraceSpan, orgID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LabelsApi#getLabels");
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
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |
| **orgID** | **String**| The organization ID. | [optional] |

### Return type

[**LabelsResponse**](LabelsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of labels |  -  |
| **0** | Unexpected error |  -  |

<a id="getLabelsID"></a>
# **getLabelsID**
> LabelResponse getLabelsID(labelID, zapTraceSpan)

Retrieve a label

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LabelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    LabelsApi apiInstance = new LabelsApi(defaultClient);
    String labelID = "labelID_example"; // String | The ID of the label to update.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      LabelResponse result = apiInstance.getLabelsID(labelID, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LabelsApi#getLabelsID");
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
| **labelID** | **String**| The ID of the label to update. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**LabelResponse**](LabelResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A label |  -  |
| **0** | Unexpected error |  -  |

<a id="patchLabelsID"></a>
# **patchLabelsID**
> LabelResponse patchLabelsID(labelID, labelUpdate, zapTraceSpan)

Update a label

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LabelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    LabelsApi apiInstance = new LabelsApi(defaultClient);
    String labelID = "labelID_example"; // String | The ID of the label to update.
    LabelUpdate labelUpdate = new LabelUpdate(); // LabelUpdate | Label update
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      LabelResponse result = apiInstance.patchLabelsID(labelID, labelUpdate, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LabelsApi#patchLabelsID");
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
| **labelID** | **String**| The ID of the label to update. | |
| **labelUpdate** | [**LabelUpdate**](LabelUpdate.md)| Label update | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**LabelResponse**](LabelResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated label |  -  |
| **404** | Label not found |  -  |
| **0** | Unexpected error |  -  |

<a id="postLabels"></a>
# **postLabels**
> LabelResponse postLabels(labelCreateRequest)

Create a label

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LabelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    LabelsApi apiInstance = new LabelsApi(defaultClient);
    LabelCreateRequest labelCreateRequest = new LabelCreateRequest(); // LabelCreateRequest | Label to create
    try {
      LabelResponse result = apiInstance.postLabels(labelCreateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LabelsApi#postLabels");
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
| **labelCreateRequest** | [**LabelCreateRequest**](LabelCreateRequest.md)| Label to create | |

### Return type

[**LabelResponse**](LabelResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Added label |  -  |
| **0** | Unexpected error |  -  |

