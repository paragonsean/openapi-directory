# PreprintsApi

All URIs are relative to *https://api.test.osf.io/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**preprintsBibliographicContributorsList**](PreprintsApi.md#preprintsBibliographicContributorsList) | **GET** /preprints/{preprint_id}/bibliographic_contributors/ | List all Bibliographic Contributors |
| [**preprintsCitationList**](PreprintsApi.md#preprintsCitationList) | **GET** /preprints/{preprint_id}/citation/ | Retrieve citation details |
| [**preprintsCitationRead**](PreprintsApi.md#preprintsCitationRead) | **GET** /preprints/{preprint_id}/citation/{style_id}/ | Retrieve a styled citation |
| [**preprintsContributorRead**](PreprintsApi.md#preprintsContributorRead) | **GET** /preprints/{preprint_id}/contributors/{user_id}/ | Retrieve a contributor |
| [**preprintsContributorsCreate**](PreprintsApi.md#preprintsContributorsCreate) | **POST** /preprints/{preprint_id}/contributors/ | Create a Contributor |
| [**preprintsContributorsList**](PreprintsApi.md#preprintsContributorsList) | **GET** /preprints/{preprint_id}/contributors/ | List all Contributors for a Preprint |
| [**preprintsCreate**](PreprintsApi.md#preprintsCreate) | **POST** /preprints/ | Create a preprint |
| [**preprintsList**](PreprintsApi.md#preprintsList) | **GET** /preprints/ | List all preprints |
| [**preprintsPartialUpdate**](PreprintsApi.md#preprintsPartialUpdate) | **PATCH** /preprints/{preprint_id}/ | Update a preprint |
| [**preprintsRead**](PreprintsApi.md#preprintsRead) | **GET** /preprints/{preprint_id}/ | Retrieve a preprint |


<a id="preprintsBibliographicContributorsList"></a>
# **preprintsBibliographicContributorsList**
> List&lt;Contributor1&gt; preprintsBibliographicContributorsList(preprintId)

List all Bibliographic Contributors

A paginated list of the Preprint&#39;s Bibliographic Contributors, sorted by their index. Contributors are users who can make changes to the Preprint. Contributors with WRITE permissions may edit preprint details, and ADMIN Contributors may add or remove other Contributors.  Contributors are categorized as either \&quot;bibliographic\&quot; or \&quot;non-bibliographic\&quot;. From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not.  Note that if an anonymous view_only key is being used to view the list of contributors, the user relationship will not be exposed and the contributor ID will be an empty string.  #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of 10 contributors. Each resource in the array contains the full representation of the contributor, meaning additional requests to a contributor&#39;s detail view are not necessary. Additionally, the full representation of the user this contributor represents is automatically embedded within the &#x60;data&#x60; key of the response.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination). #### Filtering You can optionally request that the response only include contributors that match your filters by utilizing the &#x60;filter&#x60; query parameter, e.g. https://api.osf.io/v2/preprints/y9jdt/contributors/?filter[bibliographic]&#x3D;true.  Contributors may be filtered by their &#x60;bibliographic&#x60; and &#x60;permission&#x60; attributes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreprintsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    PreprintsApi apiInstance = new PreprintsApi(defaultClient);
    String preprintId = "preprintId_example"; // String | The unique identifier of the preprint.
    try {
      List<Contributor1> result = apiInstance.preprintsBibliographicContributorsList(preprintId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreprintsApi#preprintsBibliographicContributorsList");
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
| **preprintId** | **String**| The unique identifier of the preprint. | |

### Return type

[**List&lt;Contributor1&gt;**](Contributor1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="preprintsCitationList"></a>
# **preprintsCitationList**
> CitationDetail preprintsCitationList(preprintId)

Retrieve citation details

The citation details for a preprint, in CSL format. #### Returns Returns a JSON object with a &#x60;data&#x60; key that contains the representation of the details necessary for the preprint citation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreprintsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    PreprintsApi apiInstance = new PreprintsApi(defaultClient);
    String preprintId = "preprintId_example"; // String | The unique identifier of the preprint whose citation you wish to retrieve.
    try {
      CitationDetail result = apiInstance.preprintsCitationList(preprintId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreprintsApi#preprintsCitationList");
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
| **preprintId** | **String**| The unique identifier of the preprint whose citation you wish to retrieve. | |

### Return type

[**CitationDetail**](CitationDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="preprintsCitationRead"></a>
# **preprintsCitationRead**
> StyledCitation preprintsCitationRead(styleId, preprintId)

Retrieve a styled citation

The citation for a preprint in a specific style. #### Returns Returns a JSON object with a &#x60;data&#x60; key that contains the representation of the preprint citation, in the requested style.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreprintsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    PreprintsApi apiInstance = new PreprintsApi(defaultClient);
    String styleId = "styleId_example"; // String | The unique identifier of the citation style.
    String preprintId = "preprintId_example"; // String | The unique identifier of the preprint.
    try {
      StyledCitation result = apiInstance.preprintsCitationRead(styleId, preprintId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreprintsApi#preprintsCitationRead");
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
| **styleId** | **String**| The unique identifier of the citation style. | |
| **preprintId** | **String**| The unique identifier of the preprint. | |

### Return type

[**StyledCitation**](StyledCitation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="preprintsContributorRead"></a>
# **preprintsContributorRead**
> preprintsContributorRead(preprintId, userId)

Retrieve a contributor

Retrieves the details of a contributor on this Preprint. Contributors are categorized as either \&quot;bibliographic\&quot; or \&quot;non-bibliographic\&quot;. From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not.  Note that if an anonymous view_only key is being used to view the list of contributors, the user relationship will not be exposed and the contributor ID will be an empty string. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the requested contributor, if the request is successful.  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreprintsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    PreprintsApi apiInstance = new PreprintsApi(defaultClient);
    String preprintId = "preprintId_example"; // String | The unique identifier of the Preprint.
    String userId = "userId_example"; // String | The unique identifier of the user.
    try {
      apiInstance.preprintsContributorRead(preprintId, userId);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreprintsApi#preprintsContributorRead");
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
| **preprintId** | **String**| The unique identifier of the Preprint. | |
| **userId** | **String**| The unique identifier of the user. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="preprintsContributorsCreate"></a>
# **preprintsContributorsCreate**
> preprintsContributorsCreate(preprintId, contributor1)

Create a Contributor

Adds a contributor to a Preprint, effectively creating a relationship between the Preprint and a user.  Contributors are users who can make changes to the Preprint. Contributors with WRITE permissions may edit preprint details, and ADMIN Contributors may add or remove other Contributors.  Contributors are categorized as either \&quot;bibliographic\&quot; or \&quot;non-bibliographic\&quot; contributors. From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not. #### Permissions Only project administrators can add contributors to a Preprint. #### Required A relationship object with a &#x60;data&#x60; key, containing the &#x60;users&#x60; type and valid user ID is required.  All attributes describing the relationship between the Preprint and the user are optional. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the new contributor, if the request is successful.  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreprintsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    PreprintsApi apiInstance = new PreprintsApi(defaultClient);
    String preprintId = "preprintId_example"; // String | The unique identifier of the Preprint.
    Contributor1 contributor1 = new Contributor1(); // Contributor1 | 
    try {
      apiInstance.preprintsContributorsCreate(preprintId, contributor1);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreprintsApi#preprintsContributorsCreate");
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
| **preprintId** | **String**| The unique identifier of the Preprint. | |
| **contributor1** | [**Contributor1**](Contributor1.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |

<a id="preprintsContributorsList"></a>
# **preprintsContributorsList**
> List&lt;Contributor1&gt; preprintsContributorsList(preprintId)

List all Contributors for a Preprint

A paginated list of the Preprint&#39;s Contributors, sorted by their index.  Contributors are users who can make changes to the Preprint. Contributors with WRITE permissions may edit preprint details, and ADMIN Contributors may add or remove other Contributors.  Contributors are categorized as either \&quot;bibliographic\&quot; or \&quot;non-bibliographic\&quot;. From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not.  Note that if an anonymous view_only key is being used to view the list of Contributors, the user relationship will not be exposed and the Contributor ID will be an empty string.  #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of 10 contributors. Each resource in the array contains the full representation of the contributor, meaning additional requests to a contributor&#39;s detail view are not necessary. Additionally, the full representation of the user this contributor represents is automatically embedded within the &#x60;data&#x60; key of the response.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination). #### Filtering You can optionally request that the response only include contributors that match your filters by utilizing the &#x60;filter&#x60; query parameter, e.g. https://api.osf.io/v2/preprints/y9jdt/contributors/?filter[bibliographic]&#x3D;true.  Contributors may be filtered by their &#x60;bibliographic&#x60; and &#x60;permission&#x60; attributes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreprintsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    PreprintsApi apiInstance = new PreprintsApi(defaultClient);
    String preprintId = "preprintId_example"; // String | The unique identifier of the preprint.
    try {
      List<Contributor1> result = apiInstance.preprintsContributorsList(preprintId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreprintsApi#preprintsContributorsList");
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
| **preprintId** | **String**| The unique identifier of the preprint. | |

### Return type

[**List&lt;Contributor1&gt;**](Contributor1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="preprintsCreate"></a>
# **preprintsCreate**
> preprintsCreate(preprint)

Create a preprint

Creates a new preprint. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the created preprint, if the request is successful.  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes]() to understand why this request may have failed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreprintsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    PreprintsApi apiInstance = new PreprintsApi(defaultClient);
    Preprint preprint = new Preprint(); // Preprint | 
    try {
      apiInstance.preprintsCreate(preprint);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreprintsApi#preprintsCreate");
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
| **preprint** | [**Preprint**](Preprint.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |

<a id="preprintsList"></a>
# **preprintsList**
> List&lt;Preprint&gt; preprintsList()

List all preprints

 A paginated list of preprints from all preprint providers. The returned preprints are sorted by their creation date, with the most recent preprints appearing first. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of 10 preprints. Each resource in the array is a separate preprint object.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  This request should never return an error. #### Filtering You can optionally request that the response only include preprints that match your filters by utilizing the &#x60;filter&#x60; query parameter, e.g. https://api.osf.io/v2/preprints/?filter[provider]&#x3D;socarxiv.  Preprints may be filtered by their &#x60;id&#x60;, &#x60;is_published&#x60;, &#x60;date_created&#x60;, &#x60;date_modified&#x60;, and &#x60;provider&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreprintsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    PreprintsApi apiInstance = new PreprintsApi(defaultClient);
    try {
      List<Preprint> result = apiInstance.preprintsList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreprintsApi#preprintsList");
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

<a id="preprintsPartialUpdate"></a>
# **preprintsPartialUpdate**
> preprintsPartialUpdate(preprintId, body)

Update a preprint

Updates the specified preprint by setting the values of the parameters passed. Any parameters not provided will be left unchanged. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the new representation of the updated preprint, if the request is successful.  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes]() to understand why this request may have failed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreprintsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    PreprintsApi apiInstance = new PreprintsApi(defaultClient);
    String preprintId = "preprintId_example"; // String | The unique identifier of the preprint.
    Object body = null; // Object | 
    try {
      apiInstance.preprintsPartialUpdate(preprintId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreprintsApi#preprintsPartialUpdate");
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
| **preprintId** | **String**| The unique identifier of the preprint. | |
| **body** | **Object**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="preprintsRead"></a>
# **preprintsRead**
> Preprint preprintsRead(preprintId)

Retrieve a preprint

Retrieves the details of a preprint. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the requested preprint, if the request is successful.  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreprintsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    PreprintsApi apiInstance = new PreprintsApi(defaultClient);
    String preprintId = "preprintId_example"; // String | The unique identifier of the preprint.
    try {
      Preprint result = apiInstance.preprintsRead(preprintId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreprintsApi#preprintsRead");
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
| **preprintId** | **String**| The unique identifier of the preprint. | |

### Return type

[**Preprint**](Preprint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

