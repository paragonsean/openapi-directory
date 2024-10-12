# FulfillmentsApi

All URIs are relative to *https://api.jumpseller.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fulfillmentsCountJsonGet**](FulfillmentsApi.md#fulfillmentsCountJsonGet) | **GET** /fulfillments/count.json | Count all Fulfillments. |
| [**fulfillmentsIdJsonGet**](FulfillmentsApi.md#fulfillmentsIdJsonGet) | **GET** /fulfillments/{id}.json | Retrieve a single Fulfillment. |
| [**fulfillmentsJsonGet**](FulfillmentsApi.md#fulfillmentsJsonGet) | **GET** /fulfillments.json | Retrieve all Fulfillments. |
| [**orderIdFulfillmentsJsonGet**](FulfillmentsApi.md#orderIdFulfillmentsJsonGet) | **GET** /order/{id}/fulfillments.json | Retrieve the Fulfillments associated with the Order. |


<a id="fulfillmentsCountJsonGet"></a>
# **fulfillmentsCountJsonGet**
> Count fulfillmentsCountJsonGet(login, authtoken)

Count all Fulfillments.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FulfillmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    FulfillmentsApi apiInstance = new FulfillmentsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    try {
      Count result = apiInstance.fulfillmentsCountJsonGet(login, authtoken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FulfillmentsApi#fulfillmentsCountJsonGet");
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
| **login** | **String**| API OAuth login. | |
| **authtoken** | **String**| API OAuth token. | |

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

<a id="fulfillmentsIdJsonGet"></a>
# **fulfillmentsIdJsonGet**
> Fulfillment fulfillmentsIdJsonGet(login, authtoken, id)

Retrieve a single Fulfillment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FulfillmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    FulfillmentsApi apiInstance = new FulfillmentsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the Fulfillment
    try {
      Fulfillment result = apiInstance.fulfillmentsIdJsonGet(login, authtoken, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FulfillmentsApi#fulfillmentsIdJsonGet");
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
| **login** | **String**| API OAuth login. | |
| **authtoken** | **String**| API OAuth token. | |
| **id** | **Integer**| Id of the Fulfillment | |

### Return type

[**Fulfillment**](Fulfillment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Fulfillment Not Found. |  -  |

<a id="fulfillmentsJsonGet"></a>
# **fulfillmentsJsonGet**
> List&lt;Fulfillment&gt; fulfillmentsJsonGet(login, authtoken, limit, page)

Retrieve all Fulfillments.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FulfillmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    FulfillmentsApi apiInstance = new FulfillmentsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer limit = 50; // Integer | List restriction
    Integer page = 1; // Integer | List page
    try {
      List<Fulfillment> result = apiInstance.fulfillmentsJsonGet(login, authtoken, limit, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FulfillmentsApi#fulfillmentsJsonGet");
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
| **login** | **String**| API OAuth login. | |
| **authtoken** | **String**| API OAuth token. | |
| **limit** | **Integer**| List restriction | [optional] [default to 50] |
| **page** | **Integer**| List page | [optional] [default to 1] |

### Return type

[**List&lt;Fulfillment&gt;**](Fulfillment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of Fulfillments |  -  |

<a id="orderIdFulfillmentsJsonGet"></a>
# **orderIdFulfillmentsJsonGet**
> List&lt;Fulfillment&gt; orderIdFulfillmentsJsonGet(login, authtoken, id)

Retrieve the Fulfillments associated with the Order.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FulfillmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    FulfillmentsApi apiInstance = new FulfillmentsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the Order
    try {
      List<Fulfillment> result = apiInstance.orderIdFulfillmentsJsonGet(login, authtoken, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FulfillmentsApi#orderIdFulfillmentsJsonGet");
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
| **login** | **String**| API OAuth login. | |
| **authtoken** | **String**| API OAuth token. | |
| **id** | **Integer**| Id of the Order | |

### Return type

[**List&lt;Fulfillment&gt;**](Fulfillment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Fulfillment Not Found. |  -  |

