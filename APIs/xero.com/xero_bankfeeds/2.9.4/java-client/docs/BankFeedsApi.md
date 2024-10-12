# BankFeedsApi

All URIs are relative to *https://api.xero.com/bankfeeds.xro/1.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createFeedConnections**](BankFeedsApi.md#createFeedConnections) | **POST** /FeedConnections | Create one or more new feed connection |
| [**createStatements**](BankFeedsApi.md#createStatements) | **POST** /Statements | Creates one or more new statements |
| [**deleteFeedConnections**](BankFeedsApi.md#deleteFeedConnections) | **POST** /FeedConnections/DeleteRequests | Delete an existing feed connection |
| [**getFeedConnection**](BankFeedsApi.md#getFeedConnection) | **GET** /FeedConnections/{id} | Retrieve single feed connection based on a unique id provided |
| [**getFeedConnections**](BankFeedsApi.md#getFeedConnections) | **GET** /FeedConnections | Searches for feed connections |
| [**getStatement**](BankFeedsApi.md#getStatement) | **GET** /Statements/{statementID} | Retrieve single statement based on unique id provided |
| [**getStatements**](BankFeedsApi.md#getStatements) | **GET** /Statements | Retrieve all statements |


<a id="createFeedConnections"></a>
# **createFeedConnections**
> FeedConnections createFeedConnections(xeroTenantId, feedConnections)

Create one or more new feed connection

By passing in the FeedConnections array object in the body, you can create one or more new feed connections

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BankFeedsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/bankfeeds.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    BankFeedsApi apiInstance = new BankFeedsApi(defaultClient);
    String xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
    FeedConnections feedConnections = new FeedConnections(); // FeedConnections | Feed Connection(s) array object in the body
    try {
      FeedConnections result = apiInstance.createFeedConnections(xeroTenantId, feedConnections);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BankFeedsApi#createFeedConnections");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **feedConnections** | [**FeedConnections**](FeedConnections.md)| Feed Connection(s) array object in the body | |

### Return type

[**FeedConnections**](FeedConnections.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | success new feed connection(s)response |  -  |
| **400** | invalid input, object invalid |  -  |
| **409** | failed to create new feed connection(s)response |  -  |

<a id="createStatements"></a>
# **createStatements**
> Statements createStatements(xeroTenantId, statements)

Creates one or more new statements

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BankFeedsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/bankfeeds.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    BankFeedsApi apiInstance = new BankFeedsApi(defaultClient);
    String xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
    Statements statements = new Statements(); // Statements | Statements array of objects in the body
    try {
      Statements result = apiInstance.createStatements(xeroTenantId, statements);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BankFeedsApi#createStatements");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **statements** | [**Statements**](Statements.md)| Statements array of objects in the body | [optional] |

### Return type

[**Statements**](Statements.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Success returns Statements array of objects in response |  -  |
| **400** | Statement failed validation |  -  |
| **403** | Invalid application or feed connection |  -  |
| **409** | Duplicate statement received |  -  |
| **413** | Statement exceeds size limit |  -  |
| **422** | Unprocessable Entity |  -  |
| **500** | Intermittent Xero Error |  -  |

<a id="deleteFeedConnections"></a>
# **deleteFeedConnections**
> FeedConnections deleteFeedConnections(xeroTenantId, feedConnections)

Delete an existing feed connection

By passing in FeedConnections array object in the body, you can delete a feed connection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BankFeedsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/bankfeeds.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    BankFeedsApi apiInstance = new BankFeedsApi(defaultClient);
    String xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
    FeedConnections feedConnections = new FeedConnections(); // FeedConnections | Feed Connections array object in the body
    try {
      FeedConnections result = apiInstance.deleteFeedConnections(xeroTenantId, feedConnections);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BankFeedsApi#deleteFeedConnections");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **feedConnections** | [**FeedConnections**](FeedConnections.md)| Feed Connections array object in the body | |

### Return type

[**FeedConnections**](FeedConnections.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Success response for deleted feed connection |  -  |
| **400** | bad input parameter |  -  |

<a id="getFeedConnection"></a>
# **getFeedConnection**
> FeedConnection getFeedConnection(xeroTenantId, id)

Retrieve single feed connection based on a unique id provided

By passing in a FeedConnection Id options, you can search for matching feed connections

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BankFeedsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/bankfeeds.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    BankFeedsApi apiInstance = new BankFeedsApi(defaultClient);
    String xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
    UUID id = UUID.randomUUID(); // UUID | Unique identifier for retrieving single object
    try {
      FeedConnection result = apiInstance.getFeedConnection(xeroTenantId, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BankFeedsApi#getFeedConnection");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **id** | **UUID**| Unique identifier for retrieving single object | |

### Return type

[**FeedConnection**](FeedConnection.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success returns a FeedConnection object matching the id in response |  -  |
| **400** | bad input parameter |  -  |

<a id="getFeedConnections"></a>
# **getFeedConnections**
> FeedConnections getFeedConnections(xeroTenantId, page, pageSize)

Searches for feed connections

By passing in the appropriate options, you can search for available feed connections in the system.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BankFeedsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/bankfeeds.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    BankFeedsApi apiInstance = new BankFeedsApi(defaultClient);
    String xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
    Integer page = 1; // Integer | Page number which specifies the set of records to retrieve. By default the number of the records per set is 10. Example - https://api.xero.com/bankfeeds.xro/1.0/FeedConnections?page=1 to get the second set of the records. When page value is not a number or a negative number, by default, the first set of records is returned.
    Integer pageSize = 100; // Integer | Page size which specifies how many records per page will be returned (default 10). Example - https://api.xero.com/bankfeeds.xro/1.0/FeedConnections?pageSize=100 to specify page size of 100.
    try {
      FeedConnections result = apiInstance.getFeedConnections(xeroTenantId, page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BankFeedsApi#getFeedConnections");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **page** | **Integer**| Page number which specifies the set of records to retrieve. By default the number of the records per set is 10. Example - https://api.xero.com/bankfeeds.xro/1.0/FeedConnections?page&#x3D;1 to get the second set of the records. When page value is not a number or a negative number, by default, the first set of records is returned. | [optional] |
| **pageSize** | **Integer**| Page size which specifies how many records per page will be returned (default 10). Example - https://api.xero.com/bankfeeds.xro/1.0/FeedConnections?pageSize&#x3D;100 to specify page size of 100. | [optional] |

### Return type

[**FeedConnections**](FeedConnections.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | search results matching criteria returned with pagination and items array |  -  |
| **400** | validation error response |  -  |

<a id="getStatement"></a>
# **getStatement**
> Statement getStatement(xeroTenantId, statementId, statementID)

Retrieve single statement based on unique id provided

By passing in a statement id, you can search for matching statements

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BankFeedsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/bankfeeds.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    BankFeedsApi apiInstance = new BankFeedsApi(defaultClient);
    String xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
    UUID statementId = UUID.randomUUID(); // UUID | statement id for single object
    String statementID = "statementID_example"; // String | 
    try {
      Statement result = apiInstance.getStatement(xeroTenantId, statementId, statementID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BankFeedsApi#getStatement");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **statementId** | **UUID**| statement id for single object | |
| **statementID** | **String**|  | |

### Return type

[**Statement**](Statement.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | search results matching id for single statement |  -  |
| **404** | Statement not found |  -  |

<a id="getStatements"></a>
# **getStatements**
> Statements getStatements(xeroTenantId, page, pageSize, xeroApplicationId, xeroUserId)

Retrieve all statements

By passing in parameters, you can search for matching statements

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BankFeedsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/bankfeeds.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    BankFeedsApi apiInstance = new BankFeedsApi(defaultClient);
    String xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
    Integer page = 56; // Integer | unique id for single object
    Integer pageSize = 56; // Integer | Page size which specifies how many records per page will be returned (default 10). Example - https://api.xero.com/bankfeeds.xro/1.0/Statements?pageSize=100 to specify page size of 100.
    String xeroApplicationId = "00000000-0000-0000-0000-0000000010000"; // String | 
    String xeroUserId = "00000000-0000-0000-0000-0000030000000"; // String | 
    try {
      Statements result = apiInstance.getStatements(xeroTenantId, page, pageSize, xeroApplicationId, xeroUserId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BankFeedsApi#getStatements");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **page** | **Integer**| unique id for single object | [optional] |
| **pageSize** | **Integer**| Page size which specifies how many records per page will be returned (default 10). Example - https://api.xero.com/bankfeeds.xro/1.0/Statements?pageSize&#x3D;100 to specify page size of 100. | [optional] |
| **xeroApplicationId** | **String**|  | [optional] [default to 00000000-0000-0000-0000-0000000010000] |
| **xeroUserId** | **String**|  | [optional] [default to 00000000-0000-0000-0000-0000030000000] |

### Return type

[**Statements**](Statements.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success returns Statements array of objects response |  -  |
| **400** | bad input parameter |  -  |

