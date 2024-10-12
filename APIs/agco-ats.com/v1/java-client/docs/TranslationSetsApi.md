# TranslationSetsApi

All URIs are relative to *https://secure.agco-ats.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**translationSetsDeleteTranslationSetAttribute**](TranslationSetsApi.md#translationSetsDeleteTranslationSetAttribute) | **DELETE** /api/v2/TranslationSetAttributes/{ID} | Delete a set of TranslationSetAttribute object |
| [**translationSetsGetSourceStrings**](TranslationSetsApi.md#translationSetsGetSourceStrings) | **GET** /api/v2/TranslationSets/{ID}/SourceStrings | Gets the information needed to translate a string in a translation set |
| [**translationSetsGetStatistics**](TranslationSetsApi.md#translationSetsGetStatistics) | **GET** /api/v2/TranslationSets/{ID}/Statistics | Gets the statistics for translation sets such as the language ids and count of string definitions. |
| [**translationSetsGetTranslationSet**](TranslationSetsApi.md#translationSetsGetTranslationSet) | **GET** /api/v2/TranslationSets/{ID} | Get a TranslationSet object by its id. Related TranslationSetStrings are NOT returned. |
| [**translationSetsGetTranslationSetAttributes**](TranslationSetsApi.md#translationSetsGetTranslationSetAttributes) | **GET** /api/v2/TranslationSets/{ID}/Attributes | Get a PagedResponse of TranslationSetAttribute objects |
| [**translationSetsGetTranslationSetStrings**](TranslationSetsApi.md#translationSetsGetTranslationSetStrings) | **GET** /api/v2/TranslationSets/{ID}/Strings | Get a PagedResponse of TranslationSetString objects |
| [**translationSetsGetTranslationSets**](TranslationSetsApi.md#translationSetsGetTranslationSets) | **GET** /api/v2/TranslationSets | Get a PagedResponse of TranslationSet objects. Related TranslationSetStrings are NOT returned |
| [**translationSetsPostTranslationSetAttribute**](TranslationSetsApi.md#translationSetsPostTranslationSetAttribute) | **POST** /api/v2/TranslationSets/{ID}/Attributes | Create a TranslationSetAttribute object |
| [**translationSetsPostTranslationSetAttributes**](TranslationSetsApi.md#translationSetsPostTranslationSetAttributes) | **POST** /api/v2/TranslationSets/{ID}/Attributes/Batch | No Documentation Found. |
| [**translationSetsUpdateTranslationSet**](TranslationSetsApi.md#translationSetsUpdateTranslationSet) | **PUT** /api/v2/TranslationSets/{ID} | Update a Translation Set. Accepts a TranslationSet object. Only the state property may be updated. |
| [**translationSetsUpdateTranslationSetAttribute**](TranslationSetsApi.md#translationSetsUpdateTranslationSetAttribute) | **PUT** /api/v2/TranslationSetAttributes/{ID} | Update a TranslationSetAttribute object |
| [**translationSetsUpdateTranslationSetAttributes**](TranslationSetsApi.md#translationSetsUpdateTranslationSetAttributes) | **PUT** /api/v2/TranslationSetAttributes/Batch | No Documentation Found. |
| [**translationSetsUpdateTranslationSetStrings**](TranslationSetsApi.md#translationSetsUpdateTranslationSetStrings) | **PUT** /api/v2/TranslationSets/{ID}/Strings | No Documentation Found. |


<a id="translationSetsDeleteTranslationSetAttribute"></a>
# **translationSetsDeleteTranslationSetAttribute**
> translationSetsDeleteTranslationSetAttribute(ID)

Delete a set of TranslationSetAttribute object

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranslationSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    TranslationSetsApi apiInstance = new TranslationSetsApi(defaultClient);
    Integer ID = 56; // Integer | 
    try {
      apiInstance.translationSetsDeleteTranslationSetAttribute(ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranslationSetsApi#translationSetsDeleteTranslationSetAttribute");
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
| **ID** | **Integer**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | API Error Response |  -  |

<a id="translationSetsGetSourceStrings"></a>
# **translationSetsGetSourceStrings**
> APIIPagedResponseGlobalResourcesSharedModelsTranslationSetSourceString translationSetsGetSourceStrings(ID, limit, offset)

Gets the information needed to translate a string in a translation set

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranslationSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    TranslationSetsApi apiInstance = new TranslationSetsApi(defaultClient);
    Integer ID = 56; // Integer | 
    Integer limit = 56; // Integer | 
    Integer offset = 56; // Integer | 
    try {
      APIIPagedResponseGlobalResourcesSharedModelsTranslationSetSourceString result = apiInstance.translationSetsGetSourceStrings(ID, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranslationSetsApi#translationSetsGetSourceStrings");
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
| **ID** | **Integer**|  | |
| **limit** | **Integer**|  | [optional] |
| **offset** | **Integer**|  | [optional] |

### Return type

[**APIIPagedResponseGlobalResourcesSharedModelsTranslationSetSourceString**](APIIPagedResponseGlobalResourcesSharedModelsTranslationSetSourceString.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="translationSetsGetStatistics"></a>
# **translationSetsGetStatistics**
> GlobalResourcesSharedModelsTranslationSetStatistics translationSetsGetStatistics(ID)

Gets the statistics for translation sets such as the language ids and count of string definitions.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranslationSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    TranslationSetsApi apiInstance = new TranslationSetsApi(defaultClient);
    Integer ID = 56; // Integer | 
    try {
      GlobalResourcesSharedModelsTranslationSetStatistics result = apiInstance.translationSetsGetStatistics(ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranslationSetsApi#translationSetsGetStatistics");
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
| **ID** | **Integer**|  | |

### Return type

[**GlobalResourcesSharedModelsTranslationSetStatistics**](GlobalResourcesSharedModelsTranslationSetStatistics.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="translationSetsGetTranslationSet"></a>
# **translationSetsGetTranslationSet**
> GlobalResourcesSharedModelsTranslationSet translationSetsGetTranslationSet(ID, includeAttributes)

Get a TranslationSet object by its id. Related TranslationSetStrings are NOT returned.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranslationSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    TranslationSetsApi apiInstance = new TranslationSetsApi(defaultClient);
    Integer ID = 56; // Integer | 
    String includeAttributes = "includeAttributes_example"; // String | Names of Attributes to include when retrieving this Translation set. This should be a comma-separated list. If not provided, Attributes are not included. If '*', all Attributes are included.
    try {
      GlobalResourcesSharedModelsTranslationSet result = apiInstance.translationSetsGetTranslationSet(ID, includeAttributes);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranslationSetsApi#translationSetsGetTranslationSet");
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
| **ID** | **Integer**|  | |
| **includeAttributes** | **String**| Names of Attributes to include when retrieving this Translation set. This should be a comma-separated list. If not provided, Attributes are not included. If &#39;*&#39;, all Attributes are included. | [optional] |

### Return type

[**GlobalResourcesSharedModelsTranslationSet**](GlobalResourcesSharedModelsTranslationSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="translationSetsGetTranslationSetAttributes"></a>
# **translationSetsGetTranslationSetAttributes**
> APIIPagedResponseGlobalResourcesSharedModelsTranslationSetAttribute translationSetsGetTranslationSetAttributes(ID, limit, offset, name)

Get a PagedResponse of TranslationSetAttribute objects

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranslationSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    TranslationSetsApi apiInstance = new TranslationSetsApi(defaultClient);
    Integer ID = 56; // Integer | 
    Integer limit = 56; // Integer | 
    Integer offset = 56; // Integer | 
    String name = "name_example"; // String | 
    try {
      APIIPagedResponseGlobalResourcesSharedModelsTranslationSetAttribute result = apiInstance.translationSetsGetTranslationSetAttributes(ID, limit, offset, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranslationSetsApi#translationSetsGetTranslationSetAttributes");
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
| **ID** | **Integer**|  | |
| **limit** | **Integer**|  | [optional] |
| **offset** | **Integer**|  | [optional] |
| **name** | **String**|  | [optional] |

### Return type

[**APIIPagedResponseGlobalResourcesSharedModelsTranslationSetAttribute**](APIIPagedResponseGlobalResourcesSharedModelsTranslationSetAttribute.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="translationSetsGetTranslationSetStrings"></a>
# **translationSetsGetTranslationSetStrings**
> APIIPagedResponseGlobalResourcesSharedModelsTranslationSetString translationSetsGetTranslationSetStrings(ID, limit, offset)

Get a PagedResponse of TranslationSetString objects

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranslationSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    TranslationSetsApi apiInstance = new TranslationSetsApi(defaultClient);
    Integer ID = 56; // Integer | 
    Integer limit = 56; // Integer | 
    Integer offset = 56; // Integer | 
    try {
      APIIPagedResponseGlobalResourcesSharedModelsTranslationSetString result = apiInstance.translationSetsGetTranslationSetStrings(ID, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranslationSetsApi#translationSetsGetTranslationSetStrings");
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
| **ID** | **Integer**|  | |
| **limit** | **Integer**|  | [optional] |
| **offset** | **Integer**|  | [optional] |

### Return type

[**APIIPagedResponseGlobalResourcesSharedModelsTranslationSetString**](APIIPagedResponseGlobalResourcesSharedModelsTranslationSetString.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="translationSetsGetTranslationSets"></a>
# **translationSetsGetTranslationSets**
> APIIPagedResponseGlobalResourcesSharedModelsTranslationSet translationSetsGetTranslationSets(limit, offset, translationRequestID, state, stringId, languageId, includeAttributes)

Get a PagedResponse of TranslationSet objects. Related TranslationSetStrings are NOT returned

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranslationSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    TranslationSetsApi apiInstance = new TranslationSetsApi(defaultClient);
    Integer limit = 56; // Integer | 
    Integer offset = 56; // Integer | 
    Integer translationRequestID = 56; // Integer | 
    String state = "OutForProcessing"; // String | 
    String stringId = "stringId_example"; // String | 
    Integer languageId = 56; // Integer | 
    String includeAttributes = "includeAttributes_example"; // String | Names of Attributes to include when retrieving this submission. This should be a comma-separated list. If not provided, Attributes are not included. If '*', all Attributes are included.
    try {
      APIIPagedResponseGlobalResourcesSharedModelsTranslationSet result = apiInstance.translationSetsGetTranslationSets(limit, offset, translationRequestID, state, stringId, languageId, includeAttributes);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranslationSetsApi#translationSetsGetTranslationSets");
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
| **limit** | **Integer**|  | [optional] |
| **offset** | **Integer**|  | [optional] |
| **translationRequestID** | **Integer**|  | [optional] |
| **state** | **String**|  | [optional] [enum: OutForProcessing, Processing, PendingApproval, OutForTranslation, Cancelled, Completed] |
| **stringId** | **String**|  | [optional] |
| **languageId** | **Integer**|  | [optional] |
| **includeAttributes** | **String**| Names of Attributes to include when retrieving this submission. This should be a comma-separated list. If not provided, Attributes are not included. If &#39;*&#39;, all Attributes are included. | [optional] |

### Return type

[**APIIPagedResponseGlobalResourcesSharedModelsTranslationSet**](APIIPagedResponseGlobalResourcesSharedModelsTranslationSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="translationSetsPostTranslationSetAttribute"></a>
# **translationSetsPostTranslationSetAttribute**
> Integer translationSetsPostTranslationSetAttribute(ID, globalResourcesSharedModelsTranslationSetAttribute)

Create a TranslationSetAttribute object

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranslationSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    TranslationSetsApi apiInstance = new TranslationSetsApi(defaultClient);
    Integer ID = 56; // Integer | 
    GlobalResourcesSharedModelsTranslationSetAttribute globalResourcesSharedModelsTranslationSetAttribute = new GlobalResourcesSharedModelsTranslationSetAttribute(); // GlobalResourcesSharedModelsTranslationSetAttribute | 
    try {
      Integer result = apiInstance.translationSetsPostTranslationSetAttribute(ID, globalResourcesSharedModelsTranslationSetAttribute);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranslationSetsApi#translationSetsPostTranslationSetAttribute");
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
| **ID** | **Integer**|  | |
| **globalResourcesSharedModelsTranslationSetAttribute** | [**GlobalResourcesSharedModelsTranslationSetAttribute**](GlobalResourcesSharedModelsTranslationSetAttribute.md)|  | |

### Return type

**Integer**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="translationSetsPostTranslationSetAttributes"></a>
# **translationSetsPostTranslationSetAttributes**
> translationSetsPostTranslationSetAttributes(ID, globalResourcesSharedModelsTranslationSetAttribute)

No Documentation Found.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranslationSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    TranslationSetsApi apiInstance = new TranslationSetsApi(defaultClient);
    Integer ID = 56; // Integer | 
    List<GlobalResourcesSharedModelsTranslationSetAttribute> globalResourcesSharedModelsTranslationSetAttribute = Arrays.asList(); // List<GlobalResourcesSharedModelsTranslationSetAttribute> | 
    try {
      apiInstance.translationSetsPostTranslationSetAttributes(ID, globalResourcesSharedModelsTranslationSetAttribute);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranslationSetsApi#translationSetsPostTranslationSetAttributes");
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
| **ID** | **Integer**|  | |
| **globalResourcesSharedModelsTranslationSetAttribute** | [**List&lt;GlobalResourcesSharedModelsTranslationSetAttribute&gt;**](GlobalResourcesSharedModelsTranslationSetAttribute.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | API Error Response |  -  |

<a id="translationSetsUpdateTranslationSet"></a>
# **translationSetsUpdateTranslationSet**
> translationSetsUpdateTranslationSet(ID, globalResourcesSharedModelsTranslationSet)

Update a Translation Set. Accepts a TranslationSet object. Only the state property may be updated.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranslationSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    TranslationSetsApi apiInstance = new TranslationSetsApi(defaultClient);
    Integer ID = 56; // Integer | 
    GlobalResourcesSharedModelsTranslationSet globalResourcesSharedModelsTranslationSet = new GlobalResourcesSharedModelsTranslationSet(); // GlobalResourcesSharedModelsTranslationSet | 
    try {
      apiInstance.translationSetsUpdateTranslationSet(ID, globalResourcesSharedModelsTranslationSet);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranslationSetsApi#translationSetsUpdateTranslationSet");
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
| **ID** | **Integer**|  | |
| **globalResourcesSharedModelsTranslationSet** | [**GlobalResourcesSharedModelsTranslationSet**](GlobalResourcesSharedModelsTranslationSet.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | API Error Response |  -  |

<a id="translationSetsUpdateTranslationSetAttribute"></a>
# **translationSetsUpdateTranslationSetAttribute**
> translationSetsUpdateTranslationSetAttribute(ID, globalResourcesSharedModelsTranslationSetAttribute)

Update a TranslationSetAttribute object

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranslationSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    TranslationSetsApi apiInstance = new TranslationSetsApi(defaultClient);
    Integer ID = 56; // Integer | 
    GlobalResourcesSharedModelsTranslationSetAttribute globalResourcesSharedModelsTranslationSetAttribute = new GlobalResourcesSharedModelsTranslationSetAttribute(); // GlobalResourcesSharedModelsTranslationSetAttribute | 
    try {
      apiInstance.translationSetsUpdateTranslationSetAttribute(ID, globalResourcesSharedModelsTranslationSetAttribute);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranslationSetsApi#translationSetsUpdateTranslationSetAttribute");
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
| **ID** | **Integer**|  | |
| **globalResourcesSharedModelsTranslationSetAttribute** | [**GlobalResourcesSharedModelsTranslationSetAttribute**](GlobalResourcesSharedModelsTranslationSetAttribute.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | API Error Response |  -  |

<a id="translationSetsUpdateTranslationSetAttributes"></a>
# **translationSetsUpdateTranslationSetAttributes**
> translationSetsUpdateTranslationSetAttributes(globalResourcesSharedModelsTranslationSetAttribute)

No Documentation Found.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranslationSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    TranslationSetsApi apiInstance = new TranslationSetsApi(defaultClient);
    List<GlobalResourcesSharedModelsTranslationSetAttribute> globalResourcesSharedModelsTranslationSetAttribute = Arrays.asList(); // List<GlobalResourcesSharedModelsTranslationSetAttribute> | 
    try {
      apiInstance.translationSetsUpdateTranslationSetAttributes(globalResourcesSharedModelsTranslationSetAttribute);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranslationSetsApi#translationSetsUpdateTranslationSetAttributes");
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
| **globalResourcesSharedModelsTranslationSetAttribute** | [**List&lt;GlobalResourcesSharedModelsTranslationSetAttribute&gt;**](GlobalResourcesSharedModelsTranslationSetAttribute.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | API Error Response |  -  |

<a id="translationSetsUpdateTranslationSetStrings"></a>
# **translationSetsUpdateTranslationSetStrings**
> translationSetsUpdateTranslationSetStrings(ID, globalResourcesSharedModelsTranslationSetString)

No Documentation Found.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranslationSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    TranslationSetsApi apiInstance = new TranslationSetsApi(defaultClient);
    Integer ID = 56; // Integer | 
    List<GlobalResourcesSharedModelsTranslationSetString> globalResourcesSharedModelsTranslationSetString = Arrays.asList(); // List<GlobalResourcesSharedModelsTranslationSetString> | 
    try {
      apiInstance.translationSetsUpdateTranslationSetStrings(ID, globalResourcesSharedModelsTranslationSetString);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranslationSetsApi#translationSetsUpdateTranslationSetStrings");
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
| **ID** | **Integer**|  | |
| **globalResourcesSharedModelsTranslationSetString** | [**List&lt;GlobalResourcesSharedModelsTranslationSetString&gt;**](GlobalResourcesSharedModelsTranslationSetString.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | API Error Response |  -  |

