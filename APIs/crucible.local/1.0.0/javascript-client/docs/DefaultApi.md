# Crucible.DefaultApi

All URIs are relative to *http://crucible.local/context*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addChangesetToReview**](DefaultApi.md#addChangesetToReview) | **POST** /rest-service/reviews-v1/{id}/addChangeset | 
[**addFile**](DefaultApi.md#addFile) | **POST** /rest-service/reviews-v1/{id}/addFile | 
[**addFisheyeReviewItem**](DefaultApi.md#addFisheyeReviewItem) | **POST** /rest-service/reviews-v1/{id}/reviewitems | 
[**addGeneralComment**](DefaultApi.md#addGeneralComment) | **POST** /rest-service/reviews-v1/{id}/comments | 
[**addPatchReview0**](DefaultApi.md#addPatchReview0) | **POST** /rest-service/reviews-v1/{id}/addPatch | 
[**addPatchToReview**](DefaultApi.md#addPatchToReview) | **POST** /rest-service/reviews-v1/{id}/patch | 
[**addReply**](DefaultApi.md#addReply) | **POST** /rest-service/reviews-v1/{id}/comments/{cId}/replies | 
[**addReviewItem**](DefaultApi.md#addReviewItem) | **POST** /rest-service/reviews-v1/{id}/reviewitems/details | 
[**addReviewItemRevisions**](DefaultApi.md#addReviewItemRevisions) | **POST** /rest-service/reviews-v1/{id}/reviewitems/{riId}/revisions | 
[**addReviewItems**](DefaultApi.md#addReviewItems) | **POST** /rest-service/reviews-v1/{id}/reviewitems/revisions | 
[**addReviewers**](DefaultApi.md#addReviewers) | **POST** /rest-service/reviews-v1/{id}/reviewers | 
[**addVersionedComment**](DefaultApi.md#addVersionedComment) | **POST** /rest-service/reviews-v1/{id}/reviewitems/{riId}/comments | 
[**browse**](DefaultApi.md#browse) | **GET** /rest-service/repositories-v1/browse/{repository}/{path} | 
[**change**](DefaultApi.md#change) | **GET** /rest-service/repositories-v1/change/{repository}/{revision} | 
[**changeState**](DefaultApi.md#changeState) | **POST** /rest-service/reviews-v1/{id}/transition | 
[**changes**](DefaultApi.md#changes) | **GET** /rest-service/repositories-v1/changes/{repository}/{path} | 
[**closeReviewWithComment**](DefaultApi.md#closeReviewWithComment) | **POST** /rest-service/reviews-v1/{id}/close | 
[**completeReview**](DefaultApi.md#completeReview) | **POST** /rest-service/reviews-v1/{id}/complete | 
[**createReview**](DefaultApi.md#createReview) | **POST** /rest-service/reviews-v1 | 
[**deleteReview**](DefaultApi.md#deleteReview) | **DELETE** /rest-service/reviews-v1/{id} | 
[**details**](DefaultApi.md#details) | **GET** /rest-service/repositories-v1/{repository}/{revision}/{path} | 
[**getAllComments**](DefaultApi.md#getAllComments) | **GET** /rest-service/reviews-v1/{id}/comments | 
[**getAllDetailedReviews**](DefaultApi.md#getAllDetailedReviews) | **GET** /rest-service/reviews-v1/details | 
[**getAllProjects**](DefaultApi.md#getAllProjects) | **GET** /rest-service/projects-v1 | 
[**getAllRepositories**](DefaultApi.md#getAllRepositories) | **GET** /rest-service/repositories-v1 | 
[**getAllReviews**](DefaultApi.md#getAllReviews) | **GET** /rest-service/reviews-v1 | 
[**getAvailableActions**](DefaultApi.md#getAvailableActions) | **GET** /rest-service/reviews-v1/{id}/actions | 
[**getAvailableTransitions**](DefaultApi.md#getAvailableTransitions) | **GET** /rest-service/reviews-v1/{id}/transitions | 
[**getComment**](DefaultApi.md#getComment) | **GET** /rest-service/reviews-v1/{id}/comments/{cId} | 
[**getCompletedReviewers**](DefaultApi.md#getCompletedReviewers) | **GET** /rest-service/reviews-v1/{id}/reviewers/completed | 
[**getContents**](DefaultApi.md#getContents) | **GET** /rest-service/repositories-v1/content/{repository}/{revision}/{path} | 
[**getCustomFilterReviews**](DefaultApi.md#getCustomFilterReviews) | **GET** /rest-service/reviews-v1/filter | 
[**getDetailedCustomFilterReviews**](DefaultApi.md#getDetailedCustomFilterReviews) | **GET** /rest-service/reviews-v1/filter/details | 
[**getDetailedFilteredReviewsForUser**](DefaultApi.md#getDetailedFilteredReviewsForUser) | **GET** /rest-service/reviews-v1/filter/{filter}/details | 
[**getDetailedReview**](DefaultApi.md#getDetailedReview) | **GET** /rest-service/reviews-v1/{id}/details | 
[**getFilteredReviewsForUser**](DefaultApi.md#getFilteredReviewsForUser) | **GET** /rest-service/reviews-v1/filter/{filter} | 
[**getGeneralComments**](DefaultApi.md#getGeneralComments) | **GET** /rest-service/reviews-v1/{id}/comments/general | 
[**getMappedUser**](DefaultApi.md#getMappedUser) | **GET** /rest-service/users-v1/{repository}/{username} | 
[**getMetrics**](DefaultApi.md#getMetrics) | **GET** /rest-service/reviews-v1/metrics/{version} | 
[**getProject**](DefaultApi.md#getProject) | **GET** /rest-service/projects-v1/{key} | 
[**getReplies**](DefaultApi.md#getReplies) | **GET** /rest-service/reviews-v1/{id}/comments/{cId}/replies | 
[**getRepositoryDetails**](DefaultApi.md#getRepositoryDetails) | **GET** /rest-service/repositories-v1/{repository} | 
[**getReview**](DefaultApi.md#getReview) | **GET** /rest-service/reviews-v1/{id} | 
[**getReviewItem**](DefaultApi.md#getReviewItem) | **GET** /rest-service/reviews-v1/{id}/reviewitems/{riId} | 
[**getReviewItemsComments**](DefaultApi.md#getReviewItemsComments) | **GET** /rest-service/reviews-v1/{id}/reviewitems/{riId}/comments | 
[**getReviewItemsForReview**](DefaultApi.md#getReviewItemsForReview) | **GET** /rest-service/reviews-v1/{id}/reviewitems | 
[**getReviewPatches**](DefaultApi.md#getReviewPatches) | **GET** /rest-service/reviews-v1/{id}/patch | 
[**getReviewers**](DefaultApi.md#getReviewers) | **GET** /rest-service/reviews-v1/{id}/reviewers | 
[**getReviewsDetailsForPath**](DefaultApi.md#getReviewsDetailsForPath) | **GET** /rest-service/reviews-v1/search/{repository}/details | 
[**getReviewsForIssueKey**](DefaultApi.md#getReviewsForIssueKey) | **GET** /rest-service/search-v1/reviewsForIssue | 
[**getReviewsForPath**](DefaultApi.md#getReviewsForPath) | **GET** /rest-service/reviews-v1/search/{repository} | 
[**getReviewsForTerm**](DefaultApi.md#getReviewsForTerm) | **GET** /rest-service/search-v1/reviews | 
[**getSvnRepositoryDetails**](DefaultApi.md#getSvnRepositoryDetails) | **GET** /rest-service/repositories-v1/{repository}/svn | 
[**getUncompletedReviewers**](DefaultApi.md#getUncompletedReviewers) | **GET** /rest-service/reviews-v1/{id}/reviewers/uncompleted | 
[**getUserProfile**](DefaultApi.md#getUserProfile) | **GET** /rest-service/users-v1/{username} | 
[**getUsers**](DefaultApi.md#getUsers) | **GET** /rest-service/users-v1 | 
[**getVersionInfo**](DefaultApi.md#getVersionInfo) | **GET** /rest-service/reviews-v1/versionInfo | 
[**getVersionedComments**](DefaultApi.md#getVersionedComments) | **GET** /rest-service/reviews-v1/{id}/comments/versioned | 
[**history**](DefaultApi.md#history) | **GET** /rest-service/repositories-v1/history/{repository}/{revision}/{path} | 
[**login**](DefaultApi.md#login) | **GET** /rest-service/auth-v1/login | 
[**loginPost**](DefaultApi.md#loginPost) | **POST** /rest-service/auth-v1/login | 
[**markAllCommentsAsRead**](DefaultApi.md#markAllCommentsAsRead) | **POST** /rest-service/reviews-v1/{id}/comments/markAllAsRead | 
[**markCommentAsLeaveUnread**](DefaultApi.md#markCommentAsLeaveUnread) | **POST** /rest-service/reviews-v1/{id}/comments/{cId}/markAsLeaveUnread | 
[**markCommentAsRead**](DefaultApi.md#markCommentAsRead) | **POST** /rest-service/reviews-v1/{id}/comments/{cId}/markAsRead | 
[**postCustomFilterReviews**](DefaultApi.md#postCustomFilterReviews) | **POST** /rest-service/reviews-v1/filter | 
[**postDetailedCustomFilterReviews**](DefaultApi.md#postDetailedCustomFilterReviews) | **POST** /rest-service/reviews-v1/filter/details | 
[**publishAllComments**](DefaultApi.md#publishAllComments) | **POST** /rest-service/reviews-v1/{id}/publish | 
[**publishComment**](DefaultApi.md#publishComment) | **POST** /rest-service/reviews-v1/{id}/publish/{cId} | 
[**remindIncompleteReviewers**](DefaultApi.md#remindIncompleteReviewers) | **POST** /rest-service/reviews-v1/{id}/remind | 
[**removeComment**](DefaultApi.md#removeComment) | **DELETE** /rest-service/reviews-v1/{id}/comments/{cId} | 
[**removePatch**](DefaultApi.md#removePatch) | **DELETE** /rest-service/reviews-v1/{id}/patch/{patchId} | 
[**removeReply**](DefaultApi.md#removeReply) | **DELETE** /rest-service/reviews-v1/{id}/comments/{cId}/replies/{rId} | 
[**removeReviewItem**](DefaultApi.md#removeReviewItem) | **DELETE** /rest-service/reviews-v1/{id}/reviewitems/{riId} | 
[**removeReviewItemRevisions**](DefaultApi.md#removeReviewItemRevisions) | **DELETE** /rest-service/reviews-v1/{id}/reviewitems/{riId}/revisions | 
[**removeReviewer**](DefaultApi.md#removeReviewer) | **DELETE** /rest-service/reviews-v1/{id}/reviewers/{username} | 
[**setReviewItem**](DefaultApi.md#setReviewItem) | **PUT** /rest-service/reviews-v1/{id}/reviewitems/{riId}/details | 
[**uncompleteReview**](DefaultApi.md#uncompleteReview) | **POST** /rest-service/reviews-v1/{id}/uncomplete | 
[**updateComment**](DefaultApi.md#updateComment) | **POST** /rest-service/reviews-v1/{id}/comments/{cId} | 
[**updateReply**](DefaultApi.md#updateReply) | **POST** /rest-service/reviews-v1/{id}/comments/{cId}/replies/{rId} | 



## addChangesetToReview

> addChangesetToReview(id)



### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let id = "id_example"; // String | the perm id of the review to add the changeset to
apiInstance.addChangesetToReview(id, (error, data, response) => {
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
 **id** | **String**| the perm id of the review to add the changeset to | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## addFile

> addFile(id)



### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let id = "id_example"; // String | the review perma id to add the file
apiInstance.addFile(id, (error, data, response) => {
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
 **id** | **String**| the review perma id to add the file | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## addFisheyeReviewItem

> addFisheyeReviewItem(id)



Add the changes between two files in a fisheye repository to the review.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let id = "id_example"; // String | the id of the review (e.g. \"CR-362\").
apiInstance.addFisheyeReviewItem(id, (error, data, response) => {
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
 **id** | **String**| the id of the review (e.g. \&quot;CR-362\&quot;). | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## addGeneralComment

> addGeneralComment(id)



Add a general comment to the review.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let id = "id_example"; // String | the review perma-id
apiInstance.addGeneralComment(id, (error, data, response) => {
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
 **id** | **String**| the review perma-id | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## addPatchReview0

> addPatchReview0(id)



Old, non-restful name. Kept for backwards compatibility. Exactly the same as POSTing to /{id}/patch

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let id = "id_example"; // String | 
apiInstance.addPatchReview0(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## addPatchToReview

> addPatchToReview(id)



Add the revisions in a patch to an existing review.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let id = "id_example"; // String | the review id to get the patches for
apiInstance.addPatchToReview(id, (error, data, response) => {
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
 **id** | **String**| the review id to get the patches for | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## addReply

> addReply(id, cId)



Adds a reply to the given comment. This call includes the  repsonse header that  contains the URL of the newly created entity.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let id = "id_example"; // String | the review perma-id (e.g. \"CR-45\").
let cId = "cId_example"; // String | the comment to reply to
apiInstance.addReply(id, cId, (error, data, response) => {
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
 **id** | **String**| the review perma-id (e.g. \&quot;CR-45\&quot;). | 
 **cId** | **String**| the comment to reply to | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## addReviewItem

> addReviewItem(id)



Adds the given review item to the review. This will always create a new review item, even if there is an existing  one with the same data in the review (in which case the existing item will be replaced).

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let id = "id_example"; // String | the id of the review (e.g. \"CR-362\").
apiInstance.addReviewItem(id, (error, data, response) => {
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
 **id** | **String**| the id of the review (e.g. \&quot;CR-362\&quot;). | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## addReviewItemRevisions

> addReviewItemRevisions(riId, id, opts)



Adds the given list of revisions to the supplied review item, merging if required. For example, if the review  item for  contains revisions 3 to 6, and if:

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let riId = "riId_example"; // String | the id of the review item (e.g. \"CFR-5622\").
let id = "id_example"; // String | the id of the review (e.g. \"CR-345\").
let opts = {
  'rev': "rev_example" // String | a list of revisions to add to the review item, merging if required. If a revision already exists  in the given review item, then the given revision is ignored.
};
apiInstance.addReviewItemRevisions(riId, id, opts, (error, data, response) => {
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
 **riId** | **String**| the id of the review item (e.g. \&quot;CFR-5622\&quot;). | 
 **id** | **String**| the id of the review (e.g. \&quot;CR-345\&quot;). | 
 **rev** | **String**| a list of revisions to add to the review item, merging if required. If a revision already exists  in the given review item, then the given revision is ignored. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## addReviewItems

> addReviewItems(id)



Adds a review item for each of the supplied crucibleRevisionData elements.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let id = "id_example"; // String | the id of the review (e.g. \"CR-362\").
apiInstance.addReviewItems(id, (error, data, response) => {
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
 **id** | **String**| the id of the review (e.g. \&quot;CR-362\&quot;). | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## addReviewers

> addReviewers(id)



Adds the given list of reviewers to the review.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let id = "id_example"; // String | the id of the review to add to
apiInstance.addReviewers(id, (error, data, response) => {
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
 **id** | **String**| the id of the review to add to | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## addVersionedComment

> addVersionedComment(riId, id)



This call includes the  repsonse header that contains the URL of the newly created entity.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let riId = "riId_example"; // String | the review item id.
let id = "id_example"; // String | the review perma id
apiInstance.addVersionedComment(riId, id, (error, data, response) => {
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
 **riId** | **String**| the review item id. | 
 **id** | **String**| the review perma id | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## browse

> browse(path, repository)



Lists the contents of the specified directory.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let path = "path_example"; // String | path to a directory. When path represents a file name, the result is unspecified.
let repository = "repository_example"; // String | the key of the Crucible SCM plugin repository.
apiInstance.browse(path, repository, (error, data, response) => {
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
 **path** | **String**| path to a directory. When path represents a file name, the result is unspecified. | 
 **repository** | **String**| the key of the Crucible SCM plugin repository. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## change

> change(repository, revision)



Represents a particular changeset.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let repository = "repository_example"; // String | the key of the Crucible SCM plugin repository.
let revision = "revision_example"; // String | the SCM revision string.
apiInstance.change(repository, revision, (error, data, response) => {
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
 **repository** | **String**| the key of the Crucible SCM plugin repository. | 
 **revision** | **String**| the SCM revision string. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## changeState

> changeState(id, opts)



Change the state of a review by performing an action on it.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let id = "id_example"; // String | the review perma-id (e.g. \"CR-45\").
let opts = {
  'action': "action_example", // String | the string representation of the action to perform. Valid actions are:    Note:
  'ignoreWarnings': true // Boolean | if  then condition failure warnings will be ignored
};
apiInstance.changeState(id, opts, (error, data, response) => {
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
 **id** | **String**| the review perma-id (e.g. \&quot;CR-45\&quot;). | 
 **action** | **String**| the string representation of the action to perform. Valid actions are:    Note: | [optional] 
 **ignoreWarnings** | **Boolean**| if  then condition failure warnings will be ignored | [optional] [default to true]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## changes

> changes(path, repository, opts)



Represents a sorted list of changesets, newest first.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let path = "path_example"; // String | only show change sets which contain at least one revision with a path under this path.  Changesets with some revisions outside this path still include all revisions.  i.e. Revisions outside the path are *not* excluded from the change set.
let repository = "repository_example"; // String | the key of the Crucible SCM plugin repository.
let opts = {
  'oldestCsid': "oldestCsid_example", // String | only return change sets after this change set. If omitted there is no restriction.
  'includeOldest': true, // Boolean | include the change set with id \"from\" in the change sets returned.
  'newestCsid': "newestCsid_example", // String | only return change sets before this change set. If omitted there is no restriction.
  'includeNewest': true, // Boolean | include the change set with id \"to\" in the change sets returned.
  'max': 56 // Number | return only the newest change sets, to a maximum of maxChangesets.
};
apiInstance.changes(path, repository, opts, (error, data, response) => {
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
 **path** | **String**| only show change sets which contain at least one revision with a path under this path.  Changesets with some revisions outside this path still include all revisions.  i.e. Revisions outside the path are *not* excluded from the change set. | 
 **repository** | **String**| the key of the Crucible SCM plugin repository. | 
 **oldestCsid** | **String**| only return change sets after this change set. If omitted there is no restriction. | [optional] 
 **includeOldest** | **Boolean**| include the change set with id \&quot;from\&quot; in the change sets returned. | [optional] 
 **newestCsid** | **String**| only return change sets before this change set. If omitted there is no restriction. | [optional] 
 **includeNewest** | **Boolean**| include the change set with id \&quot;to\&quot; in the change sets returned. | [optional] 
 **max** | **Number**| return only the newest change sets, to a maximum of maxChangesets. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## closeReviewWithComment

> closeReviewWithComment(id)



Closes the given review with the summary given.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let id = "id_example"; // String | the review perma id to close. it should be in the open state.
apiInstance.closeReviewWithComment(id, (error, data, response) => {
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
 **id** | **String**| the review perma id to close. it should be in the open state. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## completeReview

> completeReview(id, opts)



Completes the review for the current user

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let id = "id_example"; // String | the review perma id
let opts = {
  'ignoreWarnings': true // Boolean | if {@code ignoreWarnings==true} then condition failure warnings will be ignored
};
apiInstance.completeReview(id, opts, (error, data, response) => {
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
 **id** | **String**| the review perma id | 
 **ignoreWarnings** | **Boolean**| if {@code ignoreWarnings&#x3D;&#x3D;true} then condition failure warnings will be ignored | [optional] [default to true]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## createReview

> createReview()



### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
apiInstance.createReview((error, data, response) => {
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


## deleteReview

> deleteReview(id)



Permanently deletes the specified review.  The review must have been abandoned.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let id = "id_example"; // String | the permId of the review to delete (e.g. \"CR-45\").
apiInstance.deleteReview(id, (error, data, response) => {
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
 **id** | **String**| the permId of the review to delete (e.g. \&quot;CR-45\&quot;). | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## details

> details(path, repository, revision)



### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let path = "path_example"; // String | the path of a file or versioned directory (note that  versioned directories are not supported by all SCM plugins).
let repository = "repository_example"; // String | the key of the Crucible SCM plugin repository.
let revision = "revision_example"; // String | the SCM revision string.
apiInstance.details(path, repository, revision, (error, data, response) => {
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
 **path** | **String**| the path of a file or versioned directory (note that  versioned directories are not supported by all SCM plugins). | 
 **repository** | **String**| the key of the Crucible SCM plugin repository. | 
 **revision** | **String**| the SCM revision string. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getAllComments

> getAllComments(id, opts)



Return all the comments visible to the requesting user for the review.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let id = "id_example"; // String | the review perma-id
let opts = {
  'render': false // Boolean | indicate whether to render the wiki text in the returned comments. If set to \"true\", the comments will contain a  <messageAsHtml> element containing the wiki rendered html.
};
apiInstance.getAllComments(id, opts, (error, data, response) => {
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
 **id** | **String**| the review perma-id | 
 **render** | **Boolean**| indicate whether to render the wiki text in the returned comments. If set to \&quot;true\&quot;, the comments will contain a  &lt;messageAsHtml&gt; element containing the wiki rendered html. | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getAllDetailedReviews

> getAllDetailedReviews(opts)



Retrieves all reviews that are in one of the the specified states. For each review all details are included (review items + comments). The  wiki rendered comments will be available via the &lt;messageAsHtml&gt; element

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let opts = {
  'state': "state_example" // String | the review states to match.
};
apiInstance.getAllDetailedReviews(opts, (error, data, response) => {
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
 **state** | **String**| the review states to match. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getAllProjects

> getAllProjects(opts)



Get the list of projects that the authenticated user is entitled to access.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let opts = {
  'excludeAllowedReviewers': false // Boolean | if set to true, user data (e.g. allowedReviewers) which is expensive  to compute, will not be included in the response data. Defaults to false so allowedReviewers are included in the response.
};
apiInstance.getAllProjects(opts, (error, data, response) => {
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
 **excludeAllowedReviewers** | **Boolean**| if set to true, user data (e.g. allowedReviewers) which is expensive  to compute, will not be included in the response data. Defaults to false so allowedReviewers are included in the response. | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getAllRepositories

> getAllRepositories(opts)



Returns a list of all repositories. This includes plugin provided repositories

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let opts = {
  'name': "name_example", // String | filter repositories by the repository key, only repositories of keys containing this value  would be returned if value was provided.  Case insensitive.
  'enabled': true, // Boolean | filter repositories by enabled flag.  Only enabled/disabled repositories would be returned  accordingly if value was provided.
  'available': true, // Boolean | filter repositories by its availability.  Only available/unavailable repositories would be returned  accordingly if value was provided.
  'type': "type_example", // String | filter repositories by type.  Allowed values: cvs, svn, p4, git, hg, plugin (for light SCM repositories).  Parameter can be specified more than once.
  'limit': 10000 // Number | maximum number of repositories to be returned.
};
apiInstance.getAllRepositories(opts, (error, data, response) => {
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
 **name** | **String**| filter repositories by the repository key, only repositories of keys containing this value  would be returned if value was provided.  Case insensitive. | [optional] 
 **enabled** | **Boolean**| filter repositories by enabled flag.  Only enabled/disabled repositories would be returned  accordingly if value was provided. | [optional] 
 **available** | **Boolean**| filter repositories by its availability.  Only available/unavailable repositories would be returned  accordingly if value was provided. | [optional] 
 **type** | **String**| filter repositories by type.  Allowed values: cvs, svn, p4, git, hg, plugin (for light SCM repositories).  Parameter can be specified more than once. | [optional] 
 **limit** | **Number**| maximum number of repositories to be returned. | [optional] [default to 10000]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getAllReviews

> getAllReviews(opts)



### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let opts = {
  'state': "state_example" // String | only return reviews that are in these states.
};
apiInstance.getAllReviews(opts, (error, data, response) => {
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
 **state** | **String**| only return reviews that are in these states. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getAvailableActions

> getAvailableActions(id)



Get a list of the actions which the current user is allowed to perform  on the review.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let id = "id_example"; // String | the permId of the a review (e.g. \"CR-45\").
apiInstance.getAvailableActions(id, (error, data, response) => {
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
 **id** | **String**| the permId of the a review (e.g. \&quot;CR-45\&quot;). | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getAvailableTransitions

> getAvailableTransitions(id)



Get a list of the actions which the current user can perform on this  review, given its current state and the user&#39;s permissions.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let id = "id_example"; // String | the permId of the a review (e.g. \"CR-45\").
apiInstance.getAvailableTransitions(id, (error, data, response) => {
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
 **id** | **String**| the permId of the a review (e.g. \&quot;CR-45\&quot;). | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getComment

> getComment(id, cId, opts)



Gets the given comment.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let id = "id_example"; // String | the perma id of the review
let cId = "cId_example"; // String | the id of the comment
let opts = {
  'render': false // Boolean | true if the wiki text should be rendered into html, into the field <messageAsHtml>.
};
apiInstance.getComment(id, cId, opts, (error, data, response) => {
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
 **id** | **String**| the perma id of the review | 
 **cId** | **String**| the id of the comment | 
 **render** | **Boolean**| true if the wiki text should be rendered into html, into the field &lt;messageAsHtml&gt;. | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getCompletedReviewers

> getCompletedReviewers(id)



Gets a list of completed reviewers.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let id = "id_example"; // String | the review perma id to retrieve reviewers
apiInstance.getCompletedReviewers(id, (error, data, response) => {
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
 **id** | **String**| the review perma id to retrieve reviewers | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getContents

> getContents(path, repository, revision)



Returns the raw content of the specified file revision as a binary  stream. No attempt is made to identify the content type and no mime  type is provided.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let path = "path_example"; // String | the path of a file.
let repository = "repository_example"; // String | the key of the Crucible SCM plugin repository.
let revision = "revision_example"; // String | the SCM revision string.
apiInstance.getContents(path, repository, revision, (error, data, response) => {
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
 **path** | **String**| the path of a file. | 
 **repository** | **String**| the key of the Crucible SCM plugin repository. | 
 **revision** | **String**| the SCM revision string. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getCustomFilterReviews

> getCustomFilterReviews(opts)



To ignore a property, omit it from the query string.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let opts = {
  'title': "title_example", // String | a string that will be searched for in review titles.
  'author': "author_example", // String | reviews authored by this user.
  'moderator': "moderator_example", // String | reviews moderated by this user.
  'creator': "creator_example", // String | reviews created by this user.
  'states': "states_example", // String | comma-separated list of amy of the following strings: (Draft,  Approval, Review, Summarize, Closed, Dead, Rejected, Unknown).
  'reviewer': "reviewer_example", // String | reviews reviewed by this user.
  'orRoles': true, // Boolean | whether the value of , ,   and  should be OR'd  () or AND'd ()  together.
  'complete': true, // Boolean | reviews that the specified reviewer has completed.
  'allReviewersComplete': true, // Boolean | Reviews that all reviewers have completed.
  'project': "project_example", // String | reviews for the specified project.
  'fromDate': 789, // Number | reviews with last activity date after the specified timestamp, in milliseconds. Inclusive.
  'toDate': 789 // Number | reviews with last activity date before the specified timestamp, in milliseconds. Inclusive.
};
apiInstance.getCustomFilterReviews(opts, (error, data, response) => {
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
 **title** | **String**| a string that will be searched for in review titles. | [optional] 
 **author** | **String**| reviews authored by this user. | [optional] 
 **moderator** | **String**| reviews moderated by this user. | [optional] 
 **creator** | **String**| reviews created by this user. | [optional] 
 **states** | **String**| comma-separated list of amy of the following strings: (Draft,  Approval, Review, Summarize, Closed, Dead, Rejected, Unknown). | [optional] 
 **reviewer** | **String**| reviews reviewed by this user. | [optional] 
 **orRoles** | **Boolean**| whether the value of , ,   and  should be OR&#39;d  () or AND&#39;d ()  together. | [optional] 
 **complete** | **Boolean**| reviews that the specified reviewer has completed. | [optional] 
 **allReviewersComplete** | **Boolean**| Reviews that all reviewers have completed. | [optional] 
 **project** | **String**| reviews for the specified project. | [optional] 
 **fromDate** | **Number**| reviews with last activity date after the specified timestamp, in milliseconds. Inclusive. | [optional] 
 **toDate** | **Number**| reviews with last activity date before the specified timestamp, in milliseconds. Inclusive. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getDetailedCustomFilterReviews

> getDetailedCustomFilterReviews(opts)



To ignore a property, omit it from the query string.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let opts = {
  'title': "title_example", // String | a string that will be searched for in review titles.
  'author': "author_example", // String | reviews authored by this user.
  'moderator': "moderator_example", // String | reviews moderated by this user.
  'creator': "creator_example", // String | reviews created by this user.
  'states': "states_example", // String | comma-separated list of amy of the following strings: (Draft,  Approval, Review, Summarize, Closed, Dead, Rejected, Unknown).
  'reviewer': "reviewer_example", // String | reviews reviewed by this user.
  'orRoles': true, // Boolean | whether the value of , ,   and  should be OR'd  () or AND'd ()  together.
  'complete': true, // Boolean | reviews that the specified reviewer has completed.
  'allReviewersComplete': true, // Boolean | Reviews that all reviewers have completed.
  'project': "project_example", // String | reviews for the specified project.
  'fromDate': 789, // Number | reviews with last activity date after the specified timestamp, in milliseconds. Inclusive.
  'toDate': 789 // Number | reviews with last activity date before the specified timestamp, in milliseconds. Inclusive.
};
apiInstance.getDetailedCustomFilterReviews(opts, (error, data, response) => {
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
 **title** | **String**| a string that will be searched for in review titles. | [optional] 
 **author** | **String**| reviews authored by this user. | [optional] 
 **moderator** | **String**| reviews moderated by this user. | [optional] 
 **creator** | **String**| reviews created by this user. | [optional] 
 **states** | **String**| comma-separated list of amy of the following strings: (Draft,  Approval, Review, Summarize, Closed, Dead, Rejected, Unknown). | [optional] 
 **reviewer** | **String**| reviews reviewed by this user. | [optional] 
 **orRoles** | **Boolean**| whether the value of , ,   and  should be OR&#39;d  () or AND&#39;d ()  together. | [optional] 
 **complete** | **Boolean**| reviews that the specified reviewer has completed. | [optional] 
 **allReviewersComplete** | **Boolean**| Reviews that all reviewers have completed. | [optional] 
 **project** | **String**| reviews for the specified project. | [optional] 
 **fromDate** | **Number**| reviews with last activity date after the specified timestamp, in milliseconds. Inclusive. | [optional] 
 **toDate** | **Number**| reviews with last activity date before the specified timestamp, in milliseconds. Inclusive. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getDetailedFilteredReviewsForUser

> getDetailedFilteredReviewsForUser(filter)



Gets a list of all the reviews that match the specified filter criteria.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let filter = "filter_example"; // String | a predefined filter type.
apiInstance.getDetailedFilteredReviewsForUser(filter, (error, data, response) => {
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
 **filter** | **String**| a predefined filter type. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getDetailedReview

> getDetailedReview(id)



Returns the specified review.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let id = "id_example"; // String | the permId of the review (e.g. \"CR-45\").
apiInstance.getDetailedReview(id, (error, data, response) => {
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
 **id** | **String**| the permId of the review (e.g. \&quot;CR-45\&quot;). | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getFilteredReviewsForUser

> getFilteredReviewsForUser(filter)



Get all the reviews which match the given filter, for the current user.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let filter = "filter_example"; // String | a predefined filter type.
apiInstance.getFilteredReviewsForUser(filter, (error, data, response) => {
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
 **filter** | **String**| a predefined filter type. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getGeneralComments

> getGeneralComments(id, opts)



### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let id = "id_example"; // String | review perma-id
let opts = {
  'render': false // Boolean | indicate whether to render the wiki text in the returned comments. If set to \"true\", the comments will contain a  <messageAsHtml> element containing the wiki rendered html.
};
apiInstance.getGeneralComments(id, opts, (error, data, response) => {
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
 **id** | **String**| review perma-id | 
 **render** | **Boolean**| indicate whether to render the wiki text in the returned comments. If set to \&quot;true\&quot;, the comments will contain a  &lt;messageAsHtml&gt; element containing the wiki rendered html. | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getMappedUser

> getMappedUser(repository, username)



Returns the user details of the user mapped to a committer in a repository.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let repository = "repository_example"; // String | the key of the repository
let username = "username_example"; // String | the name of the committer
apiInstance.getMappedUser(repository, username, (error, data, response) => {
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
 **username** | **String**| the name of the committer | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getMetrics

> getMetrics(version)



Get comment metrics metadata for the specified metrics version.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let version = "version_example"; // String | a metrics version.
apiInstance.getMetrics(version, (error, data, response) => {
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
 **version** | **String**| a metrics version. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getProject

> getProject(key, opts)



Returns a project description.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let key = "key_example"; // String | the key of a Crucible project.
let opts = {
  'excludeAllowedReviewers': false // Boolean | 
};
apiInstance.getProject(key, opts, (error, data, response) => {
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
 **key** | **String**| the key of a Crucible project. | 
 **excludeAllowedReviewers** | **Boolean**|  | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getReplies

> getReplies(id, cId, opts)



Gets the replies to the given comment.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let id = "id_example"; // String | the review perma-id (e.g. \"CR-45\").
let cId = "cId_example"; // String | the comment to reply to
let opts = {
  'render': false // Boolean | true if the comments should also be rendered into html, into the element <messageAsHtml>
};
apiInstance.getReplies(id, cId, opts, (error, data, response) => {
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
 **id** | **String**| the review perma-id (e.g. \&quot;CR-45\&quot;). | 
 **cId** | **String**| the comment to reply to | 
 **render** | **Boolean**| true if the comments should also be rendered into html, into the element &lt;messageAsHtml&gt; | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getRepositoryDetails

> getRepositoryDetails(repository)



### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let repository = "repository_example"; // String | the key of the Crucible SCM plugin repository.
apiInstance.getRepositoryDetails(repository, (error, data, response) => {
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
 **repository** | **String**| the key of the Crucible SCM plugin repository. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getReview

> getReview(id)



Get a single review by its permId (e.g. \&quot;CR-45\&quot;).  If the review does not exist, a 404 is returned.    The moderator element may not exist if the review does not have a Moderator.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let id = "id_example"; // String | the permId of the review to delete (e.g. \"CR-45\").
apiInstance.getReview(id, (error, data, response) => {
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
 **id** | **String**| the permId of the review to delete (e.g. \&quot;CR-45\&quot;). | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getReviewItem

> getReviewItem(riId, id)



Returns detailed information for a specific review item.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let riId = "riId_example"; // String | review item id (e.g. \"CFR-6312\").
let id = "id_example"; // String | review id (e.g. \"CR-345\").
apiInstance.getReviewItem(riId, id, (error, data, response) => {
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
 **riId** | **String**| review item id (e.g. \&quot;CFR-6312\&quot;). | 
 **id** | **String**| review id (e.g. \&quot;CR-345\&quot;). | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getReviewItemsComments

> getReviewItemsComments(riId, id, opts)



### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let riId = "riId_example"; // String | the review item id.
let id = "id_example"; // String | the review perma id
let opts = {
  'render': false // Boolean | indicate whether to render the wiki text in the returned comments. If set to \"true\", the comments will contain a  <messageAsHtml> element containing the wiki rendered html.
};
apiInstance.getReviewItemsComments(riId, id, opts, (error, data, response) => {
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
 **riId** | **String**| the review item id. | 
 **id** | **String**| the review perma id | 
 **render** | **Boolean**| indicate whether to render the wiki text in the returned comments. If set to \&quot;true\&quot;, the comments will contain a  &lt;messageAsHtml&gt; element containing the wiki rendered html. | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getReviewItemsForReview

> getReviewItemsForReview(id)



Returns a list of all the items in a review.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let id = "id_example"; // String | the id of the review (e.g. \"CR-362\").
apiInstance.getReviewItemsForReview(id, (error, data, response) => {
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
 **id** | **String**| the id of the review (e.g. \&quot;CR-362\&quot;). | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getReviewPatches

> getReviewPatches(id)



Get a list of patches and their details for the given review

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let id = "id_example"; // String | the review id to get the patches for
apiInstance.getReviewPatches(id, (error, data, response) => {
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
 **id** | **String**| the review id to get the patches for | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getReviewers

> getReviewers(id)



Get a list of reviewers in the review given by the permaid id.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let id = "id_example"; // String | the id of the review to add to
apiInstance.getReviewers(id, (error, data, response) => {
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
 **id** | **String**| the id of the review to add to | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getReviewsDetailsForPath

> getReviewsDetailsForPath(repository, opts)



Return a list of Reviews which include a particular file.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let repository = "repository_example"; // String | the key of the repository to search for file.
let opts = {
  'path': "path_example" // String | path to find in reviews.
};
apiInstance.getReviewsDetailsForPath(repository, opts, (error, data, response) => {
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
 **repository** | **String**| the key of the repository to search for file. | 
 **path** | **String**| path to find in reviews. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getReviewsForIssueKey

> getReviewsForIssueKey(opts)



Get a list of all reviews that have been linked to the specified JIRA issue key.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let opts = {
  'jiraKey': "jiraKey_example", // String | a Jira issue key (e.g. \"FOO-3453\")
  'maxReturn': "maxReturn_example" // String | the maximum number of reviews to return.
};
apiInstance.getReviewsForIssueKey(opts, (error, data, response) => {
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
 **jiraKey** | **String**| a Jira issue key (e.g. \&quot;FOO-3453\&quot;) | [optional] 
 **maxReturn** | **String**| the maximum number of reviews to return. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getReviewsForPath

> getReviewsForPath(repository, opts)



Return a list of Reviews which include a particular file.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let repository = "repository_example"; // String | the key of the repository to search for file
let opts = {
  'path': "path_example" // String | path to find in reviews
};
apiInstance.getReviewsForPath(repository, opts, (error, data, response) => {
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
 **repository** | **String**| the key of the repository to search for file | 
 **path** | **String**| path to find in reviews | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getReviewsForTerm

> getReviewsForTerm(opts)



Search for reviews where the name, description, state or permaId contain the specified term.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let opts = {
  'term': "term_example", // String | a search term.
  'maxReturn': "maxReturn_example" // String | the maximum number of reviews to return.
};
apiInstance.getReviewsForTerm(opts, (error, data, response) => {
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
 **term** | **String**| a search term. | [optional] 
 **maxReturn** | **String**| the maximum number of reviews to return. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getSvnRepositoryDetails

> getSvnRepositoryDetails(repository)



For backward compatibility we provide this method, but repositories should be referred to just by their key.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let repository = "repository_example"; // String | the key of a FishEye or Crucible SCM plugin repository
apiInstance.getSvnRepositoryDetails(repository, (error, data, response) => {
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
 **repository** | **String**| the key of a FishEye or Crucible SCM plugin repository | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getUncompletedReviewers

> getUncompletedReviewers(id)



Gets a list of reviewers that have not completed the review.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let id = "id_example"; // String | the review perma id to retrieve reviewers
apiInstance.getUncompletedReviewers(id, (error, data, response) => {
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
 **id** | **String**| the review perma id to retrieve reviewers | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getUserProfile

> getUserProfile(username)



Returns the user&#39;s profile details.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let username = "username_example"; // String | the username of the user
apiInstance.getUserProfile(username, (error, data, response) => {
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
 **username** | **String**| the username of the user | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getUsers

> getUsers(opts)



Get a list of all the users. You can also ask for a set of users.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let opts = {
  'username': "username_example" // String | a username (or a few) to limit the number of returned entries. It will return only existing users.
};
apiInstance.getUsers(opts, (error, data, response) => {
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
 **username** | **String**| a username (or a few) to limit the number of returned entries. It will return only existing users. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getVersionInfo

> getVersionInfo()



Returns Crucible version information.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
apiInstance.getVersionInfo((error, data, response) => {
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


## getVersionedComments

> getVersionedComments(id, opts)



### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let id = "id_example"; // String | review perma-id
let opts = {
  'render': false // Boolean | indicate whether to render the wiki text in the returned comments. If set to \"true\", the comments will contain a  <messageAsHtml> element containing the wiki rendered html.
};
apiInstance.getVersionedComments(id, opts, (error, data, response) => {
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
 **id** | **String**| review perma-id | 
 **render** | **Boolean**| indicate whether to render the wiki text in the returned comments. If set to \&quot;true\&quot;, the comments will contain a  &lt;messageAsHtml&gt; element containing the wiki rendered html. | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## history

> history(path, repository, revision)



Represents the history of a versioned entity.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let path = "path_example"; // String | the path of a file or versioned directory (note that  versioned directories are not supported by all SCM plugins).
let repository = "repository_example"; // String | the key of the Crucible SCM plugin repository.
let revision = "revision_example"; // String | the SCM revision string.
apiInstance.history(path, repository, revision, (error, data, response) => {
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
 **path** | **String**| the path of a file or versioned directory (note that  versioned directories are not supported by all SCM plugins). | 
 **repository** | **String**| the key of the Crucible SCM plugin repository. | 
 **revision** | **String**| the SCM revision string. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## login

> login(opts)



Get the user authentication token.    This is a legacy version of the login request. Using GET is deprecated as your password is likely to appear in logs which record request URLs.  Use the POST version instead.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let opts = {
  'userName': "userName_example", // String | the username of the user to get the token for
  'password': "password_example" // String | the password for the user to get the token for
};
apiInstance.login(opts, (error, data, response) => {
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
 **userName** | **String**| the username of the user to get the token for | [optional] 
 **password** | **String**| the password for the user to get the token for | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## loginPost

> loginPost()



Get the user authentication token.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
apiInstance.loginPost((error, data, response) => {
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


## markAllCommentsAsRead

> markAllCommentsAsRead(id)



For the effective user, mark all comments in a review as read (except  those marked as leave unread).

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let id = "id_example"; // String | the review perma-id (e.g. \"CR-45\").
apiInstance.markAllCommentsAsRead(id, (error, data, response) => {
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
 **id** | **String**| the review perma-id (e.g. \&quot;CR-45\&quot;). | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## markCommentAsLeaveUnread

> markCommentAsLeaveUnread(id, cId)



Marks the comment as leave unread to the current user - it will not automatically be marked as read by crucible.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let id = "id_example"; // String | the review perma id for the comment
let cId = "cId_example"; // String | the comment perma id
apiInstance.markCommentAsLeaveUnread(id, cId, (error, data, response) => {
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
 **id** | **String**| the review perma id for the comment | 
 **cId** | **String**| the comment perma id | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## markCommentAsRead

> markCommentAsRead(id, cId)



Mark the given comment as read for the user used to make this POST.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let id = "id_example"; // String | the review perma id
let cId = "cId_example"; // String | the comment perma id.
apiInstance.markCommentAsRead(id, cId, (error, data, response) => {
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
 **id** | **String**| the review perma id | 
 **cId** | **String**| the comment perma id. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## postCustomFilterReviews

> postCustomFilterReviews()



This method should no longer be used, as it uses a POST for a read-only  retrieval operation and is provided for backward compatibility only.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
apiInstance.postCustomFilterReviews((error, data, response) => {
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


## postDetailedCustomFilterReviews

> postDetailedCustomFilterReviews()



This method should no longer be used, as it uses a POST for a read-only  retrieval operation and is provided for backward compatibility only.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
apiInstance.postDetailedCustomFilterReviews((error, data, response) => {
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


## publishAllComments

> publishAllComments(id)



Publishes all the draft comments of the current user.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let id = "id_example"; // String | the review perma id to look for draft comments
apiInstance.publishAllComments(id, (error, data, response) => {
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
 **id** | **String**| the review perma id to look for draft comments | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## publishComment

> publishComment(id, cId)



publishes the given draft comment.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let id = "id_example"; // String | the review perma id
let cId = "cId_example"; // String | the comment perma id
apiInstance.publishComment(id, cId, (error, data, response) => {
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
 **id** | **String**| the review perma id | 
 **cId** | **String**| the comment perma id | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## remindIncompleteReviewers

> remindIncompleteReviewers(id)



Immediately send a reminder to incomplete reviewers about the given review.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let id = "id_example"; // String | the review perma id to remind about. it should be in the open state.
apiInstance.remindIncompleteReviewers(id, (error, data, response) => {
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
 **id** | **String**| the review perma id to remind about. it should be in the open state. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## removeComment

> removeComment(id, cId)



Deletes the given comment.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let id = "id_example"; // String | the perma id of the review
let cId = "cId_example"; // String | the id of the comment
apiInstance.removeComment(id, cId, (error, data, response) => {
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
 **id** | **String**| the perma id of the review | 
 **cId** | **String**| the id of the comment | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## removePatch

> removePatch(patchId, id)



Removes the patch with the given id from the review. All of the revisions provided by the patch will be removed as well.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let patchId = 56; // Number | the id of the patch (as returned by the '{id}/patch' resource)
let id = "id_example"; // String | the permaId of the review
apiInstance.removePatch(patchId, id, (error, data, response) => {
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
 **patchId** | **Number**| the id of the patch (as returned by the &#39;{id}/patch&#39; resource) | 
 **id** | **String**| the permaId of the review | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## removeReply

> removeReply(id, rId, cId)



Deletes the reply.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let id = "id_example"; // String | The review perma id
let rId = "rId_example"; // String | the perma id of the reply to delete
let cId = "cId_example"; // String | the reply's parent comment perma id
apiInstance.removeReply(id, rId, cId, (error, data, response) => {
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
 **id** | **String**| The review perma id | 
 **rId** | **String**| the perma id of the reply to delete | 
 **cId** | **String**| the reply&#39;s parent comment perma id | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## removeReviewItem

> removeReviewItem(riId, id)



Removes an item from a review.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let riId = "riId_example"; // String | review item id (e.g. \"CFR-6312\").
let id = "id_example"; // String | review id (e.g. \"CR-345\").
apiInstance.removeReviewItem(riId, id, (error, data, response) => {
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
 **riId** | **String**| review item id (e.g. \&quot;CFR-6312\&quot;). | 
 **id** | **String**| review id (e.g. \&quot;CR-345\&quot;). | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## removeReviewItemRevisions

> removeReviewItemRevisions(riId, id, opts)



Removes the revisions given from the review item in the review specified by the id. If the review item has no  more revisions left, it is automatically deleted.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let riId = "riId_example"; // String | the id of the review item (e.g. \"CFR-5622\").
let id = "id_example"; // String | the id of the review (e.g. \"CR-345\").
let opts = {
  'rev': "rev_example" // String | a list of revisions to add to the review item, merging if required. If a revision already exists  in the given review item, then the given revision is ignored.
};
apiInstance.removeReviewItemRevisions(riId, id, opts, (error, data, response) => {
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
 **riId** | **String**| the id of the review item (e.g. \&quot;CFR-5622\&quot;). | 
 **id** | **String**| the id of the review (e.g. \&quot;CR-345\&quot;). | 
 **rev** | **String**| a list of revisions to add to the review item, merging if required. If a revision already exists  in the given review item, then the given revision is ignored. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## removeReviewer

> removeReviewer(id, username)



Removes the reviewer from the review.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let id = "id_example"; // String | the perma id of the review
let username = "username_example"; // String | the name of the reviewer.
apiInstance.removeReviewer(id, username, (error, data, response) => {
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
 **id** | **String**| the perma id of the review | 
 **username** | **String**| the name of the reviewer. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## setReviewItem

> setReviewItem(riId, id)



Sets the review item specified by itemId with the given reviewItem. The old review item is discarded. Can only  perform this operation if the old review item specified by itemId can be deleted. The old review item&#39;s permId is  not changed.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let riId = "riId_example"; // String | a valid review item id (e.g. \"CFR-5622\").
let id = "id_example"; // String | a valid review id (e.g. \"CR-345\").
apiInstance.setReviewItem(riId, id, (error, data, response) => {
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
 **riId** | **String**| a valid review item id (e.g. \&quot;CFR-5622\&quot;). | 
 **id** | **String**| a valid review id (e.g. \&quot;CR-345\&quot;). | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## uncompleteReview

> uncompleteReview(id, opts)



Uncompletes the review for the current user.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let id = "id_example"; // String | the review perma id
let opts = {
  'ignoreWarnings': true // Boolean | if {@code ignoreWarnings==true} then condition failure warnings will be ignored
};
apiInstance.uncompleteReview(id, opts, (error, data, response) => {
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
 **id** | **String**| the review perma id | 
 **ignoreWarnings** | **Boolean**| if {@code ignoreWarnings&#x3D;&#x3D;true} then condition failure warnings will be ignored | [optional] [default to true]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## updateComment

> updateComment(id, cId)



Updates the comment given by the perma id to the new comment posted.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let id = "id_example"; // String | the perma id of the review
let cId = "cId_example"; // String | the id of the comment
apiInstance.updateComment(id, cId, (error, data, response) => {
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
 **id** | **String**| the perma id of the review | 
 **cId** | **String**| the id of the comment | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## updateReply

> updateReply(id, rId, cId)



Updates a reply with the given newComment.

### Example

```javascript
import Crucible from 'crucible';

let apiInstance = new Crucible.DefaultApi();
let id = "id_example"; // String | The review perma id
let rId = "rId_example"; // String | the perma id of the reply to delete
let cId = "cId_example"; // String | the reply's parent comment perma id
apiInstance.updateReply(id, rId, cId, (error, data, response) => {
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
 **id** | **String**| The review perma id | 
 **rId** | **String**| the perma id of the reply to delete | 
 **cId** | **String**| the reply&#39;s parent comment perma id | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

