# SubRoutesApi

All URIs are relative to *http://localhost:7700*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDisplayedAttributes_0**](SubRoutesApi.md#getDisplayedAttributes_0) | **GET** /indexes/books/settings/displayed-attributes | Get displayed attributes |
| [**getDistinctAttribute_0**](SubRoutesApi.md#getDistinctAttribute_0) | **GET** /indexes/books/settings/distinct-attribute | Get distinct attribute |
| [**getFaceting_0**](SubRoutesApi.md#getFaceting_0) | **GET** /indexes/books/settings/faceting | Get faceting |
| [**getFilterableAttributes_0**](SubRoutesApi.md#getFilterableAttributes_0) | **GET** /indexes/books/settings/filterable-attributes | Get filterable attributes |
| [**getPagination_0**](SubRoutesApi.md#getPagination_0) | **GET** /indexes/books/settings/pagination | Get pagination |
| [**getRankingRules_0**](SubRoutesApi.md#getRankingRules_0) | **GET** /indexes/books/settings/ranking-rules | Get ranking rules |
| [**getSearchableAttributes_0**](SubRoutesApi.md#getSearchableAttributes_0) | **GET** /indexes/books/settings/searchable-attributes | Get searchable attributes |
| [**getSortableAttributes_0**](SubRoutesApi.md#getSortableAttributes_0) | **GET** /indexes/books/settings/sortable-attributes | Get sortable attributes |
| [**getStopWords_0**](SubRoutesApi.md#getStopWords_0) | **GET** /indexes/books/settings/stop-words | Get stop-words |
| [**getSynonyms_0**](SubRoutesApi.md#getSynonyms_0) | **GET** /indexes/books/settings/synonyms | Get synonyms |
| [**getTypoTolerance_0**](SubRoutesApi.md#getTypoTolerance_0) | **GET** /indexes/books/settings/typo-tolerance | Get typo-tolerance |
| [**resetDisplayedAttributes_0**](SubRoutesApi.md#resetDisplayedAttributes_0) | **DELETE** /indexes/books/settings/displayed-attributes | Reset displayed attributes |
| [**resetDistinctAttribute_0**](SubRoutesApi.md#resetDistinctAttribute_0) | **DELETE** /indexes/books/settings/distinct-attribute | Reset distinct attribute |
| [**resetFaceting_0**](SubRoutesApi.md#resetFaceting_0) | **DELETE** /indexes/books/settings/faceting | Reset faceting |
| [**resetFilterableAttributes_0**](SubRoutesApi.md#resetFilterableAttributes_0) | **DELETE** /indexes/books/settings/filterable-attributes | Reset filterable attributes |
| [**resetPagination_0**](SubRoutesApi.md#resetPagination_0) | **DELETE** /indexes/books/settings/pagination | Reset pagination |
| [**resetRankingRules_0**](SubRoutesApi.md#resetRankingRules_0) | **DELETE** /indexes/books/settings/ranking-rules | Reset ranking rules |
| [**resetSearchableAttributes_0**](SubRoutesApi.md#resetSearchableAttributes_0) | **DELETE** /indexes/books/settings/searchable-attributes | Reset searchable attributes |
| [**resetSortableAttributes_0**](SubRoutesApi.md#resetSortableAttributes_0) | **DELETE** /indexes/books/settings/sortable-attributes | Reset sortable attributes |
| [**resetStopWords_0**](SubRoutesApi.md#resetStopWords_0) | **DELETE** /indexes/books/settings/stop-words | Reset stop-words |
| [**resetSynonyms_0**](SubRoutesApi.md#resetSynonyms_0) | **DELETE** /indexes/books/settings/synonyms | Reset synonyms |
| [**resetTypoTolerance_0**](SubRoutesApi.md#resetTypoTolerance_0) | **DELETE** /indexes/books/settings/typo-tolerance | Reset typo-tolerance |
| [**updateDisplayedAttributes_0**](SubRoutesApi.md#updateDisplayedAttributes_0) | **PUT** /indexes/books/settings/displayed-attributes | Update displayed attributes |
| [**updateDistinctAttribute_0**](SubRoutesApi.md#updateDistinctAttribute_0) | **PUT** /indexes/books/settings/distinct-attribute | Update distinct attribute |
| [**updateFaceting_0**](SubRoutesApi.md#updateFaceting_0) | **PATCH** /indexes/books/settings/faceting | Update faceting |
| [**updateFilterableAttributes_0**](SubRoutesApi.md#updateFilterableAttributes_0) | **PUT** /indexes/books/settings/filterable-attributes | Update filterable attributes |
| [**updatePagination_0**](SubRoutesApi.md#updatePagination_0) | **PATCH** /indexes/books/settings/pagination | Update pagination |
| [**updateRankingRules_0**](SubRoutesApi.md#updateRankingRules_0) | **PUT** /indexes/books/settings/ranking-rules | Update ranking rules |
| [**updateSearchableAttributes_0**](SubRoutesApi.md#updateSearchableAttributes_0) | **PUT** /indexes/books/settings/searchable-attributes | Update searchable attributes |
| [**updateSortableAttributes_0**](SubRoutesApi.md#updateSortableAttributes_0) | **PUT** /indexes/books/settings/sortable-attributes | Update sortable attributes |
| [**updateStopWords_0**](SubRoutesApi.md#updateStopWords_0) | **PUT** /indexes/books/settings/stop-words | Update stop-words |
| [**updateSynonyms_0**](SubRoutesApi.md#updateSynonyms_0) | **PUT** /indexes/books/settings/synonyms | Update synonyms |
| [**updateTypoTolerance_0**](SubRoutesApi.md#updateTypoTolerance_0) | **PATCH** /indexes/books/settings/typo-tolerance | Update typo-tolerance |


<a id="getDisplayedAttributes_0"></a>
# **getDisplayedAttributes_0**
> getDisplayedAttributes_0()

Get displayed attributes

Get displayed attributes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubRoutesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SubRoutesApi apiInstance = new SubRoutesApi(defaultClient);
    try {
      apiInstance.getDisplayedAttributes_0();
    } catch (ApiException e) {
      System.err.println("Exception when calling SubRoutesApi#getDisplayedAttributes_0");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="getDistinctAttribute_0"></a>
# **getDistinctAttribute_0**
> getDistinctAttribute_0()

Get distinct attribute

Get distinct attribute

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubRoutesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SubRoutesApi apiInstance = new SubRoutesApi(defaultClient);
    try {
      apiInstance.getDistinctAttribute_0();
    } catch (ApiException e) {
      System.err.println("Exception when calling SubRoutesApi#getDistinctAttribute_0");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="getFaceting_0"></a>
# **getFaceting_0**
> getFaceting_0()

Get faceting

Get faceting

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubRoutesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SubRoutesApi apiInstance = new SubRoutesApi(defaultClient);
    try {
      apiInstance.getFaceting_0();
    } catch (ApiException e) {
      System.err.println("Exception when calling SubRoutesApi#getFaceting_0");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="getFilterableAttributes_0"></a>
# **getFilterableAttributes_0**
> getFilterableAttributes_0()

Get filterable attributes

Get filterable attributes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubRoutesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SubRoutesApi apiInstance = new SubRoutesApi(defaultClient);
    try {
      apiInstance.getFilterableAttributes_0();
    } catch (ApiException e) {
      System.err.println("Exception when calling SubRoutesApi#getFilterableAttributes_0");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="getPagination_0"></a>
# **getPagination_0**
> getPagination_0()

Get pagination

Get pagination

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubRoutesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SubRoutesApi apiInstance = new SubRoutesApi(defaultClient);
    try {
      apiInstance.getPagination_0();
    } catch (ApiException e) {
      System.err.println("Exception when calling SubRoutesApi#getPagination_0");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="getRankingRules_0"></a>
# **getRankingRules_0**
> getRankingRules_0()

Get ranking rules

Get ranking rules

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubRoutesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SubRoutesApi apiInstance = new SubRoutesApi(defaultClient);
    try {
      apiInstance.getRankingRules_0();
    } catch (ApiException e) {
      System.err.println("Exception when calling SubRoutesApi#getRankingRules_0");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="getSearchableAttributes_0"></a>
# **getSearchableAttributes_0**
> getSearchableAttributes_0()

Get searchable attributes

Get searchable attributes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubRoutesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SubRoutesApi apiInstance = new SubRoutesApi(defaultClient);
    try {
      apiInstance.getSearchableAttributes_0();
    } catch (ApiException e) {
      System.err.println("Exception when calling SubRoutesApi#getSearchableAttributes_0");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="getSortableAttributes_0"></a>
# **getSortableAttributes_0**
> getSortableAttributes_0()

Get sortable attributes

Get sortable attributes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubRoutesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SubRoutesApi apiInstance = new SubRoutesApi(defaultClient);
    try {
      apiInstance.getSortableAttributes_0();
    } catch (ApiException e) {
      System.err.println("Exception when calling SubRoutesApi#getSortableAttributes_0");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="getStopWords_0"></a>
# **getStopWords_0**
> getStopWords_0(requestBody)

Get stop-words

Get stop-words

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubRoutesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SubRoutesApi apiInstance = new SubRoutesApi(defaultClient);
    List<String> requestBody = ["the"]; // List<String> | 
    try {
      apiInstance.getStopWords_0(requestBody);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubRoutesApi#getStopWords_0");
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
| **requestBody** | [**List&lt;String&gt;**](String.md)|  | [optional] |

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
| **200** |  |  -  |

<a id="getSynonyms_0"></a>
# **getSynonyms_0**
> getSynonyms_0()

Get synonyms

Get synonyms

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubRoutesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SubRoutesApi apiInstance = new SubRoutesApi(defaultClient);
    try {
      apiInstance.getSynonyms_0();
    } catch (ApiException e) {
      System.err.println("Exception when calling SubRoutesApi#getSynonyms_0");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="getTypoTolerance_0"></a>
# **getTypoTolerance_0**
> getTypoTolerance_0()

Get typo-tolerance

Get typo-tolerance

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubRoutesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SubRoutesApi apiInstance = new SubRoutesApi(defaultClient);
    try {
      apiInstance.getTypoTolerance_0();
    } catch (ApiException e) {
      System.err.println("Exception when calling SubRoutesApi#getTypoTolerance_0");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="resetDisplayedAttributes_0"></a>
# **resetDisplayedAttributes_0**
> resetDisplayedAttributes_0()

Reset displayed attributes

Reset displayed attributes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubRoutesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SubRoutesApi apiInstance = new SubRoutesApi(defaultClient);
    try {
      apiInstance.resetDisplayedAttributes_0();
    } catch (ApiException e) {
      System.err.println("Exception when calling SubRoutesApi#resetDisplayedAttributes_0");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="resetDistinctAttribute_0"></a>
# **resetDistinctAttribute_0**
> resetDistinctAttribute_0()

Reset distinct attribute

Reset distinct attribute

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubRoutesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SubRoutesApi apiInstance = new SubRoutesApi(defaultClient);
    try {
      apiInstance.resetDistinctAttribute_0();
    } catch (ApiException e) {
      System.err.println("Exception when calling SubRoutesApi#resetDistinctAttribute_0");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="resetFaceting_0"></a>
# **resetFaceting_0**
> resetFaceting_0()

Reset faceting

Reset faceting

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubRoutesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SubRoutesApi apiInstance = new SubRoutesApi(defaultClient);
    try {
      apiInstance.resetFaceting_0();
    } catch (ApiException e) {
      System.err.println("Exception when calling SubRoutesApi#resetFaceting_0");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="resetFilterableAttributes_0"></a>
# **resetFilterableAttributes_0**
> resetFilterableAttributes_0()

Reset filterable attributes

Reset filterable attributes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubRoutesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SubRoutesApi apiInstance = new SubRoutesApi(defaultClient);
    try {
      apiInstance.resetFilterableAttributes_0();
    } catch (ApiException e) {
      System.err.println("Exception when calling SubRoutesApi#resetFilterableAttributes_0");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="resetPagination_0"></a>
# **resetPagination_0**
> resetPagination_0()

Reset pagination

Reset pagination

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubRoutesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SubRoutesApi apiInstance = new SubRoutesApi(defaultClient);
    try {
      apiInstance.resetPagination_0();
    } catch (ApiException e) {
      System.err.println("Exception when calling SubRoutesApi#resetPagination_0");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="resetRankingRules_0"></a>
# **resetRankingRules_0**
> resetRankingRules_0()

Reset ranking rules

Reset ranking rules

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubRoutesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SubRoutesApi apiInstance = new SubRoutesApi(defaultClient);
    try {
      apiInstance.resetRankingRules_0();
    } catch (ApiException e) {
      System.err.println("Exception when calling SubRoutesApi#resetRankingRules_0");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="resetSearchableAttributes_0"></a>
# **resetSearchableAttributes_0**
> resetSearchableAttributes_0()

Reset searchable attributes

Reset searchable attributes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubRoutesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SubRoutesApi apiInstance = new SubRoutesApi(defaultClient);
    try {
      apiInstance.resetSearchableAttributes_0();
    } catch (ApiException e) {
      System.err.println("Exception when calling SubRoutesApi#resetSearchableAttributes_0");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="resetSortableAttributes_0"></a>
# **resetSortableAttributes_0**
> resetSortableAttributes_0()

Reset sortable attributes

Reset sortable attributes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubRoutesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SubRoutesApi apiInstance = new SubRoutesApi(defaultClient);
    try {
      apiInstance.resetSortableAttributes_0();
    } catch (ApiException e) {
      System.err.println("Exception when calling SubRoutesApi#resetSortableAttributes_0");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="resetStopWords_0"></a>
# **resetStopWords_0**
> resetStopWords_0()

Reset stop-words

Reset stop-words

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubRoutesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SubRoutesApi apiInstance = new SubRoutesApi(defaultClient);
    try {
      apiInstance.resetStopWords_0();
    } catch (ApiException e) {
      System.err.println("Exception when calling SubRoutesApi#resetStopWords_0");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="resetSynonyms_0"></a>
# **resetSynonyms_0**
> resetSynonyms_0()

Reset synonyms

Reset synonyms

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubRoutesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SubRoutesApi apiInstance = new SubRoutesApi(defaultClient);
    try {
      apiInstance.resetSynonyms_0();
    } catch (ApiException e) {
      System.err.println("Exception when calling SubRoutesApi#resetSynonyms_0");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="resetTypoTolerance_0"></a>
# **resetTypoTolerance_0**
> resetTypoTolerance_0()

Reset typo-tolerance

Reset typo-tolerance

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubRoutesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SubRoutesApi apiInstance = new SubRoutesApi(defaultClient);
    try {
      apiInstance.resetTypoTolerance_0();
    } catch (ApiException e) {
      System.err.println("Exception when calling SubRoutesApi#resetTypoTolerance_0");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="updateDisplayedAttributes_0"></a>
# **updateDisplayedAttributes_0**
> updateDisplayedAttributes_0(requestBody)

Update displayed attributes

Update displayed attributes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubRoutesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SubRoutesApi apiInstance = new SubRoutesApi(defaultClient);
    List<String> requestBody = ["title"]; // List<String> | 
    try {
      apiInstance.updateDisplayedAttributes_0(requestBody);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubRoutesApi#updateDisplayedAttributes_0");
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
| **requestBody** | [**List&lt;String&gt;**](String.md)|  | [optional] |

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
| **200** |  |  -  |

<a id="updateDistinctAttribute_0"></a>
# **updateDistinctAttribute_0**
> updateDistinctAttribute_0()

Update distinct attribute

Update distinct attribute

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubRoutesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SubRoutesApi apiInstance = new SubRoutesApi(defaultClient);
    try {
      apiInstance.updateDistinctAttribute_0();
    } catch (ApiException e) {
      System.err.println("Exception when calling SubRoutesApi#updateDistinctAttribute_0");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="updateFaceting_0"></a>
# **updateFaceting_0**
> updateFaceting_0(updateFacetingRequest)

Update faceting

Update faceting

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubRoutesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SubRoutesApi apiInstance = new SubRoutesApi(defaultClient);
    UpdateFacetingRequest updateFacetingRequest = new UpdateFacetingRequest(); // UpdateFacetingRequest | 
    try {
      apiInstance.updateFaceting_0(updateFacetingRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubRoutesApi#updateFaceting_0");
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
| **updateFacetingRequest** | [**UpdateFacetingRequest**](UpdateFacetingRequest.md)|  | [optional] |

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
| **200** |  |  -  |

<a id="updateFilterableAttributes_0"></a>
# **updateFilterableAttributes_0**
> updateFilterableAttributes_0(requestBody)

Update filterable attributes

Update filterable attributes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubRoutesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SubRoutesApi apiInstance = new SubRoutesApi(defaultClient);
    List<String> requestBody = ["genre"]; // List<String> | 
    try {
      apiInstance.updateFilterableAttributes_0(requestBody);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubRoutesApi#updateFilterableAttributes_0");
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
| **requestBody** | [**List&lt;String&gt;**](String.md)|  | [optional] |

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
| **200** |  |  -  |

<a id="updatePagination_0"></a>
# **updatePagination_0**
> updatePagination_0(updatePaginationRequest)

Update pagination

Update pagination

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubRoutesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SubRoutesApi apiInstance = new SubRoutesApi(defaultClient);
    UpdatePaginationRequest updatePaginationRequest = new UpdatePaginationRequest(); // UpdatePaginationRequest | 
    try {
      apiInstance.updatePagination_0(updatePaginationRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubRoutesApi#updatePagination_0");
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
| **updatePaginationRequest** | [**UpdatePaginationRequest**](UpdatePaginationRequest.md)|  | [optional] |

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
| **200** |  |  -  |

<a id="updateRankingRules_0"></a>
# **updateRankingRules_0**
> updateRankingRules_0(requestBody)

Update ranking rules

Update ranking rules

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubRoutesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SubRoutesApi apiInstance = new SubRoutesApi(defaultClient);
    List<String> requestBody = ["typo"]; // List<String> | 
    try {
      apiInstance.updateRankingRules_0(requestBody);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubRoutesApi#updateRankingRules_0");
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
| **requestBody** | [**List&lt;String&gt;**](String.md)|  | [optional] |

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
| **200** |  |  -  |

<a id="updateSearchableAttributes_0"></a>
# **updateSearchableAttributes_0**
> updateSearchableAttributes_0(requestBody)

Update searchable attributes

Update searchable attributes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubRoutesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SubRoutesApi apiInstance = new SubRoutesApi(defaultClient);
    List<String> requestBody = ["title","author"]; // List<String> | 
    try {
      apiInstance.updateSearchableAttributes_0(requestBody);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubRoutesApi#updateSearchableAttributes_0");
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
| **requestBody** | [**List&lt;String&gt;**](String.md)|  | [optional] |

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
| **200** |  |  -  |

<a id="updateSortableAttributes_0"></a>
# **updateSortableAttributes_0**
> updateSortableAttributes_0(requestBody)

Update sortable attributes

Update sortable attributes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubRoutesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SubRoutesApi apiInstance = new SubRoutesApi(defaultClient);
    List<String> requestBody = ["price"]; // List<String> | 
    try {
      apiInstance.updateSortableAttributes_0(requestBody);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubRoutesApi#updateSortableAttributes_0");
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
| **requestBody** | [**List&lt;String&gt;**](String.md)|  | [optional] |

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
| **200** |  |  -  |

<a id="updateStopWords_0"></a>
# **updateStopWords_0**
> updateStopWords_0(requestBody)

Update stop-words

Update stop-words

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubRoutesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SubRoutesApi apiInstance = new SubRoutesApi(defaultClient);
    List<String> requestBody = ["the","of"]; // List<String> | 
    try {
      apiInstance.updateStopWords_0(requestBody);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubRoutesApi#updateStopWords_0");
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
| **requestBody** | [**List&lt;String&gt;**](String.md)|  | [optional] |

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
| **200** |  |  -  |

<a id="updateSynonyms_0"></a>
# **updateSynonyms_0**
> updateSynonyms_0(updateSynonymsRequest)

Update synonyms

Update synonyms

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubRoutesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SubRoutesApi apiInstance = new SubRoutesApi(defaultClient);
    UpdateSynonymsRequest updateSynonymsRequest = new UpdateSynonymsRequest(); // UpdateSynonymsRequest | 
    try {
      apiInstance.updateSynonyms_0(updateSynonymsRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubRoutesApi#updateSynonyms_0");
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
| **updateSynonymsRequest** | [**UpdateSynonymsRequest**](UpdateSynonymsRequest.md)|  | [optional] |

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
| **200** |  |  -  |

<a id="updateTypoTolerance_0"></a>
# **updateTypoTolerance_0**
> updateTypoTolerance_0(updateTypoToleranceRequest)

Update typo-tolerance

Update typo-tolerance

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubRoutesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SubRoutesApi apiInstance = new SubRoutesApi(defaultClient);
    UpdateTypoToleranceRequest updateTypoToleranceRequest = new UpdateTypoToleranceRequest(); // UpdateTypoToleranceRequest | 
    try {
      apiInstance.updateTypoTolerance_0(updateTypoToleranceRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubRoutesApi#updateTypoTolerance_0");
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
| **updateTypoToleranceRequest** | [**UpdateTypoToleranceRequest**](UpdateTypoToleranceRequest.md)|  | [optional] |

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
| **200** |  |  -  |

