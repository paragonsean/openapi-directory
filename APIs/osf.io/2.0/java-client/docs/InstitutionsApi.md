# InstitutionsApi

All URIs are relative to *https://api.test.osf.io/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**institutionsDetail**](InstitutionsApi.md#institutionsDetail) | **GET** /institutions/{institution_id}/ | Retrieve an institution |
| [**institutionsList**](InstitutionsApi.md#institutionsList) | **GET** /institutions/ | List all institutions |
| [**institutionsNodeList**](InstitutionsApi.md#institutionsNodeList) | **GET** /institutions/{institution_id}/nodes/ | List all affiliated nodes |
| [**institutionsRegistrationList**](InstitutionsApi.md#institutionsRegistrationList) | **GET** /institutions/{institution_id}/registrations/ | List all affiliated registrations |
| [**institutionsUsersList**](InstitutionsApi.md#institutionsUsersList) | **GET** /institutions/{institution_id}/users/ | List all affiliated users |


<a id="institutionsDetail"></a>
# **institutionsDetail**
> List&lt;Institution&gt; institutionsDetail(institutionId)

Retrieve an institution

Retrieves the details of an institution #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the requested institution, if the request was successful.  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstitutionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    InstitutionsApi apiInstance = new InstitutionsApi(defaultClient);
    String institutionId = "institutionId_example"; // String | The unique identifier of the institution you wish to retrieve.
    try {
      List<Institution> result = apiInstance.institutionsDetail(institutionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstitutionsApi#institutionsDetail");
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
| **institutionId** | **String**| The unique identifier of the institution you wish to retrieve. | |

### Return type

[**List&lt;Institution&gt;**](Institution.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="institutionsList"></a>
# **institutionsList**
> List&lt;Institution&gt; institutionsList()

List all institutions

 A paginated list of all verified institutions. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of 10 institutions. Each resource in the array is a separate institution object.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  This request should never return an error. #### Filtering You can optionally request that the response only include institutions that match your filters by utilizing the &#x60;filter&#x60; query parameter, e.g. https://api.osf.io/v2/institutions/?filter[id]&#x3D;cos.  Institutions may be filtered by their &#x60;id&#x60;, &#x60;name&#x60;, and &#x60;auth_url&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstitutionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    InstitutionsApi apiInstance = new InstitutionsApi(defaultClient);
    try {
      List<Institution> result = apiInstance.institutionsList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstitutionsApi#institutionsList");
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

[**List&lt;Institution&gt;**](Institution.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="institutionsNodeList"></a>
# **institutionsNodeList**
> List&lt;Node&gt; institutionsNodeList(institutionId)

List all affiliated nodes

A paginated list of all nodes affiliated with an institution. #### Versioning As of version &#x60;2.2&#x60;, affiliated components (in addition to affiliated top-level projects) are returned from this endpoint. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of 10 nodes. Each resource in the array is a separate nodes object.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed. #### Filtering You can optionally request that the response only include nodes that match your filters by utilizing the &#x60;filter&#x60; query parameter, e.g. https://api.osf.io/v2/institutions/cos/nodes?filter[title]&#x3D;science.  Nodes may be filtered by their &#x60;id&#x60;, &#x60;title&#x60;, &#x60;description&#x60;, &#x60;public&#x60;, &#x60;tags&#x60;, &#x60;category&#x60;, &#x60;date_created&#x60;, &#x60;date_modified&#x60;, &#x60;root&#x60;, &#x60;parent&#x60;, &#x60;contributors&#x60;, and &#x60;preprint&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstitutionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    InstitutionsApi apiInstance = new InstitutionsApi(defaultClient);
    String institutionId = "institutionId_example"; // String | The unique identifier of the institution you wish to retrieve.
    try {
      List<Node> result = apiInstance.institutionsNodeList(institutionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstitutionsApi#institutionsNodeList");
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
| **institutionId** | **String**| The unique identifier of the institution you wish to retrieve. | |

### Return type

[**List&lt;Node&gt;**](Node.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="institutionsRegistrationList"></a>
# **institutionsRegistrationList**
> institutionsRegistrationList(institutionId)

List all affiliated registrations

A paginated list of all registrations affiliated with an institution. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of 10 registrations. Each resource in the array is a separate users object.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed. #### Filtering You can optionally request that the response only include registrations that match your filters by utilizing the &#x60;filter&#x60; query parameter, e.g. https://api.osf.io/v2/institutions/cos/registrations?filter[title]&#x3D;science.  Registrations may be filtered by their  &#x60;id&#x60;, &#x60;title&#x60;, &#x60;description&#x60;, &#x60;public&#x60;, &#x60;tags&#x60;, &#x60;category&#x60;, &#x60;date_created&#x60;, &#x60;date_modified&#x60;, &#x60;root&#x60;, &#x60;parent&#x60;, &#x60;contributors&#x60;, and &#x60;preprint&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstitutionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    InstitutionsApi apiInstance = new InstitutionsApi(defaultClient);
    String institutionId = "institutionId_example"; // String | The unique identifier of the institution you wish to retrieve.
    try {
      apiInstance.institutionsRegistrationList(institutionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstitutionsApi#institutionsRegistrationList");
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
| **institutionId** | **String**| The unique identifier of the institution you wish to retrieve. | |

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
| **200** | OK |  -  |

<a id="institutionsUsersList"></a>
# **institutionsUsersList**
> List&lt;User&gt; institutionsUsersList(institutionId)

List all affiliated users

A paginated list of all users affiliated with an institution. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of 10 users. Each resource in the array is a separate users object.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed. #### Filtering You can optionally request that the response only include users that match your filters by utilizing the &#x60;filter&#x60; query parameter, e.g. https://api.osf.io/v2/institutions/cos/users?filter[family_name]&#x3D;Nosek.  Users may be filtered by their &#x60;id&#x60;, &#x60;full_name&#x60;, &#x60;given_name&#x60;, &#x60;middle_names&#x60;, and &#x60;family_name&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstitutionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    InstitutionsApi apiInstance = new InstitutionsApi(defaultClient);
    String institutionId = "institutionId_example"; // String | The unique identifier of the institution you wish to retrieve.
    try {
      List<User> result = apiInstance.institutionsUsersList(institutionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstitutionsApi#institutionsUsersList");
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
| **institutionId** | **String**| The unique identifier of the institution you wish to retrieve. | |

### Return type

[**List&lt;User&gt;**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

