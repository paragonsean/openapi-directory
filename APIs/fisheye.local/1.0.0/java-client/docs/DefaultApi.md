# DefaultApi

All URIs are relative to *http://fisheye.local/context*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**findSliceData**](DefaultApi.md#findSliceData) | **GET** /rest-service-fe/commit-graph-v1/slice/{repository} |  |
| [**getAllRepositories**](DefaultApi.md#getAllRepositories) | **GET** /rest-service-fe/repositories-v1 |  |
| [**getChangeset**](DefaultApi.md#getChangeset) | **GET** /rest-service-fe/revisionData-v1/changeset/{repository}/{csid} |  |
| [**getChangesetDetails**](DefaultApi.md#getChangesetDetails) | **POST** /rest-service-fe/commit-graph-v1/details/{repository} |  |
| [**getChangesetsForText**](DefaultApi.md#getChangesetsForText) | **GET** /rest-service-fe/changeset-v1/listChangesets |  |
| [**getCrossRepositoryQuery**](DefaultApi.md#getCrossRepositoryQuery) | **GET** /rest-service-fe/search-v1/crossRepositoryQuery |  |
| [**getPathList**](DefaultApi.md#getPathList) | **GET** /rest-service-fe/revisionData-v1/pathList/{repository} |  |
| [**getQuery**](DefaultApi.md#getQuery) | **GET** /rest-service-fe/search-v1/query/{repository} |  |
| [**getQueryAsRows**](DefaultApi.md#getQueryAsRows) | **GET** /rest-service-fe/search-v1/queryAsRows/{repository} |  |
| [**getRepositoryInfo**](DefaultApi.md#getRepositoryInfo) | **GET** /rest-service-fe/repositories-v1/{repository} |  |
| [**getReviewsForChangeset**](DefaultApi.md#getReviewsForChangeset) | **POST** /rest-service-fe/search-v1/reviewsForChangeset/{repository} |  |
| [**getReviewsForChangesets**](DefaultApi.md#getReviewsForChangesets) | **POST** /rest-service-fe/search-v1/reviewsForChangesets/{repository} |  |
| [**getRevisionInfo**](DefaultApi.md#getRevisionInfo) | **GET** /rest-service-fe/revisionData-v1/revisionInfo/{repository} |  |
| [**listChangesets**](DefaultApi.md#listChangesets) | **GET** /rest-service-fe/revisionData-v1/changesetList/{repository} |  |
| [**listPathHistory**](DefaultApi.md#listPathHistory) | **GET** /rest-service-fe/revisionData-v1/pathHistory/{repository} |  |
| [**listTagsForRevision**](DefaultApi.md#listTagsForRevision) | **GET** /rest-service-fe/revisionData-v1/revisionTags/{repository} |  |


<a id="findSliceData"></a>
# **findSliceData**
> findSliceData(repository, branch, id, direction, size)



finds slice data the query

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fisheye.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String repository = "repository_example"; // String | the key of the repository to search
    String branch = "branch_example"; // String | the set of branches to search. If not specified, will search all branches
    String id = "id_example"; // String | the id of the changeset which we are
    String direction = "around"; // String | the direction to traverse. May be \"before\", \"after\" or \"around\"
    Integer size = 50; // Integer | the number of changesets to return in the slice
    try {
      apiInstance.findSliceData(repository, branch, id, direction, size);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#findSliceData");
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
| **repository** | **String**| the key of the repository to search | |
| **branch** | **String**| the set of branches to search. If not specified, will search all branches | [optional] |
| **id** | **String**| the id of the changeset which we are | [optional] |
| **direction** | **String**| the direction to traverse. May be \&quot;before\&quot;, \&quot;after\&quot; or \&quot;around\&quot; | [optional] [default to around] |
| **size** | **Integer**| the number of changesets to return in the slice | [optional] [default to 50] |

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
| **200** | Successful Response |  -  |

<a id="getAllRepositories"></a>
# **getAllRepositories**
> getAllRepositories()



List all the repositories.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fisheye.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.getAllRepositories();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getAllRepositories");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getChangeset"></a>
# **getChangeset**
> getChangeset(csid, repository)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fisheye.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String csid = "csid_example"; // String | the ChangesetID of the changeset to return.
    String repository = "repository_example"; // String | the key of the repository to query.
    try {
      apiInstance.getChangeset(csid, repository);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getChangeset");
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
| **csid** | **String**| the ChangesetID of the changeset to return. | |
| **repository** | **String**| the key of the repository to query. | |

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
| **200** | Successful Response |  -  |

<a id="getChangesetDetails"></a>
# **getChangesetDetails**
> getChangesetDetails(repository)



Retrieves detailed information about a set of changesets in a repository, designed to be used with the FishEye commit graph

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fisheye.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String repository = "repository_example"; // String | the key of the repository
    try {
      apiInstance.getChangesetDetails(repository);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getChangesetDetails");
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
| **repository** | **String**| the key of the repository | |

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
| **200** | Successful Response |  -  |

<a id="getChangesetsForText"></a>
# **getChangesetsForText**
> getChangesetsForText(rep, path, committer, comment, p4JobFixed, expand, beforeCsid)



List of changesets from a repository.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fisheye.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String rep = "rep_example"; // String | the key of the repository
    String path = "path_example"; // String | repository path
    String committer = "committer_example"; // String | ID of the committer
    String comment = "comment_example"; // String | comment to match
    String p4JobFixed = "p4JobFixed_example"; // String | Perforce option to select the changesets marked as fixing
    String expand = "expand_example"; // String | expand query parameter to specify the maximum number of results
    String beforeCsid = "beforeCsid_example"; // String | parent of the changesets
    try {
      apiInstance.getChangesetsForText(rep, path, committer, comment, p4JobFixed, expand, beforeCsid);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getChangesetsForText");
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
| **rep** | **String**| the key of the repository | [optional] |
| **path** | **String**| repository path | [optional] |
| **committer** | **String**| ID of the committer | [optional] |
| **comment** | **String**| comment to match | [optional] |
| **p4JobFixed** | **String**| Perforce option to select the changesets marked as fixing | [optional] |
| **expand** | **String**| expand query parameter to specify the maximum number of results | [optional] |
| **beforeCsid** | **String**| parent of the changesets | [optional] |

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
| **200** | Successful Response |  -  |

<a id="getCrossRepositoryQuery"></a>
# **getCrossRepositoryQuery**
> getCrossRepositoryQuery(query, repository, expand)



Execute a query across repositories. By default, this will search all repositories.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fisheye.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String query = "query_example"; // String | text to search for in commit message and p4 jobId. Must not be empty.
    String repository = "repository_example"; // String | restrict search to only these repositories (by their keys)
    String expand = "expand_example"; // String | expand query parameter to specify the maximum number of results. Format is changesets[n:m].revisions[n:m],reviews         the default number of changesets returned is 30, the maximum returned is 100
    try {
      apiInstance.getCrossRepositoryQuery(query, repository, expand);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getCrossRepositoryQuery");
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
| **query** | **String**| text to search for in commit message and p4 jobId. Must not be empty. | [optional] |
| **repository** | **String**| restrict search to only these repositories (by their keys) | [optional] |
| **expand** | **String**| expand query parameter to specify the maximum number of results. Format is changesets[n:m].revisions[n:m],reviews         the default number of changesets returned is 30, the maximum returned is 100 | [optional] |

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
| **200** | Successful Response |  -  |

<a id="getPathList"></a>
# **getPathList**
> getPathList(repository, path)



Get a list of information about files and directories in a path.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fisheye.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String repository = "repository_example"; // String | the key of the repository to query.
    String path = "path_example"; // String | the path to query, with respect to the fisheye repository root.
    try {
      apiInstance.getPathList(repository, path);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getPathList");
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
| **repository** | **String**| the key of the repository to query. | |
| **path** | **String**| the path to query, with respect to the fisheye repository root. | [optional] |

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
| **200** | Successful Response |  -  |

<a id="getQuery"></a>
# **getQuery**
> getQuery(repository, query, maxReturn)



Execute a FishEye query against a specific repository.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fisheye.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String repository = "repository_example"; // String | the key of the repository
    String query = "query_example"; // String | FishEye query to execute
    String maxReturn = "maxReturn_example"; // String | maximum number of results (which can be left unspecified, but in that case,  the maximum number of results will set to 3000 results)
    try {
      apiInstance.getQuery(repository, query, maxReturn);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getQuery");
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
| **repository** | **String**| the key of the repository | |
| **query** | **String**| FishEye query to execute | [optional] |
| **maxReturn** | **String**| maximum number of results (which can be left unspecified, but in that case,  the maximum number of results will set to 3000 results) | [optional] |

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
| **200** | Successful Response |  -  |

<a id="getQueryAsRows"></a>
# **getQueryAsRows**
> getQueryAsRows(repository, query, maxReturn)



Execute a FishEye query (that contains a \&quot;return\&quot; statement) against a specific repository.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fisheye.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String repository = "repository_example"; // String | the key of the repository
    String query = "query_example"; // String | FishEye query to execute (which must contain a \"return\" statement)
    String maxReturn = "maxReturn_example"; // String | maximum number of results (which can be left unspecified, but in that case,  the maximum number of results will set to 3000 results)
    try {
      apiInstance.getQueryAsRows(repository, query, maxReturn);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getQueryAsRows");
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
| **repository** | **String**| the key of the repository | |
| **query** | **String**| FishEye query to execute (which must contain a \&quot;return\&quot; statement) | [optional] |
| **maxReturn** | **String**| maximum number of results (which can be left unspecified, but in that case,  the maximum number of results will set to 3000 results) | [optional] |

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
| **200** | Successful Response |  -  |

<a id="getRepositoryInfo"></a>
# **getRepositoryInfo**
> getRepositoryInfo(repository)



Get the information about a repository.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fisheye.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String repository = "repository_example"; // String | the key of the repository
    try {
      apiInstance.getRepositoryInfo(repository);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getRepositoryInfo");
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
| **repository** | **String**| the key of the repository | |

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
| **200** | Successful Response |  -  |

<a id="getReviewsForChangeset"></a>
# **getReviewsForChangeset**
> getReviewsForChangeset(repository)



Retrieve a list of reviews for a changeset in a given repository.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fisheye.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String repository = "repository_example"; // String | the key of the repository
    try {
      apiInstance.getReviewsForChangeset(repository);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getReviewsForChangeset");
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
| **repository** | **String**| the key of the repository | |

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
| **200** | Successful Response |  -  |

<a id="getReviewsForChangesets"></a>
# **getReviewsForChangesets**
> getReviewsForChangesets(repository)



Retrieve a list of reviews for each given changeset in a given repository.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fisheye.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String repository = "repository_example"; // String | the key of the repository
    try {
      apiInstance.getReviewsForChangesets(repository);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getReviewsForChangesets");
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
| **repository** | **String**| the key of the repository | |

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
| **200** | Successful Response |  -  |

<a id="getRevisionInfo"></a>
# **getRevisionInfo**
> getRevisionInfo(repository, path, revision)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fisheye.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String repository = "repository_example"; // String | the key of the repository to query.
    String path = "path_example"; // String | the path of the filerevision, with respect to the fisheye repository root.
    String revision = "revision_example"; // String | the id of the filerevision to retrieve.
    try {
      apiInstance.getRevisionInfo(repository, path, revision);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getRevisionInfo");
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
| **repository** | **String**| the key of the repository to query. | |
| **path** | **String**| the path of the filerevision, with respect to the fisheye repository root. | [optional] |
| **revision** | **String**| the id of the filerevision to retrieve. | [optional] |

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
| **200** | Successful Response |  -  |

<a id="listChangesets"></a>
# **listChangesets**
> listChangesets(repository, path, start, end, maxReturn)



Get a list of changesets on a repository.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fisheye.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String repository = "repository_example"; // String | the key of the repository to query.
    String path = "path_example"; // String | restrict the changesets to those in this path, should be \"/\" to look at the whole repository.
    String start = "start_example"; // String | only return changesets after this date.
    String end = "end_example"; // String | only return changesets before this date.
    String maxReturn = "maxReturn_example"; // String | the maximum number of changesets to return.
    try {
      apiInstance.listChangesets(repository, path, start, end, maxReturn);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listChangesets");
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
| **repository** | **String**| the key of the repository to query. | |
| **path** | **String**| restrict the changesets to those in this path, should be \&quot;/\&quot; to look at the whole repository. | [optional] |
| **start** | **String**| only return changesets after this date. | [optional] |
| **end** | **String**| only return changesets before this date. | [optional] |
| **maxReturn** | **String**| the maximum number of changesets to return. | [optional] |

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
| **200** | Successful Response |  -  |

<a id="listPathHistory"></a>
# **listPathHistory**
> listPathHistory(repository, path)



Get a list of the file revisions for a specific path.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fisheye.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String repository = "repository_example"; // String | the key of the repository to query.
    String path = "path_example"; // String | the path to query.
    try {
      apiInstance.listPathHistory(repository, path);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listPathHistory");
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
| **repository** | **String**| the key of the repository to query. | |
| **path** | **String**| the path to query. | [optional] |

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
| **200** | Successful Response |  -  |

<a id="listTagsForRevision"></a>
# **listTagsForRevision**
> listTagsForRevision(repository, path, revision)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fisheye.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String repository = "repository_example"; // String | the key of the repository to query.
    String path = "path_example"; // String | the path of the filerevision, with respect to the fisheye repository root.
    String revision = "revision_example"; // String | the id of the filerevision to retrieve.
    try {
      apiInstance.listTagsForRevision(repository, path, revision);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listTagsForRevision");
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
| **repository** | **String**| the key of the repository to query. | |
| **path** | **String**| the path of the filerevision, with respect to the fisheye repository root. | [optional] |
| **revision** | **String**| the id of the filerevision to retrieve. | [optional] |

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
| **200** | Successful Response |  -  |

