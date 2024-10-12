# ScraperTargetsApi

All URIs are relative to */api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteScrapersID**](ScraperTargetsApi.md#deleteScrapersID) | **DELETE** /scrapers/{scraperTargetID} | Delete a scraper target |
| [**deleteScrapersIDLabelsID**](ScraperTargetsApi.md#deleteScrapersIDLabelsID) | **DELETE** /scrapers/{scraperTargetID}/labels/{labelID} | Delete a label from a scraper target |
| [**deleteScrapersIDMembersID**](ScraperTargetsApi.md#deleteScrapersIDMembersID) | **DELETE** /scrapers/{scraperTargetID}/members/{userID} | Remove a member from a scraper target |
| [**deleteScrapersIDOwnersID**](ScraperTargetsApi.md#deleteScrapersIDOwnersID) | **DELETE** /scrapers/{scraperTargetID}/owners/{userID} | Remove an owner from a scraper target |
| [**getScrapers**](ScraperTargetsApi.md#getScrapers) | **GET** /scrapers | List all scraper targets |
| [**getScrapersID**](ScraperTargetsApi.md#getScrapersID) | **GET** /scrapers/{scraperTargetID} | Retrieve a scraper target |
| [**getScrapersIDLabels**](ScraperTargetsApi.md#getScrapersIDLabels) | **GET** /scrapers/{scraperTargetID}/labels | List all labels for a scraper target |
| [**getScrapersIDMembers**](ScraperTargetsApi.md#getScrapersIDMembers) | **GET** /scrapers/{scraperTargetID}/members | List all users with member privileges for a scraper target |
| [**getScrapersIDOwners**](ScraperTargetsApi.md#getScrapersIDOwners) | **GET** /scrapers/{scraperTargetID}/owners | List all owners of a scraper target |
| [**patchScrapersID**](ScraperTargetsApi.md#patchScrapersID) | **PATCH** /scrapers/{scraperTargetID} | Update a scraper target |
| [**postScrapers**](ScraperTargetsApi.md#postScrapers) | **POST** /scrapers | Create a scraper target |
| [**postScrapersIDLabels**](ScraperTargetsApi.md#postScrapersIDLabels) | **POST** /scrapers/{scraperTargetID}/labels | Add a label to a scraper target |
| [**postScrapersIDMembers**](ScraperTargetsApi.md#postScrapersIDMembers) | **POST** /scrapers/{scraperTargetID}/members | Add a member to a scraper target |
| [**postScrapersIDOwners**](ScraperTargetsApi.md#postScrapersIDOwners) | **POST** /scrapers/{scraperTargetID}/owners | Add an owner to a scraper target |


<a id="deleteScrapersID"></a>
# **deleteScrapersID**
> deleteScrapersID(scraperTargetID, zapTraceSpan)

Delete a scraper target

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScraperTargetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    ScraperTargetsApi apiInstance = new ScraperTargetsApi(defaultClient);
    String scraperTargetID = "scraperTargetID_example"; // String | The identifier of the scraper target.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      apiInstance.deleteScrapersID(scraperTargetID, zapTraceSpan);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScraperTargetsApi#deleteScrapersID");
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
| **scraperTargetID** | **String**| The identifier of the scraper target. | |
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
| **204** | Scraper target deleted |  -  |
| **0** | Internal server error |  -  |

<a id="deleteScrapersIDLabelsID"></a>
# **deleteScrapersIDLabelsID**
> deleteScrapersIDLabelsID(scraperTargetID, labelID, zapTraceSpan)

Delete a label from a scraper target

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScraperTargetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    ScraperTargetsApi apiInstance = new ScraperTargetsApi(defaultClient);
    String scraperTargetID = "scraperTargetID_example"; // String | The scraper target ID.
    String labelID = "labelID_example"; // String | The label ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      apiInstance.deleteScrapersIDLabelsID(scraperTargetID, labelID, zapTraceSpan);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScraperTargetsApi#deleteScrapersIDLabelsID");
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
| **scraperTargetID** | **String**| The scraper target ID. | |
| **labelID** | **String**| The label ID. | |
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
| **404** | Scraper target not found |  -  |
| **0** | Unexpected error |  -  |

<a id="deleteScrapersIDMembersID"></a>
# **deleteScrapersIDMembersID**
> deleteScrapersIDMembersID(userID, scraperTargetID, zapTraceSpan)

Remove a member from a scraper target

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScraperTargetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    ScraperTargetsApi apiInstance = new ScraperTargetsApi(defaultClient);
    String userID = "userID_example"; // String | The ID of member to remove.
    String scraperTargetID = "scraperTargetID_example"; // String | The scraper target ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      apiInstance.deleteScrapersIDMembersID(userID, scraperTargetID, zapTraceSpan);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScraperTargetsApi#deleteScrapersIDMembersID");
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
| **userID** | **String**| The ID of member to remove. | |
| **scraperTargetID** | **String**| The scraper target ID. | |
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
| **204** | Member removed |  -  |
| **0** | Unexpected error |  -  |

<a id="deleteScrapersIDOwnersID"></a>
# **deleteScrapersIDOwnersID**
> deleteScrapersIDOwnersID(userID, scraperTargetID, zapTraceSpan)

Remove an owner from a scraper target

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScraperTargetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    ScraperTargetsApi apiInstance = new ScraperTargetsApi(defaultClient);
    String userID = "userID_example"; // String | The ID of owner to remove.
    String scraperTargetID = "scraperTargetID_example"; // String | The scraper target ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      apiInstance.deleteScrapersIDOwnersID(userID, scraperTargetID, zapTraceSpan);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScraperTargetsApi#deleteScrapersIDOwnersID");
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
| **userID** | **String**| The ID of owner to remove. | |
| **scraperTargetID** | **String**| The scraper target ID. | |
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
| **204** | Owner removed |  -  |
| **0** | Unexpected error |  -  |

<a id="getScrapers"></a>
# **getScrapers**
> ScraperTargetResponses getScrapers(zapTraceSpan, name, id, orgID, org)

List all scraper targets

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScraperTargetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    ScraperTargetsApi apiInstance = new ScraperTargetsApi(defaultClient);
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    String name = "name_example"; // String | Specifies the name of the scraper target.
    List<String> id = Arrays.asList(); // List<String> | List of scraper target IDs to return. If both `id` and `owner` are specified, only `id` is used.
    String orgID = "orgID_example"; // String | Specifies the organization ID of the scraper target.
    String org = "org_example"; // String | Specifies the organization name of the scraper target.
    try {
      ScraperTargetResponses result = apiInstance.getScrapers(zapTraceSpan, name, id, orgID, org);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScraperTargetsApi#getScrapers");
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
| **name** | **String**| Specifies the name of the scraper target. | [optional] |
| **id** | [**List&lt;String&gt;**](String.md)| List of scraper target IDs to return. If both &#x60;id&#x60; and &#x60;owner&#x60; are specified, only &#x60;id&#x60; is used. | [optional] |
| **orgID** | **String**| Specifies the organization ID of the scraper target. | [optional] |
| **org** | **String**| Specifies the organization name of the scraper target. | [optional] |

### Return type

[**ScraperTargetResponses**](ScraperTargetResponses.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All scraper targets |  -  |

<a id="getScrapersID"></a>
# **getScrapersID**
> ScraperTargetResponse getScrapersID(scraperTargetID, zapTraceSpan)

Retrieve a scraper target

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScraperTargetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    ScraperTargetsApi apiInstance = new ScraperTargetsApi(defaultClient);
    String scraperTargetID = "scraperTargetID_example"; // String | The identifier of the scraper target.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      ScraperTargetResponse result = apiInstance.getScrapersID(scraperTargetID, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScraperTargetsApi#getScrapersID");
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
| **scraperTargetID** | **String**| The identifier of the scraper target. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**ScraperTargetResponse**](ScraperTargetResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The scraper target |  -  |
| **0** | Internal server error |  -  |

<a id="getScrapersIDLabels"></a>
# **getScrapersIDLabels**
> LabelsResponse getScrapersIDLabels(scraperTargetID, zapTraceSpan)

List all labels for a scraper target

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScraperTargetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    ScraperTargetsApi apiInstance = new ScraperTargetsApi(defaultClient);
    String scraperTargetID = "scraperTargetID_example"; // String | The scraper target ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      LabelsResponse result = apiInstance.getScrapersIDLabels(scraperTargetID, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScraperTargetsApi#getScrapersIDLabels");
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
| **scraperTargetID** | **String**| The scraper target ID. | |
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
| **200** | A list of labels for a scraper target. |  -  |
| **0** | Unexpected error |  -  |

<a id="getScrapersIDMembers"></a>
# **getScrapersIDMembers**
> ResourceMembers getScrapersIDMembers(scraperTargetID, zapTraceSpan)

List all users with member privileges for a scraper target

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScraperTargetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    ScraperTargetsApi apiInstance = new ScraperTargetsApi(defaultClient);
    String scraperTargetID = "scraperTargetID_example"; // String | The scraper target ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      ResourceMembers result = apiInstance.getScrapersIDMembers(scraperTargetID, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScraperTargetsApi#getScrapersIDMembers");
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
| **scraperTargetID** | **String**| The scraper target ID. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**ResourceMembers**](ResourceMembers.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of scraper target members |  -  |
| **0** | Unexpected error |  -  |

<a id="getScrapersIDOwners"></a>
# **getScrapersIDOwners**
> ResourceOwners getScrapersIDOwners(scraperTargetID, zapTraceSpan)

List all owners of a scraper target

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScraperTargetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    ScraperTargetsApi apiInstance = new ScraperTargetsApi(defaultClient);
    String scraperTargetID = "scraperTargetID_example"; // String | The scraper target ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      ResourceOwners result = apiInstance.getScrapersIDOwners(scraperTargetID, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScraperTargetsApi#getScrapersIDOwners");
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
| **scraperTargetID** | **String**| The scraper target ID. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**ResourceOwners**](ResourceOwners.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of scraper target owners |  -  |
| **0** | Unexpected error |  -  |

<a id="patchScrapersID"></a>
# **patchScrapersID**
> ScraperTargetResponse patchScrapersID(scraperTargetID, scraperTargetRequest, zapTraceSpan)

Update a scraper target

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScraperTargetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    ScraperTargetsApi apiInstance = new ScraperTargetsApi(defaultClient);
    String scraperTargetID = "scraperTargetID_example"; // String | The identifier of the scraper target.
    ScraperTargetRequest scraperTargetRequest = new ScraperTargetRequest(); // ScraperTargetRequest | Scraper target update to apply
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      ScraperTargetResponse result = apiInstance.patchScrapersID(scraperTargetID, scraperTargetRequest, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScraperTargetsApi#patchScrapersID");
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
| **scraperTargetID** | **String**| The identifier of the scraper target. | |
| **scraperTargetRequest** | [**ScraperTargetRequest**](ScraperTargetRequest.md)| Scraper target update to apply | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**ScraperTargetResponse**](ScraperTargetResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Scraper target updated |  -  |
| **0** | Internal server error |  -  |

<a id="postScrapers"></a>
# **postScrapers**
> ScraperTargetResponse postScrapers(scraperTargetRequest, zapTraceSpan)

Create a scraper target

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScraperTargetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    ScraperTargetsApi apiInstance = new ScraperTargetsApi(defaultClient);
    ScraperTargetRequest scraperTargetRequest = new ScraperTargetRequest(); // ScraperTargetRequest | Scraper target to create
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      ScraperTargetResponse result = apiInstance.postScrapers(scraperTargetRequest, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScraperTargetsApi#postScrapers");
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
| **scraperTargetRequest** | [**ScraperTargetRequest**](ScraperTargetRequest.md)| Scraper target to create | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**ScraperTargetResponse**](ScraperTargetResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Scraper target created |  -  |
| **0** | Internal server error |  -  |

<a id="postScrapersIDLabels"></a>
# **postScrapersIDLabels**
> LabelResponse postScrapersIDLabels(scraperTargetID, labelMapping, zapTraceSpan)

Add a label to a scraper target

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScraperTargetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    ScraperTargetsApi apiInstance = new ScraperTargetsApi(defaultClient);
    String scraperTargetID = "scraperTargetID_example"; // String | The scraper target ID.
    LabelMapping labelMapping = new LabelMapping(); // LabelMapping | Label to add
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      LabelResponse result = apiInstance.postScrapersIDLabels(scraperTargetID, labelMapping, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScraperTargetsApi#postScrapersIDLabels");
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
| **scraperTargetID** | **String**| The scraper target ID. | |
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
| **201** | The newly added label |  -  |
| **0** | Unexpected error |  -  |

<a id="postScrapersIDMembers"></a>
# **postScrapersIDMembers**
> ResourceMember postScrapersIDMembers(scraperTargetID, addResourceMemberRequestBody, zapTraceSpan)

Add a member to a scraper target

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScraperTargetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    ScraperTargetsApi apiInstance = new ScraperTargetsApi(defaultClient);
    String scraperTargetID = "scraperTargetID_example"; // String | The scraper target ID.
    AddResourceMemberRequestBody addResourceMemberRequestBody = new AddResourceMemberRequestBody(); // AddResourceMemberRequestBody | User to add as member
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      ResourceMember result = apiInstance.postScrapersIDMembers(scraperTargetID, addResourceMemberRequestBody, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScraperTargetsApi#postScrapersIDMembers");
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
| **scraperTargetID** | **String**| The scraper target ID. | |
| **addResourceMemberRequestBody** | [**AddResourceMemberRequestBody**](AddResourceMemberRequestBody.md)| User to add as member | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**ResourceMember**](ResourceMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Member added to scraper targets |  -  |
| **0** | Unexpected error |  -  |

<a id="postScrapersIDOwners"></a>
# **postScrapersIDOwners**
> ResourceOwner postScrapersIDOwners(scraperTargetID, addResourceMemberRequestBody, zapTraceSpan)

Add an owner to a scraper target

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScraperTargetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    ScraperTargetsApi apiInstance = new ScraperTargetsApi(defaultClient);
    String scraperTargetID = "scraperTargetID_example"; // String | The scraper target ID.
    AddResourceMemberRequestBody addResourceMemberRequestBody = new AddResourceMemberRequestBody(); // AddResourceMemberRequestBody | User to add as owner
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      ResourceOwner result = apiInstance.postScrapersIDOwners(scraperTargetID, addResourceMemberRequestBody, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScraperTargetsApi#postScrapersIDOwners");
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
| **scraperTargetID** | **String**| The scraper target ID. | |
| **addResourceMemberRequestBody** | [**AddResourceMemberRequestBody**](AddResourceMemberRequestBody.md)| User to add as owner | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**ResourceOwner**](ResourceOwner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Scraper target owner added |  -  |
| **0** | Unexpected error |  -  |

