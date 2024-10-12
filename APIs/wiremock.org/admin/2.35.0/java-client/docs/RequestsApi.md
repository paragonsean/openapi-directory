# RequestsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**adminRequestsCountPost**](RequestsApi.md#adminRequestsCountPost) | **POST** /__admin/requests/count | Count requests by criteria |
| [**adminRequestsDelete**](RequestsApi.md#adminRequestsDelete) | **DELETE** /__admin/requests | Delete all requests in journal |
| [**adminRequestsFindPost**](RequestsApi.md#adminRequestsFindPost) | **POST** /__admin/requests/find | Find requests by criteria |
| [**adminRequestsGet**](RequestsApi.md#adminRequestsGet) | **GET** /__admin/requests | Get all requests in journal |
| [**adminRequestsRemoveByMetadataPost**](RequestsApi.md#adminRequestsRemoveByMetadataPost) | **POST** /__admin/requests/remove-by-metadata | Delete requests mappings matching metadata |
| [**adminRequestsRemovePost**](RequestsApi.md#adminRequestsRemovePost) | **POST** /__admin/requests/remove | Remove requests by criteria |
| [**adminRequestsRequestIdDelete**](RequestsApi.md#adminRequestsRequestIdDelete) | **DELETE** /__admin/requests/{requestId} | Delete request by ID |
| [**adminRequestsRequestIdGet**](RequestsApi.md#adminRequestsRequestIdGet) | **GET** /__admin/requests/{requestId} | Get request by ID |
| [**adminRequestsResetPost**](RequestsApi.md#adminRequestsResetPost) | **POST** /__admin/requests/reset | Empty the request journal |
| [**adminRequestsUnmatchedGet**](RequestsApi.md#adminRequestsUnmatchedGet) | **GET** /__admin/requests/unmatched | Find unmatched requests |


<a id="adminRequestsCountPost"></a>
# **adminRequestsCountPost**
> AdminRequestsCountPost200Response adminRequestsCountPost(adminMappingsGet200ResponseMappingsInnerRequest)

Count requests by criteria

Count requests logged in the journal matching the specified criteria

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    RequestsApi apiInstance = new RequestsApi(defaultClient);
    AdminMappingsGet200ResponseMappingsInnerRequest adminMappingsGet200ResponseMappingsInnerRequest = new AdminMappingsGet200ResponseMappingsInnerRequest(); // AdminMappingsGet200ResponseMappingsInnerRequest | 
    try {
      AdminRequestsCountPost200Response result = apiInstance.adminRequestsCountPost(adminMappingsGet200ResponseMappingsInnerRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RequestsApi#adminRequestsCountPost");
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
| **adminMappingsGet200ResponseMappingsInnerRequest** | [**AdminMappingsGet200ResponseMappingsInnerRequest**](AdminMappingsGet200ResponseMappingsInnerRequest.md)|  | |

### Return type

[**AdminRequestsCountPost200Response**](AdminRequestsCountPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Number of matching requests |  -  |

<a id="adminRequestsDelete"></a>
# **adminRequestsDelete**
> adminRequestsDelete()

Delete all requests in journal

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    RequestsApi apiInstance = new RequestsApi(defaultClient);
    try {
      apiInstance.adminRequestsDelete();
    } catch (ApiException e) {
      System.err.println("Exception when calling RequestsApi#adminRequestsDelete");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully deleted |  -  |

<a id="adminRequestsFindPost"></a>
# **adminRequestsFindPost**
> adminRequestsFindPost(adminMappingsGet200ResponseMappingsInnerRequest)

Find requests by criteria

Retrieve details of requests logged in the journal matching the specified criteria

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    RequestsApi apiInstance = new RequestsApi(defaultClient);
    AdminMappingsGet200ResponseMappingsInnerRequest adminMappingsGet200ResponseMappingsInnerRequest = new AdminMappingsGet200ResponseMappingsInnerRequest(); // AdminMappingsGet200ResponseMappingsInnerRequest | 
    try {
      apiInstance.adminRequestsFindPost(adminMappingsGet200ResponseMappingsInnerRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling RequestsApi#adminRequestsFindPost");
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
| **adminMappingsGet200ResponseMappingsInnerRequest** | [**AdminMappingsGet200ResponseMappingsInnerRequest**](AdminMappingsGet200ResponseMappingsInnerRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Matching request details |  -  |

<a id="adminRequestsGet"></a>
# **adminRequestsGet**
> adminRequestsGet(limit, since)

Get all requests in journal

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    RequestsApi apiInstance = new RequestsApi(defaultClient);
    String limit = "10"; // String | The maximum number of results to return
    String since = "2016-10-05T12:33:01.000Z"; // String | Only return logged requests after this date
    try {
      apiInstance.adminRequestsGet(limit, since);
    } catch (ApiException e) {
      System.err.println("Exception when calling RequestsApi#adminRequestsGet");
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
| **limit** | **String**| The maximum number of results to return | [optional] |
| **since** | **String**| Only return logged requests after this date | [optional] |

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
| **200** | List of received requests |  -  |

<a id="adminRequestsRemoveByMetadataPost"></a>
# **adminRequestsRemoveByMetadataPost**
> adminRequestsRemoveByMetadataPost(adminMappingsFindByMetadataPostRequest)

Delete requests mappings matching metadata

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    RequestsApi apiInstance = new RequestsApi(defaultClient);
    AdminMappingsFindByMetadataPostRequest adminMappingsFindByMetadataPostRequest = new AdminMappingsFindByMetadataPostRequest(); // AdminMappingsFindByMetadataPostRequest | 
    try {
      apiInstance.adminRequestsRemoveByMetadataPost(adminMappingsFindByMetadataPostRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling RequestsApi#adminRequestsRemoveByMetadataPost");
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
| **adminMappingsFindByMetadataPostRequest** | [**AdminMappingsFindByMetadataPostRequest**](AdminMappingsFindByMetadataPostRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Removed request details |  -  |

<a id="adminRequestsRemovePost"></a>
# **adminRequestsRemovePost**
> adminRequestsRemovePost(adminMappingsGet200ResponseMappingsInnerRequest)

Remove requests by criteria

Removed requests logged in the journal matching the specified criteria

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    RequestsApi apiInstance = new RequestsApi(defaultClient);
    AdminMappingsGet200ResponseMappingsInnerRequest adminMappingsGet200ResponseMappingsInnerRequest = new AdminMappingsGet200ResponseMappingsInnerRequest(); // AdminMappingsGet200ResponseMappingsInnerRequest | 
    try {
      apiInstance.adminRequestsRemovePost(adminMappingsGet200ResponseMappingsInnerRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling RequestsApi#adminRequestsRemovePost");
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
| **adminMappingsGet200ResponseMappingsInnerRequest** | [**AdminMappingsGet200ResponseMappingsInnerRequest**](AdminMappingsGet200ResponseMappingsInnerRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Removed request details |  -  |

<a id="adminRequestsRequestIdDelete"></a>
# **adminRequestsRequestIdDelete**
> adminRequestsRequestIdDelete(requestId)

Delete request by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    RequestsApi apiInstance = new RequestsApi(defaultClient);
    String requestId = "12fb14bb-600e-4bfa-bd8d-be7f12562c99"; // String | The UUID of the logged request
    try {
      apiInstance.adminRequestsRequestIdDelete(requestId);
    } catch (ApiException e) {
      System.err.println("Exception when calling RequestsApi#adminRequestsRequestIdDelete");
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
| **requestId** | **String**| The UUID of the logged request | |

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
| **200** | Successfully deleted |  -  |

<a id="adminRequestsRequestIdGet"></a>
# **adminRequestsRequestIdGet**
> adminRequestsRequestIdGet(requestId)

Get request by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    RequestsApi apiInstance = new RequestsApi(defaultClient);
    String requestId = "12fb14bb-600e-4bfa-bd8d-be7f12562c99"; // String | The UUID of the logged request
    try {
      apiInstance.adminRequestsRequestIdGet(requestId);
    } catch (ApiException e) {
      System.err.println("Exception when calling RequestsApi#adminRequestsRequestIdGet");
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
| **requestId** | **String**| The UUID of the logged request | |

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
| **404** | Request not found |  -  |

<a id="adminRequestsResetPost"></a>
# **adminRequestsResetPost**
> adminRequestsResetPost()

Empty the request journal

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    RequestsApi apiInstance = new RequestsApi(defaultClient);
    try {
      apiInstance.adminRequestsResetPost();
    } catch (ApiException e) {
      System.err.println("Exception when calling RequestsApi#adminRequestsResetPost");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully reset |  -  |

<a id="adminRequestsUnmatchedGet"></a>
# **adminRequestsUnmatchedGet**
> adminRequestsUnmatchedGet()

Find unmatched requests

Get details of logged requests that weren&#39;t matched by any stub mapping

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    RequestsApi apiInstance = new RequestsApi(defaultClient);
    try {
      apiInstance.adminRequestsUnmatchedGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling RequestsApi#adminRequestsUnmatchedGet");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Unmatched request details |  -  |

