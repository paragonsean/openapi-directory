# PolicyApiApi

All URIs are relative to *http://openpolicy.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deletePolicyModule**](PolicyApiApi.md#deletePolicyModule) | **DELETE** /v1/policies/{id} | Delete a policy module |
| [**getPolicies**](PolicyApiApi.md#getPolicies) | **GET** /v1/policies | List policies |
| [**getPolicyModule**](PolicyApiApi.md#getPolicyModule) | **GET** /v1/policies/{id} | Get a policy module |
| [**putPolicyModule**](PolicyApiApi.md#putPolicyModule) | **PUT** /v1/policies/{id} | Create or update a policy module |


<a id="deletePolicyModule"></a>
# **deletePolicyModule**
> GetDocumentWithWebHook200Response deletePolicyModule(id, pretty)

Delete a policy module

This API endpoint removes an existing policy module from the server

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicyApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://openpolicy.local");

    PolicyApiApi apiInstance = new PolicyApiApi(defaultClient);
    String id = "example1"; // String | The name of a policy module
    Boolean pretty = true; // Boolean | If true, response will be in a human-readable format.
    try {
      GetDocumentWithWebHook200Response result = apiInstance.deletePolicyModule(id, pretty);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicyApiApi#deletePolicyModule");
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
| **id** | **String**| The name of a policy module | |
| **pretty** | **Boolean**| If true, response will be in a human-readable format. | [optional] |

### Return type

[**GetDocumentWithWebHook200Response**](GetDocumentWithWebHook200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad request |  -  |
| **404** | Not found (for example, a requested policy module or document does not exist) |  -  |
| **500** | Server error |  -  |

<a id="getPolicies"></a>
# **getPolicies**
> Model200Result getPolicies(pretty)

List policies

This API endpoint responds with a list of all policy modules on the server (result response)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicyApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://openpolicy.local");

    PolicyApiApi apiInstance = new PolicyApiApi(defaultClient);
    Boolean pretty = true; // Boolean | If true, response will be in a human-readable format.
    try {
      Model200Result result = apiInstance.getPolicies(pretty);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicyApiApi#getPolicies");
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
| **pretty** | **Boolean**| If true, response will be in a human-readable format. | [optional] |

### Return type

[**Model200Result**](Model200Result.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **500** | Server error |  -  |

<a id="getPolicyModule"></a>
# **getPolicyModule**
> Model200Result getPolicyModule(id, pretty)

Get a policy module

This API endpoint returns the details of the specified policy module (&#x60;{id}&#x60;)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicyApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://openpolicy.local");

    PolicyApiApi apiInstance = new PolicyApiApi(defaultClient);
    String id = "example1"; // String | The name of a policy module
    Boolean pretty = true; // Boolean | If true, response will be in a human-readable format.
    try {
      Model200Result result = apiInstance.getPolicyModule(id, pretty);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicyApiApi#getPolicyModule");
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
| **id** | **String**| The name of a policy module | |
| **pretty** | **Boolean**| If true, response will be in a human-readable format. | [optional] |

### Return type

[**Model200Result**](Model200Result.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | Not found (for example, a requested policy module or document does not exist) |  -  |
| **500** | Server error |  -  |

<a id="putPolicyModule"></a>
# **putPolicyModule**
> Model200Result putPolicyModule(id, body, pretty, metrics)

Create or update a policy module

- If the policy module does not exist, it is created. - If the policy module already exists, it is replaced.  If the policy module isn&#39;t correctly defined, a *bad request* (400) response is returned.  ### Example policy module &#x60;&#x60;&#x60;yaml package opa.examples  import data.servers import data.networks import data.ports  public_servers[server] {   some k, m    server :&#x3D; servers[_]    server.ports[_] &#x3D;&#x3D; ports[k].id    ports[k].networks[_] &#x3D;&#x3D; networks[m].id    networks[m].public &#x3D;&#x3D; true } &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicyApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://openpolicy.local");

    PolicyApiApi apiInstance = new PolicyApiApi(defaultClient);
    String id = "example1"; // String | The name of a policy module
    String body = "body_example"; // String | 
    Boolean pretty = true; // Boolean | If true, response will be in a human-readable format.
    Boolean metrics = false; // Boolean | If true, compiler performance metrics will be returned in the response.
    try {
      Model200Result result = apiInstance.putPolicyModule(id, body, pretty, metrics);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicyApiApi#putPolicyModule");
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
| **id** | **String**| The name of a policy module | |
| **body** | **String**|  | |
| **pretty** | **Boolean**| If true, response will be in a human-readable format. | [optional] |
| **metrics** | **Boolean**| If true, compiler performance metrics will be returned in the response. | [optional] |

### Return type

[**Model200Result**](Model200Result.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad request |  -  |
| **500** | Server error |  -  |

