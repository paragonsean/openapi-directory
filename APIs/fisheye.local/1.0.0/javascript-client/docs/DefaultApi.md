# FishEye.DefaultApi

All URIs are relative to *http://fisheye.local/context*

Method | HTTP request | Description
------------- | ------------- | -------------
[**findSliceData**](DefaultApi.md#findSliceData) | **GET** /rest-service-fe/commit-graph-v1/slice/{repository} | 
[**getAllRepositories**](DefaultApi.md#getAllRepositories) | **GET** /rest-service-fe/repositories-v1 | 
[**getChangeset**](DefaultApi.md#getChangeset) | **GET** /rest-service-fe/revisionData-v1/changeset/{repository}/{csid} | 
[**getChangesetDetails**](DefaultApi.md#getChangesetDetails) | **POST** /rest-service-fe/commit-graph-v1/details/{repository} | 
[**getChangesetsForText**](DefaultApi.md#getChangesetsForText) | **GET** /rest-service-fe/changeset-v1/listChangesets | 
[**getCrossRepositoryQuery**](DefaultApi.md#getCrossRepositoryQuery) | **GET** /rest-service-fe/search-v1/crossRepositoryQuery | 
[**getPathList**](DefaultApi.md#getPathList) | **GET** /rest-service-fe/revisionData-v1/pathList/{repository} | 
[**getQuery**](DefaultApi.md#getQuery) | **GET** /rest-service-fe/search-v1/query/{repository} | 
[**getQueryAsRows**](DefaultApi.md#getQueryAsRows) | **GET** /rest-service-fe/search-v1/queryAsRows/{repository} | 
[**getRepositoryInfo**](DefaultApi.md#getRepositoryInfo) | **GET** /rest-service-fe/repositories-v1/{repository} | 
[**getReviewsForChangeset**](DefaultApi.md#getReviewsForChangeset) | **POST** /rest-service-fe/search-v1/reviewsForChangeset/{repository} | 
[**getReviewsForChangesets**](DefaultApi.md#getReviewsForChangesets) | **POST** /rest-service-fe/search-v1/reviewsForChangesets/{repository} | 
[**getRevisionInfo**](DefaultApi.md#getRevisionInfo) | **GET** /rest-service-fe/revisionData-v1/revisionInfo/{repository} | 
[**listChangesets**](DefaultApi.md#listChangesets) | **GET** /rest-service-fe/revisionData-v1/changesetList/{repository} | 
[**listPathHistory**](DefaultApi.md#listPathHistory) | **GET** /rest-service-fe/revisionData-v1/pathHistory/{repository} | 
[**listTagsForRevision**](DefaultApi.md#listTagsForRevision) | **GET** /rest-service-fe/revisionData-v1/revisionTags/{repository} | 



## findSliceData

> findSliceData(repository, opts)



finds slice data the query

### Example

```javascript
import FishEye from 'fish_eye';

let apiInstance = new FishEye.DefaultApi();
let repository = "repository_example"; // String | the key of the repository to search
let opts = {
  'branch': "branch_example", // String | the set of branches to search. If not specified, will search all branches
  'id': "id_example", // String | the id of the changeset which we are
  'direction': "'around'", // String | the direction to traverse. May be \"before\", \"after\" or \"around\"
  'size': 50 // Number | the number of changesets to return in the slice
};
apiInstance.findSliceData(repository, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **String**| the key of the repository to search | 
 **branch** | **String**| the set of branches to search. If not specified, will search all branches | [optional] 
 **id** | **String**| the id of the changeset which we are | [optional] 
 **direction** | **String**| the direction to traverse. May be \&quot;before\&quot;, \&quot;after\&quot; or \&quot;around\&quot; | [optional] [default to &#39;around&#39;]
 **size** | **Number**| the number of changesets to return in the slice | [optional] [default to 50]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getAllRepositories

> getAllRepositories()



List all the repositories.

### Example

```javascript
import FishEye from 'fish_eye';

let apiInstance = new FishEye.DefaultApi();
apiInstance.getAllRepositories((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## getChangeset

> getChangeset(csid, repository)



### Example

```javascript
import FishEye from 'fish_eye';

let apiInstance = new FishEye.DefaultApi();
let csid = "csid_example"; // String | the ChangesetID of the changeset to return.
let repository = "repository_example"; // String | the key of the repository to query.
apiInstance.getChangeset(csid, repository, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **csid** | **String**| the ChangesetID of the changeset to return. | 
 **repository** | **String**| the key of the repository to query. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getChangesetDetails

> getChangesetDetails(repository)



Retrieves detailed information about a set of changesets in a repository, designed to be used with the FishEye commit graph

### Example

```javascript
import FishEye from 'fish_eye';

let apiInstance = new FishEye.DefaultApi();
let repository = "repository_example"; // String | the key of the repository
apiInstance.getChangesetDetails(repository, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **String**| the key of the repository | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getChangesetsForText

> getChangesetsForText(opts)



List of changesets from a repository.

### Example

```javascript
import FishEye from 'fish_eye';

let apiInstance = new FishEye.DefaultApi();
let opts = {
  'rep': "rep_example", // String | the key of the repository
  'path': "path_example", // String | repository path
  'committer': "committer_example", // String | ID of the committer
  'comment': "comment_example", // String | comment to match
  'p4JobFixed': "p4JobFixed_example", // String | Perforce option to select the changesets marked as fixing
  'expand': "expand_example", // String | expand query parameter to specify the maximum number of results
  'beforeCsid': "beforeCsid_example" // String | parent of the changesets
};
apiInstance.getChangesetsForText(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rep** | **String**| the key of the repository | [optional] 
 **path** | **String**| repository path | [optional] 
 **committer** | **String**| ID of the committer | [optional] 
 **comment** | **String**| comment to match | [optional] 
 **p4JobFixed** | **String**| Perforce option to select the changesets marked as fixing | [optional] 
 **expand** | **String**| expand query parameter to specify the maximum number of results | [optional] 
 **beforeCsid** | **String**| parent of the changesets | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getCrossRepositoryQuery

> getCrossRepositoryQuery(opts)



Execute a query across repositories. By default, this will search all repositories.

### Example

```javascript
import FishEye from 'fish_eye';

let apiInstance = new FishEye.DefaultApi();
let opts = {
  'query': "query_example", // String | text to search for in commit message and p4 jobId. Must not be empty.
  'repository': "repository_example", // String | restrict search to only these repositories (by their keys)
  'expand': "expand_example" // String | expand query parameter to specify the maximum number of results. Format is changesets[n:m].revisions[n:m],reviews         the default number of changesets returned is 30, the maximum returned is 100
};
apiInstance.getCrossRepositoryQuery(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **String**| text to search for in commit message and p4 jobId. Must not be empty. | [optional] 
 **repository** | **String**| restrict search to only these repositories (by their keys) | [optional] 
 **expand** | **String**| expand query parameter to specify the maximum number of results. Format is changesets[n:m].revisions[n:m],reviews         the default number of changesets returned is 30, the maximum returned is 100 | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getPathList

> getPathList(repository, opts)



Get a list of information about files and directories in a path.

### Example

```javascript
import FishEye from 'fish_eye';

let apiInstance = new FishEye.DefaultApi();
let repository = "repository_example"; // String | the key of the repository to query.
let opts = {
  'path': "path_example" // String | the path to query, with respect to the fisheye repository root.
};
apiInstance.getPathList(repository, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **String**| the key of the repository to query. | 
 **path** | **String**| the path to query, with respect to the fisheye repository root. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getQuery

> getQuery(repository, opts)



Execute a FishEye query against a specific repository.

### Example

```javascript
import FishEye from 'fish_eye';

let apiInstance = new FishEye.DefaultApi();
let repository = "repository_example"; // String | the key of the repository
let opts = {
  'query': "query_example", // String | FishEye query to execute
  'maxReturn': "maxReturn_example" // String | maximum number of results (which can be left unspecified, but in that case,  the maximum number of results will set to 3000 results)
};
apiInstance.getQuery(repository, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **String**| the key of the repository | 
 **query** | **String**| FishEye query to execute | [optional] 
 **maxReturn** | **String**| maximum number of results (which can be left unspecified, but in that case,  the maximum number of results will set to 3000 results) | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getQueryAsRows

> getQueryAsRows(repository, opts)



Execute a FishEye query (that contains a \&quot;return\&quot; statement) against a specific repository.

### Example

```javascript
import FishEye from 'fish_eye';

let apiInstance = new FishEye.DefaultApi();
let repository = "repository_example"; // String | the key of the repository
let opts = {
  'query': "query_example", // String | FishEye query to execute (which must contain a \"return\" statement)
  'maxReturn': "maxReturn_example" // String | maximum number of results (which can be left unspecified, but in that case,  the maximum number of results will set to 3000 results)
};
apiInstance.getQueryAsRows(repository, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **String**| the key of the repository | 
 **query** | **String**| FishEye query to execute (which must contain a \&quot;return\&quot; statement) | [optional] 
 **maxReturn** | **String**| maximum number of results (which can be left unspecified, but in that case,  the maximum number of results will set to 3000 results) | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getRepositoryInfo

> getRepositoryInfo(repository)



Get the information about a repository.

### Example

```javascript
import FishEye from 'fish_eye';

let apiInstance = new FishEye.DefaultApi();
let repository = "repository_example"; // String | the key of the repository
apiInstance.getRepositoryInfo(repository, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **String**| the key of the repository | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getReviewsForChangeset

> getReviewsForChangeset(repository)



Retrieve a list of reviews for a changeset in a given repository.

### Example

```javascript
import FishEye from 'fish_eye';

let apiInstance = new FishEye.DefaultApi();
let repository = "repository_example"; // String | the key of the repository
apiInstance.getReviewsForChangeset(repository, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **String**| the key of the repository | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getReviewsForChangesets

> getReviewsForChangesets(repository)



Retrieve a list of reviews for each given changeset in a given repository.

### Example

```javascript
import FishEye from 'fish_eye';

let apiInstance = new FishEye.DefaultApi();
let repository = "repository_example"; // String | the key of the repository
apiInstance.getReviewsForChangesets(repository, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **String**| the key of the repository | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getRevisionInfo

> getRevisionInfo(repository, opts)



### Example

```javascript
import FishEye from 'fish_eye';

let apiInstance = new FishEye.DefaultApi();
let repository = "repository_example"; // String | the key of the repository to query.
let opts = {
  'path': "path_example", // String | the path of the filerevision, with respect to the fisheye repository root.
  'revision': "revision_example" // String | the id of the filerevision to retrieve.
};
apiInstance.getRevisionInfo(repository, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **String**| the key of the repository to query. | 
 **path** | **String**| the path of the filerevision, with respect to the fisheye repository root. | [optional] 
 **revision** | **String**| the id of the filerevision to retrieve. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## listChangesets

> listChangesets(repository, opts)



Get a list of changesets on a repository.

### Example

```javascript
import FishEye from 'fish_eye';

let apiInstance = new FishEye.DefaultApi();
let repository = "repository_example"; // String | the key of the repository to query.
let opts = {
  'path': "path_example", // String | restrict the changesets to those in this path, should be \"/\" to look at the whole repository.
  'start': "start_example", // String | only return changesets after this date.
  'end': "end_example", // String | only return changesets before this date.
  'maxReturn': "maxReturn_example" // String | the maximum number of changesets to return.
};
apiInstance.listChangesets(repository, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **String**| the key of the repository to query. | 
 **path** | **String**| restrict the changesets to those in this path, should be \&quot;/\&quot; to look at the whole repository. | [optional] 
 **start** | **String**| only return changesets after this date. | [optional] 
 **end** | **String**| only return changesets before this date. | [optional] 
 **maxReturn** | **String**| the maximum number of changesets to return. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## listPathHistory

> listPathHistory(repository, opts)



Get a list of the file revisions for a specific path.

### Example

```javascript
import FishEye from 'fish_eye';

let apiInstance = new FishEye.DefaultApi();
let repository = "repository_example"; // String | the key of the repository to query.
let opts = {
  'path': "path_example" // String | the path to query.
};
apiInstance.listPathHistory(repository, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **String**| the key of the repository to query. | 
 **path** | **String**| the path to query. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## listTagsForRevision

> listTagsForRevision(repository, opts)



### Example

```javascript
import FishEye from 'fish_eye';

let apiInstance = new FishEye.DefaultApi();
let repository = "repository_example"; // String | the key of the repository to query.
let opts = {
  'path': "path_example", // String | the path of the filerevision, with respect to the fisheye repository root.
  'revision': "revision_example" // String | the id of the filerevision to retrieve.
};
apiInstance.listTagsForRevision(repository, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **String**| the key of the repository to query. | 
 **path** | **String**| the path of the filerevision, with respect to the fisheye repository root. | [optional] 
 **revision** | **String**| the id of the filerevision to retrieve. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

