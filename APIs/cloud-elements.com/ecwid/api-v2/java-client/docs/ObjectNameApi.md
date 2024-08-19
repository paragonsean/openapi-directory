# ObjectNameApi

All URIs are relative to *https://api.cloud-elements.com/elements/api-v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createByObjectName**](ObjectNameApi.md#createByObjectName) | **POST** /{objectName} | Create an {objectName} |
| [**createObjectNameByChildObjectName**](ObjectNameApi.md#createObjectNameByChildObjectName) | **POST** /{objectName}/{objectId}/{childObjectName} | Create an {objectName} |
| [**deleteObjectNameByChildObjectId**](ObjectNameApi.md#deleteObjectNameByChildObjectId) | **DELETE** /{objectName}/{objectId}/{childObjectName}/{childObjectId} | Delete an {childObjectName} |
| [**deleteObjectNameByObjectId**](ObjectNameApi.md#deleteObjectNameByObjectId) | **DELETE** /{objectName}/{objectId} | Delete an {objectName} |
| [**getByObjectName**](ObjectNameApi.md#getByObjectName) | **GET** /{objectName} | Search for {objectName} |
| [**getObjectNameByChildObjectId**](ObjectNameApi.md#getObjectNameByChildObjectId) | **GET** /{objectName}/{objectId}/{childObjectName}/{childObjectId} | Retrieve an {childObjectName} |
| [**getObjectNameByChildObjectName**](ObjectNameApi.md#getObjectNameByChildObjectName) | **GET** /{objectName}/{objectId}/{childObjectName} | Search for {childObjectName} |
| [**getObjectNameByObjectId**](ObjectNameApi.md#getObjectNameByObjectId) | **GET** /{objectName}/{objectId} | Retrieve an {objectName} |
| [**replaceObjectNameByChildObjectId**](ObjectNameApi.md#replaceObjectNameByChildObjectId) | **PUT** /{objectName}/{objectId}/{childObjectName}/{childObjectId} | Update an {childObjectName} |
| [**replaceObjectNameByObjectId**](ObjectNameApi.md#replaceObjectNameByObjectId) | **PUT** /{objectName}/{objectId} | Update an {objectName} |
| [**updateObjectNameByChildObjectId**](ObjectNameApi.md#updateObjectNameByChildObjectId) | **PATCH** /{objectName}/{objectId}/{childObjectName}/{childObjectId} | Update an {childObjectName} |
| [**updateObjectNameByObjectId**](ObjectNameApi.md#updateObjectNameByObjectId) | **PATCH** /{objectName}/{objectId} | Update an {objectName} |


<a id="createByObjectName"></a>
# **createByObjectName**
> createByObjectName(authorization, objectName, body)

Create an {objectName}

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObjectNameApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.cloud-elements.com/elements/api-v2");

    ObjectNameApi apiInstance = new ObjectNameApi(defaultClient);
    String authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
    String objectName = "objectName_example"; // String | The name of the object
    ModelObject body = new ModelObject(); // ModelObject | The {objectName}
    try {
      apiInstance.createByObjectName(authorization, objectName, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectNameApi#createByObjectName");
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
| **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | |
| **objectName** | **String**| The name of the object | |
| **body** | [**ModelObject**](ModelObject.md)| The {objectName} | |

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
| **200** | OK - Everything worked as expected |  -  |
| **400** | Bad Request - Often due to a missing request parameter |  -  |
| **401** | Unauthorized - An invalid element token, user secret and/or org secret provided |  -  |
| **403** | Forbidden - Access to the resource by the provider is forbidden |  -  |
| **404** | Not found - The requested resource is not found |  -  |
| **405** | Method not allowed - Incorrect HTTP verb used, e.g., GET used when POST expected |  -  |
| **406** | Not acceptable - The response content type does not match the &#39;Accept&#39; header value |  -  |
| **409** | Conflict - If a resource being created already exists |  -  |
| **415** | Unsupported media type - The server cannot handle the requested Content-Type |  -  |
| **500** | Server error - Something went wrong on the Cloud Elements server |  -  |
| **502** | Provider server error - Something went wrong on the Provider or Endpoint&#39;s server |  -  |

<a id="createObjectNameByChildObjectName"></a>
# **createObjectNameByChildObjectName**
> createObjectNameByChildObjectName(authorization, objectName, objectId, childObjectName, body)

Create an {objectName}

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObjectNameApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.cloud-elements.com/elements/api-v2");

    ObjectNameApi apiInstance = new ObjectNameApi(defaultClient);
    String authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
    String objectName = "objectName_example"; // String | The name of the object
    String objectId = "objectId_example"; // String | The {objectName} ID
    String childObjectName = "childObjectName_example"; // String | The name of the object
    ModelObject body = new ModelObject(); // ModelObject | The {childObjectName}
    try {
      apiInstance.createObjectNameByChildObjectName(authorization, objectName, objectId, childObjectName, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectNameApi#createObjectNameByChildObjectName");
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
| **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | |
| **objectName** | **String**| The name of the object | |
| **objectId** | **String**| The {objectName} ID | |
| **childObjectName** | **String**| The name of the object | |
| **body** | [**ModelObject**](ModelObject.md)| The {childObjectName} | |

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
| **200** | OK - Everything worked as expected |  -  |
| **400** | Bad Request - Often due to a missing request parameter |  -  |
| **401** | Unauthorized - An invalid element token, user secret and/or org secret provided |  -  |
| **403** | Forbidden - Access to the resource by the provider is forbidden |  -  |
| **404** | Not found - The requested resource is not found |  -  |
| **405** | Method not allowed - Incorrect HTTP verb used, e.g., GET used when POST expected |  -  |
| **406** | Not acceptable - The response content type does not match the &amp;quot;Accept&amp;quot; header value |  -  |
| **409** | Conflict - If a resource being created already exists |  -  |
| **415** | Unsupported media type - The server cannot handle the requested Content-Type |  -  |
| **500** | Server error - Something went wrong on the Cloud Elements server |  -  |
| **502** | Provider server error - Something went wrong on the Provider or Endpoint&#39;s server |  -  |

<a id="deleteObjectNameByChildObjectId"></a>
# **deleteObjectNameByChildObjectId**
> deleteObjectNameByChildObjectId(authorization, objectName, childObjectName, objectId, childObjectId)

Delete an {childObjectName}

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObjectNameApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.cloud-elements.com/elements/api-v2");

    ObjectNameApi apiInstance = new ObjectNameApi(defaultClient);
    String authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
    String objectName = "objectName_example"; // String | The name of the object
    String childObjectName = "childObjectName_example"; // String | The name of the childObjectName
    String objectId = "objectId_example"; // String | The {objectName} ID
    String childObjectId = "childObjectId_example"; // String | The {childObjectName} ID
    try {
      apiInstance.deleteObjectNameByChildObjectId(authorization, objectName, childObjectName, objectId, childObjectId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectNameApi#deleteObjectNameByChildObjectId");
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
| **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | |
| **objectName** | **String**| The name of the object | |
| **childObjectName** | **String**| The name of the childObjectName | |
| **objectId** | **String**| The {objectName} ID | |
| **childObjectId** | **String**| The {childObjectName} ID | |

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
| **200** | OK - Everything worked as expected |  -  |
| **400** | Bad Request - Often due to a missing request parameter |  -  |
| **401** | Unauthorized - An invalid element token, user secret and/or org secret provided |  -  |
| **403** | Forbidden - Access to the resource by the provider is forbidden |  -  |
| **404** | Not found - The requested resource is not found |  -  |
| **405** | Method not allowed - Incorrect HTTP verb used, e.g., GET used when POST expected |  -  |
| **406** | Not acceptable - The response content type does not match the &amp;quot;Accept&amp;quot; header value |  -  |
| **409** | Conflict - If a resource being created already exists |  -  |
| **415** | Unsupported media type - The server cannot handle the requested Content-Type |  -  |
| **500** | Server error - Something went wrong on the Cloud Elements server |  -  |
| **502** | Provider server error - Something went wrong on the Provider or Endpoint&#39;s server |  -  |

<a id="deleteObjectNameByObjectId"></a>
# **deleteObjectNameByObjectId**
> deleteObjectNameByObjectId(authorization, objectName, objectId)

Delete an {objectName}

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObjectNameApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.cloud-elements.com/elements/api-v2");

    ObjectNameApi apiInstance = new ObjectNameApi(defaultClient);
    String authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
    String objectName = "objectName_example"; // String | The name of the object
    String objectId = "objectId_example"; // String | The {objectName} ID
    try {
      apiInstance.deleteObjectNameByObjectId(authorization, objectName, objectId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectNameApi#deleteObjectNameByObjectId");
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
| **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | |
| **objectName** | **String**| The name of the object | |
| **objectId** | **String**| The {objectName} ID | |

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
| **200** | OK - Everything worked as expected |  -  |
| **400** | Bad Request - Often due to a missing request parameter |  -  |
| **401** | Unauthorized - An invalid element token, user secret and/or org secret provided |  -  |
| **403** | Forbidden - Access to the resource by the provider is forbidden |  -  |
| **404** | Not found - The requested resource is not found |  -  |
| **405** | Method not allowed - Incorrect HTTP verb used, e.g., GET used when POST expected |  -  |
| **406** | Not acceptable - The response content type does not match the &#39;Accept&#39; header value |  -  |
| **409** | Conflict - If a resource being created already exists |  -  |
| **415** | Unsupported media type - The server cannot handle the requested Content-Type |  -  |
| **500** | Server error - Something went wrong on the Cloud Elements server |  -  |
| **502** | Provider server error - Something went wrong on the Provider or Endpoint&#39;s server |  -  |

<a id="getByObjectName"></a>
# **getByObjectName**
> List&lt;ModelObject&gt; getByObjectName(authorization, objectName, where, pageSize, nextPage, fields)

Search for {objectName}

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObjectNameApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.cloud-elements.com/elements/api-v2");

    ObjectNameApi apiInstance = new ObjectNameApi(defaultClient);
    String authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
    String objectName = "objectName_example"; // String | The name of the object
    String where = "where_example"; // String | The CEQL search expression.
    Long pageSize = 56L; // Long | The page size. Defaults to 200 if not provided. Maximum of 5000.
    String nextPage = "nextPage_example"; // String | The next page cursor, taken from the response header: `elements-next-page-token`
    String fields = "fields_example"; // String | The fields to return on the response. Can be a single field or a comma-separated list of fields
    try {
      List<ModelObject> result = apiInstance.getByObjectName(authorization, objectName, where, pageSize, nextPage, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectNameApi#getByObjectName");
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
| **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | |
| **objectName** | **String**| The name of the object | |
| **where** | **String**| The CEQL search expression. | [optional] |
| **pageSize** | **Long**| The page size. Defaults to 200 if not provided. Maximum of 5000. | [optional] |
| **nextPage** | **String**| The next page cursor, taken from the response header: &#x60;elements-next-page-token&#x60; | [optional] |
| **fields** | **String**| The fields to return on the response. Can be a single field or a comma-separated list of fields | [optional] |

### Return type

[**List&lt;ModelObject&gt;**](ModelObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Everything worked as expected |  -  |
| **400** | Bad Request - Often due to a missing request parameter |  -  |
| **401** | Unauthorized - An invalid element token, user secret and/or org secret provided |  -  |
| **403** | Forbidden - Access to the resource by the provider is forbidden |  -  |
| **404** | Not found - The requested resource is not found |  -  |
| **405** | Method not allowed - Incorrect HTTP verb used, e.g., GET used when POST expected |  -  |
| **406** | Not acceptable - The response content type does not match the &#39;Accept&#39; header value |  -  |
| **409** | Conflict - If a resource being created already exists |  -  |
| **415** | Unsupported media type - The server cannot handle the requested Content-Type |  -  |
| **500** | Server error - Something went wrong on the Cloud Elements server |  -  |
| **502** | Provider server error - Something went wrong on the Provider or Endpoint&#39;s server |  -  |

<a id="getObjectNameByChildObjectId"></a>
# **getObjectNameByChildObjectId**
> ModelObject getObjectNameByChildObjectId(authorization, objectName, childObjectName, objectId, childObjectId)

Retrieve an {childObjectName}

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObjectNameApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.cloud-elements.com/elements/api-v2");

    ObjectNameApi apiInstance = new ObjectNameApi(defaultClient);
    String authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
    String objectName = "objectName_example"; // String | The name of the object
    String childObjectName = "childObjectName_example"; // String | The name of the childObjectName
    String objectId = "objectId_example"; // String | The {objectName} ID
    String childObjectId = "childObjectId_example"; // String | The {childObjectName} ID
    try {
      ModelObject result = apiInstance.getObjectNameByChildObjectId(authorization, objectName, childObjectName, objectId, childObjectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectNameApi#getObjectNameByChildObjectId");
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
| **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | |
| **objectName** | **String**| The name of the object | |
| **childObjectName** | **String**| The name of the childObjectName | |
| **objectId** | **String**| The {objectName} ID | |
| **childObjectId** | **String**| The {childObjectName} ID | |

### Return type

[**ModelObject**](ModelObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Everything worked as expected |  -  |
| **400** | Bad Request - Often due to a missing request parameter |  -  |
| **401** | Unauthorized - An invalid element token, user secret and/or org secret provided |  -  |
| **403** | Forbidden - Access to the resource by the provider is forbidden |  -  |
| **404** | Not found - The requested resource is not found |  -  |
| **405** | Method not allowed - Incorrect HTTP verb used, e.g., GET used when POST expected |  -  |
| **406** | Not acceptable - The response content type does not match the &amp;quot;Accept&amp;quot; header value |  -  |
| **409** | Conflict - If a resource being created already exists |  -  |
| **415** | Unsupported media type - The server cannot handle the requested Content-Type |  -  |
| **500** | Server error - Something went wrong on the Cloud Elements server |  -  |
| **502** | Provider server error - Something went wrong on the Provider or Endpoint&#39;s server |  -  |

<a id="getObjectNameByChildObjectName"></a>
# **getObjectNameByChildObjectName**
> List&lt;ModelObject&gt; getObjectNameByChildObjectName(authorization, objectName, objectId, childObjectName, where, pageSize, nextPage, fields)

Search for {childObjectName}

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObjectNameApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.cloud-elements.com/elements/api-v2");

    ObjectNameApi apiInstance = new ObjectNameApi(defaultClient);
    String authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
    String objectName = "objectName_example"; // String | The name of the object
    String objectId = "objectId_example"; // String | The {objectName} ID
    String childObjectName = "childObjectName_example"; // String | The name of the childObjectName
    String where = "where_example"; // String | The CEQL search expression.
    Long pageSize = 56L; // Long | The page size. Defaults to 200 if not provided. Maximum of 5000.
    String nextPage = "nextPage_example"; // String | The next page cursor, taken from the response header: `elements-next-page-token`
    String fields = "fields_example"; // String | The fields to return on the response. Can be a single field or a comma-separated list of fields
    try {
      List<ModelObject> result = apiInstance.getObjectNameByChildObjectName(authorization, objectName, objectId, childObjectName, where, pageSize, nextPage, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectNameApi#getObjectNameByChildObjectName");
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
| **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | |
| **objectName** | **String**| The name of the object | |
| **objectId** | **String**| The {objectName} ID | |
| **childObjectName** | **String**| The name of the childObjectName | |
| **where** | **String**| The CEQL search expression. | [optional] |
| **pageSize** | **Long**| The page size. Defaults to 200 if not provided. Maximum of 5000. | [optional] |
| **nextPage** | **String**| The next page cursor, taken from the response header: &#x60;elements-next-page-token&#x60; | [optional] |
| **fields** | **String**| The fields to return on the response. Can be a single field or a comma-separated list of fields | [optional] |

### Return type

[**List&lt;ModelObject&gt;**](ModelObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Everything worked as expected |  -  |
| **400** | Bad Request - Often due to a missing request parameter |  -  |
| **401** | Unauthorized - An invalid element token, user secret and/or org secret provided |  -  |
| **403** | Forbidden - Access to the resource by the provider is forbidden |  -  |
| **404** | Not found - The requested resource is not found |  -  |
| **405** | Method not allowed - Incorrect HTTP verb used, e.g., GET used when POST expected |  -  |
| **406** | Not acceptable - The response content type does not match the &amp;quot;Accept&amp;quot; header value |  -  |
| **409** | Conflict - If a resource being created already exists |  -  |
| **415** | Unsupported media type - The server cannot handle the requested Content-Type |  -  |
| **500** | Server error - Something went wrong on the Cloud Elements server |  -  |
| **502** | Provider server error - Something went wrong on the Provider or Endpoint&#39;s server |  -  |

<a id="getObjectNameByObjectId"></a>
# **getObjectNameByObjectId**
> ModelObject getObjectNameByObjectId(authorization, objectName, objectId)

Retrieve an {objectName}

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObjectNameApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.cloud-elements.com/elements/api-v2");

    ObjectNameApi apiInstance = new ObjectNameApi(defaultClient);
    String authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
    String objectName = "objectName_example"; // String | The name of the object
    String objectId = "objectId_example"; // String | The {objectName} ID
    try {
      ModelObject result = apiInstance.getObjectNameByObjectId(authorization, objectName, objectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectNameApi#getObjectNameByObjectId");
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
| **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | |
| **objectName** | **String**| The name of the object | |
| **objectId** | **String**| The {objectName} ID | |

### Return type

[**ModelObject**](ModelObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/pdf

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Everything worked as expected |  -  |
| **400** | Bad Request - Often due to a missing request parameter |  -  |
| **401** | Unauthorized - An invalid element token, user secret and/or org secret provided |  -  |
| **403** | Forbidden - Access to the resource by the provider is forbidden |  -  |
| **404** | Not found - The requested resource is not found |  -  |
| **405** | Method not allowed - Incorrect HTTP verb used, e.g., GET used when POST expected |  -  |
| **406** | Not acceptable - The response content type does not match the &#39;Accept&#39; header value |  -  |
| **409** | Conflict - If a resource being created already exists |  -  |
| **415** | Unsupported media type - The server cannot handle the requested Content-Type |  -  |
| **500** | Server error - Something went wrong on the Cloud Elements server |  -  |
| **502** | Provider server error - Something went wrong on the Provider or Endpoint&#39;s server |  -  |

<a id="replaceObjectNameByChildObjectId"></a>
# **replaceObjectNameByChildObjectId**
> ModelObject replaceObjectNameByChildObjectId(authorization, objectName, childObjectName, objectId, childObjectId, body)

Update an {childObjectName}

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObjectNameApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.cloud-elements.com/elements/api-v2");

    ObjectNameApi apiInstance = new ObjectNameApi(defaultClient);
    String authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
    String objectName = "objectName_example"; // String | The name of the object
    String childObjectName = "childObjectName_example"; // String | The name of the childObjectName
    String objectId = "objectId_example"; // String | The {objectName} ID
    String childObjectId = "childObjectId_example"; // String | The {childObjectName} ID
    ModelObject body = new ModelObject(); // ModelObject | The {objectName}
    try {
      ModelObject result = apiInstance.replaceObjectNameByChildObjectId(authorization, objectName, childObjectName, objectId, childObjectId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectNameApi#replaceObjectNameByChildObjectId");
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
| **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | |
| **objectName** | **String**| The name of the object | |
| **childObjectName** | **String**| The name of the childObjectName | |
| **objectId** | **String**| The {objectName} ID | |
| **childObjectId** | **String**| The {childObjectName} ID | |
| **body** | [**ModelObject**](ModelObject.md)| The {objectName} | |

### Return type

[**ModelObject**](ModelObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Everything worked as expected |  -  |
| **400** | Bad Request - Often due to a missing request parameter |  -  |
| **401** | Unauthorized - An invalid element token, user secret and/or org secret provided |  -  |
| **403** | Forbidden - Access to the resource by the provider is forbidden |  -  |
| **404** | Not found - The requested resource is not found |  -  |
| **405** | Method not allowed - Incorrect HTTP verb used, e.g., GET used when POST expected |  -  |
| **406** | Not acceptable - The response content type does not match the &amp;quot;Accept&amp;quot; header value |  -  |
| **409** | Conflict - If a resource being created already exists |  -  |
| **415** | Unsupported media type - The server cannot handle the requested Content-Type |  -  |
| **500** | Server error - Something went wrong on the Cloud Elements server |  -  |
| **502** | Provider server error - Something went wrong on the Provider or Endpoint&#39;s server |  -  |

<a id="replaceObjectNameByObjectId"></a>
# **replaceObjectNameByObjectId**
> ModelObject replaceObjectNameByObjectId(authorization, objectName, objectId, body)

Update an {objectName}

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObjectNameApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.cloud-elements.com/elements/api-v2");

    ObjectNameApi apiInstance = new ObjectNameApi(defaultClient);
    String authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
    String objectName = "objectName_example"; // String | The name of the object
    String objectId = "objectId_example"; // String | The {objectName} ID
    ModelObject body = new ModelObject(); // ModelObject | The {objectName}
    try {
      ModelObject result = apiInstance.replaceObjectNameByObjectId(authorization, objectName, objectId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectNameApi#replaceObjectNameByObjectId");
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
| **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | |
| **objectName** | **String**| The name of the object | |
| **objectId** | **String**| The {objectName} ID | |
| **body** | [**ModelObject**](ModelObject.md)| The {objectName} | |

### Return type

[**ModelObject**](ModelObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Everything worked as expected |  -  |
| **400** | Bad Request - Often due to a missing request parameter |  -  |
| **401** | Unauthorized - An invalid element token, user secret and/or org secret provided |  -  |
| **403** | Forbidden - Access to the resource by the provider is forbidden |  -  |
| **404** | Not found - The requested resource is not found |  -  |
| **405** | Method not allowed - Incorrect HTTP verb used, e.g., GET used when POST expected |  -  |
| **406** | Not acceptable - The response content type does not match the &#39;Accept&#39; header value |  -  |
| **409** | Conflict - If a resource being created already exists |  -  |
| **415** | Unsupported media type - The server cannot handle the requested Content-Type |  -  |
| **500** | Server error - Something went wrong on the Cloud Elements server |  -  |
| **502** | Provider server error - Something went wrong on the Provider or Endpoint&#39;s server |  -  |

<a id="updateObjectNameByChildObjectId"></a>
# **updateObjectNameByChildObjectId**
> ModelObject updateObjectNameByChildObjectId(authorization, objectName, childObjectName, objectId, childObjectId, body)

Update an {childObjectName}

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObjectNameApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.cloud-elements.com/elements/api-v2");

    ObjectNameApi apiInstance = new ObjectNameApi(defaultClient);
    String authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
    String objectName = "objectName_example"; // String | The name of the object
    String childObjectName = "childObjectName_example"; // String | The name of the childObjectName
    String objectId = "objectId_example"; // String | The {objectName} ID
    String childObjectId = "childObjectId_example"; // String | The {childObjectName} ID
    ModelObject body = new ModelObject(); // ModelObject | The {objectName}
    try {
      ModelObject result = apiInstance.updateObjectNameByChildObjectId(authorization, objectName, childObjectName, objectId, childObjectId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectNameApi#updateObjectNameByChildObjectId");
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
| **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | |
| **objectName** | **String**| The name of the object | |
| **childObjectName** | **String**| The name of the childObjectName | |
| **objectId** | **String**| The {objectName} ID | |
| **childObjectId** | **String**| The {childObjectName} ID | |
| **body** | [**ModelObject**](ModelObject.md)| The {objectName} | |

### Return type

[**ModelObject**](ModelObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Everything worked as expected |  -  |
| **400** | Bad Request - Often due to a missing request parameter |  -  |
| **401** | Unauthorized - An invalid element token, user secret and/or org secret provided |  -  |
| **403** | Forbidden - Access to the resource by the provider is forbidden |  -  |
| **404** | Not found - The requested resource is not found |  -  |
| **405** | Method not allowed - Incorrect HTTP verb used, e.g., GET used when POST expected |  -  |
| **406** | Not acceptable - The response content type does not match the &amp;quot;Accept&amp;quot; header value |  -  |
| **409** | Conflict - If a resource being created already exists |  -  |
| **415** | Unsupported media type - The server cannot handle the requested Content-Type |  -  |
| **500** | Server error - Something went wrong on the Cloud Elements server |  -  |
| **502** | Provider server error - Something went wrong on the Provider or Endpoint&#39;s server |  -  |

<a id="updateObjectNameByObjectId"></a>
# **updateObjectNameByObjectId**
> ModelObject updateObjectNameByObjectId(authorization, objectName, objectId, body)

Update an {objectName}

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObjectNameApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.cloud-elements.com/elements/api-v2");

    ObjectNameApi apiInstance = new ObjectNameApi(defaultClient);
    String authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
    String objectName = "objectName_example"; // String | The name of the object
    String objectId = "objectId_example"; // String | The {objectName} ID
    ModelObject body = new ModelObject(); // ModelObject | The {objectName}
    try {
      ModelObject result = apiInstance.updateObjectNameByObjectId(authorization, objectName, objectId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectNameApi#updateObjectNameByObjectId");
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
| **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | |
| **objectName** | **String**| The name of the object | |
| **objectId** | **String**| The {objectName} ID | |
| **body** | [**ModelObject**](ModelObject.md)| The {objectName} | |

### Return type

[**ModelObject**](ModelObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Everything worked as expected |  -  |
| **400** | Bad Request - Often due to a missing request parameter |  -  |
| **401** | Unauthorized - An invalid element token, user secret and/or org secret provided |  -  |
| **403** | Forbidden - Access to the resource by the provider is forbidden |  -  |
| **404** | Not found - The requested resource is not found |  -  |
| **405** | Method not allowed - Incorrect HTTP verb used, e.g., GET used when POST expected |  -  |
| **406** | Not acceptable - The response content type does not match the &#39;Accept&#39; header value |  -  |
| **409** | Conflict - If a resource being created already exists |  -  |
| **415** | Unsupported media type - The server cannot handle the requested Content-Type |  -  |
| **500** | Server error - Something went wrong on the Cloud Elements server |  -  |
| **502** | Provider server error - Something went wrong on the Provider or Endpoint&#39;s server |  -  |

