# SchemaResponsesApi

All URIs are relative to *https://api.test.osf.io/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**schemaResponseDelete**](SchemaResponsesApi.md#schemaResponseDelete) | **DELETE** /schema_responses/{schema_response_id} | Delete a Incomplete Schema Response |
| [**schemaResponsePatch**](SchemaResponsesApi.md#schemaResponsePatch) | **PATCH** /schema_responses/{schema_response_id} | Update a Registration&#39;s Schema Response |
| [**schemaResponsePpost**](SchemaResponsesApi.md#schemaResponsePpost) | **POST** /schema_responses/ | Create a new Schema Response |
| [**schemaResponsesList**](SchemaResponsesApi.md#schemaResponsesList) | **GET** /schema_responses/ | List all Schema Responses |
| [**schemaResponsesRead**](SchemaResponsesApi.md#schemaResponsesRead) | **GET** /schema_responses/{schema_response_id} | Retrieve a Schema Response |


<a id="schemaResponseDelete"></a>
# **schemaResponseDelete**
> schemaResponseDelete(schemaResponseId)

Delete a Incomplete Schema Response

This endpoint deletes a new Schema Response. Schema Responses can only be deleted in the &#x60;in_progress&#x60; state. Once a Schema Response is transitioned to an &#x60;approved&#x60; it is immutable and another Schema Response must be created to update the Schema Response for that registration. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing an updated representation of the requested Schema Response, if the request is successful. #### Errors If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SchemaResponsesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    SchemaResponsesApi apiInstance = new SchemaResponsesApi(defaultClient);
    String schemaResponseId = "schemaResponseId_example"; // String | The unique identifier of the Registration Schema example `6176c9d45e01f100091d4f94`.
    try {
      apiInstance.schemaResponseDelete(schemaResponseId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SchemaResponsesApi#schemaResponseDelete");
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
| **schemaResponseId** | **String**| The unique identifier of the Registration Schema example &#x60;6176c9d45e01f100091d4f94&#x60;. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

<a id="schemaResponsePatch"></a>
# **schemaResponsePatch**
> SchemaResponses schemaResponsePatch(schemaResponseId, schemaResponses)

Update a Registration&#39;s Schema Response

Patching to this endpoint allows one to directly edit the revision responses on the Schema Response of a Registration if that Schema Response is in an &#x60;in_progress&#x60; state. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing an updated representation of the requested Schema Response, if the request is successful. #### Errors If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SchemaResponsesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    SchemaResponsesApi apiInstance = new SchemaResponsesApi(defaultClient);
    String schemaResponseId = "schemaResponseId_example"; // String | The unique identifier of the Registration Schema example `6176c9d45e01f100091d4f94`.
    SchemaResponses schemaResponses = new SchemaResponses(); // SchemaResponses | 
    try {
      SchemaResponses result = apiInstance.schemaResponsePatch(schemaResponseId, schemaResponses);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SchemaResponsesApi#schemaResponsePatch");
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
| **schemaResponseId** | **String**| The unique identifier of the Registration Schema example &#x60;6176c9d45e01f100091d4f94&#x60;. | |
| **schemaResponses** | [**SchemaResponses**](SchemaResponses.md)|  | |

### Return type

[**SchemaResponses**](SchemaResponses.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | OK |  -  |

<a id="schemaResponsePpost"></a>
# **schemaResponsePpost**
> SchemaResponses schemaResponsePpost(schemaResponses)

Create a new Schema Response

This endpoint creates a new Schema Response with an &#x60;in_progress&#x60; state. A new response can only be created if the current schema response is in an &#x60;approved&#x60; state. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing an updated representation of the requested Schema Response, if the request is successful. #### Errors If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SchemaResponsesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    SchemaResponsesApi apiInstance = new SchemaResponsesApi(defaultClient);
    SchemaResponses schemaResponses = new SchemaResponses(); // SchemaResponses | 
    try {
      SchemaResponses result = apiInstance.schemaResponsePpost(schemaResponses);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SchemaResponsesApi#schemaResponsePpost");
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
| **schemaResponses** | [**SchemaResponses**](SchemaResponses.md)|  | |

### Return type

[**SchemaResponses**](SchemaResponses.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | OK |  -  |

<a id="schemaResponsesList"></a>
# **schemaResponsesList**
> SchemaResponses schemaResponsesList()

List all Schema Responses

This retrieves a paginated list of all active Schema Responses that are public. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys. The &#x60;data&#x60; key contains an array of 10 Schema Responses. Each resource in the array is a separate Registration Schemas object. The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination). #### Errors This request should never return an error.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SchemaResponsesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    SchemaResponsesApi apiInstance = new SchemaResponsesApi(defaultClient);
    try {
      SchemaResponses result = apiInstance.schemaResponsesList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SchemaResponsesApi#schemaResponsesList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SchemaResponses**](SchemaResponses.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="schemaResponsesRead"></a>
# **schemaResponsesRead**
> SchemaResponses schemaResponsesRead(schemaResponseId)

Retrieve a Schema Response

This retrieves a single Schema response using it&#39;s id. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the requested Schema Response, if the request is successful. #### Errors If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SchemaResponsesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    SchemaResponsesApi apiInstance = new SchemaResponsesApi(defaultClient);
    String schemaResponseId = "schemaResponseId_example"; // String | The unique identifier of the Registration Schema example `6176c9d45e01f100091d4f94`.
    try {
      SchemaResponses result = apiInstance.schemaResponsesRead(schemaResponseId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SchemaResponsesApi#schemaResponsesRead");
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
| **schemaResponseId** | **String**| The unique identifier of the Registration Schema example &#x60;6176c9d45e01f100091d4f94&#x60;. | |

### Return type

[**SchemaResponses**](SchemaResponses.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

