# IncidentsApi

All URIs are relative to *https://api.victorops.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiPublicV1IncidentsAckPatch**](IncidentsApi.md#apiPublicV1IncidentsAckPatch) | **PATCH** /api-public/v1/incidents/ack | Acknowledge an incident or list of incidents |
| [**apiPublicV1IncidentsByUserAckPatch**](IncidentsApi.md#apiPublicV1IncidentsByUserAckPatch) | **PATCH** /api-public/v1/incidents/byUser/ack | Acknowledge all incidents for which a user was paged. |
| [**apiPublicV1IncidentsByUserResolvePatch**](IncidentsApi.md#apiPublicV1IncidentsByUserResolvePatch) | **PATCH** /api-public/v1/incidents/byUser/resolve | Resolve all incidents for which a user was paged. |
| [**apiPublicV1IncidentsGet**](IncidentsApi.md#apiPublicV1IncidentsGet) | **GET** /api-public/v1/incidents | Get current incident information |
| [**apiPublicV1IncidentsPost**](IncidentsApi.md#apiPublicV1IncidentsPost) | **POST** /api-public/v1/incidents | Create a new incident |
| [**apiPublicV1IncidentsReroutePost**](IncidentsApi.md#apiPublicV1IncidentsReroutePost) | **POST** /api-public/v1/incidents/reroute | Reroute one or more incidents to one or more new routable destinations. |
| [**apiPublicV1IncidentsResolvePatch**](IncidentsApi.md#apiPublicV1IncidentsResolvePatch) | **PATCH** /api-public/v1/incidents/resolve | Resolve an incident or list of incidents |


<a id="apiPublicV1IncidentsAckPatch"></a>
# **apiPublicV1IncidentsAckPatch**
> AckOrResolveResponse apiPublicV1IncidentsAckPatch(xVOApiId, xVOApiKey, body)

Acknowledge an incident or list of incidents

The incident(s) must be currently open.  The user supplied must be a valid VictorOps user and a member of your organization.  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IncidentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    IncidentsApi apiInstance = new IncidentsApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    AckOrResolveRequest body = new AckOrResolveRequest(); // AckOrResolveRequest | Ack/Resolve payload
    try {
      AckOrResolveResponse result = apiInstance.apiPublicV1IncidentsAckPatch(xVOApiId, xVOApiKey, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentsApi#apiPublicV1IncidentsAckPatch");
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
| **body** | [**AckOrResolveRequest**](AckOrResolveRequest.md)| Ack/Resolve payload | |

### Return type

[**AckOrResolveResponse**](AckOrResolveResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The result of each acknowledge incident action. |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **404** | User not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiPublicV1IncidentsByUserAckPatch"></a>
# **apiPublicV1IncidentsByUserAckPatch**
> AckOrResolveResponse apiPublicV1IncidentsByUserAckPatch(xVOApiId, xVOApiKey, body)

Acknowledge all incidents for which a user was paged.

The incident(s) must be currently open.  The user supplied must be a valid VictorOps user and a member of your organization.  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IncidentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    IncidentsApi apiInstance = new IncidentsApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    AckOrResolveByUserRequest body = new AckOrResolveByUserRequest(); // AckOrResolveByUserRequest | Ack/Resolve payload
    try {
      AckOrResolveResponse result = apiInstance.apiPublicV1IncidentsByUserAckPatch(xVOApiId, xVOApiKey, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentsApi#apiPublicV1IncidentsByUserAckPatch");
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
| **body** | [**AckOrResolveByUserRequest**](AckOrResolveByUserRequest.md)| Ack/Resolve payload | |

### Return type

[**AckOrResolveResponse**](AckOrResolveResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The result of each acknowledge incident action. |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **404** | User not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiPublicV1IncidentsByUserResolvePatch"></a>
# **apiPublicV1IncidentsByUserResolvePatch**
> AckOrResolveResponse apiPublicV1IncidentsByUserResolvePatch(xVOApiId, xVOApiKey, body)

Resolve all incidents for which a user was paged.

The incident(s) must be currently open.  The user supplied must be a valid VictorOps user and a member of your organization.  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IncidentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    IncidentsApi apiInstance = new IncidentsApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    AckOrResolveByUserRequest body = new AckOrResolveByUserRequest(); // AckOrResolveByUserRequest | Ack/Resolve payload
    try {
      AckOrResolveResponse result = apiInstance.apiPublicV1IncidentsByUserResolvePatch(xVOApiId, xVOApiKey, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentsApi#apiPublicV1IncidentsByUserResolvePatch");
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
| **body** | [**AckOrResolveByUserRequest**](AckOrResolveByUserRequest.md)| Ack/Resolve payload | |

### Return type

[**AckOrResolveResponse**](AckOrResolveResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The result of each resolve incident action. |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **404** | User not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiPublicV1IncidentsGet"></a>
# **apiPublicV1IncidentsGet**
> ActiveIncidentList apiPublicV1IncidentsGet(xVOApiId, xVOApiKey)

Get current incident information

Get a list of the currently open, acknowledged and recently resolved incidents.  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IncidentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    IncidentsApi apiInstance = new IncidentsApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    try {
      ActiveIncidentList result = apiInstance.apiPublicV1IncidentsGet(xVOApiId, xVOApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentsApi#apiPublicV1IncidentsGet");
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

[**ActiveIncidentList**](ActiveIncidentList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The set of incidents.  |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **404** | Path not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiPublicV1IncidentsPost"></a>
# **apiPublicV1IncidentsPost**
> CreatedIncident apiPublicV1IncidentsPost(xVOApiId, xVOApiKey, body)

Create a new incident

Create a new incident.  This call replicates the function of our &lt;a href&#x3D;\&quot;https://help.victorops.com/knowledge-base/manual-incident-creation/\&quot;&gt;manual incident creation process&lt;/a&gt;. Monitoring tools and custom integrations should be configured using our &lt;a href&#x3D;\&quot;https://help.victorops.com/knowledge-base/victorops-restendpoint-integration/\&quot;&gt;REST Endpoint&lt;/a&gt;.  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IncidentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    IncidentsApi apiInstance = new IncidentsApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    CreateIncidentRequest body = new CreateIncidentRequest(); // CreateIncidentRequest | The incident details
    try {
      CreatedIncident result = apiInstance.apiPublicV1IncidentsPost(xVOApiId, xVOApiKey, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentsApi#apiPublicV1IncidentsPost");
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
| **body** | [**CreateIncidentRequest**](CreateIncidentRequest.md)| The incident details | |

### Return type

[**CreatedIncident**](CreatedIncident.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Information about the incident created  |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **404** | Path not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiPublicV1IncidentsReroutePost"></a>
# **apiPublicV1IncidentsReroutePost**
> RerouteStatusResponse apiPublicV1IncidentsReroutePost(xVOApiId, xVOApiKey, body)

Reroute one or more incidents to one or more new routable destinations.

Reroute one or more incidents to one or more users and/or escalation policies  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IncidentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    IncidentsApi apiInstance = new IncidentsApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    RerouteCollection body = new RerouteCollection(); // RerouteCollection | The reroute rules
    try {
      RerouteStatusResponse result = apiInstance.apiPublicV1IncidentsReroutePost(xVOApiId, xVOApiKey, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentsApi#apiPublicV1IncidentsReroutePost");
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
| **body** | [**RerouteCollection**](RerouteCollection.md)| The reroute rules | |

### Return type

[**RerouteStatusResponse**](RerouteStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The created reroute object |  -  |

<a id="apiPublicV1IncidentsResolvePatch"></a>
# **apiPublicV1IncidentsResolvePatch**
> AckOrResolveResponse apiPublicV1IncidentsResolvePatch(xVOApiId, xVOApiKey, body)

Resolve an incident or list of incidents

The incident(s) must be currently open.  The user supplied must be a valid VictorOps user and a member of your organization.  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IncidentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    IncidentsApi apiInstance = new IncidentsApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    AckOrResolveRequest body = new AckOrResolveRequest(); // AckOrResolveRequest | Ack/Resolve payload
    try {
      AckOrResolveResponse result = apiInstance.apiPublicV1IncidentsResolvePatch(xVOApiId, xVOApiKey, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentsApi#apiPublicV1IncidentsResolvePatch");
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
| **body** | [**AckOrResolveRequest**](AckOrResolveRequest.md)| Ack/Resolve payload | |

### Return type

[**AckOrResolveResponse**](AckOrResolveResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The result of each resolve incident action. |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **404** | User not found |  -  |
| **500** | Internal Server Error |  -  |

