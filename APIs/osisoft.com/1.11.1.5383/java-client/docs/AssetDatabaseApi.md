# AssetDatabaseApi

All URIs are relative to *https://devdata.osisoft.com/piwebapi*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**assetDatabaseAddReferencedElement**](AssetDatabaseApi.md#assetDatabaseAddReferencedElement) | **POST** /assetdatabases/{webId}/referencedelements | Add a reference to an existing element to the specified database. |
| [**assetDatabaseCreateAnalysisCategory**](AssetDatabaseApi.md#assetDatabaseCreateAnalysisCategory) | **POST** /assetdatabases/{webId}/analysiscategories | Create an analysis category at the Asset Database root. |
| [**assetDatabaseCreateAnalysisTemplate**](AssetDatabaseApi.md#assetDatabaseCreateAnalysisTemplate) | **POST** /assetdatabases/{webId}/analysistemplates | Create an analysis template at the Asset Database root. |
| [**assetDatabaseCreateAttributeCategory**](AssetDatabaseApi.md#assetDatabaseCreateAttributeCategory) | **POST** /assetdatabases/{webId}/attributecategories | Create an attribute category at the Asset Database root. |
| [**assetDatabaseCreateElement**](AssetDatabaseApi.md#assetDatabaseCreateElement) | **POST** /assetdatabases/{webId}/elements | Create a child element. |
| [**assetDatabaseCreateElementCategory**](AssetDatabaseApi.md#assetDatabaseCreateElementCategory) | **POST** /assetdatabases/{webId}/elementcategories | Create an element category at the Asset Database root. |
| [**assetDatabaseCreateElementTemplate**](AssetDatabaseApi.md#assetDatabaseCreateElementTemplate) | **POST** /assetdatabases/{webId}/elementtemplates | Create a template at the Asset Database root. Specify InstanceType of \&quot;Element\&quot; or \&quot;EventFrame\&quot; to create element or event frame template respectively. Only these two types of templates can be created. |
| [**assetDatabaseCreateEnumerationSet**](AssetDatabaseApi.md#assetDatabaseCreateEnumerationSet) | **POST** /assetdatabases/{webId}/enumerationsets | Create an enumeration set at the Asset Database. |
| [**assetDatabaseCreateEventFrame**](AssetDatabaseApi.md#assetDatabaseCreateEventFrame) | **POST** /assetdatabases/{webId}/eventframes | Create an event frame. |
| [**assetDatabaseCreateSecurityEntry**](AssetDatabaseApi.md#assetDatabaseCreateSecurityEntry) | **POST** /assetdatabases/{webId}/securityentries | Create a security entry owned by the asset database. |
| [**assetDatabaseCreateTable**](AssetDatabaseApi.md#assetDatabaseCreateTable) | **POST** /assetdatabases/{webId}/tables | Create a table on the Asset Database. |
| [**assetDatabaseCreateTableCategory**](AssetDatabaseApi.md#assetDatabaseCreateTableCategory) | **POST** /assetdatabases/{webId}/tablecategories | Create a table category on the Asset Database. |
| [**assetDatabaseDelete**](AssetDatabaseApi.md#assetDatabaseDelete) | **DELETE** /assetdatabases/{webId} | Delete an asset database. |
| [**assetDatabaseDeleteSecurityEntry**](AssetDatabaseApi.md#assetDatabaseDeleteSecurityEntry) | **DELETE** /assetdatabases/{webId}/securityentries/{name} | Delete a security entry owned by the asset database. |
| [**assetDatabaseExport**](AssetDatabaseApi.md#assetDatabaseExport) | **GET** /assetdatabases/{webId}/export | Export the asset database. |
| [**assetDatabaseFindAnalyses**](AssetDatabaseApi.md#assetDatabaseFindAnalyses) | **GET** /assetdatabases/{webId}/analyses | Retrieve analyses based on the specified conditions. |
| [**assetDatabaseFindElementAttributes**](AssetDatabaseApi.md#assetDatabaseFindElementAttributes) | **GET** /assetdatabases/{webId}/elementattributes | Retrieves a list of element attributes matching the specified filters from the specified asset database. |
| [**assetDatabaseFindEventFrameAttributes**](AssetDatabaseApi.md#assetDatabaseFindEventFrameAttributes) | **GET** /assetdatabases/{webId}/eventframeattributes | Retrieves a list of event frame attributes matching the specified filters from the specified asset database. |
| [**assetDatabaseGet**](AssetDatabaseApi.md#assetDatabaseGet) | **GET** /assetdatabases/{webId} | Retrieve an Asset Database. |
| [**assetDatabaseGetAnalysisCategories**](AssetDatabaseApi.md#assetDatabaseGetAnalysisCategories) | **GET** /assetdatabases/{webId}/analysiscategories | Retrieve analysis categories for a given Asset Database. |
| [**assetDatabaseGetAnalysisTemplates**](AssetDatabaseApi.md#assetDatabaseGetAnalysisTemplates) | **GET** /assetdatabases/{webId}/analysistemplates | Retrieve analysis templates based on the specified criteria. By default, all analysis templates in the specified Asset Database are returned. |
| [**assetDatabaseGetAttributeCategories**](AssetDatabaseApi.md#assetDatabaseGetAttributeCategories) | **GET** /assetdatabases/{webId}/attributecategories | Retrieve attribute categories for a given Asset Database. |
| [**assetDatabaseGetByPath**](AssetDatabaseApi.md#assetDatabaseGetByPath) | **GET** /assetdatabases | Retrieve an Asset Database by path. |
| [**assetDatabaseGetElementCategories**](AssetDatabaseApi.md#assetDatabaseGetElementCategories) | **GET** /assetdatabases/{webId}/elementcategories | Retrieve element categories for a given Asset Database. |
| [**assetDatabaseGetElementTemplates**](AssetDatabaseApi.md#assetDatabaseGetElementTemplates) | **GET** /assetdatabases/{webId}/elementtemplates | Retrieve element templates based on the specified criteria. Only templates of instance type \&quot;Element\&quot; and \&quot;EventFrame\&quot; are returned. By default, all element and event frame templates in the specified Asset Database are returned. |
| [**assetDatabaseGetElements**](AssetDatabaseApi.md#assetDatabaseGetElements) | **GET** /assetdatabases/{webId}/elements | Retrieve elements based on the specified conditions. By default, this method selects immediate children of the specified asset database. |
| [**assetDatabaseGetEnumerationSets**](AssetDatabaseApi.md#assetDatabaseGetEnumerationSets) | **GET** /assetdatabases/{webId}/enumerationsets | Retrieve enumeration sets for given asset database. |
| [**assetDatabaseGetEventFrames**](AssetDatabaseApi.md#assetDatabaseGetEventFrames) | **GET** /assetdatabases/{webId}/eventframes | Retrieve event frames based on the specified conditions. By default, returns all children of the specified root resource that have been active in the past 8 hours. |
| [**assetDatabaseGetReferencedElements**](AssetDatabaseApi.md#assetDatabaseGetReferencedElements) | **GET** /assetdatabases/{webId}/referencedelements | Retrieve referenced elements based on the specified conditions. By default, this method selects all referenced elements at the root level of the asset database. |
| [**assetDatabaseGetSecurity**](AssetDatabaseApi.md#assetDatabaseGetSecurity) | **GET** /assetdatabases/{webId}/security | Get the security information of the specified security item associated with the asset database for a specified user. |
| [**assetDatabaseGetSecurityEntries**](AssetDatabaseApi.md#assetDatabaseGetSecurityEntries) | **GET** /assetdatabases/{webId}/securityentries | Retrieve the security entries of the specified security item associated with the asset database based on the specified criteria. By default, all security entries for this asset database are returned. |
| [**assetDatabaseGetSecurityEntryByName**](AssetDatabaseApi.md#assetDatabaseGetSecurityEntryByName) | **GET** /assetdatabases/{webId}/securityentries/{name} | Retrieve the security entry of the specified security item associated with the asset database with the specified name. |
| [**assetDatabaseGetTableCategories**](AssetDatabaseApi.md#assetDatabaseGetTableCategories) | **GET** /assetdatabases/{webId}/tablecategories | Retrieve table categories for a given Asset Database. |
| [**assetDatabaseGetTables**](AssetDatabaseApi.md#assetDatabaseGetTables) | **GET** /assetdatabases/{webId}/tables | Retrieve tables for given Asset Database. |
| [**assetDatabaseImport**](AssetDatabaseApi.md#assetDatabaseImport) | **POST** /assetdatabases/{webId}/import | Import an asset database. |
| [**assetDatabaseRemoveReferencedElement**](AssetDatabaseApi.md#assetDatabaseRemoveReferencedElement) | **DELETE** /assetdatabases/{webId}/referencedelements | Remove a reference to an existing element from the specified database. |
| [**assetDatabaseUpdate**](AssetDatabaseApi.md#assetDatabaseUpdate) | **PATCH** /assetdatabases/{webId} | Update an asset database by replacing items in its definition. |
| [**assetDatabaseUpdateSecurityEntry**](AssetDatabaseApi.md#assetDatabaseUpdateSecurityEntry) | **PUT** /assetdatabases/{webId}/securityentries/{name} | Update a security entry owned by the asset database. |


<a id="assetDatabaseAddReferencedElement"></a>
# **assetDatabaseAddReferencedElement**
> assetDatabaseAddReferencedElement(webId, referencedElementWebId, referenceType)

Add a reference to an existing element to the specified database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetDatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AssetDatabaseApi apiInstance = new AssetDatabaseApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the database which the referenced element will be added to.
    List<String> referencedElementWebId = Arrays.asList(); // List<String> | The ID of the referenced element. Multiple referenced elements may be specified with multiple instances of the parameter.
    String referenceType = "referenceType_example"; // String | The name of the reference type between the parent and the referenced element. This must be a \"strong\" reference type. The default is \"parent-child\".
    try {
      apiInstance.assetDatabaseAddReferencedElement(webId, referencedElementWebId, referenceType);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetDatabaseApi#assetDatabaseAddReferencedElement");
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
| **webId** | **String**| The ID of the database which the referenced element will be added to. | |
| **referencedElementWebId** | [**List&lt;String&gt;**](String.md)| The ID of the referenced element. Multiple referenced elements may be specified with multiple instances of the parameter. | |
| **referenceType** | **String**| The name of the reference type between the parent and the referenced element. This must be a \&quot;strong\&quot; reference type. The default is \&quot;parent-child\&quot;. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The referenced element was successfully added. |  -  |
| **409** | The referenced element already exists in the collection. |  -  |

<a id="assetDatabaseCreateAnalysisCategory"></a>
# **assetDatabaseCreateAnalysisCategory**
> assetDatabaseCreateAnalysisCategory(webId, analysisCategory, webIdType)

Create an analysis category at the Asset Database root.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetDatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AssetDatabaseApi apiInstance = new AssetDatabaseApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the database in which to create the analysis category.
    AnalysisCategory analysisCategory = new AnalysisCategory(); // AnalysisCategory | The new analysis category definition.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      apiInstance.assetDatabaseCreateAnalysisCategory(webId, analysisCategory, webIdType);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetDatabaseApi#assetDatabaseCreateAnalysisCategory");
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
| **webId** | **String**| The ID of the database in which to create the analysis category. | |
| **analysisCategory** | [**AnalysisCategory**](AnalysisCategory.md)| The new analysis category definition. | |
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
| **201** | The analysis category was created. The response&#39;s Location header is a link to the analysis category. |  -  |

<a id="assetDatabaseCreateAnalysisTemplate"></a>
# **assetDatabaseCreateAnalysisTemplate**
> assetDatabaseCreateAnalysisTemplate(webId, template, webIdType)

Create an analysis template at the Asset Database root.

Analyses that are based on an analysis template will inherit characteristics defined in the template.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetDatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AssetDatabaseApi apiInstance = new AssetDatabaseApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the database in which to create the analysis template.
    AnalysisTemplate template = new AnalysisTemplate(); // AnalysisTemplate | The new analysis template definition.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      apiInstance.assetDatabaseCreateAnalysisTemplate(webId, template, webIdType);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetDatabaseApi#assetDatabaseCreateAnalysisTemplate");
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
| **webId** | **String**| The ID of the database in which to create the analysis template. | |
| **template** | [**AnalysisTemplate**](AnalysisTemplate.md)| The new analysis template definition. | |
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
| **201** | The analysis template was created. The response&#39;s Location header is a link to the created template. |  -  |

<a id="assetDatabaseCreateAttributeCategory"></a>
# **assetDatabaseCreateAttributeCategory**
> assetDatabaseCreateAttributeCategory(webId, attributeCategory, webIdType)

Create an attribute category at the Asset Database root.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetDatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AssetDatabaseApi apiInstance = new AssetDatabaseApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the database in which to create the attribute category.
    AttributeCategory attributeCategory = new AttributeCategory(); // AttributeCategory | The new attribute category definition.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      apiInstance.assetDatabaseCreateAttributeCategory(webId, attributeCategory, webIdType);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetDatabaseApi#assetDatabaseCreateAttributeCategory");
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
| **webId** | **String**| The ID of the database in which to create the attribute category. | |
| **attributeCategory** | [**AttributeCategory**](AttributeCategory.md)| The new attribute category definition. | |
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
| **201** | The attribute category was created. The response&#39;s Location header is a link to the attribute category. |  -  |

<a id="assetDatabaseCreateElement"></a>
# **assetDatabaseCreateElement**
> assetDatabaseCreateElement(webId, element, webIdType)

Create a child element.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetDatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AssetDatabaseApi apiInstance = new AssetDatabaseApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the asset database on which to create the element.
    Element element = new Element(); // Element | The new element definition.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      apiInstance.assetDatabaseCreateElement(webId, element, webIdType);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetDatabaseApi#assetDatabaseCreateElement");
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
| **webId** | **String**| The ID of the asset database on which to create the element. | |
| **element** | [**Element**](Element.md)| The new element definition. | |
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
| **201** | The element was created. The response&#39;s Location header is a link to the element. |  -  |

<a id="assetDatabaseCreateElementCategory"></a>
# **assetDatabaseCreateElementCategory**
> assetDatabaseCreateElementCategory(webId, elementCategory, webIdType)

Create an element category at the Asset Database root.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetDatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AssetDatabaseApi apiInstance = new AssetDatabaseApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the database in which to create the element category.
    ElementCategory elementCategory = new ElementCategory(); // ElementCategory | The new element category definition.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      apiInstance.assetDatabaseCreateElementCategory(webId, elementCategory, webIdType);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetDatabaseApi#assetDatabaseCreateElementCategory");
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
| **webId** | **String**| The ID of the database in which to create the element category. | |
| **elementCategory** | [**ElementCategory**](ElementCategory.md)| The new element category definition. | |
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
| **201** | The element category was created. The response&#39;s Location header is a link to the element category. |  -  |

<a id="assetDatabaseCreateElementTemplate"></a>
# **assetDatabaseCreateElementTemplate**
> assetDatabaseCreateElementTemplate(webId, template, webIdType)

Create a template at the Asset Database root. Specify InstanceType of \&quot;Element\&quot; or \&quot;EventFrame\&quot; to create element or event frame template respectively. Only these two types of templates can be created.

Elements and event frames that are based on an element template will inherit characteristics defined in the template.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetDatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AssetDatabaseApi apiInstance = new AssetDatabaseApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the database in which to create the element template.
    ElementTemplate template = new ElementTemplate(); // ElementTemplate | The new element template definition.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      apiInstance.assetDatabaseCreateElementTemplate(webId, template, webIdType);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetDatabaseApi#assetDatabaseCreateElementTemplate");
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
| **webId** | **String**| The ID of the database in which to create the element template. | |
| **template** | [**ElementTemplate**](ElementTemplate.md)| The new element template definition. | |
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
| **201** | The element template was created. The response&#39;s Location header is a link to the created template. |  -  |

<a id="assetDatabaseCreateEnumerationSet"></a>
# **assetDatabaseCreateEnumerationSet**
> assetDatabaseCreateEnumerationSet(webId, enumerationSet, webIdType)

Create an enumeration set at the Asset Database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetDatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AssetDatabaseApi apiInstance = new AssetDatabaseApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the database in which to create the enumeration set.
    EnumerationSet enumerationSet = new EnumerationSet(); // EnumerationSet | The new enumeration set definition.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      apiInstance.assetDatabaseCreateEnumerationSet(webId, enumerationSet, webIdType);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetDatabaseApi#assetDatabaseCreateEnumerationSet");
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
| **webId** | **String**| The ID of the database in which to create the enumeration set. | |
| **enumerationSet** | [**EnumerationSet**](EnumerationSet.md)| The new enumeration set definition. | |
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
| **201** | The enumeration set was created. The response&#39;s Location header is a link to the created enumeration set. |  -  |

<a id="assetDatabaseCreateEventFrame"></a>
# **assetDatabaseCreateEventFrame**
> assetDatabaseCreateEventFrame(webId, eventFrame, webIdType)

Create an event frame.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetDatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AssetDatabaseApi apiInstance = new AssetDatabaseApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the database on which to create the event frame.
    EventFrame eventFrame = new EventFrame(); // EventFrame | The new event frame definition.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      apiInstance.assetDatabaseCreateEventFrame(webId, eventFrame, webIdType);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetDatabaseApi#assetDatabaseCreateEventFrame");
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
| **webId** | **String**| The ID of the database on which to create the event frame. | |
| **eventFrame** | [**EventFrame**](EventFrame.md)| The new event frame definition. | |
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
| **201** | The event frame was created. The response&#39;s Location header is a link to the event frame. |  -  |

<a id="assetDatabaseCreateSecurityEntry"></a>
# **assetDatabaseCreateSecurityEntry**
> assetDatabaseCreateSecurityEntry(webId, securityEntry, applyToChildren, securityItem, webIdType)

Create a security entry owned by the asset database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetDatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AssetDatabaseApi apiInstance = new AssetDatabaseApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the asset database where the security entry will be created.
    SecurityEntry securityEntry = new SecurityEntry(); // SecurityEntry | The new security entry definition. The full list of allow and deny rights must be supplied.
    Boolean applyToChildren = true; // Boolean | If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.
    String securityItem = "securityItem_example"; // String | The security item of the desired security entries to be created. If the parameter is not specified, security entries of the 'Default' security item will be created.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      apiInstance.assetDatabaseCreateSecurityEntry(webId, securityEntry, applyToChildren, securityItem, webIdType);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetDatabaseApi#assetDatabaseCreateSecurityEntry");
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
| **webId** | **String**| The ID of the asset database where the security entry will be created. | |
| **securityEntry** | [**SecurityEntry**](SecurityEntry.md)| The new security entry definition. The full list of allow and deny rights must be supplied. | |
| **applyToChildren** | **Boolean**| If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change. | [optional] |
| **securityItem** | **String**| The security item of the desired security entries to be created. If the parameter is not specified, security entries of the &#39;Default&#39; security item will be created. | [optional] |
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
| **201** | The security entry was created. The response&#39;s Location header is a link to the security entry. |  -  |

<a id="assetDatabaseCreateTable"></a>
# **assetDatabaseCreateTable**
> assetDatabaseCreateTable(webId, table, webIdType)

Create a table on the Asset Database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetDatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AssetDatabaseApi apiInstance = new AssetDatabaseApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the database in which to create the table.
    Table table = new Table(); // Table | The new table definition.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      apiInstance.assetDatabaseCreateTable(webId, table, webIdType);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetDatabaseApi#assetDatabaseCreateTable");
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
| **webId** | **String**| The ID of the database in which to create the table. | |
| **table** | [**Table**](Table.md)| The new table definition. | |
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
| **201** | The table was created. The response&#39;s Location header is a link to the created table. |  -  |

<a id="assetDatabaseCreateTableCategory"></a>
# **assetDatabaseCreateTableCategory**
> assetDatabaseCreateTableCategory(webId, tableCategory, webIdType)

Create a table category on the Asset Database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetDatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AssetDatabaseApi apiInstance = new AssetDatabaseApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the database in which to create the table category.
    TableCategory tableCategory = new TableCategory(); // TableCategory | The new table category definition.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      apiInstance.assetDatabaseCreateTableCategory(webId, tableCategory, webIdType);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetDatabaseApi#assetDatabaseCreateTableCategory");
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
| **webId** | **String**| The ID of the database in which to create the table category. | |
| **tableCategory** | [**TableCategory**](TableCategory.md)| The new table category definition. | |
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
| **201** | The table category was created. The response&#39;s Location header is a link to the table category. |  -  |

<a id="assetDatabaseDelete"></a>
# **assetDatabaseDelete**
> assetDatabaseDelete(webId)

Delete an asset database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetDatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AssetDatabaseApi apiInstance = new AssetDatabaseApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the database.
    try {
      apiInstance.assetDatabaseDelete(webId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetDatabaseApi#assetDatabaseDelete");
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
| **webId** | **String**| The ID of the database. | |

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
| **204** | The database was deleted. |  -  |

<a id="assetDatabaseDeleteSecurityEntry"></a>
# **assetDatabaseDeleteSecurityEntry**
> assetDatabaseDeleteSecurityEntry(name, webId, applyToChildren, securityItem)

Delete a security entry owned by the asset database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetDatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AssetDatabaseApi apiInstance = new AssetDatabaseApi(defaultClient);
    String name = "name_example"; // String | The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username.
    String webId = "webId_example"; // String | The ID of the asset database where the security entry will be deleted.
    Boolean applyToChildren = true; // Boolean | If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.
    String securityItem = "securityItem_example"; // String | The security item of the desired security entries to be deleted. If the parameter is not specified, security entries of the 'Default' security item will be deleted.
    try {
      apiInstance.assetDatabaseDeleteSecurityEntry(name, webId, applyToChildren, securityItem);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetDatabaseApi#assetDatabaseDeleteSecurityEntry");
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
| **name** | **String**| The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username. | |
| **webId** | **String**| The ID of the asset database where the security entry will be deleted. | |
| **applyToChildren** | **Boolean**| If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change. | [optional] |
| **securityItem** | **String**| The security item of the desired security entries to be deleted. If the parameter is not specified, security entries of the &#39;Default&#39; security item will be deleted. | [optional] |

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
| **204** | The security entry was deleted. |  -  |

<a id="assetDatabaseExport"></a>
# **assetDatabaseExport**
> assetDatabaseExport(webId, endTime, exportMode, startTime)

Export the asset database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetDatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AssetDatabaseApi apiInstance = new AssetDatabaseApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the database.
    String endTime = "endTime_example"; // String | The latest ending time for AFEventFrame, AFTransfer, and AFCase objects that may be part of the export. The default is '*'.
    List<String> exportMode = Arrays.asList(); // List<String> | Indicates the type of export to perform. The default is 'StrongReferences'. Multiple export modes may be specified by using multiple instances of exportMode.
    String startTime = "startTime_example"; // String | The earliest starting time for AFEventFrame, AFTransfer, and AFCase objects that may be part of the export. The default is '*-30d'.
    try {
      apiInstance.assetDatabaseExport(webId, endTime, exportMode, startTime);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetDatabaseApi#assetDatabaseExport");
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
| **webId** | **String**| The ID of the database. | |
| **endTime** | **String**| The latest ending time for AFEventFrame, AFTransfer, and AFCase objects that may be part of the export. The default is &#39;*&#39;. | [optional] |
| **exportMode** | [**List&lt;String&gt;**](String.md)| Indicates the type of export to perform. The default is &#39;StrongReferences&#39;. Multiple export modes may be specified by using multiple instances of exportMode. | [optional] |
| **startTime** | **String**| The earliest starting time for AFEventFrame, AFTransfer, and AFCase objects that may be part of the export. The default is &#39;*-30d&#39;. | [optional] |

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
| **200** | Database exported. The response body contains the serialized database. |  -  |

<a id="assetDatabaseFindAnalyses"></a>
# **assetDatabaseFindAnalyses**
> ItemsAnalysis assetDatabaseFindAnalyses(webId, field, maxCount, query, selectedFields, sortField, sortOrder, startIndex, webIdType)

Retrieve analyses based on the specified conditions.

Users can search for the analyses based on specific search parameters. If no parameters are specified in the search, the default values for each parameter will be used and will return the analyses that match the default search.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetDatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AssetDatabaseApi apiInstance = new AssetDatabaseApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the database to search for the analyses.
    List<String> field = Arrays.asList(); // List<String> | Specifies which of the object's properties are searched. Multiple search fields may be specified with multiple instances of the parameter. The default is 'Name'.
    Integer maxCount = 56; // Integer | The maximum number of objects to be returned per call (page size). The default is 1000.
    String query = "query_example"; // String | The query string used for finding analyses. The default is null.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String sortField = "sortField_example"; // String | The field or property of the object used to sort the returned collection. The default is 'Name'.
    String sortOrder = "sortOrder_example"; // String | The order that the returned collection is sorted. The default is 'Ascending'.
    Integer startIndex = 56; // Integer | The starting index (zero based) of the items to be returned. The default is 0.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsAnalysis result = apiInstance.assetDatabaseFindAnalyses(webId, field, maxCount, query, selectedFields, sortField, sortOrder, startIndex, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetDatabaseApi#assetDatabaseFindAnalyses");
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
| **webId** | **String**| The ID of the database to search for the analyses. | |
| **field** | [**List&lt;String&gt;**](String.md)| Specifies which of the object&#39;s properties are searched. Multiple search fields may be specified with multiple instances of the parameter. The default is &#39;Name&#39;. | |
| **maxCount** | **Integer**| The maximum number of objects to be returned per call (page size). The default is 1000. | [optional] |
| **query** | **String**| The query string used for finding analyses. The default is null. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **sortField** | **String**| The field or property of the object used to sort the returned collection. The default is &#39;Name&#39;. | [optional] |
| **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] |
| **startIndex** | **Integer**| The starting index (zero based) of the items to be returned. The default is 0. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsAnalysis**](ItemsAnalysis.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of analyses matching the specified conditions. |  -  |

<a id="assetDatabaseFindElementAttributes"></a>
# **assetDatabaseFindElementAttributes**
> ItemsAttribute assetDatabaseFindElementAttributes(webId, associations, attributeCategory, attributeDescriptionFilter, attributeNameFilter, attributeType, elementCategory, elementDescriptionFilter, elementNameFilter, elementTemplate, elementType, maxCount, searchFullHierarchy, selectedFields, sortField, sortOrder, startIndex, webIdType)

Retrieves a list of element attributes matching the specified filters from the specified asset database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetDatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AssetDatabaseApi apiInstance = new AssetDatabaseApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the asset database to use as the root of the search.
    String associations = "associations_example"; // String | Associated values to return in the response, separated by semicolons (;). This call supports DataReference to return attributes with data references. If this parameter is not specified, DataReference values are not returned.
    String attributeCategory = "attributeCategory_example"; // String | Specify that returned attributes must have this category. The default is no filter.
    String attributeDescriptionFilter = "attributeDescriptionFilter_example"; // String | The attribute description filter string used for finding objects. Only the first 440 characters of the description will be searched. For Asset Servers older than 2.7, a 400 status code (Bad Request) will be returned if this parameter is specified. The default is no filter.
    String attributeNameFilter = "attributeNameFilter_example"; // String | The attribute name filter string used for finding objects. The default is no filter.
    String attributeType = "attributeType_example"; // String | Specify that returned attributes' value type must be this value type. The default is no filter.
    String elementCategory = "elementCategory_example"; // String | Specify that the owner of the returned attributes must have this category. The default is no filter.
    String elementDescriptionFilter = "elementDescriptionFilter_example"; // String | The element description filter string used for finding objects. Only the first 440 characters of the description will be searched. For Asset Servers older than 2.7, a 400 status code (Bad Request) will be returned if this parameter is specified. The default is no filter.
    String elementNameFilter = "elementNameFilter_example"; // String | The element name filter string used for finding objects. The default is no filter.
    String elementTemplate = "elementTemplate_example"; // String | Specify that the owner of the returned attributes must have this template or a template derived from this template. The default is no filter.
    String elementType = "elementType_example"; // String | Specify that the element of the returned attributes must have this AFElementType. The default is no filter.
    Integer maxCount = 56; // Integer | The maximum number of objects to be returned (the page size). The default is 1000.
    Boolean searchFullHierarchy = true; // Boolean | Specifies if the search should include objects nested further than immediate children of the given resource. The default is 'false'.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String sortField = "sortField_example"; // String | The field or property of the object used to sort the returned collection. The default is 'Name'.
    String sortOrder = "sortOrder_example"; // String | The order that the returned collection is sorted. The default is 'Ascending'.
    Integer startIndex = 56; // Integer | The starting index (zero based) of the items to be returned. The default is 0.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsAttribute result = apiInstance.assetDatabaseFindElementAttributes(webId, associations, attributeCategory, attributeDescriptionFilter, attributeNameFilter, attributeType, elementCategory, elementDescriptionFilter, elementNameFilter, elementTemplate, elementType, maxCount, searchFullHierarchy, selectedFields, sortField, sortOrder, startIndex, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetDatabaseApi#assetDatabaseFindElementAttributes");
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
| **webId** | **String**| The ID of the asset database to use as the root of the search. | |
| **associations** | **String**| Associated values to return in the response, separated by semicolons (;). This call supports DataReference to return attributes with data references. If this parameter is not specified, DataReference values are not returned. | [optional] |
| **attributeCategory** | **String**| Specify that returned attributes must have this category. The default is no filter. | [optional] |
| **attributeDescriptionFilter** | **String**| The attribute description filter string used for finding objects. Only the first 440 characters of the description will be searched. For Asset Servers older than 2.7, a 400 status code (Bad Request) will be returned if this parameter is specified. The default is no filter. | [optional] |
| **attributeNameFilter** | **String**| The attribute name filter string used for finding objects. The default is no filter. | [optional] |
| **attributeType** | **String**| Specify that returned attributes&#39; value type must be this value type. The default is no filter. | [optional] |
| **elementCategory** | **String**| Specify that the owner of the returned attributes must have this category. The default is no filter. | [optional] |
| **elementDescriptionFilter** | **String**| The element description filter string used for finding objects. Only the first 440 characters of the description will be searched. For Asset Servers older than 2.7, a 400 status code (Bad Request) will be returned if this parameter is specified. The default is no filter. | [optional] |
| **elementNameFilter** | **String**| The element name filter string used for finding objects. The default is no filter. | [optional] |
| **elementTemplate** | **String**| Specify that the owner of the returned attributes must have this template or a template derived from this template. The default is no filter. | [optional] |
| **elementType** | **String**| Specify that the element of the returned attributes must have this AFElementType. The default is no filter. | [optional] |
| **maxCount** | **Integer**| The maximum number of objects to be returned (the page size). The default is 1000. | [optional] |
| **searchFullHierarchy** | **Boolean**| Specifies if the search should include objects nested further than immediate children of the given resource. The default is &#39;false&#39;. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **sortField** | **String**| The field or property of the object used to sort the returned collection. The default is &#39;Name&#39;. | [optional] |
| **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] |
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
| **200** | a list of matching attributes. |  -  |

<a id="assetDatabaseFindEventFrameAttributes"></a>
# **assetDatabaseFindEventFrameAttributes**
> ItemsAttribute assetDatabaseFindEventFrameAttributes(webId, associations, attributeCategory, attributeDescriptionFilter, attributeNameFilter, attributeType, endTime, eventFrameCategory, eventFrameDescriptionFilter, eventFrameNameFilter, eventFrameTemplate, maxCount, referencedElementNameFilter, searchFullHierarchy, searchMode, selectedFields, sortField, sortOrder, startIndex, startTime, webIdType)

Retrieves a list of event frame attributes matching the specified filters from the specified asset database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetDatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AssetDatabaseApi apiInstance = new AssetDatabaseApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the asset database to use as the root of the search.
    String associations = "associations_example"; // String | Associated values to return in the response, separated by semicolons (;). This call supports DataReference to return attributes with data references. If this parameter is not specified, DataReference values are not returned.
    String attributeCategory = "attributeCategory_example"; // String | Specify that returned attributes must have this category. The default is no filter.
    String attributeDescriptionFilter = "attributeDescriptionFilter_example"; // String | The attribute description filter string used for finding objects. Only the first 440 characters of the description will be searched. For Asset Servers older than 2.7, a 400 status code (Bad Request) will be returned if this parameter is specified. The default is no filter.
    String attributeNameFilter = "attributeNameFilter_example"; // String | The attribute name filter string used for finding objects. The default is no filter.
    String attributeType = "attributeType_example"; // String | Specify that returned attributes' value type must be this value type. The default is no filter.
    String endTime = "endTime_example"; // String | A string representing the latest ending time for the event frames to be matched. The endTime must be greater than or equal to the startTime. The default is '*'.
    String eventFrameCategory = "eventFrameCategory_example"; // String | Specify that the owner of the returned attributes must have this category. The default is no filter.
    String eventFrameDescriptionFilter = "eventFrameDescriptionFilter_example"; // String | The event frame description filter string used for finding objects. Only the first 440 characters of the description will be searched. For Asset Servers older than 2.7, a 400 status code (Bad Request) will be returned if this parameter is specified. The default is no filter.
    String eventFrameNameFilter = "eventFrameNameFilter_example"; // String | The event frame name filter string used for finding objects. The default is no filter.
    String eventFrameTemplate = "eventFrameTemplate_example"; // String | Specify that the owner of the returned attributes must have this template or a template derived from this template. The default is no filter.
    Integer maxCount = 56; // Integer | The maximum number of objects to be returned (the page size). The default is 1000.
    String referencedElementNameFilter = "referencedElementNameFilter_example"; // String | The name query string which must match the name of a referenced element. The default is no filter.
    Boolean searchFullHierarchy = true; // Boolean | Specifies if the search should include objects nested further than immediate children of the given resource. The default is 'false'.
    String searchMode = "searchMode_example"; // String | Determines how the startTime and endTime parameters are treated when searching for event frames. The default is 'Overlapped'.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String sortField = "sortField_example"; // String | The field or property of the object used to sort the returned collection. The default is 'Name'.
    String sortOrder = "sortOrder_example"; // String | The order that the returned collection is sorted. The default is 'Ascending'.
    Integer startIndex = 56; // Integer | The starting index (zero based) of the items to be returned. The default is 0.
    String startTime = "startTime_example"; // String | A string representing the earliest starting time for the event frames to be matched. startTime must be less than or equal to the endTime. The default is '*-8h'.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsAttribute result = apiInstance.assetDatabaseFindEventFrameAttributes(webId, associations, attributeCategory, attributeDescriptionFilter, attributeNameFilter, attributeType, endTime, eventFrameCategory, eventFrameDescriptionFilter, eventFrameNameFilter, eventFrameTemplate, maxCount, referencedElementNameFilter, searchFullHierarchy, searchMode, selectedFields, sortField, sortOrder, startIndex, startTime, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetDatabaseApi#assetDatabaseFindEventFrameAttributes");
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
| **webId** | **String**| The ID of the asset database to use as the root of the search. | |
| **associations** | **String**| Associated values to return in the response, separated by semicolons (;). This call supports DataReference to return attributes with data references. If this parameter is not specified, DataReference values are not returned. | [optional] |
| **attributeCategory** | **String**| Specify that returned attributes must have this category. The default is no filter. | [optional] |
| **attributeDescriptionFilter** | **String**| The attribute description filter string used for finding objects. Only the first 440 characters of the description will be searched. For Asset Servers older than 2.7, a 400 status code (Bad Request) will be returned if this parameter is specified. The default is no filter. | [optional] |
| **attributeNameFilter** | **String**| The attribute name filter string used for finding objects. The default is no filter. | [optional] |
| **attributeType** | **String**| Specify that returned attributes&#39; value type must be this value type. The default is no filter. | [optional] |
| **endTime** | **String**| A string representing the latest ending time for the event frames to be matched. The endTime must be greater than or equal to the startTime. The default is &#39;*&#39;. | [optional] |
| **eventFrameCategory** | **String**| Specify that the owner of the returned attributes must have this category. The default is no filter. | [optional] |
| **eventFrameDescriptionFilter** | **String**| The event frame description filter string used for finding objects. Only the first 440 characters of the description will be searched. For Asset Servers older than 2.7, a 400 status code (Bad Request) will be returned if this parameter is specified. The default is no filter. | [optional] |
| **eventFrameNameFilter** | **String**| The event frame name filter string used for finding objects. The default is no filter. | [optional] |
| **eventFrameTemplate** | **String**| Specify that the owner of the returned attributes must have this template or a template derived from this template. The default is no filter. | [optional] |
| **maxCount** | **Integer**| The maximum number of objects to be returned (the page size). The default is 1000. | [optional] |
| **referencedElementNameFilter** | **String**| The name query string which must match the name of a referenced element. The default is no filter. | [optional] |
| **searchFullHierarchy** | **Boolean**| Specifies if the search should include objects nested further than immediate children of the given resource. The default is &#39;false&#39;. | [optional] |
| **searchMode** | **String**| Determines how the startTime and endTime parameters are treated when searching for event frames. The default is &#39;Overlapped&#39;. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **sortField** | **String**| The field or property of the object used to sort the returned collection. The default is &#39;Name&#39;. | [optional] |
| **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] |
| **startIndex** | **Integer**| The starting index (zero based) of the items to be returned. The default is 0. | [optional] |
| **startTime** | **String**| A string representing the earliest starting time for the event frames to be matched. startTime must be less than or equal to the endTime. The default is &#39;*-8h&#39;. | [optional] |
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
| **200** | a list of matching attributes. |  -  |

<a id="assetDatabaseGet"></a>
# **assetDatabaseGet**
> AssetDatabase assetDatabaseGet(webId, selectedFields, webIdType)

Retrieve an Asset Database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetDatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AssetDatabaseApi apiInstance = new AssetDatabaseApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the database.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      AssetDatabase result = apiInstance.assetDatabaseGet(webId, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetDatabaseApi#assetDatabaseGet");
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
| **webId** | **String**| The ID of the database. | |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**AssetDatabase**](AssetDatabase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The specified database. |  -  |

<a id="assetDatabaseGetAnalysisCategories"></a>
# **assetDatabaseGetAnalysisCategories**
> ItemsAnalysisCategory assetDatabaseGetAnalysisCategories(webId, selectedFields, webIdType)

Retrieve analysis categories for a given Asset Database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetDatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AssetDatabaseApi apiInstance = new AssetDatabaseApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the database.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsAnalysisCategory result = apiInstance.assetDatabaseGetAnalysisCategories(webId, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetDatabaseApi#assetDatabaseGetAnalysisCategories");
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
| **webId** | **String**| The ID of the database. | |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsAnalysisCategory**](ItemsAnalysisCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The analysis categories that exist in the database. |  -  |

<a id="assetDatabaseGetAnalysisTemplates"></a>
# **assetDatabaseGetAnalysisTemplates**
> ItemsAnalysisTemplate assetDatabaseGetAnalysisTemplates(webId, field, maxCount, query, selectedFields, sortField, sortOrder, webIdType)

Retrieve analysis templates based on the specified criteria. By default, all analysis templates in the specified Asset Database are returned.

Users can search for the analysis templates based on specific search parameters. If no parameters are specified in the search, the default values for each parameter will be used and will return the templates that match the default search.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetDatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AssetDatabaseApi apiInstance = new AssetDatabaseApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the database to search.
    List<String> field = Arrays.asList(); // List<String> | Specifies which of the object's properties are searched. Multiple search fields may be specified with multiple instances of the parameter. The default is 'Name'.
    Integer maxCount = 56; // Integer | The maximum number of objects to be returned per call (page size). The default is 1000.
    String query = "query_example"; // String | The query string used for finding objects. The default is no query string.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String sortField = "sortField_example"; // String | The field or property of the object used to sort the returned collection. The default is 'Name'.
    String sortOrder = "sortOrder_example"; // String | The order that the returned collection is sorted. The default is 'Ascending'.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsAnalysisTemplate result = apiInstance.assetDatabaseGetAnalysisTemplates(webId, field, maxCount, query, selectedFields, sortField, sortOrder, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetDatabaseApi#assetDatabaseGetAnalysisTemplates");
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
| **webId** | **String**| The ID of the database to search. | |
| **field** | [**List&lt;String&gt;**](String.md)| Specifies which of the object&#39;s properties are searched. Multiple search fields may be specified with multiple instances of the parameter. The default is &#39;Name&#39;. | |
| **maxCount** | **Integer**| The maximum number of objects to be returned per call (page size). The default is 1000. | [optional] |
| **query** | **String**| The query string used for finding objects. The default is no query string. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **sortField** | **String**| The field or property of the object used to sort the returned collection. The default is &#39;Name&#39;. | [optional] |
| **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsAnalysisTemplate**](ItemsAnalysisTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of analysis templates matching the specified condition. |  -  |

<a id="assetDatabaseGetAttributeCategories"></a>
# **assetDatabaseGetAttributeCategories**
> ItemsAttributeCategory assetDatabaseGetAttributeCategories(webId, selectedFields, webIdType)

Retrieve attribute categories for a given Asset Database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetDatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AssetDatabaseApi apiInstance = new AssetDatabaseApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the database.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsAttributeCategory result = apiInstance.assetDatabaseGetAttributeCategories(webId, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetDatabaseApi#assetDatabaseGetAttributeCategories");
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
| **webId** | **String**| The ID of the database. | |
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
| **200** | The attribute categories that exist in the database. |  -  |

<a id="assetDatabaseGetByPath"></a>
# **assetDatabaseGetByPath**
> AssetDatabase assetDatabaseGetByPath(path, selectedFields, webIdType)

Retrieve an Asset Database by path.

This method returns an asset database based on the hierarchical path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetDatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AssetDatabaseApi apiInstance = new AssetDatabaseApi(defaultClient);
    String path = "path_example"; // String | The path to the database.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      AssetDatabase result = apiInstance.assetDatabaseGetByPath(path, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetDatabaseApi#assetDatabaseGetByPath");
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
| **path** | **String**| The path to the database. | |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**AssetDatabase**](AssetDatabase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The specified database. |  -  |

<a id="assetDatabaseGetElementCategories"></a>
# **assetDatabaseGetElementCategories**
> ItemsElementCategory assetDatabaseGetElementCategories(webId, selectedFields, webIdType)

Retrieve element categories for a given Asset Database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetDatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AssetDatabaseApi apiInstance = new AssetDatabaseApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the database.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsElementCategory result = apiInstance.assetDatabaseGetElementCategories(webId, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetDatabaseApi#assetDatabaseGetElementCategories");
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
| **webId** | **String**| The ID of the database. | |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsElementCategory**](ItemsElementCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The element categories that exist in the database. |  -  |

<a id="assetDatabaseGetElementTemplates"></a>
# **assetDatabaseGetElementTemplates**
> ItemsElementTemplate assetDatabaseGetElementTemplates(webId, field, maxCount, query, selectedFields, sortField, sortOrder, webIdType)

Retrieve element templates based on the specified criteria. Only templates of instance type \&quot;Element\&quot; and \&quot;EventFrame\&quot; are returned. By default, all element and event frame templates in the specified Asset Database are returned.

Users can search for the element and event frame template based on specific search parameters. If no parameters are specified in the search, the default values for each parameter will be used and will return the templates that match the default search.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetDatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AssetDatabaseApi apiInstance = new AssetDatabaseApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the database to search.
    List<String> field = Arrays.asList(); // List<String> | Specifies which of the object's properties are searched. Multiple search fields may be specified with multiple instances of the parameter. The default is 'Name'.
    Integer maxCount = 56; // Integer | The maximum number of objects to be returned per call (page size). The default is 1000.
    String query = "query_example"; // String | The query string used for finding objects. The default is no query string.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String sortField = "sortField_example"; // String | The field or property of the object used to sort the returned collection. The default is 'Name'.
    String sortOrder = "sortOrder_example"; // String | The order that the returned collection is sorted. The default is 'Ascending'.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsElementTemplate result = apiInstance.assetDatabaseGetElementTemplates(webId, field, maxCount, query, selectedFields, sortField, sortOrder, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetDatabaseApi#assetDatabaseGetElementTemplates");
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
| **webId** | **String**| The ID of the database to search. | |
| **field** | [**List&lt;String&gt;**](String.md)| Specifies which of the object&#39;s properties are searched. Multiple search fields may be specified with multiple instances of the parameter. The default is &#39;Name&#39;. | |
| **maxCount** | **Integer**| The maximum number of objects to be returned per call (page size). The default is 1000. | [optional] |
| **query** | **String**| The query string used for finding objects. The default is no query string. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **sortField** | **String**| The field or property of the object used to sort the returned collection. The default is &#39;Name&#39;. | [optional] |
| **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsElementTemplate**](ItemsElementTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of element templates matching the specified condition. |  -  |

<a id="assetDatabaseGetElements"></a>
# **assetDatabaseGetElements**
> ItemsElement assetDatabaseGetElements(webId, associations, categoryName, descriptionFilter, elementType, maxCount, nameFilter, searchFullHierarchy, selectedFields, sortField, sortOrder, startIndex, templateName, webIdType)

Retrieve elements based on the specified conditions. By default, this method selects immediate children of the specified asset database.

Users can search for the elements based on specific search parameters. If no parameters are specified in the search, the default values for each parameter will be used and will return the elements that match the default search.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetDatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AssetDatabaseApi apiInstance = new AssetDatabaseApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the database to use as the root of the search.
    String associations = "associations_example"; // String | Associated values to return in the response, separated by semicolons (;). This call supports Paths to return all paths to the element. If this parameter is not specified, paths are not returned.
    String categoryName = "categoryName_example"; // String | Specify that returned elements must have this category. The default is no category filter.
    String descriptionFilter = "descriptionFilter_example"; // String | Specify that returned elements must have this description. The default is no description filter.
    String elementType = "elementType_example"; // String | Specify that returned elements must have this type. The default type is 'Any'.
    Integer maxCount = 56; // Integer | The maximum number of objects to be returned per call (page size). The default is 1000.
    String nameFilter = "nameFilter_example"; // String | The name query string used for finding objects. The default is no filter.
    Boolean searchFullHierarchy = true; // Boolean | Specifies if the search should include objects nested further than the immediate children of the searchRoot. The default is 'false'.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String sortField = "sortField_example"; // String | The field or property of the object used to sort the returned collection. The default is 'Name'.
    String sortOrder = "sortOrder_example"; // String | The order that the returned collection is sorted. The default is 'Ascending'.
    Integer startIndex = 56; // Integer | The starting index (zero based) of the items to be returned. The default is 0.
    String templateName = "templateName_example"; // String | Specify that returned elements must have this template or a template derived from this template. The default is no template filter.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsElement result = apiInstance.assetDatabaseGetElements(webId, associations, categoryName, descriptionFilter, elementType, maxCount, nameFilter, searchFullHierarchy, selectedFields, sortField, sortOrder, startIndex, templateName, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetDatabaseApi#assetDatabaseGetElements");
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
| **webId** | **String**| The ID of the database to use as the root of the search. | |
| **associations** | **String**| Associated values to return in the response, separated by semicolons (;). This call supports Paths to return all paths to the element. If this parameter is not specified, paths are not returned. | [optional] |
| **categoryName** | **String**| Specify that returned elements must have this category. The default is no category filter. | [optional] |
| **descriptionFilter** | **String**| Specify that returned elements must have this description. The default is no description filter. | [optional] |
| **elementType** | **String**| Specify that returned elements must have this type. The default type is &#39;Any&#39;. | [optional] |
| **maxCount** | **Integer**| The maximum number of objects to be returned per call (page size). The default is 1000. | [optional] |
| **nameFilter** | **String**| The name query string used for finding objects. The default is no filter. | [optional] |
| **searchFullHierarchy** | **Boolean**| Specifies if the search should include objects nested further than the immediate children of the searchRoot. The default is &#39;false&#39;. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **sortField** | **String**| The field or property of the object used to sort the returned collection. The default is &#39;Name&#39;. | [optional] |
| **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] |
| **startIndex** | **Integer**| The starting index (zero based) of the items to be returned. The default is 0. | [optional] |
| **templateName** | **String**| Specify that returned elements must have this template or a template derived from this template. The default is no template filter. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsElement**](ItemsElement.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of elements matching the specified conditions. |  -  |

<a id="assetDatabaseGetEnumerationSets"></a>
# **assetDatabaseGetEnumerationSets**
> ItemsEnumerationSet assetDatabaseGetEnumerationSets(webId, selectedFields, webIdType)

Retrieve enumeration sets for given asset database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetDatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AssetDatabaseApi apiInstance = new AssetDatabaseApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the database.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsEnumerationSet result = apiInstance.assetDatabaseGetEnumerationSets(webId, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetDatabaseApi#assetDatabaseGetEnumerationSets");
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
| **webId** | **String**| The ID of the database. | |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsEnumerationSet**](ItemsEnumerationSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The specified enumeration sets. |  -  |

<a id="assetDatabaseGetEventFrames"></a>
# **assetDatabaseGetEventFrames**
> ItemsEventFrame assetDatabaseGetEventFrames(webId, canBeAcknowledged, categoryName, endTime, isAcknowledged, maxCount, nameFilter, referencedElementNameFilter, referencedElementTemplateName, searchFullHierarchy, searchMode, selectedFields, severity, sortField, sortOrder, startIndex, startTime, templateName, webIdType)

Retrieve event frames based on the specified conditions. By default, returns all children of the specified root resource that have been active in the past 8 hours.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetDatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AssetDatabaseApi apiInstance = new AssetDatabaseApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the asset database to use as the root of the search.
    Boolean canBeAcknowledged = true; // Boolean | Specify the returned event frames' canBeAcknowledged property. The default is no canBeAcknowledged filter.
    String categoryName = "categoryName_example"; // String | Specify that returned event frames must have this category. The default is no category filter.
    String endTime = "endTime_example"; // String | The ending time for the search. The endTime must be greater than or equal to the startTime. The searchMode parameter will control whether the comparison will be performed against the event frame's startTime or endTime. The default is '*' if searchMode is not one of the 'Backward*' or 'Forward*' values.
    Boolean isAcknowledged = true; // Boolean | Specify the returned event frames' isAcknowledged property. The default no isAcknowledged filter.
    Integer maxCount = 56; // Integer | The maximum number of objects to be returned per call (page size). The default is 1000.
    String nameFilter = "nameFilter_example"; // String | The name query string used for finding event frames. The default is no filter.
    String referencedElementNameFilter = "referencedElementNameFilter_example"; // String | The name query string which must match the name of a referenced element. The default is no filter.
    String referencedElementTemplateName = "referencedElementTemplateName_example"; // String | Specify that returned event frames must have an element in the event frame's referenced elements collection that derives from the template. Specify this parameter by name.
    Boolean searchFullHierarchy = true; // Boolean | Specifies whether the search should include objects nested further than the immediate children of the search root. The default is 'false'.
    String searchMode = "searchMode_example"; // String | Determines how the startTime and endTime parameters are treated when searching for event frame objects to be included in the returned collection. If this parameter is one of the 'Backward*' or 'Forward*' values, none of endTime, sortField, or sortOrder may be specified. The default is 'Overlapped'.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    List<String> severity = Arrays.asList(); // List<String> | Specify that returned event frames must have this severity. Multiple severity values may be specified with multiple instances of the parameter. The default is no severity filter.
    String sortField = "sortField_example"; // String | The field or property of the object used to sort the returned collection. The default is 'Name' if searchMode is not one of the 'Backward*' or 'Forward*' values.
    String sortOrder = "sortOrder_example"; // String | The order that the returned collection is sorted. The default is 'Ascending' if searchMode is not one of the 'Backward*' or 'Forward*' values.
    Integer startIndex = 56; // Integer | The starting index (zero based) of the items to be returned. The default is 0.
    String startTime = "startTime_example"; // String | The starting time for the search. startTime must be less than or equal to the endTime. The searchMode parameter will control whether the comparison will be performed against the event frame's startTime or endTime. The default is '*-8h'.
    String templateName = "templateName_example"; // String | Specify that returned event frames must have this template or a template derived from this template. The default is no template filter. Specify this parameter by name.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsEventFrame result = apiInstance.assetDatabaseGetEventFrames(webId, canBeAcknowledged, categoryName, endTime, isAcknowledged, maxCount, nameFilter, referencedElementNameFilter, referencedElementTemplateName, searchFullHierarchy, searchMode, selectedFields, severity, sortField, sortOrder, startIndex, startTime, templateName, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetDatabaseApi#assetDatabaseGetEventFrames");
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
| **webId** | **String**| The ID of the asset database to use as the root of the search. | |
| **canBeAcknowledged** | **Boolean**| Specify the returned event frames&#39; canBeAcknowledged property. The default is no canBeAcknowledged filter. | [optional] |
| **categoryName** | **String**| Specify that returned event frames must have this category. The default is no category filter. | [optional] |
| **endTime** | **String**| The ending time for the search. The endTime must be greater than or equal to the startTime. The searchMode parameter will control whether the comparison will be performed against the event frame&#39;s startTime or endTime. The default is &#39;*&#39; if searchMode is not one of the &#39;Backward*&#39; or &#39;Forward*&#39; values. | [optional] |
| **isAcknowledged** | **Boolean**| Specify the returned event frames&#39; isAcknowledged property. The default no isAcknowledged filter. | [optional] |
| **maxCount** | **Integer**| The maximum number of objects to be returned per call (page size). The default is 1000. | [optional] |
| **nameFilter** | **String**| The name query string used for finding event frames. The default is no filter. | [optional] |
| **referencedElementNameFilter** | **String**| The name query string which must match the name of a referenced element. The default is no filter. | [optional] |
| **referencedElementTemplateName** | **String**| Specify that returned event frames must have an element in the event frame&#39;s referenced elements collection that derives from the template. Specify this parameter by name. | [optional] |
| **searchFullHierarchy** | **Boolean**| Specifies whether the search should include objects nested further than the immediate children of the search root. The default is &#39;false&#39;. | [optional] |
| **searchMode** | **String**| Determines how the startTime and endTime parameters are treated when searching for event frame objects to be included in the returned collection. If this parameter is one of the &#39;Backward*&#39; or &#39;Forward*&#39; values, none of endTime, sortField, or sortOrder may be specified. The default is &#39;Overlapped&#39;. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **severity** | [**List&lt;String&gt;**](String.md)| Specify that returned event frames must have this severity. Multiple severity values may be specified with multiple instances of the parameter. The default is no severity filter. | [optional] |
| **sortField** | **String**| The field or property of the object used to sort the returned collection. The default is &#39;Name&#39; if searchMode is not one of the &#39;Backward*&#39; or &#39;Forward*&#39; values. | [optional] |
| **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39; if searchMode is not one of the &#39;Backward*&#39; or &#39;Forward*&#39; values. | [optional] |
| **startIndex** | **Integer**| The starting index (zero based) of the items to be returned. The default is 0. | [optional] |
| **startTime** | **String**| The starting time for the search. startTime must be less than or equal to the endTime. The searchMode parameter will control whether the comparison will be performed against the event frame&#39;s startTime or endTime. The default is &#39;*-8h&#39;. | [optional] |
| **templateName** | **String**| Specify that returned event frames must have this template or a template derived from this template. The default is no template filter. Specify this parameter by name. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsEventFrame**](ItemsEventFrame.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of event frames matching the specified conditions. |  -  |

<a id="assetDatabaseGetReferencedElements"></a>
# **assetDatabaseGetReferencedElements**
> ItemsElement assetDatabaseGetReferencedElements(webId, associations, categoryName, descriptionFilter, elementType, maxCount, nameFilter, selectedFields, sortField, sortOrder, startIndex, templateName, webIdType)

Retrieve referenced elements based on the specified conditions. By default, this method selects all referenced elements at the root level of the asset database.

Users can search for the referenced elements based on specific search parameters. If no parameters are specified in the search, the default values for each parameter will be used and will return the elements that match the default search.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetDatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AssetDatabaseApi apiInstance = new AssetDatabaseApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the resource to use as the root of the search.
    String associations = "associations_example"; // String | Associated values to return in the response, separated by semicolons (;). This call supports Paths to return all paths to the element. If this parameter is not specified, paths are not returned.
    String categoryName = "categoryName_example"; // String | Specify that returned elements must have this category. The default is no category filter.
    String descriptionFilter = "descriptionFilter_example"; // String | Specify that returned elements must have this description. The default is no description filter.
    String elementType = "elementType_example"; // String | Specify that returned elements must have this type. The default type is 'Any'.
    Integer maxCount = 56; // Integer | The maximum number of objects to be returned per call (page size). The default is 1000.
    String nameFilter = "nameFilter_example"; // String | The name query string used for finding objects. The default is no filter.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String sortField = "sortField_example"; // String | The field or property of the object used to sort the returned collection. The default is 'Name'.
    String sortOrder = "sortOrder_example"; // String | The order that the returned collection is sorted. The default is 'Ascending'.
    Integer startIndex = 56; // Integer | The starting index (zero based) of the items to be returned. The default is 0.
    String templateName = "templateName_example"; // String | Specify that returned elements must have this template or a template derived from this template. The default is no template filter.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsElement result = apiInstance.assetDatabaseGetReferencedElements(webId, associations, categoryName, descriptionFilter, elementType, maxCount, nameFilter, selectedFields, sortField, sortOrder, startIndex, templateName, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetDatabaseApi#assetDatabaseGetReferencedElements");
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
| **webId** | **String**| The ID of the resource to use as the root of the search. | |
| **associations** | **String**| Associated values to return in the response, separated by semicolons (;). This call supports Paths to return all paths to the element. If this parameter is not specified, paths are not returned. | [optional] |
| **categoryName** | **String**| Specify that returned elements must have this category. The default is no category filter. | [optional] |
| **descriptionFilter** | **String**| Specify that returned elements must have this description. The default is no description filter. | [optional] |
| **elementType** | **String**| Specify that returned elements must have this type. The default type is &#39;Any&#39;. | [optional] |
| **maxCount** | **Integer**| The maximum number of objects to be returned per call (page size). The default is 1000. | [optional] |
| **nameFilter** | **String**| The name query string used for finding objects. The default is no filter. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **sortField** | **String**| The field or property of the object used to sort the returned collection. The default is &#39;Name&#39;. | [optional] |
| **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] |
| **startIndex** | **Integer**| The starting index (zero based) of the items to be returned. The default is 0. | [optional] |
| **templateName** | **String**| Specify that returned elements must have this template or a template derived from this template. The default is no template filter. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsElement**](ItemsElement.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of referenced elements matching the specified conditions. |  -  |

<a id="assetDatabaseGetSecurity"></a>
# **assetDatabaseGetSecurity**
> ItemsSecurityRights assetDatabaseGetSecurity(webId, securityItem, userIdentity, forceRefresh, selectedFields, webIdType)

Get the security information of the specified security item associated with the asset database for a specified user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetDatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AssetDatabaseApi apiInstance = new AssetDatabaseApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the asset database for the security to be checked.
    List<String> securityItem = Arrays.asList(); // List<String> | The security item of the desired security information to be returned. Multiple security items may be specified with multiple instances of the parameter. If the parameter is not specified, only 'Default' security item of the security information will be returned.
    List<String> userIdentity = Arrays.asList(); // List<String> | The user identity for the security information to be checked. Multiple security identities may be specified with multiple instances of the parameter. If the parameter is not specified, only the current user's security rights will be returned.
    Boolean forceRefresh = true; // Boolean | Indicates if the security cache should be refreshed before getting security information. The default is 'false'.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsSecurityRights result = apiInstance.assetDatabaseGetSecurity(webId, securityItem, userIdentity, forceRefresh, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetDatabaseApi#assetDatabaseGetSecurity");
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
| **webId** | **String**| The ID of the asset database for the security to be checked. | |
| **securityItem** | [**List&lt;String&gt;**](String.md)| The security item of the desired security information to be returned. Multiple security items may be specified with multiple instances of the parameter. If the parameter is not specified, only &#39;Default&#39; security item of the security information will be returned. | |
| **userIdentity** | [**List&lt;String&gt;**](String.md)| The user identity for the security information to be checked. Multiple security identities may be specified with multiple instances of the parameter. If the parameter is not specified, only the current user&#39;s security rights will be returned. | |
| **forceRefresh** | **Boolean**| Indicates if the security cache should be refreshed before getting security information. The default is &#39;false&#39;. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsSecurityRights**](ItemsSecurityRights.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Security rights. |  -  |
| **400** | Unsupported security item; an invalid or local account is specified as the user identity. |  -  |
| **401** | Access denied for the specified user identity. |  -  |
| **409** | Unsupported when using Anonymous authentication method. |  -  |
| **502** | Failed to retrieve the specified user identity. |  -  |

<a id="assetDatabaseGetSecurityEntries"></a>
# **assetDatabaseGetSecurityEntries**
> ItemsSecurityEntry assetDatabaseGetSecurityEntries(webId, nameFilter, securityItem, selectedFields, webIdType)

Retrieve the security entries of the specified security item associated with the asset database based on the specified criteria. By default, all security entries for this asset database are returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetDatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AssetDatabaseApi apiInstance = new AssetDatabaseApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the asset database.
    String nameFilter = "nameFilter_example"; // String | The name query string used for filtering security entries. The default is no filter.
    String securityItem = "securityItem_example"; // String | The security item of the desired security entries information to be returned. If the parameter is not specified, security entries of the 'Default' security item will be returned.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsSecurityEntry result = apiInstance.assetDatabaseGetSecurityEntries(webId, nameFilter, securityItem, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetDatabaseApi#assetDatabaseGetSecurityEntries");
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
| **webId** | **String**| The ID of the asset database. | |
| **nameFilter** | **String**| The name query string used for filtering security entries. The default is no filter. | [optional] |
| **securityItem** | **String**| The security item of the desired security entries information to be returned. If the parameter is not specified, security entries of the &#39;Default&#39; security item will be returned. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsSecurityEntry**](ItemsSecurityEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of security entries matching the specified condition. |  -  |

<a id="assetDatabaseGetSecurityEntryByName"></a>
# **assetDatabaseGetSecurityEntryByName**
> SecurityEntry assetDatabaseGetSecurityEntryByName(name, webId, securityItem, selectedFields, webIdType)

Retrieve the security entry of the specified security item associated with the asset database with the specified name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetDatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AssetDatabaseApi apiInstance = new AssetDatabaseApi(defaultClient);
    String name = "name_example"; // String | The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username.
    String webId = "webId_example"; // String | The ID of the asset database.
    String securityItem = "securityItem_example"; // String | The security item of the desired security entries information to be returned. If the parameter is not specified, security entries of the 'Default' security item will be returned.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      SecurityEntry result = apiInstance.assetDatabaseGetSecurityEntryByName(name, webId, securityItem, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetDatabaseApi#assetDatabaseGetSecurityEntryByName");
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
| **name** | **String**| The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username. | |
| **webId** | **String**| The ID of the asset database. | |
| **securityItem** | **String**| The security item of the desired security entries information to be returned. If the parameter is not specified, security entries of the &#39;Default&#39; security item will be returned. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**SecurityEntry**](SecurityEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The security entry matching the specified condition. |  -  |
| **404** | The security entry with the specified name is not found. |  -  |

<a id="assetDatabaseGetTableCategories"></a>
# **assetDatabaseGetTableCategories**
> ItemsTableCategory assetDatabaseGetTableCategories(webId, selectedFields, webIdType)

Retrieve table categories for a given Asset Database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetDatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AssetDatabaseApi apiInstance = new AssetDatabaseApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the database.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsTableCategory result = apiInstance.assetDatabaseGetTableCategories(webId, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetDatabaseApi#assetDatabaseGetTableCategories");
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
| **webId** | **String**| The ID of the database. | |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsTableCategory**](ItemsTableCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The table categories on the specified database. |  -  |

<a id="assetDatabaseGetTables"></a>
# **assetDatabaseGetTables**
> ItemsTable assetDatabaseGetTables(webId, selectedFields, webIdType)

Retrieve tables for given Asset Database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetDatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AssetDatabaseApi apiInstance = new AssetDatabaseApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the database.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsTable result = apiInstance.assetDatabaseGetTables(webId, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetDatabaseApi#assetDatabaseGetTables");
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
| **webId** | **String**| The ID of the database. | |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsTable**](ItemsTable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The tables on the specified database. |  -  |

<a id="assetDatabaseImport"></a>
# **assetDatabaseImport**
> assetDatabaseImport(webId, importMode)

Import an asset database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetDatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AssetDatabaseApi apiInstance = new AssetDatabaseApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the asset database.
    List<String> importMode = Arrays.asList(); // List<String> | Indicates the type of import to perform. The default is 'AllowCreate | AllowUpdate | AutoCheckIn'. Multiple import modes may be specified by using multiple instances of importMode.
    try {
      apiInstance.assetDatabaseImport(webId, importMode);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetDatabaseApi#assetDatabaseImport");
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
| **webId** | **String**| The ID of the asset database. | |
| **importMode** | [**List&lt;String&gt;**](String.md)| Indicates the type of import to perform. The default is &#39;AllowCreate | AllowUpdate | AutoCheckIn&#39;. Multiple import modes may be specified by using multiple instances of importMode. | [optional] |

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
| **200** | Database imported. |  -  |

<a id="assetDatabaseRemoveReferencedElement"></a>
# **assetDatabaseRemoveReferencedElement**
> assetDatabaseRemoveReferencedElement(webId, referencedElementWebId)

Remove a reference to an existing element from the specified database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetDatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AssetDatabaseApi apiInstance = new AssetDatabaseApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the database which the referenced element will be removed from.
    List<String> referencedElementWebId = Arrays.asList(); // List<String> | The ID of the referenced element. Multiple referenced elements may be specified with multiple instances of the parameter.
    try {
      apiInstance.assetDatabaseRemoveReferencedElement(webId, referencedElementWebId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetDatabaseApi#assetDatabaseRemoveReferencedElement");
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
| **webId** | **String**| The ID of the database which the referenced element will be removed from. | |
| **referencedElementWebId** | [**List&lt;String&gt;**](String.md)| The ID of the referenced element. Multiple referenced elements may be specified with multiple instances of the parameter. | |

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
| **204** | The referenced element was successfully removed. |  -  |

<a id="assetDatabaseUpdate"></a>
# **assetDatabaseUpdate**
> assetDatabaseUpdate(webId, database)

Update an asset database by replacing items in its definition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetDatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AssetDatabaseApi apiInstance = new AssetDatabaseApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the database.
    AssetDatabase database = new AssetDatabase(); // AssetDatabase | A partial database containing the desired changes.
    try {
      apiInstance.assetDatabaseUpdate(webId, database);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetDatabaseApi#assetDatabaseUpdate");
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
| **webId** | **String**| The ID of the database. | |
| **database** | [**AssetDatabase**](AssetDatabase.md)| A partial database containing the desired changes. | |

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
| **204** | The database was updated. |  -  |

<a id="assetDatabaseUpdateSecurityEntry"></a>
# **assetDatabaseUpdateSecurityEntry**
> assetDatabaseUpdateSecurityEntry(name, webId, securityEntry, applyToChildren, securityItem)

Update a security entry owned by the asset database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetDatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AssetDatabaseApi apiInstance = new AssetDatabaseApi(defaultClient);
    String name = "name_example"; // String | The name of the security entry.
    String webId = "webId_example"; // String | The ID of the asset database where the security entry will be updated.
    SecurityEntry securityEntry = new SecurityEntry(); // SecurityEntry | The new security entry definition. The full list of allow and deny rights must be supplied or they will be removed.
    Boolean applyToChildren = true; // Boolean | If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.
    String securityItem = "securityItem_example"; // String | The security item of the desired security entries to be updated. If the parameter is not specified, security entries of the 'Default' security item will be updated.
    try {
      apiInstance.assetDatabaseUpdateSecurityEntry(name, webId, securityEntry, applyToChildren, securityItem);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetDatabaseApi#assetDatabaseUpdateSecurityEntry");
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
| **name** | **String**| The name of the security entry. | |
| **webId** | **String**| The ID of the asset database where the security entry will be updated. | |
| **securityEntry** | [**SecurityEntry**](SecurityEntry.md)| The new security entry definition. The full list of allow and deny rights must be supplied or they will be removed. | |
| **applyToChildren** | **Boolean**| If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change. | [optional] |
| **securityItem** | **String**| The security item of the desired security entries to be updated. If the parameter is not specified, security entries of the &#39;Default&#39; security item will be updated. | [optional] |

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
| **204** | The security entry was updated. |  -  |

