# SearchApi

All URIs are relative to *http://apicurio.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**searchArtifacts**](SearchApi.md#searchArtifacts) | **GET** /search/artifacts | Search for artifacts |
| [**searchVersions**](SearchApi.md#searchVersions) | **GET** /search/artifacts/{artifactId}/versions | Search artifact versions |


<a id="searchArtifacts"></a>
# **searchArtifacts**
> ArtifactSearchResults searchArtifacts(offset, limit, search, over, order)

Search for artifacts

Returns a paginated list of all artifacts that match the provided search criteria. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apicurio.local");

    SearchApi apiInstance = new SearchApi(defaultClient);
    Integer offset = 0; // Integer | The number of artifacts to skip before starting to collect the result set.
    Integer limit = 20; // Integer | The number of artifacts to return.
    String search = "search_example"; // String | The text to search.
    String over = "everything"; // String | What fields to search.
    String order = "asc"; // String | Sort order, ascending or descending.
    try {
      ArtifactSearchResults result = apiInstance.searchArtifacts(offset, limit, search, over, order);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#searchArtifacts");
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
| **offset** | **Integer**| The number of artifacts to skip before starting to collect the result set. | [default to 0] |
| **limit** | **Integer**| The number of artifacts to return. | [default to 20] |
| **search** | **String**| The text to search. | [optional] |
| **over** | **String**| What fields to search. | [optional] [enum: everything, name, description, labels] |
| **order** | **String**| Sort order, ascending or descending. | [optional] [enum: asc, desc] |

### Return type

[**ArtifactSearchResults**](ArtifactSearchResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | On a successful response, returns a result set of artifacts - one for each artifact in the registry that matches the criteria. |  -  |
| **500** | Common response for all operations that can fail with an unexpected server error. |  -  |

<a id="searchVersions"></a>
# **searchVersions**
> VersionSearchResults searchVersions(artifactId, offset, limit)

Search artifact versions

Searches for versions of a specific artifact.  This is typically used to get a listing of all versions of an artifact (for example, in a user interface).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apicurio.local");

    SearchApi apiInstance = new SearchApi(defaultClient);
    String artifactId = "artifactId_example"; // String | The artifact ID.  Can be a string (client-provided) or integer (server-generated) representing the unique artifact identifier.
    Integer offset = 56; // Integer | The number of versions to skip before starting to collect the result set.
    Integer limit = 56; // Integer | The number of versions to return.
    try {
      VersionSearchResults result = apiInstance.searchVersions(artifactId, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#searchVersions");
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
| **artifactId** | **String**| The artifact ID.  Can be a string (client-provided) or integer (server-generated) representing the unique artifact identifier. | |
| **offset** | **Integer**| The number of versions to skip before starting to collect the result set. | |
| **limit** | **Integer**| The number of versions to return. | |

### Return type

[**VersionSearchResults**](VersionSearchResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | On a successful response, returns a result set of versions - one for each version of the artifact. |  -  |
| **404** | Common response for all operations that can return a &#x60;404&#x60; error. |  -  |
| **500** | Common response for all operations that can fail with an unexpected server error. |  -  |

