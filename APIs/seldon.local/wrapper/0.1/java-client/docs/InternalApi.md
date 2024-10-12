# InternalApi

All URIs are relative to *http://seldon.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**aggregate**](InternalApi.md#aggregate) | **GET** /aggregate |  |
| [**aggregate2**](InternalApi.md#aggregate2) | **POST** /aggregate |  |
| [**route**](InternalApi.md#route) | **POST** /route |  |
| [**route2**](InternalApi.md#route2) | **GET** /route |  |
| [**sendFeedback**](InternalApi.md#sendFeedback) | **POST** /send-feedback |  |
| [**sendFeedback2**](InternalApi.md#sendFeedback2) | **GET** /send-feedback |  |
| [**transformInput**](InternalApi.md#transformInput) | **POST** /transform-input |  |
| [**transformInput2**](InternalApi.md#transformInput2) | **GET** /transform-input |  |
| [**transformInput3**](InternalApi.md#transformInput3) | **POST** /predict |  |
| [**transformInput4**](InternalApi.md#transformInput4) | **GET** /predict |  |
| [**transformOutput**](InternalApi.md#transformOutput) | **POST** /transform-output |  |
| [**transformOutput2**](InternalApi.md#transformOutput2) | **GET** /transform-output |  |


<a id="aggregate"></a>
# **aggregate**
> SeldonMessage aggregate(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InternalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://seldon.local");

    InternalApi apiInstance = new InternalApi(defaultClient);
    SeldonMessageList body = new SeldonMessageList(); // SeldonMessageList | 
    try {
      SeldonMessage result = apiInstance.aggregate(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InternalApi#aggregate");
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
| **body** | [**SeldonMessageList**](.md)|  | |

### Return type

[**SeldonMessage**](SeldonMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful response. |  -  |

<a id="aggregate2"></a>
# **aggregate2**
> SeldonMessage aggregate2(json)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InternalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://seldon.local");

    InternalApi apiInstance = new InternalApi(defaultClient);
    SeldonMessageList json = new SeldonMessageList(); // SeldonMessageList | 
    try {
      SeldonMessage result = apiInstance.aggregate2(json);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InternalApi#aggregate2");
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
| **json** | [**SeldonMessageList**](SeldonMessageList.md)|  | [optional] |

### Return type

[**SeldonMessage**](SeldonMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful response. |  -  |

<a id="route"></a>
# **route**
> SeldonMessage route(json)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InternalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://seldon.local");

    InternalApi apiInstance = new InternalApi(defaultClient);
    SeldonMessage json = new SeldonMessage(); // SeldonMessage | 
    try {
      SeldonMessage result = apiInstance.route(json);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InternalApi#route");
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
| **json** | [**SeldonMessage**](SeldonMessage.md)|  | [optional] |

### Return type

[**SeldonMessage**](SeldonMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful response. |  -  |

<a id="route2"></a>
# **route2**
> SeldonMessage route2(json)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InternalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://seldon.local");

    InternalApi apiInstance = new InternalApi(defaultClient);
    SeldonMessage json = new SeldonMessage(); // SeldonMessage | 
    try {
      SeldonMessage result = apiInstance.route2(json);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InternalApi#route2");
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
| **json** | [**SeldonMessage**](.md)|  | |

### Return type

[**SeldonMessage**](SeldonMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful response. |  -  |

<a id="sendFeedback"></a>
# **sendFeedback**
> SeldonMessage sendFeedback(json)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InternalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://seldon.local");

    InternalApi apiInstance = new InternalApi(defaultClient);
    Feedback json = new Feedback(); // Feedback | 
    try {
      SeldonMessage result = apiInstance.sendFeedback(json);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InternalApi#sendFeedback");
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
| **json** | [**Feedback**](Feedback.md)|  | [optional] |

### Return type

[**SeldonMessage**](SeldonMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful response. |  -  |

<a id="sendFeedback2"></a>
# **sendFeedback2**
> SeldonMessage sendFeedback2(json)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InternalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://seldon.local");

    InternalApi apiInstance = new InternalApi(defaultClient);
    Feedback json = new Feedback(); // Feedback | 
    try {
      SeldonMessage result = apiInstance.sendFeedback2(json);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InternalApi#sendFeedback2");
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
| **json** | [**Feedback**](.md)|  | |

### Return type

[**SeldonMessage**](SeldonMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful response. |  -  |

<a id="transformInput"></a>
# **transformInput**
> SeldonMessage transformInput(json)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InternalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://seldon.local");

    InternalApi apiInstance = new InternalApi(defaultClient);
    SeldonMessage json = new SeldonMessage(); // SeldonMessage | 
    try {
      SeldonMessage result = apiInstance.transformInput(json);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InternalApi#transformInput");
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
| **json** | [**SeldonMessage**](SeldonMessage.md)|  | [optional] |

### Return type

[**SeldonMessage**](SeldonMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful response. |  -  |

<a id="transformInput2"></a>
# **transformInput2**
> SeldonMessage transformInput2(json)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InternalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://seldon.local");

    InternalApi apiInstance = new InternalApi(defaultClient);
    SeldonMessage json = new SeldonMessage(); // SeldonMessage | 
    try {
      SeldonMessage result = apiInstance.transformInput2(json);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InternalApi#transformInput2");
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
| **json** | [**SeldonMessage**](.md)|  | |

### Return type

[**SeldonMessage**](SeldonMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful response. |  -  |

<a id="transformInput3"></a>
# **transformInput3**
> SeldonMessage transformInput3(json)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InternalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://seldon.local");

    InternalApi apiInstance = new InternalApi(defaultClient);
    SeldonMessage json = new SeldonMessage(); // SeldonMessage | 
    try {
      SeldonMessage result = apiInstance.transformInput3(json);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InternalApi#transformInput3");
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
| **json** | [**SeldonMessage**](SeldonMessage.md)|  | [optional] |

### Return type

[**SeldonMessage**](SeldonMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful response. |  -  |

<a id="transformInput4"></a>
# **transformInput4**
> SeldonMessage transformInput4(json)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InternalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://seldon.local");

    InternalApi apiInstance = new InternalApi(defaultClient);
    SeldonMessage json = new SeldonMessage(); // SeldonMessage | 
    try {
      SeldonMessage result = apiInstance.transformInput4(json);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InternalApi#transformInput4");
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
| **json** | [**SeldonMessage**](.md)|  | |

### Return type

[**SeldonMessage**](SeldonMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful response. |  -  |

<a id="transformOutput"></a>
# **transformOutput**
> SeldonMessage transformOutput(json)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InternalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://seldon.local");

    InternalApi apiInstance = new InternalApi(defaultClient);
    SeldonMessage json = new SeldonMessage(); // SeldonMessage | 
    try {
      SeldonMessage result = apiInstance.transformOutput(json);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InternalApi#transformOutput");
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
| **json** | [**SeldonMessage**](SeldonMessage.md)|  | [optional] |

### Return type

[**SeldonMessage**](SeldonMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful response. |  -  |

<a id="transformOutput2"></a>
# **transformOutput2**
> SeldonMessage transformOutput2(json)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InternalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://seldon.local");

    InternalApi apiInstance = new InternalApi(defaultClient);
    SeldonMessage json = new SeldonMessage(); // SeldonMessage | 
    try {
      SeldonMessage result = apiInstance.transformOutput2(json);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InternalApi#transformOutput2");
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
| **json** | [**SeldonMessage**](.md)|  | |

### Return type

[**SeldonMessage**](SeldonMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful response. |  -  |

