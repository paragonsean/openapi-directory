# AttributeApi

All URIs are relative to *https://devdata.osisoft.com/piwebapi*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**attributeCreateAttribute**](AttributeApi.md#attributeCreateAttribute) | **POST** /attributes/{webId}/attributes | Create a new attribute as a child of the specified attribute. |
| [**attributeCreateConfig**](AttributeApi.md#attributeCreateConfig) | **POST** /attributes/{webId}/config | Create or update an attribute&#39;s DataReference configuration (Create/Update PI point for PI Point DataReference). |
| [**attributeDelete**](AttributeApi.md#attributeDelete) | **DELETE** /attributes/{webId} | Delete an attribute. |
| [**attributeGet**](AttributeApi.md#attributeGet) | **GET** /attributes/{webId} | Retrieve an attribute. |
| [**attributeGetAttributes**](AttributeApi.md#attributeGetAttributes) | **GET** /attributes/{webId}/attributes | Get the child attributes of the specified attribute. |
| [**attributeGetAttributesQuery**](AttributeApi.md#attributeGetAttributesQuery) | **GET** /attributes/search | Retrieve attributes based on the specified conditions. Returns attributes using the specified search query string. |
| [**attributeGetByPath**](AttributeApi.md#attributeGetByPath) | **GET** /attributes | Retrieve an attribute by path. |
| [**attributeGetCategories**](AttributeApi.md#attributeGetCategories) | **GET** /attributes/{webId}/categories | Get an attribute&#39;s categories. |
| [**attributeGetMultiple**](AttributeApi.md#attributeGetMultiple) | **GET** /attributes/multiple | Retrieve multiple attributes by web id or path. |
| [**attributeGetValue**](AttributeApi.md#attributeGetValue) | **GET** /attributes/{webId}/value | Get the attribute&#39;s value. This call is intended for use with attributes that have no data reference only. For attributes with a data reference, consult the documentation for Streams. |
| [**attributeSetValue**](AttributeApi.md#attributeSetValue) | **PUT** /attributes/{webId}/value | Set the value of a configuration item attribute. For attributes with a data reference or non-configuration item attributes, consult the documentation for streams. |
| [**attributeUpdate**](AttributeApi.md#attributeUpdate) | **PATCH** /attributes/{webId} | Update an attribute by replacing items in its definition. |


<a id="attributeCreateAttribute"></a>
# **attributeCreateAttribute**
> attributeCreateAttribute(webId, attribute, webIdType)

Create a new attribute as a child of the specified attribute.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AttributeApi apiInstance = new AttributeApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the parent attribute on which to create the attribute.
    Attribute attribute = new Attribute(); // Attribute | The definition of the new attribute.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      apiInstance.attributeCreateAttribute(webId, attribute, webIdType);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributeApi#attributeCreateAttribute");
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
| **webId** | **String**| The ID of the parent attribute on which to create the attribute. | |
| **attribute** | [**Attribute**](Attribute.md)| The definition of the new attribute. | |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The attribute was created. The response&#39;s Location header is a link to the created attribute. |  -  |

<a id="attributeCreateConfig"></a>
# **attributeCreateConfig**
> attributeCreateConfig(webId, webIdType)

Create or update an attribute&#39;s DataReference configuration (Create/Update PI point for PI Point DataReference).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AttributeApi apiInstance = new AttributeApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the attribute.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      apiInstance.attributeCreateConfig(webId, webIdType);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributeApi#attributeCreateConfig");
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
| **webId** | **String**| The ID of the attribute. | |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

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
| **201** | The attribute&#39;s DataReference configuration was created or updated. |  -  |

<a id="attributeDelete"></a>
# **attributeDelete**
> attributeDelete(webId)

Delete an attribute.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AttributeApi apiInstance = new AttributeApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the attribute.
    try {
      apiInstance.attributeDelete(webId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributeApi#attributeDelete");
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
| **webId** | **String**| The ID of the attribute. | |

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
| **204** | The attribute was deleted. |  -  |

<a id="attributeGet"></a>
# **attributeGet**
> Attribute attributeGet(webId, associations, selectedFields, webIdType)

Retrieve an attribute.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AttributeApi apiInstance = new AttributeApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the attribute.
    String associations = "associations_example"; // String | Associated values to return in the response, separated by semicolons (;). This call supports DataReference to return attributes with data references. If this parameter is not specified, DataReference values are not returned.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      Attribute result = apiInstance.attributeGet(webId, associations, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributeApi#attributeGet");
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
| **webId** | **String**| The ID of the attribute. | |
| **associations** | **String**| Associated values to return in the response, separated by semicolons (;). This call supports DataReference to return attributes with data references. If this parameter is not specified, DataReference values are not returned. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**Attribute**](Attribute.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested attribute. |  -  |

<a id="attributeGetAttributes"></a>
# **attributeGetAttributes**
> ItemsAttribute attributeGetAttributes(webId, associations, categoryName, maxCount, nameFilter, searchFullHierarchy, selectedFields, showExcluded, showHidden, sortField, sortOrder, startIndex, templateName, trait, traitCategory, valueType, webIdType)

Get the child attributes of the specified attribute.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AttributeApi apiInstance = new AttributeApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the parent attribute.
    String associations = "associations_example"; // String | Associated values to return in the response, separated by semicolons (;). This call supports DataReference to return attributes with data references. If this parameter is not specified, DataReference values are not returned.
    String categoryName = "categoryName_example"; // String | Specify that returned attributes must have this category. The default is no category filter.
    Integer maxCount = 56; // Integer | The maximum number of objects to be returned per call (page size). The default is 1000.
    String nameFilter = "nameFilter_example"; // String | The name query string used for finding attributes. The default is no filter.
    Boolean searchFullHierarchy = true; // Boolean | Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is 'false'.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    Boolean showExcluded = true; // Boolean | Specified if the search should include attributes with the Excluded property set. The default is 'false'.
    Boolean showHidden = true; // Boolean | Specified if the search should include attributes with the Hidden property set. The default is 'false'.
    String sortField = "sortField_example"; // String | The field or property of the object used to sort the returned collection. The default is 'Name'.
    String sortOrder = "sortOrder_example"; // String | The order that the returned collection is sorted. The default is 'Ascending'.
    Integer startIndex = 56; // Integer | The starting index (zero based) of the items to be returned. The default is 0.
    String templateName = "templateName_example"; // String | Specify that returned attributes must be members of this template. The default is no template filter.
    List<String> trait = Arrays.asList(); // List<String> | The name of the attribute trait. Multiple traits may be specified with multiple instances of the parameter.
    List<String> traitCategory = Arrays.asList(); // List<String> | The category of the attribute traits. Multiple categories may be specified with multiple instances of the parameter. If the parameter is not specified, or if its value is \"all\", then all attribute traits of all categories will be returned.
    String valueType = "valueType_example"; // String | Specify that returned attributes' value type must be the given value type. The default is no value type filter.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsAttribute result = apiInstance.attributeGetAttributes(webId, associations, categoryName, maxCount, nameFilter, searchFullHierarchy, selectedFields, showExcluded, showHidden, sortField, sortOrder, startIndex, templateName, trait, traitCategory, valueType, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributeApi#attributeGetAttributes");
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
| **webId** | **String**| The ID of the parent attribute. | |
| **associations** | **String**| Associated values to return in the response, separated by semicolons (;). This call supports DataReference to return attributes with data references. If this parameter is not specified, DataReference values are not returned. | [optional] |
| **categoryName** | **String**| Specify that returned attributes must have this category. The default is no category filter. | [optional] |
| **maxCount** | **Integer**| The maximum number of objects to be returned per call (page size). The default is 1000. | [optional] |
| **nameFilter** | **String**| The name query string used for finding attributes. The default is no filter. | [optional] |
| **searchFullHierarchy** | **Boolean**| Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is &#39;false&#39;. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **showExcluded** | **Boolean**| Specified if the search should include attributes with the Excluded property set. The default is &#39;false&#39;. | [optional] |
| **showHidden** | **Boolean**| Specified if the search should include attributes with the Hidden property set. The default is &#39;false&#39;. | [optional] |
| **sortField** | **String**| The field or property of the object used to sort the returned collection. The default is &#39;Name&#39;. | [optional] |
| **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] |
| **startIndex** | **Integer**| The starting index (zero based) of the items to be returned. The default is 0. | [optional] |
| **templateName** | **String**| Specify that returned attributes must be members of this template. The default is no template filter. | [optional] |
| **trait** | [**List&lt;String&gt;**](String.md)| The name of the attribute trait. Multiple traits may be specified with multiple instances of the parameter. | [optional] |
| **traitCategory** | [**List&lt;String&gt;**](String.md)| The category of the attribute traits. Multiple categories may be specified with multiple instances of the parameter. If the parameter is not specified, or if its value is \&quot;all\&quot;, then all attribute traits of all categories will be returned. | [optional] |
| **valueType** | **String**| Specify that returned attributes&#39; value type must be the given value type. The default is no value type filter. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsAttribute**](ItemsAttribute.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of child attributes. |  -  |

<a id="attributeGetAttributesQuery"></a>
# **attributeGetAttributesQuery**
> ItemsAttribute attributeGetAttributesQuery(associations, databaseWebId, maxCount, query, selectedFields, startIndex, webIdType)

Retrieve attributes based on the specified conditions. Returns attributes using the specified search query string.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AttributeApi apiInstance = new AttributeApi(defaultClient);
    String associations = "associations_example"; // String | Associated values to return in the response, separated by semicolons (;). This call supports DataReference to return attributes with data references. If this parameter is not specified, DataReference values are not returned.
    String databaseWebId = "databaseWebId_example"; // String | The ID of the asset database to use as the root of the query.
    Integer maxCount = 56; // Integer | The maximum number of objects to be returned per call (page size). The default is 1000.
    String query = "query_example"; // String | The query string is a list of filters used to perform an AFSearch for the attributes in the asset database. An example would be: \"query=Element:{ Name:='MyElement' } Type:=Int32\".
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    Integer startIndex = 56; // Integer | The starting index (zero based) of the items to be returned. The default is 0.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsAttribute result = apiInstance.attributeGetAttributesQuery(associations, databaseWebId, maxCount, query, selectedFields, startIndex, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributeApi#attributeGetAttributesQuery");
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
| **associations** | **String**| Associated values to return in the response, separated by semicolons (;). This call supports DataReference to return attributes with data references. If this parameter is not specified, DataReference values are not returned. | [optional] |
| **databaseWebId** | **String**| The ID of the asset database to use as the root of the query. | [optional] |
| **maxCount** | **Integer**| The maximum number of objects to be returned per call (page size). The default is 1000. | [optional] |
| **query** | **String**| The query string is a list of filters used to perform an AFSearch for the attributes in the asset database. An example would be: \&quot;query&#x3D;Element:{ Name:&#x3D;&#39;MyElement&#39; } Type:&#x3D;Int32\&quot;. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **startIndex** | **Integer**| The starting index (zero based) of the items to be returned. The default is 0. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsAttribute**](ItemsAttribute.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of attributes matching the specified conditions. |  -  |

<a id="attributeGetByPath"></a>
# **attributeGetByPath**
> Attribute attributeGetByPath(path, associations, selectedFields, webIdType)

Retrieve an attribute by path.

This method returns an attribute based on the hierarchical path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AttributeApi apiInstance = new AttributeApi(defaultClient);
    String path = "path_example"; // String | The path to the attribute.
    String associations = "associations_example"; // String | Associated values to return in the response, separated by semicolons (;). This call supports DataReference to return attributes with data references. If this parameter is not specified, DataReference values are not returned.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      Attribute result = apiInstance.attributeGetByPath(path, associations, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributeApi#attributeGetByPath");
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
| **path** | **String**| The path to the attribute. | |
| **associations** | **String**| Associated values to return in the response, separated by semicolons (;). This call supports DataReference to return attributes with data references. If this parameter is not specified, DataReference values are not returned. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**Attribute**](Attribute.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested attribute. |  -  |

<a id="attributeGetCategories"></a>
# **attributeGetCategories**
> ItemsAttributeCategory attributeGetCategories(webId, selectedFields, webIdType)

Get an attribute&#39;s categories.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AttributeApi apiInstance = new AttributeApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the attribute.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsAttributeCategory result = apiInstance.attributeGetCategories(webId, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributeApi#attributeGetCategories");
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
| **webId** | **String**| The ID of the attribute. | |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsAttributeCategory**](ItemsAttributeCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of categories. |  -  |

<a id="attributeGetMultiple"></a>
# **attributeGetMultiple**
> ItemsItemAttribute attributeGetMultiple(asParallel, associations, includeMode, path, selectedFields, webId, webIdType)

Retrieve multiple attributes by web id or path.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AttributeApi apiInstance = new AttributeApi(defaultClient);
    Boolean asParallel = true; // Boolean | Specifies if the retrieval processes should be run in parallel on the server. This may improve the response time for large amounts of requested attributes. The default is 'false'.
    String associations = "associations_example"; // String | Associated values to return in the response, separated by semicolons (;). This call supports DataReference to return attributes with data references. If this parameter is not specified, DataReference values are not returned.
    String includeMode = "includeMode_example"; // String | The include mode for the return list. The default is 'All'.
    List<String> path = Arrays.asList(); // List<String> | The path of an attribute. Multiple attributes may be specified with multiple instances of the parameter.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    List<String> webId = Arrays.asList(); // List<String> | The ID of an attribute. Multiple attributes may be specified with multiple instances of the parameter.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsItemAttribute result = apiInstance.attributeGetMultiple(asParallel, associations, includeMode, path, selectedFields, webId, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributeApi#attributeGetMultiple");
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
| **asParallel** | **Boolean**| Specifies if the retrieval processes should be run in parallel on the server. This may improve the response time for large amounts of requested attributes. The default is &#39;false&#39;. | [optional] |
| **associations** | **String**| Associated values to return in the response, separated by semicolons (;). This call supports DataReference to return attributes with data references. If this parameter is not specified, DataReference values are not returned. | [optional] |
| **includeMode** | **String**| The include mode for the return list. The default is &#39;All&#39;. | [optional] |
| **path** | [**List&lt;String&gt;**](String.md)| The path of an attribute. Multiple attributes may be specified with multiple instances of the parameter. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **webId** | [**List&lt;String&gt;**](String.md)| The ID of an attribute. Multiple attributes may be specified with multiple instances of the parameter. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsItemAttribute**](ItemsItemAttribute.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested attributes |  -  |
| **207** | Some or all items contain exceptions. |  -  |

<a id="attributeGetValue"></a>
# **attributeGetValue**
> TimedValue attributeGetValue(webId, selectedFields)

Get the attribute&#39;s value. This call is intended for use with attributes that have no data reference only. For attributes with a data reference, consult the documentation for Streams.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AttributeApi apiInstance = new AttributeApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the attribute.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    try {
      TimedValue result = apiInstance.attributeGetValue(webId, selectedFields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributeApi#attributeGetValue");
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
| **webId** | **String**| The ID of the attribute. | |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |

### Return type

[**TimedValue**](TimedValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The attribute&#39;s value. |  -  |

<a id="attributeSetValue"></a>
# **attributeSetValue**
> attributeSetValue(webId, value)

Set the value of a configuration item attribute. For attributes with a data reference or non-configuration item attributes, consult the documentation for streams.

Users must be aware of the value type that the attribute takes before changing the value. If a value entered by the user does not match the value type expressed in the attribute, it will not work or it will return an error. Users should also be careful of what the value type means, for instance, if a value type accepts strings and the user enters a number, the attribute will interpret it as a string of characters and not as the integer value that the user may have wanted.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AttributeApi apiInstance = new AttributeApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the attribute.
    TimedValue value = new TimedValue(); // TimedValue | The value to write.
    try {
      apiInstance.attributeSetValue(webId, value);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributeApi#attributeSetValue");
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
| **webId** | **String**| The ID of the attribute. | |
| **value** | [**TimedValue**](TimedValue.md)| The value to write. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The value was set successfully. |  -  |

<a id="attributeUpdate"></a>
# **attributeUpdate**
> attributeUpdate(webId, attribute)

Update an attribute by replacing items in its definition.

If an attribute is based on a template, the user must make sure to update the attribute appropriately so that it does not conflict with the template&#39;s design. Once a template is applied to an attribute, it can not be changed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AttributeApi apiInstance = new AttributeApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the attribute.
    Attribute attribute = new Attribute(); // Attribute | A partial attribute containing the desired changes.
    try {
      apiInstance.attributeUpdate(webId, attribute);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributeApi#attributeUpdate");
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
| **webId** | **String**| The ID of the attribute. | |
| **attribute** | [**Attribute**](Attribute.md)| A partial attribute containing the desired changes. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The attribute was updated. |  -  |

