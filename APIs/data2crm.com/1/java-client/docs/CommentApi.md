# CommentApi

All URIs are relative to *https://api-2445581398133.apicast.io:443/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createCommentEntity**](CommentApi.md#createCommentEntity) | **POST** /application/entity/comment | POST for comment |
| [**createCommentEntityBulk**](CommentApi.md#createCommentEntityBulk) | **POST** /application/entity/comment/bulk | POST bulk  for comment |
| [**deleteCommentCollectionBulk**](CommentApi.md#deleteCommentCollectionBulk) | **DELETE** /application/entity/comment/bulk | DELETE bulk  for comment |
| [**deleteCommentEntity**](CommentApi.md#deleteCommentEntity) | **DELETE** /application/entity/comment/{comment_id} | DELETE for comment |
| [**getCommentAggregate**](CommentApi.md#getCommentAggregate) | **GET** /application/entity/comment/aggregate | AGGREGATE for comment |
| [**getCommentCollection**](CommentApi.md#getCommentCollection) | **GET** /application/entity/comment/list | GET for comment |
| [**getCommentCountCollection**](CommentApi.md#getCommentCountCollection) | **GET** /application/entity/comment/count | COUNT for comment |
| [**getCommentDescribe**](CommentApi.md#getCommentDescribe) | **GET** /application/entity/comment/describe | DESCRIBE for comment |
| [**getCommentEntity**](CommentApi.md#getCommentEntity) | **GET** /application/entity/comment/{comment_id} | GET for comment |
| [**updateCommentEntity**](CommentApi.md#updateCommentEntity) | **PUT** /application/entity/comment/{comment_id} | PUT for comment |
| [**updateCommentEntityBulk**](CommentApi.md#updateCommentEntityBulk) | **PUT** /application/entity/comment/bulk | PUT bulk  for comment |


<a id="createCommentEntity"></a>
# **createCommentEntity**
> CommentEntityRelation createCommentEntity(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, body, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DESCRIBE_LIFETIME)

POST for comment

Add comment into the system

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    CommentApi apiInstance = new CommentApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | User Key
    String X_API2CRM_APPLICATION_KEY = "7ae5b17008fb414d84981191cf3b66a476ef8bef"; // String | Application Key
    CommentEntity body = new CommentEntity(); // CommentEntity | Add comment into the system
    String X_API2CRM_NATIVE_ENABLE = "false"; // String | Return native response
    String X_API2CRM_DESCRIBE_LIFETIME = "X_API2CRM_DESCRIBE_LIFETIME_example"; // String | Describe lifetime
    try {
      CommentEntityRelation result = apiInstance.createCommentEntity(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, body, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DESCRIBE_LIFETIME);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommentApi#createCommentEntity");
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
| **body** | [**CommentEntity**](CommentEntity.md)| Add comment into the system | |
| **X_API2CRM_NATIVE_ENABLE** | **String**| Return native response | [optional] [enum: false, true] |
| **X_API2CRM_DESCRIBE_LIFETIME** | **String**| Describe lifetime | [optional] |

### Return type

[**CommentEntityRelation**](CommentEntityRelation.md)

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

<a id="createCommentEntityBulk"></a>
# **createCommentEntityBulk**
> BulkEntityRelation createCommentEntityBulk(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, body, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DESCRIBE_LIFETIME)

POST bulk  for comment

Add comment into the system

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    CommentApi apiInstance = new CommentApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | User Key
    String X_API2CRM_APPLICATION_KEY = "7ae5b17008fb414d84981191cf3b66a476ef8bef"; // String | Application Key
    BulkEntity body = new BulkEntity(); // BulkEntity | Add comment into the system
    String X_API2CRM_NATIVE_ENABLE = "false"; // String | Return native response
    String X_API2CRM_DESCRIBE_LIFETIME = "X_API2CRM_DESCRIBE_LIFETIME_example"; // String | Describe lifetime
    try {
      BulkEntityRelation result = apiInstance.createCommentEntityBulk(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, body, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DESCRIBE_LIFETIME);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommentApi#createCommentEntityBulk");
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
| **body** | [**BulkEntity**](BulkEntity.md)| Add comment into the system | |
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

<a id="deleteCommentCollectionBulk"></a>
# **deleteCommentCollectionBulk**
> BulkEntity deleteCommentCollectionBulk(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, body)

DELETE bulk  for comment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    CommentApi apiInstance = new CommentApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | User Key
    String X_API2CRM_APPLICATION_KEY = "7ae5b17008fb414d84981191cf3b66a476ef8bef"; // String | Application Key
    BulkEntity body = new BulkEntity(); // BulkEntity | 
    try {
      BulkEntity result = apiInstance.deleteCommentCollectionBulk(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommentApi#deleteCommentCollectionBulk");
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

<a id="deleteCommentEntity"></a>
# **deleteCommentEntity**
> deleteCommentEntity(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, commentId)

DELETE for comment

Delete comment information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    CommentApi apiInstance = new CommentApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | User Key
    String X_API2CRM_APPLICATION_KEY = "7ae5b17008fb414d84981191cf3b66a476ef8bef"; // String | Application Key
    String commentId = "commentId_example"; // String | Comment Identifier
    try {
      apiInstance.deleteCommentEntity(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, commentId);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommentApi#deleteCommentEntity");
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
| **commentId** | **String**| Comment Identifier | |

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

<a id="getCommentAggregate"></a>
# **getCommentAggregate**
> Aggregate getCommentAggregate(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DATA_ENABLE, X_API2CRM_DATA_BUILD, X_API2CRM_DATA_IS_FINAL, X_API2CRM_DATA_STRATEGY, X_API2CRM_DATA_COHERENT_ENTITIES, X_API2CRM_DATA_ALWAYS_ACTUAL, X_API2CRM_DATA_ACTUAL_AT, X_API2CRM_DESCRIBE_LIFETIME, filter, pipeline)

AGGREGATE for comment

Returns aggregate for comments

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    CommentApi apiInstance = new CommentApi(defaultClient);
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
      Aggregate result = apiInstance.getCommentAggregate(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DATA_ENABLE, X_API2CRM_DATA_BUILD, X_API2CRM_DATA_IS_FINAL, X_API2CRM_DATA_STRATEGY, X_API2CRM_DATA_COHERENT_ENTITIES, X_API2CRM_DATA_ALWAYS_ACTUAL, X_API2CRM_DATA_ACTUAL_AT, X_API2CRM_DESCRIBE_LIFETIME, filter, pipeline);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommentApi#getCommentAggregate");
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

<a id="getCommentCollection"></a>
# **getCommentCollection**
> List&lt;CommentEntity&gt; getCommentCollection(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DATA_ENABLE, X_API2CRM_DATA_BUILD, X_API2CRM_DATA_IS_FINAL, X_API2CRM_DATA_STRATEGY, X_API2CRM_DATA_COHERENT_ENTITIES, X_API2CRM_DATA_ALWAYS_ACTUAL, X_API2CRM_DATA_ACTUAL_AT, X_API2CRM_DESCRIBE_LIFETIME, pageSize, page, filter, expand, fields, sort, unique)

GET for comment

Returns all comments from the system

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    CommentApi apiInstance = new CommentApi(defaultClient);
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
      List<CommentEntity> result = apiInstance.getCommentCollection(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DATA_ENABLE, X_API2CRM_DATA_BUILD, X_API2CRM_DATA_IS_FINAL, X_API2CRM_DATA_STRATEGY, X_API2CRM_DATA_COHERENT_ENTITIES, X_API2CRM_DATA_ALWAYS_ACTUAL, X_API2CRM_DATA_ACTUAL_AT, X_API2CRM_DESCRIBE_LIFETIME, pageSize, page, filter, expand, fields, sort, unique);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommentApi#getCommentCollection");
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

[**List&lt;CommentEntity&gt;**](CommentEntity.md)

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

<a id="getCommentCountCollection"></a>
# **getCommentCountCollection**
> Count getCommentCountCollection(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, X_API2CRM_DATA_ENABLE, X_API2CRM_DATA_BUILD, X_API2CRM_DATA_IS_FINAL, X_API2CRM_DATA_STRATEGY, X_API2CRM_DATA_COHERENT_ENTITIES, X_API2CRM_DATA_ALWAYS_ACTUAL, X_API2CRM_DATA_ACTUAL_AT, filter)

COUNT for comment

Count all comments from the system

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    CommentApi apiInstance = new CommentApi(defaultClient);
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
      Count result = apiInstance.getCommentCountCollection(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, X_API2CRM_DATA_ENABLE, X_API2CRM_DATA_BUILD, X_API2CRM_DATA_IS_FINAL, X_API2CRM_DATA_STRATEGY, X_API2CRM_DATA_COHERENT_ENTITIES, X_API2CRM_DATA_ALWAYS_ACTUAL, X_API2CRM_DATA_ACTUAL_AT, filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommentApi#getCommentCountCollection");
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

<a id="getCommentDescribe"></a>
# **getCommentDescribe**
> CommentDescribe getCommentDescribe(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, X_API2CRM_DATA_ENABLE, X_API2CRM_DATA_BUILD, X_API2CRM_DATA_IS_FINAL, X_API2CRM_DATA_STRATEGY, X_API2CRM_DATA_COHERENT_ENTITIES, X_API2CRM_DATA_ALWAYS_ACTUAL, X_API2CRM_DATA_ACTUAL_AT, X_API2CRM_DESCRIBE_LIFETIME)

DESCRIBE for comment

Returns describe for comments

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    CommentApi apiInstance = new CommentApi(defaultClient);
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
      CommentDescribe result = apiInstance.getCommentDescribe(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, X_API2CRM_DATA_ENABLE, X_API2CRM_DATA_BUILD, X_API2CRM_DATA_IS_FINAL, X_API2CRM_DATA_STRATEGY, X_API2CRM_DATA_COHERENT_ENTITIES, X_API2CRM_DATA_ALWAYS_ACTUAL, X_API2CRM_DATA_ACTUAL_AT, X_API2CRM_DESCRIBE_LIFETIME);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommentApi#getCommentDescribe");
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

[**CommentDescribe**](CommentDescribe.md)

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

<a id="getCommentEntity"></a>
# **getCommentEntity**
> CommentEntity getCommentEntity(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, commentId, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DATA_ENABLE, X_API2CRM_DATA_BUILD, X_API2CRM_DATA_IS_FINAL, X_API2CRM_DATA_STRATEGY, X_API2CRM_DATA_COHERENT_ENTITIES, X_API2CRM_DATA_ALWAYS_ACTUAL, X_API2CRM_DATA_ACTUAL_AT, X_API2CRM_DESCRIBE_LIFETIME, expand, fields)

GET for comment

Return comment information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    CommentApi apiInstance = new CommentApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | User Key
    String X_API2CRM_APPLICATION_KEY = "7ae5b17008fb414d84981191cf3b66a476ef8bef"; // String | Application Key
    String commentId = "commentId_example"; // String | Comment Identifier
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
      CommentEntity result = apiInstance.getCommentEntity(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, commentId, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DATA_ENABLE, X_API2CRM_DATA_BUILD, X_API2CRM_DATA_IS_FINAL, X_API2CRM_DATA_STRATEGY, X_API2CRM_DATA_COHERENT_ENTITIES, X_API2CRM_DATA_ALWAYS_ACTUAL, X_API2CRM_DATA_ACTUAL_AT, X_API2CRM_DESCRIBE_LIFETIME, expand, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommentApi#getCommentEntity");
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
| **commentId** | **String**| Comment Identifier | |
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

[**CommentEntity**](CommentEntity.md)

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

<a id="updateCommentEntity"></a>
# **updateCommentEntity**
> CommentEntityRelation updateCommentEntity(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, commentId, body, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DESCRIBE_LIFETIME)

PUT for comment

Update comment information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    CommentApi apiInstance = new CommentApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | User Key
    String X_API2CRM_APPLICATION_KEY = "7ae5b17008fb414d84981191cf3b66a476ef8bef"; // String | Application Key
    String commentId = "commentId_example"; // String | Comment Identifier
    CommentEntity body = new CommentEntity(); // CommentEntity | Update comment information
    String X_API2CRM_NATIVE_ENABLE = "false"; // String | Return native response
    String X_API2CRM_DESCRIBE_LIFETIME = "X_API2CRM_DESCRIBE_LIFETIME_example"; // String | Describe lifetime
    try {
      CommentEntityRelation result = apiInstance.updateCommentEntity(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, commentId, body, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DESCRIBE_LIFETIME);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommentApi#updateCommentEntity");
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
| **commentId** | **String**| Comment Identifier | |
| **body** | [**CommentEntity**](CommentEntity.md)| Update comment information | |
| **X_API2CRM_NATIVE_ENABLE** | **String**| Return native response | [optional] [enum: false, true] |
| **X_API2CRM_DESCRIBE_LIFETIME** | **String**| Describe lifetime | [optional] |

### Return type

[**CommentEntityRelation**](CommentEntityRelation.md)

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

<a id="updateCommentEntityBulk"></a>
# **updateCommentEntityBulk**
> BulkEntityRelation updateCommentEntityBulk(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, body, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DESCRIBE_LIFETIME)

PUT bulk  for comment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    CommentApi apiInstance = new CommentApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | User Key
    String X_API2CRM_APPLICATION_KEY = "7ae5b17008fb414d84981191cf3b66a476ef8bef"; // String | Application Key
    BulkEntity body = new BulkEntity(); // BulkEntity | 
    String X_API2CRM_NATIVE_ENABLE = "false"; // String | Return native response
    String X_API2CRM_DESCRIBE_LIFETIME = "X_API2CRM_DESCRIBE_LIFETIME_example"; // String | Describe lifetime
    try {
      BulkEntityRelation result = apiInstance.updateCommentEntityBulk(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, body, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DESCRIBE_LIFETIME);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommentApi#updateCommentEntityBulk");
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

