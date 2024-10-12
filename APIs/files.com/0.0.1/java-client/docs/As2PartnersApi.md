# As2PartnersApi

All URIs are relative to *http://app.files.com/api/rest/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteAs2PartnersId**](As2PartnersApi.md#deleteAs2PartnersId) | **DELETE** /as2_partners/{id} | Delete As2 Partner |
| [**getAs2Partners**](As2PartnersApi.md#getAs2Partners) | **GET** /as2_partners | List As2 Partners |
| [**getAs2PartnersId**](As2PartnersApi.md#getAs2PartnersId) | **GET** /as2_partners/{id} | Show As2 Partner |
| [**patchAs2PartnersId**](As2PartnersApi.md#patchAs2PartnersId) | **PATCH** /as2_partners/{id} | Update As2 Partner |
| [**postAs2Partners**](As2PartnersApi.md#postAs2Partners) | **POST** /as2_partners | Create As2 Partner |


<a id="deleteAs2PartnersId"></a>
# **deleteAs2PartnersId**
> deleteAs2PartnersId(id)

Delete As2 Partner

Delete As2 Partner

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.As2PartnersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    As2PartnersApi apiInstance = new As2PartnersApi(defaultClient);
    Integer id = 56; // Integer | As2 Partner ID.
    try {
      apiInstance.deleteAs2PartnersId(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling As2PartnersApi#deleteAs2PartnersId");
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
| **id** | **Integer**| As2 Partner ID. | |

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

<a id="getAs2Partners"></a>
# **getAs2Partners**
> List&lt;As2PartnerEntity&gt; getAs2Partners(cursor, perPage)

List As2 Partners

List As2 Partners

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.As2PartnersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    As2PartnersApi apiInstance = new As2PartnersApi(defaultClient);
    String cursor = "cursor_example"; // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    Integer perPage = 56; // Integer | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    try {
      List<As2PartnerEntity> result = apiInstance.getAs2Partners(cursor, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling As2PartnersApi#getAs2Partners");
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

[**List&lt;As2PartnerEntity&gt;**](As2PartnerEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of As2Partners objects. |  -  |
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

<a id="getAs2PartnersId"></a>
# **getAs2PartnersId**
> As2PartnerEntity getAs2PartnersId(id)

Show As2 Partner

Show As2 Partner

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.As2PartnersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    As2PartnersApi apiInstance = new As2PartnersApi(defaultClient);
    Integer id = 56; // Integer | As2 Partner ID.
    try {
      As2PartnerEntity result = apiInstance.getAs2PartnersId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling As2PartnersApi#getAs2PartnersId");
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
| **id** | **Integer**| As2 Partner ID. | |

### Return type

[**As2PartnerEntity**](As2PartnerEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The As2Partners object. |  -  |
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

<a id="patchAs2PartnersId"></a>
# **patchAs2PartnersId**
> As2PartnerEntity patchAs2PartnersId(id, enableDedicatedIps, name, publicCertificate, serverCertificate, uri)

Update As2 Partner

Update As2 Partner

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.As2PartnersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    As2PartnersApi apiInstance = new As2PartnersApi(defaultClient);
    Integer id = 56; // Integer | As2 Partner ID.
    Boolean enableDedicatedIps = true; // Boolean | 
    String name = "name_example"; // String | AS2 Name
    String publicCertificate = "publicCertificate_example"; // String | 
    String serverCertificate = "serverCertificate_example"; // String | Remote server certificate security setting
    String uri = "uri_example"; // String | URL base for AS2 responses
    try {
      As2PartnerEntity result = apiInstance.patchAs2PartnersId(id, enableDedicatedIps, name, publicCertificate, serverCertificate, uri);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling As2PartnersApi#patchAs2PartnersId");
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
| **id** | **Integer**| As2 Partner ID. | |
| **enableDedicatedIps** | **Boolean**|  | [optional] |
| **name** | **String**| AS2 Name | [optional] |
| **publicCertificate** | **String**|  | [optional] |
| **serverCertificate** | **String**| Remote server certificate security setting | [optional] |
| **uri** | **String**| URL base for AS2 responses | [optional] |

### Return type

[**As2PartnerEntity**](As2PartnerEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The As2Partners object. |  -  |
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

<a id="postAs2Partners"></a>
# **postAs2Partners**
> As2PartnerEntity postAs2Partners(as2StationId, name, publicCertificate, uri, enableDedicatedIps, serverCertificate)

Create As2 Partner

Create As2 Partner

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.As2PartnersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    As2PartnersApi apiInstance = new As2PartnersApi(defaultClient);
    Integer as2StationId = 56; // Integer | Id of As2Station for this partner
    String name = "name_example"; // String | AS2 Name
    String publicCertificate = "publicCertificate_example"; // String | 
    String uri = "uri_example"; // String | URL base for AS2 responses
    Boolean enableDedicatedIps = true; // Boolean | 
    String serverCertificate = "serverCertificate_example"; // String | Remote server certificate security setting
    try {
      As2PartnerEntity result = apiInstance.postAs2Partners(as2StationId, name, publicCertificate, uri, enableDedicatedIps, serverCertificate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling As2PartnersApi#postAs2Partners");
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
| **as2StationId** | **Integer**| Id of As2Station for this partner | |
| **name** | **String**| AS2 Name | |
| **publicCertificate** | **String**|  | |
| **uri** | **String**| URL base for AS2 responses | |
| **enableDedicatedIps** | **Boolean**|  | [optional] |
| **serverCertificate** | **String**| Remote server certificate security setting | [optional] |

### Return type

[**As2PartnerEntity**](As2PartnerEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The As2Partners object. |  -  |
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

