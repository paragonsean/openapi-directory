# EventsV1SchemaVersionApi

All URIs are relative to *https://events.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchSchemaVersion**](EventsV1SchemaVersionApi.md#fetchSchemaVersion) | **GET** /v1/Schemas/{Id}/Versions/{SchemaVersion} |  |
| [**listSchemaVersion**](EventsV1SchemaVersionApi.md#listSchemaVersion) | **GET** /v1/Schemas/{Id}/Versions |  |


<a id="fetchSchemaVersion"></a>
# **fetchSchemaVersion**
> EventsV1SchemaSchemaVersion fetchSchemaVersion(id, schemaVersion)



Fetch a specific schema and version.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsV1SchemaVersionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://events.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    EventsV1SchemaVersionApi apiInstance = new EventsV1SchemaVersionApi(defaultClient);
    String id = "id_example"; // String | The unique identifier of the schema. Each schema can have multiple versions, that share the same id.
    Integer schemaVersion = 56; // Integer | The version of the schema
    try {
      EventsV1SchemaSchemaVersion result = apiInstance.fetchSchemaVersion(id, schemaVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsV1SchemaVersionApi#fetchSchemaVersion");
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
| **id** | **String**| The unique identifier of the schema. Each schema can have multiple versions, that share the same id. | |
| **schemaVersion** | **Integer**| The version of the schema | |

### Return type

[**EventsV1SchemaSchemaVersion**](EventsV1SchemaSchemaVersion.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listSchemaVersion"></a>
# **listSchemaVersion**
> ListSchemaVersionResponse listSchemaVersion(id, pageSize, page, pageToken)



Retrieve a paginated list of versions of the schema.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsV1SchemaVersionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://events.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    EventsV1SchemaVersionApi apiInstance = new EventsV1SchemaVersionApi(defaultClient);
    String id = "id_example"; // String | The unique identifier of the schema. Each schema can have multiple versions, that share the same id.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListSchemaVersionResponse result = apiInstance.listSchemaVersion(id, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsV1SchemaVersionApi#listSchemaVersion");
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
| **id** | **String**| The unique identifier of the schema. Each schema can have multiple versions, that share the same id. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListSchemaVersionResponse**](ListSchemaVersionResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

