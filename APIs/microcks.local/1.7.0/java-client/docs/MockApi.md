# MockApi

All URIs are relative to *http://microcks.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteService**](MockApi.md#deleteService) | **DELETE** /services/{id} | Delete Service |
| [**exportSnapshot**](MockApi.md#exportSnapshot) | **GET** /export | Export a snapshot |
| [**getService**](MockApi.md#getService) | **GET** /services/{id} | Get Service |
| [**getServices**](MockApi.md#getServices) | **GET** /services | Get Services and APIs |
| [**getServicesCounter**](MockApi.md#getServicesCounter) | **GET** /services/count | Get the Services counter |
| [**getServicesLabels**](MockApi.md#getServicesLabels) | **GET** /services/labels | Get the already used labels for Services |
| [**importSnapshot**](MockApi.md#importSnapshot) | **POST** /import | Import a snapshot |
| [**overrideServiceOperation**](MockApi.md#overrideServiceOperation) | **PUT** /services/{id}/operation | Override Service Operation |
| [**searchServices**](MockApi.md#searchServices) | **GET** /services/search | Search for Services and APIs |
| [**updateServiceMetadata**](MockApi.md#updateServiceMetadata) | **PUT** /services/{id}/metadata | Update Service Metadata |


<a id="deleteService"></a>
# **deleteService**
> deleteService(id)

Delete Service

Delete a Service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MockApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://microcks.local");
    
    // Configure OAuth2 access token for authorization: jwt-bearer
    OAuth jwt-bearer = (OAuth) defaultClient.getAuthentication("jwt-bearer");
    jwt-bearer.setAccessToken("YOUR ACCESS TOKEN");

    MockApi apiInstance = new MockApi(defaultClient);
    String id = "id_example"; // String | Unique identifier of Service to managed
    try {
      apiInstance.deleteService(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling MockApi#deleteService");
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
| **id** | **String**| Unique identifier of Service to managed | |

### Return type

null (empty response body)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Service has been deleted |  -  |

<a id="exportSnapshot"></a>
# **exportSnapshot**
> File exportSnapshot(serviceIds)

Export a snapshot

Export a repostiory snapshot with requested services

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MockApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://microcks.local");
    
    // Configure OAuth2 access token for authorization: jwt-bearer
    OAuth jwt-bearer = (OAuth) defaultClient.getAuthentication("jwt-bearer");
    jwt-bearer.setAccessToken("YOUR ACCESS TOKEN");

    MockApi apiInstance = new MockApi(defaultClient);
    List<String> serviceIds = Arrays.asList(); // List<String> | List of service identifiers to export
    try {
      File result = apiInstance.exportSnapshot(serviceIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MockApi#exportSnapshot");
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
| **serviceIds** | [**List&lt;String&gt;**](String.md)| List of service identifiers to export | |

### Return type

[**File**](File.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Snapshot file representing the export of requested services |  * Content-Disposition -  <br>  |

<a id="getService"></a>
# **getService**
> GetService200Response getService(id, messages)

Get Service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MockApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://microcks.local");
    
    // Configure OAuth2 access token for authorization: jwt-bearer
    OAuth jwt-bearer = (OAuth) defaultClient.getAuthentication("jwt-bearer");
    jwt-bearer.setAccessToken("YOUR ACCESS TOKEN");

    MockApi apiInstance = new MockApi(defaultClient);
    String id = "id_example"; // String | Unique identifier of Service to managed
    Boolean messages = true; // Boolean | Whether to include details on services messages into result. Default is false
    try {
      GetService200Response result = apiInstance.getService(id, messages);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MockApi#getService");
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
| **id** | **String**| Unique identifier of Service to managed | |
| **messages** | **Boolean**| Whether to include details on services messages into result. Default is false | [optional] |

### Return type

[**GetService200Response**](GetService200Response.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="getServices"></a>
# **getServices**
> Service getServices(page, size)

Get Services and APIs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MockApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://microcks.local");
    
    // Configure OAuth2 access token for authorization: jwt-bearer
    OAuth jwt-bearer = (OAuth) defaultClient.getAuthentication("jwt-bearer");
    jwt-bearer.setAccessToken("YOUR ACCESS TOKEN");

    MockApi apiInstance = new MockApi(defaultClient);
    Integer page = 56; // Integer | Page of Services to retrieve (starts at and defaults to 0)
    Integer size = 56; // Integer | Size of a page. Maximum number of Services to include in a response (defaults to 20)
    try {
      Service result = apiInstance.getServices(page, size);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MockApi#getServices");
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
| **page** | **Integer**| Page of Services to retrieve (starts at and defaults to 0) | [optional] |
| **size** | **Integer**| Size of a page. Maximum number of Services to include in a response (defaults to 20) | [optional] |

### Return type

[**Service**](Service.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of found Services |  -  |

<a id="getServicesCounter"></a>
# **getServicesCounter**
> Counter getServicesCounter()

Get the Services counter

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MockApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://microcks.local");
    
    // Configure OAuth2 access token for authorization: jwt-bearer
    OAuth jwt-bearer = (OAuth) defaultClient.getAuthentication("jwt-bearer");
    jwt-bearer.setAccessToken("YOUR ACCESS TOKEN");

    MockApi apiInstance = new MockApi(defaultClient);
    try {
      Counter result = apiInstance.getServicesCounter();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MockApi#getServicesCounter");
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

[**Counter**](Counter.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Number of Services in datastore |  -  |

<a id="getServicesLabels"></a>
# **getServicesLabels**
> Map&lt;String, List&lt;String&gt;&gt; getServicesLabels()

Get the already used labels for Services

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MockApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://microcks.local");
    
    // Configure OAuth2 access token for authorization: jwt-bearer
    OAuth jwt-bearer = (OAuth) defaultClient.getAuthentication("jwt-bearer");
    jwt-bearer.setAccessToken("YOUR ACCESS TOKEN");

    MockApi apiInstance = new MockApi(defaultClient);
    try {
      Map<String, List<String>> result = apiInstance.getServicesLabels();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MockApi#getServicesLabels");
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

[**Map&lt;String, List&lt;String&gt;&gt;**](List.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Already used labels: keys are label Keys, values are array of label Values |  -  |

<a id="importSnapshot"></a>
# **importSnapshot**
> importSnapshot(_file)

Import a snapshot

Import a repository snapshot previsouly exported into Microcks

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MockApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://microcks.local");
    
    // Configure OAuth2 access token for authorization: jwt-bearer
    OAuth jwt-bearer = (OAuth) defaultClient.getAuthentication("jwt-bearer");
    jwt-bearer.setAccessToken("YOUR ACCESS TOKEN");

    MockApi apiInstance = new MockApi(defaultClient);
    File _file = new File("/path/to/file"); // File | The repository snapshot file
    try {
      apiInstance.importSnapshot(_file);
    } catch (ApiException e) {
      System.err.println("Exception when calling MockApi#importSnapshot");
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
| **_file** | **File**| The repository snapshot file | |

### Return type

null (empty response body)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Snasphot has been correctly imported |  -  |

<a id="overrideServiceOperation"></a>
# **overrideServiceOperation**
> overrideServiceOperation(id, operationName, operationOverrideDTO)

Override Service Operation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MockApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://microcks.local");
    
    // Configure OAuth2 access token for authorization: jwt-bearer
    OAuth jwt-bearer = (OAuth) defaultClient.getAuthentication("jwt-bearer");
    jwt-bearer.setAccessToken("YOUR ACCESS TOKEN");

    MockApi apiInstance = new MockApi(defaultClient);
    String id = "id_example"; // String | Unique identifier of Service to managed
    String operationName = "operationName_example"; // String | Name of operation to update
    OperationOverrideDTO operationOverrideDTO = new OperationOverrideDTO(); // OperationOverrideDTO | 
    try {
      apiInstance.overrideServiceOperation(id, operationName, operationOverrideDTO);
    } catch (ApiException e) {
      System.err.println("Exception when calling MockApi#overrideServiceOperation");
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
| **id** | **String**| Unique identifier of Service to managed | |
| **operationName** | **String**| Name of operation to update | |
| **operationOverrideDTO** | [**OperationOverrideDTO**](OperationOverrideDTO.md)|  | |

### Return type

null (empty response body)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Operation has been updated |  -  |
| **500** | Operation cannot be updated |  -  |

<a id="searchServices"></a>
# **searchServices**
> List&lt;Service&gt; searchServices(queryMap)

Search for Services and APIs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MockApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://microcks.local");
    
    // Configure OAuth2 access token for authorization: jwt-bearer
    OAuth jwt-bearer = (OAuth) defaultClient.getAuthentication("jwt-bearer");
    jwt-bearer.setAccessToken("YOUR ACCESS TOKEN");

    MockApi apiInstance = new MockApi(defaultClient);
    Map<String, String> queryMap = new HashMap(); // Map<String, String> | Map of criterion. Key can be simply 'name' with value as the searched string. You can also search by label using keys like 'labels.x' where 'x' is the label and value the label value
    try {
      List<Service> result = apiInstance.searchServices(queryMap);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MockApi#searchServices");
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
| **queryMap** | [**Map&lt;String, String&gt;**](String.md)| Map of criterion. Key can be simply &#39;name&#39; with value as the searched string. You can also search by label using keys like &#39;labels.x&#39; where &#39;x&#39; is the label and value the label value | |

### Return type

[**List&lt;Service&gt;**](Service.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of found Services (filtered according search criteria) |  -  |

<a id="updateServiceMetadata"></a>
# **updateServiceMetadata**
> updateServiceMetadata(id, metadata)

Update Service Metadata

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MockApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://microcks.local");
    
    // Configure OAuth2 access token for authorization: jwt-bearer
    OAuth jwt-bearer = (OAuth) defaultClient.getAuthentication("jwt-bearer");
    jwt-bearer.setAccessToken("YOUR ACCESS TOKEN");

    MockApi apiInstance = new MockApi(defaultClient);
    String id = "id_example"; // String | Unique identifier of Service to managed
    Metadata metadata = new Metadata(); // Metadata | 
    try {
      apiInstance.updateServiceMetadata(id, metadata);
    } catch (ApiException e) {
      System.err.println("Exception when calling MockApi#updateServiceMetadata");
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
| **id** | **String**| Unique identifier of Service to managed | |
| **metadata** | [**Metadata**](Metadata.md)|  | |

### Return type

null (empty response body)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Service metadata has been updated |  -  |
| **500** | Update of metadata failed |  -  |

