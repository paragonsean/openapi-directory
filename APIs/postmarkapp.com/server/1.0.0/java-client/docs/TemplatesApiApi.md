# TemplatesApiApi

All URIs are relative to *http://api.postmarkapp.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteTemplate**](TemplatesApiApi.md#deleteTemplate) | **DELETE** /templates/{templateIdOrAlias} | Delete a Template |
| [**getSingleTemplate**](TemplatesApiApi.md#getSingleTemplate) | **GET** /templates/{templateIdOrAlias} | Get a Template |
| [**listTemplates**](TemplatesApiApi.md#listTemplates) | **GET** /templates | Get the Templates associated with this Server |
| [**sendEmailBatchWithTemplates_0**](TemplatesApiApi.md#sendEmailBatchWithTemplates_0) | **POST** /email/batchWithTemplates | Send a batch of email using templates. |
| [**sendEmailWithTemplate_0**](TemplatesApiApi.md#sendEmailWithTemplate_0) | **POST** /email/withTemplate | Send an email using a Template |
| [**templatesPost**](TemplatesApiApi.md#templatesPost) | **POST** /templates | Create a Template |
| [**testTemplateContent**](TemplatesApiApi.md#testTemplateContent) | **POST** /templates/validate | Test Template Content |
| [**updateTemplate**](TemplatesApiApi.md#updateTemplate) | **PUT** /templates/{templateIdOrAlias} | Update a Template |


<a id="deleteTemplate"></a>
# **deleteTemplate**
> TemplateDetailResponse deleteTemplate(xPostmarkServerToken, templateIdOrAlias)

Delete a Template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TemplatesApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    TemplatesApiApi apiInstance = new TemplatesApiApi(defaultClient);
    String xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
    String templateIdOrAlias = "templateIdOrAlias_example"; // String | The 'TemplateID' or 'Alias' value for the Template you wish to delete.
    try {
      TemplateDetailResponse result = apiInstance.deleteTemplate(xPostmarkServerToken, templateIdOrAlias);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TemplatesApiApi#deleteTemplate");
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
| **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | |
| **templateIdOrAlias** | **String**| The &#39;TemplateID&#39; or &#39;Alias&#39; value for the Template you wish to delete. | |

### Return type

[**TemplateDetailResponse**](TemplateDetailResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

<a id="getSingleTemplate"></a>
# **getSingleTemplate**
> TemplateDetailResponse getSingleTemplate(xPostmarkServerToken, templateIdOrAlias)

Get a Template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TemplatesApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    TemplatesApiApi apiInstance = new TemplatesApiApi(defaultClient);
    String xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
    String templateIdOrAlias = "templateIdOrAlias_example"; // String | The 'TemplateID' or 'Alias' value for the Template you wish to retrieve.
    try {
      TemplateDetailResponse result = apiInstance.getSingleTemplate(xPostmarkServerToken, templateIdOrAlias);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TemplatesApiApi#getSingleTemplate");
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
| **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | |
| **templateIdOrAlias** | **String**| The &#39;TemplateID&#39; or &#39;Alias&#39; value for the Template you wish to retrieve. | |

### Return type

[**TemplateDetailResponse**](TemplateDetailResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

<a id="listTemplates"></a>
# **listTemplates**
> TemplateListingResponse listTemplates(xPostmarkServerToken, count, offset)

Get the Templates associated with this Server

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TemplatesApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    TemplatesApiApi apiInstance = new TemplatesApiApi(defaultClient);
    String xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
    BigDecimal count = new BigDecimal(78); // BigDecimal | The number of Templates to return
    BigDecimal offset = new BigDecimal(78); // BigDecimal | The number of Templates to \"skip\" before returning results.
    try {
      TemplateListingResponse result = apiInstance.listTemplates(xPostmarkServerToken, count, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TemplatesApiApi#listTemplates");
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
| **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | |
| **count** | **BigDecimal**| The number of Templates to return | |
| **offset** | **BigDecimal**| The number of Templates to \&quot;skip\&quot; before returning results. | |

### Return type

[**TemplateListingResponse**](TemplateListingResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

<a id="sendEmailBatchWithTemplates_0"></a>
# **sendEmailBatchWithTemplates_0**
> List&lt;SendEmailResponse&gt; sendEmailBatchWithTemplates_0(xPostmarkServerToken, body)

Send a batch of email using templates.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TemplatesApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    TemplatesApiApi apiInstance = new TemplatesApiApi(defaultClient);
    String xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
    SendEmailTemplatedBatchRequest body = new SendEmailTemplatedBatchRequest(); // SendEmailTemplatedBatchRequest | 
    try {
      List<SendEmailResponse> result = apiInstance.sendEmailBatchWithTemplates_0(xPostmarkServerToken, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TemplatesApiApi#sendEmailBatchWithTemplates_0");
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
| **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | |
| **body** | [**SendEmailTemplatedBatchRequest**](SendEmailTemplatedBatchRequest.md)|  | |

### Return type

[**List&lt;SendEmailResponse&gt;**](SendEmailResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

<a id="sendEmailWithTemplate_0"></a>
# **sendEmailWithTemplate_0**
> SendEmailResponse sendEmailWithTemplate_0(xPostmarkServerToken, body)

Send an email using a Template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TemplatesApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    TemplatesApiApi apiInstance = new TemplatesApiApi(defaultClient);
    String xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
    EmailWithTemplateRequest body = new EmailWithTemplateRequest(); // EmailWithTemplateRequest | 
    try {
      SendEmailResponse result = apiInstance.sendEmailWithTemplate_0(xPostmarkServerToken, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TemplatesApiApi#sendEmailWithTemplate_0");
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
| **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | |
| **body** | [**EmailWithTemplateRequest**](EmailWithTemplateRequest.md)|  | |

### Return type

[**SendEmailResponse**](SendEmailResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

<a id="templatesPost"></a>
# **templatesPost**
> TemplateRecordResponse templatesPost(xPostmarkServerToken, body)

Create a Template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TemplatesApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    TemplatesApiApi apiInstance = new TemplatesApiApi(defaultClient);
    String xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
    CreateTemplateRequest body = new CreateTemplateRequest(); // CreateTemplateRequest | 
    try {
      TemplateRecordResponse result = apiInstance.templatesPost(xPostmarkServerToken, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TemplatesApiApi#templatesPost");
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
| **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | |
| **body** | [**CreateTemplateRequest**](CreateTemplateRequest.md)|  | |

### Return type

[**TemplateRecordResponse**](TemplateRecordResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

<a id="testTemplateContent"></a>
# **testTemplateContent**
> TemplateValidationResponse testTemplateContent(xPostmarkServerToken, body)

Test Template Content

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TemplatesApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    TemplatesApiApi apiInstance = new TemplatesApiApi(defaultClient);
    String xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
    TemplateValidationRequest body = new TemplateValidationRequest(); // TemplateValidationRequest | 
    try {
      TemplateValidationResponse result = apiInstance.testTemplateContent(xPostmarkServerToken, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TemplatesApiApi#testTemplateContent");
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
| **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | |
| **body** | [**TemplateValidationRequest**](TemplateValidationRequest.md)|  | [optional] |

### Return type

[**TemplateValidationResponse**](TemplateValidationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

<a id="updateTemplate"></a>
# **updateTemplate**
> TemplateRecordResponse updateTemplate(xPostmarkServerToken, templateIdOrAlias, body)

Update a Template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TemplatesApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    TemplatesApiApi apiInstance = new TemplatesApiApi(defaultClient);
    String xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
    String templateIdOrAlias = "templateIdOrAlias_example"; // String | The 'TemplateID' or 'Alias' value for the Template you wish to update.
    EditTemplateRequest body = new EditTemplateRequest(); // EditTemplateRequest | 
    try {
      TemplateRecordResponse result = apiInstance.updateTemplate(xPostmarkServerToken, templateIdOrAlias, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TemplatesApiApi#updateTemplate");
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
| **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | |
| **templateIdOrAlias** | **String**| The &#39;TemplateID&#39; or &#39;Alias&#39; value for the Template you wish to update. | |
| **body** | [**EditTemplateRequest**](EditTemplateRequest.md)|  | |

### Return type

[**TemplateRecordResponse**](TemplateRecordResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

