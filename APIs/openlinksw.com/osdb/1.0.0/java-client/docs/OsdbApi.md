# OsdbApi

All URIs are relative to *https://osdb.openlinksw.com/osdb*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**actionHelp**](OsdbApi.md#actionHelp) | **GET** /api/v1/actions/{serviceId}/{actionId}/help | Action help |
| [**describeAction**](OsdbApi.md#describeAction) | **GET** /api/v1/actions/{serviceId}/{actionId} | Describe action |
| [**describeService**](OsdbApi.md#describeService) | **GET** /api/v1/services/{serviceId} | Describe service |
| [**executeAction**](OsdbApi.md#executeAction) | **POST** /api/v1/actions/{serviceId}/{actionId}/exec | Execute action |
| [**listActions**](OsdbApi.md#listActions) | **GET** /api/v1/actions/{serviceId} | List actions |
| [**listServices**](OsdbApi.md#listServices) | **GET** /api/v1/services | List services |
| [**loadService**](OsdbApi.md#loadService) | **POST** /api/v1/services | Load service |
| [**login**](OsdbApi.md#login) | **GET** /api/v1/login | Login |
| [**logout**](OsdbApi.md#logout) | **GET** /api/v1/logout | Logout |
| [**unloadService**](OsdbApi.md#unloadService) | **DELETE** /api/v1/services/{serviceId} | Unload service |


<a id="actionHelp"></a>
# **actionHelp**
> ActionHelpResponse actionHelp(serviceId, actionId)

Action help

Returns the help text for a given service action

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OsdbApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://osdb.openlinksw.com/osdb");

    OsdbApi apiInstance = new OsdbApi(defaultClient);
    String serviceId = "serviceId_example"; // String | Service ID of the service supporting the action.
    String actionId = "actionId_example"; // String | Action ID of the action for which help text is being requested.
    try {
      ActionHelpResponse result = apiInstance.actionHelp(serviceId, actionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OsdbApi#actionHelp");
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
| **serviceId** | **String**| Service ID of the service supporting the action. | |
| **actionId** | **String**| Action ID of the action for which help text is being requested. | |

### Return type

[**ActionHelpResponse**](ActionHelpResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Action help text |  -  |
| **0** | Error response |  -  |

<a id="describeAction"></a>
# **describeAction**
> DescribeActionResponse describeAction(serviceId, actionId)

Describe action

Returns a description of a given service action.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OsdbApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://osdb.openlinksw.com/osdb");

    OsdbApi apiInstance = new OsdbApi(defaultClient);
    String serviceId = "serviceId_example"; // String | Service ID of the service supporting the action.
    String actionId = "actionId_example"; // String | Action ID of the action to describe.
    try {
      DescribeActionResponse result = apiInstance.describeAction(serviceId, actionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OsdbApi#describeAction");
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
| **serviceId** | **String**| Service ID of the service supporting the action. | |
| **actionId** | **String**| Action ID of the action to describe. | |

### Return type

[**DescribeActionResponse**](DescribeActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A single action description |  -  |
| **0** | Error response |  -  |

<a id="describeService"></a>
# **describeService**
> DescribeServiceResponse describeService(serviceId)

Describe service

Returns a description of a given service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OsdbApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://osdb.openlinksw.com/osdb");

    OsdbApi apiInstance = new OsdbApi(defaultClient);
    String serviceId = "serviceId_example"; // String | Service ID of the service to describe.
    try {
      DescribeServiceResponse result = apiInstance.describeService(serviceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OsdbApi#describeService");
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
| **serviceId** | **String**| Service ID of the service to describe. | |

### Return type

[**DescribeServiceResponse**](DescribeServiceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A single service description |  -  |
| **0** | Error response |  -  |

<a id="executeAction"></a>
# **executeAction**
> executeAction(serviceId, actionId, execBody)

Execute action

Executes a registered service action and returns any output from the action. The data returned in the POST response body may be:  * the raw action output,  * a URL encapsulating the action request which executes the action when dereferenced  (only for actions using GET),  * RDF generated from the action output, * a URL to an RDF viewer&#39;s display of the generated RDF.  Any parameters required by the action are supplied as a JSON object in the POST body. The parameter types supported are: \&quot;query\&quot;, \&quot;header\&quot;, \&quot;uri\&quot;, \&quot;path\&quot; and \&quot;body\&quot;.  The parameter type determines where a supplied parameter value is inserted into the HTTP request constructed by OSDB to invoke the target service action. In addition to native parameters required by the service action, &#39;Execute action&#39; accepts some OSDB-specific parameters.&lt;br/&gt;&lt;br/&gt;  **Examples** * &#x60;&#x60;&#x60;curl -ik -X POST -d &#39;{ \&quot;latitude\&quot;:\&quot;37.7759792\&quot;, \&quot;longitude\&quot;:\&quot;-122.41823\&quot; }&#39; -H &#39;Content-Type: application/json&#39; https://osdb.openlinksw.com/osdb/api/v1/actions/uber/products/exec&#x60;&#x60;&#x60;   * &#x60;&#x60;&#x60;curl -ikL -X POST -d &#39;{ \&quot;latitude\&quot;:\&quot;37.7759792\&quot;, \&quot;longitude\&quot;:\&quot;-122.41823\&quot;, \&quot;osdb:output_type\&quot;:\&quot;generate_rdf\&quot;, \&quot;osdb:response_format\&quot;:\&quot;application/rdf+xml\&quot; }&#39; -H &#39;Content-Type: application/json&#39; https://osdb.openlinksw.com/osdb/api/v1/actions/uber/products/exec&#x60;&#x60;&#x60;  * &#x60;&#x60;&#x60;curl -ikL -X POST -d &#39;{ \&quot;latitude\&quot;:\&quot;37.7759792\&quot;, \&quot;longitude\&quot;:\&quot;-122.41823\&quot;, \&quot;osdb:output_type\&quot;:\&quot;display_rdf\&quot; }&#39; -H &#39;Content-Type: application/json&#39; https://osdb.openlinksw.com/osdb/api/v1/actions/uber/products/exec&#x60;&#x60;&#x60;  * &#x60;&#x60;&#x60;curl -ik -X POST -d &#39;{ \&quot;q\&quot;:\&quot;skiing\&quot;, \&quot;osdb:response_format\&quot;: \&quot;application/rdf+xml\&quot; }&#39; -H &#39;Content-Type: application/json&#39; https://osdb.openlinksw.com/osdb/api/v1/actions/facet/search/exec&#x60;&#x60;&#x60;  * &#x60;&#x60;&#x60;curl -ik -X POST -d &#39;{ \&quot;q\&quot;:\&quot;skiing\&quot;, \&quot;osdb:output_type\&quot;: \&quot;url_only\&quot; }&#39; -H &#39;Content-Type: application/json&#39; https://osdb.openlinksw.com/osdb/api/v1/actions/facet/search/exec&#x60;&#x60;&#x60;  * &#x60;&#x60;&#x60;curl -ik -X POST -d &#39;{ \&quot;Content-Location\&quot;: \&quot;http://demo.openlinksw.co.uk/pubs\&quot;, \&quot;osdb:body_data_src_url\&quot;: \&quot;http://ods-qa.openlinksw.com/DAV/home/osdb/pubs.csv\&quot;, \&quot;extractor\&quot;: \&quot;csv\&quot;, \&quot;osdb:response_format\&quot;: \&quot;application/rdf+xml\&quot;, \&quot;osdb:body_data_encoding\&quot;: \&quot;text/csv\&quot; }&#39; -H &#39;Content-Type: application/json&#39; https://osdb.openlinksw.com/osdb/api/v1/actions/csv_transformer/transform/exec&#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OsdbApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://osdb.openlinksw.com/osdb");

    OsdbApi apiInstance = new OsdbApi(defaultClient);
    String serviceId = "serviceId_example"; // String | Service ID of the service supporting the action.
    String actionId = "actionId_example"; // String | Action ID of the action to execute.
    ExecBody execBody = new ExecBody(); // ExecBody | Any parameters required by the action are supplied as a JSON object in the request body. The properties of this object depend on the service action being invoked.
    try {
      apiInstance.executeAction(serviceId, actionId, execBody);
    } catch (ApiException e) {
      System.err.println("Exception when calling OsdbApi#executeAction");
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
| **serviceId** | **String**| Service ID of the service supporting the action. | |
| **actionId** | **String**| Action ID of the action to execute. | |
| **execBody** | [**ExecBody**](ExecBody.md)| Any parameters required by the action are supplied as a JSON object in the request body. The properties of this object depend on the service action being invoked. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | Response from an OSDB action invocation. |  -  |
| **0** | Error response |  -  |

<a id="listActions"></a>
# **listActions**
> ListActionsResponse listActions(serviceId)

List actions

Returns an array of action descriptions for the actions supported by the given service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OsdbApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://osdb.openlinksw.com/osdb");

    OsdbApi apiInstance = new OsdbApi(defaultClient);
    String serviceId = "serviceId_example"; // String | Service ID of the service for which actions are to be listed
    try {
      ListActionsResponse result = apiInstance.listActions(serviceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OsdbApi#listActions");
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
| **serviceId** | **String**| Service ID of the service for which actions are to be listed | |

### Return type

[**ListActionsResponse**](ListActionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of action descriptions for the actions supported by the given service. |  -  |
| **0** | Error response |  -  |

<a id="listServices"></a>
# **listServices**
> ListServicesResponse listServices()

List services

Returns descriptions of all services registered with the OSDB server.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OsdbApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://osdb.openlinksw.com/osdb");

    OsdbApi apiInstance = new OsdbApi(defaultClient);
    try {
      ListServicesResponse result = apiInstance.listServices();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OsdbApi#listServices");
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

[**ListServicesResponse**](ListServicesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of service descriptions for all services registered with the OSDB server |  -  |
| **0** | Error response |  -  |

<a id="loadService"></a>
# **loadService**
> LoadService200Response loadService(loadServiceRequest)

Load service

Loads a service description into the OSDB Service Registry

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OsdbApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://osdb.openlinksw.com/osdb");

    OsdbApi apiInstance = new OsdbApi(defaultClient);
    LoadServiceRequest loadServiceRequest = new LoadServiceRequest(); // LoadServiceRequest | Service to register with OSDB
    try {
      LoadService200Response result = apiInstance.loadService(loadServiceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OsdbApi#loadService");
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
| **loadServiceRequest** | [**LoadServiceRequest**](LoadServiceRequest.md)| Service to register with OSDB | [optional] |

### Return type

[**LoadService200Response**](LoadService200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | loadService response |  -  |
| **0** | Error response |  -  |

<a id="login"></a>
# **login**
> LoginResponse login()

Login

Logs a user into the OSDB server, authenticating them by their WebID and returning an OSDB session ID in cookie osdb.sid

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OsdbApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://osdb.openlinksw.com/osdb");

    OsdbApi apiInstance = new OsdbApi(defaultClient);
    try {
      LoginResponse result = apiInstance.login();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OsdbApi#login");
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

[**LoginResponse**](LoginResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Confirmation of a successful OSDB login. |  -  |
| **0** | Error response |  -  |

<a id="logout"></a>
# **logout**
> LogoutResponse logout()

Logout

Logs a user out of the OSDB server, ending their OSDB session

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OsdbApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://osdb.openlinksw.com/osdb");

    OsdbApi apiInstance = new OsdbApi(defaultClient);
    try {
      LogoutResponse result = apiInstance.logout();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OsdbApi#logout");
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

[**LogoutResponse**](LogoutResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Confirmation of a successful OSDB logout. |  -  |
| **0** | Error response |  -  |

<a id="unloadService"></a>
# **unloadService**
> LoadService200Response unloadService(serviceId)

Unload service

Removes a service description from the OSDB Service Registry

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OsdbApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://osdb.openlinksw.com/osdb");

    OsdbApi apiInstance = new OsdbApi(defaultClient);
    String serviceId = "serviceId_example"; // String | Service ID of the service to be unloaded
    try {
      LoadService200Response result = apiInstance.unloadService(serviceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OsdbApi#unloadService");
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
| **serviceId** | **String**| Service ID of the service to be unloaded | |

### Return type

[**LoadService200Response**](LoadService200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | unloadService response |  -  |
| **0** | Error response |  -  |

