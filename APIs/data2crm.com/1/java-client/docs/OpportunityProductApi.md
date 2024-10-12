# OpportunityProductApi

All URIs are relative to *https://api-2445581398133.apicast.io:443/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createOpportunityProductEntity**](OpportunityProductApi.md#createOpportunityProductEntity) | **POST** /application/entity/opportunityProduct | POST for opportunityProduct |
| [**createOpportunityProductEntityBulk**](OpportunityProductApi.md#createOpportunityProductEntityBulk) | **POST** /application/entity/opportunityProduct/bulk | POST bulk  for opportunityProduct |
| [**deleteOpportunityProductCollectionBulk**](OpportunityProductApi.md#deleteOpportunityProductCollectionBulk) | **DELETE** /application/entity/opportunityProduct/bulk | DELETE bulk  for opportunityProduct |
| [**deleteOpportunityProductEntity**](OpportunityProductApi.md#deleteOpportunityProductEntity) | **DELETE** /application/entity/opportunityProduct/{opportunityProduct_id} | DELETE for opportunityProduct |
| [**getOpportunityProductAggregate**](OpportunityProductApi.md#getOpportunityProductAggregate) | **GET** /application/entity/opportunityProduct/aggregate | AGGREGATE for opportunityProduct |
| [**getOpportunityProductCollection**](OpportunityProductApi.md#getOpportunityProductCollection) | **GET** /application/entity/opportunityProduct/list | GET for opportunityProduct |
| [**getOpportunityProductCountCollection**](OpportunityProductApi.md#getOpportunityProductCountCollection) | **GET** /application/entity/opportunityProduct/count | COUNT for opportunityProduct |
| [**getOpportunityProductDescribe**](OpportunityProductApi.md#getOpportunityProductDescribe) | **GET** /application/entity/opportunityProduct/describe | DESCRIBE for opportunityProduct |
| [**getOpportunityProductEntity**](OpportunityProductApi.md#getOpportunityProductEntity) | **GET** /application/entity/opportunityProduct/{opportunityProduct_id} | GET for opportunityProduct |
| [**updateOpportunityProductEntity**](OpportunityProductApi.md#updateOpportunityProductEntity) | **PUT** /application/entity/opportunityProduct/{opportunityProduct_id} | PUT for opportunityProduct |
| [**updateOpportunityProductEntityBulk**](OpportunityProductApi.md#updateOpportunityProductEntityBulk) | **PUT** /application/entity/opportunityProduct/bulk | PUT bulk  for opportunityProduct |


<a id="createOpportunityProductEntity"></a>
# **createOpportunityProductEntity**
> OpportunityProductEntityRelation createOpportunityProductEntity(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, body, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DESCRIBE_LIFETIME)

POST for opportunityProduct

Add opportunityProduct into the system

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OpportunityProductApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    OpportunityProductApi apiInstance = new OpportunityProductApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | User Key
    String X_API2CRM_APPLICATION_KEY = "7ae5b17008fb414d84981191cf3b66a476ef8bef"; // String | Application Key
    OpportunityProductEntity body = new OpportunityProductEntity(); // OpportunityProductEntity | Add opportunityProduct into the system
    String X_API2CRM_NATIVE_ENABLE = "false"; // String | Return native response
    String X_API2CRM_DESCRIBE_LIFETIME = "X_API2CRM_DESCRIBE_LIFETIME_example"; // String | Describe lifetime
    try {
      OpportunityProductEntityRelation result = apiInstance.createOpportunityProductEntity(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, body, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DESCRIBE_LIFETIME);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OpportunityProductApi#createOpportunityProductEntity");
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
| **body** | [**OpportunityProductEntity**](OpportunityProductEntity.md)| Add opportunityProduct into the system | |
| **X_API2CRM_NATIVE_ENABLE** | **String**| Return native response | [optional] [enum: false, true] |
| **X_API2CRM_DESCRIBE_LIFETIME** | **String**| Describe lifetime | [optional] |

### Return type

[**OpportunityProductEntityRelation**](OpportunityProductEntityRelation.md)

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

<a id="createOpportunityProductEntityBulk"></a>
# **createOpportunityProductEntityBulk**
> BulkEntityRelation createOpportunityProductEntityBulk(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, body, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DESCRIBE_LIFETIME)

POST bulk  for opportunityProduct

Add opportunityProduct into the system

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OpportunityProductApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    OpportunityProductApi apiInstance = new OpportunityProductApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | User Key
    String X_API2CRM_APPLICATION_KEY = "7ae5b17008fb414d84981191cf3b66a476ef8bef"; // String | Application Key
    BulkEntity body = new BulkEntity(); // BulkEntity | Add opportunityProduct into the system
    String X_API2CRM_NATIVE_ENABLE = "false"; // String | Return native response
    String X_API2CRM_DESCRIBE_LIFETIME = "X_API2CRM_DESCRIBE_LIFETIME_example"; // String | Describe lifetime
    try {
      BulkEntityRelation result = apiInstance.createOpportunityProductEntityBulk(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, body, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DESCRIBE_LIFETIME);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OpportunityProductApi#createOpportunityProductEntityBulk");
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
| **body** | [**BulkEntity**](BulkEntity.md)| Add opportunityProduct into the system | |
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

<a id="deleteOpportunityProductCollectionBulk"></a>
# **deleteOpportunityProductCollectionBulk**
> BulkEntity deleteOpportunityProductCollectionBulk(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, body)

DELETE bulk  for opportunityProduct

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OpportunityProductApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    OpportunityProductApi apiInstance = new OpportunityProductApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | User Key
    String X_API2CRM_APPLICATION_KEY = "7ae5b17008fb414d84981191cf3b66a476ef8bef"; // String | Application Key
    BulkEntity body = new BulkEntity(); // BulkEntity | 
    try {
      BulkEntity result = apiInstance.deleteOpportunityProductCollectionBulk(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OpportunityProductApi#deleteOpportunityProductCollectionBulk");
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

<a id="deleteOpportunityProductEntity"></a>
# **deleteOpportunityProductEntity**
> deleteOpportunityProductEntity(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, opportunityProductId)

DELETE for opportunityProduct

Delete opportunityProduct information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OpportunityProductApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    OpportunityProductApi apiInstance = new OpportunityProductApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | User Key
    String X_API2CRM_APPLICATION_KEY = "7ae5b17008fb414d84981191cf3b66a476ef8bef"; // String | Application Key
    String opportunityProductId = "opportunityProductId_example"; // String | Opportunity Product Identifier
    try {
      apiInstance.deleteOpportunityProductEntity(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, opportunityProductId);
    } catch (ApiException e) {
      System.err.println("Exception when calling OpportunityProductApi#deleteOpportunityProductEntity");
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
| **opportunityProductId** | **String**| Opportunity Product Identifier | |

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

<a id="getOpportunityProductAggregate"></a>
# **getOpportunityProductAggregate**
> Aggregate getOpportunityProductAggregate(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DATA_ENABLE, X_API2CRM_DATA_BUILD, X_API2CRM_DATA_IS_FINAL, X_API2CRM_DATA_STRATEGY, X_API2CRM_DATA_COHERENT_ENTITIES, X_API2CRM_DATA_ALWAYS_ACTUAL, X_API2CRM_DATA_ACTUAL_AT, X_API2CRM_DESCRIBE_LIFETIME, filter, pipeline)

AGGREGATE for opportunityProduct

Returns aggregate for opportunityProducts

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OpportunityProductApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    OpportunityProductApi apiInstance = new OpportunityProductApi(defaultClient);
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
      Aggregate result = apiInstance.getOpportunityProductAggregate(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DATA_ENABLE, X_API2CRM_DATA_BUILD, X_API2CRM_DATA_IS_FINAL, X_API2CRM_DATA_STRATEGY, X_API2CRM_DATA_COHERENT_ENTITIES, X_API2CRM_DATA_ALWAYS_ACTUAL, X_API2CRM_DATA_ACTUAL_AT, X_API2CRM_DESCRIBE_LIFETIME, filter, pipeline);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OpportunityProductApi#getOpportunityProductAggregate");
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

<a id="getOpportunityProductCollection"></a>
# **getOpportunityProductCollection**
> List&lt;OpportunityProductEntity&gt; getOpportunityProductCollection(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DATA_ENABLE, X_API2CRM_DATA_BUILD, X_API2CRM_DATA_IS_FINAL, X_API2CRM_DATA_STRATEGY, X_API2CRM_DATA_COHERENT_ENTITIES, X_API2CRM_DATA_ALWAYS_ACTUAL, X_API2CRM_DATA_ACTUAL_AT, X_API2CRM_DESCRIBE_LIFETIME, pageSize, page, filter, expand, fields, sort, unique)

GET for opportunityProduct

Returns all opportunityProducts from the system

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OpportunityProductApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    OpportunityProductApi apiInstance = new OpportunityProductApi(defaultClient);
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
      List<OpportunityProductEntity> result = apiInstance.getOpportunityProductCollection(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DATA_ENABLE, X_API2CRM_DATA_BUILD, X_API2CRM_DATA_IS_FINAL, X_API2CRM_DATA_STRATEGY, X_API2CRM_DATA_COHERENT_ENTITIES, X_API2CRM_DATA_ALWAYS_ACTUAL, X_API2CRM_DATA_ACTUAL_AT, X_API2CRM_DESCRIBE_LIFETIME, pageSize, page, filter, expand, fields, sort, unique);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OpportunityProductApi#getOpportunityProductCollection");
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

[**List&lt;OpportunityProductEntity&gt;**](OpportunityProductEntity.md)

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

<a id="getOpportunityProductCountCollection"></a>
# **getOpportunityProductCountCollection**
> Count getOpportunityProductCountCollection(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, X_API2CRM_DATA_ENABLE, X_API2CRM_DATA_BUILD, X_API2CRM_DATA_IS_FINAL, X_API2CRM_DATA_STRATEGY, X_API2CRM_DATA_COHERENT_ENTITIES, X_API2CRM_DATA_ALWAYS_ACTUAL, X_API2CRM_DATA_ACTUAL_AT, filter)

COUNT for opportunityProduct

Count all opportunityProducts from the system

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OpportunityProductApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    OpportunityProductApi apiInstance = new OpportunityProductApi(defaultClient);
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
      Count result = apiInstance.getOpportunityProductCountCollection(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, X_API2CRM_DATA_ENABLE, X_API2CRM_DATA_BUILD, X_API2CRM_DATA_IS_FINAL, X_API2CRM_DATA_STRATEGY, X_API2CRM_DATA_COHERENT_ENTITIES, X_API2CRM_DATA_ALWAYS_ACTUAL, X_API2CRM_DATA_ACTUAL_AT, filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OpportunityProductApi#getOpportunityProductCountCollection");
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

<a id="getOpportunityProductDescribe"></a>
# **getOpportunityProductDescribe**
> OpportunityProductDescribe getOpportunityProductDescribe(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, X_API2CRM_DATA_ENABLE, X_API2CRM_DATA_BUILD, X_API2CRM_DATA_IS_FINAL, X_API2CRM_DATA_STRATEGY, X_API2CRM_DATA_COHERENT_ENTITIES, X_API2CRM_DATA_ALWAYS_ACTUAL, X_API2CRM_DATA_ACTUAL_AT, X_API2CRM_DESCRIBE_LIFETIME)

DESCRIBE for opportunityProduct

Returns describe for opportunityProducts

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OpportunityProductApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    OpportunityProductApi apiInstance = new OpportunityProductApi(defaultClient);
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
      OpportunityProductDescribe result = apiInstance.getOpportunityProductDescribe(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, X_API2CRM_DATA_ENABLE, X_API2CRM_DATA_BUILD, X_API2CRM_DATA_IS_FINAL, X_API2CRM_DATA_STRATEGY, X_API2CRM_DATA_COHERENT_ENTITIES, X_API2CRM_DATA_ALWAYS_ACTUAL, X_API2CRM_DATA_ACTUAL_AT, X_API2CRM_DESCRIBE_LIFETIME);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OpportunityProductApi#getOpportunityProductDescribe");
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

[**OpportunityProductDescribe**](OpportunityProductDescribe.md)

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

<a id="getOpportunityProductEntity"></a>
# **getOpportunityProductEntity**
> OpportunityProductEntity getOpportunityProductEntity(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, opportunityProductId, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DATA_ENABLE, X_API2CRM_DATA_BUILD, X_API2CRM_DATA_IS_FINAL, X_API2CRM_DATA_STRATEGY, X_API2CRM_DATA_COHERENT_ENTITIES, X_API2CRM_DATA_ALWAYS_ACTUAL, X_API2CRM_DATA_ACTUAL_AT, X_API2CRM_DESCRIBE_LIFETIME, expand, fields)

GET for opportunityProduct

Return opportunityProduct information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OpportunityProductApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    OpportunityProductApi apiInstance = new OpportunityProductApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | User Key
    String X_API2CRM_APPLICATION_KEY = "7ae5b17008fb414d84981191cf3b66a476ef8bef"; // String | Application Key
    String opportunityProductId = "opportunityProductId_example"; // String | Opportunity Product Identifier
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
      OpportunityProductEntity result = apiInstance.getOpportunityProductEntity(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, opportunityProductId, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DATA_ENABLE, X_API2CRM_DATA_BUILD, X_API2CRM_DATA_IS_FINAL, X_API2CRM_DATA_STRATEGY, X_API2CRM_DATA_COHERENT_ENTITIES, X_API2CRM_DATA_ALWAYS_ACTUAL, X_API2CRM_DATA_ACTUAL_AT, X_API2CRM_DESCRIBE_LIFETIME, expand, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OpportunityProductApi#getOpportunityProductEntity");
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
| **opportunityProductId** | **String**| Opportunity Product Identifier | |
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

[**OpportunityProductEntity**](OpportunityProductEntity.md)

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

<a id="updateOpportunityProductEntity"></a>
# **updateOpportunityProductEntity**
> OpportunityProductEntityRelation updateOpportunityProductEntity(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, opportunityProductId, body, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DESCRIBE_LIFETIME)

PUT for opportunityProduct

Update opportunityProduct information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OpportunityProductApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    OpportunityProductApi apiInstance = new OpportunityProductApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | User Key
    String X_API2CRM_APPLICATION_KEY = "7ae5b17008fb414d84981191cf3b66a476ef8bef"; // String | Application Key
    String opportunityProductId = "opportunityProductId_example"; // String | Opportunity Product Identifier
    OpportunityProductEntity body = new OpportunityProductEntity(); // OpportunityProductEntity | Update opportunityProduct information
    String X_API2CRM_NATIVE_ENABLE = "false"; // String | Return native response
    String X_API2CRM_DESCRIBE_LIFETIME = "X_API2CRM_DESCRIBE_LIFETIME_example"; // String | Describe lifetime
    try {
      OpportunityProductEntityRelation result = apiInstance.updateOpportunityProductEntity(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, opportunityProductId, body, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DESCRIBE_LIFETIME);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OpportunityProductApi#updateOpportunityProductEntity");
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
| **opportunityProductId** | **String**| Opportunity Product Identifier | |
| **body** | [**OpportunityProductEntity**](OpportunityProductEntity.md)| Update opportunityProduct information | |
| **X_API2CRM_NATIVE_ENABLE** | **String**| Return native response | [optional] [enum: false, true] |
| **X_API2CRM_DESCRIBE_LIFETIME** | **String**| Describe lifetime | [optional] |

### Return type

[**OpportunityProductEntityRelation**](OpportunityProductEntityRelation.md)

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

<a id="updateOpportunityProductEntityBulk"></a>
# **updateOpportunityProductEntityBulk**
> BulkEntityRelation updateOpportunityProductEntityBulk(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, body, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DESCRIBE_LIFETIME)

PUT bulk  for opportunityProduct

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OpportunityProductApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    OpportunityProductApi apiInstance = new OpportunityProductApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | User Key
    String X_API2CRM_APPLICATION_KEY = "7ae5b17008fb414d84981191cf3b66a476ef8bef"; // String | Application Key
    BulkEntity body = new BulkEntity(); // BulkEntity | 
    String X_API2CRM_NATIVE_ENABLE = "false"; // String | Return native response
    String X_API2CRM_DESCRIBE_LIFETIME = "X_API2CRM_DESCRIBE_LIFETIME_example"; // String | Describe lifetime
    try {
      BulkEntityRelation result = apiInstance.updateOpportunityProductEntityBulk(X_API2CRM_USER_KEY, X_API2CRM_APPLICATION_KEY, body, X_API2CRM_NATIVE_ENABLE, X_API2CRM_DESCRIBE_LIFETIME);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OpportunityProductApi#updateOpportunityProductEntityBulk");
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

