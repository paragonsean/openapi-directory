# CallApi

All URIs are relative to *https://api-2445581398133.apicast.io:443/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createCallEntity**](CallApi.md#createCallEntity) | **POST** /application/entity/call | POST for call |
| [**createCallEntityBulk**](CallApi.md#createCallEntityBulk) | **POST** /application/entity/call/bulk | POST bulk  for call |
| [**deleteCallCollectionBulk**](CallApi.md#deleteCallCollectionBulk) | **DELETE** /application/entity/call/bulk | DELETE bulk  for call |
| [**deleteCallEntity**](CallApi.md#deleteCallEntity) | **DELETE** /application/entity/call/{call_id} | DELETE for call |
| [**getCallAggregate**](CallApi.md#getCallAggregate) | **GET** /application/entity/call/aggregate | AGGREGATE for call |
| [**getCallCollection**](CallApi.md#getCallCollection) | **GET** /application/entity/call/list | GET for call |
| [**getCallCountCollection**](CallApi.md#getCallCountCollection) | **GET** /application/entity/call/count | COUNT for call |
| [**getCallDescribe**](CallApi.md#getCallDescribe) | **GET** /application/entity/call/describe | DESCRIBE for call |
| [**getCallEntity**](CallApi.md#getCallEntity) | **GET** /application/entity/call/{call_id} | GET for call |
| [**updateCallEntity**](CallApi.md#updateCallEntity) | **PUT** /application/entity/call/{call_id} | PUT for call |
| [**updateCallEntityBulk**](CallApi.md#updateCallEntityBulk) | **PUT** /application/entity/call/bulk | PUT bulk  for call |


<a id="createCallEntity"></a>
# **createCallEntity**
> CallEntityRelation createCallEntity(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, body, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DESCRIBE_LIFETIME)

POST for call

Add call into the system

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    CallApi apiInstance = new CallApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | User Key
    String X_API2CRM_APPLICATION_KEY = "7ae5b17008fb414d84981191cf3b66a476ef8bef"; // String | Application Key
    CallEntity body = new CallEntity(); // CallEntity | Add call into the system
    String X_API2CRM_NATIVE_ENABLE = "false"; // String | Return native response
    String X_API2CRM_DESCRIBE_LIFETIME = "X_API2CRM_DESCRIBE_LIFETIME_example"; // String | Describe lifetime
    try {
      CallEntityRelation result = apiInstance.createCallEntity(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, body, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DESCRIBE_LIFETIME);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallApi#createCallEntity");
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
| **body** | [**CallEntity**](CallEntity.md)| Add call into the system | |
| **X_API2CRM_NATIVE_ENABLE** | **String**| Return native response | [optional] [enum: false, true] |
| **X_API2CRM_DESCRIBE_LIFETIME** | **String**| Describe lifetime | [optional] |

### Return type

[**CallEntityRelation**](CallEntityRelation.md)

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

<a id="createCallEntityBulk"></a>
# **createCallEntityBulk**
> BulkEntityRelation createCallEntityBulk(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, body, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DESCRIBE_LIFETIME)

POST bulk  for call

Add call into the system

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    CallApi apiInstance = new CallApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | User Key
    String X_API2CRM_APPLICATION_KEY = "7ae5b17008fb414d84981191cf3b66a476ef8bef"; // String | Application Key
    BulkEntity body = new BulkEntity(); // BulkEntity | Add call into the system
    String X_API2CRM_NATIVE_ENABLE = "false"; // String | Return native response
    String X_API2CRM_DESCRIBE_LIFETIME = "X_API2CRM_DESCRIBE_LIFETIME_example"; // String | Describe lifetime
    try {
      BulkEntityRelation result = apiInstance.createCallEntityBulk(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, body, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DESCRIBE_LIFETIME);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallApi#createCallEntityBulk");
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
| **body** | [**BulkEntity**](BulkEntity.md)| Add call into the system | |
| **X_API2CRM_NATIVE_ENABLE** | **String**| Return native response | [optional] [enum: false, true] |
| **X_API2CRM_DESCRIBE_LIFETIME** | **String**| Describe lifetime | [optional] |

### Return type

[**BulkEntityRelation**](BulkEntityRelation.md)

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

<a id="deleteCallCollectionBulk"></a>
# **deleteCallCollectionBulk**
> BulkEntity deleteCallCollectionBulk(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, body)

DELETE bulk  for call

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    CallApi apiInstance = new CallApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | User Key
    String X_API2CRM_APPLICATION_KEY = "7ae5b17008fb414d84981191cf3b66a476ef8bef"; // String | Application Key
    BulkEntity body = new BulkEntity(); // BulkEntity | 
    try {
      BulkEntity result = apiInstance.deleteCallCollectionBulk(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallApi#deleteCallCollectionBulk");
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
| **body** | [**BulkEntity**](BulkEntity.md)|  | |

### Return type

[**BulkEntity**](BulkEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **204** | No Content |  -  |
| **404** | Not Found |  -  |

<a id="deleteCallEntity"></a>
# **deleteCallEntity**
> deleteCallEntity(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, callId)

DELETE for call

Delete call information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    CallApi apiInstance = new CallApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | User Key
    String X_API2CRM_APPLICATION_KEY = "7ae5b17008fb414d84981191cf3b66a476ef8bef"; // String | Application Key
    String callId = "callId_example"; // String | Call Identifier
    try {
      apiInstance.deleteCallEntity(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, callId);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallApi#deleteCallEntity");
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
| **callId** | **String**| Call Identifier | |

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

<a id="getCallAggregate"></a>
# **getCallAggregate**
> Aggregate getCallAggregate(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DATA_ENABLE, X_API2CRM_DATA_BUILD, X_API2CRM_DATA_IS_FINAL, X_API2CRM_DATA_STRATEGY, X_API2CRM_DATA_COHERENT_ENTITIES, X_API2CRM_DATA_ALWAYS_ACTUAL, X_API2CRM_DATA_ACTUAL_AT, X_API2CRM_DESCRIBE_LIFETIME, filter, pipeline)

AGGREGATE for call

Returns aggregate for calls

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    CallApi apiInstance = new CallApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | User Key
    String X_API2CRM_APPLICATION_KEY = "7ae5b17008fb414d84981191cf3b66a476ef8bef"; // String | Application Key
    String X_API2CRM_NATIVE_ENABLE = "false"; // String | Return native response
    String X_API2CRM_DATA_ENABLE = "false"; // String | Data Enable
    String X_API2CRM_DATA_BUILD = "false"; // String | Data Build
    String X_API2CRM_DATA_IS_FINAL = "true"; // String | Data Is Final
    String X_API2CRM_DATA_STRATEGY = "simple"; // String | Data Strategy
    String X_API2CRM_DATA_COHERENT_ENTITIES = "X_API2CRM_DATA_COHERENT_ENTITIES_example"; // String | Coherent Entities
    String X_API2CRM_DATA_ALWAYS_ACTUAL = "true"; // String | Data Is Actual
    OffsetDateTime X_API2CRM_DATA_ACTUAL_AT = OffsetDateTime.now(); // OffsetDateTime | Data Actual At
    String X_API2CRM_DESCRIBE_LIFETIME = "X_API2CRM_DESCRIBE_LIFETIME_example"; // String | Describe lifetime
    String filter = "filter_example"; // String | Filter
    String pipeline = "pipeline_example"; // String | Pipeline
    try {
      Aggregate result = apiInstance.getCallAggregate(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DATA_ENABLE, X_API2CRM_DATA_BUILD, X_API2CRM_DATA_IS_FINAL, X_API2CRM_DATA_STRATEGY, X_API2CRM_DATA_COHERENT_ENTITIES, X_API2CRM_DATA_ALWAYS_ACTUAL, X_API2CRM_DATA_ACTUAL_AT, X_API2CRM_DESCRIBE_LIFETIME, filter, pipeline);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallApi#getCallAggregate");
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
| **X_API2CRM_NATIVE_ENABLE** | **String**| Return native response | [optional] [enum: false, true] |
| **X_API2CRM_DATA_ENABLE** | **String**| Data Enable | [optional] [enum: false, true] |
| **X_API2CRM_DATA_BUILD** | **String**| Data Build | [optional] [enum: false] |
| **X_API2CRM_DATA_IS_FINAL** | **String**| Data Is Final | [optional] [enum: true, false] |
| **X_API2CRM_DATA_STRATEGY** | **String**| Data Strategy | [optional] [enum: simple] |
| **X_API2CRM_DATA_COHERENT_ENTITIES** | **String**| Coherent Entities | [optional] |
| **X_API2CRM_DATA_ALWAYS_ACTUAL** | **String**| Data Is Actual | [optional] [enum: true] |
| **X_API2CRM_DATA_ACTUAL_AT** | **OffsetDateTime**| Data Actual At | [optional] |
| **X_API2CRM_DESCRIBE_LIFETIME** | **String**| Describe lifetime | [optional] |
| **filter** | **String**| Filter | [optional] |
| **pipeline** | **String**| Pipeline | [optional] |

### Return type

[**Aggregate**](Aggregate.md)

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

<a id="getCallCollection"></a>
# **getCallCollection**
> List&lt;CallEntity&gt; getCallCollection(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DATA_ENABLE, X_API2CRM_DATA_BUILD, X_API2CRM_DATA_IS_FINAL, X_API2CRM_DATA_STRATEGY, X_API2CRM_DATA_COHERENT_ENTITIES, X_API2CRM_DATA_ALWAYS_ACTUAL, X_API2CRM_DATA_ACTUAL_AT, X_API2CRM_DESCRIBE_LIFETIME, pageSize, page, filter, expand, fields, sort, unique)

GET for call

Returns all calls from the system

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    CallApi apiInstance = new CallApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | User Key
    String X_API2CRM_APPLICATION_KEY = "7ae5b17008fb414d84981191cf3b66a476ef8bef"; // String | Application Key
    String X_API2CRM_NATIVE_ENABLE = "false"; // String | Return native response
    String X_API2CRM_DATA_ENABLE = "false"; // String | Data Enable
    String X_API2CRM_DATA_BUILD = "false"; // String | Data Build
    String X_API2CRM_DATA_IS_FINAL = "true"; // String | Data Is Final
    String X_API2CRM_DATA_STRATEGY = "simple"; // String | Data Strategy
    String X_API2CRM_DATA_COHERENT_ENTITIES = "X_API2CRM_DATA_COHERENT_ENTITIES_example"; // String | Coherent Entities
    String X_API2CRM_DATA_ALWAYS_ACTUAL = "true"; // String | Data Is Actual
    OffsetDateTime X_API2CRM_DATA_ACTUAL_AT = OffsetDateTime.now(); // OffsetDateTime | Data Actual At
    String X_API2CRM_DESCRIBE_LIFETIME = "X_API2CRM_DESCRIBE_LIFETIME_example"; // String | Describe lifetime
    Integer pageSize = 56; // Integer | Amount of results (default: 25)
    Integer page = 56; // Integer | Page to show (default: 1)
    String filter = "filter_example"; // String | Filter
    String expand = "expand_example"; // String | Expand relations
    String fields = "fields_example"; // String | Comma-separated list of fields to include in the response
    String sort = "sort_example"; // String | Specifies ascending or descending sort on existing fields
    String unique = "false"; // String | Find all unique values for selected field
    try {
      List<CallEntity> result = apiInstance.getCallCollection(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DATA_ENABLE, X_API2CRM_DATA_BUILD, X_API2CRM_DATA_IS_FINAL, X_API2CRM_DATA_STRATEGY, X_API2CRM_DATA_COHERENT_ENTITIES, X_API2CRM_DATA_ALWAYS_ACTUAL, X_API2CRM_DATA_ACTUAL_AT, X_API2CRM_DESCRIBE_LIFETIME, pageSize, page, filter, expand, fields, sort, unique);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallApi#getCallCollection");
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
| **X_API2CRM_NATIVE_ENABLE** | **String**| Return native response | [optional] [enum: false, true] |
| **X_API2CRM_DATA_ENABLE** | **String**| Data Enable | [optional] [enum: false, true] |
| **X_API2CRM_DATA_BUILD** | **String**| Data Build | [optional] [enum: false] |
| **X_API2CRM_DATA_IS_FINAL** | **String**| Data Is Final | [optional] [enum: true, false] |
| **X_API2CRM_DATA_STRATEGY** | **String**| Data Strategy | [optional] [enum: simple] |
| **X_API2CRM_DATA_COHERENT_ENTITIES** | **String**| Coherent Entities | [optional] |
| **X_API2CRM_DATA_ALWAYS_ACTUAL** | **String**| Data Is Actual | [optional] [enum: true] |
| **X_API2CRM_DATA_ACTUAL_AT** | **OffsetDateTime**| Data Actual At | [optional] |
| **X_API2CRM_DESCRIBE_LIFETIME** | **String**| Describe lifetime | [optional] |
| **pageSize** | **Integer**| Amount of results (default: 25) | [optional] |
| **page** | **Integer**| Page to show (default: 1) | [optional] |
| **filter** | **String**| Filter | [optional] |
| **expand** | **String**| Expand relations | [optional] |
| **fields** | **String**| Comma-separated list of fields to include in the response | [optional] |
| **sort** | **String**| Specifies ascending or descending sort on existing fields | [optional] |
| **unique** | **String**| Find all unique values for selected field | [optional] [enum: false, true] |

### Return type

[**List&lt;CallEntity&gt;**](CallEntity.md)

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

<a id="getCallCountCollection"></a>
# **getCallCountCollection**
> Count getCallCountCollection(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, X_API2CRM_DATA_ENABLE, X_API2CRM_DATA_BUILD, X_API2CRM_DATA_IS_FINAL, X_API2CRM_DATA_STRATEGY, X_API2CRM_DATA_COHERENT_ENTITIES, X_API2CRM_DATA_ALWAYS_ACTUAL, X_API2CRM_DATA_ACTUAL_AT, filter)

COUNT for call

Count all calls from the system

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    CallApi apiInstance = new CallApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | User Key
    String X_API2CRM_APPLICATION_KEY = "7ae5b17008fb414d84981191cf3b66a476ef8bef"; // String | Application Key
    String X_API2CRM_DATA_ENABLE = "false"; // String | Data Enable
    String X_API2CRM_DATA_BUILD = "false"; // String | Data Build
    String X_API2CRM_DATA_IS_FINAL = "true"; // String | Data Is Final
    String X_API2CRM_DATA_STRATEGY = "simple"; // String | Data Strategy
    String X_API2CRM_DATA_COHERENT_ENTITIES = "X_API2CRM_DATA_COHERENT_ENTITIES_example"; // String | Coherent Entities
    String X_API2CRM_DATA_ALWAYS_ACTUAL = "true"; // String | Data Is Actual
    OffsetDateTime X_API2CRM_DATA_ACTUAL_AT = OffsetDateTime.now(); // OffsetDateTime | Data Actual At
    String filter = "filter_example"; // String | Filter
    try {
      Count result = apiInstance.getCallCountCollection(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, X_API2CRM_DATA_ENABLE, X_API2CRM_DATA_BUILD, X_API2CRM_DATA_IS_FINAL, X_API2CRM_DATA_STRATEGY, X_API2CRM_DATA_COHERENT_ENTITIES, X_API2CRM_DATA_ALWAYS_ACTUAL, X_API2CRM_DATA_ACTUAL_AT, filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallApi#getCallCountCollection");
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
| **X_API2CRM_DATA_ENABLE** | **String**| Data Enable | [optional] [enum: false, true] |
| **X_API2CRM_DATA_BUILD** | **String**| Data Build | [optional] [enum: false] |
| **X_API2CRM_DATA_IS_FINAL** | **String**| Data Is Final | [optional] [enum: true, false] |
| **X_API2CRM_DATA_STRATEGY** | **String**| Data Strategy | [optional] [enum: simple] |
| **X_API2CRM_DATA_COHERENT_ENTITIES** | **String**| Coherent Entities | [optional] |
| **X_API2CRM_DATA_ALWAYS_ACTUAL** | **String**| Data Is Actual | [optional] [enum: true] |
| **X_API2CRM_DATA_ACTUAL_AT** | **OffsetDateTime**| Data Actual At | [optional] |
| **filter** | **String**| Filter | [optional] |

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

<a id="getCallDescribe"></a>
# **getCallDescribe**
> CallDescribe getCallDescribe(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, X_API2CRM_DATA_ENABLE, X_API2CRM_DATA_BUILD, X_API2CRM_DATA_IS_FINAL, X_API2CRM_DATA_STRATEGY, X_API2CRM_DATA_COHERENT_ENTITIES, X_API2CRM_DATA_ALWAYS_ACTUAL, X_API2CRM_DATA_ACTUAL_AT, X_API2CRM_DESCRIBE_LIFETIME)

DESCRIBE for call

Returns describe for calls

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    CallApi apiInstance = new CallApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | User Key
    String X_API2CRM_APPLICATION_KEY = "7ae5b17008fb414d84981191cf3b66a476ef8bef"; // String | Application Key
    String X_API2CRM_DATA_ENABLE = "false"; // String | Data Enable
    String X_API2CRM_DATA_BUILD = "false"; // String | Data Build
    String X_API2CRM_DATA_IS_FINAL = "true"; // String | Data Is Final
    String X_API2CRM_DATA_STRATEGY = "simple"; // String | Data Strategy
    String X_API2CRM_DATA_COHERENT_ENTITIES = "X_API2CRM_DATA_COHERENT_ENTITIES_example"; // String | Coherent Entities
    String X_API2CRM_DATA_ALWAYS_ACTUAL = "true"; // String | Data Is Actual
    OffsetDateTime X_API2CRM_DATA_ACTUAL_AT = OffsetDateTime.now(); // OffsetDateTime | Data Actual At
    String X_API2CRM_DESCRIBE_LIFETIME = "X_API2CRM_DESCRIBE_LIFETIME_example"; // String | Describe lifetime
    try {
      CallDescribe result = apiInstance.getCallDescribe(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, X_API2CRM_DATA_ENABLE, X_API2CRM_DATA_BUILD, X_API2CRM_DATA_IS_FINAL, X_API2CRM_DATA_STRATEGY, X_API2CRM_DATA_COHERENT_ENTITIES, X_API2CRM_DATA_ALWAYS_ACTUAL, X_API2CRM_DATA_ACTUAL_AT, X_API2CRM_DESCRIBE_LIFETIME);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallApi#getCallDescribe");
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
| **X_API2CRM_DATA_ENABLE** | **String**| Data Enable | [optional] [enum: false, true] |
| **X_API2CRM_DATA_BUILD** | **String**| Data Build | [optional] [enum: false] |
| **X_API2CRM_DATA_IS_FINAL** | **String**| Data Is Final | [optional] [enum: true, false] |
| **X_API2CRM_DATA_STRATEGY** | **String**| Data Strategy | [optional] [enum: simple] |
| **X_API2CRM_DATA_COHERENT_ENTITIES** | **String**| Coherent Entities | [optional] |
| **X_API2CRM_DATA_ALWAYS_ACTUAL** | **String**| Data Is Actual | [optional] [enum: true] |
| **X_API2CRM_DATA_ACTUAL_AT** | **OffsetDateTime**| Data Actual At | [optional] |
| **X_API2CRM_DESCRIBE_LIFETIME** | **String**| Describe lifetime | [optional] |

### Return type

[**CallDescribe**](CallDescribe.md)

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

<a id="getCallEntity"></a>
# **getCallEntity**
> CallEntity getCallEntity(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, callId, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DATA_ENABLE, X_API2CRM_DATA_BUILD, X_API2CRM_DATA_IS_FINAL, X_API2CRM_DATA_STRATEGY, X_API2CRM_DATA_COHERENT_ENTITIES, X_API2CRM_DATA_ALWAYS_ACTUAL, X_API2CRM_DATA_ACTUAL_AT, X_API2CRM_DESCRIBE_LIFETIME, expand, fields)

GET for call

Return call information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    CallApi apiInstance = new CallApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | User Key
    String X_API2CRM_APPLICATION_KEY = "7ae5b17008fb414d84981191cf3b66a476ef8bef"; // String | Application Key
    String callId = "callId_example"; // String | Call Identifier
    String X_API2CRM_NATIVE_ENABLE = "false"; // String | Return native response
    String X_API2CRM_DATA_ENABLE = "false"; // String | Data Enable
    String X_API2CRM_DATA_BUILD = "false"; // String | Data Build
    String X_API2CRM_DATA_IS_FINAL = "true"; // String | Data Is Final
    String X_API2CRM_DATA_STRATEGY = "simple"; // String | Data Strategy
    String X_API2CRM_DATA_COHERENT_ENTITIES = "X_API2CRM_DATA_COHERENT_ENTITIES_example"; // String | Coherent Entities
    String X_API2CRM_DATA_ALWAYS_ACTUAL = "true"; // String | Data Is Actual
    OffsetDateTime X_API2CRM_DATA_ACTUAL_AT = OffsetDateTime.now(); // OffsetDateTime | Data Actual At
    String X_API2CRM_DESCRIBE_LIFETIME = "X_API2CRM_DESCRIBE_LIFETIME_example"; // String | Describe lifetime
    String expand = "expand_example"; // String | Expand relations
    String fields = "fields_example"; // String | Comma-separated list of fields to include in the response
    try {
      CallEntity result = apiInstance.getCallEntity(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, callId, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DATA_ENABLE, X_API2CRM_DATA_BUILD, X_API2CRM_DATA_IS_FINAL, X_API2CRM_DATA_STRATEGY, X_API2CRM_DATA_COHERENT_ENTITIES, X_API2CRM_DATA_ALWAYS_ACTUAL, X_API2CRM_DATA_ACTUAL_AT, X_API2CRM_DESCRIBE_LIFETIME, expand, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallApi#getCallEntity");
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
| **callId** | **String**| Call Identifier | |
| **X_API2CRM_NATIVE_ENABLE** | **String**| Return native response | [optional] [enum: false, true] |
| **X_API2CRM_DATA_ENABLE** | **String**| Data Enable | [optional] [enum: false, true] |
| **X_API2CRM_DATA_BUILD** | **String**| Data Build | [optional] [enum: false] |
| **X_API2CRM_DATA_IS_FINAL** | **String**| Data Is Final | [optional] [enum: true, false] |
| **X_API2CRM_DATA_STRATEGY** | **String**| Data Strategy | [optional] [enum: simple] |
| **X_API2CRM_DATA_COHERENT_ENTITIES** | **String**| Coherent Entities | [optional] |
| **X_API2CRM_DATA_ALWAYS_ACTUAL** | **String**| Data Is Actual | [optional] [enum: true] |
| **X_API2CRM_DATA_ACTUAL_AT** | **OffsetDateTime**| Data Actual At | [optional] |
| **X_API2CRM_DESCRIBE_LIFETIME** | **String**| Describe lifetime | [optional] |
| **expand** | **String**| Expand relations | [optional] |
| **fields** | **String**| Comma-separated list of fields to include in the response | [optional] |

### Return type

[**CallEntity**](CallEntity.md)

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

<a id="updateCallEntity"></a>
# **updateCallEntity**
> CallEntityRelation updateCallEntity(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, callId, body, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DESCRIBE_LIFETIME)

PUT for call

Update call information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    CallApi apiInstance = new CallApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | User Key
    String X_API2CRM_APPLICATION_KEY = "7ae5b17008fb414d84981191cf3b66a476ef8bef"; // String | Application Key
    String callId = "callId_example"; // String | Call Identifier
    CallEntity body = new CallEntity(); // CallEntity | Update call information
    String X_API2CRM_NATIVE_ENABLE = "false"; // String | Return native response
    String X_API2CRM_DESCRIBE_LIFETIME = "X_API2CRM_DESCRIBE_LIFETIME_example"; // String | Describe lifetime
    try {
      CallEntityRelation result = apiInstance.updateCallEntity(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, callId, body, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DESCRIBE_LIFETIME);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallApi#updateCallEntity");
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
| **callId** | **String**| Call Identifier | |
| **body** | [**CallEntity**](CallEntity.md)| Update call information | |
| **X_API2CRM_NATIVE_ENABLE** | **String**| Return native response | [optional] [enum: false, true] |
| **X_API2CRM_DESCRIBE_LIFETIME** | **String**| Describe lifetime | [optional] |

### Return type

[**CallEntityRelation**](CallEntityRelation.md)

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

<a id="updateCallEntityBulk"></a>
# **updateCallEntityBulk**
> BulkEntityRelation updateCallEntityBulk(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, body, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DESCRIBE_LIFETIME)

PUT bulk  for call

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    CallApi apiInstance = new CallApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | User Key
    String X_API2CRM_APPLICATION_KEY = "7ae5b17008fb414d84981191cf3b66a476ef8bef"; // String | Application Key
    BulkEntity body = new BulkEntity(); // BulkEntity | 
    String X_API2CRM_NATIVE_ENABLE = "false"; // String | Return native response
    String X_API2CRM_DESCRIBE_LIFETIME = "X_API2CRM_DESCRIBE_LIFETIME_example"; // String | Describe lifetime
    try {
      BulkEntityRelation result = apiInstance.updateCallEntityBulk(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, body, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DESCRIBE_LIFETIME);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallApi#updateCallEntityBulk");
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
| **body** | [**BulkEntity**](BulkEntity.md)|  | |
| **X_API2CRM_NATIVE_ENABLE** | **String**| Return native response | [optional] [enum: false, true] |
| **X_API2CRM_DESCRIBE_LIFETIME** | **String**| Describe lifetime | [optional] |

### Return type

[**BulkEntityRelation**](BulkEntityRelation.md)

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

