# FieldApi

All URIs are relative to *https://api-2445581398133.apicast.io:443/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getFieldCollection**](FieldApi.md#getFieldCollection) | **GET** /application/field/list | GET for field |
| [**getFieldCountCollection**](FieldApi.md#getFieldCountCollection) | **GET** /application/field/count | COUNT for field |
| [**getFieldEntity**](FieldApi.md#getFieldEntity) | **GET** /application/field/{field_id} | GET for field |


<a id="getFieldCollection"></a>
# **getFieldCollection**
> List&lt;FieldEntity&gt; getFieldCollection(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, X_API2CRM_DESCRIBE_LIFETIME, pageSize, page, filter, fields)

GET for field

Returns all fields from the system

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FieldApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    FieldApi apiInstance = new FieldApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | User Key
    String X_API2CRM_APPLICATION_KEY = "7ae5b17008fb414d84981191cf3b66a476ef8bef"; // String | Application Key
    String X_API2CRM_DESCRIBE_LIFETIME = "X_API2CRM_DESCRIBE_LIFETIME_example"; // String | Describe lifetime
    Integer pageSize = 56; // Integer | Amount of results (default: 25)
    Integer page = 56; // Integer | Page to show (default: 1)
    String filter = "filter_example"; // String | Filter
    String fields = "fields_example"; // String | Comma-separated list of fields to include in the response
    try {
      List<FieldEntity> result = apiInstance.getFieldCollection(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, X_API2CRM_DESCRIBE_LIFETIME, pageSize, page, filter, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FieldApi#getFieldCollection");
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
| **X_API2CRM_USER_KEY** | **String**| User Key | [default to e2a6379ab878ae7e58119d4ec842bf9c] |
| **X_API2CRM_APPLICATION_KEY** | **String**| Application Key | [default to 7ae5b17008fb414d84981191cf3b66a476ef8bef] |
| **X_API2CRM_DESCRIBE_LIFETIME** | **String**| Describe lifetime | [optional] |
| **pageSize** | **Integer**| Amount of results (default: 25) | [optional] |
| **page** | **Integer**| Page to show (default: 1) | [optional] |
| **filter** | **String**| Filter | [optional] |
| **fields** | **String**| Comma-separated list of fields to include in the response | [optional] |

### Return type

[**List&lt;FieldEntity&gt;**](FieldEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not Found |  -  |

<a id="getFieldCountCollection"></a>
# **getFieldCountCollection**
> Count getFieldCountCollection(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY)

COUNT for field

Count all fields from the system

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FieldApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    FieldApi apiInstance = new FieldApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | User Key
    String X_API2CRM_APPLICATION_KEY = "7ae5b17008fb414d84981191cf3b66a476ef8bef"; // String | Application Key
    try {
      Count result = apiInstance.getFieldCountCollection(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FieldApi#getFieldCountCollection");
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
| **X_API2CRM_USER_KEY** | **String**| User Key | [default to e2a6379ab878ae7e58119d4ec842bf9c] |
| **X_API2CRM_APPLICATION_KEY** | **String**| Application Key | [default to 7ae5b17008fb414d84981191cf3b66a476ef8bef] |

### Return type

[**Count**](Count.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not Found |  -  |

<a id="getFieldEntity"></a>
# **getFieldEntity**
> FieldEntity getFieldEntity(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, fieldId, X_API2CRM_DESCRIBE_LIFETIME, fields)

GET for field

Return field information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FieldApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    FieldApi apiInstance = new FieldApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | User Key
    String X_API2CRM_APPLICATION_KEY = "7ae5b17008fb414d84981191cf3b66a476ef8bef"; // String | Application Key
    String fieldId = "fieldId_example"; // String | Field Identifier
    String X_API2CRM_DESCRIBE_LIFETIME = "X_API2CRM_DESCRIBE_LIFETIME_example"; // String | Describe lifetime
    String fields = "fields_example"; // String | Comma-separated list of fields to include in the response
    try {
      FieldEntity result = apiInstance.getFieldEntity(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, fieldId, X_API2CRM_DESCRIBE_LIFETIME, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FieldApi#getFieldEntity");
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
| **X_API2CRM_USER_KEY** | **String**| User Key | [default to e2a6379ab878ae7e58119d4ec842bf9c] |
| **X_API2CRM_APPLICATION_KEY** | **String**| Application Key | [default to 7ae5b17008fb414d84981191cf3b66a476ef8bef] |
| **fieldId** | **String**| Field Identifier | |
| **X_API2CRM_DESCRIBE_LIFETIME** | **String**| Describe lifetime | [optional] |
| **fields** | **String**| Comma-separated list of fields to include in the response | [optional] |

### Return type

[**FieldEntity**](FieldEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not Found |  -  |

