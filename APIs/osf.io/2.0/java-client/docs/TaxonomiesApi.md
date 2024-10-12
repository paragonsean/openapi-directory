# TaxonomiesApi

All URIs are relative to *https://api.test.osf.io/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**taxonomiesList**](TaxonomiesApi.md#taxonomiesList) | **GET** /taxonomies/ | List all taxonomies |
| [**taxonomiesRead**](TaxonomiesApi.md#taxonomiesRead) | **GET** /taxonomies/{taxonomy_id}/ | Retrieve a taxonomy |


<a id="taxonomiesList"></a>
# **taxonomiesList**
> List&lt;Taxonomy&gt; taxonomiesList()

List all taxonomies

 A paginated list of all [bepress disciplines taxonomies](https://www.bepress.com/wp-content/uploads/2016/12/Digital-Commons-Disciplines-taxonomy-2017-01.pdf). Note: this API endpoint is under active development, and is subject to change in the future. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of up to 10 taxonomies. Each resource in the array is a separate taxonomy object.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  This request should never return an error. #### Filtering You can optionally request that the response only include taxonomies that match your filters by utilizing the &#x60;filter&#x60; query parameter, e.g. https://api.osf.io/v2/taxonomies/?filter[&#39;id&#39;]&#x3D;&#39;{taxonomy_id}&#39;.  Taxonomies may be filtered by their &#x60;id&#x60;, &#x60;parents&#x60;, and &#x60;text&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaxonomiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    TaxonomiesApi apiInstance = new TaxonomiesApi(defaultClient);
    try {
      List<Taxonomy> result = apiInstance.taxonomiesList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaxonomiesApi#taxonomiesList");
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

[**List&lt;Taxonomy&gt;**](Taxonomy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="taxonomiesRead"></a>
# **taxonomiesRead**
> Taxonomy taxonomiesRead(taxonomyId)

Retrieve a taxonomy

Retrieves the details of a taxonomy. #### Returns  Returns a JSON object with a &#x60;data&#x60; key containing the representation of the requested taxonomy, if the request is successful.  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaxonomiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    TaxonomiesApi apiInstance = new TaxonomiesApi(defaultClient);
    String taxonomyId = "taxonomyId_example"; // String | The unique identifier of the taxonomy.
    try {
      Taxonomy result = apiInstance.taxonomiesRead(taxonomyId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaxonomiesApi#taxonomiesRead");
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
| **taxonomyId** | **String**| The unique identifier of the taxonomy. | |

### Return type

[**Taxonomy**](Taxonomy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

