# As2StationsApi

All URIs are relative to *http://app.files.com/api/rest/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteAs2StationsId**](As2StationsApi.md#deleteAs2StationsId) | **DELETE** /as2_stations/{id} | Delete As2 Station |
| [**getAs2Stations**](As2StationsApi.md#getAs2Stations) | **GET** /as2_stations | List As2 Stations |
| [**getAs2StationsId**](As2StationsApi.md#getAs2StationsId) | **GET** /as2_stations/{id} | Show As2 Station |
| [**patchAs2StationsId**](As2StationsApi.md#patchAs2StationsId) | **PATCH** /as2_stations/{id} | Update As2 Station |
| [**postAs2Stations**](As2StationsApi.md#postAs2Stations) | **POST** /as2_stations | Create As2 Station |


<a id="deleteAs2StationsId"></a>
# **deleteAs2StationsId**
> deleteAs2StationsId(id)

Delete As2 Station

Delete As2 Station

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.As2StationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    As2StationsApi apiInstance = new As2StationsApi(defaultClient);
    Integer id = 56; // Integer | As2 Station ID.
    try {
      apiInstance.deleteAs2StationsId(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling As2StationsApi#deleteAs2StationsId");
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
| **id** | **Integer**| As2 Station ID. | |

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
| **204** | No body. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **409** | Conflict |  -  |
| **412** | Precondition Failed |  -  |
| **422** | Unprocessable Entity |  -  |
| **423** | Locked |  -  |
| **429** | Too Many Requests |  -  |

<a id="getAs2Stations"></a>
# **getAs2Stations**
> List&lt;As2StationEntity&gt; getAs2Stations(cursor, perPage)

List As2 Stations

List As2 Stations

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.As2StationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    As2StationsApi apiInstance = new As2StationsApi(defaultClient);
    String cursor = "cursor_example"; // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    Integer perPage = 56; // Integer | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    try {
      List<As2StationEntity> result = apiInstance.getAs2Stations(cursor, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling As2StationsApi#getAs2Stations");
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
| **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] |
| **perPage** | **Integer**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] |

### Return type

[**List&lt;As2StationEntity&gt;**](As2StationEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of As2Stations objects. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **409** | Conflict |  -  |
| **412** | Precondition Failed |  -  |
| **422** | Unprocessable Entity |  -  |
| **423** | Locked |  -  |
| **429** | Too Many Requests |  -  |

<a id="getAs2StationsId"></a>
# **getAs2StationsId**
> As2StationEntity getAs2StationsId(id)

Show As2 Station

Show As2 Station

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.As2StationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    As2StationsApi apiInstance = new As2StationsApi(defaultClient);
    Integer id = 56; // Integer | As2 Station ID.
    try {
      As2StationEntity result = apiInstance.getAs2StationsId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling As2StationsApi#getAs2StationsId");
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
| **id** | **Integer**| As2 Station ID. | |

### Return type

[**As2StationEntity**](As2StationEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The As2Stations object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **409** | Conflict |  -  |
| **412** | Precondition Failed |  -  |
| **422** | Unprocessable Entity |  -  |
| **423** | Locked |  -  |
| **429** | Too Many Requests |  -  |

<a id="patchAs2StationsId"></a>
# **patchAs2StationsId**
> As2StationEntity patchAs2StationsId(id, name, privateKey, privateKeyPassword, publicCertificate)

Update As2 Station

Update As2 Station

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.As2StationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    As2StationsApi apiInstance = new As2StationsApi(defaultClient);
    Integer id = 56; // Integer | As2 Station ID.
    String name = "name_example"; // String | AS2 Name
    String privateKey = "privateKey_example"; // String | 
    String privateKeyPassword = "privateKeyPassword_example"; // String | 
    String publicCertificate = "publicCertificate_example"; // String | 
    try {
      As2StationEntity result = apiInstance.patchAs2StationsId(id, name, privateKey, privateKeyPassword, publicCertificate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling As2StationsApi#patchAs2StationsId");
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
| **id** | **Integer**| As2 Station ID. | |
| **name** | **String**| AS2 Name | [optional] |
| **privateKey** | **String**|  | [optional] |
| **privateKeyPassword** | **String**|  | [optional] |
| **publicCertificate** | **String**|  | [optional] |

### Return type

[**As2StationEntity**](As2StationEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The As2Stations object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **409** | Conflict |  -  |
| **412** | Precondition Failed |  -  |
| **422** | Unprocessable Entity |  -  |
| **423** | Locked |  -  |
| **429** | Too Many Requests |  -  |

<a id="postAs2Stations"></a>
# **postAs2Stations**
> As2StationEntity postAs2Stations(name, privateKey, publicCertificate, privateKeyPassword)

Create As2 Station

Create As2 Station

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.As2StationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    As2StationsApi apiInstance = new As2StationsApi(defaultClient);
    String name = "name_example"; // String | AS2 Name
    String privateKey = "privateKey_example"; // String | 
    String publicCertificate = "publicCertificate_example"; // String | 
    String privateKeyPassword = "privateKeyPassword_example"; // String | 
    try {
      As2StationEntity result = apiInstance.postAs2Stations(name, privateKey, publicCertificate, privateKeyPassword);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling As2StationsApi#postAs2Stations");
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
| **name** | **String**| AS2 Name | |
| **privateKey** | **String**|  | |
| **publicCertificate** | **String**|  | |
| **privateKeyPassword** | **String**|  | [optional] |

### Return type

[**As2StationEntity**](As2StationEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The As2Stations object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **409** | Conflict |  -  |
| **412** | Precondition Failed |  -  |
| **422** | Unprocessable Entity |  -  |
| **423** | Locked |  -  |
| **429** | Too Many Requests |  -  |

