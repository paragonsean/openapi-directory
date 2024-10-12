# AttachmentApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiCatalogPvtAttachmentAttachmentidDelete**](AttachmentApi.md#apiCatalogPvtAttachmentAttachmentidDelete) | **DELETE** /api/catalog/pvt/attachment/{attachmentid} | Delete attachment |
| [**apiCatalogPvtAttachmentAttachmentidGet**](AttachmentApi.md#apiCatalogPvtAttachmentAttachmentidGet) | **GET** /api/catalog/pvt/attachment/{attachmentid} | Get attachment |
| [**apiCatalogPvtAttachmentAttachmentidPut**](AttachmentApi.md#apiCatalogPvtAttachmentAttachmentidPut) | **PUT** /api/catalog/pvt/attachment/{attachmentid} | Update attachment |
| [**apiCatalogPvtAttachmentPost**](AttachmentApi.md#apiCatalogPvtAttachmentPost) | **POST** /api/catalog/pvt/attachment | Create attachment |
| [**apiCatalogPvtAttachmentsGet**](AttachmentApi.md#apiCatalogPvtAttachmentsGet) | **GET** /api/catalog/pvt/attachments | Get all attachments |


<a id="apiCatalogPvtAttachmentAttachmentidDelete"></a>
# **apiCatalogPvtAttachmentAttachmentidDelete**
> apiCatalogPvtAttachmentAttachmentidDelete(attachmentid, contentType, accept)

Delete attachment

Deletes a previously existing SKU attachment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttachmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    AttachmentApi apiInstance = new AttachmentApi(defaultClient);
    String attachmentid = "vtexcommercestable"; // String | Attachment ID.
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    try {
      apiInstance.apiCatalogPvtAttachmentAttachmentidDelete(attachmentid, contentType, accept);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttachmentApi#apiCatalogPvtAttachmentAttachmentidDelete");
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
| **attachmentid** | **String**| Attachment ID. | |
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiCatalogPvtAttachmentAttachmentidGet"></a>
# **apiCatalogPvtAttachmentAttachmentidGet**
> AttachmentResponse apiCatalogPvtAttachmentAttachmentidGet(attachmentid, contentType, accept)

Get attachment

Gets information about a registered attachment.    &gt;⚠️ To understand the specific syntax for Assembly Options attachments, read the [Assembly Options](https://help.vtex.com/en/tutorial/assembly-options--5x5FhNr4f5RUGDEGWzV1nH#assembly-options-syntax) documentation.  ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;Id\&quot;: 8,    \&quot;Name\&quot;: \&quot;Test\&quot;,    \&quot;IsRequired\&quot;: true,    \&quot;IsActive\&quot;: true,    \&quot;Domains\&quot;: [      {        \&quot;FieldName\&quot;: \&quot;Basic test\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[1-2]#9[1-1][1]basic;#11[0-1][1]basic\&quot;      },      {        \&quot;FieldName\&quot;: \&quot;teste\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[0-10]#8[0-3][0]medium;#9[0-3][0]medium;#10[0-3][0]medium;#11[0-3][0]medium;#36[0-3][0]medium;#37[0-3][0]medium;#38[0-3][0]medium\&quot;      }    ]  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttachmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    AttachmentApi apiInstance = new AttachmentApi(defaultClient);
    String attachmentid = "8"; // String | Attachment ID.
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    try {
      AttachmentResponse result = apiInstance.apiCatalogPvtAttachmentAttachmentidGet(attachmentid, contentType, accept);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttachmentApi#apiCatalogPvtAttachmentAttachmentidGet");
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
| **attachmentid** | **String**| Attachment ID. | |
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |

### Return type

[**AttachmentResponse**](AttachmentResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiCatalogPvtAttachmentAttachmentidPut"></a>
# **apiCatalogPvtAttachmentAttachmentidPut**
> AttachmentResponse apiCatalogPvtAttachmentAttachmentidPut(attachmentid, contentType, accept, attachmentRequest)

Update attachment

Updates a previously existing SKU attachment with new information.    &gt;⚠️ To understand the specific syntax for Assembly Options attachments, read the [Assembly Options](https://help.vtex.com/en/tutorial/assembly-options--5x5FhNr4f5RUGDEGWzV1nH#assembly-options-syntax) documentation.   ## Request body example    &#x60;&#x60;&#x60;json  {    \&quot;Name\&quot;: \&quot;Test\&quot;,    \&quot;IsRequired\&quot;: true,    \&quot;IsActive\&quot;: true,    \&quot;Domains\&quot;: [      {        \&quot;FieldName\&quot;: \&quot;Basic test\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[1-2]#9[1-1][1]basic;#11[0-1][1]basic\&quot;      },      {        \&quot;FieldName\&quot;: \&quot;teste\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[0-10]#8[0-3][0]medium;#9[0-3][0]medium;#10[0-3][0]medium;#11[0-3][0]medium;#36[0-3][0]medium;#37[0-3][0]medium;#38[0-3][0]medium\&quot;      }    ]  }  &#x60;&#x60;&#x60;  ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;Id\&quot;: 8,    \&quot;Name\&quot;: \&quot;Test\&quot;,    \&quot;IsRequired\&quot;: true,    \&quot;IsActive\&quot;: true,    \&quot;Domains\&quot;: [      {        \&quot;FieldName\&quot;: \&quot;Basic test\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[1-2]#9[1-1][1]basic;#11[0-1][1]basic\&quot;      },      {        \&quot;FieldName\&quot;: \&quot;teste\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[0-10]#8[0-3][0]medium;#9[0-3][0]medium;#10[0-3][0]medium;#11[0-3][0]medium;#36[0-3][0]medium;#37[0-3][0]medium;#38[0-3][0]medium\&quot;      }    ]  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttachmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    AttachmentApi apiInstance = new AttachmentApi(defaultClient);
    String attachmentid = "vtexcommercestable"; // String | Attachment ID.
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    AttachmentRequest attachmentRequest = new AttachmentRequest(); // AttachmentRequest | 
    try {
      AttachmentResponse result = apiInstance.apiCatalogPvtAttachmentAttachmentidPut(attachmentid, contentType, accept, attachmentRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttachmentApi#apiCatalogPvtAttachmentAttachmentidPut");
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
| **attachmentid** | **String**| Attachment ID. | |
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **attachmentRequest** | [**AttachmentRequest**](AttachmentRequest.md)|  | [optional] |

### Return type

[**AttachmentResponse**](AttachmentResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiCatalogPvtAttachmentPost"></a>
# **apiCatalogPvtAttachmentPost**
> AttachmentResponse apiCatalogPvtAttachmentPost(contentType, accept, attachmentRequest)

Create attachment

Creates a new SKU attachment.   &gt;⚠️ To understand the specific syntax for Assembly Options attachments, read the [Assembly Options](https://help.vtex.com/en/tutorial/assembly-options--5x5FhNr4f5RUGDEGWzV1nH#assembly-options-syntax) documentation.   ## Request body example    &#x60;&#x60;&#x60;json  {    \&quot;Name\&quot;: \&quot;Test\&quot;,    \&quot;IsRequired\&quot;: true,    \&quot;IsActive\&quot;: true,    \&quot;Domains\&quot;: [      {        \&quot;FieldName\&quot;: \&quot;Basic test\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[1-2]#9[1-1][1]basic;#11[0-1][1]basic\&quot;      },      {        \&quot;FieldName\&quot;: \&quot;teste\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[0-10]#8[0-3][0]medium;#9[0-3][0]medium;#10[0-3][0]medium;#11[0-3][0]medium;#36[0-3][0]medium;#37[0-3][0]medium;#38[0-3][0]medium\&quot;      }    ]  }  &#x60;&#x60;&#x60;  ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;Id\&quot;: 8,    \&quot;Name\&quot;: \&quot;Test\&quot;,    \&quot;IsRequired\&quot;: true,    \&quot;IsActive\&quot;: true,    \&quot;Domains\&quot;: [      {        \&quot;FieldName\&quot;: \&quot;Basic test\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[1-2]#9[1-1][1]basic;#11[0-1][1]basic\&quot;      },      {        \&quot;FieldName\&quot;: \&quot;teste\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[0-10]#8[0-3][0]medium;#9[0-3][0]medium;#10[0-3][0]medium;#11[0-3][0]medium;#36[0-3][0]medium;#37[0-3][0]medium;#38[0-3][0]medium\&quot;      }    ]  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttachmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    AttachmentApi apiInstance = new AttachmentApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    AttachmentRequest attachmentRequest = new AttachmentRequest(); // AttachmentRequest | 
    try {
      AttachmentResponse result = apiInstance.apiCatalogPvtAttachmentPost(contentType, accept, attachmentRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttachmentApi#apiCatalogPvtAttachmentPost");
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
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **attachmentRequest** | [**AttachmentRequest**](AttachmentRequest.md)|  | [optional] |

### Return type

[**AttachmentResponse**](AttachmentResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiCatalogPvtAttachmentsGet"></a>
# **apiCatalogPvtAttachmentsGet**
> ApiCatalogPvtAttachmentsGet200Response apiCatalogPvtAttachmentsGet(contentType, accept)

Get all attachments

Retrieves information about all registered attachments.    &gt;⚠️ To understand the specific syntax for Assembly Options attachments, read the [Assembly Options](https://help.vtex.com/en/tutorial/assembly-options--5x5FhNr4f5RUGDEGWzV1nH#assembly-options-syntax) documentation.   ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Page\&quot;: 1,      \&quot;Size\&quot;: 11,      \&quot;TotalRows\&quot;: 11,      \&quot;TotalPage\&quot;: 1,      \&quot;Data\&quot;: [          {              \&quot;Id\&quot;: 1,              \&quot;Name\&quot;: \&quot;Acessórios do bicho\&quot;,              \&quot;IsRequired\&quot;: true,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: [                  {                      \&quot;FieldName\&quot;: \&quot;extra\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;\&quot;,                      \&quot;DomainValues\&quot;: \&quot;[0-3]#1[1-2][1]pricetable1;#3[0-2][0]pricetable2;#5[0-2][0]pricetable3\&quot;                  }              ]          },          {              \&quot;Id\&quot;: 2,              \&quot;Name\&quot;: \&quot;Sobrenome\&quot;,              \&quot;IsRequired\&quot;: false,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: []          },          {              \&quot;Id\&quot;: 3,              \&quot;Name\&quot;: \&quot;Assinatura Teste\&quot;,              \&quot;IsRequired\&quot;: false,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: [                  {                      \&quot;FieldName\&quot;: \&quot; vtex.subscription.key.frequency\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;\&quot;,                      \&quot;DomainValues\&quot;: \&quot;1 day, 7 day, 1 month, 6 month\&quot;                  },                  {                      \&quot;FieldName\&quot;: \&quot;vtex.subscription.key.validity.begin\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;\&quot;,                      \&quot;DomainValues\&quot;: \&quot;1\&quot;                  },                  {                      \&quot;FieldName\&quot;: \&quot;vtex.subscription.key.validity.end\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;\&quot;,                      \&quot;DomainValues\&quot;: \&quot;31\&quot;                  },                  {                      \&quot;FieldName\&quot;: \&quot;vtex.subscription.key.purchaseday\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;\&quot;,                      \&quot;DomainValues\&quot;: \&quot;1, 2, 20, 31\&quot;                  }              ]          },          {              \&quot;Id\&quot;: 5,              \&quot;Name\&quot;: \&quot;teste\&quot;,              \&quot;IsRequired\&quot;: false,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: []          },          {              \&quot;Id\&quot;: 6,              \&quot;Name\&quot;: \&quot;teste2\&quot;,              \&quot;IsRequired\&quot;: false,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: []          },          {              \&quot;Id\&quot;: 7,              \&quot;Name\&quot;: \&quot;vtex.subscription.teste3\&quot;,              \&quot;IsRequired\&quot;: false,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: []          },          {              \&quot;Id\&quot;: 8,              \&quot;Name\&quot;: \&quot;teste api nova\&quot;,              \&quot;IsRequired\&quot;: true,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: [                  {                      \&quot;FieldName\&quot;: \&quot;Basic teste\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;\&quot;,                      \&quot;DomainValues\&quot;: \&quot;[1-2]#9[1-1][1]basic;#11[0-1][1]basic\&quot;                  },                  {                      \&quot;FieldName\&quot;: \&quot;teste\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;\&quot;,                      \&quot;DomainValues\&quot;: \&quot;[0-10]#8[0-3][0]medium;#9[0-3][0]medium;#10[0-3][0]medium;#11[0-3][0]medium;#36[0-3][0]medium;#37[0-3][0]medium;#38[0-3][0]medium\&quot;                  }              ]          },          {              \&quot;Id\&quot;: 9,              \&quot;Name\&quot;: \&quot;vtex.subscription.teste\&quot;,              \&quot;IsRequired\&quot;: false,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: []          },          {              \&quot;Id\&quot;: 10,              \&quot;Name\&quot;: \&quot;Montagens\&quot;,              \&quot;IsRequired\&quot;: false,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: []          },          {              \&quot;Id\&quot;: 11,              \&quot;Name\&quot;: \&quot;vtex.subscription.subscription\&quot;,              \&quot;IsRequired\&quot;: false,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: [                  {                      \&quot;FieldName\&quot;: \&quot;vtex.subscription.key.frequency\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;15\&quot;,                      \&quot;DomainValues\&quot;: \&quot;1 month\&quot;                  },                  {                      \&quot;FieldName\&quot;: \&quot;vtex.subscription.key.purchaseday\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;15\&quot;,                      \&quot;DomainValues\&quot;: \&quot;1,15,28\&quot;                  }              ]          },          {              \&quot;Id\&quot;: 12,              \&quot;Name\&quot;: \&quot;T-Shirt Customization\&quot;,              \&quot;IsRequired\&quot;: false,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: [                  {                      \&quot;FieldName\&quot;: \&quot;T-Shirt Name\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;15\&quot;,                      \&quot;DomainValues\&quot;: \&quot;[]\&quot;                  }              ]          }      ]  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttachmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    AttachmentApi apiInstance = new AttachmentApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    try {
      ApiCatalogPvtAttachmentsGet200Response result = apiInstance.apiCatalogPvtAttachmentsGet(contentType, accept);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttachmentApi#apiCatalogPvtAttachmentsGet");
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
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |

### Return type

[**ApiCatalogPvtAttachmentsGet200Response**](ApiCatalogPvtAttachmentsGet200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

