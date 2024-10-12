# StubMappingsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**adminMappingsDelete**](StubMappingsApi.md#adminMappingsDelete) | **DELETE** /__admin/mappings | Delete all stub mappings |
| [**adminMappingsFindByMetadataPost**](StubMappingsApi.md#adminMappingsFindByMetadataPost) | **POST** /__admin/mappings/find-by-metadata |  |
| [**adminMappingsGet**](StubMappingsApi.md#adminMappingsGet) | **GET** /__admin/mappings | Get all stub mappings |
| [**adminMappingsImportPost**](StubMappingsApi.md#adminMappingsImportPost) | **POST** /__admin/mappings/import | Import stub mappings |
| [**adminMappingsPost**](StubMappingsApi.md#adminMappingsPost) | **POST** /__admin/mappings | Create a new stub mapping |
| [**adminMappingsRemoveByMetadataPost**](StubMappingsApi.md#adminMappingsRemoveByMetadataPost) | **POST** /__admin/mappings/remove-by-metadata | Delete stub mappings matching metadata |
| [**adminMappingsResetPost**](StubMappingsApi.md#adminMappingsResetPost) | **POST** /__admin/mappings/reset | Reset stub mappings |
| [**adminMappingsSavePost**](StubMappingsApi.md#adminMappingsSavePost) | **POST** /__admin/mappings/save | Persist stub mappings |
| [**adminMappingsStubMappingIdDelete**](StubMappingsApi.md#adminMappingsStubMappingIdDelete) | **DELETE** /__admin/mappings/{stubMappingId} | Delete a stub mapping |
| [**adminMappingsStubMappingIdGet**](StubMappingsApi.md#adminMappingsStubMappingIdGet) | **GET** /__admin/mappings/{stubMappingId} | Get stub mapping by ID |
| [**adminMappingsStubMappingIdPut**](StubMappingsApi.md#adminMappingsStubMappingIdPut) | **PUT** /__admin/mappings/{stubMappingId} | Update a stub mapping |


<a id="adminMappingsDelete"></a>
# **adminMappingsDelete**
> adminMappingsDelete()

Delete all stub mappings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StubMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    StubMappingsApi apiInstance = new StubMappingsApi(defaultClient);
    try {
      apiInstance.adminMappingsDelete();
    } catch (ApiException e) {
      System.err.println("Exception when calling StubMappingsApi#adminMappingsDelete");
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

<a id="adminMappingsFindByMetadataPost"></a>
# **adminMappingsFindByMetadataPost**
> AdminMappingsGet200Response adminMappingsFindByMetadataPost(adminMappingsFindByMetadataPostRequest)



Find stubs by matching on their metadata

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StubMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    StubMappingsApi apiInstance = new StubMappingsApi(defaultClient);
    AdminMappingsFindByMetadataPostRequest adminMappingsFindByMetadataPostRequest = new AdminMappingsFindByMetadataPostRequest(); // AdminMappingsFindByMetadataPostRequest | 
    try {
      AdminMappingsGet200Response result = apiInstance.adminMappingsFindByMetadataPost(adminMappingsFindByMetadataPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StubMappingsApi#adminMappingsFindByMetadataPost");
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
| **adminMappingsFindByMetadataPostRequest** | [**AdminMappingsFindByMetadataPostRequest**](AdminMappingsFindByMetadataPostRequest.md)|  | |

### Return type

[**AdminMappingsGet200Response**](AdminMappingsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Matched stub mappings |  -  |

<a id="adminMappingsGet"></a>
# **adminMappingsGet**
> AdminMappingsGet200Response adminMappingsGet(limit, offset)

Get all stub mappings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StubMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    StubMappingsApi apiInstance = new StubMappingsApi(defaultClient);
    Integer limit = 10; // Integer | The maximum number of results to return
    Integer offset = 0; // Integer | The start index of the results to return
    try {
      AdminMappingsGet200Response result = apiInstance.adminMappingsGet(limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StubMappingsApi#adminMappingsGet");
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
| **limit** | **Integer**| The maximum number of results to return | [optional] |
| **offset** | **Integer**| The start index of the results to return | [optional] |

### Return type

[**AdminMappingsGet200Response**](AdminMappingsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All stub mappings |  -  |

<a id="adminMappingsImportPost"></a>
# **adminMappingsImportPost**
> adminMappingsImportPost()

Import stub mappings

Import given stub mappings to the backing store

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StubMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    StubMappingsApi apiInstance = new StubMappingsApi(defaultClient);
    try {
      apiInstance.adminMappingsImportPost();
    } catch (ApiException e) {
      System.err.println("Exception when calling StubMappingsApi#adminMappingsImportPost");
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
| **200** | Successfully imported |  -  |

<a id="adminMappingsPost"></a>
# **adminMappingsPost**
> AdminMappingsGet200ResponseMappingsInner adminMappingsPost(adminMappingsGet200ResponseMappingsInner)

Create a new stub mapping

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StubMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    StubMappingsApi apiInstance = new StubMappingsApi(defaultClient);
    AdminMappingsGet200ResponseMappingsInner adminMappingsGet200ResponseMappingsInner = new AdminMappingsGet200ResponseMappingsInner(); // AdminMappingsGet200ResponseMappingsInner | 
    try {
      AdminMappingsGet200ResponseMappingsInner result = apiInstance.adminMappingsPost(adminMappingsGet200ResponseMappingsInner);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StubMappingsApi#adminMappingsPost");
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
| **adminMappingsGet200ResponseMappingsInner** | [**AdminMappingsGet200ResponseMappingsInner**](AdminMappingsGet200ResponseMappingsInner.md)|  | [optional] |

### Return type

[**AdminMappingsGet200ResponseMappingsInner**](AdminMappingsGet200ResponseMappingsInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The stub mapping |  -  |

<a id="adminMappingsRemoveByMetadataPost"></a>
# **adminMappingsRemoveByMetadataPost**
> adminMappingsRemoveByMetadataPost(adminMappingsFindByMetadataPostRequest)

Delete stub mappings matching metadata

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StubMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    StubMappingsApi apiInstance = new StubMappingsApi(defaultClient);
    AdminMappingsFindByMetadataPostRequest adminMappingsFindByMetadataPostRequest = new AdminMappingsFindByMetadataPostRequest(); // AdminMappingsFindByMetadataPostRequest | 
    try {
      apiInstance.adminMappingsRemoveByMetadataPost(adminMappingsFindByMetadataPostRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling StubMappingsApi#adminMappingsRemoveByMetadataPost");
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
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The stub mappings were successfully removed |  -  |

<a id="adminMappingsResetPost"></a>
# **adminMappingsResetPost**
> adminMappingsResetPost()

Reset stub mappings

Restores stub mappings to the defaults defined back in the backing store

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StubMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    StubMappingsApi apiInstance = new StubMappingsApi(defaultClient);
    try {
      apiInstance.adminMappingsResetPost();
    } catch (ApiException e) {
      System.err.println("Exception when calling StubMappingsApi#adminMappingsResetPost");
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

<a id="adminMappingsSavePost"></a>
# **adminMappingsSavePost**
> adminMappingsSavePost()

Persist stub mappings

Save all persistent stub mappings to the backing store

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StubMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    StubMappingsApi apiInstance = new StubMappingsApi(defaultClient);
    try {
      apiInstance.adminMappingsSavePost();
    } catch (ApiException e) {
      System.err.println("Exception when calling StubMappingsApi#adminMappingsSavePost");
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
| **200** | Successfully saved |  -  |

<a id="adminMappingsStubMappingIdDelete"></a>
# **adminMappingsStubMappingIdDelete**
> adminMappingsStubMappingIdDelete(stubMappingId)

Delete a stub mapping

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StubMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    StubMappingsApi apiInstance = new StubMappingsApi(defaultClient);
    String stubMappingId = "730d3e32-d098-4169-a20c-554c3bedce58"; // String | The UUID of stub mapping
    try {
      apiInstance.adminMappingsStubMappingIdDelete(stubMappingId);
    } catch (ApiException e) {
      System.err.println("Exception when calling StubMappingsApi#adminMappingsStubMappingIdDelete");
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
| **stubMappingId** | **String**| The UUID of stub mapping | |

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
| **200** | OK |  -  |
| **404** | Stub mapping not found |  -  |

<a id="adminMappingsStubMappingIdGet"></a>
# **adminMappingsStubMappingIdGet**
> AdminMappingsGet200ResponseMappingsInner adminMappingsStubMappingIdGet(stubMappingId)

Get stub mapping by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StubMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    StubMappingsApi apiInstance = new StubMappingsApi(defaultClient);
    String stubMappingId = "730d3e32-d098-4169-a20c-554c3bedce58"; // String | The UUID of stub mapping
    try {
      AdminMappingsGet200ResponseMappingsInner result = apiInstance.adminMappingsStubMappingIdGet(stubMappingId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StubMappingsApi#adminMappingsStubMappingIdGet");
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
| **stubMappingId** | **String**| The UUID of stub mapping | |

### Return type

[**AdminMappingsGet200ResponseMappingsInner**](AdminMappingsGet200ResponseMappingsInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The stub mapping |  -  |
| **404** | Stub mapping not found |  -  |

<a id="adminMappingsStubMappingIdPut"></a>
# **adminMappingsStubMappingIdPut**
> AdminMappingsGet200ResponseMappingsInner adminMappingsStubMappingIdPut(stubMappingId, adminMappingsGet200ResponseMappingsInner)

Update a stub mapping

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StubMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    StubMappingsApi apiInstance = new StubMappingsApi(defaultClient);
    String stubMappingId = "730d3e32-d098-4169-a20c-554c3bedce58"; // String | The UUID of stub mapping
    AdminMappingsGet200ResponseMappingsInner adminMappingsGet200ResponseMappingsInner = new AdminMappingsGet200ResponseMappingsInner(); // AdminMappingsGet200ResponseMappingsInner | 
    try {
      AdminMappingsGet200ResponseMappingsInner result = apiInstance.adminMappingsStubMappingIdPut(stubMappingId, adminMappingsGet200ResponseMappingsInner);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StubMappingsApi#adminMappingsStubMappingIdPut");
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
| **stubMappingId** | **String**| The UUID of stub mapping | |
| **adminMappingsGet200ResponseMappingsInner** | [**AdminMappingsGet200ResponseMappingsInner**](AdminMappingsGet200ResponseMappingsInner.md)|  | [optional] |

### Return type

[**AdminMappingsGet200ResponseMappingsInner**](AdminMappingsGet200ResponseMappingsInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The stub mapping |  -  |
| **404** | Stub mapping not found |  -  |

