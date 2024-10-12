# DocumentsApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createnewdocument**](DocumentsApi.md#createnewdocument) | **POST** /api/dataentities/{dataEntityName}/documents | Create new document |
| [**createorupdatepartialdocument**](DocumentsApi.md#createorupdatepartialdocument) | **PATCH** /api/dataentities/{dataEntityName}/documents | Create partial document |
| [**deletedocument**](DocumentsApi.md#deletedocument) | **DELETE** /api/dataentities/{dataEntityName}/documents/{id} | Delete document |
| [**getdocument**](DocumentsApi.md#getdocument) | **GET** /api/dataentities/{dataEntityName}/documents/{id} | Get document |
| [**updateentiredocument**](DocumentsApi.md#updateentiredocument) | **PUT** /api/dataentities/{dataEntityName}/documents/{id} | Update entire document |
| [**updatepartialdocument**](DocumentsApi.md#updatepartialdocument) | **PATCH** /api/dataentities/{dataEntityName}/documents/{id} | Update partial document |


<a id="createnewdocument"></a>
# **createnewdocument**
> DocumentResponse createnewdocument(contentType, accept, dataEntityName, requestBody, schema)

Create new document

This request allows you to create a new document corresponding to a given data entity. For example, you can create a new customer profile or address.    &gt; You can use this request to create documents for any given data entity. Because of this, you are not restricted to using the fields exemplified below in your requests. But you should be aware of the fields allowed or required for each document you wish to create.    ## Example use cases    ### Client profile    In order to create a new customer profile, choose the &#x60;CL&#x60; data entity and send a request similar to this:    POST  &#x60;&#x60;&#x60;  https://examplestore.vtexcommercestable.com.br/api/dataentities/Client/documents  &#x60;&#x60;&#x60;    Request body  &#x60;&#x60;&#x60;json  {      \&quot;email\&quot;: \&quot;clark.kent@examplemail.com\&quot;,      \&quot;firstName\&quot;: \&quot;Clark\&quot;,      \&quot;lastName\&quot;: \&quot;Kent\&quot;,      \&quot;phone\&quot;: \&quot;+12025550195\&quot;,      \&quot;documentType\&quot;: \&quot;CPF\&quot;,      \&quot;document\&quot;: \&quot;12345678900\&quot;      \&quot;isCorporate\&quot;: false,      \&quot;isNewsletterOptIn\&quot;: false,      \&quot;localeDefault\&quot;: \&quot;en-US\&quot;   }  &#x60;&#x60;&#x60;    ### Client address    For a new address, the data entity is &#x60;AD&#x60; and the request would look like this:    POST  &#x60;&#x60;&#x60;  https://examplestore.vtexcommercestable.com.br/api/dataentities/Address/documents  &#x60;&#x60;&#x60;    Request body  &#x60;&#x60;&#x60;json  {      \&quot;addressName\&quot;: \&quot;My House\&quot;,      \&quot;addressType\&quot;: \&quot;residential\&quot;,      \&quot;city\&quot;: \&quot;Metropolis\&quot;,      \&quot;complement\&quot;: \&quot;\&quot;,      \&quot;country\&quot;: \&quot;USA\&quot;,      \&quot;postalCode\&quot;: \&quot;11375\&quot;,      \&quot;receiverName\&quot;: \&quot;Clark Kent\&quot;,      \&quot;reference\&quot;: null,      \&quot;state\&quot;: \&quot;MP\&quot;,      \&quot;street\&quot;: \&quot;Baker Street\&quot;,      \&quot;neighborhood\&quot;: \&quot;Upper east side\&quot;,      \&quot;number\&quot;: \&quot;21\&quot;,      \&quot;userId\&quot;: \&quot;7e03m794-a33a-11e9-84rt6-0adfa64s5a8e\&quot;  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentsApi;

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

    DocumentsApi apiInstance = new DocumentsApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String dataEntityName = "Client"; // String | Name of the data entity. Defined by the api. Examples of native data entities you can use are `CL` for client profiles and `AD` for client addresses.
    Map<String, String> requestBody = new HashMap(); // Map<String, String> | 
    String schema = "schema"; // String | Name of the schema the document to be created needs to be compliant with.
    try {
      DocumentResponse result = apiInstance.createnewdocument(contentType, accept, dataEntityName, requestBody, schema);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentsApi#createnewdocument");
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
| **contentType** | **String**| Type of the content being sent. | |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | |
| **dataEntityName** | **String**| Name of the data entity. Defined by the api. Examples of native data entities you can use are &#x60;CL&#x60; for client profiles and &#x60;AD&#x60; for client addresses. | |
| **requestBody** | [**Map&lt;String, String&gt;**](String.md)|  | |
| **schema** | **String**| Name of the schema the document to be created needs to be compliant with. | [optional] |

### Return type

[**DocumentResponse**](DocumentResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="createorupdatepartialdocument"></a>
# **createorupdatepartialdocument**
> DocumentResponse createorupdatepartialdocument(dataEntityName, contentType, accept, requestBody, schema)

Create partial document

This request allows you to partially update a document corresponding to a given data entity.    &gt; You can use this request to create documents for any given data entity. Because of this, you are not restricted to using the fields exemplified below in your requests. But you should be aware of the fields allowed or required for each document you wish to update.    ## Example use cases    ### Client profile    In order to create a customer profile&#39;s &#x60;phone&#x60; and &#x60;isNewsletterOptIn&#x60; fields, choose the &#x60;CL&#x60; data entity and send a request similar to this:    PATCH  &#x60;&#x60;&#x60;  https://examplestore.vtexcommercestable.com.br/api/dataentities/Client/documents  &#x60;&#x60;&#x60;    Request body  &#x60;&#x60;&#x60;json  {      \&quot;phone\&quot;: \&quot;+12025550195\&quot;,      \&quot;isNewsletterOptIn\&quot;: false   }  &#x60;&#x60;&#x60;    ### Client address    In order to update the &#x60;receiverName&#x60; of an existing address, the data entity is &#x60;AD&#x60; and the request would look like this:    PATCH  &#x60;&#x60;&#x60;  https://examplestore.vtexcommercestable.com.br/api/dataentities/Address/documents  &#x60;&#x60;&#x60;    Request body  &#x60;&#x60;&#x60;json  {      \&quot;receiverName\&quot;: \&quot;Lois Lane\&quot;  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentsApi;

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

    DocumentsApi apiInstance = new DocumentsApi(defaultClient);
    String dataEntityName = "Client"; // String | Name of the data entity. Defined by the api. Examples of native data entities you can use are `CL` for client profiles and `AD` for client addresses.
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Map<String, String> requestBody = new HashMap(); // Map<String, String> | JSON with the fields to be updated.
    String schema = "schema"; // String | Name of the schema the document to be created needs to be compliant with.
    try {
      DocumentResponse result = apiInstance.createorupdatepartialdocument(dataEntityName, contentType, accept, requestBody, schema);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentsApi#createorupdatepartialdocument");
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
| **dataEntityName** | **String**| Name of the data entity. Defined by the api. Examples of native data entities you can use are &#x60;CL&#x60; for client profiles and &#x60;AD&#x60; for client addresses. | |
| **contentType** | **String**| Type of the content being sent. | |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | |
| **requestBody** | [**Map&lt;String, String&gt;**](String.md)| JSON with the fields to be updated. | |
| **schema** | **String**| Name of the schema the document to be created needs to be compliant with. | [optional] |

### Return type

[**DocumentResponse**](DocumentResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="deletedocument"></a>
# **deletedocument**
> deletedocument(dataEntityName, contentType, accept, id)

Delete document

It allows to delete a document.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentsApi;

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

    DocumentsApi apiInstance = new DocumentsApi(defaultClient);
    String dataEntityName = "Client"; // String | Name of the data entity. Defined by the api. Examples of native data entities you can use are `CL` for client profiles and `AD` for client addresses.
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String id = "Client-b818cbda-e489-11e6-94f4-0ac138d2d42e"; // String | ID of the Document.
    try {
      apiInstance.deletedocument(dataEntityName, contentType, accept, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentsApi#deletedocument");
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
| **dataEntityName** | **String**| Name of the data entity. Defined by the api. Examples of native data entities you can use are &#x60;CL&#x60; for client profiles and &#x60;AD&#x60; for client addresses. | |
| **contentType** | **String**| Type of the content being sent. | |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | |
| **id** | **String**| ID of the Document. | |

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

<a id="getdocument"></a>
# **getdocument**
> UsingFieldsAll getdocument(dataEntityName, contentType, accept, id)

Get document

Gets document by ID.    &gt; Assign the &#x60;_fields&#x60; parameter in the query string to retrieve the desired fields. If you want to return all the fields use &#x60;_fields&#x3D;_all&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentsApi;

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

    DocumentsApi apiInstance = new DocumentsApi(defaultClient);
    String dataEntityName = "Client"; // String | Name of the data entity. Defined by the api. Examples of native data entities you can use are `CL` for client profiles and `AD` for client addresses.
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String id = "Client-b818cbda-e489-11e6-94f4-0ac138d2d42e"; // String | ID of the Document.
    try {
      UsingFieldsAll result = apiInstance.getdocument(dataEntityName, contentType, accept, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentsApi#getdocument");
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
| **dataEntityName** | **String**| Name of the data entity. Defined by the api. Examples of native data entities you can use are &#x60;CL&#x60; for client profiles and &#x60;AD&#x60; for client addresses. | |
| **contentType** | **String**| Type of the content being sent. | |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | |
| **id** | **String**| ID of the Document. | |

### Return type

[**UsingFieldsAll**](UsingFieldsAll.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Sucessful response |  -  |

<a id="updateentiredocument"></a>
# **updateentiredocument**
> DocumentResponse updateentiredocument(dataEntityName, accept, id, requestBody, where, schema)

Update entire document

Update an existing document corresponding to a given data entity. For example, you can update a customer profile or address.    &gt; You can use this request to update documents in any given data entity. Because of this, you are not restricted to using the fields exemplified below in your requests. But you should be aware of the fields allowed or required for each document you wish to update.    ## Example use cases    ### Client profile    In order to update an existing customer profile, choose the &#x60;CL&#x60; data entity and send a request similar to this:    PUT  &#x60;&#x60;&#x60;  https://examplestore.vtexcommercestable.com.br/api/dataentities/Client/documents/123456789abc  &#x60;&#x60;&#x60;    Request body  &#x60;&#x60;&#x60;json  {      \&quot;email\&quot;: \&quot;clark.kent@examplemail.com\&quot;,      \&quot;firstName\&quot;: \&quot;Clark\&quot;,      \&quot;lastName\&quot;: \&quot;Kent\&quot;,      \&quot;phone\&quot;: \&quot;+12025550195\&quot;,      \&quot;documentType\&quot;: \&quot;CPF\&quot;,      \&quot;document\&quot;: \&quot;12345678900\&quot;      \&quot;isCorporate\&quot;: false,      \&quot;isNewsletterOptIn\&quot;: false,      \&quot;localeDefault\&quot;: \&quot;en-US\&quot;   }  &#x60;&#x60;&#x60;    ### Client address    To update an address, the data entity is &#x60;AD&#x60; and the request would look like this:    PUT  &#x60;&#x60;&#x60;  https://examplestore.vtexcommercestable.com.br/api/dataentities/Address/documents/123456789abc  &#x60;&#x60;&#x60;    Request body  &#x60;&#x60;&#x60;json  {      \&quot;addressName\&quot;: \&quot;My House\&quot;,      \&quot;addressType\&quot;: \&quot;residential\&quot;,      \&quot;city\&quot;: \&quot;Metropolis\&quot;,      \&quot;complement\&quot;: \&quot;\&quot;,      \&quot;country\&quot;: \&quot;USA\&quot;,      \&quot;postalCode\&quot;: \&quot;11375\&quot;,      \&quot;receiverName\&quot;: \&quot;Clark Kent\&quot;,      \&quot;reference\&quot;: null,      \&quot;state\&quot;: \&quot;MP\&quot;,      \&quot;street\&quot;: \&quot;Baker Street\&quot;,      \&quot;neighborhood\&quot;: \&quot;Upper east side\&quot;,      \&quot;number\&quot;: \&quot;21\&quot;,      \&quot;userId\&quot;: \&quot;7e03m794-a33a-11e9-84rt6-0adfa64s5a8e\&quot;  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentsApi;

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

    DocumentsApi apiInstance = new DocumentsApi(defaultClient);
    String dataEntityName = "Client"; // String | Name of the data entity. Defined by the api. Examples of native data entities you can use are `CL` for client profiles and `AD` for client addresses.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String id = "Client-b818cbda-e489-11e6-94f4-0ac138d2d42e"; // String | ID of the Document.
    Map<String, String> requestBody = new HashMap(); // Map<String, String> | 
    String where = "firstName is not null."; // String | Filter specification.
    String schema = "schema"; // String | Name of the schema the document to be created needs to be compliant with.
    try {
      DocumentResponse result = apiInstance.updateentiredocument(dataEntityName, accept, id, requestBody, where, schema);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentsApi#updateentiredocument");
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
| **dataEntityName** | **String**| Name of the data entity. Defined by the api. Examples of native data entities you can use are &#x60;CL&#x60; for client profiles and &#x60;AD&#x60; for client addresses. | |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | |
| **id** | **String**| ID of the Document. | |
| **requestBody** | [**Map&lt;String, String&gt;**](String.md)|  | |
| **where** | **String**| Filter specification. | [optional] |
| **schema** | **String**| Name of the schema the document to be created needs to be compliant with. | [optional] |

### Return type

[**DocumentResponse**](DocumentResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updatepartialdocument"></a>
# **updatepartialdocument**
> DocumentResponse updatepartialdocument(dataEntityName, accept, id, requestBody, where, schema)

Update partial document

This request allows you to partially update a document corresponding to a given data entity. For example, you can update some fields of a customer profile or address.    &gt; You can use this request to update documents for any given data entity. Because of this, you are not restricted to using the fields exemplified below in your requests. But you should be aware of the fields allowed or required for each document you wish to update.    ## Example use cases    ### Client profile    In order to update a customer profile&#39;s &#x60;phone&#x60; and &#x60;isNewsletterOptIn&#x60; fields, choose the &#x60;CL&#x60; data entity and send a request similar to this:    PATCH  &#x60;&#x60;&#x60;  https://examplestore.vtexcommercestable.com.br/api/dataentities/Client/documents/123456789abc  &#x60;&#x60;&#x60;    Request body  &#x60;&#x60;&#x60;json  {      \&quot;phone\&quot;: \&quot;+12025550195\&quot;,      \&quot;isNewsletterOptIn\&quot;: false   }  &#x60;&#x60;&#x60;    ### Client address    In order to update the &#x60;receiverName&#x60; of an existing address, the data entity is &#x60;AD&#x60; and the request would look like this:    PATCH  &#x60;&#x60;&#x60;  https://examplestore.vtexcommercestable.com.br/api/dataentities/Address/documents/123456789abc  &#x60;&#x60;&#x60;    Request body  &#x60;&#x60;&#x60;json  {      \&quot;receiverName\&quot;: \&quot;Lois Lane\&quot;  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentsApi;

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

    DocumentsApi apiInstance = new DocumentsApi(defaultClient);
    String dataEntityName = "Client"; // String | Name of the data entity. Defined by the api. Examples of native data entities you can use are `CL` for client profiles and `AD` for client addresses.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String id = "Client-b818cbda-e489-11e6-94f4-0ac138d2d42e"; // String | ID of the Document.
    Map<String, String> requestBody = new HashMap(); // Map<String, String> | 
    String where = "firstName is not null."; // String | Filter specification.
    String schema = "schema"; // String | Name of the schema the document to be created needs to be compliant with.
    try {
      DocumentResponse result = apiInstance.updatepartialdocument(dataEntityName, accept, id, requestBody, where, schema);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentsApi#updatepartialdocument");
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
| **dataEntityName** | **String**| Name of the data entity. Defined by the api. Examples of native data entities you can use are &#x60;CL&#x60; for client profiles and &#x60;AD&#x60; for client addresses. | |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | |
| **id** | **String**| ID of the Document. | |
| **requestBody** | [**Map&lt;String, String&gt;**](String.md)|  | |
| **where** | **String**| Filter specification. | [optional] |
| **schema** | **String**| Name of the schema the document to be created needs to be compliant with. | [optional] |

### Return type

[**DocumentResponse**](DocumentResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

