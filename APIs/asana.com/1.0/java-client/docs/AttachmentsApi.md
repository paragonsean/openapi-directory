# AttachmentsApi

All URIs are relative to *https://app.asana.com/api/1.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createAttachmentForObject**](AttachmentsApi.md#createAttachmentForObject) | **POST** /attachments | Upload an attachment |
| [**deleteAttachment**](AttachmentsApi.md#deleteAttachment) | **DELETE** /attachments/{attachment_gid} | Delete an attachment |
| [**getAttachment**](AttachmentsApi.md#getAttachment) | **GET** /attachments/{attachment_gid} | Get an attachment |
| [**getAttachmentsForObject**](AttachmentsApi.md#getAttachmentsForObject) | **GET** /attachments | Get attachments from an object |


<a id="createAttachmentForObject"></a>
# **createAttachmentForObject**
> CreateAttachmentForObject200Response createAttachmentForObject(optPretty, optFields, connectToApp, _file, name, parent, resourceSubtype, url)

Upload an attachment

Upload an attachment.  This method uploads an attachment on an object and returns the compact record for the created attachment object. This is possible by either:  - Providing the URL of the external resource being attached, or - Downloading the file content first and then uploading it as any other attachment. Note that it is not possible to attach files from third party services such as Dropbox, Box, Vimeo &amp; Google Drive via the API  The 100MB size limit on attachments in Asana is enforced on this endpoint.  This endpoint expects a multipart/form-data encoded request containing the full contents of the file to be uploaded.  Requests made should follow the HTTP/1.1 specification that line terminators are of the form &#x60;CRLF&#x60; or &#x60;\\r\\n&#x60; outlined [here](http://www.w3.org/Protocols/HTTP/1.1/draft-ietf-http-v11-spec-01#Basic-Rules) in order for the server to reliably and properly handle the request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttachmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.asana.com/api/1.0");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AttachmentsApi apiInstance = new AttachmentsApi(defaultClient);
    Boolean optPretty = true; // Boolean | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    List<String> optFields = Arrays.asList(); // List<String> | Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    Boolean connectToApp = true; // Boolean | *Optional*. Only relevant for external attachments with a parent task. A boolean indicating whether the current app should be connected with the attachment for the purposes of showing an app components widget. Requires the app to have been added to a project the parent task is in. 
    File _file = new File("/path/to/file"); // File | Required for `asana` attachments. 
    String name = "name_example"; // String | The name of the external resource being attached. Required for attachments of type `external`. 
    String parent = "parent_example"; // String | Required identifier of the parent task, project, or project_brief, as a string. 
    String resourceSubtype = "asana"; // String | The type of the attachment. Must be one of the given values. If not specified, a file attachment of type `asana` will be assumed. Note that if the value of `resource_subtype` is `external`, a `parent`, `name`, and `url` must also be provided. 
    String url = "url_example"; // String | The URL of the external resource being attached. Required for attachments of type `external`. 
    try {
      CreateAttachmentForObject200Response result = apiInstance.createAttachmentForObject(optPretty, optFields, connectToApp, _file, name, parent, resourceSubtype, url);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttachmentsApi#createAttachmentForObject");
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
| **optPretty** | **Boolean**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] |
| **optFields** | [**List&lt;String&gt;**](String.md)| Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options. | [optional] |
| **connectToApp** | **Boolean**| *Optional*. Only relevant for external attachments with a parent task. A boolean indicating whether the current app should be connected with the attachment for the purposes of showing an app components widget. Requires the app to have been added to a project the parent task is in.  | [optional] |
| **_file** | **File**| Required for &#x60;asana&#x60; attachments.  | [optional] |
| **name** | **String**| The name of the external resource being attached. Required for attachments of type &#x60;external&#x60;.  | [optional] |
| **parent** | **String**| Required identifier of the parent task, project, or project_brief, as a string.  | [optional] |
| **resourceSubtype** | **String**| The type of the attachment. Must be one of the given values. If not specified, a file attachment of type &#x60;asana&#x60; will be assumed. Note that if the value of &#x60;resource_subtype&#x60; is &#x60;external&#x60;, a &#x60;parent&#x60;, &#x60;name&#x60;, and &#x60;url&#x60; must also be provided.  | [optional] [enum: asana, dropbox, gdrive, onedrive, box, vimeo, external] |
| **url** | **String**| The URL of the external resource being attached. Required for attachments of type &#x60;external&#x60;.  | [optional] |

### Return type

[**CreateAttachmentForObject200Response**](CreateAttachmentForObject200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully uploaded the attachment to the parent object. |  -  |
| **400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
| **401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
| **403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
| **404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
| **500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

<a id="deleteAttachment"></a>
# **deleteAttachment**
> DeleteAttachment200Response deleteAttachment(attachmentGid, optPretty, optFields)

Delete an attachment

Deletes a specific, existing attachment.  Returns an empty data record.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttachmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.asana.com/api/1.0");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AttachmentsApi apiInstance = new AttachmentsApi(defaultClient);
    String attachmentGid = "12345"; // String | Globally unique identifier for the attachment.
    Boolean optPretty = true; // Boolean | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    List<String> optFields = Arrays.asList(); // List<String> | Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    try {
      DeleteAttachment200Response result = apiInstance.deleteAttachment(attachmentGid, optPretty, optFields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttachmentsApi#deleteAttachment");
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
| **attachmentGid** | **String**| Globally unique identifier for the attachment. | |
| **optPretty** | **Boolean**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] |
| **optFields** | [**List&lt;String&gt;**](String.md)| Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options. | [optional] |

### Return type

[**DeleteAttachment200Response**](DeleteAttachment200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully deleted the specified attachment. |  -  |
| **400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
| **401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
| **403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
| **404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
| **500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

<a id="getAttachment"></a>
# **getAttachment**
> CreateAttachmentForObject200Response getAttachment(attachmentGid, optPretty, optFields)

Get an attachment

Get the full record for a single attachment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttachmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.asana.com/api/1.0");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AttachmentsApi apiInstance = new AttachmentsApi(defaultClient);
    String attachmentGid = "12345"; // String | Globally unique identifier for the attachment.
    Boolean optPretty = true; // Boolean | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    List<String> optFields = Arrays.asList(); // List<String> | Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    try {
      CreateAttachmentForObject200Response result = apiInstance.getAttachment(attachmentGid, optPretty, optFields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttachmentsApi#getAttachment");
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
| **attachmentGid** | **String**| Globally unique identifier for the attachment. | |
| **optPretty** | **Boolean**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] |
| **optFields** | [**List&lt;String&gt;**](String.md)| Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options. | [optional] |

### Return type

[**CreateAttachmentForObject200Response**](CreateAttachmentForObject200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the record for a single attachment. |  -  |
| **400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
| **401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
| **402** | The request was valid, but the queried object or object mutation specified in the request is above your current premium level. |  -  |
| **403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
| **404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
| **424** | You have exceeded one of the enforced rate limits in the API. See the [documentation on rate limiting](https://developers.asana.com/docs/#rate-limits) for more information. |  -  |
| **500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |
| **501** | There is an issue between the load balancers and Asana&#39;s API. |  -  |
| **503** | Either the upstream service is unavailable to the API, or the API has been intentionally shut off. |  -  |
| **504** | This request took too long to complete. |  -  |

<a id="getAttachmentsForObject"></a>
# **getAttachmentsForObject**
> GetAttachmentsForObject200Response getAttachmentsForObject(parent, optPretty, optFields, limit, offset)

Get attachments from an object

Returns the compact records for all attachments on the object.  There are three possible &#x60;parent&#x60; values for this request: &#x60;project&#x60;, &#x60;project_brief&#x60;, and &#x60;task&#x60;. For a project, an attachment refers to a file uploaded to the \&quot;Key resources\&quot; section in the project Overview. For a project brief, an attachment refers to inline files in the project brief itself. For a task, an attachment refers to a file directly associated to that task.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttachmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.asana.com/api/1.0");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AttachmentsApi apiInstance = new AttachmentsApi(defaultClient);
    String parent = "159874"; // String | Globally unique identifier for object to fetch statuses from. Must be a GID for a `project`, `project_brief`, or `task`.
    Boolean optPretty = true; // Boolean | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    List<String> optFields = Arrays.asList(); // List<String> | Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    Integer limit = 50; // Integer | Results per page. The number of objects to return per page. The value must be between 1 and 100.
    String offset = "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9"; // String | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
    try {
      GetAttachmentsForObject200Response result = apiInstance.getAttachmentsForObject(parent, optPretty, optFields, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttachmentsApi#getAttachmentsForObject");
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
| **parent** | **String**| Globally unique identifier for object to fetch statuses from. Must be a GID for a &#x60;project&#x60;, &#x60;project_brief&#x60;, or &#x60;task&#x60;. | |
| **optPretty** | **Boolean**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] |
| **optFields** | [**List&lt;String&gt;**](String.md)| Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options. | [optional] |
| **limit** | **Integer**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] |
| **offset** | **String**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#39;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#39; | [optional] |

### Return type

[**GetAttachmentsForObject200Response**](GetAttachmentsForObject200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the specified object&#39;s attachments. |  -  |
| **400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
| **401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
| **403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
| **404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
| **500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

