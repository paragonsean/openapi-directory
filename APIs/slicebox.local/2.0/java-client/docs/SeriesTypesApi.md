# SeriesTypesApi

All URIs are relative to *http://slicebox.local/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**seriestypesGet**](SeriesTypesApi.md#seriestypesGet) | **GET** /seriestypes |  |
| [**seriestypesIdDelete**](SeriesTypesApi.md#seriestypesIdDelete) | **DELETE** /seriestypes/{id} |  |
| [**seriestypesIdPut**](SeriesTypesApi.md#seriestypesIdPut) | **PUT** /seriestypes/{id} |  |
| [**seriestypesPost**](SeriesTypesApi.md#seriestypesPost) | **POST** /seriestypes |  |
| [**seriestypesRulesGet**](SeriesTypesApi.md#seriestypesRulesGet) | **GET** /seriestypes/rules |  |
| [**seriestypesRulesIdAttributesGet**](SeriesTypesApi.md#seriestypesRulesIdAttributesGet) | **GET** /seriestypes/rules/{id}/attributes |  |
| [**seriestypesRulesIdAttributesPost**](SeriesTypesApi.md#seriestypesRulesIdAttributesPost) | **POST** /seriestypes/rules/{id}/attributes |  |
| [**seriestypesRulesIdDelete**](SeriesTypesApi.md#seriestypesRulesIdDelete) | **DELETE** /seriestypes/rules/{id} |  |
| [**seriestypesRulesPost**](SeriesTypesApi.md#seriestypesRulesPost) | **POST** /seriestypes/rules |  |
| [**seriestypesRulesRuleIdAttributesAttributeIdDelete**](SeriesTypesApi.md#seriestypesRulesRuleIdAttributesAttributeIdDelete) | **DELETE** /seriestypes/rules/{ruleId}/attributes/{attributeId} |  |
| [**seriestypesRulesUpdatestatusGet**](SeriesTypesApi.md#seriestypesRulesUpdatestatusGet) | **GET** /seriestypes/rules/updatestatus |  |


<a id="seriestypesGet"></a>
# **seriestypesGet**
> List&lt;Seriestype&gt; seriestypesGet(startindex, count)



get a list of all added series types. By filtering search results for certain series types, it is easier for applications to ensure that they read images of applicable types.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SeriesTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    SeriesTypesApi apiInstance = new SeriesTypesApi(defaultClient);
    Long startindex = 0L; // Long | start index of returned slice of series types
    Long count = 20L; // Long | size of returned slice of series types
    try {
      List<Seriestype> result = apiInstance.seriestypesGet(startindex, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SeriesTypesApi#seriestypesGet");
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
| **startindex** | **Long**| start index of returned slice of series types | [optional] [default to 0] |
| **count** | **Long**| size of returned slice of series types | [optional] [default to 20] |

### Return type

[**List&lt;Seriestype&gt;**](Seriestype.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the list of series types |  -  |

<a id="seriestypesIdDelete"></a>
# **seriestypesIdDelete**
> seriestypesIdDelete(id)



remove the series type corresponding to the supplied ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SeriesTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    SeriesTypesApi apiInstance = new SeriesTypesApi(defaultClient);
    Long id = 56L; // Long | id of series type to remove
    try {
      apiInstance.seriestypesIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling SeriesTypesApi#seriestypesIdDelete");
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
| **id** | **Long**| id of series type to remove | |

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
| **204** | series type removed |  -  |

<a id="seriestypesIdPut"></a>
# **seriestypesIdPut**
> seriestypesIdPut(id)



request an asynchronous update of all series, labelling appropriate series with the series type corresponding to the supplied ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SeriesTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    SeriesTypesApi apiInstance = new SeriesTypesApi(defaultClient);
    Long id = 56L; // Long | id of series type to update series labels for
    try {
      apiInstance.seriestypesIdPut(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling SeriesTypesApi#seriestypesIdPut");
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
| **id** | **Long**| id of series type to update series labels for | |

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
| **204** | update successfully added to queue of series type updates |  -  |

<a id="seriestypesPost"></a>
# **seriestypesPost**
> Seriestype seriestypesPost(seriesType)



add a new series type

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SeriesTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    SeriesTypesApi apiInstance = new SeriesTypesApi(defaultClient);
    Seriestype seriesType = new Seriestype(); // Seriestype | Series type information. The ID property is irrelevant, the ID of the inserted record is present in the returned data.
    try {
      Seriestype result = apiInstance.seriestypesPost(seriesType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SeriesTypesApi#seriestypesPost");
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
| **seriesType** | [**Seriestype**](Seriestype.md)| Series type information. The ID property is irrelevant, the ID of the inserted record is present in the returned data. | [optional] |

### Return type

[**Seriestype**](Seriestype.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream, multipart/form-data
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | the created series type |  -  |

<a id="seriestypesRulesGet"></a>
# **seriestypesRulesGet**
> List&lt;Seriestyperule&gt; seriestypesRulesGet(seriestypeid)



get a list of rules for assigning series types to series. A rule connects to a series of attributes with values and a resulting series type. If a series has the required values of the listed attributes, it is assigned to the series type of the rule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SeriesTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    SeriesTypesApi apiInstance = new SeriesTypesApi(defaultClient);
    Long seriestypeid = 56L; // Long | ID of series type to list rules for
    try {
      List<Seriestyperule> result = apiInstance.seriestypesRulesGet(seriestypeid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SeriesTypesApi#seriestypesRulesGet");
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
| **seriestypeid** | **Long**| ID of series type to list rules for | |

### Return type

[**List&lt;Seriestyperule&gt;**](Seriestyperule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the list of series type rules for the series type with the supplied ID |  -  |

<a id="seriestypesRulesIdAttributesGet"></a>
# **seriestypesRulesIdAttributesGet**
> List&lt;Seriestyperuleattribute&gt; seriestypesRulesIdAttributesGet(id)



get the list of attributes for the series type rule with the supplied ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SeriesTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    SeriesTypesApi apiInstance = new SeriesTypesApi(defaultClient);
    Long id = 56L; // Long | index of series type rule to list rule attributes for
    try {
      List<Seriestyperuleattribute> result = apiInstance.seriestypesRulesIdAttributesGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SeriesTypesApi#seriestypesRulesIdAttributesGet");
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
| **id** | **Long**| index of series type rule to list rule attributes for | |

### Return type

[**List&lt;Seriestyperuleattribute&gt;**](Seriestyperuleattribute.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the list of series type rule attributes for the series type rule with the supplied ID |  -  |

<a id="seriestypesRulesIdAttributesPost"></a>
# **seriestypesRulesIdAttributesPost**
> Seriestyperuleattribute seriestypesRulesIdAttributesPost(id, seriesTypeRuleAttribute)



add a new series type rule attribute

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SeriesTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    SeriesTypesApi apiInstance = new SeriesTypesApi(defaultClient);
    Long id = 56L; // Long | ID of rule
    Seriestyperuleattribute seriesTypeRuleAttribute = new Seriestyperuleattribute(); // Seriestyperuleattribute | Series type rule attribute information. The ID property is irrelevant, the ID of the inserted record is present in the returned data.
    try {
      Seriestyperuleattribute result = apiInstance.seriestypesRulesIdAttributesPost(id, seriesTypeRuleAttribute);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SeriesTypesApi#seriestypesRulesIdAttributesPost");
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
| **id** | **Long**| ID of rule | |
| **seriesTypeRuleAttribute** | [**Seriestyperuleattribute**](Seriestyperuleattribute.md)| Series type rule attribute information. The ID property is irrelevant, the ID of the inserted record is present in the returned data. | [optional] |

### Return type

[**Seriestyperuleattribute**](Seriestyperuleattribute.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream, multipart/form-data
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | the created series type rule attribute |  -  |

<a id="seriestypesRulesIdDelete"></a>
# **seriestypesRulesIdDelete**
> seriestypesRulesIdDelete(id)



remove the series type rule corresponding to the supplied ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SeriesTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    SeriesTypesApi apiInstance = new SeriesTypesApi(defaultClient);
    Long id = 56L; // Long | id of series type rule to remove
    try {
      apiInstance.seriestypesRulesIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling SeriesTypesApi#seriestypesRulesIdDelete");
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
| **id** | **Long**| id of series type rule to remove | |

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
| **204** | series type rule removed |  -  |

<a id="seriestypesRulesPost"></a>
# **seriestypesRulesPost**
> Seriestyperule seriestypesRulesPost(seriesTypeRule)



add a new series type rule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SeriesTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    SeriesTypesApi apiInstance = new SeriesTypesApi(defaultClient);
    Seriestyperule seriesTypeRule = new Seriestyperule(); // Seriestyperule | Series type rule information. The ID property is irrelevant, the ID of the inserted record is present in the returned data.
    try {
      Seriestyperule result = apiInstance.seriestypesRulesPost(seriesTypeRule);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SeriesTypesApi#seriestypesRulesPost");
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
| **seriesTypeRule** | [**Seriestyperule**](Seriestyperule.md)| Series type rule information. The ID property is irrelevant, the ID of the inserted record is present in the returned data. | [optional] |

### Return type

[**Seriestyperule**](Seriestyperule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream, multipart/form-data
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | the created series type rule |  -  |

<a id="seriestypesRulesRuleIdAttributesAttributeIdDelete"></a>
# **seriestypesRulesRuleIdAttributesAttributeIdDelete**
> seriestypesRulesRuleIdAttributesAttributeIdDelete(ruleId, attributeId)



remove the series type rule attribute corresponding to the supplied series type and attribute IDs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SeriesTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    SeriesTypesApi apiInstance = new SeriesTypesApi(defaultClient);
    Long ruleId = 56L; // Long | id of series type rule for which to remove an attribute
    Long attributeId = 56L; // Long | id of attribute to remove
    try {
      apiInstance.seriestypesRulesRuleIdAttributesAttributeIdDelete(ruleId, attributeId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SeriesTypesApi#seriestypesRulesRuleIdAttributesAttributeIdDelete");
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
| **ruleId** | **Long**| id of series type rule for which to remove an attribute | |
| **attributeId** | **Long**| id of attribute to remove | |

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
| **204** | series type rule attribute removed |  -  |

<a id="seriestypesRulesUpdatestatusGet"></a>
# **seriestypesRulesUpdatestatusGet**
> Seriestypeupdatestatus seriestypesRulesUpdatestatusGet()



get the status of the internal process of updating series types for series following a change of series types, rules or attributes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SeriesTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    SeriesTypesApi apiInstance = new SeriesTypesApi(defaultClient);
    try {
      Seriestypeupdatestatus result = apiInstance.seriestypesRulesUpdatestatusGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SeriesTypesApi#seriestypesRulesUpdatestatusGet");
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

[**Seriestypeupdatestatus**](Seriestypeupdatestatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | a status message, indicating if an update is running |  -  |

