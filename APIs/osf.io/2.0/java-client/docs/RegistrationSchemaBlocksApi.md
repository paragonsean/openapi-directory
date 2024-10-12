# RegistrationSchemaBlocksApi

All URIs are relative to *https://api.test.osf.io/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**schemaResponseBlocksRead**](RegistrationSchemaBlocksApi.md#schemaResponseBlocksRead) | **GET** /schema_responses/{schema_response_id}/schema_blocks/ | Retrieve a list of Registration Schema Blocks for a Schema Response |
| [**schemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdGet**](RegistrationSchemaBlocksApi.md#schemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdGet) | **GET** /schema_responses/{schema_response_id}/schema_blocks/{schema_response_block_id} | Retrieve a Registration Schema Block |


<a id="schemaResponseBlocksRead"></a>
# **schemaResponseBlocksRead**
> RegistrationSchemaBlock schemaResponseBlocksRead(schemaResponseId)

Retrieve a list of Registration Schema Blocks for a Schema Response

This returns a list of all the Registration Schema Blocks are contained in Registration Schema. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the requested Registration Schemas, if the request is successful. #### Errors If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrationSchemaBlocksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    RegistrationSchemaBlocksApi apiInstance = new RegistrationSchemaBlocksApi(defaultClient);
    String schemaResponseId = "schemaResponseId_example"; // String | The unique identifier of the Registration Schema example `6176c9d45e01f100091d4f94`.
    try {
      RegistrationSchemaBlock result = apiInstance.schemaResponseBlocksRead(schemaResponseId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationSchemaBlocksApi#schemaResponseBlocksRead");
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

[**RegistrationSchemaBlock**](RegistrationSchemaBlock.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="schemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdGet"></a>
# **schemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdGet**
> RegistrationSchemaBlock schemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdGet(schemaResponseId, schemaResponseBlockId)

Retrieve a Registration Schema Block

This returns a Registration Schema Block by it&#39;s ID. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the requested Registration Schemas, if the request is successful. #### Errors If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrationSchemaBlocksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    RegistrationSchemaBlocksApi apiInstance = new RegistrationSchemaBlocksApi(defaultClient);
    String schemaResponseId = "schemaResponseId_example"; // String | The unique identifier of the Registration Schema example `6176c9d45e01f100091d4f94`.
    String schemaResponseBlockId = "schemaResponseBlockId_example"; // String | The unique identifier of the Schema Response Block example `61b79f9eadbb5701424a2d5e`.
    try {
      RegistrationSchemaBlock result = apiInstance.schemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdGet(schemaResponseId, schemaResponseBlockId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationSchemaBlocksApi#schemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdGet");
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
| **schemaResponseBlockId** | **String**| The unique identifier of the Schema Response Block example &#x60;61b79f9eadbb5701424a2d5e&#x60;. | |

### Return type

[**RegistrationSchemaBlock**](RegistrationSchemaBlock.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

