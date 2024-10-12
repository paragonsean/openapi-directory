# SitesApi

All URIs are relative to *https://watchful.li/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addSiteToBackupQueue**](SitesApi.md#addSiteToBackupQueue) | **POST** /sites/{id}/backupnow | Add the site to the backup queue |
| [**createAudits**](SitesApi.md#createAudits) | **POST** /sites/{id}/audits | Create an audit for the site |
| [**createLog**](SitesApi.md#createLog) | **POST** /sites/{id}/logs | Create a custom log for a specific website |
| [**createSite**](SitesApi.md#createSite) | **POST** /sites | Create a site |
| [**deleteMonitor**](SitesApi.md#deleteMonitor) | **DELETE** /sites/{id}/monitor | Delete uptime monitor |
| [**getBackupProfiles**](SitesApi.md#getBackupProfiles) | **GET** /sites/{id}/backupprofiles | Return backup profile |
| [**getListBackups**](SitesApi.md#getListBackups) | **GET** /sites/{id}/backups | List of latest backups |
| [**getSiteAudits**](SitesApi.md#getSiteAudits) | **GET** /sites/{id}/audits | Return audits for a specific website |
| [**getSiteById**](SitesApi.md#getSiteById) | **GET** /sites/{id} | Find sites by ID |
| [**getSites**](SitesApi.md#getSites) | **GET** /sites | Get a list of Sites |
| [**getUptime**](SitesApi.md#getUptime) | **GET** /sites/{id}/uptime | Return uptime data |
| [**installExtension**](SitesApi.md#installExtension) | **POST** /sites/{id}/extensions | Install extension |
| [**postMonitor**](SitesApi.md#postMonitor) | **POST** /sites/{id}/monitor | Post uptime monitor |
| [**postTags**](SitesApi.md#postTags) | **POST** /sites/{id}/tags | Add tags for a specific website |
| [**scanner**](SitesApi.md#scanner) | **GET** /sites/{id}/scanner | Scan the site for malware |
| [**seoAnalyze**](SitesApi.md#seoAnalyze) | **GET** /sites/{id}/seo | SEO analyze for a page |
| [**sitesIdDelete**](SitesApi.md#sitesIdDelete) | **DELETE** /sites/{id} | Delete a specific Site |
| [**sitesIdExtensionsGet**](SitesApi.md#sitesIdExtensionsGet) | **GET** /sites/{id}/extensions | Get extensions for a site |
| [**sitesIdLogsGet**](SitesApi.md#sitesIdLogsGet) | **GET** /sites/{id}/logs | Return logs for a specific website |
| [**sitesIdPut**](SitesApi.md#sitesIdPut) | **PUT** /sites/{id} | Update a site |
| [**sitesIdTagsGet**](SitesApi.md#sitesIdTagsGet) | **GET** /sites/{id}/tags | Return tags for a specific website |
| [**sitesMetadataGet**](SitesApi.md#sitesMetadataGet) | **GET** /sites/metadata | Get the list of fields |
| [**startSiteBackup**](SitesApi.md#startSiteBackup) | **POST** /sites/{id}/backupstart | Start a remote backup for the site |
| [**stepSiteBackup**](SitesApi.md#stepSiteBackup) | **POST** /sites/{id}/backupstep | Step (continue) a remote backup for the site |
| [**updateJoomla**](SitesApi.md#updateJoomla) | **POST** /sites/{id}/updatejoomla | Update Joomla core on the remote site |
| [**validateDebugSite**](SitesApi.md#validateDebugSite) | **GET** /sites/{id}/validatedebug | validate the site, return the debug information |
| [**validateSite**](SitesApi.md#validateSite) | **GET** /sites/{id}/validate | validate the site, return the new logs |


<a id="addSiteToBackupQueue"></a>
# **addSiteToBackupQueue**
> Site addSiteToBackupQueue(id)

Add the site to the backup queue

Add the site to the backup queue

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://watchful.li/api/v1");

    SitesApi apiInstance = new SitesApi(defaultClient);
    Long id = 56L; // Long | ID of the website
    try {
      Site result = apiInstance.addSiteToBackupQueue(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#addSiteToBackupQueue");
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
| **id** | **Long**| ID of the website | |

### Return type

[**Site**](Site.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **403** | Invalid API Key |  -  |
| **404** | Invalid ID |  -  |

<a id="createAudits"></a>
# **createAudits**
> Audit createAudits(id)

Create an audit for the site

Create an audit for the site

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://watchful.li/api/v1");

    SitesApi apiInstance = new SitesApi(defaultClient);
    Long id = 56L; // Long | ID of the website
    try {
      Audit result = apiInstance.createAudits(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#createAudits");
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
| **id** | **Long**| ID of the website | |

### Return type

[**Audit**](Audit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **201** | Saved successfully |  -  |
| **400** | Invalid data |  -  |
| **403** | Invalid API Key |  -  |
| **404** | Not saved |  -  |

<a id="createLog"></a>
# **createLog**
> Log createLog(id, body)

Create a custom log for a specific website

Create a custom log for a specific website

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://watchful.li/api/v1");

    SitesApi apiInstance = new SitesApi(defaultClient);
    Long id = 56L; // Long | ID of the website
    PostLog body = new PostLog(); // PostLog | JSON object Log (only type custom)
    try {
      Log result = apiInstance.createLog(id, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#createLog");
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
| **id** | **Long**| ID of the website | |
| **body** | [**PostLog**](PostLog.md)| JSON object Log (only type custom) | |

### Return type

[**Log**](Log.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **201** | Saved successfully |  -  |
| **400** | Invalid data |  -  |
| **403** | Invalid API Key |  -  |
| **404** | Not saved |  -  |

<a id="createSite"></a>
# **createSite**
> Site createSite(body)

Create a site

Create a site

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://watchful.li/api/v1");

    SitesApi apiInstance = new SitesApi(defaultClient);
    PostSite body = new PostSite(); // PostSite | JSON object Site
    try {
      Site result = apiInstance.createSite(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#createSite");
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
| **body** | [**PostSite**](PostSite.md)| JSON object Site | |

### Return type

[**Site**](Site.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **201** | Saved successfully |  -  |
| **400** | Invalid data |  -  |
| **403** | Not allowed to add sites |  -  |
| **404** | Not saved |  -  |

<a id="deleteMonitor"></a>
# **deleteMonitor**
> Object deleteMonitor(id)

Delete uptime monitor

Return boolean

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://watchful.li/api/v1");

    SitesApi apiInstance = new SitesApi(defaultClient);
    Long id = 56L; // Long | ID of the website
    try {
      Object result = apiInstance.deleteMonitor(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#deleteMonitor");
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
| **id** | **Long**| ID of the website | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **403** | Invalid API Key |  -  |
| **404** | Invalid ID |  -  |

<a id="getBackupProfiles"></a>
# **getBackupProfiles**
> getBackupProfiles(id)

Return backup profile

Return backup profile

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://watchful.li/api/v1");

    SitesApi apiInstance = new SitesApi(defaultClient);
    Long id = 56L; // Long | ID of the website
    try {
      apiInstance.getBackupProfiles(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#getBackupProfiles");
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
| **id** | **Long**| ID of the website | |

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
| **200** | No response was specified |  -  |
| **403** | Invalid API Key |  -  |
| **404** | Invalid ID |  -  |

<a id="getListBackups"></a>
# **getListBackups**
> getListBackups(id)

List of latest backups

List of latest backups

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://watchful.li/api/v1");

    SitesApi apiInstance = new SitesApi(defaultClient);
    Long id = 56L; // Long | ID of the website
    try {
      apiInstance.getListBackups(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#getListBackups");
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
| **id** | **Long**| ID of the website | |

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
| **200** | No response was specified |  -  |
| **403** | Invalid API Key |  -  |
| **404** | Invalid ID |  -  |

<a id="getSiteAudits"></a>
# **getSiteAudits**
> List&lt;Audit&gt; getSiteAudits(id, fields, limit, limitstart, order)

Return audits for a specific website

Return audits for a specific website

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://watchful.li/api/v1");

    SitesApi apiInstance = new SitesApi(defaultClient);
    Long id = 56L; // Long | ID of the website
    String fields = "fields_example"; // String | Fields to return separate by comas: name,id
    Long limit = 56L; // Long | Number of object to return (max 100, default 25)
    Long limitstart = 56L; // Long | Start of the return (default 0)
    String order = "order_example"; // String | ORDER by this field
    try {
      List<Audit> result = apiInstance.getSiteAudits(id, fields, limit, limitstart, order);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#getSiteAudits");
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
| **id** | **Long**| ID of the website | |
| **fields** | **String**| Fields to return separate by comas: name,id | [optional] |
| **limit** | **Long**| Number of object to return (max 100, default 25) | [optional] |
| **limitstart** | **Long**| Start of the return (default 0) | [optional] |
| **order** | **String**| ORDER by this field | [optional] |

### Return type

[**List&lt;Audit&gt;**](Audit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **403** | Invalid API Key |  -  |
| **404** | Invalid ID |  -  |

<a id="getSiteById"></a>
# **getSiteById**
> Site getSiteById(id, fields)

Find sites by ID

Return a site based on ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://watchful.li/api/v1");

    SitesApi apiInstance = new SitesApi(defaultClient);
    Long id = 56L; // Long | ID that needs to be fetched
    String fields = "fields_example"; // String | Fields to return separate by comas: name,id
    try {
      Site result = apiInstance.getSiteById(id, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#getSiteById");
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
| **id** | **Long**| ID that needs to be fetched | |
| **fields** | **String**| Fields to return separate by comas: name,id | [optional] |

### Return type

[**Site**](Site.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **403** | Invalid API Key |  -  |
| **404** | Invalid ID |  -  |

<a id="getSites"></a>
# **getSites**
> Site getSites(siteids, name, accessUrl, jVersion, ip, jUpdate, canUpdate, published, error, nbUpdates, up, fields, limit, limitstart, order)

Get a list of Sites

Returns a list of Sites

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://watchful.li/api/v1");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String siteids = "siteids_example"; // String | List of sites id separated by comma
    String name = "name_example"; // String | Site name. Do a 'LIKE' search, you can also use '%'
    String accessUrl = "accessUrl_example"; // String | Access URL. Do a 'LIKE' search, you can also use '%'
    String jVersion = "jVersion_example"; // String | Joomla version. Do a 'LIKE' search, you can also use '%'
    String ip = "ip_example"; // String | Ip address. Do a 'LIKE' search, you can also use '%'
    Integer jUpdate = 1; // Integer | Joomla core update status (1: update required, 0: update not required)
    Integer canUpdate = 1; // Integer | canUpdate
    Integer published = 1; // Integer | Is published
    String error = "error_example"; // String | Has errors
    String nbUpdates = "nbUpdates_example"; // String | 
    Integer up = 1; // Integer | Is online
    String fields = "fields_example"; // String | Fields to return separated by commas (e.g. name,id)
    Long limit = 56L; // Long | Number of objects to return (max 100, default 25)
    Long limitstart = 56L; // Long | Start of the return (default 0)
    String order = "order_example"; // String | ORDER by this field separete by comas. Add + / - after field for set ASC / DESC: type+,name-
    try {
      Site result = apiInstance.getSites(siteids, name, accessUrl, jVersion, ip, jUpdate, canUpdate, published, error, nbUpdates, up, fields, limit, limitstart, order);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#getSites");
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
| **siteids** | **String**| List of sites id separated by comma | [optional] |
| **name** | **String**| Site name. Do a &#39;LIKE&#39; search, you can also use &#39;%&#39; | [optional] |
| **accessUrl** | **String**| Access URL. Do a &#39;LIKE&#39; search, you can also use &#39;%&#39; | [optional] |
| **jVersion** | **String**| Joomla version. Do a &#39;LIKE&#39; search, you can also use &#39;%&#39; | [optional] |
| **ip** | **String**| Ip address. Do a &#39;LIKE&#39; search, you can also use &#39;%&#39; | [optional] |
| **jUpdate** | **Integer**| Joomla core update status (1: update required, 0: update not required) | [optional] [enum: 1, 0] |
| **canUpdate** | **Integer**| canUpdate | [optional] [enum: 1, 0] |
| **published** | **Integer**| Is published | [optional] [enum: 1, 0] |
| **error** | **String**| Has errors | [optional] |
| **nbUpdates** | **String**|  | [optional] |
| **up** | **Integer**| Is online | [optional] [enum: 1, 0] |
| **fields** | **String**| Fields to return separated by commas (e.g. name,id) | [optional] |
| **limit** | **Long**| Number of objects to return (max 100, default 25) | [optional] |
| **limitstart** | **Long**| Start of the return (default 0) | [optional] |
| **order** | **String**| ORDER by this field separete by comas. Add + / - after field for set ASC / DESC: type+,name- | [optional] |

### Return type

[**Site**](Site.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **403** | Invalid API Key |  -  |
| **404** | Invalid ID |  -  |

<a id="getUptime"></a>
# **getUptime**
> Object getUptime(id)

Return uptime data

Return uptime data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://watchful.li/api/v1");

    SitesApi apiInstance = new SitesApi(defaultClient);
    Long id = 56L; // Long | ID of the website
    try {
      Object result = apiInstance.getUptime(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#getUptime");
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
| **id** | **Long**| ID of the website | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **403** | Invalid API Key |  -  |
| **404** | Invalid ID |  -  |

<a id="installExtension"></a>
# **installExtension**
> installExtension(id, url)

Install extension

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://watchful.li/api/v1");

    SitesApi apiInstance = new SitesApi(defaultClient);
    Long id = 56L; // Long | ID of the website
    String url = "url_example"; // String | URL to install the extension from
    try {
      apiInstance.installExtension(id, url);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#installExtension");
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
| **id** | **Long**| ID of the website | |
| **url** | **String**| URL to install the extension from | |

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
| **200** | No response was specified |  -  |
| **403** | Invalid API Key |  -  |
| **404** | Invalid ID |  -  |

<a id="postMonitor"></a>
# **postMonitor**
> Object postMonitor(id)

Post uptime monitor

Return boolean

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://watchful.li/api/v1");

    SitesApi apiInstance = new SitesApi(defaultClient);
    Long id = 56L; // Long | ID of the website
    try {
      Object result = apiInstance.postMonitor(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#postMonitor");
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
| **id** | **Long**| ID of the website | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **403** | Invalid API Key |  -  |
| **404** | Invalid ID |  -  |

<a id="postTags"></a>
# **postTags**
> Site postTags(id, body)

Add tags for a specific website

Add tags for a specific website

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://watchful.li/api/v1");

    SitesApi apiInstance = new SitesApi(defaultClient);
    Long id = 56L; // Long | ID of the website
    Tag body = new Tag(); // Tag | JSON object Tag
    try {
      Site result = apiInstance.postTags(id, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#postTags");
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
| **id** | **Long**| ID of the website | |
| **body** | [**Tag**](Tag.md)| JSON object Tag | |

### Return type

[**Site**](Site.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **201** | Saved successfully |  -  |
| **403** | Invalid API Key |  -  |
| **404** | Invalid ID |  -  |

<a id="scanner"></a>
# **scanner**
> String scanner(id)

Scan the site for malware

Scan the site for malware

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://watchful.li/api/v1");

    SitesApi apiInstance = new SitesApi(defaultClient);
    Long id = 56L; // Long | ID of the website
    try {
      String result = apiInstance.scanner(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#scanner");
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
| **id** | **Long**| ID of the website | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **403** | Invalid API Key |  -  |
| **404** | Invalid ID |  -  |

<a id="seoAnalyze"></a>
# **seoAnalyze**
> String seoAnalyze(id)

SEO analyze for a page

SEO analyze for a page

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://watchful.li/api/v1");

    SitesApi apiInstance = new SitesApi(defaultClient);
    Long id = 56L; // Long | ID of the website
    try {
      String result = apiInstance.seoAnalyze(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#seoAnalyze");
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
| **id** | **Long**| ID of the website | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **403** | Invalid API Key |  -  |
| **404** | Invalid ID |  -  |

<a id="sitesIdDelete"></a>
# **sitesIdDelete**
> String sitesIdDelete(id)

Delete a specific Site

Delete a specific Site

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://watchful.li/api/v1");

    SitesApi apiInstance = new SitesApi(defaultClient);
    Long id = 56L; // Long | ID of Site that needs to be deleted
    try {
      String result = apiInstance.sitesIdDelete(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesIdDelete");
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
| **id** | **Long**| ID of Site that needs to be deleted | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deleted successfully |  -  |
| **403** | Invalid API Key |  -  |
| **404** | Invalid ID |  -  |

<a id="sitesIdExtensionsGet"></a>
# **sitesIdExtensionsGet**
> Extension sitesIdExtensionsGet(id, fields, limit, limitstart, order)

Get extensions for a site

Get extensions for a site

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://watchful.li/api/v1");

    SitesApi apiInstance = new SitesApi(defaultClient);
    Long id = 56L; // Long | ID of the website
    String fields = "fields_example"; // String | Fields to return separate by comas: name,id
    Long limit = 56L; // Long | Number of object to return (max 100, default 25)
    Long limitstart = 56L; // Long | Start of the return (default 0)
    String order = "order_example"; // String | ORDER by this field
    try {
      Extension result = apiInstance.sitesIdExtensionsGet(id, fields, limit, limitstart, order);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesIdExtensionsGet");
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
| **id** | **Long**| ID of the website | |
| **fields** | **String**| Fields to return separate by comas: name,id | [optional] |
| **limit** | **Long**| Number of object to return (max 100, default 25) | [optional] |
| **limitstart** | **Long**| Start of the return (default 0) | [optional] |
| **order** | **String**| ORDER by this field | [optional] |

### Return type

[**Extension**](Extension.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **403** | Invalid API Key |  -  |
| **404** | Invalid |  -  |

<a id="sitesIdLogsGet"></a>
# **sitesIdLogsGet**
> Log sitesIdLogsGet(id, logEntry, logType, from, to, fields, limit, limitstart, order)

Return logs for a specific website

Return logs for a specific website

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://watchful.li/api/v1");

    SitesApi apiInstance = new SitesApi(defaultClient);
    Long id = 56L; // Long | ID of the website
    String logEntry = "logEntry_example"; // String | Do a 'LIKE' search, you can also use '%'
    String logType = ""; // String | Type of the log
    String from = "from_example"; // String | Logs after this date, format YYYY-MM-DD HH:MM:SS
    String to = "to_example"; // String | Logs before this date, format YYYY-MM-DD HH:MM:SS
    String fields = "fields_example"; // String | Fields to return separate by comas: name,id
    Long limit = 56L; // Long | Number of object to return (max 100, default 25)
    Long limitstart = 56L; // Long | Start of the return (default 0)
    String order = "order_example"; // String | ORDER by this field separete by comas. Add + / - after field for set ASC / DESC: type+,name-
    try {
      Log result = apiInstance.sitesIdLogsGet(id, logEntry, logType, from, to, fields, limit, limitstart, order);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesIdLogsGet");
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
| **id** | **Long**| ID of the website | |
| **logEntry** | **String**| Do a &#39;LIKE&#39; search, you can also use &#39;%&#39; | [optional] |
| **logType** | **String**| Type of the log | [optional] [enum: , plugin_sends_error, curlerror, modified_file, word_not_in_homepage, file_not_exists, update_available, new_extension, deleted_extension, extension_not_saved, modified_value_files] |
| **from** | **String**| Logs after this date, format YYYY-MM-DD HH:MM:SS | [optional] |
| **to** | **String**| Logs before this date, format YYYY-MM-DD HH:MM:SS | [optional] |
| **fields** | **String**| Fields to return separate by comas: name,id | [optional] |
| **limit** | **Long**| Number of object to return (max 100, default 25) | [optional] |
| **limitstart** | **Long**| Start of the return (default 0) | [optional] |
| **order** | **String**| ORDER by this field separete by comas. Add + / - after field for set ASC / DESC: type+,name- | [optional] |

### Return type

[**Log**](Log.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **403** | Invalid API Key |  -  |
| **404** | Invalid ID |  -  |

<a id="sitesIdPut"></a>
# **sitesIdPut**
> Site sitesIdPut(id, body)

Update a site

Update a site

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://watchful.li/api/v1");

    SitesApi apiInstance = new SitesApi(defaultClient);
    Long id = 56L; // Long | ID of the website that needs to be update
    PostSite body = new PostSite(); // PostSite | JSON object Site
    try {
      Site result = apiInstance.sitesIdPut(id, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesIdPut");
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
| **id** | **Long**| ID of the website that needs to be update | |
| **body** | [**PostSite**](PostSite.md)| JSON object Site | |

### Return type

[**Site**](Site.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated successfully |  -  |
| **400** | Invalid data |  -  |
| **403** | Invalid API Key |  -  |
| **404** | Invalid ID |  -  |

<a id="sitesIdTagsGet"></a>
# **sitesIdTagsGet**
> Tag sitesIdTagsGet(id, name, type, fields, limit, limitstart, order)

Return tags for a specific website

Return tags for a specific website

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://watchful.li/api/v1");

    SitesApi apiInstance = new SitesApi(defaultClient);
    Long id = 56L; // Long | ID of the website
    String name = "name_example"; // String | Do a 'LIKE' search, you can also use '%'
    String type = ""; // String | Bootstrap color of the tag
    String fields = "fields_example"; // String | Fields to return separate by comas: name,id
    Long limit = 56L; // Long | Number of object to return (max 100, default 25)
    Long limitstart = 56L; // Long | Start of the return (default 0)
    String order = "order_example"; // String | ORDER by this field
    try {
      Tag result = apiInstance.sitesIdTagsGet(id, name, type, fields, limit, limitstart, order);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesIdTagsGet");
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
| **id** | **Long**| ID of the website | |
| **name** | **String**| Do a &#39;LIKE&#39; search, you can also use &#39;%&#39; | [optional] |
| **type** | **String**| Bootstrap color of the tag | [optional] [enum: , default, success, warning, important, info, inverse] |
| **fields** | **String**| Fields to return separate by comas: name,id | [optional] |
| **limit** | **Long**| Number of object to return (max 100, default 25) | [optional] |
| **limitstart** | **Long**| Start of the return (default 0) | [optional] |
| **order** | **String**| ORDER by this field | [optional] |

### Return type

[**Tag**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **403** | Invalid API Key |  -  |
| **404** | Invalid ID |  -  |

<a id="sitesMetadataGet"></a>
# **sitesMetadataGet**
> String sitesMetadataGet()

Get the list of fields

Returns a list of fields

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://watchful.li/api/v1");

    SitesApi apiInstance = new SitesApi(defaultClient);
    try {
      String result = apiInstance.sitesMetadataGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesMetadataGet");
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

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="startSiteBackup"></a>
# **startSiteBackup**
> Site startSiteBackup(id)

Start a remote backup for the site

Start a remote backup for the site

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://watchful.li/api/v1");

    SitesApi apiInstance = new SitesApi(defaultClient);
    Long id = 56L; // Long | ID of the website
    try {
      Site result = apiInstance.startSiteBackup(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#startSiteBackup");
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
| **id** | **Long**| ID of the website | |

### Return type

[**Site**](Site.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **403** | Invalid API Key |  -  |
| **404** | Invalid ID |  -  |

<a id="stepSiteBackup"></a>
# **stepSiteBackup**
> Site stepSiteBackup(id)

Step (continue) a remote backup for the site

Step (continue) a remote backup for the site

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://watchful.li/api/v1");

    SitesApi apiInstance = new SitesApi(defaultClient);
    Long id = 56L; // Long | ID of the website
    try {
      Site result = apiInstance.stepSiteBackup(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#stepSiteBackup");
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
| **id** | **Long**| ID of the website | |

### Return type

[**Site**](Site.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **403** | Invalid API Key |  -  |
| **404** | Invalid ID |  -  |

<a id="updateJoomla"></a>
# **updateJoomla**
> String updateJoomla(id)

Update Joomla core on the remote site

Update Joomla core on the remote site

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://watchful.li/api/v1");

    SitesApi apiInstance = new SitesApi(defaultClient);
    Long id = 56L; // Long | ID of the website
    try {
      String result = apiInstance.updateJoomla(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#updateJoomla");
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
| **id** | **Long**| ID of the website | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Joomla core successfully updated |  -  |
| **403** | Invalid API Key |  -  |
| **404** | Invalid ID or Joomla Update not found |  -  |

<a id="validateDebugSite"></a>
# **validateDebugSite**
> Log validateDebugSite(id)

validate the site, return the debug information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://watchful.li/api/v1");

    SitesApi apiInstance = new SitesApi(defaultClient);
    Long id = 56L; // Long | ID of the website
    try {
      Log result = apiInstance.validateDebugSite(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#validateDebugSite");
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
| **id** | **Long**| ID of the website | |

### Return type

[**Log**](Log.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **403** | Invalid API Key |  -  |
| **404** | Invalid ID |  -  |

<a id="validateSite"></a>
# **validateSite**
> Log validateSite(id)

validate the site, return the new logs

validate the site

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://watchful.li/api/v1");

    SitesApi apiInstance = new SitesApi(defaultClient);
    Long id = 56L; // Long | ID of the website
    try {
      Log result = apiInstance.validateSite(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#validateSite");
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
| **id** | **Long**| ID of the website | |

### Return type

[**Log**](Log.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **403** | Invalid API Key |  -  |
| **404** | Invalid ID |  -  |

