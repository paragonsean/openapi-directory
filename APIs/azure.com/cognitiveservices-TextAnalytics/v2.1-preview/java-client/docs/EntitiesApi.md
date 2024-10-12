# EntitiesApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**entities**](EntitiesApi.md#entities) | **POST** /entities | The API returns a list of recognized entities in a given document. |


<a id="entities"></a>
# **entities**
> EntitiesBatchResultV2dot1 entities(input)

The API returns a list of recognized entities in a given document.

The API returns a list of recognized entities in a given document. To get even more information on each recognized entity we recommend using the Bing Entity Search API by querying for the recognized entities names. See the &lt;a href&#x3D;\&quot;https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/text-analytics-supported-languages\&quot;&gt;Supported languages in Text Analytics API&lt;/a&gt; for the list of enabled languages.The API returns a list of known entities and general named entities (\&quot;Person\&quot;, \&quot;Location\&quot;, \&quot;Organization\&quot; etc) in a given document. Known entities are returned with Wikipedia Id and Wikipedia link, and also Bing Id which can be used in Bing Entity Search API. General named entities are returned with entity types. If a general named entity is also a known entity, then all information regarding it (Wikipedia Id, Bing Id, entity type etc) will be returned. See the &lt;a href&#x3D;\&quot;https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/how-tos/text-analytics-how-to-entity-linking#supported-types-for-named-entity-recognition\&quot;&gt;Supported Entity Types in Text Analytics API&lt;/a&gt; for the list of supported Entity Types. See the &lt;a href&#x3D;\&quot;https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/text-analytics-supported-languages\&quot;&gt;Supported languages in Text Analytics API&lt;/a&gt; for the list of enabled languages.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    EntitiesApi apiInstance = new EntitiesApi(defaultClient);
    MultiLanguageBatchInput input = new MultiLanguageBatchInput(); // MultiLanguageBatchInput | Collection of documents to analyze.
    try {
      EntitiesBatchResultV2dot1 result = apiInstance.entities(input);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntitiesApi#entities");
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
| **input** | [**MultiLanguageBatchInput**](MultiLanguageBatchInput.md)| Collection of documents to analyze. | |

### Return type

[**EntitiesBatchResultV2dot1**](EntitiesBatchResultV2dot1.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful call results in a list of recognized entities returned for each valid document |  -  |
| **0** | Error Response |  -  |

