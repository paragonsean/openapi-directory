# StringDefinitionsApi

All URIs are relative to *https://secure.agco-ats.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**stringDefinitionsGetDefinition**](StringDefinitionsApi.md#stringDefinitionsGetDefinition) | **GET** /api/v2/StringDefinitions/{ID} | Get a paged response of Global String Definitions. |
| [**stringDefinitionsGetDefinitions**](StringDefinitionsApi.md#stringDefinitionsGetDefinitions) | **GET** /api/v2/StringDefinitions | Get a paged response of Global String Definitions. |
| [**stringDefinitionsPostDefinition**](StringDefinitionsApi.md#stringDefinitionsPostDefinition) | **POST** /api/v2/StringDefinitions/Batch | Create StringDefinition object. The originating translation must be provided. Accepts an array of StringDefinition objects. Returns nothing. |
| [**stringDefinitionsUpdateDefinitions**](StringDefinitionsApi.md#stringDefinitionsUpdateDefinitions) | **PUT** /api/v2/StringDefinitions/Batch | Update StringDefinition objects. Accepts an array of StringDefinition objects. This endpoint will add StringDefinitionChange objects to the database. The DescriptionForTranslator may not be modified after a String is submitted for translation. |


<a id="stringDefinitionsGetDefinition"></a>
# **stringDefinitionsGetDefinition**
> GlobalResourcesSharedModelsStringDefinition stringDefinitionsGetDefinition(ID, includeTranslations, includeDeletedLanguages, languageIds)

Get a paged response of Global String Definitions.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StringDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    StringDefinitionsApi apiInstance = new StringDefinitionsApi(defaultClient);
    String ID = "ID_example"; // String | 
    Boolean includeTranslations = true; // Boolean | Optional. Indicates whether to include the StringTranslations for the StringDefinition. Defaults to false.
    Boolean includeDeletedLanguages = true; // Boolean | Optional. Indicates whether to include languages marked as deleted. includeTranslations must be true. Defaults to false.
    String languageIds = "languageIds_example"; // String | Optional. A comma-delimited list of language ids. Only StringTranslation objects with a matching language id will be returned. Optional. By default all locales are returned. includeTranslations must be true. The StringDefinition is still returned even if the filtered translations list is empty.
    try {
      GlobalResourcesSharedModelsStringDefinition result = apiInstance.stringDefinitionsGetDefinition(ID, includeTranslations, includeDeletedLanguages, languageIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StringDefinitionsApi#stringDefinitionsGetDefinition");
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
| **ID** | **String**|  | |
| **includeTranslations** | **Boolean**| Optional. Indicates whether to include the StringTranslations for the StringDefinition. Defaults to false. | [optional] |
| **includeDeletedLanguages** | **Boolean**| Optional. Indicates whether to include languages marked as deleted. includeTranslations must be true. Defaults to false. | [optional] |
| **languageIds** | **String**| Optional. A comma-delimited list of language ids. Only StringTranslation objects with a matching language id will be returned. Optional. By default all locales are returned. includeTranslations must be true. The StringDefinition is still returned even if the filtered translations list is empty. | [optional] |

### Return type

[**GlobalResourcesSharedModelsStringDefinition**](GlobalResourcesSharedModelsStringDefinition.md)

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

<a id="stringDefinitionsGetDefinitions"></a>
# **stringDefinitionsGetDefinitions**
> APIIPagedResponseGlobalResourcesSharedModelsStringDefinition stringDefinitionsGetDefinitions(limit, modifiedAfterTimestamp, includeTranslations, stringText, descriptionText, useFullText, includeDeletedLanguages, languageIds, stringIds, matchingTranslationsOnly)

Get a paged response of Global String Definitions.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StringDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    StringDefinitionsApi apiInstance = new StringDefinitionsApi(defaultClient);
    Integer limit = 56; // Integer | Optional. The page limit. The default page limit is 10. Ignored if 'stringIds' is provided.
    String modifiedAfterTimestamp = "modifiedAfterTimestamp_example"; // String | Optional. Return only the StringDefinition objects that have a Timestamp value greater than that provided. This will be an encoded byte array.
    Boolean includeTranslations = true; // Boolean | Optional. Indicates whether to include the StringTranslations for the StringDefinition. Defaults to false.
    String stringText = "stringText_example"; // String | Optional. The text for which to search in the StringDefinition object’s translations. Only StringDefinition objects for matching StringTranslation objects are returned. Does not filter if no value is provided. Supports beginning and/or ending wildcards. includeTranslations must be true.
    String descriptionText = "descriptionText_example"; // String | Optional. The text for which to search in the StringDefinition description field. Only matching objects are returned. Does not filter if no value is provided. Supports beginning and/or ending wildcards.
    Boolean useFullText = true; // Boolean | Optional. This flag is used to determin whether to use the FullText Search or not.
    Boolean includeDeletedLanguages = true; // Boolean | Optional. Indicates whether to include languages marked as deleted. includeTranslations must be true. Defaults to false.
    String languageIds = "languageIds_example"; // String | Optional. A comma-delimited list of language ids. Only StringTranslation objects with a matching language id will be returned. Optional. By default all locales are returned. includeTranslations must be true. The StringDefinition is still returned even if the filtered translations list is empty.
    String stringIds = "stringIds_example"; // String | Optional. A comma-delimited list of string ids. Up to 40 string IDs may be provided. May not be used with 'modifiedAfterTimestamp', 'stringText', 'descriptionText', or 'useFullText'.
    Boolean matchingTranslationsOnly = true; // Boolean | Optional. If false, all translations for returned String Definitions are included. Must be used with 'stringText' provided and 'includeTranslations' = true.
    try {
      APIIPagedResponseGlobalResourcesSharedModelsStringDefinition result = apiInstance.stringDefinitionsGetDefinitions(limit, modifiedAfterTimestamp, includeTranslations, stringText, descriptionText, useFullText, includeDeletedLanguages, languageIds, stringIds, matchingTranslationsOnly);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StringDefinitionsApi#stringDefinitionsGetDefinitions");
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
| **limit** | **Integer**| Optional. The page limit. The default page limit is 10. Ignored if &#39;stringIds&#39; is provided. | [optional] |
| **modifiedAfterTimestamp** | **String**| Optional. Return only the StringDefinition objects that have a Timestamp value greater than that provided. This will be an encoded byte array. | [optional] |
| **includeTranslations** | **Boolean**| Optional. Indicates whether to include the StringTranslations for the StringDefinition. Defaults to false. | [optional] |
| **stringText** | **String**| Optional. The text for which to search in the StringDefinition object’s translations. Only StringDefinition objects for matching StringTranslation objects are returned. Does not filter if no value is provided. Supports beginning and/or ending wildcards. includeTranslations must be true. | [optional] |
| **descriptionText** | **String**| Optional. The text for which to search in the StringDefinition description field. Only matching objects are returned. Does not filter if no value is provided. Supports beginning and/or ending wildcards. | [optional] |
| **useFullText** | **Boolean**| Optional. This flag is used to determin whether to use the FullText Search or not. | [optional] |
| **includeDeletedLanguages** | **Boolean**| Optional. Indicates whether to include languages marked as deleted. includeTranslations must be true. Defaults to false. | [optional] |
| **languageIds** | **String**| Optional. A comma-delimited list of language ids. Only StringTranslation objects with a matching language id will be returned. Optional. By default all locales are returned. includeTranslations must be true. The StringDefinition is still returned even if the filtered translations list is empty. | [optional] |
| **stringIds** | **String**| Optional. A comma-delimited list of string ids. Up to 40 string IDs may be provided. May not be used with &#39;modifiedAfterTimestamp&#39;, &#39;stringText&#39;, &#39;descriptionText&#39;, or &#39;useFullText&#39;. | [optional] |
| **matchingTranslationsOnly** | **Boolean**| Optional. If false, all translations for returned String Definitions are included. Must be used with &#39;stringText&#39; provided and &#39;includeTranslations&#39; &#x3D; true. | [optional] |

### Return type

[**APIIPagedResponseGlobalResourcesSharedModelsStringDefinition**](APIIPagedResponseGlobalResourcesSharedModelsStringDefinition.md)

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

<a id="stringDefinitionsPostDefinition"></a>
# **stringDefinitionsPostDefinition**
> stringDefinitionsPostDefinition(globalResourcesSharedModelsStringDefinition)

Create StringDefinition object. The originating translation must be provided. Accepts an array of StringDefinition objects. Returns nothing.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StringDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    StringDefinitionsApi apiInstance = new StringDefinitionsApi(defaultClient);
    List<GlobalResourcesSharedModelsStringDefinition> globalResourcesSharedModelsStringDefinition = Arrays.asList(); // List<GlobalResourcesSharedModelsStringDefinition> | The StringDefinition Object array, along with originating translation.
    try {
      apiInstance.stringDefinitionsPostDefinition(globalResourcesSharedModelsStringDefinition);
    } catch (ApiException e) {
      System.err.println("Exception when calling StringDefinitionsApi#stringDefinitionsPostDefinition");
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
| **globalResourcesSharedModelsStringDefinition** | [**List&lt;GlobalResourcesSharedModelsStringDefinition&gt;**](GlobalResourcesSharedModelsStringDefinition.md)| The StringDefinition Object array, along with originating translation. | |

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

<a id="stringDefinitionsUpdateDefinitions"></a>
# **stringDefinitionsUpdateDefinitions**
> stringDefinitionsUpdateDefinitions(globalResourcesSharedModelsStringDefinition)

Update StringDefinition objects. Accepts an array of StringDefinition objects. This endpoint will add StringDefinitionChange objects to the database. The DescriptionForTranslator may not be modified after a String is submitted for translation.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StringDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    StringDefinitionsApi apiInstance = new StringDefinitionsApi(defaultClient);
    List<GlobalResourcesSharedModelsStringDefinition> globalResourcesSharedModelsStringDefinition = Arrays.asList(); // List<GlobalResourcesSharedModelsStringDefinition> | The Array of Definitions to update
    try {
      apiInstance.stringDefinitionsUpdateDefinitions(globalResourcesSharedModelsStringDefinition);
    } catch (ApiException e) {
      System.err.println("Exception when calling StringDefinitionsApi#stringDefinitionsUpdateDefinitions");
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
| **globalResourcesSharedModelsStringDefinition** | [**List&lt;GlobalResourcesSharedModelsStringDefinition&gt;**](GlobalResourcesSharedModelsStringDefinition.md)| The Array of Definitions to update | |

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

