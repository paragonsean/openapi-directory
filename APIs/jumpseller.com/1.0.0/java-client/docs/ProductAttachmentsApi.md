# ProductAttachmentsApi

All URIs are relative to *https://api.jumpseller.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**productsIdAttachmentsAttachmentIdJsonDelete**](ProductAttachmentsApi.md#productsIdAttachmentsAttachmentIdJsonDelete) | **DELETE** /products/{id}/attachments/{attachment_id}.json | Delete a Product Attachment. |
| [**productsIdAttachmentsAttachmentIdJsonGet**](ProductAttachmentsApi.md#productsIdAttachmentsAttachmentIdJsonGet) | **GET** /products/{id}/attachments/{attachment_id}.json | Retrieve a single Product Attachment. |
| [**productsIdAttachmentsCountJsonGet**](ProductAttachmentsApi.md#productsIdAttachmentsCountJsonGet) | **GET** /products/{id}/attachments/count.json | Count all Product Attachments. |
| [**productsIdAttachmentsJsonGet**](ProductAttachmentsApi.md#productsIdAttachmentsJsonGet) | **GET** /products/{id}/attachments.json | Retrieve all Product Attachments. |
| [**productsIdAttachmentsJsonPost**](ProductAttachmentsApi.md#productsIdAttachmentsJsonPost) | **POST** /products/{id}/attachments.json | Create a new Product Attachment. |


<a id="productsIdAttachmentsAttachmentIdJsonDelete"></a>
# **productsIdAttachmentsAttachmentIdJsonDelete**
> String productsIdAttachmentsAttachmentIdJsonDelete(login, authtoken, id, attachmentId)

Delete a Product Attachment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductAttachmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    ProductAttachmentsApi apiInstance = new ProductAttachmentsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the Product
    Integer attachmentId = 56; // Integer | Id of the Product Attachment
    try {
      String result = apiInstance.productsIdAttachmentsAttachmentIdJsonDelete(login, authtoken, id, attachmentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductAttachmentsApi#productsIdAttachmentsAttachmentIdJsonDelete");
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
| **id** | **Integer**| Id of the Product | |
| **attachmentId** | **Integer**| Id of the Product Attachment | |

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
| **404** | Product Not Found. |  -  |

<a id="productsIdAttachmentsAttachmentIdJsonGet"></a>
# **productsIdAttachmentsAttachmentIdJsonGet**
> Attachment productsIdAttachmentsAttachmentIdJsonGet(login, authtoken, id, attachmentId)

Retrieve a single Product Attachment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductAttachmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    ProductAttachmentsApi apiInstance = new ProductAttachmentsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the Product
    Integer attachmentId = 56; // Integer | Id of the Product Attachment
    try {
      Attachment result = apiInstance.productsIdAttachmentsAttachmentIdJsonGet(login, authtoken, id, attachmentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductAttachmentsApi#productsIdAttachmentsAttachmentIdJsonGet");
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
| **id** | **Integer**| Id of the Product | |
| **attachmentId** | **Integer**| Id of the Product Attachment | |

### Return type

[**Attachment**](Attachment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Product Not Found. |  -  |

<a id="productsIdAttachmentsCountJsonGet"></a>
# **productsIdAttachmentsCountJsonGet**
> Count productsIdAttachmentsCountJsonGet(login, authtoken, id)

Count all Product Attachments.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductAttachmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    ProductAttachmentsApi apiInstance = new ProductAttachmentsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | ID of the Product
    try {
      Count result = apiInstance.productsIdAttachmentsCountJsonGet(login, authtoken, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductAttachmentsApi#productsIdAttachmentsCountJsonGet");
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
| **id** | **Integer**| ID of the Product | |

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
| **404** | Product Not Found. |  -  |

<a id="productsIdAttachmentsJsonGet"></a>
# **productsIdAttachmentsJsonGet**
> List&lt;Attachment&gt; productsIdAttachmentsJsonGet(login, authtoken, id)

Retrieve all Product Attachments.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductAttachmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    ProductAttachmentsApi apiInstance = new ProductAttachmentsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | ID of the Product
    try {
      List<Attachment> result = apiInstance.productsIdAttachmentsJsonGet(login, authtoken, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductAttachmentsApi#productsIdAttachmentsJsonGet");
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
| **id** | **Integer**| ID of the Product | |

### Return type

[**List&lt;Attachment&gt;**](Attachment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Product Not Found. |  -  |

<a id="productsIdAttachmentsJsonPost"></a>
# **productsIdAttachmentsJsonPost**
> Attachment productsIdAttachmentsJsonPost(login, authtoken, id, attachmentEdit)

Create a new Product Attachment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductAttachmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    ProductAttachmentsApi apiInstance = new ProductAttachmentsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the Product
    AttachmentEdit attachmentEdit = new AttachmentEdit(); // AttachmentEdit | Product Attachment parameters.
    try {
      Attachment result = apiInstance.productsIdAttachmentsJsonPost(login, authtoken, id, attachmentEdit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductAttachmentsApi#productsIdAttachmentsJsonPost");
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
| **id** | **Integer**| Id of the Product | |
| **attachmentEdit** | [**AttachmentEdit**](AttachmentEdit.md)| Product Attachment parameters. | |

### Return type

[**Attachment**](Attachment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

