# ContentSubmissionsApi

All URIs are relative to *https://secure.agco-ats.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**contentSubmissionsDeleteContentSubmission**](ContentSubmissionsApi.md#contentSubmissionsDeleteContentSubmission) | **DELETE** /api/v2/ContentSubmissions/{contentSubmissionID} | Delete a ContentSubmission |
| [**contentSubmissionsDeleteContentSubmissionAttribute**](ContentSubmissionsApi.md#contentSubmissionsDeleteContentSubmissionAttribute) | **DELETE** /api/v2/ContentSubmissionAttributes/{contentSubmissionAttributeID} | Remove an Attribute from a ContentSubmission |
| [**contentSubmissionsGetContentSubmission**](ContentSubmissionsApi.md#contentSubmissionsGetContentSubmission) | **GET** /api/v2/ContentSubmissions/{contentSubmissionID} | Get a ContentSubmission by ID |
| [**contentSubmissionsGetContentSubmissionAttributes**](ContentSubmissionsApi.md#contentSubmissionsGetContentSubmissionAttributes) | **GET** /api/v2/ContentSubmissions/{contentSubmissionID}/Attributes | Get Attributes for a ContentSubmission |
| [**contentSubmissionsGetContentSubmissionStatus**](ContentSubmissionsApi.md#contentSubmissionsGetContentSubmissionStatus) | **GET** /api/v2/ContentSubmissions/{contentSubmissionID}/Status | Get the status of a ContentSubmission |
| [**contentSubmissionsGetContentSubmissions**](ContentSubmissionsApi.md#contentSubmissionsGetContentSubmissions) | **GET** /api/v2/ContentSubmissions | Get ContentSubmissions |
| [**contentSubmissionsPostContentSubmission**](ContentSubmissionsApi.md#contentSubmissionsPostContentSubmission) | **POST** /api/v2/ContentSubmissions | Create a ContentSubmission |
| [**contentSubmissionsPostContentSubmissionAttribute**](ContentSubmissionsApi.md#contentSubmissionsPostContentSubmissionAttribute) | **POST** /api/v2/ContentSubmissions/{contentSubmissionID}/Attributes | Add an Attribute to a ContentSubmission |
| [**contentSubmissionsPostContentSubmissionAttributes**](ContentSubmissionsApi.md#contentSubmissionsPostContentSubmissionAttributes) | **POST** /api/v2/ContentSubmissions/{contentSubmissionID}/Attributes/Batch | No Documentation Found. |
| [**contentSubmissionsPutContentSubmission**](ContentSubmissionsApi.md#contentSubmissionsPutContentSubmission) | **PUT** /api/v2/ContentSubmissions/{contentSubmissionID} | Update a ContentSubmission |
| [**contentSubmissionsPutContentSubmissionAttributeAsync**](ContentSubmissionsApi.md#contentSubmissionsPutContentSubmissionAttributeAsync) | **PUT** /api/v2/ContentSubmissionAttributes/{contentSubmissionAttributeID} | Update an Attribute for a ContentSubmission |
| [**contentSubmissionsPutContentSubmissionAttributes**](ContentSubmissionsApi.md#contentSubmissionsPutContentSubmissionAttributes) | **PUT** /api/v2/ContentSubmissionAttributes/Batch | No Documentation Found. |


<a id="contentSubmissionsDeleteContentSubmission"></a>
# **contentSubmissionsDeleteContentSubmission**
> contentSubmissionsDeleteContentSubmission(contentSubmissionID)

Delete a ContentSubmission

Deletes an ContentSubmission. When successful, the response is empty.  If unsuccessful, an appropriate              ApiError is returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentSubmissionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ContentSubmissionsApi apiInstance = new ContentSubmissionsApi(defaultClient);
    Integer contentSubmissionID = 56; // Integer | The ID of the ContentSubmission to delete
    try {
      apiInstance.contentSubmissionsDeleteContentSubmission(contentSubmissionID);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentSubmissionsApi#contentSubmissionsDeleteContentSubmission");
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
| **contentSubmissionID** | **Integer**| The ID of the ContentSubmission to delete | |

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

<a id="contentSubmissionsDeleteContentSubmissionAttribute"></a>
# **contentSubmissionsDeleteContentSubmissionAttribute**
> contentSubmissionsDeleteContentSubmissionAttribute(contentSubmissionAttributeID)

Remove an Attribute from a ContentSubmission

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentSubmissionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ContentSubmissionsApi apiInstance = new ContentSubmissionsApi(defaultClient);
    Integer contentSubmissionAttributeID = 56; // Integer | The ID of the Attribute to remove.
    try {
      apiInstance.contentSubmissionsDeleteContentSubmissionAttribute(contentSubmissionAttributeID);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentSubmissionsApi#contentSubmissionsDeleteContentSubmissionAttribute");
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
| **contentSubmissionAttributeID** | **Integer**| The ID of the Attribute to remove. | |

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

<a id="contentSubmissionsGetContentSubmission"></a>
# **contentSubmissionsGetContentSubmission**
> ContentSubmissionSharedBusinessEntitiesContentSubmission contentSubmissionsGetContentSubmission(contentSubmissionID, includeAttributes)

Get a ContentSubmission by ID

Gets a ContentSubmission by ID. When successful, the response is the requested ContentSubmission.              If unsuccessful, an appropriate ApiError is returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentSubmissionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ContentSubmissionsApi apiInstance = new ContentSubmissionsApi(defaultClient);
    Integer contentSubmissionID = 56; // Integer | The ID of the ContentSubmission to get.
    String includeAttributes = "includeAttributes_example"; // String | Names of Attributes to include when retrieving this submission. This should be a comma-separated list.
    try {
      ContentSubmissionSharedBusinessEntitiesContentSubmission result = apiInstance.contentSubmissionsGetContentSubmission(contentSubmissionID, includeAttributes);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentSubmissionsApi#contentSubmissionsGetContentSubmission");
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
| **contentSubmissionID** | **Integer**| The ID of the ContentSubmission to get. | |
| **includeAttributes** | **String**| Names of Attributes to include when retrieving this submission. This should be a comma-separated list. | [optional] |

### Return type

[**ContentSubmissionSharedBusinessEntitiesContentSubmission**](ContentSubmissionSharedBusinessEntitiesContentSubmission.md)

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

<a id="contentSubmissionsGetContentSubmissionAttributes"></a>
# **contentSubmissionsGetContentSubmissionAttributes**
> APIPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute contentSubmissionsGetContentSubmissionAttributes(contentSubmissionID, limit, offset, name)

Get Attributes for a ContentSubmission

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentSubmissionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ContentSubmissionsApi apiInstance = new ContentSubmissionsApi(defaultClient);
    Integer contentSubmissionID = 56; // Integer | The ID of the ContentSubmission.
    Integer limit = 56; // Integer | Optional. The page limit.  If not specified, the default page limit is 10.
    Integer offset = 56; // Integer | Optional. The page offset.  If not specified, the default page offset is 0.
    String name = "name_example"; // String | Optional. Filter the attributes by Name.
    try {
      APIPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute result = apiInstance.contentSubmissionsGetContentSubmissionAttributes(contentSubmissionID, limit, offset, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentSubmissionsApi#contentSubmissionsGetContentSubmissionAttributes");
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
| **contentSubmissionID** | **Integer**| The ID of the ContentSubmission. | |
| **limit** | **Integer**| Optional. The page limit.  If not specified, the default page limit is 10. | [optional] |
| **offset** | **Integer**| Optional. The page offset.  If not specified, the default page offset is 0. | [optional] |
| **name** | **String**| Optional. Filter the attributes by Name. | [optional] |

### Return type

[**APIPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute**](APIPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute.md)

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

<a id="contentSubmissionsGetContentSubmissionStatus"></a>
# **contentSubmissionsGetContentSubmissionStatus**
> BuildSystemSharedInterfacesIJobRun contentSubmissionsGetContentSubmissionStatus(contentSubmissionID, includeActivityRunDetails)

Get the status of a ContentSubmission

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentSubmissionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ContentSubmissionsApi apiInstance = new ContentSubmissionsApi(defaultClient);
    Integer contentSubmissionID = 56; // Integer | The ID of the ContentSubmission to get.
    Boolean includeActivityRunDetails = true; // Boolean | True to include all status details if JobRun. Defaults to false
    try {
      BuildSystemSharedInterfacesIJobRun result = apiInstance.contentSubmissionsGetContentSubmissionStatus(contentSubmissionID, includeActivityRunDetails);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentSubmissionsApi#contentSubmissionsGetContentSubmissionStatus");
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
| **contentSubmissionID** | **Integer**| The ID of the ContentSubmission to get. | |
| **includeActivityRunDetails** | **Boolean**| True to include all status details if JobRun. Defaults to false | [optional] |

### Return type

[**BuildSystemSharedInterfacesIJobRun**](BuildSystemSharedInterfacesIJobRun.md)

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

<a id="contentSubmissionsGetContentSubmissions"></a>
# **contentSubmissionsGetContentSubmissions**
> APIPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmission contentSubmissionsGetContentSubmissions(limit, offset, userID, contentDefinitionID, includeAttributes, releaseID, typeID, version, includeDefinition)

Get ContentSubmissions

Gets a collection of ContentSubmissions. When successful, the response is a PagedResponse of ContentSubmissions. Additional searches: attributes[Name]&#x3D;Value. This can be used to search for submissions that have the specified values for attributes. Beginning and ending wildcard (*) supported for value.              If unsuccessful, an appropriate ApiError is returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentSubmissionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ContentSubmissionsApi apiInstance = new ContentSubmissionsApi(defaultClient);
    Integer limit = 56; // Integer | Optional. The page limit.  If not specified, the default page limit is 10.
    Integer offset = 56; // Integer | Optional. The page offset.  If not specified, the default page offset is 0.
    Integer userID = 56; // Integer | Optional. Filter by UserID.
    Integer contentDefinitionID = 56; // Integer | Optional. Filter by ContentDefinitionID
    String includeAttributes = "includeAttributes_example"; // String | Names of Attributes to include when retrieving this submission. This should be a comma-separated list. If not provided, Attributes are not included. If '*', all Attributes are included.
    Integer releaseID = 56; // Integer | Optional. Filter the submissions by whether they are part of the Release with the specified Release ID.
    Integer typeID = 56; // Integer | Optional. Filter submissions by their ContentDefinition's Type ID.
    Integer version = 56; // Integer | Optional. Filter submissions by their Version.
    Boolean includeDefinition = true; // Boolean | Optional. If true, includes the ContentDefinition for each submission.
    try {
      APIPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmission result = apiInstance.contentSubmissionsGetContentSubmissions(limit, offset, userID, contentDefinitionID, includeAttributes, releaseID, typeID, version, includeDefinition);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentSubmissionsApi#contentSubmissionsGetContentSubmissions");
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
| **contentDefinitionID** | **Integer**| Optional. Filter by ContentDefinitionID | [optional] |
| **includeAttributes** | **String**| Names of Attributes to include when retrieving this submission. This should be a comma-separated list. If not provided, Attributes are not included. If &#39;*&#39;, all Attributes are included. | [optional] |
| **releaseID** | **Integer**| Optional. Filter the submissions by whether they are part of the Release with the specified Release ID. | [optional] |
| **typeID** | **Integer**| Optional. Filter submissions by their ContentDefinition&#39;s Type ID. | [optional] |
| **version** | **Integer**| Optional. Filter submissions by their Version. | [optional] |
| **includeDefinition** | **Boolean**| Optional. If true, includes the ContentDefinition for each submission. | [optional] |

### Return type

[**APIPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmission**](APIPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmission.md)

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

<a id="contentSubmissionsPostContentSubmission"></a>
# **contentSubmissionsPostContentSubmission**
> Integer contentSubmissionsPostContentSubmission(contentSubmissionSharedBusinessEntitiesContentSubmission)

Create a ContentSubmission

Creates a ContentSubmission.  The body of the POST is the ContentSubmission to create.              The ContentSubmissionID will be assigned on creation of the Job.  When successful, the response              is the ContentSubmissionID.  If unsuccessful, an appropriate ApiError is returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentSubmissionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ContentSubmissionsApi apiInstance = new ContentSubmissionsApi(defaultClient);
    ContentSubmissionSharedBusinessEntitiesContentSubmission contentSubmissionSharedBusinessEntitiesContentSubmission = new ContentSubmissionSharedBusinessEntitiesContentSubmission(); // ContentSubmissionSharedBusinessEntitiesContentSubmission | The ContentSubmission to create.
    try {
      Integer result = apiInstance.contentSubmissionsPostContentSubmission(contentSubmissionSharedBusinessEntitiesContentSubmission);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentSubmissionsApi#contentSubmissionsPostContentSubmission");
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
| **contentSubmissionSharedBusinessEntitiesContentSubmission** | [**ContentSubmissionSharedBusinessEntitiesContentSubmission**](ContentSubmissionSharedBusinessEntitiesContentSubmission.md)| The ContentSubmission to create. | |

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

<a id="contentSubmissionsPostContentSubmissionAttribute"></a>
# **contentSubmissionsPostContentSubmissionAttribute**
> Integer contentSubmissionsPostContentSubmissionAttribute(contentSubmissionID, contentSubmissionSharedBusinessEntitiesContentSubmissionAttribute)

Add an Attribute to a ContentSubmission

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentSubmissionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ContentSubmissionsApi apiInstance = new ContentSubmissionsApi(defaultClient);
    Integer contentSubmissionID = 56; // Integer | The ID of the ContentSubmission
    ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute contentSubmissionSharedBusinessEntitiesContentSubmissionAttribute = new ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute(); // ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute | The Attribute to add.
    try {
      Integer result = apiInstance.contentSubmissionsPostContentSubmissionAttribute(contentSubmissionID, contentSubmissionSharedBusinessEntitiesContentSubmissionAttribute);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentSubmissionsApi#contentSubmissionsPostContentSubmissionAttribute");
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
| **contentSubmissionID** | **Integer**| The ID of the ContentSubmission | |
| **contentSubmissionSharedBusinessEntitiesContentSubmissionAttribute** | [**ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute**](ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute.md)| The Attribute to add. | |

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

<a id="contentSubmissionsPostContentSubmissionAttributes"></a>
# **contentSubmissionsPostContentSubmissionAttributes**
> contentSubmissionsPostContentSubmissionAttributes(contentSubmissionID, contentSubmissionSharedBusinessEntitiesContentSubmissionAttribute)

No Documentation Found.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentSubmissionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ContentSubmissionsApi apiInstance = new ContentSubmissionsApi(defaultClient);
    Integer contentSubmissionID = 56; // Integer | 
    List<ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute> contentSubmissionSharedBusinessEntitiesContentSubmissionAttribute = Arrays.asList(); // List<ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute> | 
    try {
      apiInstance.contentSubmissionsPostContentSubmissionAttributes(contentSubmissionID, contentSubmissionSharedBusinessEntitiesContentSubmissionAttribute);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentSubmissionsApi#contentSubmissionsPostContentSubmissionAttributes");
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
| **contentSubmissionID** | **Integer**|  | |
| **contentSubmissionSharedBusinessEntitiesContentSubmissionAttribute** | [**List&lt;ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute&gt;**](ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute.md)|  | |

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

<a id="contentSubmissionsPutContentSubmission"></a>
# **contentSubmissionsPutContentSubmission**
> contentSubmissionsPutContentSubmission(contentSubmissionID, contentSubmissionSharedBusinessEntitiesContentSubmission)

Update a ContentSubmission

Updates a ContentSubmission.  The body of the PUT is the updated ContentSubmission.                When successful, the response is empty.  If unsuccessful, an appropriate ApiError is returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentSubmissionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ContentSubmissionsApi apiInstance = new ContentSubmissionsApi(defaultClient);
    Integer contentSubmissionID = 56; // Integer | The ID of the ContentSubmission to update
    ContentSubmissionSharedBusinessEntitiesContentSubmission contentSubmissionSharedBusinessEntitiesContentSubmission = new ContentSubmissionSharedBusinessEntitiesContentSubmission(); // ContentSubmissionSharedBusinessEntitiesContentSubmission | The updated ContentSubmission
    try {
      apiInstance.contentSubmissionsPutContentSubmission(contentSubmissionID, contentSubmissionSharedBusinessEntitiesContentSubmission);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentSubmissionsApi#contentSubmissionsPutContentSubmission");
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
| **contentSubmissionID** | **Integer**| The ID of the ContentSubmission to update | |
| **contentSubmissionSharedBusinessEntitiesContentSubmission** | [**ContentSubmissionSharedBusinessEntitiesContentSubmission**](ContentSubmissionSharedBusinessEntitiesContentSubmission.md)| The updated ContentSubmission | |

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

<a id="contentSubmissionsPutContentSubmissionAttributeAsync"></a>
# **contentSubmissionsPutContentSubmissionAttributeAsync**
> contentSubmissionsPutContentSubmissionAttributeAsync(contentSubmissionAttributeID, contentSubmissionSharedBusinessEntitiesContentSubmissionAttribute)

Update an Attribute for a ContentSubmission

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentSubmissionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ContentSubmissionsApi apiInstance = new ContentSubmissionsApi(defaultClient);
    Integer contentSubmissionAttributeID = 56; // Integer | The ID of the Attribute to update.
    ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute contentSubmissionSharedBusinessEntitiesContentSubmissionAttribute = new ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute(); // ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute | The Attribute to update.
    try {
      apiInstance.contentSubmissionsPutContentSubmissionAttributeAsync(contentSubmissionAttributeID, contentSubmissionSharedBusinessEntitiesContentSubmissionAttribute);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentSubmissionsApi#contentSubmissionsPutContentSubmissionAttributeAsync");
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
| **contentSubmissionAttributeID** | **Integer**| The ID of the Attribute to update. | |
| **contentSubmissionSharedBusinessEntitiesContentSubmissionAttribute** | [**ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute**](ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute.md)| The Attribute to update. | |

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

<a id="contentSubmissionsPutContentSubmissionAttributes"></a>
# **contentSubmissionsPutContentSubmissionAttributes**
> contentSubmissionsPutContentSubmissionAttributes(contentSubmissionSharedBusinessEntitiesContentSubmissionAttribute)

No Documentation Found.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentSubmissionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ContentSubmissionsApi apiInstance = new ContentSubmissionsApi(defaultClient);
    List<ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute> contentSubmissionSharedBusinessEntitiesContentSubmissionAttribute = Arrays.asList(); // List<ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute> | 
    try {
      apiInstance.contentSubmissionsPutContentSubmissionAttributes(contentSubmissionSharedBusinessEntitiesContentSubmissionAttribute);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentSubmissionsApi#contentSubmissionsPutContentSubmissionAttributes");
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
| **contentSubmissionSharedBusinessEntitiesContentSubmissionAttribute** | [**List&lt;ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute&gt;**](ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute.md)|  | |

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

