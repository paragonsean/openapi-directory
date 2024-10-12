# DefaultApi

All URIs are relative to *http://api.opendatanetwork.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createAMap**](DefaultApi.md#createAMap) | **GET** /data/v1/map/new | Create a map |
| [**findAllAvailableDataForSomeEntities**](DefaultApi.md#findAllAvailableDataForSomeEntities) | **GET** /data/v1/availability/ | Find all available data for some entities |
| [**findTheRelativesOfAnEntity**](DefaultApi.md#findTheRelativesOfAnEntity) | **GET** /entity/v1/{relation} | Find the relatives of an entity |
| [**getConstraintPermutationsForEntities**](DefaultApi.md#getConstraintPermutationsForEntities) | **GET** /data/v1/constraint/{variable} | Get constraint permutations for entities |
| [**getDatasets**](DefaultApi.md#getDatasets) | **GET** /search/v1/dataset | Get datasets |
| [**getEntities**](DefaultApi.md#getEntities) | **GET** /entity/v1 | Get Entities |
| [**getQuestions**](DefaultApi.md#getQuestions) | **GET** /search/v1/question | Get questions |
| [**getSuggestions**](DefaultApi.md#getSuggestions) | **GET** /suggest/v1/{type} | Get suggestions |
| [**getValuesForVariables**](DefaultApi.md#getValuesForVariables) | **GET** /data/v1/values | Get values for variables |


<a id="createAMap"></a>
# **createAMap**
> createAMap(variable, entityId, constraint, appToken, xAppToken)

Create a map



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.opendatanetwork.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String variable = "demographics.population.count"; // String | A single variable ID.
    String entityId = "0400000US53,0400000US08"; // String | A comma separated list of entity IDs. Entities must have the same type and represent geographical regions.
    String constraint = "constraint_example"; // String | Values must be specified for each constraint in the dataset. For example, to generate map data for `demographics.population.count`, you must specify a value for `year` by passing `year=2013`.
    String appToken = "cQovpGcdUT1CSzgYk0KPYdAI0"; // String | The [Socrata App Token](https://dev.socrata.com/docs/app-tokens.html) to be used with your request. The `app_token` parameter is required if an app token is not passed via the `X-App-Token` HTTP header. Clients must [register for their own app tokens](https://dev.socrata.com/docs/app-tokens.html).
    String xAppToken = "cQovpGcdUT1CSzgYk0KPYdAI0"; // String | e.g. cQovpGcdUT1CSzgYk0KPYdAI0
    try {
      apiInstance.createAMap(variable, entityId, constraint, appToken, xAppToken);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createAMap");
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
| **variable** | **String**| A single variable ID. | |
| **entityId** | **String**| A comma separated list of entity IDs. Entities must have the same type and represent geographical regions. | |
| **constraint** | **String**| Values must be specified for each constraint in the dataset. For example, to generate map data for &#x60;demographics.population.count&#x60;, you must specify a value for &#x60;year&#x60; by passing &#x60;year&#x3D;2013&#x60;. | [optional] |
| **appToken** | **String**| The [Socrata App Token](https://dev.socrata.com/docs/app-tokens.html) to be used with your request. The &#x60;app_token&#x60; parameter is required if an app token is not passed via the &#x60;X-App-Token&#x60; HTTP header. Clients must [register for their own app tokens](https://dev.socrata.com/docs/app-tokens.html). | [optional] |
| **xAppToken** | **String**| e.g. cQovpGcdUT1CSzgYk0KPYdAI0 | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="findAllAvailableDataForSomeEntities"></a>
# **findAllAvailableDataForSomeEntities**
> findAllAvailableDataForSomeEntities(entityId, appToken, xAppToken)

Find all available data for some entities



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.opendatanetwork.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String entityId = "0100000US,0400000US53"; // String | Comma separated list of entity IDs.
    String appToken = "cQovpGcdUT1CSzgYk0KPYdAI0"; // String | The [Socrata App Token](https://dev.socrata.com/docs/app-tokens.html) to be used with your request. The `app_token` parameter is required if an app token is not passed via the `X-App-Token` HTTP header. Clients must [register for their own app tokens](https://dev.socrata.com/docs/app-tokens.html).
    String xAppToken = "cQovpGcdUT1CSzgYk0KPYdAI0"; // String | e.g. cQovpGcdUT1CSzgYk0KPYdAI0
    try {
      apiInstance.findAllAvailableDataForSomeEntities(entityId, appToken, xAppToken);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#findAllAvailableDataForSomeEntities");
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
| **entityId** | **String**| Comma separated list of entity IDs. | |
| **appToken** | **String**| The [Socrata App Token](https://dev.socrata.com/docs/app-tokens.html) to be used with your request. The &#x60;app_token&#x60; parameter is required if an app token is not passed via the &#x60;X-App-Token&#x60; HTTP header. Clients must [register for their own app tokens](https://dev.socrata.com/docs/app-tokens.html). | [optional] |
| **xAppToken** | **String**| e.g. cQovpGcdUT1CSzgYk0KPYdAI0 | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="findTheRelativesOfAnEntity"></a>
# **findTheRelativesOfAnEntity**
> findTheRelativesOfAnEntity(relation, entityId, variableId, limit, appToken, xAppToken)

Find the relatives of an entity



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.opendatanetwork.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String relation = "parent"; // String | The type of relation to find.
    String entityId = "0400000US53"; // String | ID of the target entity.
    String variableId = "demographics.population.seattle"; // String | If this parameter is included, only entities with data for the given variable will be returned. Note that this may cause the number of entities returned to be less than the specified `limit`.
    BigDecimal limit = new BigDecimal("10"); // BigDecimal | Maximum number of entities in each group. Must be an integer from 1 to 1000.
    String appToken = "cQovpGcdUT1CSzgYk0KPYdAI0"; // String | The [Socrata App Token](https://dev.socrata.com/docs/app-tokens.html) to be used with your request. The `app_token` parameter is required if an app token is not passed via the `X-App-Token` HTTP header. Clients must [register for their own app tokens](https://dev.socrata.com/docs/app-tokens.html).
    String xAppToken = "cQovpGcdUT1CSzgYk0KPYdAI0"; // String | e.g. cQovpGcdUT1CSzgYk0KPYdAI0
    try {
      apiInstance.findTheRelativesOfAnEntity(relation, entityId, variableId, limit, appToken, xAppToken);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#findTheRelativesOfAnEntity");
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
| **relation** | **String**| The type of relation to find. | [enum: parent, child, sibling, peer] |
| **entityId** | **String**| ID of the target entity. | |
| **variableId** | **String**| If this parameter is included, only entities with data for the given variable will be returned. Note that this may cause the number of entities returned to be less than the specified &#x60;limit&#x60;. | [optional] |
| **limit** | **BigDecimal**| Maximum number of entities in each group. Must be an integer from 1 to 1000. | [optional] [default to 10] |
| **appToken** | **String**| The [Socrata App Token](https://dev.socrata.com/docs/app-tokens.html) to be used with your request. The &#x60;app_token&#x60; parameter is required if an app token is not passed via the &#x60;X-App-Token&#x60; HTTP header. Clients must [register for their own app tokens](https://dev.socrata.com/docs/app-tokens.html). | [optional] |
| **xAppToken** | **String**| e.g. cQovpGcdUT1CSzgYk0KPYdAI0 | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getConstraintPermutationsForEntities"></a>
# **getConstraintPermutationsForEntities**
> getConstraintPermutationsForEntities(variable, entityId, constraint, appToken, xAppToken)

Get constraint permutations for entities



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.opendatanetwork.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String variable = "demographics.population.count"; // String | Full ID of the variable to retrieve.
    String entityId = "0100000US,0400000US53"; // String | Comma separated list of entity IDs.
    String constraint = "year"; // String | Constraint to use.
    String appToken = "cQovpGcdUT1CSzgYk0KPYdAI0"; // String | The [Socrata App Token](https://dev.socrata.com/docs/app-tokens.html) to be used with your request. The `app_token` parameter is required if an app token is not passed via the `X-App-Token` HTTP header. Clients must [register for their own app tokens](https://dev.socrata.com/docs/app-tokens.html).
    String xAppToken = "cQovpGcdUT1CSzgYk0KPYdAI0"; // String | e.g. cQovpGcdUT1CSzgYk0KPYdAI0
    try {
      apiInstance.getConstraintPermutationsForEntities(variable, entityId, constraint, appToken, xAppToken);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getConstraintPermutationsForEntities");
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
| **variable** | **String**| Full ID of the variable to retrieve. | |
| **entityId** | **String**| Comma separated list of entity IDs. | |
| **constraint** | **String**| Constraint to use. | |
| **appToken** | **String**| The [Socrata App Token](https://dev.socrata.com/docs/app-tokens.html) to be used with your request. The &#x60;app_token&#x60; parameter is required if an app token is not passed via the &#x60;X-App-Token&#x60; HTTP header. Clients must [register for their own app tokens](https://dev.socrata.com/docs/app-tokens.html). | [optional] |
| **xAppToken** | **String**| e.g. cQovpGcdUT1CSzgYk0KPYdAI0 | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getDatasets"></a>
# **getDatasets**
> getDatasets(entityId, datasetId, limit, offset, appToken, xAppToken)

Get datasets



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.opendatanetwork.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String entityId = "0100000US"; // String | Entities to use in formulating the query.
    String datasetId = "demographics.population"; // String | If included, the search terms of the dataset will be used in the query.
    BigDecimal limit = new BigDecimal("10"); // BigDecimal | Maximum number of results to return. Must be an integer from 0 to 50000.
    BigDecimal offset = new BigDecimal(78); // BigDecimal | Number of results to skip. Used for pagination.
    String appToken = "cQovpGcdUT1CSzgYk0KPYdAI0"; // String | The [Socrata App Token](https://dev.socrata.com/docs/app-tokens.html) to be used with your request. The `app_token` parameter is required if an app token is not passed via the `X-App-Token` HTTP header. Clients must [register for their own app tokens](https://dev.socrata.com/docs/app-tokens.html).
    String xAppToken = "cQovpGcdUT1CSzgYk0KPYdAI0"; // String | e.g. cQovpGcdUT1CSzgYk0KPYdAI0
    try {
      apiInstance.getDatasets(entityId, datasetId, limit, offset, appToken, xAppToken);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getDatasets");
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
| **entityId** | **String**| Entities to use in formulating the query. | [optional] |
| **datasetId** | **String**| If included, the search terms of the dataset will be used in the query. | [optional] |
| **limit** | **BigDecimal**| Maximum number of results to return. Must be an integer from 0 to 50000. | [optional] [default to 10] |
| **offset** | **BigDecimal**| Number of results to skip. Used for pagination. | [optional] |
| **appToken** | **String**| The [Socrata App Token](https://dev.socrata.com/docs/app-tokens.html) to be used with your request. The &#x60;app_token&#x60; parameter is required if an app token is not passed via the &#x60;X-App-Token&#x60; HTTP header. Clients must [register for their own app tokens](https://dev.socrata.com/docs/app-tokens.html). | [optional] |
| **xAppToken** | **String**| e.g. cQovpGcdUT1CSzgYk0KPYdAI0 | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getEntities"></a>
# **getEntities**
> getEntities(entityId, entityName, entityType, appToken, xAppToken)

Get Entities



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.opendatanetwork.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String entityId = "0400000US53"; // String | ID of the entity.
    String entityName = "washington"; // String | Name of the entity.
    String entityType = "region.state"; // String | Type of the entity.
    String appToken = "cQovpGcdUT1CSzgYk0KPYdAI0"; // String | The [Socrata App Token](https://dev.socrata.com/docs/app-tokens.html) to be used with your request. The `app_token` parameter is required if an app token is not passed via the `X-App-Token` HTTP header. Clients must [register for their own app tokens](https://dev.socrata.com/docs/app-tokens.html).
    String xAppToken = "cQovpGcdUT1CSzgYk0KPYdAI0"; // String | e.g. cQovpGcdUT1CSzgYk0KPYdAI0
    try {
      apiInstance.getEntities(entityId, entityName, entityType, appToken, xAppToken);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getEntities");
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
| **entityId** | **String**| ID of the entity. | [optional] |
| **entityName** | **String**| Name of the entity. | [optional] |
| **entityType** | **String**| Type of the entity. | [optional] |
| **appToken** | **String**| The [Socrata App Token](https://dev.socrata.com/docs/app-tokens.html) to be used with your request. The &#x60;app_token&#x60; parameter is required if an app token is not passed via the &#x60;X-App-Token&#x60; HTTP header. Clients must [register for their own app tokens](https://dev.socrata.com/docs/app-tokens.html). | [optional] |
| **xAppToken** | **String**| e.g. cQovpGcdUT1CSzgYk0KPYdAI0 | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getQuestions"></a>
# **getQuestions**
> getQuestions(query, limit, offset, appToken, xAppToken)

Get questions



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.opendatanetwork.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String query = "seattle"; // String | String to search against.
    BigDecimal limit = new BigDecimal("10"); // BigDecimal | Maximum number of results to return. Must be an integer from 0 to 50000.
    BigDecimal offset = new BigDecimal(78); // BigDecimal | Number of results to skip. Used for pagination.
    String appToken = "cQovpGcdUT1CSzgYk0KPYdAI0"; // String | The [Socrata App Token](https://dev.socrata.com/docs/app-tokens.html) to be used with your request. The `app_token` parameter is required if an app token is not passed via the `X-App-Token` HTTP header. Clients must [register for their own app tokens](https://dev.socrata.com/docs/app-tokens.html).
    String xAppToken = "cQovpGcdUT1CSzgYk0KPYdAI0"; // String | e.g. cQovpGcdUT1CSzgYk0KPYdAI0
    try {
      apiInstance.getQuestions(query, limit, offset, appToken, xAppToken);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getQuestions");
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
| **query** | **String**| String to search against. | |
| **limit** | **BigDecimal**| Maximum number of results to return. Must be an integer from 0 to 50000. | [optional] [default to 10] |
| **offset** | **BigDecimal**| Number of results to skip. Used for pagination. | [optional] |
| **appToken** | **String**| The [Socrata App Token](https://dev.socrata.com/docs/app-tokens.html) to be used with your request. The &#x60;app_token&#x60; parameter is required if an app token is not passed via the &#x60;X-App-Token&#x60; HTTP header. Clients must [register for their own app tokens](https://dev.socrata.com/docs/app-tokens.html). | [optional] |
| **xAppToken** | **String**| e.g. cQovpGcdUT1CSzgYk0KPYdAI0 | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getSuggestions"></a>
# **getSuggestions**
> getSuggestions(type, query, limit, variableId, appToken, xAppToken)

Get suggestions



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.opendatanetwork.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String type = "entity"; // String | Type of the object to find.
    String query = "seattl"; // String | Query to match.
    BigDecimal limit = new BigDecimal("5"); // BigDecimal | Maximum number of results to return. Must be an integer from 0 to 100.
    String variableId = "demographics.population.count"; // String | This parameter is only available when suggesting entities with `type=entity`. If it is provided, suggestions will be filtered to include only entities that have data for the given variable.  If the variable provided is invalid, no entities will be returned.  Note that this filtering will increase response time significantly, so it should only be used when necessary.
    String appToken = "cQovpGcdUT1CSzgYk0KPYdAI0"; // String | The [Socrata App Token](https://dev.socrata.com/docs/app-tokens.html) to be used with your request. The `app_token` parameter is required if an app token is not passed via the `X-App-Token` HTTP header. Clients must [register for their own app tokens](https://dev.socrata.com/docs/app-tokens.html).
    String xAppToken = "cQovpGcdUT1CSzgYk0KPYdAI0"; // String | e.g. cQovpGcdUT1CSzgYk0KPYdAI0
    try {
      apiInstance.getSuggestions(type, query, limit, variableId, appToken, xAppToken);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getSuggestions");
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
| **type** | **String**| Type of the object to find. | [enum: entity, category, publisher, dataset, question] |
| **query** | **String**| Query to match. | |
| **limit** | **BigDecimal**| Maximum number of results to return. Must be an integer from 0 to 100. | [optional] [default to 5] |
| **variableId** | **String**| This parameter is only available when suggesting entities with &#x60;type&#x3D;entity&#x60;. If it is provided, suggestions will be filtered to include only entities that have data for the given variable.  If the variable provided is invalid, no entities will be returned.  Note that this filtering will increase response time significantly, so it should only be used when necessary. | [optional] |
| **appToken** | **String**| The [Socrata App Token](https://dev.socrata.com/docs/app-tokens.html) to be used with your request. The &#x60;app_token&#x60; parameter is required if an app token is not passed via the &#x60;X-App-Token&#x60; HTTP header. Clients must [register for their own app tokens](https://dev.socrata.com/docs/app-tokens.html). | [optional] |
| **xAppToken** | **String**| e.g. cQovpGcdUT1CSzgYk0KPYdAI0 | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getValuesForVariables"></a>
# **getValuesForVariables**
> getValuesForVariables(variable, entityId, forecast, describe, format, appToken, xAppToken)

Get values for variables



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.opendatanetwork.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String variable = "demographics.population.count"; // String | Comma separated list of variable IDs. Defaults to retrieving all variables. It is also possible to pass in a topic such as `demographics`, or a dataset such as `demographics.population`, which would both be equivalent to specifying `demographics.population.count` and `demographics.population.change`. Note that only variables in the same dataset are allowed.
    String entityId = "0100000US,0400000US53"; // String | Comma separated list of entity IDs. Defaults to retrieving all entities. Note that since there is currently no results pagination, retrieving values for all entities may produce incomplete results.
    BigDecimal forecast = new BigDecimal("3"); // BigDecimal | Number of steps to forecast. Must be an integer between 0 and 20. Forecasts are produced using linear extrapolation on the data. They are only available when retrieving data for a single variable across many numerical constraint options.  + Default `0`
    Boolean describe = false; // Boolean | Whether or not to produce a description of the data. Set to `true` to produce a description. Descriptions are not available if no entities are specified.  + Default `false`
    String format = "google"; // String | If format is set to `google`, the data frame will be formatted as a [Google Visualizations data table](https://developers.google.com/chart/interactive/docs/reference#datatable-class). If the format is not provided or invalid, then the frame will be formatted normally.
    String appToken = "cQovpGcdUT1CSzgYk0KPYdAI0"; // String | The [Socrata App Token](https://dev.socrata.com/docs/app-tokens.html) to be used with your request. The `app_token` parameter is required if an app token is not passed via the `X-App-Token` HTTP header. Clients must [register for their own app tokens](https://dev.socrata.com/docs/app-tokens.html).
    String xAppToken = "cQovpGcdUT1CSzgYk0KPYdAI0"; // String | e.g. cQovpGcdUT1CSzgYk0KPYdAI0
    try {
      apiInstance.getValuesForVariables(variable, entityId, forecast, describe, format, appToken, xAppToken);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getValuesForVariables");
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
| **variable** | **String**| Comma separated list of variable IDs. Defaults to retrieving all variables. It is also possible to pass in a topic such as &#x60;demographics&#x60;, or a dataset such as &#x60;demographics.population&#x60;, which would both be equivalent to specifying &#x60;demographics.population.count&#x60; and &#x60;demographics.population.change&#x60;. Note that only variables in the same dataset are allowed. | |
| **entityId** | **String**| Comma separated list of entity IDs. Defaults to retrieving all entities. Note that since there is currently no results pagination, retrieving values for all entities may produce incomplete results. | [optional] |
| **forecast** | **BigDecimal**| Number of steps to forecast. Must be an integer between 0 and 20. Forecasts are produced using linear extrapolation on the data. They are only available when retrieving data for a single variable across many numerical constraint options.  + Default &#x60;0&#x60; | [optional] |
| **describe** | **Boolean**| Whether or not to produce a description of the data. Set to &#x60;true&#x60; to produce a description. Descriptions are not available if no entities are specified.  + Default &#x60;false&#x60; | [optional] |
| **format** | **String**| If format is set to &#x60;google&#x60;, the data frame will be formatted as a [Google Visualizations data table](https://developers.google.com/chart/interactive/docs/reference#datatable-class). If the format is not provided or invalid, then the frame will be formatted normally. | [optional] [enum: google] |
| **appToken** | **String**| The [Socrata App Token](https://dev.socrata.com/docs/app-tokens.html) to be used with your request. The &#x60;app_token&#x60; parameter is required if an app token is not passed via the &#x60;X-App-Token&#x60; HTTP header. Clients must [register for their own app tokens](https://dev.socrata.com/docs/app-tokens.html). | [optional] |
| **xAppToken** | **String**| e.g. cQovpGcdUT1CSzgYk0KPYdAI0 | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

