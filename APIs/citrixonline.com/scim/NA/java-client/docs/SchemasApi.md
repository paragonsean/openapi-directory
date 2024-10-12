# SchemasApi

All URIs are relative to *https://api.citrixonline.com/identity/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getServiceProviderConfigs**](SchemasApi.md#getServiceProviderConfigs) | **GET** /ServiceProviderConfigs | Get Service Provider Configurations |
| [**getUserSchema**](SchemasApi.md#getUserSchema) | **GET** /Schemas/Users | Get User Schema |


<a id="getServiceProviderConfigs"></a>
# **getServiceProviderConfigs**
> ServiceProviderConfigs getServiceProviderConfigs(authorization)

Get Service Provider Configurations

Queries service provider configurations. The service provider configurations are defined in SCIM Core Schema (http://www.simplecloud.info/specs/draft-scim-core-schema-01.html#anchor6). This call returns a description, a documentationURL, name, and specURL.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SchemasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.citrixonline.com/identity/v1");

    SchemasApi apiInstance = new SchemasApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token prefixed with 'Bearer ', e.g. 'Bearer 123456abcdef'
    try {
      ServiceProviderConfigs result = apiInstance.getServiceProviderConfigs(authorization);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SchemasApi#getServiceProviderConfigs");
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
| **authorization** | **String**| Access token prefixed with &#39;Bearer &#39;, e.g. &#39;Bearer 123456abcdef&#39; | |

### Return type

[**ServiceProviderConfigs**](ServiceProviderConfigs.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request has succeeded. |  -  |
| **403** | Invalid token passed |  -  |
| **502** | Authentication or account gateway error occurred |  -  |
| **504** | Authentication or account gateway timeout occurred |  -  |

<a id="getUserSchema"></a>
# **getUserSchema**
> ResourceSchema getUserSchema(authorization)

Get User Schema

Queries the user schema. The user schema is defined in SCIM Core Schema (http://www.simplecloud.info/specs/draft-scim-core-schema-01.html#resource-schema).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SchemasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.citrixonline.com/identity/v1");

    SchemasApi apiInstance = new SchemasApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token prefixed with 'Bearer ', e.g. 'Bearer 123456abcdef'
    try {
      ResourceSchema result = apiInstance.getUserSchema(authorization);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SchemasApi#getUserSchema");
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
| **authorization** | **String**| Access token prefixed with &#39;Bearer &#39;, e.g. &#39;Bearer 123456abcdef&#39; | |

### Return type

[**ResourceSchema**](ResourceSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request has succeeded. |  -  |
| **403** | Invalid token passed |  -  |
| **502** | Authentication or account gateway error occurred |  -  |
| **504** | Authentication or account gateway timeout occurred |  -  |

