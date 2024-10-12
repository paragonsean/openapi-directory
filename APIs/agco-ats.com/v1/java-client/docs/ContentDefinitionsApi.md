# ContentDefinitionsApi

All URIs are relative to *https://secure.agco-ats.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**contentDefinitionsDeleteContentDefinition**](ContentDefinitionsApi.md#contentDefinitionsDeleteContentDefinition) | **DELETE** /api/v2/ContentDefinitions/{contentDefinitionID} | Delete a ContentDefinition |
| [**contentDefinitionsDeleteContentDefinitionAttribute**](ContentDefinitionsApi.md#contentDefinitionsDeleteContentDefinitionAttribute) | **DELETE** /api/v2/ContentDefinitionAttributes/{contentDefinitionAttributeID} | Remove an Attribute from a ContentDefinition |
| [**contentDefinitionsGetContentDefinition**](ContentDefinitionsApi.md#contentDefinitionsGetContentDefinition) | **GET** /api/v2/ContentDefinitions/{contentDefinitionID} | Get a ContentDefinition by ID |
| [**contentDefinitionsGetContentDefinitionAttributes**](ContentDefinitionsApi.md#contentDefinitionsGetContentDefinitionAttributes) | **GET** /api/v2/ContentDefinitions/{contentDefinitionID}/Attributes | Get Attributes for a ContentDefinition |
| [**contentDefinitionsGetContentDefinitions**](ContentDefinitionsApi.md#contentDefinitionsGetContentDefinitions) | **GET** /api/v2/ContentDefinitions | Get ContentDefinitions |
| [**contentDefinitionsPostContentDefinition**](ContentDefinitionsApi.md#contentDefinitionsPostContentDefinition) | **POST** /api/v2/ContentDefinitions | Create a ContentDefinition |
| [**contentDefinitionsPostContentDefinitionAttribute**](ContentDefinitionsApi.md#contentDefinitionsPostContentDefinitionAttribute) | **POST** /api/v2/ContentDefinitions/{contentDefinitionID}/Attributes | Add an Attribute to a ContentDefinition |
| [**contentDefinitionsPostContentDefinitionAttributes**](ContentDefinitionsApi.md#contentDefinitionsPostContentDefinitionAttributes) | **POST** /api/v2/ContentDefinitions/{contentDefinitionID}/Attributes/Batch | No Documentation Found. |
| [**contentDefinitionsPutContentDefinition**](ContentDefinitionsApi.md#contentDefinitionsPutContentDefinition) | **PUT** /api/v2/ContentDefinitions/{contentDefinitionID} | Update a ContentDefinition |
| [**contentDefinitionsPutContentDefinitionAttributeAsync**](ContentDefinitionsApi.md#contentDefinitionsPutContentDefinitionAttributeAsync) | **PUT** /api/v2/ContentDefinitionAttributes/{contentDefinitionAttributeID} | Update an Attribute for a ContentDefinition |
| [**contentDefinitionsPutContentDefinitionAttributes**](ContentDefinitionsApi.md#contentDefinitionsPutContentDefinitionAttributes) | **PUT** /api/v2/ContentDefinitionAttributes/Batch | No Documentation Found. |


<a id="contentDefinitionsDeleteContentDefinition"></a>
# **contentDefinitionsDeleteContentDefinition**
> contentDefinitionsDeleteContentDefinition(contentDefinitionID)

Delete a ContentDefinition

Deletes an ContentDefinition. When successful, the response is empty.  If unsuccessful, an appropriate              ApiError is returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ContentDefinitionsApi apiInstance = new ContentDefinitionsApi(defaultClient);
    Integer contentDefinitionID = 56; // Integer | The ID of the ContentDefinition to delete
    try {
      apiInstance.contentDefinitionsDeleteContentDefinition(contentDefinitionID);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentDefinitionsApi#contentDefinitionsDeleteContentDefinition");
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
| **contentDefinitionID** | **Integer**| The ID of the ContentDefinition to delete | |

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

<a id="contentDefinitionsDeleteContentDefinitionAttribute"></a>
# **contentDefinitionsDeleteContentDefinitionAttribute**
> contentDefinitionsDeleteContentDefinitionAttribute(contentDefinitionAttributeID)

Remove an Attribute from a ContentDefinition

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ContentDefinitionsApi apiInstance = new ContentDefinitionsApi(defaultClient);
    Integer contentDefinitionAttributeID = 56; // Integer | The ID of the Attribute to remove.
    try {
      apiInstance.contentDefinitionsDeleteContentDefinitionAttribute(contentDefinitionAttributeID);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentDefinitionsApi#contentDefinitionsDeleteContentDefinitionAttribute");
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
| **contentDefinitionAttributeID** | **Integer**| The ID of the Attribute to remove. | |

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

<a id="contentDefinitionsGetContentDefinition"></a>
# **contentDefinitionsGetContentDefinition**
> ContentSubmissionSharedBusinessEntitiesContentDefinition contentDefinitionsGetContentDefinition(contentDefinitionID, includeAttributes)

Get a ContentDefinition by ID

Gets a ContentDefinition by ID. When successful, the response is the requested ContentDefinition.              If unsuccessful, an appropriate ApiError is returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ContentDefinitionsApi apiInstance = new ContentDefinitionsApi(defaultClient);
    Integer contentDefinitionID = 56; // Integer | The ID of the ContentDefinition to get.
    String includeAttributes = "includeAttributes_example"; // String | Names of Attributes to include when retrieving this definition. This should be a comma-separated list. If not provided, Attributes are not included. If '*', all Attributes are included.
    try {
      ContentSubmissionSharedBusinessEntitiesContentDefinition result = apiInstance.contentDefinitionsGetContentDefinition(contentDefinitionID, includeAttributes);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentDefinitionsApi#contentDefinitionsGetContentDefinition");
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
| **contentDefinitionID** | **Integer**| The ID of the ContentDefinition to get. | |
| **includeAttributes** | **String**| Names of Attributes to include when retrieving this definition. This should be a comma-separated list. If not provided, Attributes are not included. If &#39;*&#39;, all Attributes are included. | [optional] |

### Return type

[**ContentSubmissionSharedBusinessEntitiesContentDefinition**](ContentSubmissionSharedBusinessEntitiesContentDefinition.md)

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

<a id="contentDefinitionsGetContentDefinitionAttributes"></a>
# **contentDefinitionsGetContentDefinitionAttributes**
> APIPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute contentDefinitionsGetContentDefinitionAttributes(contentDefinitionID, limit, offset, name)

Get Attributes for a ContentDefinition

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ContentDefinitionsApi apiInstance = new ContentDefinitionsApi(defaultClient);
    Integer contentDefinitionID = 56; // Integer | The ID of the ContentDefinition.
    Integer limit = 56; // Integer | Optional. The page limit.  If not specified, the default page limit is 10.
    Integer offset = 56; // Integer | Optional. The page offset.  If not specified, the default page offset is 0.
    String name = "name_example"; // String | Optional. Filter the attributes by Name.
    try {
      APIPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute result = apiInstance.contentDefinitionsGetContentDefinitionAttributes(contentDefinitionID, limit, offset, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentDefinitionsApi#contentDefinitionsGetContentDefinitionAttributes");
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
| **contentDefinitionID** | **Integer**| The ID of the ContentDefinition. | |
| **limit** | **Integer**| Optional. The page limit.  If not specified, the default page limit is 10. | [optional] |
| **offset** | **Integer**| Optional. The page offset.  If not specified, the default page offset is 0. | [optional] |
| **name** | **String**| Optional. Filter the attributes by Name. | [optional] |

### Return type

[**APIPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute**](APIPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="contentDefinitionsGetContentDefinitions"></a>
# **contentDefinitionsGetContentDefinitions**
> APIPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinition contentDefinitionsGetContentDefinitions(limit, offset, userID, includeAttributes, name, typeID, packageTypeID)

Get ContentDefinitions

Gets a collection of ContentDefinitions. When successful, the response is a PagedResponse of ContentDefinitions.              If unsuccessful, an appropriate ApiError is returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ContentDefinitionsApi apiInstance = new ContentDefinitionsApi(defaultClient);
    Integer limit = 56; // Integer | Optional. The page limit.  If not specified, the default page limit is 10.
    Integer offset = 56; // Integer | Optional. The page offset.  If not specified, the default page offset is 0.
    Integer userID = 56; // Integer | Optional. Filter by UserID.
    String includeAttributes = "includeAttributes_example"; // String | Names of Attributes to include when retrieving this definition. This should be a comma-separated list. If not provided, Attributes are not included. If '*', all Attributes are included.
    String name = "name_example"; // String | Optional. Filter by Name. Supports beginning and ending wildcard (*).
    Integer typeID = 56; // Integer | Optional. Filter by TypeID.
    String packageTypeID = "packageTypeID_example"; // String | Optional. Filter by PackageTypeID.
    try {
      APIPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinition result = apiInstance.contentDefinitionsGetContentDefinitions(limit, offset, userID, includeAttributes, name, typeID, packageTypeID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentDefinitionsApi#contentDefinitionsGetContentDefinitions");
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
| **limit** | **Integer**| Optional. The page limit.  If not specified, the default page limit is 10. | [optional] |
| **offset** | **Integer**| Optional. The page offset.  If not specified, the default page offset is 0. | [optional] |
| **userID** | **Integer**| Optional. Filter by UserID. | [optional] |
| **includeAttributes** | **String**| Names of Attributes to include when retrieving this definition. This should be a comma-separated list. If not provided, Attributes are not included. If &#39;*&#39;, all Attributes are included. | [optional] |
| **name** | **String**| Optional. Filter by Name. Supports beginning and ending wildcard (*). | [optional] |
| **typeID** | **Integer**| Optional. Filter by TypeID. | [optional] |
| **packageTypeID** | **String**| Optional. Filter by PackageTypeID. | [optional] |

### Return type

[**APIPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinition**](APIPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="contentDefinitionsPostContentDefinition"></a>
# **contentDefinitionsPostContentDefinition**
> Integer contentDefinitionsPostContentDefinition(contentSubmissionSharedBusinessEntitiesContentDefinition)

Create a ContentDefinition

Creates a ContentDefinition.  The body of the POST is the ContentDefinition to create.              The ContentDefinitionID will be assigned on creation of the Job.  When successful, the response              is the JobID.  If unsuccessful, an appropriate ApiError is returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ContentDefinitionsApi apiInstance = new ContentDefinitionsApi(defaultClient);
    ContentSubmissionSharedBusinessEntitiesContentDefinition contentSubmissionSharedBusinessEntitiesContentDefinition = new ContentSubmissionSharedBusinessEntitiesContentDefinition(); // ContentSubmissionSharedBusinessEntitiesContentDefinition | The ContentDefinition to create.
    try {
      Integer result = apiInstance.contentDefinitionsPostContentDefinition(contentSubmissionSharedBusinessEntitiesContentDefinition);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentDefinitionsApi#contentDefinitionsPostContentDefinition");
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
| **contentSubmissionSharedBusinessEntitiesContentDefinition** | [**ContentSubmissionSharedBusinessEntitiesContentDefinition**](ContentSubmissionSharedBusinessEntitiesContentDefinition.md)| The ContentDefinition to create. | |

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

<a id="contentDefinitionsPostContentDefinitionAttribute"></a>
# **contentDefinitionsPostContentDefinitionAttribute**
> Integer contentDefinitionsPostContentDefinitionAttribute(contentDefinitionID, contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute)

Add an Attribute to a ContentDefinition

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ContentDefinitionsApi apiInstance = new ContentDefinitionsApi(defaultClient);
    Integer contentDefinitionID = 56; // Integer | The ID of the ContentDefinition
    ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute = new ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute(); // ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute | The Attribute to add.
    try {
      Integer result = apiInstance.contentDefinitionsPostContentDefinitionAttribute(contentDefinitionID, contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentDefinitionsApi#contentDefinitionsPostContentDefinitionAttribute");
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
| **contentDefinitionID** | **Integer**| The ID of the ContentDefinition | |
| **contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute** | [**ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute**](ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute.md)| The Attribute to add. | |

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

<a id="contentDefinitionsPostContentDefinitionAttributes"></a>
# **contentDefinitionsPostContentDefinitionAttributes**
> contentDefinitionsPostContentDefinitionAttributes(contentDefinitionID, contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute)

No Documentation Found.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ContentDefinitionsApi apiInstance = new ContentDefinitionsApi(defaultClient);
    Integer contentDefinitionID = 56; // Integer | 
    List<ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute> contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute = Arrays.asList(); // List<ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute> | 
    try {
      apiInstance.contentDefinitionsPostContentDefinitionAttributes(contentDefinitionID, contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentDefinitionsApi#contentDefinitionsPostContentDefinitionAttributes");
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
| **contentDefinitionID** | **Integer**|  | |
| **contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute** | [**List&lt;ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute&gt;**](ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute.md)|  | |

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

<a id="contentDefinitionsPutContentDefinition"></a>
# **contentDefinitionsPutContentDefinition**
> contentDefinitionsPutContentDefinition(contentDefinitionID, contentSubmissionSharedBusinessEntitiesContentDefinition)

Update a ContentDefinition

Updates a ContentDefinition.  The body of the PUT is the updated ContentDefinition.                When successful, the response is empty.  If unsuccessful, an appropriate ApiError is returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ContentDefinitionsApi apiInstance = new ContentDefinitionsApi(defaultClient);
    Integer contentDefinitionID = 56; // Integer | The ID of the ContentDefinition to update
    ContentSubmissionSharedBusinessEntitiesContentDefinition contentSubmissionSharedBusinessEntitiesContentDefinition = new ContentSubmissionSharedBusinessEntitiesContentDefinition(); // ContentSubmissionSharedBusinessEntitiesContentDefinition | The updated ContentDefinition
    try {
      apiInstance.contentDefinitionsPutContentDefinition(contentDefinitionID, contentSubmissionSharedBusinessEntitiesContentDefinition);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentDefinitionsApi#contentDefinitionsPutContentDefinition");
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
| **contentDefinitionID** | **Integer**| The ID of the ContentDefinition to update | |
| **contentSubmissionSharedBusinessEntitiesContentDefinition** | [**ContentSubmissionSharedBusinessEntitiesContentDefinition**](ContentSubmissionSharedBusinessEntitiesContentDefinition.md)| The updated ContentDefinition | |

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

<a id="contentDefinitionsPutContentDefinitionAttributeAsync"></a>
# **contentDefinitionsPutContentDefinitionAttributeAsync**
> contentDefinitionsPutContentDefinitionAttributeAsync(contentDefinitionAttributeID, contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute)

Update an Attribute for a ContentDefinition

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ContentDefinitionsApi apiInstance = new ContentDefinitionsApi(defaultClient);
    Integer contentDefinitionAttributeID = 56; // Integer | The ID of the Attribute to update.
    ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute = new ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute(); // ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute | The Attribute to update.
    try {
      apiInstance.contentDefinitionsPutContentDefinitionAttributeAsync(contentDefinitionAttributeID, contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentDefinitionsApi#contentDefinitionsPutContentDefinitionAttributeAsync");
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
| **contentDefinitionAttributeID** | **Integer**| The ID of the Attribute to update. | |
| **contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute** | [**ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute**](ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute.md)| The Attribute to update. | |

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

<a id="contentDefinitionsPutContentDefinitionAttributes"></a>
# **contentDefinitionsPutContentDefinitionAttributes**
> contentDefinitionsPutContentDefinitionAttributes(contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute)

No Documentation Found.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ContentDefinitionsApi apiInstance = new ContentDefinitionsApi(defaultClient);
    List<ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute> contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute = Arrays.asList(); // List<ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute> | 
    try {
      apiInstance.contentDefinitionsPutContentDefinitionAttributes(contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentDefinitionsApi#contentDefinitionsPutContentDefinitionAttributes");
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
| **contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute** | [**List&lt;ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute&gt;**](ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute.md)|  | |

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

