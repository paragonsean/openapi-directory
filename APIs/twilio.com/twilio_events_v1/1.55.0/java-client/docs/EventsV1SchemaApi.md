# EventsV1SchemaApi

All URIs are relative to *https://events.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchSchema**](EventsV1SchemaApi.md#fetchSchema) | **GET** /v1/Schemas/{Id} |  |


<a id="fetchSchema"></a>
# **fetchSchema**
> EventsV1Schema fetchSchema(id)



Fetch a specific schema with its nested versions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsV1SchemaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://events.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    EventsV1SchemaApi apiInstance = new EventsV1SchemaApi(defaultClient);
    String id = "id_example"; // String | The unique identifier of the schema. Each schema can have multiple versions, that share the same id.
    try {
      EventsV1Schema result = apiInstance.fetchSchema(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsV1SchemaApi#fetchSchema");
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

### Return type

[**EventsV1Schema**](EventsV1Schema.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

