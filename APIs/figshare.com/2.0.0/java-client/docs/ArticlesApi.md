# ArticlesApi

All URIs are relative to *https://api.figshare.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**accountArticleReport**](ArticlesApi.md#accountArticleReport) | **GET** /account/articles/export | Account Article Report |
| [**accountArticleReportGenerate**](ArticlesApi.md#accountArticleReportGenerate) | **POST** /account/articles/export | Initiate a new Report |
| [**articleDetails**](ArticlesApi.md#articleDetails) | **GET** /articles/{article_id} | View article details |
| [**articleFileDetails**](ArticlesApi.md#articleFileDetails) | **GET** /articles/{article_id}/files/{file_id} | Article file details |
| [**articleFiles**](ArticlesApi.md#articleFiles) | **GET** /articles/{article_id}/files | List article files |
| [**articleVersionConfidentiality**](ArticlesApi.md#articleVersionConfidentiality) | **GET** /articles/{article_id}/versions/{v_number}/confidentiality | Public Article Confidentiality for article version |
| [**articleVersionDetails**](ArticlesApi.md#articleVersionDetails) | **GET** /articles/{article_id}/versions/{v_number} | Article details for version |
| [**articleVersionEmbargo**](ArticlesApi.md#articleVersionEmbargo) | **GET** /articles/{article_id}/versions/{v_number}/embargo | Public Article Embargo for article version |
| [**articleVersionUpdate**](ArticlesApi.md#articleVersionUpdate) | **PUT** /account/articles/{article_id}/versions/{version_id}/ | Update article version |
| [**articleVersionUpdateThumb**](ArticlesApi.md#articleVersionUpdateThumb) | **PUT** /account/articles/{article_id}/versions/{version_id}/update_thumb | Update article version thumbnail |
| [**articleVersions**](ArticlesApi.md#articleVersions) | **GET** /articles/{article_id}/versions | List article versions |
| [**articlesList**](ArticlesApi.md#articlesList) | **GET** /articles | Public Articles |
| [**articlesSearch**](ArticlesApi.md#articlesSearch) | **POST** /articles/search | Public Articles Search |
| [**privateArticleAuthorDelete**](ArticlesApi.md#privateArticleAuthorDelete) | **DELETE** /account/articles/{article_id}/authors/{author_id} | Delete article author |
| [**privateArticleAuthorsAdd**](ArticlesApi.md#privateArticleAuthorsAdd) | **POST** /account/articles/{article_id}/authors | Add article authors |
| [**privateArticleAuthorsList**](ArticlesApi.md#privateArticleAuthorsList) | **GET** /account/articles/{article_id}/authors | List article authors |
| [**privateArticleAuthorsReplace**](ArticlesApi.md#privateArticleAuthorsReplace) | **PUT** /account/articles/{article_id}/authors | Replace article authors |
| [**privateArticleCategoriesAdd**](ArticlesApi.md#privateArticleCategoriesAdd) | **POST** /account/articles/{article_id}/categories | Add article categories |
| [**privateArticleCategoriesList**](ArticlesApi.md#privateArticleCategoriesList) | **GET** /account/articles/{article_id}/categories | List article categories |
| [**privateArticleCategoriesReplace**](ArticlesApi.md#privateArticleCategoriesReplace) | **PUT** /account/articles/{article_id}/categories | Replace article categories |
| [**privateArticleCategoryDelete**](ArticlesApi.md#privateArticleCategoryDelete) | **DELETE** /account/articles/{article_id}/categories/{category_id} | Delete article category |
| [**privateArticleConfidentialityDelete**](ArticlesApi.md#privateArticleConfidentialityDelete) | **DELETE** /account/articles/{article_id}/confidentiality | Delete article confidentiality |
| [**privateArticleConfidentialityDetails**](ArticlesApi.md#privateArticleConfidentialityDetails) | **GET** /account/articles/{article_id}/confidentiality | Article confidentiality details |
| [**privateArticleConfidentialityUpdate**](ArticlesApi.md#privateArticleConfidentialityUpdate) | **PUT** /account/articles/{article_id}/confidentiality | Update article confidentiality |
| [**privateArticleCreate**](ArticlesApi.md#privateArticleCreate) | **POST** /account/articles | Create new Article |
| [**privateArticleDelete**](ArticlesApi.md#privateArticleDelete) | **DELETE** /account/articles/{article_id} | Delete article |
| [**privateArticleDetails**](ArticlesApi.md#privateArticleDetails) | **GET** /account/articles/{article_id} | Article details |
| [**privateArticleEmbargoDelete**](ArticlesApi.md#privateArticleEmbargoDelete) | **DELETE** /account/articles/{article_id}/embargo | Delete Article Embargo |
| [**privateArticleEmbargoDetails**](ArticlesApi.md#privateArticleEmbargoDetails) | **GET** /account/articles/{article_id}/embargo | Article Embargo Details |
| [**privateArticleEmbargoUpdate**](ArticlesApi.md#privateArticleEmbargoUpdate) | **PUT** /account/articles/{article_id}/embargo | Update Article Embargo |
| [**privateArticleFile**](ArticlesApi.md#privateArticleFile) | **GET** /account/articles/{article_id}/files/{file_id} | Single File |
| [**privateArticleFileDelete**](ArticlesApi.md#privateArticleFileDelete) | **DELETE** /account/articles/{article_id}/files/{file_id} | File Delete |
| [**privateArticleFilesList**](ArticlesApi.md#privateArticleFilesList) | **GET** /account/articles/{article_id}/files | List article files |
| [**privateArticlePrivateLink**](ArticlesApi.md#privateArticlePrivateLink) | **GET** /account/articles/{article_id}/private_links | List private links |
| [**privateArticlePrivateLinkCreate**](ArticlesApi.md#privateArticlePrivateLinkCreate) | **POST** /account/articles/{article_id}/private_links | Create private link |
| [**privateArticlePrivateLinkDelete**](ArticlesApi.md#privateArticlePrivateLinkDelete) | **DELETE** /account/articles/{article_id}/private_links/{link_id} | Disable private link |
| [**privateArticlePrivateLinkUpdate**](ArticlesApi.md#privateArticlePrivateLinkUpdate) | **PUT** /account/articles/{article_id}/private_links/{link_id} | Update private link |
| [**privateArticlePublish**](ArticlesApi.md#privateArticlePublish) | **POST** /account/articles/{article_id}/publish | Private Article Publish |
| [**privateArticleReserveDoi**](ArticlesApi.md#privateArticleReserveDoi) | **POST** /account/articles/{article_id}/reserve_doi | Private Article Reserve DOI |
| [**privateArticleReserveHandle**](ArticlesApi.md#privateArticleReserveHandle) | **POST** /account/articles/{article_id}/reserve_handle | Private Article Reserve Handle |
| [**privateArticleResource**](ArticlesApi.md#privateArticleResource) | **POST** /account/articles/{article_id}/resource | Private Article Resource |
| [**privateArticleUpdate**](ArticlesApi.md#privateArticleUpdate) | **PUT** /account/articles/{article_id} | Update article |
| [**privateArticleUploadComplete**](ArticlesApi.md#privateArticleUploadComplete) | **POST** /account/articles/{article_id}/files/{file_id} | Complete Upload |
| [**privateArticleUploadInitiate**](ArticlesApi.md#privateArticleUploadInitiate) | **POST** /account/articles/{article_id}/files | Initiate Upload |
| [**privateArticlesList**](ArticlesApi.md#privateArticlesList) | **GET** /account/articles | Private Articles |
| [**privateArticlesSearch**](ArticlesApi.md#privateArticlesSearch) | **POST** /account/articles/search | Private Articles search |


<a id="accountArticleReport"></a>
# **accountArticleReport**
> List&lt;AccountReport&gt; accountArticleReport(groupId)

Account Article Report

Return status on all reports generated for the account from the oauth credentials

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    Long groupId = 56L; // Long | A group ID to filter by
    try {
      List<AccountReport> result = apiInstance.accountArticleReport(groupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#accountArticleReport");
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
| **groupId** | **Long**| A group ID to filter by | [optional] |

### Return type

[**List&lt;AccountReport&gt;**](AccountReport.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. An array of account report entries |  -  |
| **400** | Bad Request |  -  |
| **500** | Internal Server Error |  -  |

<a id="accountArticleReportGenerate"></a>
# **accountArticleReportGenerate**
> AccountReport accountArticleReportGenerate()

Initiate a new Report

Initiate a new Article Report for this Account. There is a limit of 1 report per day.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    try {
      AccountReport result = apiInstance.accountArticleReportGenerate();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#accountArticleReportGenerate");
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

[**AccountReport**](AccountReport.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. AccountReport created. |  -  |
| **429** | Too Many Requests |  -  |
| **500** | Internal Server Error |  -  |

<a id="articleDetails"></a>
# **articleDetails**
> ArticleComplete articleDetails(articleId)

View article details

View an article

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    Long articleId = 56L; // Long | Article Unique identifier
    try {
      ArticleComplete result = apiInstance.articleDetails(articleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#articleDetails");
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
| **articleId** | **Long**| Article Unique identifier | |

### Return type

[**ArticleComplete**](ArticleComplete.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Article representation |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="articleFileDetails"></a>
# **articleFileDetails**
> PublicFile articleFileDetails(articleId, fileId)

Article file details

File by id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    Long articleId = 56L; // Long | Article Unique identifier
    Long fileId = 56L; // Long | File Unique identifier
    try {
      PublicFile result = apiInstance.articleFileDetails(articleId, fileId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#articleFileDetails");
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
| **articleId** | **Long**| Article Unique identifier | |
| **fileId** | **Long**| File Unique identifier | |

### Return type

[**PublicFile**](PublicFile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. File representation |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="articleFiles"></a>
# **articleFiles**
> List&lt;PublicFile&gt; articleFiles(articleId)

List article files

Files list for article

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    Long articleId = 56L; // Long | Article Unique identifier
    try {
      List<PublicFile> result = apiInstance.articleFiles(articleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#articleFiles");
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
| **articleId** | **Long**| Article Unique identifier | |

### Return type

[**List&lt;PublicFile&gt;**](PublicFile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. List of article files |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="articleVersionConfidentiality"></a>
# **articleVersionConfidentiality**
> ArticleConfidentiality articleVersionConfidentiality(articleId, vNumber)

Public Article Confidentiality for article version

Confidentiality for article version. The confidentiality feature is now deprecated. This has been replaced by the new extended embargo functionality and all items that used to be confidential have now been migrated to items with a permanent embargo on files. All API endpoints related to this functionality will remain for backwards compatibility, but will now be attached to the new extended embargo workflows.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    Long articleId = 56L; // Long | Article Unique identifier
    Long vNumber = 56L; // Long | Version Number
    try {
      ArticleConfidentiality result = apiInstance.articleVersionConfidentiality(articleId, vNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#articleVersionConfidentiality");
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
| **articleId** | **Long**| Article Unique identifier | |
| **vNumber** | **Long**| Version Number | |

### Return type

[**ArticleConfidentiality**](ArticleConfidentiality.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Confidentiality representation |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="articleVersionDetails"></a>
# **articleVersionDetails**
> ArticleComplete articleVersionDetails(articleId, vNumber)

Article details for version

Article with specified version

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    Long articleId = 56L; // Long | Article Unique identifier
    Long vNumber = 56L; // Long | Article Version Number
    try {
      ArticleComplete result = apiInstance.articleVersionDetails(articleId, vNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#articleVersionDetails");
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
| **articleId** | **Long**| Article Unique identifier | |
| **vNumber** | **Long**| Article Version Number | |

### Return type

[**ArticleComplete**](ArticleComplete.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Article representation |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="articleVersionEmbargo"></a>
# **articleVersionEmbargo**
> ArticleEmbargo articleVersionEmbargo(articleId, vNumber)

Public Article Embargo for article version

Embargo for article version

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    Long articleId = 56L; // Long | Article Unique identifier
    Long vNumber = 56L; // Long | Version Number
    try {
      ArticleEmbargo result = apiInstance.articleVersionEmbargo(articleId, vNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#articleVersionEmbargo");
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
| **articleId** | **Long**| Article Unique identifier | |
| **vNumber** | **Long**| Version Number | |

### Return type

[**ArticleEmbargo**](ArticleEmbargo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Embargo representation |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="articleVersionUpdate"></a>
# **articleVersionUpdate**
> LocationWarningsUpdate articleVersionUpdate(articleId, versionId, articleUpdate)

Update article version

Updating an article version by passing body parameters; request can also be made with the PATCH method.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    Long articleId = 56L; // Long | Article unique identifier
    Long versionId = 56L; // Long | Article version identifier
    ArticleUpdate articleUpdate = new ArticleUpdate(); // ArticleUpdate | Article description
    try {
      LocationWarningsUpdate result = apiInstance.articleVersionUpdate(articleId, versionId, articleUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#articleVersionUpdate");
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
| **articleId** | **Long**| Article unique identifier | |
| **versionId** | **Long**| Article version identifier | |
| **articleUpdate** | [**ArticleUpdate**](ArticleUpdate.md)| Article description | |

### Return type

[**LocationWarningsUpdate**](LocationWarningsUpdate.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **205** | Reset Content |  * Location - Location of project <br>  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="articleVersionUpdateThumb"></a>
# **articleVersionUpdateThumb**
> articleVersionUpdateThumb(articleId, versionId, fileId)

Update article version thumbnail

For a given public article version update the article thumbnail by choosing one of the associated files

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    Long articleId = 56L; // Long | Article unique identifier
    Long versionId = 56L; // Long | Article version identifier
    FileId fileId = new FileId(); // FileId | File ID
    try {
      apiInstance.articleVersionUpdateThumb(articleId, versionId, fileId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#articleVersionUpdateThumb");
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
| **articleId** | **Long**| Article unique identifier | |
| **versionId** | **Long**| Article version identifier | |
| **fileId** | [**FileId**](FileId.md)| File ID | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **205** | Reset Content |  * Location - Location of project <br>  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **422** | Unprocessable Entity |  -  |

<a id="articleVersions"></a>
# **articleVersions**
> List&lt;ArticleVersions&gt; articleVersions(articleId)

List article versions

List public article versions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    Long articleId = 56L; // Long | Article Unique identifier
    try {
      List<ArticleVersions> result = apiInstance.articleVersions(articleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#articleVersions");
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
| **articleId** | **Long**| Article Unique identifier | |

### Return type

[**List&lt;ArticleVersions&gt;**](ArticleVersions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Article version representations |  -  |
| **400** | Bad Request. Article ID must be an integer and bigger than 0. |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="articlesList"></a>
# **articlesList**
> List&lt;Article&gt; articlesList(xCursor, page, pageSize, limit, offset, order, orderDirection, institution, publishedSince, modifiedSince, group, resourceDoi, itemType, doi, handle)

Public Articles

Returns a list of public articles

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    UUID xCursor = UUID.randomUUID(); // UUID | Unique hash used for bypassing the item retrieval limit of 9,000 entities. When using this parameter, please note that the offset parameter will not be available, but the limit parameter will still work as expected.
    Long page = 56L; // Long | Page number. Used for pagination with page_size
    Long pageSize = 10L; // Long | The number of results included on a page. Used for pagination with page
    Long limit = 56L; // Long | Number of results included on a page. Used for pagination with query
    Long offset = 56L; // Long | Where to start the listing(the offset of the first result). Used for pagination with limit
    String order = "published_date"; // String | The field by which to order. Default varies by endpoint/resource.
    String orderDirection = "asc"; // String | 
    Long institution = 56L; // Long | only return articles from this institution
    String publishedSince = "publishedSince_example"; // String | Filter by article publishing date. Will only return articles published after the date. date(ISO 8601) YYYY-MM-DD
    String modifiedSince = "modifiedSince_example"; // String | Filter by article modified date. Will only return articles published after the date. date(ISO 8601) YYYY-MM-DD
    Long group = 56L; // Long | only return articles from this group
    String resourceDoi = "resourceDoi_example"; // String | only return articles with this resource_doi
    Long itemType = 56L; // Long | Only return articles with the respective type. Mapping for item_type is: 1 - Figure, 2 - Media, 3 - Dataset, 5 - Poster, 6 - Journal contribution, 7 - Presentation, 8 - Thesis, 9 - Software, 11 - Online resource, 12 - Preprint, 13 - Book, 14 - Conference contribution, 15 - Chapter, 16 - Peer review, 17 - Educational resource, 18 - Report, 19 - Standard, 20 - Composition, 21 - Funding, 22 - Physical object, 23 - Data management plan, 24 - Workflow, 25 - Monograph, 26 - Performance, 27 - Event, 28 - Service, 29 - Model
    String doi = "doi_example"; // String | only return articles with this doi
    String handle = "handle_example"; // String | only return articles with this handle
    try {
      List<Article> result = apiInstance.articlesList(xCursor, page, pageSize, limit, offset, order, orderDirection, institution, publishedSince, modifiedSince, group, resourceDoi, itemType, doi, handle);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#articlesList");
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
| **xCursor** | **UUID**| Unique hash used for bypassing the item retrieval limit of 9,000 entities. When using this parameter, please note that the offset parameter will not be available, but the limit parameter will still work as expected. | [optional] |
| **page** | **Long**| Page number. Used for pagination with page_size | [optional] |
| **pageSize** | **Long**| The number of results included on a page. Used for pagination with page | [optional] [default to 10] |
| **limit** | **Long**| Number of results included on a page. Used for pagination with query | [optional] |
| **offset** | **Long**| Where to start the listing(the offset of the first result). Used for pagination with limit | [optional] |
| **order** | **String**| The field by which to order. Default varies by endpoint/resource. | [optional] [default to published_date] [enum: published_date, modified_date, views, shares, downloads, cites] |
| **orderDirection** | **String**|  | [optional] [default to desc] [enum: asc, desc] |
| **institution** | **Long**| only return articles from this institution | [optional] |
| **publishedSince** | **String**| Filter by article publishing date. Will only return articles published after the date. date(ISO 8601) YYYY-MM-DD | [optional] |
| **modifiedSince** | **String**| Filter by article modified date. Will only return articles published after the date. date(ISO 8601) YYYY-MM-DD | [optional] |
| **group** | **Long**| only return articles from this group | [optional] |
| **resourceDoi** | **String**| only return articles with this resource_doi | [optional] |
| **itemType** | **Long**| Only return articles with the respective type. Mapping for item_type is: 1 - Figure, 2 - Media, 3 - Dataset, 5 - Poster, 6 - Journal contribution, 7 - Presentation, 8 - Thesis, 9 - Software, 11 - Online resource, 12 - Preprint, 13 - Book, 14 - Conference contribution, 15 - Chapter, 16 - Peer review, 17 - Educational resource, 18 - Report, 19 - Standard, 20 - Composition, 21 - Funding, 22 - Physical object, 23 - Data management plan, 24 - Workflow, 25 - Monograph, 26 - Performance, 27 - Event, 28 - Service, 29 - Model | [optional] |
| **doi** | **String**| only return articles with this doi | [optional] |
| **handle** | **String**| only return articles with this handle | [optional] |

### Return type

[**List&lt;Article&gt;**](Article.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. An array of articles |  * X-Cursor - Unique hash used for bypassing the item retrieval limit of 9,000 entities. <br>  |
| **400** | Bad Request |  -  |
| **422** | Unprocessable Entity. Syntax is correct but one of the parameters isn&#39;t correctly processed |  -  |
| **500** | Internal Server Error |  -  |

<a id="articlesSearch"></a>
# **articlesSearch**
> List&lt;ArticleWithProject&gt; articlesSearch(xCursor, articleSearch)

Public Articles Search

Returns a list of public articles, filtered by the search parameters

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    UUID xCursor = UUID.randomUUID(); // UUID | Unique hash used for bypassing the item retrieval limit of 9,000 entities. When using this parameter, please note that the offset parameter will not be available, but the limit parameter will still work as expected.
    ArticleSearch articleSearch = new ArticleSearch(); // ArticleSearch | Search Parameters
    try {
      List<ArticleWithProject> result = apiInstance.articlesSearch(xCursor, articleSearch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#articlesSearch");
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
| **xCursor** | **UUID**| Unique hash used for bypassing the item retrieval limit of 9,000 entities. When using this parameter, please note that the offset parameter will not be available, but the limit parameter will still work as expected. | [optional] |
| **articleSearch** | [**ArticleSearch**](ArticleSearch.md)| Search Parameters | [optional] |

### Return type

[**List&lt;ArticleWithProject&gt;**](ArticleWithProject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. An array of articles |  * X-Cursor - Unique hash used for bypassing the item retrieval limit of 9,000 entities. <br>  |
| **400** | Bad Request |  -  |
| **422** | Unprocessable Entity. Syntax is correct but one of the parameters isn&#39;t correctly processed |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateArticleAuthorDelete"></a>
# **privateArticleAuthorDelete**
> privateArticleAuthorDelete(articleId, authorId)

Delete article author

De-associate author from article

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    Long articleId = 56L; // Long | Article unique identifier
    Long authorId = 56L; // Long | Article Author unique identifier
    try {
      apiInstance.privateArticleAuthorDelete(articleId, authorId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#privateArticleAuthorDelete");
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
| **articleId** | **Long**| Article unique identifier | |
| **authorId** | **Long**| Article Author unique identifier | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateArticleAuthorsAdd"></a>
# **privateArticleAuthorsAdd**
> privateArticleAuthorsAdd(articleId, authorsCreator)

Add article authors

Associate new authors with the article. This will add new authors to the list of already associated authors

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    Long articleId = 56L; // Long | Article unique identifier
    AuthorsCreator authorsCreator = new AuthorsCreator(); // AuthorsCreator | Authors description
    try {
      apiInstance.privateArticleAuthorsAdd(articleId, authorsCreator);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#privateArticleAuthorsAdd");
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
| **articleId** | **Long**| Article unique identifier | |
| **authorsCreator** | [**AuthorsCreator**](AuthorsCreator.md)| Authors description | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **205** | Reset Content |  * Location - Location note <br>  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateArticleAuthorsList"></a>
# **privateArticleAuthorsList**
> List&lt;Author&gt; privateArticleAuthorsList(articleId)

List article authors

List article authors

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    Long articleId = 56L; // Long | Article unique identifier
    try {
      List<Author> result = apiInstance.privateArticleAuthorsList(articleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#privateArticleAuthorsList");
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
| **articleId** | **Long**| Article unique identifier | |

### Return type

[**List&lt;Author&gt;**](Author.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Authors list for article |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateArticleAuthorsReplace"></a>
# **privateArticleAuthorsReplace**
> privateArticleAuthorsReplace(articleId, authorsCreator)

Replace article authors

Associate new authors with the article. This will remove all already associated authors and add these new ones

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    Long articleId = 56L; // Long | Article unique identifier
    AuthorsCreator authorsCreator = new AuthorsCreator(); // AuthorsCreator | Authors description
    try {
      apiInstance.privateArticleAuthorsReplace(articleId, authorsCreator);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#privateArticleAuthorsReplace");
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
| **articleId** | **Long**| Article unique identifier | |
| **authorsCreator** | [**AuthorsCreator**](AuthorsCreator.md)| Authors description | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **205** | Reset Content |  * Location - Location note <br>  |
| **400** | Bad Request. Article ID must be an integer and bigger than 0. Author with ID Not Found. |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateArticleCategoriesAdd"></a>
# **privateArticleCategoriesAdd**
> privateArticleCategoriesAdd(articleId, categoriesCreator)

Add article categories

Associate new categories with the article. This will add new categories to the list of already associated categories

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    Long articleId = 56L; // Long | Article unique identifier
    CategoriesCreator categoriesCreator = new CategoriesCreator(); // CategoriesCreator | 
    try {
      apiInstance.privateArticleCategoriesAdd(articleId, categoriesCreator);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#privateArticleCategoriesAdd");
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
| **articleId** | **Long**| Article unique identifier | |
| **categoriesCreator** | [**CategoriesCreator**](CategoriesCreator.md)|  | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **205** | Reset Content |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateArticleCategoriesList"></a>
# **privateArticleCategoriesList**
> List&lt;Category&gt; privateArticleCategoriesList(articleId)

List article categories

List article categories

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    Long articleId = 56L; // Long | Article unique identifier
    try {
      List<Category> result = apiInstance.privateArticleCategoriesList(articleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#privateArticleCategoriesList");
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
| **articleId** | **Long**| Article unique identifier | |

### Return type

[**List&lt;Category&gt;**](Category.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Article categories |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateArticleCategoriesReplace"></a>
# **privateArticleCategoriesReplace**
> privateArticleCategoriesReplace(articleId, categoriesCreator)

Replace article categories

Associate new categories with the article. This will remove all already associated categories and add these new ones

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    Long articleId = 56L; // Long | Article unique identifier
    CategoriesCreator categoriesCreator = new CategoriesCreator(); // CategoriesCreator | 
    try {
      apiInstance.privateArticleCategoriesReplace(articleId, categoriesCreator);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#privateArticleCategoriesReplace");
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
| **articleId** | **Long**| Article unique identifier | |
| **categoriesCreator** | [**CategoriesCreator**](CategoriesCreator.md)|  | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **205** | Reset Content |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateArticleCategoryDelete"></a>
# **privateArticleCategoryDelete**
> privateArticleCategoryDelete(articleId, categoryId)

Delete article category

De-associate category from article

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    Long articleId = 56L; // Long | Article unique identifier
    Long categoryId = 56L; // Long | Category unique identifier
    try {
      apiInstance.privateArticleCategoryDelete(articleId, categoryId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#privateArticleCategoryDelete");
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
| **articleId** | **Long**| Article unique identifier | |
| **categoryId** | **Long**| Category unique identifier | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateArticleConfidentialityDelete"></a>
# **privateArticleConfidentialityDelete**
> privateArticleConfidentialityDelete(articleId)

Delete article confidentiality

Delete confidentiality settings. The confidentiality feature is now deprecated. This has been replaced by the new extended embargo functionality and all items that used to be confidential have now been migrated to items with a permanent embargo on files. All API endpoints related to this functionality will remain for backwards compatibility, but will now be attached to the new extended embargo workflows.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    Long articleId = 56L; // Long | Article unique identifier
    try {
      apiInstance.privateArticleConfidentialityDelete(articleId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#privateArticleConfidentialityDelete");
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
| **articleId** | **Long**| Article unique identifier | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateArticleConfidentialityDetails"></a>
# **privateArticleConfidentialityDetails**
> ArticleConfidentiality privateArticleConfidentialityDetails(articleId)

Article confidentiality details

View confidentiality settings. The confidentiality feature is now deprecated. This has been replaced by the new extended embargo functionality and all items that used to be confidential have now been migrated to items with a permanent embargo on files. All API endpoints related to this functionality will remain for backwards compatibility, but will now be attached to the new extended embargo workflows.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    Long articleId = 56L; // Long | Article unique identifier
    try {
      ArticleConfidentiality result = apiInstance.privateArticleConfidentialityDetails(articleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#privateArticleConfidentialityDetails");
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
| **articleId** | **Long**| Article unique identifier | |

### Return type

[**ArticleConfidentiality**](ArticleConfidentiality.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Article categories |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateArticleConfidentialityUpdate"></a>
# **privateArticleConfidentialityUpdate**
> privateArticleConfidentialityUpdate(articleId, confidentialityCreator)

Update article confidentiality

Update confidentiality settings. The confidentiality feature is now deprecated. This has been replaced by the new extended embargo functionality and all items that used to be confidential have now been migrated to items with a permanent embargo on files. All API endpoints related to this functionality will remain for backwards compatibility, but will now be attached to the new extended embargo workflows.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    Long articleId = 56L; // Long | Article unique identifier
    ConfidentialityCreator confidentialityCreator = new ConfidentialityCreator(); // ConfidentialityCreator | 
    try {
      apiInstance.privateArticleConfidentialityUpdate(articleId, confidentialityCreator);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#privateArticleConfidentialityUpdate");
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
| **articleId** | **Long**| Article unique identifier | |
| **confidentialityCreator** | [**ConfidentialityCreator**](ConfidentialityCreator.md)|  | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **205** | Reset Content |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateArticleCreate"></a>
# **privateArticleCreate**
> LocationWarnings privateArticleCreate(articleCreate)

Create new Article

Create a new Article by sending article information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    ArticleCreate articleCreate = new ArticleCreate(); // ArticleCreate | Article description
    try {
      LocationWarnings result = apiInstance.privateArticleCreate(articleCreate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#privateArticleCreate");
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
| **articleCreate** | [**ArticleCreate**](ArticleCreate.md)| Article description | |

### Return type

[**LocationWarnings**](LocationWarnings.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateArticleDelete"></a>
# **privateArticleDelete**
> privateArticleDelete(articleId)

Delete article

Delete an article

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    Long articleId = 56L; // Long | Article unique identifier
    try {
      apiInstance.privateArticleDelete(articleId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#privateArticleDelete");
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
| **articleId** | **Long**| Article unique identifier | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateArticleDetails"></a>
# **privateArticleDetails**
> ArticleCompletePrivate privateArticleDetails(articleId)

Article details

View a private article

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    Long articleId = 56L; // Long | Article unique identifier
    try {
      ArticleCompletePrivate result = apiInstance.privateArticleDetails(articleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#privateArticleDetails");
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
| **articleId** | **Long**| Article unique identifier | |

### Return type

[**ArticleCompletePrivate**](ArticleCompletePrivate.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Article representation |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateArticleEmbargoDelete"></a>
# **privateArticleEmbargoDelete**
> privateArticleEmbargoDelete(articleId)

Delete Article Embargo

Will lift the embargo for the specified article

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    Long articleId = 56L; // Long | Article unique identifier
    try {
      apiInstance.privateArticleEmbargoDelete(articleId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#privateArticleEmbargoDelete");
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
| **articleId** | **Long**| Article unique identifier | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateArticleEmbargoDetails"></a>
# **privateArticleEmbargoDetails**
> ArticleEmbargo privateArticleEmbargoDetails(articleId)

Article Embargo Details

View a private article embargo details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    Long articleId = 56L; // Long | Article unique identifier
    try {
      ArticleEmbargo result = apiInstance.privateArticleEmbargoDetails(articleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#privateArticleEmbargoDetails");
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
| **articleId** | **Long**| Article unique identifier | |

### Return type

[**ArticleEmbargo**](ArticleEmbargo.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Embargo for article |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateArticleEmbargoUpdate"></a>
# **privateArticleEmbargoUpdate**
> privateArticleEmbargoUpdate(articleId, articleEmbargoUpdater)

Update Article Embargo

Note: setting an article under whole embargo does not imply that the article will be published when the embargo will expire. You must explicitly call the publish endpoint to enable this functionality.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    Long articleId = 56L; // Long | Article unique identifier
    ArticleEmbargoUpdater articleEmbargoUpdater = new ArticleEmbargoUpdater(); // ArticleEmbargoUpdater | Embargo description
    try {
      apiInstance.privateArticleEmbargoUpdate(articleId, articleEmbargoUpdater);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#privateArticleEmbargoUpdate");
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
| **articleId** | **Long**| Article unique identifier | |
| **articleEmbargoUpdater** | [**ArticleEmbargoUpdater**](ArticleEmbargoUpdater.md)| Embargo description | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **205** | Reset Content |  * Location - Location of project <br>  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateArticleFile"></a>
# **privateArticleFile**
> PrivateFile privateArticleFile(articleId, fileId)

Single File

View details of file for specified article

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    Long articleId = 56L; // Long | Article unique identifier
    Long fileId = 56L; // Long | File unique identifier
    try {
      PrivateFile result = apiInstance.privateArticleFile(articleId, fileId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#privateArticleFile");
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
| **articleId** | **Long**| Article unique identifier | |
| **fileId** | **Long**| File unique identifier | |

### Return type

[**PrivateFile**](PrivateFile.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Article private file |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateArticleFileDelete"></a>
# **privateArticleFileDelete**
> privateArticleFileDelete(articleId, fileId)

File Delete

Complete file upload

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    Long articleId = 56L; // Long | Article unique identifier
    Long fileId = 56L; // Long | File unique identifier
    try {
      apiInstance.privateArticleFileDelete(articleId, fileId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#privateArticleFileDelete");
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
| **articleId** | **Long**| Article unique identifier | |
| **fileId** | **Long**| File unique identifier | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateArticleFilesList"></a>
# **privateArticleFilesList**
> List&lt;PrivateFile&gt; privateArticleFilesList(articleId)

List article files

List private files

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    Long articleId = 56L; // Long | Article unique identifier
    try {
      List<PrivateFile> result = apiInstance.privateArticleFilesList(articleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#privateArticleFilesList");
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
| **articleId** | **Long**| Article unique identifier | |

### Return type

[**List&lt;PrivateFile&gt;**](PrivateFile.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Article files list |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateArticlePrivateLink"></a>
# **privateArticlePrivateLink**
> List&lt;PrivateLink&gt; privateArticlePrivateLink(articleId)

List private links

List private links

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    Long articleId = 56L; // Long | Article unique identifier
    try {
      List<PrivateLink> result = apiInstance.privateArticlePrivateLink(articleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#privateArticlePrivateLink");
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
| **articleId** | **Long**| Article unique identifier | |

### Return type

[**List&lt;PrivateLink&gt;**](PrivateLink.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Article private links |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateArticlePrivateLinkCreate"></a>
# **privateArticlePrivateLinkCreate**
> PrivateLinkResponse privateArticlePrivateLinkCreate(articleId, privateLinkCreator)

Create private link

Create new private link for this article

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    Long articleId = 56L; // Long | Article unique identifier
    PrivateLinkCreator privateLinkCreator = new PrivateLinkCreator(); // PrivateLinkCreator | 
    try {
      PrivateLinkResponse result = apiInstance.privateArticlePrivateLinkCreate(articleId, privateLinkCreator);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#privateArticlePrivateLinkCreate");
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
| **articleId** | **Long**| Article unique identifier | |
| **privateLinkCreator** | [**PrivateLinkCreator**](PrivateLinkCreator.md)|  | [optional] |

### Return type

[**PrivateLinkResponse**](PrivateLinkResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  * Location - Location note <br>  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **422** | Unprocessable Entity |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateArticlePrivateLinkDelete"></a>
# **privateArticlePrivateLinkDelete**
> privateArticlePrivateLinkDelete(articleId, linkId)

Disable private link

Disable/delete private link for this article

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    Long articleId = 56L; // Long | Article unique identifier
    String linkId = "linkId_example"; // String | Private link token
    try {
      apiInstance.privateArticlePrivateLinkDelete(articleId, linkId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#privateArticlePrivateLinkDelete");
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
| **articleId** | **Long**| Article unique identifier | |
| **linkId** | **String**| Private link token | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateArticlePrivateLinkUpdate"></a>
# **privateArticlePrivateLinkUpdate**
> privateArticlePrivateLinkUpdate(articleId, linkId, privateLinkCreator)

Update private link

Update existing private link for this article

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    Long articleId = 56L; // Long | Article unique identifier
    String linkId = "linkId_example"; // String | Private link token
    PrivateLinkCreator privateLinkCreator = new PrivateLinkCreator(); // PrivateLinkCreator | 
    try {
      apiInstance.privateArticlePrivateLinkUpdate(articleId, linkId, privateLinkCreator);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#privateArticlePrivateLinkUpdate");
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
| **articleId** | **Long**| Article unique identifier | |
| **linkId** | **String**| Private link token | |
| **privateLinkCreator** | [**PrivateLinkCreator**](PrivateLinkCreator.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **205** | Reset Content |  * Location - Location note <br>  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **422** | Unprocessable Entity |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateArticlePublish"></a>
# **privateArticlePublish**
> Location privateArticlePublish(articleId)

Private Article Publish

- If the whole article is under embargo, it will not be published immediately, but when the embargo expires or is lifted. - When an article is published, a new public version will be generated. Any further updates to the article will affect the private article data. In order to make these changes publicly visible, an explicit publish operation is needed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    Long articleId = 56L; // Long | Article unique identifier
    try {
      Location result = apiInstance.privateArticlePublish(articleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#privateArticlePublish");
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
| **articleId** | **Long**| Article unique identifier | |

### Return type

[**Location**](Location.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  * Location - Location of project <br>  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateArticleReserveDoi"></a>
# **privateArticleReserveDoi**
> ArticleDOI privateArticleReserveDoi(articleId)

Private Article Reserve DOI

Reserve DOI for article

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    Long articleId = 56L; // Long | Article unique identifier
    try {
      ArticleDOI result = apiInstance.privateArticleReserveDoi(articleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#privateArticleReserveDoi");
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
| **articleId** | **Long**| Article unique identifier | |

### Return type

[**ArticleDOI**](ArticleDOI.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateArticleReserveHandle"></a>
# **privateArticleReserveHandle**
> ArticleHandle privateArticleReserveHandle(articleId)

Private Article Reserve Handle

Reserve Handle for article

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    Long articleId = 56L; // Long | Article unique identifier
    try {
      ArticleHandle result = apiInstance.privateArticleReserveHandle(articleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#privateArticleReserveHandle");
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
| **articleId** | **Long**| Article unique identifier | |

### Return type

[**ArticleHandle**](ArticleHandle.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateArticleResource"></a>
# **privateArticleResource**
> Location privateArticleResource(articleId, resource)

Private Article Resource

Edit article resource data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    Long articleId = 56L; // Long | Article unique identifier
    Resource resource = new Resource(); // Resource | Resource data
    try {
      Location result = apiInstance.privateArticleResource(articleId, resource);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#privateArticleResource");
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
| **articleId** | **Long**| Article unique identifier | |
| **resource** | [**Resource**](Resource.md)| Resource data | |

### Return type

[**Location**](Location.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **205** | Reset Content |  * Location - Location of project <br>  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **422** | Unprocessable Entity |  -  |

<a id="privateArticleUpdate"></a>
# **privateArticleUpdate**
> LocationWarningsUpdate privateArticleUpdate(articleId, articleUpdate)

Update article

Updating an article by passing body parameters; request can also be made with the PATCH method.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    Long articleId = 56L; // Long | Article unique identifier
    ArticleUpdate articleUpdate = new ArticleUpdate(); // ArticleUpdate | Article description
    try {
      LocationWarningsUpdate result = apiInstance.privateArticleUpdate(articleId, articleUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#privateArticleUpdate");
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
| **articleId** | **Long**| Article unique identifier | |
| **articleUpdate** | [**ArticleUpdate**](ArticleUpdate.md)| Article description | |

### Return type

[**LocationWarningsUpdate**](LocationWarningsUpdate.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **205** | Reset Content |  * Location - Location of project <br>  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateArticleUploadComplete"></a>
# **privateArticleUploadComplete**
> privateArticleUploadComplete(articleId, fileId)

Complete Upload

Complete file upload

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    Long articleId = 56L; // Long | Article unique identifier
    Long fileId = 56L; // Long | File unique identifier
    try {
      apiInstance.privateArticleUploadComplete(articleId, fileId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#privateArticleUploadComplete");
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
| **articleId** | **Long**| Article unique identifier | |
| **fileId** | **Long**| File unique identifier | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateArticleUploadInitiate"></a>
# **privateArticleUploadInitiate**
> Location privateArticleUploadInitiate(articleId, fileCreator)

Initiate Upload

Initiate a new file upload within the article. Either use the link property to point to an existing file that resides elsewhere and will not be uploaded to Figshare or use the other 3 parameters (md5, name, size).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    Long articleId = 56L; // Long | Article unique identifier
    FileCreator fileCreator = new FileCreator(); // FileCreator | 
    try {
      Location result = apiInstance.privateArticleUploadInitiate(articleId, fileCreator);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#privateArticleUploadInitiate");
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
| **articleId** | **Long**| Article unique identifier | |
| **fileCreator** | [**FileCreator**](FileCreator.md)|  | |

### Return type

[**Location**](Location.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  * Location - Location note <br>  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **422** | Unprocessable Entity. Parameters missing or incorrect |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateArticlesList"></a>
# **privateArticlesList**
> List&lt;Article&gt; privateArticlesList(page, pageSize, limit, offset)

Private Articles

Get Own Articles

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    Long page = 56L; // Long | Page number. Used for pagination with page_size
    Long pageSize = 10L; // Long | The number of results included on a page. Used for pagination with page
    Long limit = 56L; // Long | Number of results included on a page. Used for pagination with query
    Long offset = 56L; // Long | Where to start the listing(the offset of the first result). Used for pagination with limit
    try {
      List<Article> result = apiInstance.privateArticlesList(page, pageSize, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#privateArticlesList");
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
| **page** | **Long**| Page number. Used for pagination with page_size | [optional] |
| **pageSize** | **Long**| The number of results included on a page. Used for pagination with page | [optional] [default to 10] |
| **limit** | **Long**| Number of results included on a page. Used for pagination with query | [optional] |
| **offset** | **Long**| Where to start the listing(the offset of the first result). Used for pagination with limit | [optional] |

### Return type

[**List&lt;Article&gt;**](Article.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. An array of articles belonging to the account |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateArticlesSearch"></a>
# **privateArticlesSearch**
> List&lt;ArticleWithProject&gt; privateArticlesSearch(privateArticleSearch)

Private Articles search

Returns a list of private articles filtered by the search parameters

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    PrivateArticleSearch privateArticleSearch = new PrivateArticleSearch(); // PrivateArticleSearch | Search Parameters
    try {
      List<ArticleWithProject> result = apiInstance.privateArticlesSearch(privateArticleSearch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#privateArticlesSearch");
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
| **privateArticleSearch** | [**PrivateArticleSearch**](PrivateArticleSearch.md)| Search Parameters | |

### Return type

[**List&lt;ArticleWithProject&gt;**](ArticleWithProject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. An array of articles |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **500** | Internal Server Error |  -  |

