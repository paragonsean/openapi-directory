# SpecificationFieldApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**specificationsField**](SpecificationFieldApi.md#specificationsField) | **GET** /api/catalog_system/pub/specification/fieldGet/{fieldId} | Get Specification Field |
| [**specificationsInsertField**](SpecificationFieldApi.md#specificationsInsertField) | **POST** /api/catalog_system/pvt/specification/field | Create Specification Field |
| [**specificationsInsertFieldUpdate**](SpecificationFieldApi.md#specificationsInsertFieldUpdate) | **PUT** /api/catalog_system/pvt/specification/field | Update Specification Field |


<a id="specificationsField"></a>
# **specificationsField**
> SpecificationsField200Response specificationsField(contentType, accept, fieldId)

Get Specification Field

Retrieves details from a specification field by this field&#39;s ID.   &gt;⚠️ This is a legacy endpoint. We recommend using [Get Specification](https://developers.vtex.com/vtex-rest-api/reference/get_api-catalog-pvt-specification-specificationid) instead.    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Name\&quot;: \&quot;Material\&quot;,      \&quot;CategoryId\&quot;: 4,      \&quot;FieldId\&quot;: 88,      \&quot;IsActive\&quot;: true,      \&quot;IsRequired\&quot;: true,      \&quot;FieldTypeId\&quot;: 1,      \&quot;FieldTypeName\&quot;: \&quot;Texto\&quot;,      \&quot;FieldValueId\&quot;: null,      \&quot;Description\&quot;: \&quot;Composition of the product.\&quot;,      \&quot;IsStockKeepingUnit\&quot;: false,      \&quot;IsFilter\&quot;: true,      \&quot;IsOnProductDetails\&quot;: false,      \&quot;Position\&quot;: 1,      \&quot;IsWizard\&quot;: false,      \&quot;IsTopMenuLinkActive\&quot;: false,      \&quot;IsSideMenuLinkActive\&quot;: true,      \&quot;DefaultValue\&quot;: null,      \&quot;FieldGroupId\&quot;: 20,      \&quot;FieldGroupName\&quot;: \&quot;Clothes specifications\&quot;  }  &#x60;&#x60;&#x60;    

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpecificationFieldApi;

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

    SpecificationFieldApi apiInstance = new SpecificationFieldApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer fieldId = 88; // Integer | Specification Field ID.
    try {
      SpecificationsField200Response result = apiInstance.specificationsField(contentType, accept, fieldId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpecificationFieldApi#specificationsField");
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
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **fieldId** | **Integer**| Specification Field ID. | |

### Return type

[**SpecificationsField200Response**](SpecificationsField200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="specificationsInsertField"></a>
# **specificationsInsertField**
> Integer specificationsInsertField(contentType, accept, specificationsInsertFieldRequest)

Create Specification Field

Creates a specification field in a category.   &gt;⚠️ This is a legacy endpoint. We recommend using [Create Specification](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-post-specification) instead.    ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;Name\&quot;: \&quot;Material\&quot;,      \&quot;CategoryId\&quot;: 4,      \&quot;FieldId\&quot;: 88,      \&quot;IsActive\&quot;: true,      \&quot;IsRequired\&quot;: true,      \&quot;FieldTypeId\&quot;: 1,      \&quot;FieldValueId\&quot;: 1,      \&quot;IsStockKeepingUnit\&quot;: false,      \&quot;Description\&quot;: \&quot;Composition of the product.\&quot;,      \&quot;IsFilter\&quot;: true,      \&quot;IsOnProductDetails\&quot;: false,      \&quot;Position\&quot;: 1,      \&quot;IsWizard\&quot;: false,      \&quot;IsTopMenuLinkActive\&quot;: true,      \&quot;IsSideMenuLinkActive\&quot;: true,      \&quot;DefaultValue\&quot;: null,      \&quot;FieldGroupId\&quot;: 20,      \&quot;FieldGroupName\&quot;: \&quot;Clothes specifications\&quot;  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  89  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpecificationFieldApi;

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

    SpecificationFieldApi apiInstance = new SpecificationFieldApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    SpecificationsInsertFieldRequest specificationsInsertFieldRequest = new SpecificationsInsertFieldRequest(); // SpecificationsInsertFieldRequest | 
    try {
      Integer result = apiInstance.specificationsInsertField(contentType, accept, specificationsInsertFieldRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpecificationFieldApi#specificationsInsertField");
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
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **specificationsInsertFieldRequest** | [**SpecificationsInsertFieldRequest**](SpecificationsInsertFieldRequest.md)|  | |

### Return type

**Integer**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="specificationsInsertFieldUpdate"></a>
# **specificationsInsertFieldUpdate**
> Integer specificationsInsertFieldUpdate(contentType, accept, specificationsInsertFieldUpdateRequest)

Update Specification Field

Updates a specification field in a category.   &gt;⚠️ This is a legacy endpoint. We recommend using [Update Specification](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-put-specification) instead.    ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldId\&quot;: 89,      \&quot;Name\&quot;: \&quot;Material\&quot;,      \&quot;CategoryId\&quot;: 4,      \&quot;IsActive\&quot;: true,      \&quot;IsRequired\&quot;: true,      \&quot;FieldTypeId\&quot;: 1,      \&quot;Description\&quot;: \&quot;Composition of the product.\&quot;,      \&quot;IsStockKeepingUnit\&quot;: false,      \&quot;IsFilter\&quot;: true,      \&quot;IsOnProductDetails\&quot;: true,      \&quot;Position\&quot;: 1,      \&quot;IsWizard\&quot;: false,      \&quot;IsTopMenuLinkActive\&quot;: false,      \&quot;IsSideMenuLinkActive\&quot;: false,      \&quot;DefaultValue\&quot;: \&quot;Cotton\&quot;,      \&quot;FieldGroupId\&quot;: 20,      \&quot;FieldGroupName\&quot;: \&quot;Clothes specifications\&quot;  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  89  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpecificationFieldApi;

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

    SpecificationFieldApi apiInstance = new SpecificationFieldApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    SpecificationsInsertFieldUpdateRequest specificationsInsertFieldUpdateRequest = new SpecificationsInsertFieldUpdateRequest(); // SpecificationsInsertFieldUpdateRequest | 
    try {
      Integer result = apiInstance.specificationsInsertFieldUpdate(contentType, accept, specificationsInsertFieldUpdateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpecificationFieldApi#specificationsInsertFieldUpdate");
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
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **specificationsInsertFieldUpdateRequest** | [**SpecificationsInsertFieldUpdateRequest**](SpecificationsInsertFieldUpdateRequest.md)|  | |

### Return type

**Integer**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

