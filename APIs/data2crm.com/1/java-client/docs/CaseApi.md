# CaseApi

All URIs are relative to *https://api-2445581398133.apicast.io:443/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createCaseEntity**](CaseApi.md#createCaseEntity) | **POST** /application/entity/case | POST for case |
| [**createCaseEntityBulk**](CaseApi.md#createCaseEntityBulk) | **POST** /application/entity/case/bulk | POST bulk  for case |
| [**deleteCaseCollectionBulk**](CaseApi.md#deleteCaseCollectionBulk) | **DELETE** /application/entity/case/bulk | DELETE bulk  for case |
| [**deleteCaseEntity**](CaseApi.md#deleteCaseEntity) | **DELETE** /application/entity/case/{case_id} | DELETE for case |
| [**getCaseAggregate**](CaseApi.md#getCaseAggregate) | **GET** /application/entity/case/aggregate | AGGREGATE for case |
| [**getCaseCollection**](CaseApi.md#getCaseCollection) | **GET** /application/entity/case/list | GET for case |
| [**getCaseCountCollection**](CaseApi.md#getCaseCountCollection) | **GET** /application/entity/case/count | COUNT for case |
| [**getCaseDescribe**](CaseApi.md#getCaseDescribe) | **GET** /application/entity/case/describe | DESCRIBE for case |
| [**getCaseEntity**](CaseApi.md#getCaseEntity) | **GET** /application/entity/case/{case_id} | GET for case |
| [**updateCaseEntity**](CaseApi.md#updateCaseEntity) | **PUT** /application/entity/case/{case_id} | PUT for case |
| [**updateCaseEntityBulk**](CaseApi.md#updateCaseEntityBulk) | **PUT** /application/entity/case/bulk | PUT bulk  for case |


<a id="createCaseEntity"></a>
# **createCaseEntity**
> CasesEntityRelation createCaseEntity(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, body, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DESCRIBE_LIFETIME)

POST for case

Add case into the system

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    CaseApi apiInstance = new CaseApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | User Key
    String X_API2CRM_APPLICATION_KEY = "7ae5b17008fb414d84981191cf3b66a476ef8bef"; // String | Application Key
    CasesEntity body = new CasesEntity(); // CasesEntity | Add case into the system
    String X_API2CRM_NATIVE_ENABLE = "false"; // String | Return native response
    String X_API2CRM_DESCRIBE_LIFETIME = "X_API2CRM_DESCRIBE_LIFETIME_example"; // String | Describe lifetime
    try {
      CasesEntityRelation result = apiInstance.createCaseEntity(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, body, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DESCRIBE_LIFETIME);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseApi#createCaseEntity");
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
| **body** | [**CasesEntity**](CasesEntity.md)| Add case into the system | |
| **X_API2CRM_NATIVE_ENABLE** | **String**| Return native response | [optional] [enum: false, true] |
| **X_API2CRM_DESCRIBE_LIFETIME** | **String**| Describe lifetime | [optional] |

### Return type

[**CasesEntityRelation**](CasesEntityRelation.md)

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

<a id="createCaseEntityBulk"></a>
# **createCaseEntityBulk**
> BulkEntityRelation createCaseEntityBulk(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, body, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DESCRIBE_LIFETIME)

POST bulk  for case

Add case into the system

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    CaseApi apiInstance = new CaseApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | User Key
    String X_API2CRM_APPLICATION_KEY = "7ae5b17008fb414d84981191cf3b66a476ef8bef"; // String | Application Key
    BulkEntity body = new BulkEntity(); // BulkEntity | Add case into the system
    String X_API2CRM_NATIVE_ENABLE = "false"; // String | Return native response
    String X_API2CRM_DESCRIBE_LIFETIME = "X_API2CRM_DESCRIBE_LIFETIME_example"; // String | Describe lifetime
    try {
      BulkEntityRelation result = apiInstance.createCaseEntityBulk(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, body, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DESCRIBE_LIFETIME);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseApi#createCaseEntityBulk");
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
| **body** | [**BulkEntity**](BulkEntity.md)| Add case into the system | |
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

<a id="deleteCaseCollectionBulk"></a>
# **deleteCaseCollectionBulk**
> BulkEntity deleteCaseCollectionBulk(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, body)

DELETE bulk  for case

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    CaseApi apiInstance = new CaseApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | User Key
    String X_API2CRM_APPLICATION_KEY = "7ae5b17008fb414d84981191cf3b66a476ef8bef"; // String | Application Key
    BulkEntity body = new BulkEntity(); // BulkEntity | 
    try {
      BulkEntity result = apiInstance.deleteCaseCollectionBulk(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseApi#deleteCaseCollectionBulk");
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

<a id="deleteCaseEntity"></a>
# **deleteCaseEntity**
> deleteCaseEntity(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, caseId)

DELETE for case

Delete case information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    CaseApi apiInstance = new CaseApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | User Key
    String X_API2CRM_APPLICATION_KEY = "7ae5b17008fb414d84981191cf3b66a476ef8bef"; // String | Application Key
    String caseId = "caseId_example"; // String | Case Identifier
    try {
      apiInstance.deleteCaseEntity(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, caseId);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseApi#deleteCaseEntity");
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
| **caseId** | **String**| Case Identifier | |

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

<a id="getCaseAggregate"></a>
# **getCaseAggregate**
> Aggregate getCaseAggregate(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DATA_ENABLE, X_API2CRM_DATA_BUILD, X_API2CRM_DATA_IS_FINAL, X_API2CRM_DATA_STRATEGY, X_API2CRM_DATA_COHERENT_ENTITIES, X_API2CRM_DATA_ALWAYS_ACTUAL, X_API2CRM_DATA_ACTUAL_AT, X_API2CRM_DESCRIBE_LIFETIME, filter, pipeline)

AGGREGATE for case

Returns aggregate for cases

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    CaseApi apiInstance = new CaseApi(defaultClient);
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
      Aggregate result = apiInstance.getCaseAggregate(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DATA_ENABLE, X_API2CRM_DATA_BUILD, X_API2CRM_DATA_IS_FINAL, X_API2CRM_DATA_STRATEGY, X_API2CRM_DATA_COHERENT_ENTITIES, X_API2CRM_DATA_ALWAYS_ACTUAL, X_API2CRM_DATA_ACTUAL_AT, X_API2CRM_DESCRIBE_LIFETIME, filter, pipeline);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseApi#getCaseAggregate");
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

<a id="getCaseCollection"></a>
# **getCaseCollection**
> List&lt;CasesEntity&gt; getCaseCollection(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DATA_ENABLE, X_API2CRM_DATA_BUILD, X_API2CRM_DATA_IS_FINAL, X_API2CRM_DATA_STRATEGY, X_API2CRM_DATA_COHERENT_ENTITIES, X_API2CRM_DATA_ALWAYS_ACTUAL, X_API2CRM_DATA_ACTUAL_AT, X_API2CRM_DESCRIBE_LIFETIME, pageSize, page, filter, expand, fields, sort, unique)

GET for case

Returns all cases from the system

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    CaseApi apiInstance = new CaseApi(defaultClient);
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
      List<CasesEntity> result = apiInstance.getCaseCollection(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DATA_ENABLE, X_API2CRM_DATA_BUILD, X_API2CRM_DATA_IS_FINAL, X_API2CRM_DATA_STRATEGY, X_API2CRM_DATA_COHERENT_ENTITIES, X_API2CRM_DATA_ALWAYS_ACTUAL, X_API2CRM_DATA_ACTUAL_AT, X_API2CRM_DESCRIBE_LIFETIME, pageSize, page, filter, expand, fields, sort, unique);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseApi#getCaseCollection");
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

[**List&lt;CasesEntity&gt;**](CasesEntity.md)

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

<a id="getCaseCountCollection"></a>
# **getCaseCountCollection**
> Count getCaseCountCollection(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, X_API2CRM_DATA_ENABLE, X_API2CRM_DATA_BUILD, X_API2CRM_DATA_IS_FINAL, X_API2CRM_DATA_STRATEGY, X_API2CRM_DATA_COHERENT_ENTITIES, X_API2CRM_DATA_ALWAYS_ACTUAL, X_API2CRM_DATA_ACTUAL_AT, filter)

COUNT for case

Count all cases from the system

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    CaseApi apiInstance = new CaseApi(defaultClient);
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
      Count result = apiInstance.getCaseCountCollection(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, X_API2CRM_DATA_ENABLE, X_API2CRM_DATA_BUILD, X_API2CRM_DATA_IS_FINAL, X_API2CRM_DATA_STRATEGY, X_API2CRM_DATA_COHERENT_ENTITIES, X_API2CRM_DATA_ALWAYS_ACTUAL, X_API2CRM_DATA_ACTUAL_AT, filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseApi#getCaseCountCollection");
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

<a id="getCaseDescribe"></a>
# **getCaseDescribe**
> CaseDescribe getCaseDescribe(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, X_API2CRM_DATA_ENABLE, X_API2CRM_DATA_BUILD, X_API2CRM_DATA_IS_FINAL, X_API2CRM_DATA_STRATEGY, X_API2CRM_DATA_COHERENT_ENTITIES, X_API2CRM_DATA_ALWAYS_ACTUAL, X_API2CRM_DATA_ACTUAL_AT, X_API2CRM_DESCRIBE_LIFETIME)

DESCRIBE for case

Returns describe for cases

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    CaseApi apiInstance = new CaseApi(defaultClient);
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
      CaseDescribe result = apiInstance.getCaseDescribe(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, X_API2CRM_DATA_ENABLE, X_API2CRM_DATA_BUILD, X_API2CRM_DATA_IS_FINAL, X_API2CRM_DATA_STRATEGY, X_API2CRM_DATA_COHERENT_ENTITIES, X_API2CRM_DATA_ALWAYS_ACTUAL, X_API2CRM_DATA_ACTUAL_AT, X_API2CRM_DESCRIBE_LIFETIME);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseApi#getCaseDescribe");
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

[**CaseDescribe**](CaseDescribe.md)

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

<a id="getCaseEntity"></a>
# **getCaseEntity**
> CasesEntity getCaseEntity(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, caseId, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DATA_ENABLE, X_API2CRM_DATA_BUILD, X_API2CRM_DATA_IS_FINAL, X_API2CRM_DATA_STRATEGY, X_API2CRM_DATA_COHERENT_ENTITIES, X_API2CRM_DATA_ALWAYS_ACTUAL, X_API2CRM_DATA_ACTUAL_AT, X_API2CRM_DESCRIBE_LIFETIME, expand, fields)

GET for case

Return case information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    CaseApi apiInstance = new CaseApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | User Key
    String X_API2CRM_APPLICATION_KEY = "7ae5b17008fb414d84981191cf3b66a476ef8bef"; // String | Application Key
    String caseId = "caseId_example"; // String | Case Identifier
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
      CasesEntity result = apiInstance.getCaseEntity(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, caseId, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DATA_ENABLE, X_API2CRM_DATA_BUILD, X_API2CRM_DATA_IS_FINAL, X_API2CRM_DATA_STRATEGY, X_API2CRM_DATA_COHERENT_ENTITIES, X_API2CRM_DATA_ALWAYS_ACTUAL, X_API2CRM_DATA_ACTUAL_AT, X_API2CRM_DESCRIBE_LIFETIME, expand, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseApi#getCaseEntity");
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
| **caseId** | **String**| Case Identifier | |
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

[**CasesEntity**](CasesEntity.md)

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

<a id="updateCaseEntity"></a>
# **updateCaseEntity**
> CasesEntityRelation updateCaseEntity(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, caseId, body, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DESCRIBE_LIFETIME)

PUT for case

Update case information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    CaseApi apiInstance = new CaseApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | User Key
    String X_API2CRM_APPLICATION_KEY = "7ae5b17008fb414d84981191cf3b66a476ef8bef"; // String | Application Key
    String caseId = "caseId_example"; // String | Case Identifier
    CasesEntity body = new CasesEntity(); // CasesEntity | Update case information
    String X_API2CRM_NATIVE_ENABLE = "false"; // String | Return native response
    String X_API2CRM_DESCRIBE_LIFETIME = "X_API2CRM_DESCRIBE_LIFETIME_example"; // String | Describe lifetime
    try {
      CasesEntityRelation result = apiInstance.updateCaseEntity(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, caseId, body, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DESCRIBE_LIFETIME);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseApi#updateCaseEntity");
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
| **caseId** | **String**| Case Identifier | |
| **body** | [**CasesEntity**](CasesEntity.md)| Update case information | |
| **X_API2CRM_NATIVE_ENABLE** | **String**| Return native response | [optional] [enum: false, true] |
| **X_API2CRM_DESCRIBE_LIFETIME** | **String**| Describe lifetime | [optional] |

### Return type

[**CasesEntityRelation**](CasesEntityRelation.md)

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

<a id="updateCaseEntityBulk"></a>
# **updateCaseEntityBulk**
> BulkEntityRelation updateCaseEntityBulk(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, body, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DESCRIBE_LIFETIME)

PUT bulk  for case

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    CaseApi apiInstance = new CaseApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | User Key
    String X_API2CRM_APPLICATION_KEY = "7ae5b17008fb414d84981191cf3b66a476ef8bef"; // String | Application Key
    BulkEntity body = new BulkEntity(); // BulkEntity | 
    String X_API2CRM_NATIVE_ENABLE = "false"; // String | Return native response
    String X_API2CRM_DESCRIBE_LIFETIME = "X_API2CRM_DESCRIBE_LIFETIME_example"; // String | Describe lifetime
    try {
      BulkEntityRelation result = apiInstance.updateCaseEntityBulk(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, body, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DESCRIBE_LIFETIME);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseApi#updateCaseEntityBulk");
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

