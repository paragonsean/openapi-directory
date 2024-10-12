# TelegrafsApi

All URIs are relative to */api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteTelegrafsID**](TelegrafsApi.md#deleteTelegrafsID) | **DELETE** /telegrafs/{telegrafID} | Delete a Telegraf configuration |
| [**deleteTelegrafsIDLabelsID**](TelegrafsApi.md#deleteTelegrafsIDLabelsID) | **DELETE** /telegrafs/{telegrafID}/labels/{labelID} | Delete a label from a Telegraf config |
| [**deleteTelegrafsIDMembersID**](TelegrafsApi.md#deleteTelegrafsIDMembersID) | **DELETE** /telegrafs/{telegrafID}/members/{userID} | Remove a member from a Telegraf config |
| [**deleteTelegrafsIDOwnersID**](TelegrafsApi.md#deleteTelegrafsIDOwnersID) | **DELETE** /telegrafs/{telegrafID}/owners/{userID} | Remove an owner from a Telegraf config |
| [**getTelegrafs**](TelegrafsApi.md#getTelegrafs) | **GET** /telegrafs | List all Telegraf configurations |
| [**getTelegrafsID**](TelegrafsApi.md#getTelegrafsID) | **GET** /telegrafs/{telegrafID} | Retrieve a Telegraf configuration |
| [**getTelegrafsIDLabels**](TelegrafsApi.md#getTelegrafsIDLabels) | **GET** /telegrafs/{telegrafID}/labels | List all labels for a Telegraf config |
| [**getTelegrafsIDMembers**](TelegrafsApi.md#getTelegrafsIDMembers) | **GET** /telegrafs/{telegrafID}/members | List all users with member privileges for a Telegraf config |
| [**getTelegrafsIDOwners**](TelegrafsApi.md#getTelegrafsIDOwners) | **GET** /telegrafs/{telegrafID}/owners | List all owners of a Telegraf configuration |
| [**postTelegrafs**](TelegrafsApi.md#postTelegrafs) | **POST** /telegrafs | Create a Telegraf configuration |
| [**postTelegrafsIDLabels**](TelegrafsApi.md#postTelegrafsIDLabels) | **POST** /telegrafs/{telegrafID}/labels | Add a label to a Telegraf config |
| [**postTelegrafsIDMembers**](TelegrafsApi.md#postTelegrafsIDMembers) | **POST** /telegrafs/{telegrafID}/members | Add a member to a Telegraf config |
| [**postTelegrafsIDOwners**](TelegrafsApi.md#postTelegrafsIDOwners) | **POST** /telegrafs/{telegrafID}/owners | Add an owner to a Telegraf configuration |
| [**putTelegrafsID**](TelegrafsApi.md#putTelegrafsID) | **PUT** /telegrafs/{telegrafID} | Update a Telegraf configuration |


<a id="deleteTelegrafsID"></a>
# **deleteTelegrafsID**
> deleteTelegrafsID(telegrafID, zapTraceSpan)

Delete a Telegraf configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TelegrafsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    TelegrafsApi apiInstance = new TelegrafsApi(defaultClient);
    String telegrafID = "telegrafID_example"; // String | The Telegraf configuration ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      apiInstance.deleteTelegrafsID(telegrafID, zapTraceSpan);
    } catch (ApiException e) {
      System.err.println("Exception when calling TelegrafsApi#deleteTelegrafsID");
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
| **telegrafID** | **String**| The Telegraf configuration ID. | |
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
| **0** | Unexpected error |  -  |

<a id="deleteTelegrafsIDLabelsID"></a>
# **deleteTelegrafsIDLabelsID**
> deleteTelegrafsIDLabelsID(telegrafID, labelID, zapTraceSpan)

Delete a label from a Telegraf config

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TelegrafsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    TelegrafsApi apiInstance = new TelegrafsApi(defaultClient);
    String telegrafID = "telegrafID_example"; // String | The Telegraf config ID.
    String labelID = "labelID_example"; // String | The label ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      apiInstance.deleteTelegrafsIDLabelsID(telegrafID, labelID, zapTraceSpan);
    } catch (ApiException e) {
      System.err.println("Exception when calling TelegrafsApi#deleteTelegrafsIDLabelsID");
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
| **telegrafID** | **String**| The Telegraf config ID. | |
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
| **404** | Telegraf config not found |  -  |
| **0** | Unexpected error |  -  |

<a id="deleteTelegrafsIDMembersID"></a>
# **deleteTelegrafsIDMembersID**
> deleteTelegrafsIDMembersID(userID, telegrafID, zapTraceSpan)

Remove a member from a Telegraf config

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TelegrafsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    TelegrafsApi apiInstance = new TelegrafsApi(defaultClient);
    String userID = "userID_example"; // String | The ID of the member to remove.
    String telegrafID = "telegrafID_example"; // String | The Telegraf config ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      apiInstance.deleteTelegrafsIDMembersID(userID, telegrafID, zapTraceSpan);
    } catch (ApiException e) {
      System.err.println("Exception when calling TelegrafsApi#deleteTelegrafsIDMembersID");
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
| **userID** | **String**| The ID of the member to remove. | |
| **telegrafID** | **String**| The Telegraf config ID. | |
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

<a id="deleteTelegrafsIDOwnersID"></a>
# **deleteTelegrafsIDOwnersID**
> deleteTelegrafsIDOwnersID(userID, telegrafID, zapTraceSpan)

Remove an owner from a Telegraf config

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TelegrafsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    TelegrafsApi apiInstance = new TelegrafsApi(defaultClient);
    String userID = "userID_example"; // String | The ID of the owner to remove.
    String telegrafID = "telegrafID_example"; // String | The Telegraf config ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      apiInstance.deleteTelegrafsIDOwnersID(userID, telegrafID, zapTraceSpan);
    } catch (ApiException e) {
      System.err.println("Exception when calling TelegrafsApi#deleteTelegrafsIDOwnersID");
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
| **userID** | **String**| The ID of the owner to remove. | |
| **telegrafID** | **String**| The Telegraf config ID. | |
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

<a id="getTelegrafs"></a>
# **getTelegrafs**
> Telegrafs getTelegrafs(zapTraceSpan, orgID)

List all Telegraf configurations

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TelegrafsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    TelegrafsApi apiInstance = new TelegrafsApi(defaultClient);
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    String orgID = "orgID_example"; // String | The organization ID the Telegraf config belongs to.
    try {
      Telegrafs result = apiInstance.getTelegrafs(zapTraceSpan, orgID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TelegrafsApi#getTelegrafs");
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
| **orgID** | **String**| The organization ID the Telegraf config belongs to. | [optional] |

### Return type

[**Telegrafs**](Telegrafs.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of Telegraf configurations |  -  |
| **0** | Unexpected error |  -  |

<a id="getTelegrafsID"></a>
# **getTelegrafsID**
> Telegraf getTelegrafsID(telegrafID, zapTraceSpan, accept)

Retrieve a Telegraf configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TelegrafsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    TelegrafsApi apiInstance = new TelegrafsApi(defaultClient);
    String telegrafID = "telegrafID_example"; // String | The Telegraf configuration ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    String accept = "application/toml"; // String | 
    try {
      Telegraf result = apiInstance.getTelegrafsID(telegrafID, zapTraceSpan, accept);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TelegrafsApi#getTelegrafsID");
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
| **telegrafID** | **String**| The Telegraf configuration ID. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |
| **accept** | **String**|  | [optional] [default to application/toml] [enum: application/toml, application/json, application/octet-stream] |

### Return type

[**Telegraf**](Telegraf.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream, application/toml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Telegraf configuration details |  -  |
| **0** | Unexpected error |  -  |

<a id="getTelegrafsIDLabels"></a>
# **getTelegrafsIDLabels**
> LabelsResponse getTelegrafsIDLabels(telegrafID, zapTraceSpan)

List all labels for a Telegraf config

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TelegrafsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    TelegrafsApi apiInstance = new TelegrafsApi(defaultClient);
    String telegrafID = "telegrafID_example"; // String | The Telegraf config ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      LabelsResponse result = apiInstance.getTelegrafsIDLabels(telegrafID, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TelegrafsApi#getTelegrafsIDLabels");
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
| **telegrafID** | **String**| The Telegraf config ID. | |
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
| **200** | A list of all labels for a Telegraf config |  -  |
| **0** | Unexpected error |  -  |

<a id="getTelegrafsIDMembers"></a>
# **getTelegrafsIDMembers**
> ResourceMembers getTelegrafsIDMembers(telegrafID, zapTraceSpan)

List all users with member privileges for a Telegraf config

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TelegrafsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    TelegrafsApi apiInstance = new TelegrafsApi(defaultClient);
    String telegrafID = "telegrafID_example"; // String | The Telegraf config ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      ResourceMembers result = apiInstance.getTelegrafsIDMembers(telegrafID, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TelegrafsApi#getTelegrafsIDMembers");
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
| **telegrafID** | **String**| The Telegraf config ID. | |
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
| **200** | A list of Telegraf config members |  -  |
| **0** | Unexpected error |  -  |

<a id="getTelegrafsIDOwners"></a>
# **getTelegrafsIDOwners**
> ResourceOwners getTelegrafsIDOwners(telegrafID, zapTraceSpan)

List all owners of a Telegraf configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TelegrafsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    TelegrafsApi apiInstance = new TelegrafsApi(defaultClient);
    String telegrafID = "telegrafID_example"; // String | The Telegraf configuration ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      ResourceOwners result = apiInstance.getTelegrafsIDOwners(telegrafID, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TelegrafsApi#getTelegrafsIDOwners");
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
| **telegrafID** | **String**| The Telegraf configuration ID. | |
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
| **200** | Returns Telegraf configuration owners as a ResourceOwners list |  -  |
| **0** | Unexpected error |  -  |

<a id="postTelegrafs"></a>
# **postTelegrafs**
> Telegraf postTelegrafs(telegrafRequest, zapTraceSpan)

Create a Telegraf configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TelegrafsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    TelegrafsApi apiInstance = new TelegrafsApi(defaultClient);
    TelegrafRequest telegrafRequest = new TelegrafRequest(); // TelegrafRequest | Telegraf configuration to create
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      Telegraf result = apiInstance.postTelegrafs(telegrafRequest, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TelegrafsApi#postTelegrafs");
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
| **telegrafRequest** | [**TelegrafRequest**](TelegrafRequest.md)| Telegraf configuration to create | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**Telegraf**](Telegraf.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Telegraf configuration created |  -  |
| **0** | Unexpected error |  -  |

<a id="postTelegrafsIDLabels"></a>
# **postTelegrafsIDLabels**
> LabelResponse postTelegrafsIDLabels(telegrafID, labelMapping, zapTraceSpan)

Add a label to a Telegraf config

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TelegrafsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    TelegrafsApi apiInstance = new TelegrafsApi(defaultClient);
    String telegrafID = "telegrafID_example"; // String | The Telegraf config ID.
    LabelMapping labelMapping = new LabelMapping(); // LabelMapping | Label to add
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      LabelResponse result = apiInstance.postTelegrafsIDLabels(telegrafID, labelMapping, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TelegrafsApi#postTelegrafsIDLabels");
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
| **telegrafID** | **String**| The Telegraf config ID. | |
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
| **201** | The label added to the Telegraf config |  -  |
| **0** | Unexpected error |  -  |

<a id="postTelegrafsIDMembers"></a>
# **postTelegrafsIDMembers**
> ResourceMember postTelegrafsIDMembers(telegrafID, addResourceMemberRequestBody, zapTraceSpan)

Add a member to a Telegraf config

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TelegrafsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    TelegrafsApi apiInstance = new TelegrafsApi(defaultClient);
    String telegrafID = "telegrafID_example"; // String | The Telegraf config ID.
    AddResourceMemberRequestBody addResourceMemberRequestBody = new AddResourceMemberRequestBody(); // AddResourceMemberRequestBody | User to add as member
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      ResourceMember result = apiInstance.postTelegrafsIDMembers(telegrafID, addResourceMemberRequestBody, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TelegrafsApi#postTelegrafsIDMembers");
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
| **telegrafID** | **String**| The Telegraf config ID. | |
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
| **201** | Member added to Telegraf config |  -  |
| **0** | Unexpected error |  -  |

<a id="postTelegrafsIDOwners"></a>
# **postTelegrafsIDOwners**
> ResourceOwner postTelegrafsIDOwners(telegrafID, addResourceMemberRequestBody, zapTraceSpan)

Add an owner to a Telegraf configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TelegrafsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    TelegrafsApi apiInstance = new TelegrafsApi(defaultClient);
    String telegrafID = "telegrafID_example"; // String | The Telegraf configuration ID.
    AddResourceMemberRequestBody addResourceMemberRequestBody = new AddResourceMemberRequestBody(); // AddResourceMemberRequestBody | User to add as owner
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      ResourceOwner result = apiInstance.postTelegrafsIDOwners(telegrafID, addResourceMemberRequestBody, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TelegrafsApi#postTelegrafsIDOwners");
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
| **telegrafID** | **String**| The Telegraf configuration ID. | |
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
| **201** | Telegraf configuration owner was added. Returns a ResourceOwner that references the User. |  -  |
| **0** | Unexpected error |  -  |

<a id="putTelegrafsID"></a>
# **putTelegrafsID**
> Telegraf putTelegrafsID(telegrafID, telegrafRequest, zapTraceSpan)

Update a Telegraf configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TelegrafsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    TelegrafsApi apiInstance = new TelegrafsApi(defaultClient);
    String telegrafID = "telegrafID_example"; // String | The Telegraf config ID.
    TelegrafRequest telegrafRequest = new TelegrafRequest(); // TelegrafRequest | Telegraf configuration update to apply
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      Telegraf result = apiInstance.putTelegrafsID(telegrafID, telegrafRequest, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TelegrafsApi#putTelegrafsID");
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
| **telegrafID** | **String**| The Telegraf config ID. | |
| **telegrafRequest** | [**TelegrafRequest**](TelegrafRequest.md)| Telegraf configuration update to apply | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**Telegraf**](Telegraf.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An updated Telegraf configurations |  -  |
| **0** | Unexpected error |  -  |

