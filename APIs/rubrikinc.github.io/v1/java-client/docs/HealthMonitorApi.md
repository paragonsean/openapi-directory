# HealthMonitorApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getPolicies**](HealthMonitorApi.md#getPolicies) | **GET** /health_monitor/policies | Get details of health monitor policies |
| [**getPolicyStatus**](HealthMonitorApi.md#getPolicyStatus) | **GET** /health_monitor/policy_status | Get the status of health monitor policy enforcement |
| [**runPolicies**](HealthMonitorApi.md#runPolicies) | **POST** /health_monitor/run_policy | Enforce health monitor policies |


<a id="getPolicies"></a>
# **getPolicies**
> List&lt;HealthMonitorPolicy&gt; getPolicies(policyIds)

Get details of health monitor policies

Retrieves the details of all the health monitor policies when policy IDs are not specified in the query parameter. If the request includes a list of policy IDs in the query parameter, the response will include the details of the specified policies.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HealthMonitorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    HealthMonitorApi apiInstance = new HealthMonitorApi(defaultClient);
    List<String> policyIds = Arrays.asList(); // List<String> | Optional list of policy IDs.
    try {
      List<HealthMonitorPolicy> result = apiInstance.getPolicies(policyIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HealthMonitorApi#getPolicies");
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
| **policyIds** | [**List&lt;String&gt;**](String.md)| Optional list of policy IDs. | [optional] |

### Return type

[**List&lt;HealthMonitorPolicy&gt;**](HealthMonitorPolicy.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of health monitor policies. |  -  |

<a id="getPolicyStatus"></a>
# **getPolicyStatus**
> List&lt;NodePolicyCheckResult&gt; getPolicyStatus(policyIds, nodeIds, hasDetailedStatus)

Get the status of health monitor policy enforcement

Retrieves the status of the policy enforcement for a list of nodes if specified. If nodes are not specified, the response includes the policy enforcement status for all the nodes on the Rubrik cluster.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HealthMonitorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    HealthMonitorApi apiInstance = new HealthMonitorApi(defaultClient);
    List<String> policyIds = Arrays.asList(); // List<String> | Optional list of policy IDs. If not provided, the response includes the status of all the policies.
    List<String> nodeIds = Arrays.asList(); // List<String> | Optional list of Node IDs. If not provided, the response includes the status of all the nodes.
    Boolean hasDetailedStatus = true; // Boolean | Indicates if the policy enforcement status should include expanded result for each policy.
    try {
      List<NodePolicyCheckResult> result = apiInstance.getPolicyStatus(policyIds, nodeIds, hasDetailedStatus);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HealthMonitorApi#getPolicyStatus");
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
| **policyIds** | [**List&lt;String&gt;**](String.md)| Optional list of policy IDs. If not provided, the response includes the status of all the policies. | [optional] |
| **nodeIds** | [**List&lt;String&gt;**](String.md)| Optional list of Node IDs. If not provided, the response includes the status of all the nodes. | [optional] |
| **hasDetailedStatus** | **Boolean**| Indicates if the policy enforcement status should include expanded result for each policy. | [optional] |

### Return type

[**List&lt;NodePolicyCheckResult&gt;**](NodePolicyCheckResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Enforcement status of policies. |  -  |

<a id="runPolicies"></a>
# **runPolicies**
> List&lt;NodePolicyCheckResult&gt; runPolicies(runPolicyArg)

Enforce health monitor policies

Triggers on-demand enforcement of the set of policies specified in the request body. If a list of nodes is provided, policies are run against these nodes, otherwise the policies are run on all active nodes of the Rubrik cluster.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HealthMonitorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    HealthMonitorApi apiInstance = new HealthMonitorApi(defaultClient);
    RunPolicyArg runPolicyArg = new RunPolicyArg(); // RunPolicyArg | The request object.
    try {
      List<NodePolicyCheckResult> result = apiInstance.runPolicies(runPolicyArg);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HealthMonitorApi#runPolicies");
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
| **runPolicyArg** | [**RunPolicyArg**](RunPolicyArg.md)| The request object. | |

### Return type

[**List&lt;NodePolicyCheckResult&gt;**](NodePolicyCheckResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Policy enforcement result. |  -  |

