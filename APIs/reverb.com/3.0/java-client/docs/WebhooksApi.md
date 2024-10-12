# WebhooksApi

All URIs are relative to *https://api.reverb.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**webhooksRegistrationsGet**](WebhooksApi.md#webhooksRegistrationsGet) | **GET** /webhooks/registrations | Get webhook registrations |
| [**webhooksRegistrationsIdDelete**](WebhooksApi.md#webhooksRegistrationsIdDelete) | **DELETE** /webhooks/registrations/{id} | Remove a webhook |
| [**webhooksRegistrationsIdGet**](WebhooksApi.md#webhooksRegistrationsIdGet) | **GET** /webhooks/registrations/{id} | Get details of a webhook registration |
| [**webhooksRegistrationsPost**](WebhooksApi.md#webhooksRegistrationsPost) | **POST** /webhooks/registrations | Register a webhook |


<a id="webhooksRegistrationsGet"></a>
# **webhooksRegistrationsGet**
> webhooksRegistrationsGet()

Get webhook registrations

Get webhook registrations

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    try {
      apiInstance.webhooksRegistrationsGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#webhooksRegistrationsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

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
| **0** | Unexpected error |  -  |

<a id="webhooksRegistrationsIdDelete"></a>
# **webhooksRegistrationsIdDelete**
> webhooksRegistrationsIdDelete(id)

Remove a webhook

Remove a webhook

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.webhooksRegistrationsIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#webhooksRegistrationsIdDelete");
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
| **id** | **String**|  | |

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
| **0** | Unexpected error |  -  |

<a id="webhooksRegistrationsIdGet"></a>
# **webhooksRegistrationsIdGet**
> webhooksRegistrationsIdGet(id)

Get details of a webhook registration

Get details of a webhook registration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.webhooksRegistrationsIdGet(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#webhooksRegistrationsIdGet");
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
| **id** | **String**|  | |

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
| **0** | Unexpected error |  -  |

<a id="webhooksRegistrationsPost"></a>
# **webhooksRegistrationsPost**
> webhooksRegistrationsPost(webhooksRegistrationsPostRequest)

Register a webhook

Register a webhook

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    WebhooksRegistrationsPostRequest webhooksRegistrationsPostRequest = new WebhooksRegistrationsPostRequest(); // WebhooksRegistrationsPostRequest | the content of the request
    try {
      apiInstance.webhooksRegistrationsPost(webhooksRegistrationsPostRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#webhooksRegistrationsPost");
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
| **webhooksRegistrationsPostRequest** | [**WebhooksRegistrationsPostRequest**](WebhooksRegistrationsPostRequest.md)| the content of the request | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

