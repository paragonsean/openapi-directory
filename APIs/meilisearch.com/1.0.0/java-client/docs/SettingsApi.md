# SettingsApi

All URIs are relative to *http://localhost:7700*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAllSettings**](SettingsApi.md#getAllSettings) | **GET** /indexes/books/settings | Get all settings |
| [**getDisplayedAttributes**](SettingsApi.md#getDisplayedAttributes) | **GET** /indexes/books/settings/displayed-attributes | Get displayed attributes |
| [**getDistinctAttribute**](SettingsApi.md#getDistinctAttribute) | **GET** /indexes/books/settings/distinct-attribute | Get distinct attribute |
| [**getFaceting**](SettingsApi.md#getFaceting) | **GET** /indexes/books/settings/faceting | Get faceting |
| [**getFilterableAttributes**](SettingsApi.md#getFilterableAttributes) | **GET** /indexes/books/settings/filterable-attributes | Get filterable attributes |
| [**getPagination**](SettingsApi.md#getPagination) | **GET** /indexes/books/settings/pagination | Get pagination |
| [**getRankingRules**](SettingsApi.md#getRankingRules) | **GET** /indexes/books/settings/ranking-rules | Get ranking rules |
| [**getSearchableAttributes**](SettingsApi.md#getSearchableAttributes) | **GET** /indexes/books/settings/searchable-attributes | Get searchable attributes |
| [**getSortableAttributes**](SettingsApi.md#getSortableAttributes) | **GET** /indexes/books/settings/sortable-attributes | Get sortable attributes |
| [**getStopWords**](SettingsApi.md#getStopWords) | **GET** /indexes/books/settings/stop-words | Get stop-words |
| [**getSynonyms**](SettingsApi.md#getSynonyms) | **GET** /indexes/books/settings/synonyms | Get synonyms |
| [**getTypoTolerance**](SettingsApi.md#getTypoTolerance) | **GET** /indexes/books/settings/typo-tolerance | Get typo-tolerance |
| [**resetAllSettings**](SettingsApi.md#resetAllSettings) | **DELETE** /indexes/books/settings | Reset all settings |
| [**resetDisplayedAttributes**](SettingsApi.md#resetDisplayedAttributes) | **DELETE** /indexes/books/settings/displayed-attributes | Reset displayed attributes |
| [**resetDistinctAttribute**](SettingsApi.md#resetDistinctAttribute) | **DELETE** /indexes/books/settings/distinct-attribute | Reset distinct attribute |
| [**resetFaceting**](SettingsApi.md#resetFaceting) | **DELETE** /indexes/books/settings/faceting | Reset faceting |
| [**resetFilterableAttributes**](SettingsApi.md#resetFilterableAttributes) | **DELETE** /indexes/books/settings/filterable-attributes | Reset filterable attributes |
| [**resetPagination**](SettingsApi.md#resetPagination) | **DELETE** /indexes/books/settings/pagination | Reset pagination |
| [**resetRankingRules**](SettingsApi.md#resetRankingRules) | **DELETE** /indexes/books/settings/ranking-rules | Reset ranking rules |
| [**resetSearchableAttributes**](SettingsApi.md#resetSearchableAttributes) | **DELETE** /indexes/books/settings/searchable-attributes | Reset searchable attributes |
| [**resetSortableAttributes**](SettingsApi.md#resetSortableAttributes) | **DELETE** /indexes/books/settings/sortable-attributes | Reset sortable attributes |
| [**resetStopWords**](SettingsApi.md#resetStopWords) | **DELETE** /indexes/books/settings/stop-words | Reset stop-words |
| [**resetSynonyms**](SettingsApi.md#resetSynonyms) | **DELETE** /indexes/books/settings/synonyms | Reset synonyms |
| [**resetTypoTolerance**](SettingsApi.md#resetTypoTolerance) | **DELETE** /indexes/books/settings/typo-tolerance | Reset typo-tolerance |
| [**updateDisplayedAttributes**](SettingsApi.md#updateDisplayedAttributes) | **PUT** /indexes/books/settings/displayed-attributes | Update displayed attributes |
| [**updateDistinctAttribute**](SettingsApi.md#updateDistinctAttribute) | **PUT** /indexes/books/settings/distinct-attribute | Update distinct attribute |
| [**updateFaceting**](SettingsApi.md#updateFaceting) | **PATCH** /indexes/books/settings/faceting | Update faceting |
| [**updateFilterableAttributes**](SettingsApi.md#updateFilterableAttributes) | **PUT** /indexes/books/settings/filterable-attributes | Update filterable attributes |
| [**updatePagination**](SettingsApi.md#updatePagination) | **PATCH** /indexes/books/settings/pagination | Update pagination |
| [**updateRankingRules**](SettingsApi.md#updateRankingRules) | **PUT** /indexes/books/settings/ranking-rules | Update ranking rules |
| [**updateSearchableAttributes**](SettingsApi.md#updateSearchableAttributes) | **PUT** /indexes/books/settings/searchable-attributes | Update searchable attributes |
| [**updateSettings**](SettingsApi.md#updateSettings) | **PATCH** /indexes/books/settings | Update settings |
| [**updateSortableAttributes**](SettingsApi.md#updateSortableAttributes) | **PUT** /indexes/books/settings/sortable-attributes | Update sortable attributes |
| [**updateStopWords**](SettingsApi.md#updateStopWords) | **PUT** /indexes/books/settings/stop-words | Update stop-words |
| [**updateSynonyms**](SettingsApi.md#updateSynonyms) | **PUT** /indexes/books/settings/synonyms | Update synonyms |
| [**updateTypoTolerance**](SettingsApi.md#updateTypoTolerance) | **PATCH** /indexes/books/settings/typo-tolerance | Update typo-tolerance |


<a id="getAllSettings"></a>
# **getAllSettings**
> getAllSettings()

Get all settings

Get all settings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SettingsApi apiInstance = new SettingsApi(defaultClient);
    try {
      apiInstance.getAllSettings();
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsApi#getAllSettings");
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

<a id="getDisplayedAttributes"></a>
# **getDisplayedAttributes**
> getDisplayedAttributes()

Get displayed attributes

Get displayed attributes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SettingsApi apiInstance = new SettingsApi(defaultClient);
    try {
      apiInstance.getDisplayedAttributes();
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsApi#getDisplayedAttributes");
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

<a id="getDistinctAttribute"></a>
# **getDistinctAttribute**
> getDistinctAttribute()

Get distinct attribute

Get distinct attribute

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SettingsApi apiInstance = new SettingsApi(defaultClient);
    try {
      apiInstance.getDistinctAttribute();
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsApi#getDistinctAttribute");
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

<a id="getFaceting"></a>
# **getFaceting**
> getFaceting()

Get faceting

Get faceting

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SettingsApi apiInstance = new SettingsApi(defaultClient);
    try {
      apiInstance.getFaceting();
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsApi#getFaceting");
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

<a id="getFilterableAttributes"></a>
# **getFilterableAttributes**
> getFilterableAttributes()

Get filterable attributes

Get filterable attributes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SettingsApi apiInstance = new SettingsApi(defaultClient);
    try {
      apiInstance.getFilterableAttributes();
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsApi#getFilterableAttributes");
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

<a id="getPagination"></a>
# **getPagination**
> getPagination()

Get pagination

Get pagination

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SettingsApi apiInstance = new SettingsApi(defaultClient);
    try {
      apiInstance.getPagination();
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsApi#getPagination");
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

<a id="getRankingRules"></a>
# **getRankingRules**
> getRankingRules()

Get ranking rules

Get ranking rules

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SettingsApi apiInstance = new SettingsApi(defaultClient);
    try {
      apiInstance.getRankingRules();
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsApi#getRankingRules");
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

<a id="getSearchableAttributes"></a>
# **getSearchableAttributes**
> getSearchableAttributes()

Get searchable attributes

Get searchable attributes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SettingsApi apiInstance = new SettingsApi(defaultClient);
    try {
      apiInstance.getSearchableAttributes();
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsApi#getSearchableAttributes");
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

<a id="getSortableAttributes"></a>
# **getSortableAttributes**
> getSortableAttributes()

Get sortable attributes

Get sortable attributes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SettingsApi apiInstance = new SettingsApi(defaultClient);
    try {
      apiInstance.getSortableAttributes();
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsApi#getSortableAttributes");
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

<a id="getStopWords"></a>
# **getStopWords**
> getStopWords(requestBody)

Get stop-words

Get stop-words

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SettingsApi apiInstance = new SettingsApi(defaultClient);
    List<String> requestBody = ["the"]; // List<String> | 
    try {
      apiInstance.getStopWords(requestBody);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsApi#getStopWords");
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

<a id="getSynonyms"></a>
# **getSynonyms**
> getSynonyms()

Get synonyms

Get synonyms

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SettingsApi apiInstance = new SettingsApi(defaultClient);
    try {
      apiInstance.getSynonyms();
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsApi#getSynonyms");
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

<a id="getTypoTolerance"></a>
# **getTypoTolerance**
> getTypoTolerance()

Get typo-tolerance

Get typo-tolerance

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SettingsApi apiInstance = new SettingsApi(defaultClient);
    try {
      apiInstance.getTypoTolerance();
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsApi#getTypoTolerance");
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

<a id="resetAllSettings"></a>
# **resetAllSettings**
> resetAllSettings()

Reset all settings

Reset all settings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SettingsApi apiInstance = new SettingsApi(defaultClient);
    try {
      apiInstance.resetAllSettings();
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsApi#resetAllSettings");
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

<a id="resetDisplayedAttributes"></a>
# **resetDisplayedAttributes**
> resetDisplayedAttributes()

Reset displayed attributes

Reset displayed attributes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SettingsApi apiInstance = new SettingsApi(defaultClient);
    try {
      apiInstance.resetDisplayedAttributes();
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsApi#resetDisplayedAttributes");
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

<a id="resetDistinctAttribute"></a>
# **resetDistinctAttribute**
> resetDistinctAttribute()

Reset distinct attribute

Reset distinct attribute

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SettingsApi apiInstance = new SettingsApi(defaultClient);
    try {
      apiInstance.resetDistinctAttribute();
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsApi#resetDistinctAttribute");
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

<a id="resetFaceting"></a>
# **resetFaceting**
> resetFaceting()

Reset faceting

Reset faceting

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SettingsApi apiInstance = new SettingsApi(defaultClient);
    try {
      apiInstance.resetFaceting();
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsApi#resetFaceting");
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

<a id="resetFilterableAttributes"></a>
# **resetFilterableAttributes**
> resetFilterableAttributes()

Reset filterable attributes

Reset filterable attributes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SettingsApi apiInstance = new SettingsApi(defaultClient);
    try {
      apiInstance.resetFilterableAttributes();
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsApi#resetFilterableAttributes");
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

<a id="resetPagination"></a>
# **resetPagination**
> resetPagination()

Reset pagination

Reset pagination

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SettingsApi apiInstance = new SettingsApi(defaultClient);
    try {
      apiInstance.resetPagination();
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsApi#resetPagination");
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

<a id="resetRankingRules"></a>
# **resetRankingRules**
> resetRankingRules()

Reset ranking rules

Reset ranking rules

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SettingsApi apiInstance = new SettingsApi(defaultClient);
    try {
      apiInstance.resetRankingRules();
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsApi#resetRankingRules");
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

<a id="resetSearchableAttributes"></a>
# **resetSearchableAttributes**
> resetSearchableAttributes()

Reset searchable attributes

Reset searchable attributes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SettingsApi apiInstance = new SettingsApi(defaultClient);
    try {
      apiInstance.resetSearchableAttributes();
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsApi#resetSearchableAttributes");
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

<a id="resetSortableAttributes"></a>
# **resetSortableAttributes**
> resetSortableAttributes()

Reset sortable attributes

Reset sortable attributes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SettingsApi apiInstance = new SettingsApi(defaultClient);
    try {
      apiInstance.resetSortableAttributes();
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsApi#resetSortableAttributes");
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

<a id="resetStopWords"></a>
# **resetStopWords**
> resetStopWords()

Reset stop-words

Reset stop-words

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SettingsApi apiInstance = new SettingsApi(defaultClient);
    try {
      apiInstance.resetStopWords();
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsApi#resetStopWords");
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

<a id="resetSynonyms"></a>
# **resetSynonyms**
> resetSynonyms()

Reset synonyms

Reset synonyms

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SettingsApi apiInstance = new SettingsApi(defaultClient);
    try {
      apiInstance.resetSynonyms();
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsApi#resetSynonyms");
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

<a id="resetTypoTolerance"></a>
# **resetTypoTolerance**
> resetTypoTolerance()

Reset typo-tolerance

Reset typo-tolerance

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SettingsApi apiInstance = new SettingsApi(defaultClient);
    try {
      apiInstance.resetTypoTolerance();
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsApi#resetTypoTolerance");
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

<a id="updateDisplayedAttributes"></a>
# **updateDisplayedAttributes**
> updateDisplayedAttributes(requestBody)

Update displayed attributes

Update displayed attributes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SettingsApi apiInstance = new SettingsApi(defaultClient);
    List<String> requestBody = ["title"]; // List<String> | 
    try {
      apiInstance.updateDisplayedAttributes(requestBody);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsApi#updateDisplayedAttributes");
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

<a id="updateDistinctAttribute"></a>
# **updateDistinctAttribute**
> updateDistinctAttribute()

Update distinct attribute

Update distinct attribute

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SettingsApi apiInstance = new SettingsApi(defaultClient);
    try {
      apiInstance.updateDistinctAttribute();
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsApi#updateDistinctAttribute");
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

<a id="updateFaceting"></a>
# **updateFaceting**
> updateFaceting(updateFacetingRequest)

Update faceting

Update faceting

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SettingsApi apiInstance = new SettingsApi(defaultClient);
    UpdateFacetingRequest updateFacetingRequest = new UpdateFacetingRequest(); // UpdateFacetingRequest | 
    try {
      apiInstance.updateFaceting(updateFacetingRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsApi#updateFaceting");
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

<a id="updateFilterableAttributes"></a>
# **updateFilterableAttributes**
> updateFilterableAttributes(requestBody)

Update filterable attributes

Update filterable attributes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SettingsApi apiInstance = new SettingsApi(defaultClient);
    List<String> requestBody = ["genre"]; // List<String> | 
    try {
      apiInstance.updateFilterableAttributes(requestBody);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsApi#updateFilterableAttributes");
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

<a id="updatePagination"></a>
# **updatePagination**
> updatePagination(updatePaginationRequest)

Update pagination

Update pagination

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SettingsApi apiInstance = new SettingsApi(defaultClient);
    UpdatePaginationRequest updatePaginationRequest = new UpdatePaginationRequest(); // UpdatePaginationRequest | 
    try {
      apiInstance.updatePagination(updatePaginationRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsApi#updatePagination");
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

<a id="updateRankingRules"></a>
# **updateRankingRules**
> updateRankingRules(requestBody)

Update ranking rules

Update ranking rules

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SettingsApi apiInstance = new SettingsApi(defaultClient);
    List<String> requestBody = ["typo"]; // List<String> | 
    try {
      apiInstance.updateRankingRules(requestBody);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsApi#updateRankingRules");
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

<a id="updateSearchableAttributes"></a>
# **updateSearchableAttributes**
> updateSearchableAttributes(requestBody)

Update searchable attributes

Update searchable attributes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SettingsApi apiInstance = new SettingsApi(defaultClient);
    List<String> requestBody = ["title","author"]; // List<String> | 
    try {
      apiInstance.updateSearchableAttributes(requestBody);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsApi#updateSearchableAttributes");
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

<a id="updateSettings"></a>
# **updateSettings**
> updateSettings(updateSettingsRequest)

Update settings

Update settings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SettingsApi apiInstance = new SettingsApi(defaultClient);
    UpdateSettingsRequest updateSettingsRequest = new UpdateSettingsRequest(); // UpdateSettingsRequest | 
    try {
      apiInstance.updateSettings(updateSettingsRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsApi#updateSettings");
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
| **updateSettingsRequest** | [**UpdateSettingsRequest**](UpdateSettingsRequest.md)|  | [optional] |

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

<a id="updateSortableAttributes"></a>
# **updateSortableAttributes**
> updateSortableAttributes(requestBody)

Update sortable attributes

Update sortable attributes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SettingsApi apiInstance = new SettingsApi(defaultClient);
    List<String> requestBody = ["price"]; // List<String> | 
    try {
      apiInstance.updateSortableAttributes(requestBody);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsApi#updateSortableAttributes");
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

<a id="updateStopWords"></a>
# **updateStopWords**
> updateStopWords(requestBody)

Update stop-words

Update stop-words

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SettingsApi apiInstance = new SettingsApi(defaultClient);
    List<String> requestBody = ["the","of"]; // List<String> | 
    try {
      apiInstance.updateStopWords(requestBody);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsApi#updateStopWords");
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

<a id="updateSynonyms"></a>
# **updateSynonyms**
> updateSynonyms(updateSynonymsRequest)

Update synonyms

Update synonyms

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SettingsApi apiInstance = new SettingsApi(defaultClient);
    UpdateSynonymsRequest updateSynonymsRequest = new UpdateSynonymsRequest(); // UpdateSynonymsRequest | 
    try {
      apiInstance.updateSynonyms(updateSynonymsRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsApi#updateSynonyms");
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

<a id="updateTypoTolerance"></a>
# **updateTypoTolerance**
> updateTypoTolerance(updateTypoToleranceRequest)

Update typo-tolerance

Update typo-tolerance

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    SettingsApi apiInstance = new SettingsApi(defaultClient);
    UpdateTypoToleranceRequest updateTypoToleranceRequest = new UpdateTypoToleranceRequest(); // UpdateTypoToleranceRequest | 
    try {
      apiInstance.updateTypoTolerance(updateTypoToleranceRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsApi#updateTypoTolerance");
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

