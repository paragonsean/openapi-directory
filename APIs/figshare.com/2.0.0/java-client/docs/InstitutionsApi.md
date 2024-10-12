# InstitutionsApi

All URIs are relative to *https://api.figshare.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**accountInstitutionCuration**](InstitutionsApi.md#accountInstitutionCuration) | **GET** /account/institution/review/{curation_id} | Institution Curation Review |
| [**accountInstitutionCurationComments**](InstitutionsApi.md#accountInstitutionCurationComments) | **GET** /account/institution/review/{curation_id}/comments | Institution Curation Review Comments |
| [**accountInstitutionCurations**](InstitutionsApi.md#accountInstitutionCurations) | **GET** /account/institution/reviews | Institution Curation Reviews |
| [**accountInstitutionReviewCurationIdCommentsPost**](InstitutionsApi.md#accountInstitutionReviewCurationIdCommentsPost) | **POST** /account/institution/review/{curation_id}/comments | POST Institution Curation Review Comment |
| [**customFieldsList**](InstitutionsApi.md#customFieldsList) | **GET** /account/institution/custom_fields | Private account institution group custom fields |
| [**customFieldsUpload**](InstitutionsApi.md#customFieldsUpload) | **POST** /account/institution/custom_fields/{custom_field_id}/items/upload | Custom fields values files upload |
| [**institutionArticles**](InstitutionsApi.md#institutionArticles) | **GET** /institutions/{institution_string_id}/articles/filter-by | Public Licenses |
| [**institutionHrfeedUpload**](InstitutionsApi.md#institutionHrfeedUpload) | **POST** /institution/hrfeed/upload | Private Institution HRfeed Upload |
| [**privateAccountInstitutionUser**](InstitutionsApi.md#privateAccountInstitutionUser) | **GET** /account/institution/users/{account_id} | Private Account Institution User |
| [**privateCategoriesList**](InstitutionsApi.md#privateCategoriesList) | **GET** /account/categories | Private Account Categories |
| [**privateGroupEmbargoOptionsDetails**](InstitutionsApi.md#privateGroupEmbargoOptionsDetails) | **GET** /account/institution/groups/{group_id}/embargo_options | Private Account Institution Group Embargo Options |
| [**privateInstitutionAccountGroupRoleDelete**](InstitutionsApi.md#privateInstitutionAccountGroupRoleDelete) | **DELETE** /account/institution/roles/{account_id}/{group_id}/{role_id} | Delete Institution Account Group Role |
| [**privateInstitutionAccountGroupRoles**](InstitutionsApi.md#privateInstitutionAccountGroupRoles) | **GET** /account/institution/roles/{account_id} | List Institution Account Group Roles |
| [**privateInstitutionAccountGroupRolesCreate**](InstitutionsApi.md#privateInstitutionAccountGroupRolesCreate) | **POST** /account/institution/roles/{account_id} | Add Institution Account Group Roles |
| [**privateInstitutionAccountsCreate**](InstitutionsApi.md#privateInstitutionAccountsCreate) | **POST** /account/institution/accounts | Create new Institution Account |
| [**privateInstitutionAccountsList**](InstitutionsApi.md#privateInstitutionAccountsList) | **GET** /account/institution/accounts | Private Account Institution Accounts |
| [**privateInstitutionAccountsSearch**](InstitutionsApi.md#privateInstitutionAccountsSearch) | **POST** /account/institution/accounts/search | Private Account Institution Accounts Search |
| [**privateInstitutionAccountsUpdate**](InstitutionsApi.md#privateInstitutionAccountsUpdate) | **PUT** /account/institution/accounts/{account_id} | Update Institution Account |
| [**privateInstitutionArticles**](InstitutionsApi.md#privateInstitutionArticles) | **GET** /account/institution/articles | Private Institution Articles |
| [**privateInstitutionDetails**](InstitutionsApi.md#privateInstitutionDetails) | **GET** /account/institution | Private Account Institutions |
| [**privateInstitutionEmbargoOptionsDetails**](InstitutionsApi.md#privateInstitutionEmbargoOptionsDetails) | **GET** /account/institution/embargo_options | Private Account Institution embargo options |
| [**privateInstitutionGroupsList**](InstitutionsApi.md#privateInstitutionGroupsList) | **GET** /account/institution/groups | Private Account Institution Groups |
| [**privateInstitutionRolesList**](InstitutionsApi.md#privateInstitutionRolesList) | **GET** /account/institution/roles | Private Account Institution Roles |


<a id="accountInstitutionCuration"></a>
# **accountInstitutionCuration**
> CurationDetail accountInstitutionCuration(curationId)

Institution Curation Review

Retrieve a certain curation review by its ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstitutionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    InstitutionsApi apiInstance = new InstitutionsApi(defaultClient);
    Long curationId = 56L; // Long | ID of the curation
    try {
      CurationDetail result = apiInstance.accountInstitutionCuration(curationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstitutionsApi#accountInstitutionCuration");
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
| **curationId** | **Long**| ID of the curation | |

### Return type

[**CurationDetail**](CurationDetail.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. A curation review. |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="accountInstitutionCurationComments"></a>
# **accountInstitutionCurationComments**
> CurationComment accountInstitutionCurationComments(curationId, limit, offset)

Institution Curation Review Comments

Retrieve a certain curation review&#39;s comments.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstitutionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    InstitutionsApi apiInstance = new InstitutionsApi(defaultClient);
    Long curationId = 56L; // Long | ID of the curation
    Long limit = 56L; // Long | Number of results included on a page. Used for pagination with query
    Long offset = 56L; // Long | Where to start the listing(the offset of the first result). Used for pagination with limit
    try {
      CurationComment result = apiInstance.accountInstitutionCurationComments(curationId, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstitutionsApi#accountInstitutionCurationComments");
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
| **curationId** | **Long**| ID of the curation | |
| **limit** | **Long**| Number of results included on a page. Used for pagination with query | [optional] |
| **offset** | **Long**| Where to start the listing(the offset of the first result). Used for pagination with limit | [optional] |

### Return type

[**CurationComment**](CurationComment.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. A curation review&#39;s comments. |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="accountInstitutionCurations"></a>
# **accountInstitutionCurations**
> Curation accountInstitutionCurations(groupId, articleId, status, limit, offset)

Institution Curation Reviews

Retrieve a list of curation reviews for this institution

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstitutionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    InstitutionsApi apiInstance = new InstitutionsApi(defaultClient);
    Long groupId = 56L; // Long | Filter by the group ID
    Long articleId = 56L; // Long | Retrieve the reviews for this article
    String status = "pending"; // String | Filter by the status of the review
    Long limit = 56L; // Long | Number of results included on a page. Used for pagination with query
    Long offset = 56L; // Long | Where to start the listing(the offset of the first result). Used for pagination with limit
    try {
      Curation result = apiInstance.accountInstitutionCurations(groupId, articleId, status, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstitutionsApi#accountInstitutionCurations");
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
| **groupId** | **Long**| Filter by the group ID | [optional] |
| **articleId** | **Long**| Retrieve the reviews for this article | [optional] |
| **status** | **String**| Filter by the status of the review | [optional] [enum: pending, approved, rejected, closed] |
| **limit** | **Long**| Number of results included on a page. Used for pagination with query | [optional] |
| **offset** | **Long**| Where to start the listing(the offset of the first result). Used for pagination with limit | [optional] |

### Return type

[**Curation**](Curation.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. A list of curation reviews. |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="accountInstitutionReviewCurationIdCommentsPost"></a>
# **accountInstitutionReviewCurationIdCommentsPost**
> accountInstitutionReviewCurationIdCommentsPost(curationId, curationCommentCreate)

POST Institution Curation Review Comment

Add a new comment to the review.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstitutionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    InstitutionsApi apiInstance = new InstitutionsApi(defaultClient);
    Long curationId = 56L; // Long | ID of the curation
    CurationCommentCreate curationCommentCreate = new CurationCommentCreate(); // CurationCommentCreate | The content/value of the comment.
    try {
      apiInstance.accountInstitutionReviewCurationIdCommentsPost(curationId, curationCommentCreate);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstitutionsApi#accountInstitutionReviewCurationIdCommentsPost");
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
| **curationId** | **Long**| ID of the curation | |
| **curationCommentCreate** | [**CurationCommentCreate**](CurationCommentCreate.md)| The content/value of the comment. | |

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
| **200** | OK. |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="customFieldsList"></a>
# **customFieldsList**
> List&lt;ShortCustomField&gt; customFieldsList(groupId)

Private account institution group custom fields

Returns the custom fields in the group the user belongs to, or the ones in the group specified, if the user has access.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstitutionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    InstitutionsApi apiInstance = new InstitutionsApi(defaultClient);
    Long groupId = 56L; // Long | Group_id
    try {
      List<ShortCustomField> result = apiInstance.customFieldsList(groupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstitutionsApi#customFieldsList");
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
| **groupId** | **Long**| Group_id | [optional] |

### Return type

[**List&lt;ShortCustomField&gt;**](ShortCustomField.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. An array of custom fields |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **500** | Internal Server Error |  -  |

<a id="customFieldsUpload"></a>
# **customFieldsUpload**
> Object customFieldsUpload(customFieldId, externalFile)

Custom fields values files upload

Uploads a CSV containing values for a specific custom field of type &lt;b&gt;dropdown_large_list&lt;/b&gt;. More details in the &lt;a href&#x3D;\&quot;#custom_fields\&quot;&gt;Custom Fields section&lt;/a&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstitutionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    InstitutionsApi apiInstance = new InstitutionsApi(defaultClient);
    Long customFieldId = 56L; // Long | Custom field identifier
    File externalFile = new File("/path/to/file"); // File | CSV file to be uploaded
    try {
      Object result = apiInstance.customFieldsUpload(customFieldId, externalFile);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstitutionsApi#customFieldsUpload");
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
| **customFieldId** | **Long**| Custom field identifier | |
| **externalFile** | **File**| CSV file to be uploaded | [optional] |

### Return type

**Object**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **409** | Conflict |  -  |
| **500** | Internal Server Error |  -  |

<a id="institutionArticles"></a>
# **institutionArticles**
> List&lt;Article&gt; institutionArticles(institutionStringId, resourceId, filename)

Public Licenses

Returns a list of articles belonging to the institution

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstitutionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");

    InstitutionsApi apiInstance = new InstitutionsApi(defaultClient);
    String institutionStringId = "institutionStringId_example"; // String | 
    String resourceId = "resourceId_example"; // String | 
    String filename = "filename_example"; // String | 
    try {
      List<Article> result = apiInstance.institutionArticles(institutionStringId, resourceId, filename);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstitutionsApi#institutionArticles");
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
| **institutionStringId** | **String**|  | |
| **resourceId** | **String**|  | |
| **filename** | **String**|  | |

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
| **200** | OK. An array of articles |  -  |
| **500** | Internal Server Error |  -  |

<a id="institutionHrfeedUpload"></a>
# **institutionHrfeedUpload**
> ResponseMessage institutionHrfeedUpload(hrfeed)

Private Institution HRfeed Upload

More info in the &lt;a href&#x3D;\&quot;#hr_feed\&quot;&gt;HR Feed section&lt;/a&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstitutionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    InstitutionsApi apiInstance = new InstitutionsApi(defaultClient);
    File hrfeed = new File("/path/to/file"); // File | You can find an example in the Hr Feed section
    try {
      ResponseMessage result = apiInstance.institutionHrfeedUpload(hrfeed);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstitutionsApi#institutionHrfeedUpload");
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
| **hrfeed** | **File**| You can find an example in the Hr Feed section | [optional] |

### Return type

[**ResponseMessage**](ResponseMessage.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateAccountInstitutionUser"></a>
# **privateAccountInstitutionUser**
> User privateAccountInstitutionUser(accountId)

Private Account Institution User

Retrieve institution user information using the account_id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstitutionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    InstitutionsApi apiInstance = new InstitutionsApi(defaultClient);
    Long accountId = 56L; // Long | Account identifier the user is associated to
    try {
      User result = apiInstance.privateAccountInstitutionUser(accountId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstitutionsApi#privateAccountInstitutionUser");
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
| **accountId** | **Long**| Account identifier the user is associated to | |

### Return type

[**User**](User.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. User representation |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateCategoriesList"></a>
# **privateCategoriesList**
> List&lt;Category&gt; privateCategoriesList()

Private Account Categories

List institution categories (including parent Categories)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstitutionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    InstitutionsApi apiInstance = new InstitutionsApi(defaultClient);
    try {
      List<Category> result = apiInstance.privateCategoriesList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstitutionsApi#privateCategoriesList");
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

[**List&lt;Category&gt;**](Category.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. An array of categories |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateGroupEmbargoOptionsDetails"></a>
# **privateGroupEmbargoOptionsDetails**
> List&lt;GroupEmbargoOptions&gt; privateGroupEmbargoOptionsDetails(groupId)

Private Account Institution Group Embargo Options

Account institution group embargo options details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstitutionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    InstitutionsApi apiInstance = new InstitutionsApi(defaultClient);
    Long groupId = 56L; // Long | Group identifier
    try {
      List<GroupEmbargoOptions> result = apiInstance.privateGroupEmbargoOptionsDetails(groupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstitutionsApi#privateGroupEmbargoOptionsDetails");
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
| **groupId** | **Long**| Group identifier | |

### Return type

[**List&lt;GroupEmbargoOptions&gt;**](GroupEmbargoOptions.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. An array of embargo options |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateInstitutionAccountGroupRoleDelete"></a>
# **privateInstitutionAccountGroupRoleDelete**
> privateInstitutionAccountGroupRoleDelete(accountId, groupId, roleId)

Delete Institution Account Group Role

Delete Institution Account Group Role

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstitutionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    InstitutionsApi apiInstance = new InstitutionsApi(defaultClient);
    Long accountId = 56L; // Long | Account identifier for which to remove the role
    Long groupId = 56L; // Long | Group identifier for which to remove the role
    Long roleId = 56L; // Long | Role identifier
    try {
      apiInstance.privateInstitutionAccountGroupRoleDelete(accountId, groupId, roleId);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstitutionsApi#privateInstitutionAccountGroupRoleDelete");
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
| **accountId** | **Long**| Account identifier for which to remove the role | |
| **groupId** | **Long**| Group identifier for which to remove the role | |
| **roleId** | **Long**| Role identifier | |

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

<a id="privateInstitutionAccountGroupRoles"></a>
# **privateInstitutionAccountGroupRoles**
> Object privateInstitutionAccountGroupRoles(accountId)

List Institution Account Group Roles

List Institution Account Group Roles

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstitutionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    InstitutionsApi apiInstance = new InstitutionsApi(defaultClient);
    Long accountId = 56L; // Long | Account identifier the user is associated to
    try {
      Object result = apiInstance.privateInstitutionAccountGroupRoles(accountId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstitutionsApi#privateInstitutionAccountGroupRoles");
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
| **accountId** | **Long**| Account identifier the user is associated to | |

### Return type

**Object**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Account Group Roles |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateInstitutionAccountGroupRolesCreate"></a>
# **privateInstitutionAccountGroupRolesCreate**
> privateInstitutionAccountGroupRolesCreate(accountId, body)

Add Institution Account Group Roles

Add Institution Account Group Roles

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstitutionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    InstitutionsApi apiInstance = new InstitutionsApi(defaultClient);
    Long accountId = 56L; // Long | Account identifier the user is associated to
    Object body = null; // Object | Account description
    try {
      apiInstance.privateInstitutionAccountGroupRolesCreate(accountId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstitutionsApi#privateInstitutionAccountGroupRolesCreate");
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
| **accountId** | **Long**| Account identifier the user is associated to | |
| **body** | **Object**| Account description | |

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
| **201** | Created |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateInstitutionAccountsCreate"></a>
# **privateInstitutionAccountsCreate**
> privateInstitutionAccountsCreate(accountCreate)

Create new Institution Account

Create a new Account by sending account information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstitutionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    InstitutionsApi apiInstance = new InstitutionsApi(defaultClient);
    AccountCreate accountCreate = new AccountCreate(); // AccountCreate | Account description
    try {
      apiInstance.privateInstitutionAccountsCreate(accountCreate);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstitutionsApi#privateInstitutionAccountsCreate");
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
| **accountCreate** | [**AccountCreate**](AccountCreate.md)| Account description | |

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
| **201** | Created |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateInstitutionAccountsList"></a>
# **privateInstitutionAccountsList**
> List&lt;ShortAccount&gt; privateInstitutionAccountsList(page, pageSize, limit, offset, isActive, institutionUserId, email, idLte, idGte)

Private Account Institution Accounts

Returns the accounts for which the account has administrative privileges (assigned and inherited).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstitutionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    InstitutionsApi apiInstance = new InstitutionsApi(defaultClient);
    Long page = 56L; // Long | Page number. Used for pagination with page_size
    Long pageSize = 10L; // Long | The number of results included on a page. Used for pagination with page
    Long limit = 56L; // Long | Number of results included on a page. Used for pagination with query
    Long offset = 56L; // Long | Where to start the listing(the offset of the first result). Used for pagination with limit
    Long isActive = 56L; // Long | Filter by active status
    String institutionUserId = "institutionUserId_example"; // String | Filter by institution_user_id
    String email = "email_example"; // String | Filter by email
    Long idLte = 56L; // Long | Retrieve accounts with an ID lower or equal to the specified value
    Long idGte = 56L; // Long | Retrieve accounts with an ID greater or equal to the specified value
    try {
      List<ShortAccount> result = apiInstance.privateInstitutionAccountsList(page, pageSize, limit, offset, isActive, institutionUserId, email, idLte, idGte);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstitutionsApi#privateInstitutionAccountsList");
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
| **isActive** | **Long**| Filter by active status | [optional] |
| **institutionUserId** | **String**| Filter by institution_user_id | [optional] |
| **email** | **String**| Filter by email | [optional] |
| **idLte** | **Long**| Retrieve accounts with an ID lower or equal to the specified value | [optional] |
| **idGte** | **Long**| Retrieve accounts with an ID greater or equal to the specified value | [optional] |

### Return type

[**List&lt;ShortAccount&gt;**](ShortAccount.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. An array of Accounts |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateInstitutionAccountsSearch"></a>
# **privateInstitutionAccountsSearch**
> List&lt;ShortAccount&gt; privateInstitutionAccountsSearch(institutionAccountsSearch)

Private Account Institution Accounts Search

Returns the accounts for which the account has administrative privileges (assigned and inherited).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstitutionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    InstitutionsApi apiInstance = new InstitutionsApi(defaultClient);
    InstitutionAccountsSearch institutionAccountsSearch = new InstitutionAccountsSearch(); // InstitutionAccountsSearch | Search Parameters
    try {
      List<ShortAccount> result = apiInstance.privateInstitutionAccountsSearch(institutionAccountsSearch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstitutionsApi#privateInstitutionAccountsSearch");
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
| **institutionAccountsSearch** | [**InstitutionAccountsSearch**](InstitutionAccountsSearch.md)| Search Parameters | |

### Return type

[**List&lt;ShortAccount&gt;**](ShortAccount.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. An array of Accounts |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateInstitutionAccountsUpdate"></a>
# **privateInstitutionAccountsUpdate**
> privateInstitutionAccountsUpdate(accountId, accountUpdate)

Update Institution Account

Update Institution Account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstitutionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    InstitutionsApi apiInstance = new InstitutionsApi(defaultClient);
    Long accountId = 56L; // Long | Account identifier the user is associated to
    AccountUpdate accountUpdate = new AccountUpdate(); // AccountUpdate | Account description
    try {
      apiInstance.privateInstitutionAccountsUpdate(accountId, accountUpdate);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstitutionsApi#privateInstitutionAccountsUpdate");
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
| **accountId** | **Long**| Account identifier the user is associated to | |
| **accountUpdate** | [**AccountUpdate**](AccountUpdate.md)| Account description | |

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

<a id="privateInstitutionArticles"></a>
# **privateInstitutionArticles**
> List&lt;Article&gt; privateInstitutionArticles(page, pageSize, limit, offset, order, orderDirection, publishedSince, modifiedSince, status, resourceDoi, itemType)

Private Institution Articles

Get Articles from own institution. User must be administrator of the institution

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstitutionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    InstitutionsApi apiInstance = new InstitutionsApi(defaultClient);
    Long page = 56L; // Long | Page number. Used for pagination with page_size
    Long pageSize = 10L; // Long | The number of results included on a page. Used for pagination with page
    Long limit = 56L; // Long | Number of results included on a page. Used for pagination with query
    Long offset = 56L; // Long | Where to start the listing(the offset of the first result). Used for pagination with limit
    String order = "published_date"; // String | The field by which to order. Default varies by endpoint/resource.
    String orderDirection = "asc"; // String | 
    String publishedSince = "publishedSince_example"; // String | Filter by article publishing date. Will only return articles published after the date. date(ISO 8601) YYYY-MM-DD
    String modifiedSince = "modifiedSince_example"; // String | Filter by article modified date. Will only return articles published after the date. date(ISO 8601) YYYY-MM-DD
    Long status = 56L; // Long | only return collections with this status
    String resourceDoi = "resourceDoi_example"; // String | only return collections with this resource_doi
    Long itemType = 56L; // Long | Only return articles with the respective type. Mapping for item_type is: 1 - Figure, 2 - Media, 3 - Dataset, 5 - Poster, 6 - Journal contribution, 7 - Presentation, 8 - Thesis, 9 - Software, 11 - Online resource, 12 - Preprint, 13 - Book, 14 - Conference contribution, 15 - Chapter, 16 - Peer review, 17 - Educational resource, 18 - Report, 19 - Standard, 20 - Composition, 21 - Funding, 22 - Physical object, 23 - Data management plan, 24 - Workflow, 25 - Monograph, 26 - Performance, 27 - Event, 28 - Service, 29 - Model
    try {
      List<Article> result = apiInstance.privateInstitutionArticles(page, pageSize, limit, offset, order, orderDirection, publishedSince, modifiedSince, status, resourceDoi, itemType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstitutionsApi#privateInstitutionArticles");
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
| **order** | **String**| The field by which to order. Default varies by endpoint/resource. | [optional] [default to published_date] [enum: published_date, modified_date, views, shares, downloads, cites] |
| **orderDirection** | **String**|  | [optional] [default to desc] [enum: asc, desc] |
| **publishedSince** | **String**| Filter by article publishing date. Will only return articles published after the date. date(ISO 8601) YYYY-MM-DD | [optional] |
| **modifiedSince** | **String**| Filter by article modified date. Will only return articles published after the date. date(ISO 8601) YYYY-MM-DD | [optional] |
| **status** | **Long**| only return collections with this status | [optional] |
| **resourceDoi** | **String**| only return collections with this resource_doi | [optional] |
| **itemType** | **Long**| Only return articles with the respective type. Mapping for item_type is: 1 - Figure, 2 - Media, 3 - Dataset, 5 - Poster, 6 - Journal contribution, 7 - Presentation, 8 - Thesis, 9 - Software, 11 - Online resource, 12 - Preprint, 13 - Book, 14 - Conference contribution, 15 - Chapter, 16 - Peer review, 17 - Educational resource, 18 - Report, 19 - Standard, 20 - Composition, 21 - Funding, 22 - Physical object, 23 - Data management plan, 24 - Workflow, 25 - Monograph, 26 - Performance, 27 - Event, 28 - Service, 29 - Model | [optional] |

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
| **200** | OK. An array of articles belonging to the institution |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateInstitutionDetails"></a>
# **privateInstitutionDetails**
> Institution privateInstitutionDetails()

Private Account Institutions

Account institution details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstitutionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    InstitutionsApi apiInstance = new InstitutionsApi(defaultClient);
    try {
      Institution result = apiInstance.privateInstitutionDetails();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstitutionsApi#privateInstitutionDetails");
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

[**Institution**](Institution.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. An array of institutions |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateInstitutionEmbargoOptionsDetails"></a>
# **privateInstitutionEmbargoOptionsDetails**
> List&lt;GroupEmbargoOptions&gt; privateInstitutionEmbargoOptionsDetails()

Private Account Institution embargo options

Account institution embargo options details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstitutionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    InstitutionsApi apiInstance = new InstitutionsApi(defaultClient);
    try {
      List<GroupEmbargoOptions> result = apiInstance.privateInstitutionEmbargoOptionsDetails();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstitutionsApi#privateInstitutionEmbargoOptionsDetails");
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

[**List&lt;GroupEmbargoOptions&gt;**](GroupEmbargoOptions.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. An array of embargo options |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateInstitutionGroupsList"></a>
# **privateInstitutionGroupsList**
> List&lt;Group&gt; privateInstitutionGroupsList()

Private Account Institution Groups

Returns the groups for which the account has administrative privileges (assigned and inherited).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstitutionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    InstitutionsApi apiInstance = new InstitutionsApi(defaultClient);
    try {
      List<Group> result = apiInstance.privateInstitutionGroupsList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstitutionsApi#privateInstitutionGroupsList");
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

[**List&lt;Group&gt;**](Group.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. An array of Groups |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateInstitutionRolesList"></a>
# **privateInstitutionRolesList**
> List&lt;Role&gt; privateInstitutionRolesList()

Private Account Institution Roles

Returns the roles available for groups and the institution group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstitutionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    InstitutionsApi apiInstance = new InstitutionsApi(defaultClient);
    try {
      List<Role> result = apiInstance.privateInstitutionRolesList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstitutionsApi#privateInstitutionRolesList");
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

[**List&lt;Role&gt;**](Role.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. An array of Roles |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **500** | Internal Server Error |  -  |

