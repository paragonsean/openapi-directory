# ReferencesApi

All URIs are relative to *https://api.exhibitday.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**referencesEventCostTypes0Get**](ReferencesApi.md#referencesEventCostTypes0Get) | **GET** /v1/references/event_cost_types |  |
| [**referencesEventCustomFields0Get**](ReferencesApi.md#referencesEventCustomFields0Get) | **GET** /v1/references/event_custom_fields |  |
| [**referencesEventParticipationTypes0Get**](ReferencesApi.md#referencesEventParticipationTypes0Get) | **GET** /v1/references/event_participation_types |  |
| [**referencesEventTags0Get**](ReferencesApi.md#referencesEventTags0Get) | **GET** /v1/references/event_tags |  |
| [**referencesUsersAndResources0Get**](ReferencesApi.md#referencesUsersAndResources0Get) | **GET** /v1/references/users_and_resources |  |


<a id="referencesEventCostTypes0Get"></a>
# **referencesEventCostTypes0Get**
> String referencesEventCostTypes0Get(apiKey)



Event Cost Types

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReferencesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.exhibitday.com");

    ReferencesApi apiInstance = new ReferencesApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    try {
      String result = apiInstance.referencesEventCostTypes0Get(apiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReferencesApi#referencesEventCostTypes0Get");
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
| **apiKey** | **String**|  | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="referencesEventCustomFields0Get"></a>
# **referencesEventCustomFields0Get**
> String referencesEventCustomFields0Get(apiKey)



Event Custom Fields

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReferencesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.exhibitday.com");

    ReferencesApi apiInstance = new ReferencesApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    try {
      String result = apiInstance.referencesEventCustomFields0Get(apiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReferencesApi#referencesEventCustomFields0Get");
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
| **apiKey** | **String**|  | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="referencesEventParticipationTypes0Get"></a>
# **referencesEventParticipationTypes0Get**
> String referencesEventParticipationTypes0Get(apiKey)



Event Participation Types

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReferencesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.exhibitday.com");

    ReferencesApi apiInstance = new ReferencesApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    try {
      String result = apiInstance.referencesEventParticipationTypes0Get(apiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReferencesApi#referencesEventParticipationTypes0Get");
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
| **apiKey** | **String**|  | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="referencesEventTags0Get"></a>
# **referencesEventTags0Get**
> String referencesEventTags0Get(apiKey)



Event Tags

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReferencesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.exhibitday.com");

    ReferencesApi apiInstance = new ReferencesApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    try {
      String result = apiInstance.referencesEventTags0Get(apiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReferencesApi#referencesEventTags0Get");
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
| **apiKey** | **String**|  | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="referencesUsersAndResources0Get"></a>
# **referencesUsersAndResources0Get**
> String referencesUsersAndResources0Get(apiKey)



User and Resources

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReferencesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.exhibitday.com");

    ReferencesApi apiInstance = new ReferencesApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    try {
      String result = apiInstance.referencesUsersAndResources0Get(apiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReferencesApi#referencesUsersAndResources0Get");
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
| **apiKey** | **String**|  | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

