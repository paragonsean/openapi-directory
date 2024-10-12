# AgentsApi

All URIs are relative to *https://secure.agco-ats.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**agentsDeleteAgent**](AgentsApi.md#agentsDeleteAgent) | **DELETE** /api/v2/agents/{agentID} | Delete an Agent |
| [**agentsGetAgentActivityRun**](AgentsApi.md#agentsGetAgentActivityRun) | **GET** /api/v2/agents/{agentID}/ActivityRun | Get an Agent&#39;s ActivityRun |
| [**agentsGetAgentAsync**](AgentsApi.md#agentsGetAgentAsync) | **GET** /api/v2/agents/{agentID} | Get Agent |
| [**agentsGetAgents**](AgentsApi.md#agentsGetAgents) | **GET** /api/v2/agents | Get Agents |
| [**agentsGetCurrentAgentActivityRun**](AgentsApi.md#agentsGetCurrentAgentActivityRun) | **GET** /api/v2/agents/Current/ActivityRun | Get the ActivityRun of Agent associated with the current user |
| [**agentsGetCurrentAgentAsync**](AgentsApi.md#agentsGetCurrentAgentAsync) | **GET** /api/v2/agents/Current | Get Agent associated with the current user |
| [**agentsPostAgent**](AgentsApi.md#agentsPostAgent) | **POST** /api/v2/agents | Create an Agent |
| [**agentsPutAgent**](AgentsApi.md#agentsPutAgent) | **PUT** /api/v2/agents/{agentID} | Update an Agent |
| [**agentsPutAgentActivityRun**](AgentsApi.md#agentsPutAgentActivityRun) | **PUT** /api/v2/agents/{agentID}/ActivityRun | Update the ActivityRun assigned to the Agent. |
| [**agentsPutAgentStatus**](AgentsApi.md#agentsPutAgentStatus) | **PUT** /api/v2/agents/{agentID}/Status | Update an Agent |


<a id="agentsDeleteAgent"></a>
# **agentsDeleteAgent**
> agentsDeleteAgent(agentID)

Delete an Agent

Deletes an Agent. When successful, the response is empty.  If unsuccessful, an appropriate              ApiError is returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    AgentsApi apiInstance = new AgentsApi(defaultClient);
    Integer agentID = 56; // Integer | The id of the Agent to delete.
    try {
      apiInstance.agentsDeleteAgent(agentID);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentsApi#agentsDeleteAgent");
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
| **agentID** | **Integer**| The id of the Agent to delete. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | API Error Response |  -  |

<a id="agentsGetAgentActivityRun"></a>
# **agentsGetAgentActivityRun**
> BuildSystemSharedDTOActivityRun agentsGetAgentActivityRun(agentID)

Get an Agent&#39;s ActivityRun

Gets the activity run assigned to an agent.  When successful, the response is the ActivityRun              assigned to the Agent.  If unsuccessful, an appropriate ApiError is returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    AgentsApi apiInstance = new AgentsApi(defaultClient);
    Integer agentID = 56; // Integer | The id of the Agent to get.
    try {
      BuildSystemSharedDTOActivityRun result = apiInstance.agentsGetAgentActivityRun(agentID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentsApi#agentsGetAgentActivityRun");
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
| **agentID** | **Integer**| The id of the Agent to get. | |

### Return type

[**BuildSystemSharedDTOActivityRun**](BuildSystemSharedDTOActivityRun.md)

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

<a id="agentsGetAgentAsync"></a>
# **agentsGetAgentAsync**
> BuildSystemSharedDTOAgent agentsGetAgentAsync(agentID)

Get Agent

Gets an Agent by ID. When successful, the response is the requested Agent.  If unsuccessful,              an appropriate ApiError is returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    AgentsApi apiInstance = new AgentsApi(defaultClient);
    Integer agentID = 56; // Integer | The id of the Agent to get.
    try {
      BuildSystemSharedDTOAgent result = apiInstance.agentsGetAgentAsync(agentID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentsApi#agentsGetAgentAsync");
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
| **agentID** | **Integer**| The id of the Agent to get. | |

### Return type

[**BuildSystemSharedDTOAgent**](BuildSystemSharedDTOAgent.md)

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

<a id="agentsGetAgents"></a>
# **agentsGetAgents**
> APIPagedResponseBuildSystemSharedDTOAgent agentsGetAgents(limit, offset)

Get Agents

Gets a collection of Agents. When successful, the response is a PagedResponse of Agents.                If unsuccessful, an appropriate ApiError is returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    AgentsApi apiInstance = new AgentsApi(defaultClient);
    Integer limit = 56; // Integer | Optional. The page limit.  If not specified, the default page limit is 10.
    Integer offset = 56; // Integer | Optional. The page offset.  If not specified, the default page offset is 0.
    try {
      APIPagedResponseBuildSystemSharedDTOAgent result = apiInstance.agentsGetAgents(limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentsApi#agentsGetAgents");
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

### Return type

[**APIPagedResponseBuildSystemSharedDTOAgent**](APIPagedResponseBuildSystemSharedDTOAgent.md)

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

<a id="agentsGetCurrentAgentActivityRun"></a>
# **agentsGetCurrentAgentActivityRun**
> BuildSystemSharedDTOActivityRun agentsGetCurrentAgentActivityRun()

Get the ActivityRun of Agent associated with the current user

Gets the activity run assigned to an agent.  When successful, the response is the ActivityRun              assigned to the Agent.  If unsuccessful, an appropriate ApiError is returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    AgentsApi apiInstance = new AgentsApi(defaultClient);
    try {
      BuildSystemSharedDTOActivityRun result = apiInstance.agentsGetCurrentAgentActivityRun();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentsApi#agentsGetCurrentAgentActivityRun");
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

[**BuildSystemSharedDTOActivityRun**](BuildSystemSharedDTOActivityRun.md)

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

<a id="agentsGetCurrentAgentAsync"></a>
# **agentsGetCurrentAgentAsync**
> BuildSystemSharedDTOAgent agentsGetCurrentAgentAsync()

Get Agent associated with the current user

Gets the Agent associated with the current user. When successful, the response is the requested Agent.  If unsuccessful,              an appropriate ApiError is returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    AgentsApi apiInstance = new AgentsApi(defaultClient);
    try {
      BuildSystemSharedDTOAgent result = apiInstance.agentsGetCurrentAgentAsync();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentsApi#agentsGetCurrentAgentAsync");
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

[**BuildSystemSharedDTOAgent**](BuildSystemSharedDTOAgent.md)

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

<a id="agentsPostAgent"></a>
# **agentsPostAgent**
> Integer agentsPostAgent(buildSystemSharedDTOAgent)

Create an Agent

Creates an Agent.  The body of the POST is the Agent to create.  The AgentID will be assigned              on creation of the Agent.  When successful, the response is the AgentID.  If unsuccessful, an              appropriate ApiError is returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    AgentsApi apiInstance = new AgentsApi(defaultClient);
    BuildSystemSharedDTOAgent buildSystemSharedDTOAgent = new BuildSystemSharedDTOAgent(); // BuildSystemSharedDTOAgent | The Agent to create.  The AgentID will be assigned on creation of the Agent.
    try {
      Integer result = apiInstance.agentsPostAgent(buildSystemSharedDTOAgent);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentsApi#agentsPostAgent");
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
| **buildSystemSharedDTOAgent** | [**BuildSystemSharedDTOAgent**](BuildSystemSharedDTOAgent.md)| The Agent to create.  The AgentID will be assigned on creation of the Agent. | |

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

<a id="agentsPutAgent"></a>
# **agentsPutAgent**
> agentsPutAgent(agentID, buildSystemSharedDTOAgent)

Update an Agent

Updates an Agent.  The body of the PUT is the updated Agent.  When successful, the response is empty.              If unsuccessful, an appropriate ApiError is returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    AgentsApi apiInstance = new AgentsApi(defaultClient);
    Integer agentID = 56; // Integer | The id of the Agent to update.
    BuildSystemSharedDTOAgent buildSystemSharedDTOAgent = new BuildSystemSharedDTOAgent(); // BuildSystemSharedDTOAgent | The updated Agent
    try {
      apiInstance.agentsPutAgent(agentID, buildSystemSharedDTOAgent);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentsApi#agentsPutAgent");
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
| **agentID** | **Integer**| The id of the Agent to update. | |
| **buildSystemSharedDTOAgent** | [**BuildSystemSharedDTOAgent**](BuildSystemSharedDTOAgent.md)| The updated Agent | |

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

<a id="agentsPutAgentActivityRun"></a>
# **agentsPutAgentActivityRun**
> agentsPutAgentActivityRun(agentID, buildSystemSharedDTOActivityRun)

Update the ActivityRun assigned to the Agent.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    AgentsApi apiInstance = new AgentsApi(defaultClient);
    Integer agentID = 56; // Integer | The id of the Agent to update.
    BuildSystemSharedDTOActivityRun buildSystemSharedDTOActivityRun = new BuildSystemSharedDTOActivityRun(); // BuildSystemSharedDTOActivityRun | The ActivityRun assigned to the agent.  Only the ActivityRunID is used.
    try {
      apiInstance.agentsPutAgentActivityRun(agentID, buildSystemSharedDTOActivityRun);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentsApi#agentsPutAgentActivityRun");
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
| **agentID** | **Integer**| The id of the Agent to update. | |
| **buildSystemSharedDTOActivityRun** | [**BuildSystemSharedDTOActivityRun**](BuildSystemSharedDTOActivityRun.md)| The ActivityRun assigned to the agent.  Only the ActivityRunID is used. | |

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

<a id="agentsPutAgentStatus"></a>
# **agentsPutAgentStatus**
> agentsPutAgentStatus(agentID, buildSystemSharedDTOAgentStatus)

Update an Agent

Updates the status of an Agent.The body of the PUT is the updated Agent status.  When successful,              the response is empty.If unsuccessful, an appropriate ApiError is returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    AgentsApi apiInstance = new AgentsApi(defaultClient);
    Integer agentID = 56; // Integer | The id of the Agent to update.
    BuildSystemSharedDTOAgentStatus buildSystemSharedDTOAgentStatus = new BuildSystemSharedDTOAgentStatus(); // BuildSystemSharedDTOAgentStatus | The updated AgentStatus.
    try {
      apiInstance.agentsPutAgentStatus(agentID, buildSystemSharedDTOAgentStatus);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentsApi#agentsPutAgentStatus");
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
| **agentID** | **Integer**| The id of the Agent to update. | |
| **buildSystemSharedDTOAgentStatus** | [**BuildSystemSharedDTOAgentStatus**](BuildSystemSharedDTOAgentStatus.md)| The updated AgentStatus. | |

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

