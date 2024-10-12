# DocumentApi

All URIs are relative to *http://www.bclaws.ca/civix*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**documentIdAspectIdCivixIndexIdCivixDocumentIdGet**](DocumentApi.md#documentIdAspectIdCivixIndexIdCivixDocumentIdGet) | **GET** /document/id/{aspectId}/{civixIndexId}/{civixDocumentId} | Retrieves a specific document from the BCLaws legislative repository (HTML format) |
| [**documentIdAspectIdCivixIndexIdCivixDocumentIdSearchSearchStringGet**](DocumentApi.md#documentIdAspectIdCivixIndexIdCivixDocumentIdSearchSearchStringGet) | **GET** /document/id/{aspectId}/{civixIndexId}/{civixDocumentId}/search/{searchString} | Retrieves a specific document from the BCLaws legislative repository with search text highlighted (HTML format) |
| [**documentIdAspectIdCivixIndexIdCivixDocumentIdXmlGet**](DocumentApi.md#documentIdAspectIdCivixIndexIdCivixDocumentIdXmlGet) | **GET** /document/id/{aspectId}/{civixIndexId}/{civixDocumentId}/xml | Retrieves a specific document from the BCLaws legislative repository (XML format) |
| [**documentIdAspectIdCivixIndexIdCivixDocumentIdXmlSearchSearchStringGet**](DocumentApi.md#documentIdAspectIdCivixIndexIdCivixDocumentIdXmlSearchSearchStringGet) | **GET** /document/id/{aspectId}/{civixIndexId}/{civixDocumentId}/xml/search/{searchString} | Retrieves a specific document from the BCLaws legislative repository with search text highlighted (XML format) |


<a id="documentIdAspectIdCivixIndexIdCivixDocumentIdGet"></a>
# **documentIdAspectIdCivixIndexIdCivixDocumentIdGet**
> documentIdAspectIdCivixIndexIdCivixDocumentIdGet(aspectId, civixIndexId, civixDocumentId)

Retrieves a specific document from the BCLaws legislative repository (HTML format)

The /document API allows you to retrieve actual documents from the BCLaws legislative repository. To retrieve a document from the repository you need the aspect identifier and two other specific pieces of information about the document: the index identifier and the document identifier. These unique identifiers can be retrieved from the /content API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://www.bclaws.ca/civix");

    DocumentApi apiInstance = new DocumentApi(defaultClient);
    String aspectId = "complete"; // String | The identifier of the 'aspect' (content group) to search
    String civixIndexId = "statreg"; // String | Index identification code
    String civixDocumentId = "01009_01"; // String | The document identification code for an index or directory
    try {
      apiInstance.documentIdAspectIdCivixIndexIdCivixDocumentIdGet(aspectId, civixIndexId, civixDocumentId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentApi#documentIdAspectIdCivixIndexIdCivixDocumentIdGet");
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
| **aspectId** | **String**| The identifier of the &#39;aspect&#39; (content group) to search | [default to complete] [enum: complete, corpreg, bcgaz1, bcgaz2, oic, psl, ecb, hscr, arch_oic] |
| **civixIndexId** | **String**| Index identification code | [default to statreg] |
| **civixDocumentId** | **String**| The document identification code for an index or directory | [default to 01009_01] |

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
| **200** | List documents and directories within the aspect. |  -  |

<a id="documentIdAspectIdCivixIndexIdCivixDocumentIdSearchSearchStringGet"></a>
# **documentIdAspectIdCivixIndexIdCivixDocumentIdSearchSearchStringGet**
> documentIdAspectIdCivixIndexIdCivixDocumentIdSearchSearchStringGet(aspectId, civixIndexId, civixDocumentId, searchString)

Retrieves a specific document from the BCLaws legislative repository with search text highlighted (HTML format)

The /document API allows you to retrieve actual documents from the BCLaws legislative repository. To retrieve a document from the repository you need the aspect identifier and two other specific pieces of information about the document: the index identifier and the document identifier. These unique identifiers can be retrieved from the /content API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://www.bclaws.ca/civix");

    DocumentApi apiInstance = new DocumentApi(defaultClient);
    String aspectId = "complete"; // String | The identifier of the 'aspect' (content group) to search
    String civixIndexId = "statreg"; // String | Index identification code
    String civixDocumentId = "01009_01"; // String | The document identification code for an index or directory
    String searchString = "water"; // String | The text to search for within the document
    try {
      apiInstance.documentIdAspectIdCivixIndexIdCivixDocumentIdSearchSearchStringGet(aspectId, civixIndexId, civixDocumentId, searchString);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentApi#documentIdAspectIdCivixIndexIdCivixDocumentIdSearchSearchStringGet");
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
| **aspectId** | **String**| The identifier of the &#39;aspect&#39; (content group) to search | [default to complete] [enum: complete, corpreg, bcgaz1, bcgaz2, oic, psl, ecb, hscr, arch_oic] |
| **civixIndexId** | **String**| Index identification code | [default to statreg] |
| **civixDocumentId** | **String**| The document identification code for an index or directory | [default to 01009_01] |
| **searchString** | **String**| The text to search for within the document | [default to water] |

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
| **200** | List documents and directories within the aspect. |  -  |

<a id="documentIdAspectIdCivixIndexIdCivixDocumentIdXmlGet"></a>
# **documentIdAspectIdCivixIndexIdCivixDocumentIdXmlGet**
> documentIdAspectIdCivixIndexIdCivixDocumentIdXmlGet(aspectId, civixIndexId, civixDocumentId)

Retrieves a specific document from the BCLaws legislative repository (XML format)

The /document API allows you to retrieve actual documents from the BCLaws legislative repository. To retrieve a document from the repository you need the aspect identifier and two other specific pieces of information about the document: the index identifier and the document identifier. These unique identifiers can be retrieved from the /content API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://www.bclaws.ca/civix");

    DocumentApi apiInstance = new DocumentApi(defaultClient);
    String aspectId = "complete"; // String | The identifier of the 'aspect' (content group) to search
    String civixIndexId = "statreg"; // String | Index identification code
    String civixDocumentId = "01009_01"; // String | The document identification code for an index or directory
    try {
      apiInstance.documentIdAspectIdCivixIndexIdCivixDocumentIdXmlGet(aspectId, civixIndexId, civixDocumentId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentApi#documentIdAspectIdCivixIndexIdCivixDocumentIdXmlGet");
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
| **aspectId** | **String**| The identifier of the &#39;aspect&#39; (content group) to search | [default to complete] [enum: complete, corpreg, bcgaz1, bcgaz2, oic, psl, ecb, hscr, arch_oic] |
| **civixIndexId** | **String**| Index identification code | [default to statreg] |
| **civixDocumentId** | **String**| The document identification code for an index or directory | [default to 01009_01] |

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
| **200** | List documents and directories within the aspect. |  -  |

<a id="documentIdAspectIdCivixIndexIdCivixDocumentIdXmlSearchSearchStringGet"></a>
# **documentIdAspectIdCivixIndexIdCivixDocumentIdXmlSearchSearchStringGet**
> documentIdAspectIdCivixIndexIdCivixDocumentIdXmlSearchSearchStringGet(aspectId, civixIndexId, civixDocumentId, searchString)

Retrieves a specific document from the BCLaws legislative repository with search text highlighted (XML format)

The /document API allows you to retrieve actual documents from the BCLaws legislative repository. To retrieve a document from the repository you need the aspect identifier and two other specific pieces of information about the document: the index identifier and the document identifier. These unique identifiers can be retrieved from the /content API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://www.bclaws.ca/civix");

    DocumentApi apiInstance = new DocumentApi(defaultClient);
    String aspectId = "complete"; // String | The identifier of the 'aspect' (content group) to search
    String civixIndexId = "statreg"; // String | Index identification code
    String civixDocumentId = "01009_01"; // String | The document identification code for an index or directory
    String searchString = "water"; // String | The text to search for within the document
    try {
      apiInstance.documentIdAspectIdCivixIndexIdCivixDocumentIdXmlSearchSearchStringGet(aspectId, civixIndexId, civixDocumentId, searchString);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentApi#documentIdAspectIdCivixIndexIdCivixDocumentIdXmlSearchSearchStringGet");
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
| **aspectId** | **String**| The identifier of the &#39;aspect&#39; (content group) to search | [default to complete] [enum: complete, corpreg, bcgaz1, bcgaz2, oic, psl, ecb, hscr, arch_oic] |
| **civixIndexId** | **String**| Index identification code | [default to statreg] |
| **civixDocumentId** | **String**| The document identification code for an index or directory | [default to 01009_01] |
| **searchString** | **String**| The text to search for within the document | [default to water] |

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
| **200** | List documents and directories within the aspect. |  -  |

