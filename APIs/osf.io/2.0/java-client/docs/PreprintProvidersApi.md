# PreprintProvidersApi

All URIs are relative to *https://api.test.osf.io/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**preprintProviderDetail**](PreprintProvidersApi.md#preprintProviderDetail) | **GET** /preprint_providers/{preprint_provider_id}/ | Retrieve a preprint provider |
| [**preprintProviderLicensesList**](PreprintProvidersApi.md#preprintProviderLicensesList) | **GET** /preprint_providers/{preprint_provider_id}/licenses/ | List all licenses |
| [**preprintProviderList**](PreprintProvidersApi.md#preprintProviderList) | **GET** /preprint_providers/ | List all preprint providers |
| [**preprintProviderTaxonomiesList**](PreprintProvidersApi.md#preprintProviderTaxonomiesList) | **GET** /preprint_providers/{preprint_provider_id}/taxonomies/ | List all taxonomies |
| [**preprintProvidersPreprintsList**](PreprintProvidersApi.md#preprintProvidersPreprintsList) | **GET** /preprint_providers/{preprint_provider_id}/preprints/ | List all preprints |


<a id="preprintProviderDetail"></a>
# **preprintProviderDetail**
> PreprintProviders preprintProviderDetail(preprintProviderId)

Retrieve a preprint provider

Retrieves the details of a preprint provider. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the requested preprint provider, if the request is successful.  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.  #### Acceptable Subjects Structure Each preprint provider specifies acceptable subjects. &#x60;subjects_acceptable&#x60; is an array found in &#x60;attributes&#x60;. Subjects consist of general parent subjects (e.g., Engineering), more specific child subjects (e.g., Aerospace Engineering), and even more specific grandchild subjects (e.g., Aerodynamics and Fluid Mechanics). Subjects can only be nested 3 deep.       \&quot;subjects_acceptable\&quot;: [         [             [                 # Parent Subject:                 # Architecture                 \&quot;584240d954be81056ceca9e5\&quot;,                  # Child Subject:                 # Architectural Engineering                 \&quot;584240da54be81056cecac87\&quot;             ],             # Include all Architectural Engineering&#39;s children:             true         ],         [             [                 # Parent Subject:                 # Engineering                 \&quot;584240da54be81056cecaca9\&quot;,                  # Child Subject:                 # Aerospace Engineering                 \&quot;584240db54be81056cecacd6\&quot;,                  # Grandchild Subject:                 # Aerodynamics and Fluid Mechanics                 \&quot;584240da54be81056cecaa74\&quot;             ],             # All nestings 3 deep must be false             false         ]     ]  The above structure would allow Architecture, Architectural Engineering, all of Architectural Engineering&#39;s children, Engineering, Aerospace Engineering, and Aerodynamics and Fluid Mechanics.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreprintProvidersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    PreprintProvidersApi apiInstance = new PreprintProvidersApi(defaultClient);
    String preprintProviderId = "preprintProviderId_example"; // String | The unique identifier of the preprint provider.
    try {
      PreprintProviders result = apiInstance.preprintProviderDetail(preprintProviderId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreprintProvidersApi#preprintProviderDetail");
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
| **preprintProviderId** | **String**| The unique identifier of the preprint provider. | |

### Return type

[**PreprintProviders**](PreprintProviders.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="preprintProviderLicensesList"></a>
# **preprintProviderLicensesList**
> License preprintProviderLicensesList(preprintProviderId)

List all licenses

 A paginated list of the licenses allowed by a preprint provider. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of 10 preprint providers. Each resource in the array is a separate preprint provider object.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreprintProvidersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    PreprintProvidersApi apiInstance = new PreprintProvidersApi(defaultClient);
    String preprintProviderId = "preprintProviderId_example"; // String | The unique identifier of the preprint provider.
    try {
      License result = apiInstance.preprintProviderLicensesList(preprintProviderId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreprintProvidersApi#preprintProviderLicensesList");
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
| **preprintProviderId** | **String**| The unique identifier of the preprint provider. | |

### Return type

[**License**](License.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="preprintProviderList"></a>
# **preprintProviderList**
> PreprintProviders preprintProviderList()

List all preprint providers

 A paginated list of all preprint providers. The returned preprint providers are sorted by their creation date, with the most recent preprints appearing first. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of 10 preprint providers. Each resource in the array is a separate preprint provider object.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  This request should never return an error. #### Filtering You can optionally request that the response only include preprint providers that match your filters by utilizing the &#x60;filter&#x60; query parameter, e.g. https://api.osf.io/v2/preprint_providers/?filter[id]&#x3D;osf.  Preprint Providers may be filtered by their &#x60;id&#x60;, &#x60;name&#x60;,  and &#x60;description&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreprintProvidersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    PreprintProvidersApi apiInstance = new PreprintProvidersApi(defaultClient);
    try {
      PreprintProviders result = apiInstance.preprintProviderList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreprintProvidersApi#preprintProviderList");
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

[**PreprintProviders**](PreprintProviders.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="preprintProviderTaxonomiesList"></a>
# **preprintProviderTaxonomiesList**
> Taxonomy preprintProviderTaxonomiesList(preprintProviderId)

List all taxonomies

 A paginated list of the taxonomies for a preprint provider. The returned preprint providers taxonomies are sorted by their creation date, with the most recent preprints appearing first. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of 10 preprint providers. Each resource in the array is a separate preprint provider object.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreprintProvidersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    PreprintProvidersApi apiInstance = new PreprintProvidersApi(defaultClient);
    String preprintProviderId = "preprintProviderId_example"; // String | The unique identifier of the preprint provider.
    try {
      Taxonomy result = apiInstance.preprintProviderTaxonomiesList(preprintProviderId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreprintProvidersApi#preprintProviderTaxonomiesList");
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
| **preprintProviderId** | **String**| The unique identifier of the preprint provider. | |

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

<a id="preprintProvidersPreprintsList"></a>
# **preprintProvidersPreprintsList**
> List&lt;Preprint&gt; preprintProvidersPreprintsList(preprintProviderId)

List all preprints

 A paginated list of preprints from the specified preprint provider. The returned preprints are sorted by their creation date, with the most recent preprints appearing first. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of 10 preprints. Each resource in the array is a separate preprint object.  The &#x60;links&#x60; key contains a dictionary with keys that can be used for [pagination](#tag/Pagination).  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.  #### Filtering You can optionally request that the response only include preprints that match your filters by utilizing the &#x60;filter&#x60; query parameter, e.g. https://api.osf.io/v2/preprint_providers/osf/preprints/?filter[is_published]&#x3D;true.  Preprints may be filtered by their &#x60;id&#x60;, &#x60;is_published&#x60;, &#x60;date_created&#x60;, &#x60;date_modified&#x60;, and &#x60;provider&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreprintProvidersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    PreprintProvidersApi apiInstance = new PreprintProvidersApi(defaultClient);
    String preprintProviderId = "preprintProviderId_example"; // String | The unique identifier of the preprint provider.
    try {
      List<Preprint> result = apiInstance.preprintProvidersPreprintsList(preprintProviderId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreprintProvidersApi#preprintProvidersPreprintsList");
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
| **preprintProviderId** | **String**| The unique identifier of the preprint provider. | |

### Return type

[**List&lt;Preprint&gt;**](Preprint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

