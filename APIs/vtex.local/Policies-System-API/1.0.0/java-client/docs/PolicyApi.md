# PolicyApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiPolicyEnginePoliciesIdPut**](PolicyApi.md#apiPolicyEnginePoliciesIdPut) | **PUT** /api/policy-engine/policies/{id} | Update Policy |
| [**policyCreateOrUpdate**](PolicyApi.md#policyCreateOrUpdate) | **POST** /api/policy-engine/policies/{id} | Create Policy |
| [**policyDelete**](PolicyApi.md#policyDelete) | **DELETE** /api/policy-engine/policies/{id} | Delete Policy by ID |
| [**policyEvaluate**](PolicyApi.md#policyEvaluate) | **POST** /api/policy-engine/evaluate | Evaluate Policies |
| [**policyGet**](PolicyApi.md#policyGet) | **GET** /api/policy-engine/policies/{id} | Get Policy by ID |
| [**policyList**](PolicyApi.md#policyList) | **GET** /api/policy-engine/policies | Get Policy List |


<a id="apiPolicyEnginePoliciesIdPut"></a>
# **apiPolicyEnginePoliciesIdPut**
> List&lt;PolicyGetResponse&gt; apiPolicyEnginePoliciesIdPut(contentType, accept, id, policySaveRequest)

Update Policy

Updates an existing policy at your account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");

    PolicyApi apiInstance = new PolicyApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
    String id = "pa_test_001"; // String | Policy ID
    PolicySaveRequest policySaveRequest = new PolicySaveRequest(); // PolicySaveRequest | 
    try {
      List<PolicyGetResponse> result = apiInstance.apiPolicyEnginePoliciesIdPut(contentType, accept, id, policySaveRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicyApi#apiPolicyEnginePoliciesIdPut");
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
| **contentType** | **String**| Describes the type of the content being sent | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand  | [default to application/json] |
| **id** | **String**| Policy ID | [default to pa_test_001] |
| **policySaveRequest** | [**PolicySaveRequest**](PolicySaveRequest.md)|  | |

### Return type

[**List&lt;PolicyGetResponse&gt;**](PolicyGetResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="policyCreateOrUpdate"></a>
# **policyCreateOrUpdate**
> List&lt;PolicyGetResponse&gt; policyCreateOrUpdate(contentType, accept, id, policySaveRequest)

Create Policy

Creates a new policy from scratch.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");

    PolicyApi apiInstance = new PolicyApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
    String id = "pa_test_001"; // String | Policy ID
    PolicySaveRequest policySaveRequest = new PolicySaveRequest(); // PolicySaveRequest | 
    try {
      List<PolicyGetResponse> result = apiInstance.policyCreateOrUpdate(contentType, accept, id, policySaveRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicyApi#policyCreateOrUpdate");
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
| **contentType** | **String**| Describes the type of the content being sent | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand  | [default to application/json] |
| **id** | **String**| Policy ID | [default to pa_test_001] |
| **policySaveRequest** | [**PolicySaveRequest**](PolicySaveRequest.md)|  | [optional] |

### Return type

[**List&lt;PolicyGetResponse&gt;**](PolicyGetResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="policyDelete"></a>
# **policyDelete**
> policyDelete(contentType, accept, id)

Delete Policy by ID

Deletes a specific policy of the account by its ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");

    PolicyApi apiInstance = new PolicyApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
    String id = "pa_test_001"; // String | Policy ID
    try {
      apiInstance.policyDelete(contentType, accept, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicyApi#policyDelete");
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
| **contentType** | **String**| Describes the type of the content being sent | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand  | [default to application/json] |
| **id** | **String**| Policy ID | [default to pa_test_001] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 OK |  -  |

<a id="policyEvaluate"></a>
# **policyEvaluate**
> List&lt;PolicyActionGetResponse&gt; policyEvaluate(contentType, accept, evaluatePolicyRequest)

Evaluate Policies

This endpoint consults all policies and checks the ones that satisfy the request body’s conditions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");

    PolicyApi apiInstance = new PolicyApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
    EvaluatePolicyRequest evaluatePolicyRequest = new EvaluatePolicyRequest(); // EvaluatePolicyRequest | 
    try {
      List<PolicyActionGetResponse> result = apiInstance.policyEvaluate(contentType, accept, evaluatePolicyRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicyApi#policyEvaluate");
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
| **contentType** | **String**| Describes the type of the content being sent | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand  | [default to application/json] |
| **evaluatePolicyRequest** | [**EvaluatePolicyRequest**](EvaluatePolicyRequest.md)|  | |

### Return type

[**List&lt;PolicyActionGetResponse&gt;**](PolicyActionGetResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="policyGet"></a>
# **policyGet**
> List&lt;PolicyGetResponse&gt; policyGet(contentType, accept, id)

Get Policy by ID

Retrieves general information of a policy by its ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");

    PolicyApi apiInstance = new PolicyApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
    String id = "pa_test_001"; // String | Policy ID
    try {
      List<PolicyGetResponse> result = apiInstance.policyGet(contentType, accept, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicyApi#policyGet");
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
| **contentType** | **String**| Describes the type of the content being sent | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand  | [default to application/json] |
| **id** | **String**| Policy ID | [default to pa_test_001] |

### Return type

[**List&lt;PolicyGetResponse&gt;**](PolicyGetResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="policyList"></a>
# **policyList**
> List&lt;PolicyGetResponse&gt; policyList(contentType, accept)

Get Policy List

Retrieves a list of all policies in the account and general information of each policy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");

    PolicyApi apiInstance = new PolicyApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
    try {
      List<PolicyGetResponse> result = apiInstance.policyList(contentType, accept);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicyApi#policyList");
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
| **contentType** | **String**| Describes the type of the content being sent | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand  | [default to application/json] |

### Return type

[**List&lt;PolicyGetResponse&gt;**](PolicyGetResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

