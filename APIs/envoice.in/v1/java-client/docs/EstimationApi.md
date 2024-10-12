# EstimationApi

All URIs are relative to *https://www.envoice.in*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**estimationApiAll**](EstimationApi.md#estimationApiAll) | **GET** /api/estimation/all | Return all estimation for the account |
| [**estimationApiChangeStatus**](EstimationApi.md#estimationApiChangeStatus) | **POST** /api/estimation/changestatus | Change estimation status |
| [**estimationApiConvert**](EstimationApi.md#estimationApiConvert) | **POST** /api/estimation/convert | Convert the estimation to an invoice |
| [**estimationApiDelete**](EstimationApi.md#estimationApiDelete) | **POST** /api/estimation/delete | Delete an existing estimation |
| [**estimationApiDetails**](EstimationApi.md#estimationApiDetails) | **GET** /api/estimation/details | Return estimation data |
| [**estimationApiNew**](EstimationApi.md#estimationApiNew) | **POST** /api/estimation/new | Create an estimation |
| [**estimationApiSendToClient**](EstimationApi.md#estimationApiSendToClient) | **POST** /api/estimation/sendtoclient | Send the provided estimation to the client |
| [**estimationApiStatus**](EstimationApi.md#estimationApiStatus) | **GET** /api/estimation/status | Retrieve the status of the estimation |
| [**estimationApiUpdate**](EstimationApi.md#estimationApiUpdate) | **POST** /api/estimation/update | Update an existing estimation |
| [**estimationApiUri**](EstimationApi.md#estimationApiUri) | **GET** /api/estimation/uri | Return the unique url to the client&#39;s invoice |


<a id="estimationApiAll"></a>
# **estimationApiAll**
> ListResultEstimationDetailsApiModel estimationApiAll(xAuthKey, xAuthSecret, queryOptionsPage, queryOptionsPageSize)

Return all estimation for the account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EstimationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.envoice.in");

    EstimationApi apiInstance = new EstimationApi(defaultClient);
    String xAuthKey = "[authentication key]"; // String | 
    String xAuthSecret = "[authentication secret]"; // String | 
    Integer queryOptionsPage = 56; // Integer | 
    Integer queryOptionsPageSize = 56; // Integer | 
    try {
      ListResultEstimationDetailsApiModel result = apiInstance.estimationApiAll(xAuthKey, xAuthSecret, queryOptionsPage, queryOptionsPageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EstimationApi#estimationApiAll");
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
| **queryOptionsPage** | **Integer**|  | [optional] |
| **queryOptionsPageSize** | **Integer**|  | [optional] |

### Return type

[**ListResultEstimationDetailsApiModel**](ListResultEstimationDetailsApiModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/html, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="estimationApiChangeStatus"></a>
# **estimationApiChangeStatus**
> Boolean estimationApiChangeStatus(xAuthKey, xAuthSecret, estimationChangeStatusApiModel)

Change estimation status

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EstimationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.envoice.in");

    EstimationApi apiInstance = new EstimationApi(defaultClient);
    String xAuthKey = "[authentication key]"; // String | 
    String xAuthSecret = "[authentication secret]"; // String | 
    EstimationChangeStatusApiModel estimationChangeStatusApiModel = new EstimationChangeStatusApiModel(); // EstimationChangeStatusApiModel | 
    try {
      Boolean result = apiInstance.estimationApiChangeStatus(xAuthKey, xAuthSecret, estimationChangeStatusApiModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EstimationApi#estimationApiChangeStatus");
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
| **estimationChangeStatusApiModel** | [**EstimationChangeStatusApiModel**](EstimationChangeStatusApiModel.md)|  | |

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
 - **Accept**: application/json, application/xml, text/html, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="estimationApiConvert"></a>
# **estimationApiConvert**
> InvoiceFullDetailsApiModel estimationApiConvert(xAuthKey, xAuthSecret, body)

Convert the estimation to an invoice

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EstimationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.envoice.in");

    EstimationApi apiInstance = new EstimationApi(defaultClient);
    String xAuthKey = "[authentication key]"; // String | 
    String xAuthSecret = "[authentication secret]"; // String | 
    Integer body = 56; // Integer | 
    try {
      InvoiceFullDetailsApiModel result = apiInstance.estimationApiConvert(xAuthKey, xAuthSecret, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EstimationApi#estimationApiConvert");
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
| **body** | **Integer**|  | |

### Return type

[**InvoiceFullDetailsApiModel**](InvoiceFullDetailsApiModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
 - **Accept**: application/json, application/xml, text/html, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="estimationApiDelete"></a>
# **estimationApiDelete**
> Integer estimationApiDelete(xAuthKey, xAuthSecret, estimationDeleteApiModel)

Delete an existing estimation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EstimationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.envoice.in");

    EstimationApi apiInstance = new EstimationApi(defaultClient);
    String xAuthKey = "[authentication key]"; // String | 
    String xAuthSecret = "[authentication secret]"; // String | 
    EstimationDeleteApiModel estimationDeleteApiModel = new EstimationDeleteApiModel(); // EstimationDeleteApiModel | 
    try {
      Integer result = apiInstance.estimationApiDelete(xAuthKey, xAuthSecret, estimationDeleteApiModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EstimationApi#estimationApiDelete");
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
| **estimationDeleteApiModel** | [**EstimationDeleteApiModel**](EstimationDeleteApiModel.md)|  | |

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

<a id="estimationApiDetails"></a>
# **estimationApiDetails**
> EstimationFullDetailsApiModel estimationApiDetails(id, xAuthKey, xAuthSecret)

Return estimation data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EstimationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.envoice.in");

    EstimationApi apiInstance = new EstimationApi(defaultClient);
    Integer id = 56; // Integer | 
    String xAuthKey = "[authentication key]"; // String | 
    String xAuthSecret = "[authentication secret]"; // String | 
    try {
      EstimationFullDetailsApiModel result = apiInstance.estimationApiDetails(id, xAuthKey, xAuthSecret);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EstimationApi#estimationApiDetails");
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
| **id** | **Integer**|  | |
| **xAuthKey** | **String**|  | [default to [authentication key]] |
| **xAuthSecret** | **String**|  | [default to [authentication secret]] |

### Return type

[**EstimationFullDetailsApiModel**](EstimationFullDetailsApiModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/html, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="estimationApiNew"></a>
# **estimationApiNew**
> EstimationFullDetailsApiModel estimationApiNew(xAuthKey, xAuthSecret, estimationCreateApiModel)

Create an estimation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EstimationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.envoice.in");

    EstimationApi apiInstance = new EstimationApi(defaultClient);
    String xAuthKey = "[authentication key]"; // String | 
    String xAuthSecret = "[authentication secret]"; // String | 
    EstimationCreateApiModel estimationCreateApiModel = new EstimationCreateApiModel(); // EstimationCreateApiModel | 
    try {
      EstimationFullDetailsApiModel result = apiInstance.estimationApiNew(xAuthKey, xAuthSecret, estimationCreateApiModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EstimationApi#estimationApiNew");
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
| **estimationCreateApiModel** | [**EstimationCreateApiModel**](EstimationCreateApiModel.md)|  | |

### Return type

[**EstimationFullDetailsApiModel**](EstimationFullDetailsApiModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
 - **Accept**: application/json, application/xml, text/html, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="estimationApiSendToClient"></a>
# **estimationApiSendToClient**
> Integer estimationApiSendToClient(xAuthKey, xAuthSecret, sendEstimationToClientApiModel)

Send the provided estimation to the client

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EstimationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.envoice.in");

    EstimationApi apiInstance = new EstimationApi(defaultClient);
    String xAuthKey = "[authentication key]"; // String | 
    String xAuthSecret = "[authentication secret]"; // String | 
    SendEstimationToClientApiModel sendEstimationToClientApiModel = new SendEstimationToClientApiModel(); // SendEstimationToClientApiModel | 
    try {
      Integer result = apiInstance.estimationApiSendToClient(xAuthKey, xAuthSecret, sendEstimationToClientApiModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EstimationApi#estimationApiSendToClient");
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
| **sendEstimationToClientApiModel** | [**SendEstimationToClientApiModel**](SendEstimationToClientApiModel.md)|  | |

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

<a id="estimationApiStatus"></a>
# **estimationApiStatus**
> String estimationApiStatus(id, xAuthKey, xAuthSecret)

Retrieve the status of the estimation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EstimationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.envoice.in");

    EstimationApi apiInstance = new EstimationApi(defaultClient);
    Integer id = 56; // Integer | 
    String xAuthKey = "[authentication key]"; // String | 
    String xAuthSecret = "[authentication secret]"; // String | 
    try {
      String result = apiInstance.estimationApiStatus(id, xAuthKey, xAuthSecret);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EstimationApi#estimationApiStatus");
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
| **id** | **Integer**|  | |
| **xAuthKey** | **String**|  | [default to [authentication key]] |
| **xAuthSecret** | **String**|  | [default to [authentication secret]] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/html, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="estimationApiUpdate"></a>
# **estimationApiUpdate**
> EstimationFullDetailsApiModel estimationApiUpdate(xAuthKey, xAuthSecret, estimationUpdateApiModel)

Update an existing estimation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EstimationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.envoice.in");

    EstimationApi apiInstance = new EstimationApi(defaultClient);
    String xAuthKey = "[authentication key]"; // String | 
    String xAuthSecret = "[authentication secret]"; // String | 
    EstimationUpdateApiModel estimationUpdateApiModel = new EstimationUpdateApiModel(); // EstimationUpdateApiModel | 
    try {
      EstimationFullDetailsApiModel result = apiInstance.estimationApiUpdate(xAuthKey, xAuthSecret, estimationUpdateApiModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EstimationApi#estimationApiUpdate");
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
| **estimationUpdateApiModel** | [**EstimationUpdateApiModel**](EstimationUpdateApiModel.md)|  | |

### Return type

[**EstimationFullDetailsApiModel**](EstimationFullDetailsApiModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
 - **Accept**: application/json, application/xml, text/html, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="estimationApiUri"></a>
# **estimationApiUri**
> EstimationUriApiModel estimationApiUri(id, xAuthKey, xAuthSecret)

Return the unique url to the client&#39;s invoice

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EstimationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.envoice.in");

    EstimationApi apiInstance = new EstimationApi(defaultClient);
    Integer id = 56; // Integer | 
    String xAuthKey = "[authentication key]"; // String | 
    String xAuthSecret = "[authentication secret]"; // String | 
    try {
      EstimationUriApiModel result = apiInstance.estimationApiUri(id, xAuthKey, xAuthSecret);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EstimationApi#estimationApiUri");
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
| **id** | **Integer**|  | |
| **xAuthKey** | **String**|  | [default to [authentication key]] |
| **xAuthSecret** | **String**|  | [default to [authentication secret]] |

### Return type

[**EstimationUriApiModel**](EstimationUriApiModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/html, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

