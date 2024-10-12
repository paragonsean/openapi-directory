# AuditsApi

All URIs are relative to *https://watchful.li/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteAuditById**](AuditsApi.md#deleteAuditById) | **DELETE** /audits/{id} | Delete a specific audit |
| [**getAuditById**](AuditsApi.md#getAuditById) | **GET** /audits/{id} | Find audit by ID |
| [**getAudits**](AuditsApi.md#getAudits) | **GET** /audits | Get a list of audits |
| [**getFieldsAudits**](AuditsApi.md#getFieldsAudits) | **GET** /audits/metadata | Get the list of fields |


<a id="deleteAuditById"></a>
# **deleteAuditById**
> String deleteAuditById(id)

Delete a specific audit

Delete a specific audit

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuditsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://watchful.li/api/v1");

    AuditsApi apiInstance = new AuditsApi(defaultClient);
    Long id = 56L; // Long | ID of audit that needs to be deleted
    try {
      String result = apiInstance.deleteAuditById(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuditsApi#deleteAuditById");
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
| **id** | **Long**| ID of audit that needs to be deleted | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Audit correctly deleted |  -  |
| **403** | Invalid API Key |  -  |
| **404** | Invalid ID |  -  |

<a id="getAuditById"></a>
# **getAuditById**
> Audit getAuditById(id, fields)

Find audit by ID

Returns a audit based on ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuditsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://watchful.li/api/v1");

    AuditsApi apiInstance = new AuditsApi(defaultClient);
    Long id = 56L; // Long | ID of audit that needs to be fetched
    String fields = "fields_example"; // String | Fields to return separate by comas: name,id
    try {
      Audit result = apiInstance.getAuditById(id, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuditsApi#getAuditById");
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
| **id** | **Long**| ID of audit that needs to be fetched | |
| **fields** | **String**| Fields to return separate by comas: name,id | [optional] |

### Return type

[**Audit**](Audit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **400** | Invalid ID |  -  |
| **403** | Invalid API Key |  -  |

<a id="getAudits"></a>
# **getAudits**
> Audit getAudits(limit, limitstart, order)

Get a list of audits

Returns a list of audits

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuditsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://watchful.li/api/v1");

    AuditsApi apiInstance = new AuditsApi(defaultClient);
    Long limit = 56L; // Long | Number of object to return (max 100, default 25)
    Long limitstart = 56L; // Long | Start of the return (default 0)
    String order = "order_example"; // String | ORDER by this field separete by comas. Add + / - after field for set ASC / DESC: type+,name-
    try {
      Audit result = apiInstance.getAudits(limit, limitstart, order);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuditsApi#getAudits");
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
| **limit** | **Long**| Number of object to return (max 100, default 25) | [optional] |
| **limitstart** | **Long**| Start of the return (default 0) | [optional] |
| **order** | **String**| ORDER by this field separete by comas. Add + / - after field for set ASC / DESC: type+,name- | [optional] |

### Return type

[**Audit**](Audit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **403** | Invalid API Key |  -  |

<a id="getFieldsAudits"></a>
# **getFieldsAudits**
> String getFieldsAudits()

Get the list of fields

Returns a list of fields

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuditsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://watchful.li/api/v1");

    AuditsApi apiInstance = new AuditsApi(defaultClient);
    try {
      String result = apiInstance.getFieldsAudits();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuditsApi#getFieldsAudits");
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

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

