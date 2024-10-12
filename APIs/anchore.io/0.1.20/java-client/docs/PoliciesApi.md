# PoliciesApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addPolicy**](PoliciesApi.md#addPolicy) | **POST** /policies | Add a new policy |
| [**deletePolicy**](PoliciesApi.md#deletePolicy) | **DELETE** /policies/{policyId} | Delete policy |
| [**getPolicy**](PoliciesApi.md#getPolicy) | **GET** /policies/{policyId} | Get specific policy |
| [**listPolicies**](PoliciesApi.md#listPolicies) | **GET** /policies | List policies |
| [**updatePolicy**](PoliciesApi.md#updatePolicy) | **PUT** /policies/{policyId} | Update policy |


<a id="addPolicy"></a>
# **addPolicy**
> PolicyBundleRecord addPolicy(policyBundle, xAnchoreAccount)

Add a new policy

Adds a new policy bundle to the system

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    PoliciesApi apiInstance = new PoliciesApi(defaultClient);
    PolicyBundle policyBundle = new PolicyBundle(); // PolicyBundle | 
    String xAnchoreAccount = "xAnchoreAccount_example"; // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    try {
      PolicyBundleRecord result = apiInstance.addPolicy(policyBundle, xAnchoreAccount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PoliciesApi#addPolicy");
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
| **policyBundle** | [**PolicyBundle**](PolicyBundle.md)|  | |
| **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] |

### Return type

[**PolicyBundleRecord**](PolicyBundleRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Saved bundle |  -  |
| **500** | Internal Error |  -  |

<a id="deletePolicy"></a>
# **deletePolicy**
> deletePolicy(policyId, xAnchoreAccount)

Delete policy

Delete the specified policy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    PoliciesApi apiInstance = new PoliciesApi(defaultClient);
    String policyId = "policyId_example"; // String | 
    String xAnchoreAccount = "xAnchoreAccount_example"; // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    try {
      apiInstance.deletePolicy(policyId, xAnchoreAccount);
    } catch (ApiException e) {
      System.err.println("Exception when calling PoliciesApi#deletePolicy");
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
| **policyId** | **String**|  | |
| **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] |

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
| **200** | Delete success |  -  |
| **404** | Policy not found to delete |  -  |
| **500** | Internal Error |  -  |

<a id="getPolicy"></a>
# **getPolicy**
> List&lt;PolicyBundleRecord&gt; getPolicy(policyId, detail, xAnchoreAccount)

Get specific policy

Get the policy bundle content

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    PoliciesApi apiInstance = new PoliciesApi(defaultClient);
    String policyId = "policyId_example"; // String | 
    Boolean detail = true; // Boolean | Include policy bundle detail in the form of the full bundle content for each entry
    String xAnchoreAccount = "xAnchoreAccount_example"; // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    try {
      List<PolicyBundleRecord> result = apiInstance.getPolicy(policyId, detail, xAnchoreAccount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PoliciesApi#getPolicy");
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
| **policyId** | **String**|  | |
| **detail** | **Boolean**| Include policy bundle detail in the form of the full bundle content for each entry | [optional] |
| **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] |

### Return type

[**List&lt;PolicyBundleRecord&gt;**](PolicyBundleRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list with a single fetched policy bundle record |  -  |
| **500** | Internal Error |  -  |

<a id="listPolicies"></a>
# **listPolicies**
> List&lt;PolicyBundleRecord&gt; listPolicies(detail, xAnchoreAccount)

List policies

List all saved policy bundles

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    PoliciesApi apiInstance = new PoliciesApi(defaultClient);
    Boolean detail = true; // Boolean | Include policy bundle detail in the form of the full bundle content for each entry
    String xAnchoreAccount = "xAnchoreAccount_example"; // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    try {
      List<PolicyBundleRecord> result = apiInstance.listPolicies(detail, xAnchoreAccount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PoliciesApi#listPolicies");
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
| **detail** | **Boolean**| Include policy bundle detail in the form of the full bundle content for each entry | [optional] |
| **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] |

### Return type

[**List&lt;PolicyBundleRecord&gt;**](PolicyBundleRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Policy listing |  -  |

<a id="updatePolicy"></a>
# **updatePolicy**
> List&lt;PolicyBundleRecord&gt; updatePolicy(policyId, policyBundleRecord, active, xAnchoreAccount)

Update policy

Update/replace and existing policy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    PoliciesApi apiInstance = new PoliciesApi(defaultClient);
    String policyId = "policyId_example"; // String | 
    PolicyBundleRecord policyBundleRecord = new PolicyBundleRecord(); // PolicyBundleRecord | 
    Boolean active = true; // Boolean | Mark policy as active
    String xAnchoreAccount = "xAnchoreAccount_example"; // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    try {
      List<PolicyBundleRecord> result = apiInstance.updatePolicy(policyId, policyBundleRecord, active, xAnchoreAccount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PoliciesApi#updatePolicy");
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
| **policyId** | **String**|  | |
| **policyBundleRecord** | [**PolicyBundleRecord**](PolicyBundleRecord.md)|  | |
| **active** | **Boolean**| Mark policy as active | [optional] |
| **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] |

### Return type

[**List&lt;PolicyBundleRecord&gt;**](PolicyBundleRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list with a single updated policy bundle record |  -  |
| **500** | Internal Error |  -  |

