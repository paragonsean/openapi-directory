# FieldItemApi

All URIs are relative to *https://api-2445581398133.apicast.io:443/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createFieldItemEntity**](FieldItemApi.md#createFieldItemEntity) | **POST** /application/field/{field_id} | POST for fieldItem |
| [**deleteFieldItemEntity**](FieldItemApi.md#deleteFieldItemEntity) | **DELETE** /application/field/{field_id}/{field_item_id} | DELETE for fieldItem |
| [**getFieldItemCollection**](FieldItemApi.md#getFieldItemCollection) | **GET** /application/field/{field_id}/list | GET for fieldItem |
| [**getFieldItemCountCollection**](FieldItemApi.md#getFieldItemCountCollection) | **GET** /application/field/{field_id}/count | COUNT for fieldItem |
| [**getFieldItemDescribe**](FieldItemApi.md#getFieldItemDescribe) | **GET** /application/field/{field_id}/describe | DESCRIBE for fieldItem |
| [**getFieldItemEntity**](FieldItemApi.md#getFieldItemEntity) | **GET** /application/field/{field_id}/{field_item_id} | GET for fieldItem |
| [**updateFieldItemEntity**](FieldItemApi.md#updateFieldItemEntity) | **PUT** /application/field/{field_id}/{field_item_id} | PUT for fieldItem |


<a id="createFieldItemEntity"></a>
# **createFieldItemEntity**
> FieldItemEntityRelation createFieldItemEntity(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, fieldId, body, X_API2CRM_DESCRIBE_LIFETIME)

POST for fieldItem

Add field item into the system

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FieldItemApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    FieldItemApi apiInstance = new FieldItemApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | User Key
    String X_API2CRM_APPLICATION_KEY = "7ae5b17008fb414d84981191cf3b66a476ef8bef"; // String | Application Key
    String fieldId = "fieldId_example"; // String | Field Identifier
    FieldItemEntity body = new FieldItemEntity(); // FieldItemEntity | Add field item into the system
    String X_API2CRM_DESCRIBE_LIFETIME = "X_API2CRM_DESCRIBE_LIFETIME_example"; // String | Describe lifetime
    try {
      FieldItemEntityRelation result = apiInstance.createFieldItemEntity(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, fieldId, body, X_API2CRM_DESCRIBE_LIFETIME);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FieldItemApi#createFieldItemEntity");
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
| **body** | [**FieldItemEntity**](FieldItemEntity.md)| Add field item into the system | |
| **X_API2CRM_DESCRIBE_LIFETIME** | **String**| Describe lifetime | [optional] |

### Return type

[**FieldItemEntityRelation**](FieldItemEntityRelation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | Client Error |  -  |
| **404** | Not Found |  -  |
| **422** | Unprocessable Entity |  -  |

<a id="deleteFieldItemEntity"></a>
# **deleteFieldItemEntity**
> deleteFieldItemEntity(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, fieldId, fieldItemId)

DELETE for fieldItem

Delete field item information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FieldItemApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    FieldItemApi apiInstance = new FieldItemApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | User Key
    String X_API2CRM_APPLICATION_KEY = "7ae5b17008fb414d84981191cf3b66a476ef8bef"; // String | Application Key
    String fieldId = "fieldId_example"; // String | Field Identifier
    String fieldItemId = "fieldItemId_example"; // String | Field Item Identifier
    try {
      apiInstance.deleteFieldItemEntity(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, fieldId, fieldItemId);
    } catch (ApiException e) {
      System.err.println("Exception when calling FieldItemApi#deleteFieldItemEntity");
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
| **fieldItemId** | **String**| Field Item Identifier | |

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
| **204** | No Content |  -  |
| **404** | Not Found |  -  |

<a id="getFieldItemCollection"></a>
# **getFieldItemCollection**
> List&lt;FieldItemEntity&gt; getFieldItemCollection(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, fieldId, X_API2CRM_DESCRIBE_LIFETIME, pageSize, page, fields)

GET for fieldItem

Returns all fields from the system items

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FieldItemApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    FieldItemApi apiInstance = new FieldItemApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | User Key
    String X_API2CRM_APPLICATION_KEY = "7ae5b17008fb414d84981191cf3b66a476ef8bef"; // String | Application Key
    String fieldId = "fieldId_example"; // String | Field Identifier
    String X_API2CRM_DESCRIBE_LIFETIME = "X_API2CRM_DESCRIBE_LIFETIME_example"; // String | Describe lifetime
    Integer pageSize = 56; // Integer | Amount of results (default: 25)
    Integer page = 56; // Integer | Page to show (default: 1)
    String fields = "fields_example"; // String | Comma-separated list of fields to include in the response
    try {
      List<FieldItemEntity> result = apiInstance.getFieldItemCollection(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, fieldId, X_API2CRM_DESCRIBE_LIFETIME, pageSize, page, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FieldItemApi#getFieldItemCollection");
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
| **pageSize** | **Integer**| Amount of results (default: 25) | [optional] |
| **page** | **Integer**| Page to show (default: 1) | [optional] |
| **fields** | **String**| Comma-separated list of fields to include in the response | [optional] |

### Return type

[**List&lt;FieldItemEntity&gt;**](FieldItemEntity.md)

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

<a id="getFieldItemCountCollection"></a>
# **getFieldItemCountCollection**
> Count getFieldItemCountCollection(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, fieldId)

COUNT for fieldItem

Count all field items from the system

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FieldItemApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    FieldItemApi apiInstance = new FieldItemApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | User Key
    String X_API2CRM_APPLICATION_KEY = "7ae5b17008fb414d84981191cf3b66a476ef8bef"; // String | Application Key
    String fieldId = "fieldId_example"; // String | Field Identifier
    try {
      Count result = apiInstance.getFieldItemCountCollection(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, fieldId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FieldItemApi#getFieldItemCountCollection");
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

<a id="getFieldItemDescribe"></a>
# **getFieldItemDescribe**
> FieldItemDescribe getFieldItemDescribe(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, fieldId, X_API2CRM_DESCRIBE_LIFETIME)

DESCRIBE for fieldItem

Returns describe for field items

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FieldItemApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    FieldItemApi apiInstance = new FieldItemApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | User Key
    String X_API2CRM_APPLICATION_KEY = "7ae5b17008fb414d84981191cf3b66a476ef8bef"; // String | Application Key
    String fieldId = "fieldId_example"; // String | Field Identifier
    String X_API2CRM_DESCRIBE_LIFETIME = "X_API2CRM_DESCRIBE_LIFETIME_example"; // String | Describe lifetime
    try {
      FieldItemDescribe result = apiInstance.getFieldItemDescribe(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, fieldId, X_API2CRM_DESCRIBE_LIFETIME);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FieldItemApi#getFieldItemDescribe");
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

### Return type

[**FieldItemDescribe**](FieldItemDescribe.md)

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

<a id="getFieldItemEntity"></a>
# **getFieldItemEntity**
> FieldItemEntity getFieldItemEntity(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, fieldId, fieldItemId, X_API2CRM_DESCRIBE_LIFETIME, fields)

GET for fieldItem

Return field item information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FieldItemApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    FieldItemApi apiInstance = new FieldItemApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | User Key
    String X_API2CRM_APPLICATION_KEY = "7ae5b17008fb414d84981191cf3b66a476ef8bef"; // String | Application Key
    String fieldId = "fieldId_example"; // String | Field Identifier
    String fieldItemId = "fieldItemId_example"; // String | Field Item Identifier
    String X_API2CRM_DESCRIBE_LIFETIME = "X_API2CRM_DESCRIBE_LIFETIME_example"; // String | Describe lifetime
    String fields = "fields_example"; // String | Comma-separated list of fields to include in the response
    try {
      FieldItemEntity result = apiInstance.getFieldItemEntity(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, fieldId, fieldItemId, X_API2CRM_DESCRIBE_LIFETIME, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FieldItemApi#getFieldItemEntity");
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
| **fieldItemId** | **String**| Field Item Identifier | |
| **X_API2CRM_DESCRIBE_LIFETIME** | **String**| Describe lifetime | [optional] |
| **fields** | **String**| Comma-separated list of fields to include in the response | [optional] |

### Return type

[**FieldItemEntity**](FieldItemEntity.md)

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

<a id="updateFieldItemEntity"></a>
# **updateFieldItemEntity**
> FieldItemEntityRelation updateFieldItemEntity(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, fieldId, fieldItemId, body, X_API2CRM_DESCRIBE_LIFETIME)

PUT for fieldItem

Update field item information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FieldItemApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    FieldItemApi apiInstance = new FieldItemApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | User Key
    String X_API2CRM_APPLICATION_KEY = "7ae5b17008fb414d84981191cf3b66a476ef8bef"; // String | Application Key
    String fieldId = "fieldId_example"; // String | Field Identifier
    String fieldItemId = "fieldItemId_example"; // String | Field Item Identifier
    FieldItemEntity body = new FieldItemEntity(); // FieldItemEntity | Update field item information
    String X_API2CRM_DESCRIBE_LIFETIME = "X_API2CRM_DESCRIBE_LIFETIME_example"; // String | Describe lifetime
    try {
      FieldItemEntityRelation result = apiInstance.updateFieldItemEntity(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, fieldId, fieldItemId, body, X_API2CRM_DESCRIBE_LIFETIME);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FieldItemApi#updateFieldItemEntity");
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
| **fieldItemId** | **String**| Field Item Identifier | |
| **body** | [**FieldItemEntity**](FieldItemEntity.md)| Update field item information | |
| **X_API2CRM_DESCRIBE_LIFETIME** | **String**| Describe lifetime | [optional] |

### Return type

[**FieldItemEntityRelation**](FieldItemEntityRelation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Client Error |  -  |
| **404** | Not Found |  -  |
| **422** | Unprocessable Entity |  -  |

