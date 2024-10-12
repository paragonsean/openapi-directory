# PromotionsApi

All URIs are relative to *https://api.jumpseller.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**promotionsIdJsonDelete**](PromotionsApi.md#promotionsIdJsonDelete) | **DELETE** /promotions/{id}.json | Delete an existing Promotion. |
| [**promotionsIdJsonGet**](PromotionsApi.md#promotionsIdJsonGet) | **GET** /promotions/{id}.json | Retrieve a single Promotion. |
| [**promotionsIdJsonPut**](PromotionsApi.md#promotionsIdJsonPut) | **PUT** /promotions/{id}.json | Update a Promotion. |
| [**promotionsJsonGet**](PromotionsApi.md#promotionsJsonGet) | **GET** /promotions.json | Retrieve all Promotions. |
| [**promotionsJsonPost**](PromotionsApi.md#promotionsJsonPost) | **POST** /promotions.json | Create a new Promotion. |


<a id="promotionsIdJsonDelete"></a>
# **promotionsIdJsonDelete**
> String promotionsIdJsonDelete(login, authtoken, id)

Delete an existing Promotion.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PromotionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    PromotionsApi apiInstance = new PromotionsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the Promotion
    try {
      String result = apiInstance.promotionsIdJsonDelete(login, authtoken, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PromotionsApi#promotionsIdJsonDelete");
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
| **id** | **Integer**| Id of the Promotion | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Promotion Not Found. |  -  |

<a id="promotionsIdJsonGet"></a>
# **promotionsIdJsonGet**
> Promotion promotionsIdJsonGet(login, authtoken, id)

Retrieve a single Promotion.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PromotionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    PromotionsApi apiInstance = new PromotionsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the Promotion
    try {
      Promotion result = apiInstance.promotionsIdJsonGet(login, authtoken, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PromotionsApi#promotionsIdJsonGet");
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
| **id** | **Integer**| Id of the Promotion | |

### Return type

[**Promotion**](Promotion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Promotion Not Found. |  -  |

<a id="promotionsIdJsonPut"></a>
# **promotionsIdJsonPut**
> Promotion promotionsIdJsonPut(login, authtoken, id, promotionEdit)

Update a Promotion.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PromotionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    PromotionsApi apiInstance = new PromotionsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the Promotion
    PromotionEdit promotionEdit = new PromotionEdit(); // PromotionEdit | Promotion parameters.
    try {
      Promotion result = apiInstance.promotionsIdJsonPut(login, authtoken, id, promotionEdit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PromotionsApi#promotionsIdJsonPut");
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
| **id** | **Integer**| Id of the Promotion | |
| **promotionEdit** | [**PromotionEdit**](PromotionEdit.md)| Promotion parameters. | |

### Return type

[**Promotion**](Promotion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Promotion Not Found. |  -  |

<a id="promotionsJsonGet"></a>
# **promotionsJsonGet**
> List&lt;Promotion&gt; promotionsJsonGet(login, authtoken, limit, page)

Retrieve all Promotions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PromotionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    PromotionsApi apiInstance = new PromotionsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer limit = 56; // Integer | Promotions' list restriction (default: 50 | max: 200).
    Integer page = 56; // Integer | Promotions' list page (default: 1).
    try {
      List<Promotion> result = apiInstance.promotionsJsonGet(login, authtoken, limit, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PromotionsApi#promotionsJsonGet");
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
| **limit** | **Integer**| Promotions&#39; list restriction (default: 50 | max: 200). | [optional] |
| **page** | **Integer**| Promotions&#39; list page (default: 1). | [optional] |

### Return type

[**List&lt;Promotion&gt;**](Promotion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of Promotions |  -  |

<a id="promotionsJsonPost"></a>
# **promotionsJsonPost**
> Promotion promotionsJsonPost(login, authtoken, promotionEdit)

Create a new Promotion.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PromotionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    PromotionsApi apiInstance = new PromotionsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    PromotionEdit promotionEdit = new PromotionEdit(); // PromotionEdit | Promotion parameters.
    try {
      Promotion result = apiInstance.promotionsJsonPost(login, authtoken, promotionEdit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PromotionsApi#promotionsJsonPost");
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
| **promotionEdit** | [**PromotionEdit**](PromotionEdit.md)| Promotion parameters. | |

### Return type

[**Promotion**](Promotion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Promotion Not Found. |  -  |

