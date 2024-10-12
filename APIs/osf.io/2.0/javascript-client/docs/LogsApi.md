# OsfApiv2Documentation.LogsApi

All URIs are relative to *https://api.test.osf.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**logsActions**](LogsApi.md#logsActions) | **GET** /actions/ | Actions
[**logsRead**](LogsApi.md#logsRead) | **GET** /logs/{log_id}/ | Retrieve a log



## logsActions

> logsActions()

Actions

 A log can have one of many actions. The complete list of loggable actions (in the format {identifier}: {description}) is as follows: * &#x60;project_created&#x60;: A Node is created * &#x60;project_registered&#x60;: A Node is registered * &#x60;project_deleted&#x60;: A Node is deleted * &#x60;created_from&#x60;: A Node is created using an existing Node as a template * &#x60;pointer_created&#x60;: A Pointer is created * &#x60;pointer_forked&#x60;: A Pointer is forked * &#x60;pointer_removed&#x60;: A Pointer is removed * &#x60;node_removed&#x60;: A component is deleted * &#x60;node_forked&#x60;: A Node is forked --- * &#x60;made_public&#x60;: A Node is made public * &#x60;made_private&#x60;: A Node is made private * &#x60;tag_added&#x60;: A tag is added to a Node * &#x60;tag_removed&#x60;: A tag is removed from a Node * &#x60;edit_title&#x60;: A Node&#39;s title is changed * &#x60;edit_description&#x60;: A Node&#39;s description is changed * &#x60;updated_fields&#x60;: One or more of a Node&#39;s fields are changed * &#x60;external_ids_added&#x60;: An external identifier is added to a Node (e.g. DOI, ARK) * &#x60;view_only_link_added&#x60;: A view-only link was added to a Node * &#x60;view_only_link_removed&#x60;:  A view-only link was removed from a Node --- * &#x60;contributor_added&#x60;: A Contributor is added to a Node * &#x60;contributor_removed&#x60;: A Contributor is removed from a Node * &#x60;contributors_reordered&#x60;: A Contributor&#39;s position in a Node&#39;s bibliography is changed * &#x60;permissions_updated&#x60;: A Contributor&#x60;s permissions on a Node are changed * &#x60;made_contributor_visible&#x60;: A Contributor is made bibliographically visible on a Node * &#x60;made_contributor_invisible&#x60;: A Contributor is made bibliographically invisible on a Node --- * &#x60;wiki_updated&#x60;: A Node&#39;s wiki is updated * &#x60;wiki_deleted&#x60;: A Node&#39;s wiki is deleted * &#x60;wiki_renamed&#x60;: A Node&#39;s wiki is renamed * &#x60;made_wiki_public&#x60;: A Node&#39;s wiki is made public * &#x60;made_wiki_private&#x60;: A Node&#39;s wiki is made private --- * &#x60;addon_added&#x60;: An add-on is linked to a Node * &#x60;addon_removed&#x60;: An add-on is unlinked from a Node * &#x60;addon_file_moved&#x60;: A File in a Node&#39;s linked add-on is moved * &#x60;addon_file_copied&#x60;: A File in a Node&#39;s linked add-on is copied * &#x60;addon_file_renamed&#x60;: A File in a Node&#39;s linked add-on is renamed * &#x60;node_authorized&#x60;: An addon is authorized for a project * &#x60;node_deauthorized&#x60;: An addon is deauthorized for a project * &#x60;folder_created&#x60;: A Folder is created in a Node&#39;s linked add-on * &#x60;file_added&#x60;: A File is added to a Node&#39;s linked add-on * &#x60;file_updated&#x60;: A File is updated on a Node&#39;s linked add-on * &#x60;file_removed&#x60;: A File is removed from a Node&#39;s linked add-on * &#x60;file_restored&#x60;: A File is restored in a Node&#39;s linked add-on --- * &#x60;comment_added&#x60;: A Comment is added to some item * &#x60;comment_removed&#x60;: A Comment is removed from some item * &#x60;comment_updated&#x60;: A Comment is updated on some item --- * &#x60;embargo_initiated&#x60;: An embargoed Registration is proposed on a Node * &#x60;embargo_approved&#x60;: A proposed Embargo of a Node is approved * &#x60;embargo_cancelled&#x60;: A proposed Embargo of a Node is cancelled * &#x60;embargo_completed&#x60;: A proposed Embargo of a Node is completed * &#x60;retraction_initiated&#x60;: A Withdrawal of a Registration is proposed * &#x60;retraction_approved&#x60;: A Withdrawal of a Registration is approved * &#x60;retraction_cancelled&#x60;: A Withdrawal of a Registration is cancelled * &#x60;registration_initiated&#x60;: A Registration of a Node is proposed * &#x60;registration_approved&#x60;: A proposed Registration is approved * &#x60;registration_cancelled&#x60;: A proposed Registration is cancelled

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.LogsApi();
apiInstance.logsActions((error, data, response) => {
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


## logsRead

> Log logsRead(logId)

Retrieve a log

Retrieves the details of a log. A log is permanent immutable record of a node&#39;s history. A log is created when a user performs one of many actions. See the [actions](#Logs_logs_actions) section for more details. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the requested log, if the request was successful.  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.LogsApi();
let logId = "logId_example"; // String | The unique identifier of the log you wish to retrieve.
apiInstance.logsRead(logId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logId** | **String**| The unique identifier of the log you wish to retrieve. | 

### Return type

[**Log**](Log.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

