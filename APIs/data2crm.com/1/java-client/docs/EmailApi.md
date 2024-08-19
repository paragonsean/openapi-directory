# EmailApi

All URIs are relative to *https://api-2445581398133.apicast.io:443/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createEmailEntity**](EmailApi.md#createEmailEntity) | **POST** /application/entity/email | POST for email |
| [**createEmailEntityBulk**](EmailApi.md#createEmailEntityBulk) | **POST** /application/entity/email/bulk | POST bulk  for email |
| [**deleteEmailCollectionBulk**](EmailApi.md#deleteEmailCollectionBulk) | **DELETE** /application/entity/email/bulk | DELETE bulk  for email |
| [**deleteEmailEntity**](EmailApi.md#deleteEmailEntity) | **DELETE** /application/entity/email/{email_id} | DELETE for email |
| [**getEmailAggregate**](EmailApi.md#getEmailAggregate) | **GET** /application/entity/email/aggregate | AGGREGATE for email |
| [**getEmailCollection**](EmailApi.md#getEmailCollection) | **GET** /application/entity/email/list | GET for email |
| [**getEmailCountCollection**](EmailApi.md#getEmailCountCollection) | **GET** /application/entity/email/count | COUNT for email |
| [**getEmailDescribe**](EmailApi.md#getEmailDescribe) | **GET** /application/entity/email/describe | DESCRIBE for email |
| [**getEmailEntity**](EmailApi.md#getEmailEntity) | **GET** /application/entity/email/{email_id} | GET for email |
| [**updateEmailEntity**](EmailApi.md#updateEmailEntity) | **PUT** /application/entity/email/{email_id} | PUT for email |
| [**updateEmailEntityBulk**](EmailApi.md#updateEmailEntityBulk) | **PUT** /application/entity/email/bulk | PUT bulk  for email |


<a id="createEmailEntity"></a>
# **createEmailEntity**
> EmailEntityRelation createEmailEntity(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, body, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DESCRIBE_LIFETIME)

POST for email

Add email into the system

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmailApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    EmailApi apiInstance = new EmailApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | User Key
    String X_API2CRM_APPLICATION_KEY = "7ae5b17008fb414d84981191cf3b66a476ef8bef"; // String | Application Key
    EmailEntity body = new EmailEntity(); // EmailEntity | Add email into the system
    String X_API2CRM_NATIVE_ENABLE = "false"; // String | Return native response
    String X_API2CRM_DESCRIBE_LIFETIME = "X_API2CRM_DESCRIBE_LIFETIME_example"; // String | Describe lifetime
    try {
      EmailEntityRelation result = apiInstance.createEmailEntity(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, body, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DESCRIBE_LIFETIME);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmailApi#createEmailEntity");
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
| **body** | [**EmailEntity**](EmailEntity.md)| Add email into the system | |
| **X_API2CRM_NATIVE_ENABLE** | **String**| Return native response | [optional] [enum: false, true] |
| **X_API2CRM_DESCRIBE_LIFETIME** | **String**| Describe lifetime | [optional] |

### Return type

[**EmailEntityRelation**](EmailEntityRelation.md)

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

<a id="createEmailEntityBulk"></a>
# **createEmailEntityBulk**
> BulkEntityRelation createEmailEntityBulk(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, body, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DESCRIBE_LIFETIME)

POST bulk  for email

Add email into the system

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmailApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    EmailApi apiInstance = new EmailApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | User Key
    String X_API2CRM_APPLICATION_KEY = "7ae5b17008fb414d84981191cf3b66a476ef8bef"; // String | Application Key
    BulkEntity body = new BulkEntity(); // BulkEntity | Add email into the system
    String X_API2CRM_NATIVE_ENABLE = "false"; // String | Return native response
    String X_API2CRM_DESCRIBE_LIFETIME = "X_API2CRM_DESCRIBE_LIFETIME_example"; // String | Describe lifetime
    try {
      BulkEntityRelation result = apiInstance.createEmailEntityBulk(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, body, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DESCRIBE_LIFETIME);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmailApi#createEmailEntityBulk");
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
| **body** | [**BulkEntity**](BulkEntity.md)| Add email into the system | |
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

<a id="deleteEmailCollectionBulk"></a>
# **deleteEmailCollectionBulk**
> BulkEntity deleteEmailCollectionBulk(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, body)

DELETE bulk  for email

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmailApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    EmailApi apiInstance = new EmailApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | User Key
    String X_API2CRM_APPLICATION_KEY = "7ae5b17008fb414d84981191cf3b66a476ef8bef"; // String | Application Key
    BulkEntity body = new BulkEntity(); // BulkEntity | 
    try {
      BulkEntity result = apiInstance.deleteEmailCollectionBulk(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmailApi#deleteEmailCollectionBulk");
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

<a id="deleteEmailEntity"></a>
# **deleteEmailEntity**
> deleteEmailEntity(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, emailId)

DELETE for email

Delete email information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmailApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    EmailApi apiInstance = new EmailApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | User Key
    String X_API2CRM_APPLICATION_KEY = "7ae5b17008fb414d84981191cf3b66a476ef8bef"; // String | Application Key
    String emailId = "emailId_example"; // String | Email Identifier
    try {
      apiInstance.deleteEmailEntity(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, emailId);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmailApi#deleteEmailEntity");
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
| **emailId** | **String**| Email Identifier | |

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

<a id="getEmailAggregate"></a>
# **getEmailAggregate**
> Aggregate getEmailAggregate(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DATA_ENABLE, X_API2CRM_DATA_BUILD, X_API2CRM_DATA_IS_FINAL, X_API2CRM_DATA_STRATEGY, X_API2CRM_DATA_COHERENT_ENTITIES, X_API2CRM_DATA_ALWAYS_ACTUAL, X_API2CRM_DATA_ACTUAL_AT, X_API2CRM_DESCRIBE_LIFETIME, filter, pipeline)

AGGREGATE for email

Returns aggregate for emails

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmailApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    EmailApi apiInstance = new EmailApi(defaultClient);
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
      Aggregate result = apiInstance.getEmailAggregate(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DATA_ENABLE, X_API2CRM_DATA_BUILD, X_API2CRM_DATA_IS_FINAL, X_API2CRM_DATA_STRATEGY, X_API2CRM_DATA_COHERENT_ENTITIES, X_API2CRM_DATA_ALWAYS_ACTUAL, X_API2CRM_DATA_ACTUAL_AT, X_API2CRM_DESCRIBE_LIFETIME, filter, pipeline);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmailApi#getEmailAggregate");
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

<a id="getEmailCollection"></a>
# **getEmailCollection**
> List&lt;EmailEntity&gt; getEmailCollection(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DATA_ENABLE, X_API2CRM_DATA_BUILD, X_API2CRM_DATA_IS_FINAL, X_API2CRM_DATA_STRATEGY, X_API2CRM_DATA_COHERENT_ENTITIES, X_API2CRM_DATA_ALWAYS_ACTUAL, X_API2CRM_DATA_ACTUAL_AT, X_API2CRM_DESCRIBE_LIFETIME, pageSize, page, filter, expand, fields, sort, unique)

GET for email

Returns all emails from the system

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmailApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    EmailApi apiInstance = new EmailApi(defaultClient);
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
      List<EmailEntity> result = apiInstance.getEmailCollection(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DATA_ENABLE, X_API2CRM_DATA_BUILD, X_API2CRM_DATA_IS_FINAL, X_API2CRM_DATA_STRATEGY, X_API2CRM_DATA_COHERENT_ENTITIES, X_API2CRM_DATA_ALWAYS_ACTUAL, X_API2CRM_DATA_ACTUAL_AT, X_API2CRM_DESCRIBE_LIFETIME, pageSize, page, filter, expand, fields, sort, unique);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmailApi#getEmailCollection");
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

[**List&lt;EmailEntity&gt;**](EmailEntity.md)

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

<a id="getEmailCountCollection"></a>
# **getEmailCountCollection**
> Count getEmailCountCollection(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, X_API2CRM_DATA_ENABLE, X_API2CRM_DATA_BUILD, X_API2CRM_DATA_IS_FINAL, X_API2CRM_DATA_STRATEGY, X_API2CRM_DATA_COHERENT_ENTITIES, X_API2CRM_DATA_ALWAYS_ACTUAL, X_API2CRM_DATA_ACTUAL_AT, filter)

COUNT for email

Count all emails from the system

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmailApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    EmailApi apiInstance = new EmailApi(defaultClient);
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
      Count result = apiInstance.getEmailCountCollection(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, X_API2CRM_DATA_ENABLE, X_API2CRM_DATA_BUILD, X_API2CRM_DATA_IS_FINAL, X_API2CRM_DATA_STRATEGY, X_API2CRM_DATA_COHERENT_ENTITIES, X_API2CRM_DATA_ALWAYS_ACTUAL, X_API2CRM_DATA_ACTUAL_AT, filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmailApi#getEmailCountCollection");
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

<a id="getEmailDescribe"></a>
# **getEmailDescribe**
> EmailDescribe getEmailDescribe(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, X_API2CRM_DATA_ENABLE, X_API2CRM_DATA_BUILD, X_API2CRM_DATA_IS_FINAL, X_API2CRM_DATA_STRATEGY, X_API2CRM_DATA_COHERENT_ENTITIES, X_API2CRM_DATA_ALWAYS_ACTUAL, X_API2CRM_DATA_ACTUAL_AT, X_API2CRM_DESCRIBE_LIFETIME)

DESCRIBE for email

Returns describe for emails

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmailApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    EmailApi apiInstance = new EmailApi(defaultClient);
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
      EmailDescribe result = apiInstance.getEmailDescribe(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, X_API2CRM_DATA_ENABLE, X_API2CRM_DATA_BUILD, X_API2CRM_DATA_IS_FINAL, X_API2CRM_DATA_STRATEGY, X_API2CRM_DATA_COHERENT_ENTITIES, X_API2CRM_DATA_ALWAYS_ACTUAL, X_API2CRM_DATA_ACTUAL_AT, X_API2CRM_DESCRIBE_LIFETIME);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmailApi#getEmailDescribe");
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

[**EmailDescribe**](EmailDescribe.md)

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

<a id="getEmailEntity"></a>
# **getEmailEntity**
> EmailEntity getEmailEntity(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, emailId, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DATA_ENABLE, X_API2CRM_DATA_BUILD, X_API2CRM_DATA_IS_FINAL, X_API2CRM_DATA_STRATEGY, X_API2CRM_DATA_COHERENT_ENTITIES, X_API2CRM_DATA_ALWAYS_ACTUAL, X_API2CRM_DATA_ACTUAL_AT, X_API2CRM_DESCRIBE_LIFETIME, expand, fields)

GET for email

Return email information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmailApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    EmailApi apiInstance = new EmailApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | User Key
    String X_API2CRM_APPLICATION_KEY = "7ae5b17008fb414d84981191cf3b66a476ef8bef"; // String | Application Key
    String emailId = "emailId_example"; // String | Email Identifier
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
      EmailEntity result = apiInstance.getEmailEntity(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, emailId, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DATA_ENABLE, X_API2CRM_DATA_BUILD, X_API2CRM_DATA_IS_FINAL, X_API2CRM_DATA_STRATEGY, X_API2CRM_DATA_COHERENT_ENTITIES, X_API2CRM_DATA_ALWAYS_ACTUAL, X_API2CRM_DATA_ACTUAL_AT, X_API2CRM_DESCRIBE_LIFETIME, expand, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmailApi#getEmailEntity");
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
| **emailId** | **String**| Email Identifier | |
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

[**EmailEntity**](EmailEntity.md)

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

<a id="updateEmailEntity"></a>
# **updateEmailEntity**
> EmailEntityRelation updateEmailEntity(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, emailId, body, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DESCRIBE_LIFETIME)

PUT for email

Update email information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmailApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    EmailApi apiInstance = new EmailApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | User Key
    String X_API2CRM_APPLICATION_KEY = "7ae5b17008fb414d84981191cf3b66a476ef8bef"; // String | Application Key
    String emailId = "emailId_example"; // String | Email Identifier
    EmailEntity body = new EmailEntity(); // EmailEntity | Update email information
    String X_API2CRM_NATIVE_ENABLE = "false"; // String | Return native response
    String X_API2CRM_DESCRIBE_LIFETIME = "X_API2CRM_DESCRIBE_LIFETIME_example"; // String | Describe lifetime
    try {
      EmailEntityRelation result = apiInstance.updateEmailEntity(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, emailId, body, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DESCRIBE_LIFETIME);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmailApi#updateEmailEntity");
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
| **emailId** | **String**| Email Identifier | |
| **body** | [**EmailEntity**](EmailEntity.md)| Update email information | |
| **X_API2CRM_NATIVE_ENABLE** | **String**| Return native response | [optional] [enum: false, true] |
| **X_API2CRM_DESCRIBE_LIFETIME** | **String**| Describe lifetime | [optional] |

### Return type

[**EmailEntityRelation**](EmailEntityRelation.md)

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

<a id="updateEmailEntityBulk"></a>
# **updateEmailEntityBulk**
> BulkEntityRelation updateEmailEntityBulk(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, body, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DESCRIBE_LIFETIME)

PUT bulk  for email

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmailApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    EmailApi apiInstance = new EmailApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | User Key
    String X_API2CRM_APPLICATION_KEY = "7ae5b17008fb414d84981191cf3b66a476ef8bef"; // String | Application Key
    BulkEntity body = new BulkEntity(); // BulkEntity | 
    String X_API2CRM_NATIVE_ENABLE = "false"; // String | Return native response
    String X_API2CRM_DESCRIBE_LIFETIME = "X_API2CRM_DESCRIBE_LIFETIME_example"; // String | Describe lifetime
    try {
      BulkEntityRelation result = apiInstance.updateEmailEntityBulk(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, body, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DESCRIBE_LIFETIME);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmailApi#updateEmailEntityBulk");
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

