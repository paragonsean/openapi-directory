# TaxApi

All URIs are relative to *https://www.envoice.in*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**taxApiAll**](TaxApi.md#taxApiAll) | **GET** /api/tax/all | Return all taxes for the account |
| [**taxApiDelete**](TaxApi.md#taxApiDelete) | **POST** /api/tax/delete | Delete an existing tax |
| [**taxApiNew**](TaxApi.md#taxApiNew) | **POST** /api/tax/new | Create a tax |
| [**taxApiUpdate**](TaxApi.md#taxApiUpdate) | **POST** /api/tax/update | Update an existing tax |


<a id="taxApiAll"></a>
# **taxApiAll**
> List&lt;TaxDetailsApiModel&gt; taxApiAll(xAuthKey, xAuthSecret)

Return all taxes for the account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaxApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.envoice.in");

    TaxApi apiInstance = new TaxApi(defaultClient);
    String xAuthKey = "[authentication key]"; // String | 
    String xAuthSecret = "[authentication secret]"; // String | 
    try {
      List<TaxDetailsApiModel> result = apiInstance.taxApiAll(xAuthKey, xAuthSecret);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaxApi#taxApiAll");
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
| **xAuthKey** | **String**|  | [default to [authentication key]] |
| **xAuthSecret** | **String**|  | [default to [authentication secret]] |

### Return type

[**List&lt;TaxDetailsApiModel&gt;**](TaxDetailsApiModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/html, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="taxApiDelete"></a>
# **taxApiDelete**
> Integer taxApiDelete(xAuthKey, xAuthSecret, taxDeleteApiModel)

Delete an existing tax

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaxApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.envoice.in");

    TaxApi apiInstance = new TaxApi(defaultClient);
    String xAuthKey = "[authentication key]"; // String | 
    String xAuthSecret = "[authentication secret]"; // String | 
    TaxDeleteApiModel taxDeleteApiModel = new TaxDeleteApiModel(); // TaxDeleteApiModel | 
    try {
      Integer result = apiInstance.taxApiDelete(xAuthKey, xAuthSecret, taxDeleteApiModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaxApi#taxApiDelete");
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
| **xAuthKey** | **String**|  | [default to [authentication key]] |
| **xAuthSecret** | **String**|  | [default to [authentication secret]] |
| **taxDeleteApiModel** | [**TaxDeleteApiModel**](TaxDeleteApiModel.md)|  | |

### Return type

**Integer**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
 - **Accept**: application/json, application/xml, text/html, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="taxApiNew"></a>
# **taxApiNew**
> Integer taxApiNew(xAuthKey, xAuthSecret, taxCreateApiModel)

Create a tax

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaxApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.envoice.in");

    TaxApi apiInstance = new TaxApi(defaultClient);
    String xAuthKey = "[authentication key]"; // String | 
    String xAuthSecret = "[authentication secret]"; // String | 
    TaxCreateApiModel taxCreateApiModel = new TaxCreateApiModel(); // TaxCreateApiModel | 
    try {
      Integer result = apiInstance.taxApiNew(xAuthKey, xAuthSecret, taxCreateApiModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaxApi#taxApiNew");
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
| **xAuthKey** | **String**|  | [default to [authentication key]] |
| **xAuthSecret** | **String**|  | [default to [authentication secret]] |
| **taxCreateApiModel** | [**TaxCreateApiModel**](TaxCreateApiModel.md)|  | |

### Return type

**Integer**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
 - **Accept**: application/json, application/xml, text/html, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="taxApiUpdate"></a>
# **taxApiUpdate**
> taxApiUpdate(xAuthKey, xAuthSecret, taxUpdateApiModel)

Update an existing tax

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaxApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.envoice.in");

    TaxApi apiInstance = new TaxApi(defaultClient);
    String xAuthKey = "[authentication key]"; // String | 
    String xAuthSecret = "[authentication secret]"; // String | 
    TaxUpdateApiModel taxUpdateApiModel = new TaxUpdateApiModel(); // TaxUpdateApiModel | 
    try {
      apiInstance.taxApiUpdate(xAuthKey, xAuthSecret, taxUpdateApiModel);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaxApi#taxApiUpdate");
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
| **xAuthKey** | **String**|  | [default to [authentication key]] |
| **xAuthSecret** | **String**|  | [default to [authentication secret]] |
| **taxUpdateApiModel** | [**TaxUpdateApiModel**](TaxUpdateApiModel.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

