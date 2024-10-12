# ChecksApi

All URIs are relative to */api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createCheck**](ChecksApi.md#createCheck) | **POST** /checks | Add new check |
| [**deleteChecksID**](ChecksApi.md#deleteChecksID) | **DELETE** /checks/{checkID} | Delete a check |
| [**deleteChecksIDLabelsID**](ChecksApi.md#deleteChecksIDLabelsID) | **DELETE** /checks/{checkID}/labels/{labelID} | Delete label from a check |
| [**getChecks**](ChecksApi.md#getChecks) | **GET** /checks | List all checks |
| [**getChecksID**](ChecksApi.md#getChecksID) | **GET** /checks/{checkID} | Retrieve a check |
| [**getChecksIDLabels**](ChecksApi.md#getChecksIDLabels) | **GET** /checks/{checkID}/labels | List all labels for a check |
| [**getChecksIDQuery**](ChecksApi.md#getChecksIDQuery) | **GET** /checks/{checkID}/query | Retrieve a check query |
| [**patchChecksID**](ChecksApi.md#patchChecksID) | **PATCH** /checks/{checkID} | Update a check |
| [**postChecksIDLabels**](ChecksApi.md#postChecksIDLabels) | **POST** /checks/{checkID}/labels | Add a label to a check |
| [**putChecksID**](ChecksApi.md#putChecksID) | **PUT** /checks/{checkID} | Update a check |


<a id="createCheck"></a>
# **createCheck**
> Check createCheck(postCheck)

Add new check

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChecksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    ChecksApi apiInstance = new ChecksApi(defaultClient);
    PostCheck postCheck = new PostCheck(); // PostCheck | Check to create
    try {
      Check result = apiInstance.createCheck(postCheck);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChecksApi#createCheck");
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
| **postCheck** | [**PostCheck**](PostCheck.md)| Check to create | |

### Return type

[**Check**](Check.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Check created |  -  |
| **0** | Unexpected error |  -  |

<a id="deleteChecksID"></a>
# **deleteChecksID**
> deleteChecksID(checkID, zapTraceSpan)

Delete a check

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChecksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    ChecksApi apiInstance = new ChecksApi(defaultClient);
    String checkID = "checkID_example"; // String | The check ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      apiInstance.deleteChecksID(checkID, zapTraceSpan);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChecksApi#deleteChecksID");
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
| **checkID** | **String**| The check ID. | |
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
| **404** | The check was not found |  -  |
| **0** | Unexpected error |  -  |

<a id="deleteChecksIDLabelsID"></a>
# **deleteChecksIDLabelsID**
> deleteChecksIDLabelsID(checkID, labelID, zapTraceSpan)

Delete label from a check

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChecksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    ChecksApi apiInstance = new ChecksApi(defaultClient);
    String checkID = "checkID_example"; // String | The check ID.
    String labelID = "labelID_example"; // String | The ID of the label to delete.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      apiInstance.deleteChecksIDLabelsID(checkID, labelID, zapTraceSpan);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChecksApi#deleteChecksIDLabelsID");
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
| **checkID** | **String**| The check ID. | |
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
| **404** | Check or label not found |  -  |
| **0** | Unexpected error |  -  |

<a id="getChecks"></a>
# **getChecks**
> Checks getChecks(orgID, zapTraceSpan, offset, limit)

List all checks

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChecksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    ChecksApi apiInstance = new ChecksApi(defaultClient);
    String orgID = "orgID_example"; // String | Only show checks that belong to a specific organization ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    Integer offset = 56; // Integer | 
    Integer limit = 20; // Integer | 
    try {
      Checks result = apiInstance.getChecks(orgID, zapTraceSpan, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChecksApi#getChecks");
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
| **orgID** | **String**| Only show checks that belong to a specific organization ID. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |
| **offset** | **Integer**|  | [optional] |
| **limit** | **Integer**|  | [optional] [default to 20] |

### Return type

[**Checks**](Checks.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of checks |  -  |
| **0** | Unexpected error |  -  |

<a id="getChecksID"></a>
# **getChecksID**
> Check getChecksID(checkID, zapTraceSpan)

Retrieve a check

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChecksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    ChecksApi apiInstance = new ChecksApi(defaultClient);
    String checkID = "checkID_example"; // String | The check ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      Check result = apiInstance.getChecksID(checkID, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChecksApi#getChecksID");
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
| **checkID** | **String**| The check ID. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**Check**](Check.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The check requested |  -  |
| **0** | Unexpected error |  -  |

<a id="getChecksIDLabels"></a>
# **getChecksIDLabels**
> LabelsResponse getChecksIDLabels(checkID, zapTraceSpan)

List all labels for a check

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChecksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    ChecksApi apiInstance = new ChecksApi(defaultClient);
    String checkID = "checkID_example"; // String | The check ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      LabelsResponse result = apiInstance.getChecksIDLabels(checkID, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChecksApi#getChecksIDLabels");
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
| **checkID** | **String**| The check ID. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

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
| **200** | A list of all labels for a check |  -  |
| **0** | Unexpected error |  -  |

<a id="getChecksIDQuery"></a>
# **getChecksIDQuery**
> FluxResponse getChecksIDQuery(checkID, zapTraceSpan)

Retrieve a check query

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChecksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    ChecksApi apiInstance = new ChecksApi(defaultClient);
    String checkID = "checkID_example"; // String | The check ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      FluxResponse result = apiInstance.getChecksIDQuery(checkID, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChecksApi#getChecksIDQuery");
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
| **checkID** | **String**| The check ID. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**FluxResponse**](FluxResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The check query requested |  -  |
| **400** | Invalid request |  -  |
| **404** | Check not found |  -  |
| **0** | Unexpected error |  -  |

<a id="patchChecksID"></a>
# **patchChecksID**
> Check patchChecksID(checkID, checkPatch, zapTraceSpan)

Update a check

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChecksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    ChecksApi apiInstance = new ChecksApi(defaultClient);
    String checkID = "checkID_example"; // String | The check ID.
    CheckPatch checkPatch = new CheckPatch(); // CheckPatch | Check update to apply
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      Check result = apiInstance.patchChecksID(checkID, checkPatch, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChecksApi#patchChecksID");
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
| **checkID** | **String**| The check ID. | |
| **checkPatch** | [**CheckPatch**](CheckPatch.md)| Check update to apply | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**Check**](Check.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An updated check |  -  |
| **404** | The check was not found |  -  |
| **0** | Unexpected error |  -  |

<a id="postChecksIDLabels"></a>
# **postChecksIDLabels**
> LabelResponse postChecksIDLabels(checkID, labelMapping, zapTraceSpan)

Add a label to a check

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChecksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    ChecksApi apiInstance = new ChecksApi(defaultClient);
    String checkID = "checkID_example"; // String | The check ID.
    LabelMapping labelMapping = new LabelMapping(); // LabelMapping | Label to add
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      LabelResponse result = apiInstance.postChecksIDLabels(checkID, labelMapping, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChecksApi#postChecksIDLabels");
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
| **checkID** | **String**| The check ID. | |
| **labelMapping** | [**LabelMapping**](LabelMapping.md)| Label to add | |
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
| **201** | The label was added to the check |  -  |
| **0** | Unexpected error |  -  |

<a id="putChecksID"></a>
# **putChecksID**
> Check putChecksID(checkID, check, zapTraceSpan)

Update a check

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChecksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    ChecksApi apiInstance = new ChecksApi(defaultClient);
    String checkID = "checkID_example"; // String | The check ID.
    Check check = new Check(); // Check | Check update to apply
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      Check result = apiInstance.putChecksID(checkID, check, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChecksApi#putChecksID");
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
| **checkID** | **String**| The check ID. | |
| **check** | [**Check**](Check.md)| Check update to apply | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**Check**](Check.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An updated check |  -  |
| **404** | The check was not found |  -  |
| **0** | Unexpected error |  -  |

