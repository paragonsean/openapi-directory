# DracoonApi.NodesApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addFavorite**](NodesApi.md#addFavorite) | **POST** /v4/nodes/{node_id}/favorite | Mark a node (room, folder or file) as favorite
[**addRoomGuestUsers**](NodesApi.md#addRoomGuestUsers) | **PUT** /v4/nodes/rooms/{room_id}/guest_users | Add guest users to a room
[**cancelFileUpload**](NodesApi.md#cancelFileUpload) | **DELETE** /v4/nodes/files/uploads/{upload_id} | Cancel file upload
[**changePendingAssignments**](NodesApi.md#changePendingAssignments) | **PUT** /v4/nodes/rooms/pending | Handle user-room assignments per group
[**completeFileUpload**](NodesApi.md#completeFileUpload) | **PUT** /v4/nodes/files/uploads/{upload_id} | Complete file upload
[**completeS3FileUpload**](NodesApi.md#completeS3FileUpload) | **PUT** /v4/nodes/files/uploads/{upload_id}/s3 | Complete S3 file upload
[**configureRoom**](NodesApi.md#configureRoom) | **PUT** /v4/nodes/rooms/{room_id}/config | Configure room
[**copyNodes**](NodesApi.md#copyNodes) | **POST** /v4/nodes/{node_id}/copy_to | Copy node(s)
[**createAndPreserveRoomRescueKeyPair**](NodesApi.md#createAndPreserveRoomRescueKeyPair) | **POST** /v4/nodes/rooms/{room_id}/keypairs | Create key pair and preserve copy of old private key
[**createFileUploadChannel**](NodesApi.md#createFileUploadChannel) | **POST** /v4/nodes/files/uploads | Create new file upload channel
[**createFolder**](NodesApi.md#createFolder) | **POST** /v4/nodes/folders | Create new folder
[**createNodeComment**](NodesApi.md#createNodeComment) | **POST** /v4/nodes/{node_id}/comments | Create node comment
[**createRoom**](NodesApi.md#createRoom) | **POST** /v4/nodes/rooms | Create new room
[**downloadZipArchive**](NodesApi.md#downloadZipArchive) | **POST** /v4/nodes/zip/download | Download files / folders as ZIP archive
[**emptyDeletedNodes**](NodesApi.md#emptyDeletedNodes) | **DELETE** /v4/nodes/{node_id}/deleted_nodes | Empty recycle bin
[**encryptRoom**](NodesApi.md#encryptRoom) | **PUT** /v4/nodes/rooms/{room_id}/encrypt | Encrypt room
[**generateDownloadUrl**](NodesApi.md#generateDownloadUrl) | **POST** /v4/nodes/files/{file_id}/downloads | Generate download URL
[**generateDownloadUrlForZipArchive**](NodesApi.md#generateDownloadUrlForZipArchive) | **POST** /v4/nodes/zip | Generate download URL for ZIP download
[**generatePresignedUrlsFiles**](NodesApi.md#generatePresignedUrlsFiles) | **POST** /v4/nodes/files/uploads/{upload_id}/s3_urls | Generate presigned URLs for S3 file upload
[**handleRoomWebhookAssignments**](NodesApi.md#handleRoomWebhookAssignments) | **PUT** /v4/nodes/rooms/{room_id}/webhooks | Assign or unassign webhooks to room
[**moveNodes**](NodesApi.md#moveNodes) | **POST** /v4/nodes/{node_id}/move_to | Move node(s)
[**removeDeletedNodes**](NodesApi.md#removeDeletedNodes) | **DELETE** /v4/nodes/deleted_nodes | Remove nodes from recycle bin
[**removeFavorite**](NodesApi.md#removeFavorite) | **DELETE** /v4/nodes/{node_id}/favorite | Unmark a node (room, folder or file) as favorite
[**removeNode**](NodesApi.md#removeNode) | **DELETE** /v4/nodes/{node_id} | Remove node
[**removeNodeComment**](NodesApi.md#removeNodeComment) | **DELETE** /v4/nodes/comments/{comment_id} | Remove node comment
[**removeNodes**](NodesApi.md#removeNodes) | **DELETE** /v4/nodes | Remove nodes
[**removeRoomRescueKeyPair**](NodesApi.md#removeRoomRescueKeyPair) | **DELETE** /v4/nodes/rooms/{room_id}/keypair | Remove rooms&#39;s rescue key pair
[**requestDeletedNode**](NodesApi.md#requestDeletedNode) | **GET** /v4/nodes/deleted_nodes/{deleted_node_id} | Request deleted node
[**requestDeletedNodeVersions**](NodesApi.md#requestDeletedNodeVersions) | **GET** /v4/nodes/{node_id}/deleted_nodes/versions | Request deleted versions of nodes
[**requestDeletedNodesSummary**](NodesApi.md#requestDeletedNodesSummary) | **GET** /v4/nodes/{node_id}/deleted_nodes | Request list of deleted nodes
[**requestFileVersionList**](NodesApi.md#requestFileVersionList) | **GET** /v4/nodes/files/versions/{reference_id} | Request list of file versions
[**requestListOfWebhooksForRoom**](NodesApi.md#requestListOfWebhooksForRoom) | **GET** /v4/nodes/rooms/{room_id}/webhooks | Request list of webhooks that are assigned or can be assigned to this room
[**requestMissingFileKeys**](NodesApi.md#requestMissingFileKeys) | **GET** /v4/nodes/missingFileKeys | Request files without user&#39;s file key
[**requestNode**](NodesApi.md#requestNode) | **GET** /v4/nodes/{node_id} | Request node
[**requestNodeComments**](NodesApi.md#requestNodeComments) | **GET** /v4/nodes/{node_id}/comments | Request list of node comments
[**requestNodeParents**](NodesApi.md#requestNodeParents) | **GET** /v4/nodes/{node_id}/parents | Request list of parent nodes
[**requestNodes**](NodesApi.md#requestNodes) | **GET** /v4/nodes | Request list of nodes
[**requestPendingAssignments**](NodesApi.md#requestPendingAssignments) | **GET** /v4/nodes/rooms/pending | Request user-room assignments per group
[**requestRoomActivitiesLogAsJson**](NodesApi.md#requestRoomActivitiesLogAsJson) | **GET** /v4/nodes/rooms/{room_id}/events | Request events of a room
[**requestRoomGroups**](NodesApi.md#requestRoomGroups) | **GET** /v4/nodes/rooms/{room_id}/groups | Request room granted group(s) or / and group(s) that can be granted
[**requestRoomPolicies**](NodesApi.md#requestRoomPolicies) | **GET** /v4/nodes/rooms/{room_id}/policies | Request Room Policies
[**requestRoomRescueKey**](NodesApi.md#requestRoomRescueKey) | **GET** /v4/nodes/files/{file_id}/data_room_file_key | Request room rescue key
[**requestRoomRescueKeyPair**](NodesApi.md#requestRoomRescueKeyPair) | **GET** /v4/nodes/rooms/{room_id}/keypair | Request room rescue key
[**requestRoomRescueKeyPairs**](NodesApi.md#requestRoomRescueKeyPairs) | **GET** /v4/nodes/rooms/{room_id}/keypairs | Request all room rescue key pairs
[**requestRoomS3Tags**](NodesApi.md#requestRoomS3Tags) | **GET** /v4/nodes/rooms/{room_id}/s3_tags | Request list of all assigned S3 tags to the room
[**requestRoomUsers**](NodesApi.md#requestRoomUsers) | **GET** /v4/nodes/rooms/{room_id}/users | Request room granted user(s) or / and user(s) that can be granted
[**requestSystemRescueKey**](NodesApi.md#requestSystemRescueKey) | **GET** /v4/nodes/files/{file_id}/data_space_file_key | Request system rescue key
[**requestUploadStatusFiles**](NodesApi.md#requestUploadStatusFiles) | **GET** /v4/nodes/files/uploads/{upload_id} | Request status of S3 file upload
[**requestUserFileKey**](NodesApi.md#requestUserFileKey) | **GET** /v4/nodes/files/{file_id}/user_file_key | Request user&#39;s file key
[**restoreNodes**](NodesApi.md#restoreNodes) | **POST** /v4/nodes/deleted_nodes/actions/restore | Restore deleted nodes
[**revokeRoomGroups**](NodesApi.md#revokeRoomGroups) | **DELETE** /v4/nodes/rooms/{room_id}/groups | Revoke granted group(s) from room
[**revokeRoomUsers**](NodesApi.md#revokeRoomUsers) | **DELETE** /v4/nodes/rooms/{room_id}/users | Revoke granted user(s) from room
[**searchNodes**](NodesApi.md#searchNodes) | **GET** /v4/nodes/search | Search nodes
[**setRoomPolicies**](NodesApi.md#setRoomPolicies) | **PUT** /v4/nodes/rooms/{room_id}/policies | Set room policies
[**setRoomRescueKeyPair**](NodesApi.md#setRoomRescueKeyPair) | **POST** /v4/nodes/rooms/{room_id}/keypair | Set room&#39;s rescue key pair
[**setRoomS3Tags**](NodesApi.md#setRoomS3Tags) | **POST** /v4/nodes/rooms/{room_id}/s3_tags | Set S3 tags for a room
[**setUserFileKeys**](NodesApi.md#setUserFileKeys) | **POST** /v4/nodes/files/keys | Set file keys for a list of users and files
[**updateFavorites**](NodesApi.md#updateFavorites) | **PUT** /v4/nodes/favorites | Mark or unmark a list of nodes (room, folder or file) as favorite
[**updateFile**](NodesApi.md#updateFile) | **PUT** /v4/nodes/files/{file_id} | Updates a file’s metadata
[**updateFiles**](NodesApi.md#updateFiles) | **PUT** /v4/nodes/files | Updates a list of  file’s metadata
[**updateFolder**](NodesApi.md#updateFolder) | **PUT** /v4/nodes/folders/{folder_id} | Updates folder’s metadata
[**updateNodeComment**](NodesApi.md#updateNodeComment) | **PUT** /v4/nodes/comments/{comment_id} | Edit node comment
[**updateRoom**](NodesApi.md#updateRoom) | **PUT** /v4/nodes/rooms/{room_id} | Updates room’s metadata
[**updateRoomGroups**](NodesApi.md#updateRoomGroups) | **PUT** /v4/nodes/rooms/{room_id}/groups | Add or change room granted group(s)
[**updateRoomUsers**](NodesApi.md#updateRoomUsers) | **PUT** /v4/nodes/rooms/{room_id}/users | Add or change room granted user(s)
[**uploadFileAsMultipart**](NodesApi.md#uploadFileAsMultipart) | **POST** /v4/nodes/files/uploads/{upload_id} | Upload file



## addFavorite

> Node addFavorite(nodeId, opts)

Mark a node (room, folder or file) as favorite

### Description:   Marks a node (room, folder or file) as favorite.  ### Precondition: Authenticated user is allowed to &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128065; see&lt;/span&gt; the node (i.e. &#x60;isBrowsable &#x3D; true&#x60;).  ### Postcondition: A node gets marked as favorite.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let nodeId = 789; // Number | Node ID
let opts = {
  'xSdsDateFormat': "xSdsDateFormat_example", // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.addFavorite(nodeId, opts, (error, data, response) => {
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
 **nodeId** | **Number**| Node ID | 
 **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**Node**](Node.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## addRoomGuestUsers

> addRoomGuestUsers(roomId, roomGuestUserAddRequest, opts)

Add guest users to a room

### Description: Add guest users to a room  ### Precondition: User needs to be a &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Room Administrator&lt;/span&gt;. To add new members, the user needs the right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; non-members add&lt;/span&gt;, which is included in any role. &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Guest User Policy&lt;/span&gt; needs to be enabled.   ### Postcondition: New or existing Guest-Users now have guest-permissions for this room  ### Further Information: Batch function.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let roomId = 789; // Number | Room ID
let roomGuestUserAddRequest = new DracoonApi.RoomGuestUserAddRequest(); // RoomGuestUserAddRequest | 
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.addRoomGuestUsers(roomId, roomGuestUserAddRequest, opts, (error, data, response) => {
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
 **roomId** | **Number**| Room ID | 
 **roomGuestUserAddRequest** | [**RoomGuestUserAddRequest**](RoomGuestUserAddRequest.md)|  | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## cancelFileUpload

> cancelFileUpload(uploadId, opts)

Cancel file upload

### Description: Cancel a (S3) file upload and destroy the upload channel.  ### Precondition: An upload channel has been created and user has to be the creator of the upload channel.  ### Postcondition: The upload channel is removed and all temporary uploaded data is purged.  ### Further Information: It is recommended to notify the API about cancelled uploads if possible.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let uploadId = "uploadId_example"; // String | Upload channel ID
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.cancelFileUpload(uploadId, opts, (error, data, response) => {
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
 **uploadId** | **String**| Upload channel ID | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## changePendingAssignments

> changePendingAssignments(pendingAssignmentsRequest, opts)

Handle user-room assignments per group

### Description:   Handles a list of user-room assignments by groups that have **NOT** been approved yet   **WAITING** or **DENIED** assignments can be **ACCEPTED**.  ### Precondition: None.  ### Postcondition: User-room assignment is approved and the user gets access to the group.  ### Further Information: Room administrators should **SHOULD** handle pending assignments to provide access to rooms for other users.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let pendingAssignmentsRequest = new DracoonApi.PendingAssignmentsRequest(); // PendingAssignmentsRequest | 
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.changePendingAssignments(pendingAssignmentsRequest, opts, (error, data, response) => {
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
 **pendingAssignmentsRequest** | [**PendingAssignmentsRequest**](PendingAssignmentsRequest.md)|  | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## completeFileUpload

> Node completeFileUpload(uploadId, opts)

Complete file upload

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128679; Deprecated since v4.9.0&lt;/h3&gt;  ### Use &#x60;uploads&#x60; API  ### Description: Finishes an upload and closes the corresponding upload channel.  ### Precondition: An upload channel has been created and data has been transmitted.  ### Postcondition: The upload is finished and the temporary file is moved to the productive environment.  ### Further Information: The provided file name might be changed in accordance with the resolution strategy:   * **autorename**: changes the file name and adds a number to avoid conflicts. * **overwrite**: deletes any old file with the same file name. * **fail**: returns an error; in this case, another &#x60;PUT&#x60; request with a different file name may be sent.  Please ensure that all chunks have been transferred correctly before finishing the upload.   Download share id (if exists) gets changed if: - node with the same name exists in the target container - &#x60;resolutionStrategy&#x60; is &#x60;overwrite&#x60; - &#x60;keepShareLinks&#x60; is &#x60;true&#x60;  ### Node naming convention: * Node (room, folder, file) names are limited to **150** characters. * Illegal names:   &#x60;&#39;CON&#39;, &#39;PRN&#39;, &#39;AUX&#39;, &#39;NUL&#39;, &#39;COM1&#39;, &#39;COM2&#39;, &#39;COM3&#39;, &#39;COM4&#39;, &#39;COM5&#39;, &#39;COM6&#39;, &#39;COM7&#39;, &#39;COM8&#39;, &#39;COM9&#39;, &#39;LPT1&#39;, &#39;LPT2&#39;, &#39;LPT3&#39;, &#39;LPT4&#39;, &#39;LPT5&#39;, &#39;LPT6&#39;, &#39;LPT7&#39;, &#39;LPT8&#39;, &#39;LPT9&#39;, (and any of those with an extension)&#x60; * Illegal characters in names:   &#x60;&#39;\\\\&#39;, &#39;&lt;&#39;,&#39;&gt;&#39;, &#39;:&#39;, &#39;\\\&quot;&#39;, &#39;|&#39;, &#39;?&#39;, &#39;*&#39;, &#39;/&#39;, leading &#39;-&#39;, trailing &#39;.&#39; &#x60;

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let uploadId = "uploadId_example"; // String | Upload channel ID
let opts = {
  'xSdsDateFormat': "xSdsDateFormat_example", // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
  'xSdsAuthToken': "xSdsAuthToken_example", // String | Authentication token
  'completeUploadRequest': new DracoonApi.CompleteUploadRequest() // CompleteUploadRequest | 
};
apiInstance.completeFileUpload(uploadId, opts, (error, data, response) => {
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
 **uploadId** | **String**| Upload channel ID | 
 **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 
 **completeUploadRequest** | [**CompleteUploadRequest**](CompleteUploadRequest.md)|  | [optional] 

### Return type

[**Node**](Node.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## completeS3FileUpload

> completeS3FileUpload(uploadId, completeS3FileUploadRequest, opts)

Complete S3 file upload

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.15.0&lt;/h3&gt;  ### Description: Finishes a S3 file upload and closes the corresponding upload channel.  ### Precondition: An upload channel has been created, data has been transmitted and user has to be the creator of the upload channel  ### Postcondition: Upload channel is closed. S3 multipart upload request is completed.  ### Further Information: Download share id (if exists) gets changed if: - node with the same name exists in the target container - &#x60;resolutionStrategy&#x60; is &#x60;overwrite&#x60; - &#x60;keepShareLinks&#x60; is &#x60;true&#x60;

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let uploadId = "uploadId_example"; // String | Upload channel ID
let completeS3FileUploadRequest = new DracoonApi.CompleteS3FileUploadRequest(); // CompleteS3FileUploadRequest | 
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.completeS3FileUpload(uploadId, completeS3FileUploadRequest, opts, (error, data, response) => {
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
 **uploadId** | **String**| Upload channel ID | 
 **completeS3FileUploadRequest** | [**CompleteS3FileUploadRequest**](CompleteS3FileUploadRequest.md)|  | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## configureRoom

> Node configureRoom(roomId, configRoomRequest, opts)

Configure room

### Description: Configure a room.  ### Precondition: User needs to be a &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Room Administrator&lt;/span&gt;.  ### Postcondition: Room&#39;s configuration is changed.  ### Further Information: Provided (or default) classification is taken from room when file gets uploaded without any classification.    To set &#x60;adminIds&#x60; or &#x60;adminGroupIds&#x60; the &#x60;inheritPermissions&#x60; value has to be &#x60;false&#x60;. Otherwise use: * &#x60;PUT /nodes/rooms/{room_id}/groups&#x60; * &#x60;PUT /nodes/rooms/{room_id}/users &#x60;    APIs.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let roomId = 789; // Number | Room ID
let configRoomRequest = new DracoonApi.ConfigRoomRequest(); // ConfigRoomRequest | 
let opts = {
  'xSdsDateFormat': "xSdsDateFormat_example", // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.configureRoom(roomId, configRoomRequest, opts, (error, data, response) => {
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
 **roomId** | **Number**| Room ID | 
 **configRoomRequest** | [**ConfigRoomRequest**](ConfigRoomRequest.md)|  | 
 **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**Node**](Node.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## copyNodes

> Node copyNodes(nodeId, copyNodesRequest, opts)

Copy node(s)

### Description: Copies nodes (folder, file) to another parent.  ### Precondition: Authenticated user with &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read&lt;/span&gt; permissions in the source parent and &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; create&lt;/span&gt; permissions in the target parent node.  ### Postcondition: Nodes are copied to target parent.  ### Further Information: Nodes **MUST** be in same source parent.   **Rooms **CANNOT** be copied.**  Download share id (if exists) gets changed if: - node with the same name exists in the target container - &#x60;resolutionStrategy&#x60; is &#x60;overwrite&#x60; - &#x60;keepShareLinks&#x60; is &#x60;true&#x60;  ### Node naming convention: * Node (room, folder, file) names are limited to **150** characters. * Illegal names:   &#x60;&#39;CON&#39;, &#39;PRN&#39;, &#39;AUX&#39;, &#39;NUL&#39;, &#39;COM1&#39;, &#39;COM2&#39;, &#39;COM3&#39;, &#39;COM4&#39;, &#39;COM5&#39;, &#39;COM6&#39;, &#39;COM7&#39;, &#39;COM8&#39;, &#39;COM9&#39;, &#39;LPT1&#39;, &#39;LPT2&#39;, &#39;LPT3&#39;, &#39;LPT4&#39;, &#39;LPT5&#39;, &#39;LPT6&#39;, &#39;LPT7&#39;, &#39;LPT8&#39;, &#39;LPT9&#39;, (and any of those with an extension)&#x60; * Illegal characters in names:   &#x60;&#39;\\\\&#39;, &#39;&lt;&#39;,&#39;&gt;&#39;, &#39;:&#39;, &#39;\\\&quot;&#39;, &#39;|&#39;, &#39;?&#39;, &#39;*&#39;, &#39;/&#39;, leading &#39;-&#39;, trailing &#39;.&#39; &#x60; 

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let nodeId = 789; // Number | Target parent node ID
let copyNodesRequest = new DracoonApi.CopyNodesRequest(); // CopyNodesRequest | 
let opts = {
  'xSdsDateFormat': "xSdsDateFormat_example", // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.copyNodes(nodeId, copyNodesRequest, opts, (error, data, response) => {
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
 **nodeId** | **Number**| Target parent node ID | 
 **copyNodesRequest** | [**CopyNodesRequest**](CopyNodesRequest.md)|  | 
 **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**Node**](Node.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createAndPreserveRoomRescueKeyPair

> createAndPreserveRoomRescueKeyPair(roomId, createKeyPairRequest, opts)

Create key pair and preserve copy of old private key

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.24.0&lt;/h3&gt;  ### Description:   Create room rescue key pair and preserve copy of old private key.  ### Precondition: User needs to be a &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Room Administrator&lt;/span&gt;.  ### Postcondition: Room rescue key pair is created.   Copy of old private key is preserved.  ### Further Information: You can submit your old private key, encrypted with your current password.   This allows migrating file keys encrypted with your old key pair to the new one.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let roomId = 789; // Number | Room ID
let createKeyPairRequest = new DracoonApi.CreateKeyPairRequest(); // CreateKeyPairRequest | 
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.createAndPreserveRoomRescueKeyPair(roomId, createKeyPairRequest, opts, (error, data, response) => {
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
 **roomId** | **Number**| Room ID | 
 **createKeyPairRequest** | [**CreateKeyPairRequest**](CreateKeyPairRequest.md)|  | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createFileUploadChannel

> CreateFileUploadResponse createFileUploadChannel(createFileUploadRequest, opts)

Create new file upload channel

### Description: This endpoint creates a new upload channel which is the first step in any file upload workflow.  ### Precondition: User has &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; create&lt;/span&gt; permissions in the parent container (room or folder).  ### Postcondition: A new upload channel for a file is created.   Its ID and an upload token are returned.  ### Further Information: The upload ID is used for uploads with &#x60;X-Sds-Auth-Token&#x60; header, the upload token can be used for uploads without authentication header.  Please provide the size of the intended upload so that the quota can be checked in advanced and no data is transferred unnecessarily.  Notes are limited to **255** characters.  ### Node naming convention: * Node (room, folder, file) names are limited to **150** characters. * Illegal names:   &#x60;&#39;CON&#39;, &#39;PRN&#39;, &#39;AUX&#39;, &#39;NUL&#39;, &#39;COM1&#39;, &#39;COM2&#39;, &#39;COM3&#39;, &#39;COM4&#39;, &#39;COM5&#39;, &#39;COM6&#39;, &#39;COM7&#39;, &#39;COM8&#39;, &#39;COM9&#39;, &#39;LPT1&#39;, &#39;LPT2&#39;, &#39;LPT3&#39;, &#39;LPT4&#39;, &#39;LPT5&#39;, &#39;LPT6&#39;, &#39;LPT7&#39;, &#39;LPT8&#39;, &#39;LPT9&#39;, (and any of those with an extension)&#x60; * Illegal characters in names:   &#x60;&#39;\\\\&#39;, &#39;&lt;&#39;,&#39;&gt;&#39;, &#39;:&#39;, &#39;\\\&quot;&#39;, &#39;|&#39;, &#39;?&#39;, &#39;*&#39;, &#39;/&#39;, leading &#39;-&#39;, trailing &#39;.&#39; &#x60; 

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let createFileUploadRequest = new DracoonApi.CreateFileUploadRequest(); // CreateFileUploadRequest | 
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.createFileUploadChannel(createFileUploadRequest, opts, (error, data, response) => {
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
 **createFileUploadRequest** | [**CreateFileUploadRequest**](CreateFileUploadRequest.md)|  | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**CreateFileUploadResponse**](CreateFileUploadResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createFolder

> Node createFolder(createFolderRequest, opts)

Create new folder

### Description: Create a new folder.  ### Precondition: User has &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; create&lt;/span&gt; permissions in current room.  ### Postcondition: New folder is created.  ### Further Information: Folders **CANNOT** be created on top level (without parent element).   Notes are limited to **255** characters.  ### Node naming convention: * Node (room, folder, file) names are limited to **150** characters. * Illegal names:   &#x60;&#39;CON&#39;, &#39;PRN&#39;, &#39;AUX&#39;, &#39;NUL&#39;, &#39;COM1&#39;, &#39;COM2&#39;, &#39;COM3&#39;, &#39;COM4&#39;, &#39;COM5&#39;, &#39;COM6&#39;, &#39;COM7&#39;, &#39;COM8&#39;, &#39;COM9&#39;, &#39;LPT1&#39;, &#39;LPT2&#39;, &#39;LPT3&#39;, &#39;LPT4&#39;, &#39;LPT5&#39;, &#39;LPT6&#39;, &#39;LPT7&#39;, &#39;LPT8&#39;, &#39;LPT9&#39;, (and any of those with an extension)&#x60; * Illegal characters in names:   &#x60;&#39;\\\\&#39;, &#39;&lt;&#39;,&#39;&gt;&#39;, &#39;:&#39;, &#39;\\\&quot;&#39;, &#39;|&#39;, &#39;?&#39;, &#39;*&#39;, &#39;/&#39;, leading &#39;-&#39;, trailing &#39;.&#39; &#x60; 

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let createFolderRequest = new DracoonApi.CreateFolderRequest(); // CreateFolderRequest | 
let opts = {
  'xSdsDateFormat': "xSdsDateFormat_example", // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.createFolder(createFolderRequest, opts, (error, data, response) => {
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
 **createFolderRequest** | [**CreateFolderRequest**](CreateFolderRequest.md)|  | 
 **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**Node**](Node.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createNodeComment

> Comment createNodeComment(nodeId, createNodeCommentRequest, opts)

Create node comment

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.10.0&lt;/h3&gt;  ### Description: Create a comment for a specific node.  ### Precondition: User has &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read&lt;/span&gt; permissions on the node.  ### Postcondition: Comment is created.  ### Further Information: Maximum allowed text length: **65535** characters.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let nodeId = 789; // Number | Node ID
let createNodeCommentRequest = new DracoonApi.CreateNodeCommentRequest(); // CreateNodeCommentRequest | 
let opts = {
  'xSdsDateFormat': "xSdsDateFormat_example", // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.createNodeComment(nodeId, createNodeCommentRequest, opts, (error, data, response) => {
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
 **nodeId** | **Number**| Node ID | 
 **createNodeCommentRequest** | [**CreateNodeCommentRequest**](CreateNodeCommentRequest.md)|  | 
 **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**Comment**](Comment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createRoom

> Node createRoom(createRoomRequest, opts)

Create new room

### Description: Creates a new room at the provided parent node.   Creation of top level rooms provided.  ### Precondition: User has &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage&lt;/span&gt; permissions in the parent room.  ### Postcondition: A new room is created.  ### Further Information:   Rooms may only have other rooms as parent.   Rooms on top level do **NOT** have any parent.   Rooms may have rooms as children on n hierarchy levels.   If permission inheritance is disabled, there **MUST** be at least one admin user / group (with neither the group nor the user having an expiration date).  Notes are limited to **255** characters.  Provided (or default) classification is taken from room when file gets uploaded without any classification.  ### Node naming convention: * Node (room, folder, file) names are limited to **150** characters. * Illegal names:   &#x60;&#39;CON&#39;, &#39;PRN&#39;, &#39;AUX&#39;, &#39;NUL&#39;, &#39;COM1&#39;, &#39;COM2&#39;, &#39;COM3&#39;, &#39;COM4&#39;, &#39;COM5&#39;, &#39;COM6&#39;, &#39;COM7&#39;, &#39;COM8&#39;, &#39;COM9&#39;, &#39;LPT1&#39;, &#39;LPT2&#39;, &#39;LPT3&#39;, &#39;LPT4&#39;, &#39;LPT5&#39;, &#39;LPT6&#39;, &#39;LPT7&#39;, &#39;LPT8&#39;, &#39;LPT9&#39;, (and any of those with an extension)&#x60; * Illegal characters in names:   &#x60;&#39;\\\\&#39;, &#39;&lt;&#39;,&#39;&gt;&#39;, &#39;:&#39;, &#39;\\\&quot;&#39;, &#39;|&#39;, &#39;?&#39;, &#39;*&#39;, &#39;/&#39;, leading &#39;-&#39;, trailing &#39;.&#39; &#x60;

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let createRoomRequest = new DracoonApi.CreateRoomRequest(); // CreateRoomRequest | 
let opts = {
  'xSdsDateFormat': "xSdsDateFormat_example", // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.createRoom(createRoomRequest, opts, (error, data, response) => {
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
 **createRoomRequest** | [**CreateRoomRequest**](CreateRoomRequest.md)|  | 
 **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**Node**](Node.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## downloadZipArchive

> downloadZipArchive(zipDownloadRequest, opts)

Download files / folders as ZIP archive

### Description:   Download multiple files in a ZIP archive.  ### Precondition: User has &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read&lt;/span&gt; permissions in auth parent room.  ### Postcondition: Stream is returned.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let zipDownloadRequest = new DracoonApi.ZipDownloadRequest(); // ZipDownloadRequest | 
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.downloadZipArchive(zipDownloadRequest, opts, (error, data, response) => {
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
 **zipDownloadRequest** | [**ZipDownloadRequest**](ZipDownloadRequest.md)|  | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/octet-stream


## emptyDeletedNodes

> emptyDeletedNodes(nodeId, opts)

Empty recycle bin

### Description:   Empty a recycle bin.  ### Precondition: User has &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; delete recycle bin&lt;/span&gt; permissions in parent room.  ### Postcondition: All files in the recycle bin are permanently removed.  ### Further Information: Actually removes the previously deleted files from the system.   **This action is irreversible.**

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let nodeId = 789; // Number | Room ID
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.emptyDeletedNodes(nodeId, opts, (error, data, response) => {
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
 **nodeId** | **Number**| Room ID | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## encryptRoom

> Node encryptRoom(roomId, encryptRoomRequest, opts)

Encrypt room

### Description:   Activates the client-side encryption for a room.  ### Precondition: User needs to be a &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Room Administrator&lt;/span&gt;.  ### Postcondition: Encryption of room is activated.  ### Further Information: Only empty rooms at the top level may be encrypted.   This endpoint may also be used to disable encryption of an empty room.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let roomId = 789; // Number | Room ID
let encryptRoomRequest = new DracoonApi.EncryptRoomRequest(); // EncryptRoomRequest | 
let opts = {
  'xSdsDateFormat': "xSdsDateFormat_example", // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.encryptRoom(roomId, encryptRoomRequest, opts, (error, data, response) => {
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
 **roomId** | **Number**| Room ID | 
 **encryptRoomRequest** | [**EncryptRoomRequest**](EncryptRoomRequest.md)|  | 
 **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**Node**](Node.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## generateDownloadUrl

> DownloadTokenGenerateResponse generateDownloadUrl(fileId, opts)

Generate download URL

### Description: Create a download URL to retrieve a file without &#x60;X-Sds-Auth-Token&#x60; Header.  ### Precondition: User with &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read&lt;/span&gt; permissions in parent room.  ### Postcondition: Download token is generated and returned.  ### Further Information: The token is necessary to access &#x60;downloads&#x60; ressources.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let fileId = 789; // Number | File ID
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.generateDownloadUrl(fileId, opts, (error, data, response) => {
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
 **fileId** | **Number**| File ID | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**DownloadTokenGenerateResponse**](DownloadTokenGenerateResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## generateDownloadUrlForZipArchive

> DownloadTokenGenerateResponse generateDownloadUrlForZipArchive(zipDownloadRequest, opts)

Generate download URL for ZIP download

### Description:   Create a download URL to retrieve several files in one ZIP archive.  ### Precondition: User has &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read&lt;/span&gt; permissions in parent room.  ### Postcondition: Download URL is generated and returned.  ### Further Information: The token is necessary to access &#x60;downloads&#x60; resources.   ZIP download is only available for files and folders.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let zipDownloadRequest = new DracoonApi.ZipDownloadRequest(); // ZipDownloadRequest | 
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.generateDownloadUrlForZipArchive(zipDownloadRequest, opts, (error, data, response) => {
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
 **zipDownloadRequest** | [**ZipDownloadRequest**](ZipDownloadRequest.md)|  | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**DownloadTokenGenerateResponse**](DownloadTokenGenerateResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## generatePresignedUrlsFiles

> PresignedUrlList generatePresignedUrlsFiles(uploadId, generatePresignedUrlsRequest, opts)

Generate presigned URLs for S3 file upload

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.15.0&lt;/h3&gt;  ### Description: Generate presigned URLs for S3 file upload.  ### Precondition: An upload channel has been created and user has to be the creator of the upload channel.  ### Postcondition: List of presigned URLs is returned.  ### Further Information: The size for each part must be &gt;&#x3D; 5 MB, except for the last part.   The part number of the first part in S3 is 1 (not 0).   Use HTTP method &#x60;PUT&#x60; for uploading bytes via presigned URL.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let uploadId = "uploadId_example"; // String | Upload channel ID
let generatePresignedUrlsRequest = new DracoonApi.GeneratePresignedUrlsRequest(); // GeneratePresignedUrlsRequest | 
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.generatePresignedUrlsFiles(uploadId, generatePresignedUrlsRequest, opts, (error, data, response) => {
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
 **uploadId** | **String**| Upload channel ID | 
 **generatePresignedUrlsRequest** | [**GeneratePresignedUrlsRequest**](GeneratePresignedUrlsRequest.md)|  | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**PresignedUrlList**](PresignedUrlList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## handleRoomWebhookAssignments

> RoomWebhookList handleRoomWebhookAssignments(roomId, updateRoomWebhookRequest, opts)

Assign or unassign webhooks to room

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.19.0&lt;/h3&gt;  ### Description:   Handle room webhook assignments.  ### Precondition: User needs to be a &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Room Administrator&lt;/span&gt;.  ### Postcondition: List of webhooks is returned.  ### Further Information: None.  ### Available event types:  &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | Name | Description | Scope | | :--- | :--- | :--- | | **&#x60;downloadshare.created&#x60;** | Triggered when a new download share is created in affected room | Node Webhook | | **&#x60;downloadshare.deleted&#x60;** | Triggered when a download share is deleted in affected room | Node Webhook | | **&#x60;downloadshare.used&#x60;** | Triggered when a download share is utilized in affected room | Node Webhook | | **&#x60;uploadshare.created&#x60;** | Triggered when a new upload share is created in affected room | Node Webhook | | **&#x60;uploadshare.deleted&#x60;** | Triggered when a upload share is deleted in affected room | Node Webhook | | **&#x60;uploadshare.used&#x60;** | Triggered when a new file is uploaded via the upload share in affected room | Node Webhook | | **&#x60;file.created&#x60;** | Triggered when a new file is uploaded in affected room | Node Webhook | | **&#x60;folder.created&#x60;** | Triggered when a new folder is created in affected room | Node Webhook | | **&#x60;room.created&#x60;** | Triggered when a new room is created (in affected room) | Node Webhook | | **&#x60;file.deleted&#x60;** | Triggered when a file is deleted in affected room | Node Webhook | | **&#x60;folder.deleted&#x60;** | Triggered when a folder is deleted in affected room | Node Webhook | | **&#x60;room.deleted&#x60;** | Triggered when a room is deleted in affected room | Node Webhook |  &lt;/details&gt;

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let roomId = 789; // Number | Room ID
let updateRoomWebhookRequest = new DracoonApi.UpdateRoomWebhookRequest(); // UpdateRoomWebhookRequest | 
let opts = {
  'xSdsDateFormat': "xSdsDateFormat_example", // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.handleRoomWebhookAssignments(roomId, updateRoomWebhookRequest, opts, (error, data, response) => {
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
 **roomId** | **Number**| Room ID | 
 **updateRoomWebhookRequest** | [**UpdateRoomWebhookRequest**](UpdateRoomWebhookRequest.md)|  | 
 **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**RoomWebhookList**](RoomWebhookList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## moveNodes

> Node moveNodes(nodeId, moveNodesRequest, opts)

Move node(s)

### Description:   Moves nodes (folder, file) to another parent.  ### Precondition: Authenticated user with &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read&lt;/span&gt; and &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; delete&lt;/span&gt; permissions in the source parent and &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; create&lt;/span&gt; permissions in the target parent node.  ### Postcondition: Nodes are moved to target parent.  ### Further Information: Nodes **MUST** be in same source parent.   **Rooms **CANNOT** be moved.**  Download share id (if exists) gets changed if: - node with the same name exists in the target container - &#x60;resolutionStrategy&#x60; is &#x60;overwrite&#x60; - &#x60;keepShareLinks&#x60; is &#x60;true&#x60;  ### Node naming convention: * Node (room, folder, file) names are limited to **150** characters. * Illegal names:   &#x60;&#39;CON&#39;, &#39;PRN&#39;, &#39;AUX&#39;, &#39;NUL&#39;, &#39;COM1&#39;, &#39;COM2&#39;, &#39;COM3&#39;, &#39;COM4&#39;, &#39;COM5&#39;, &#39;COM6&#39;, &#39;COM7&#39;, &#39;COM8&#39;, &#39;COM9&#39;, &#39;LPT1&#39;, &#39;LPT2&#39;, &#39;LPT3&#39;, &#39;LPT4&#39;, &#39;LPT5&#39;, &#39;LPT6&#39;, &#39;LPT7&#39;, &#39;LPT8&#39;, &#39;LPT9&#39;, (and any of those with an extension)&#x60; * Illegal characters in names:   &#x60;&#39;\\\\&#39;, &#39;&lt;&#39;,&#39;&gt;&#39;, &#39;:&#39;, &#39;\\\&quot;&#39;, &#39;|&#39;, &#39;?&#39;, &#39;*&#39;, &#39;/&#39;, leading &#39;-&#39;, trailing &#39;.&#39; &#x60; 

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let nodeId = 789; // Number | Target parent node ID
let moveNodesRequest = new DracoonApi.MoveNodesRequest(); // MoveNodesRequest | 
let opts = {
  'xSdsDateFormat': "xSdsDateFormat_example", // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.moveNodes(nodeId, moveNodesRequest, opts, (error, data, response) => {
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
 **nodeId** | **Number**| Target parent node ID | 
 **moveNodesRequest** | [**MoveNodesRequest**](MoveNodesRequest.md)|  | 
 **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**Node**](Node.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## removeDeletedNodes

> removeDeletedNodes(deleteDeletedNodesRequest, opts)

Remove nodes from recycle bin

### Description: Permanently remove a list of nodes from the recycle bin.  ### Precondition: User has &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; delete recycle bin&lt;/span&gt; permissions in parent room.  ### Postcondition: All provided nodes are removed.  ### Further Information: The removal of deleted nodes from the recycle bin is irreversible.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let deleteDeletedNodesRequest = new DracoonApi.DeleteDeletedNodesRequest(); // DeleteDeletedNodesRequest | 
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.removeDeletedNodes(deleteDeletedNodesRequest, opts, (error, data, response) => {
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
 **deleteDeletedNodesRequest** | [**DeleteDeletedNodesRequest**](DeleteDeletedNodesRequest.md)|  | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## removeFavorite

> removeFavorite(nodeId, opts)

Unmark a node (room, folder or file) as favorite

### Description: Unmarks a node (room, folder or file) as favorite.  ### Precondition: Authenticated user is allowed to &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128065; see&lt;/span&gt; the node (i.e. &#x60;isBrowsable &#x3D; true&#x60;).  ### Postcondition: A node gets unmarked as favorite.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let nodeId = 789; // Number | Node ID
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.removeFavorite(nodeId, opts, (error, data, response) => {
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
 **nodeId** | **Number**| Node ID | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## removeNode

> removeNode(nodeId, opts)

Remove node

### Description: Delete node (room, folder or file).  ### Precondition: Authenticated user with &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; delete&lt;/span&gt; permissions on supplied nodes (for folders or files) or on superordinated node (for rooms).  ### Postcondition: Node gets deleted.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let nodeId = 789; // Number | Node ID
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.removeNode(nodeId, opts, (error, data, response) => {
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
 **nodeId** | **Number**| Node ID | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## removeNodeComment

> removeNodeComment(commentId, opts)

Remove node comment

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.10.0&lt;/h3&gt;  ### Description: Delete an existing comment for a specific node.  ### Precondition: User has &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read&lt;/span&gt; permissions on the node and is the creator of the comment **OR** &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Room Administrator&lt;/span&gt; in auth parent room.  ### Postcondition: Comment is deleted.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let commentId = 789; // Number | Comment ID
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.removeNodeComment(commentId, opts, (error, data, response) => {
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
 **commentId** | **Number**| Comment ID | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## removeNodes

> removeNodes(deleteNodesRequest, opts)

Remove nodes

### Description: Delete nodes (room, folder or file).  ### Precondition: Authenticated user with &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; delete&lt;/span&gt; permissions on supplied nodes (for folders or files) or on superordinated node (for rooms).  ### Postcondition: Nodes are deleted.  ### Further Information: Nodes **MUST** be in same parent.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let deleteNodesRequest = new DracoonApi.DeleteNodesRequest(); // DeleteNodesRequest | 
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.removeNodes(deleteNodesRequest, opts, (error, data, response) => {
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
 **deleteNodesRequest** | [**DeleteNodesRequest**](DeleteNodesRequest.md)|  | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## removeRoomRescueKeyPair

> removeRoomRescueKeyPair(roomId, opts)

Remove rooms&#39;s rescue key pair

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.24.0&lt;/h3&gt;  ### Description:   Delete room rescue key pair.  ### Precondition: Authenticated user.  ### Postcondition: Key pair is removed (cf. further information below).  ### Further Information: Please set a new room rescue key pair first and re-encrypt file keys with it.   If no version is set, deleted key pair with lowest preference value.   Although, &#x60;version&#x60; **SHOULD** be set. 

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let roomId = 789; // Number | Room ID
let opts = {
  'version': "version_example", // String | Version (NEW)
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.removeRoomRescueKeyPair(roomId, opts, (error, data, response) => {
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
 **roomId** | **Number**| Room ID | 
 **version** | **String**| Version (NEW) | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestDeletedNode

> DeletedNode requestDeletedNode(deletedNodeId, opts)

Request deleted node

### Description:   Get metadata of a deleted node.  ### Precondition: User can access parent room and has &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read recycle bin&lt;/span&gt; permissions.  ### Postcondition: Requested deleted node is returned.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let deletedNodeId = 789; // Number | Deleted node ID
let opts = {
  'xSdsDateFormat': "xSdsDateFormat_example", // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestDeletedNode(deletedNodeId, opts, (error, data, response) => {
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
 **deletedNodeId** | **Number**| Deleted node ID | 
 **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**DeletedNode**](DeletedNode.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestDeletedNodeVersions

> DeletedNodeVersionsList requestDeletedNodeVersions(nodeId, type, name, opts)

Request deleted versions of nodes

### Description:   Retrieve all deleted versions of a node.  ### Precondition: User can access parent room and has &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read recycle bin&lt;/span&gt; permissions.  ### Postcondition: List of deleted versions of a node is returned.  ### Further Information: The node is identified by three parameters: * parent ID * name * type (file, folder).  Sort string syntax: &#x60;FIELD_NAME:ORDER&#x60;   &#x60;ORDER&#x60; can be &#x60;asc&#x60; or &#x60;desc&#x60;.   Multiple sort criteria are possible.   Fields are connected via logical conjunction **AND**.  &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;expireAt:desc|size:asc&#x60;   Sort by &#x60;expireAt&#x60; descending **AND** &#x60;size&#x60; ascending.  &lt;/details&gt;  ### Sorting options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Description | | :--- | :--- | | &#x60;expireAt&#x60; | Expiration date | | &#x60;accessedAt&#x60; | Last access date | | &#x60;size&#x60; | Node size | | &#x60;classification&#x60; | Classification ID:&lt;ul&gt;&lt;li&gt;1 - public&lt;/li&gt;&lt;li&gt;2 - internal&lt;/li&gt;&lt;li&gt;3 - confidential&lt;/li&gt;&lt;li&gt;4 - strictly confidential&lt;/li&gt;&lt;/ul&gt; | | &#x60;createdAt&#x60; | Creation date | | &#x60;createdBy&#x60; | Creator first name, last name | | &#x60;updatedAt&#x60; | Last modification date | | &#x60;updatedBy&#x60; | Last modifier first name, last name | | &#x60;deletedAt&#x60; | Deleted date | | &#x60;deletedBy&#x60; | Deleter first name, last name |  &lt;/details&gt;

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let nodeId = 789; // Number | Parent ID (room or folder ID)
let type = "type_example"; // String | Node type
let name = "name_example"; // String | Node name
let opts = {
  'xSdsDateFormat': "xSdsDateFormat_example", // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
  'sort': "sort_example", // String | Sort string
  'offset': 56, // Number | Range offset
  'limit': 56, // Number | Range limit.  Maximum 500.   For more results please use paging (`offset` + `limit`).
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestDeletedNodeVersions(nodeId, type, name, opts, (error, data, response) => {
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
 **nodeId** | **Number**| Parent ID (room or folder ID) | 
 **type** | **String**| Node type | 
 **name** | **String**| Node name | 
 **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] 
 **sort** | **String**| Sort string | [optional] 
 **offset** | **Number**| Range offset | [optional] 
 **limit** | **Number**| Range limit.  Maximum 500.   For more results please use paging (&#x60;offset&#x60; + &#x60;limit&#x60;). | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**DeletedNodeVersionsList**](DeletedNodeVersionsList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestDeletedNodesSummary

> DeletedNodeSummaryList requestDeletedNodesSummary(nodeId, opts)

Request list of deleted nodes

### Description:   Retrieve a list of deleted nodes in a recycle bin.  ### Precondition: User can access parent room and has &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read recycle bin&lt;/span&gt; permissions.  ### Postcondition: List of deleted nodes is returned.  ### Further Information: Only room IDs are accepted as parent ID since only rooms may have a recycle bin.  ### Filtering: All filter fields are connected via logical conjunction (**AND**)   Filter string syntax: &#x60;FIELD_NAME:OPERATOR:VALUE[:VALUE...]&#x60;    &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;type:eq:file:folder|name:cn:searchString_1|parentPath:cn:searchString_2&#x60;   Get deleted nodes where type equals (&#x60;file&#x60; **OR** &#x60;folder&#x60;) **AND** deleted node name containing &#x60;searchString_1&#x60; **AND** deleted node parent path containing &#x60;searchString 2&#x60;.  &lt;/details&gt;  ### Filtering options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Filter Description | &#x60;OPERATOR&#x60; | Operator Description | &#x60;VALUE&#x60; | | :--- | :--- | :--- | :--- | :--- | | &#x60;type&#x60; | Node type filter | &#x60;eq&#x60; | Node type equals value(s).&lt;br&gt;Multiple values are allowed and will be connected via logical disjunction (**OR**).&lt;br&gt;e.g. &#x60;type:eq:folder:file&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;folder&#x60;&lt;/li&gt;&lt;li&gt;&#x60;file&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;name&#x60; | Node name filter | &#x60;cn&#x60; | Node name contains value. | &#x60;search String&#x60; | | &#x60;parentPath&#x60; | Parent path filter | &#x60;cn&#x60; | Parent path contains value. | &#x60;search String&#x60; | | &#x60;timestampCreation&#x60; | Creation timestamp filter | &#x60;ge, le&#x60; | Creation timestamp is greater / less equals than value.&lt;br&gt;Multiple operator values are allowed and will be connected via logical conjunction (**AND**).&lt;br&gt;e.g. &#x60;timestampCreation:ge:2016-12-31&#x60;&amp;#124;&lt;br&gt;&#x60;timestampCreation:le:2018-01-01&#x60; | &#x60;Date (yyyy-MM-dd)&#x60; | | &#x60;timestampModification&#x60; | Modification timestamp filter | &#x60;ge, le&#x60; | Modification timestamp is greater / less equals than value.&lt;br&gt;Multiple operator values are allowed and will be connected via logical conjunction (**AND**).&lt;br&gt;e.g. &#x60;timestampModification:ge:2016-12-31T23:00:00.123&#x60;&amp;#124;&lt;br&gt;&#x60;timestampModification:le:2018-01-01T11:00:00.540&#x60; | &#x60;Date (yyyy-MM-dd)&#x60; |  &lt;/details&gt;  ---  ### Sorting: Sort string syntax: &#x60;FIELD_NAME:ORDER&#x60;   &#x60;ORDER&#x60; can be &#x60;asc&#x60; or &#x60;desc&#x60;.   Multiple sort criteria are possible.   Fields are connected via logical conjunction **AND**.   Nodes are sorted by type first, then by sent sort string.    &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;name:desc|timestampCreation:asc&#x60;   Sort by &#x60;name&#x60; descending **AND** &#x60;timestampCreation&#x60; ascending.  &lt;/details&gt;  ### Sorting options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Description | | :--- | :--- | | &#x60;name&#x60; | Node name | | &#x60;cntVersions&#x60; | Number of deleted versions of this file | | &#x60;firstDeletedAt&#x60; | First deleted version | | &#x60;lastDeletedAt&#x60; | Last deleted version | | &#x60;parentPath&#x60; | Parent path of deleted node | | &#x60;timestampCreation&#x60; | Creation timestamp | | &#x60;timestampModification&#x60; | Modification timestamp |  &lt;/details&gt;

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let nodeId = 789; // Number | Parent ID (can only be a room ID)
let opts = {
  'xSdsDateFormat': "xSdsDateFormat_example", // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
  'filter': "filter_example", // String | Filter string
  'sort': "sort_example", // String | Sort string
  'offset': 56, // Number | Range offset
  'limit': 56, // Number | Range limit.  Maximum 500.   For more results please use paging (`offset` + `limit`).
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestDeletedNodesSummary(nodeId, opts, (error, data, response) => {
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
 **nodeId** | **Number**| Parent ID (can only be a room ID) | 
 **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] 
 **filter** | **String**| Filter string | [optional] 
 **sort** | **String**| Sort string | [optional] 
 **offset** | **Number**| Range offset | [optional] 
 **limit** | **Number**| Range limit.  Maximum 500.   For more results please use paging (&#x60;offset&#x60; + &#x60;limit&#x60;). | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**DeletedNodeSummaryList**](DeletedNodeSummaryList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestFileVersionList

> FileVersionList requestFileVersionList(referenceId, opts)

Request list of file versions

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.37.0&lt;/h3&gt;  ### Description:   Request a list of file versions. Both nodes and deleted nodes are included, depending on the user&#39;s permissions.  ### Precondition: User has &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read/read recycle bin&lt;/span&gt; permissions in parent room.  ### Postcondition: List of file versions is returned.  ### Further Information: Maximum number of file versions is 500. The list is sorted by ID DESC. 

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let referenceId = 789; // Number | Reference ID
let opts = {
  'xSdsDateFormat': "xSdsDateFormat_example", // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
  'offset': 56, // Number | Range offset
  'limit': 56, // Number | Range limit.  Maximum 500.   For more results please use paging (`offset` + `limit`).
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestFileVersionList(referenceId, opts, (error, data, response) => {
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
 **referenceId** | **Number**| Reference ID | 
 **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] 
 **offset** | **Number**| Range offset | [optional] 
 **limit** | **Number**| Range limit.  Maximum 500.   For more results please use paging (&#x60;offset&#x60; + &#x60;limit&#x60;). | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**FileVersionList**](FileVersionList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestListOfWebhooksForRoom

> RoomWebhookList requestListOfWebhooksForRoom(roomId, opts)

Request list of webhooks that are assigned or can be assigned to this room

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.19.0&lt;/h3&gt;  ### Description:   Get a list of webhooks for the room scope with their assignment status.  ### Precondition: User needs to be a &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Room Administrator&lt;/span&gt;.  ### Postcondition: List of webhooks is returned.  ### Further Information:  ### Filtering: All filter fields are connected via logical conjunction (**AND**)   Filter string syntax: &#x60;FIELD_NAME:OPERATOR:VALUE[:VALUE...]&#x60;    &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;isAssigned:eq:true&#x60;   Get a list of assigned webhooks to the room.  &lt;/details&gt;  ### Filtering options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Filter Description | &#x60;OPERATOR&#x60; | Operator Description | &#x60;VALUE&#x60; | | :--- | :--- | :--- | :--- | :--- | | **&#x60;isAssigned&#x60;** | Assigned/unassigned webhooks filter | &#x60;eq&#x60; |  | &#x60;true or false&#x60; |  &lt;/details&gt;

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let roomId = 789; // Number | Room ID
let opts = {
  'xSdsDateFormat': "xSdsDateFormat_example", // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
  'offset': 56, // Number | Range offset
  'limit': 56, // Number | Range limit.  Maximum 500.   For more results please use paging (`offset` + `limit`).
  'filter': "filter_example", // String | Filter string
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestListOfWebhooksForRoom(roomId, opts, (error, data, response) => {
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
 **roomId** | **Number**| Room ID | 
 **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] 
 **offset** | **Number**| Range offset | [optional] 
 **limit** | **Number**| Range limit.  Maximum 500.   For more results please use paging (&#x60;offset&#x60; + &#x60;limit&#x60;). | [optional] 
 **filter** | **String**| Filter string | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**RoomWebhookList**](RoomWebhookList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestMissingFileKeys

> MissingKeysResponse requestMissingFileKeys(opts)

Request files without user&#39;s file key

### Description:   Requests a list of missing file keys that may be generated by the current user.    ### Precondition: User has a key pair.   Only returns users that owns one of the following permissions: &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage&lt;/span&gt;, &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read&lt;/span&gt;, &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage download share&lt;/span&gt;  ### Postcondition: None.  ### Further Information: Clients **SHOULD** regularly request missing file keys to provide access to files for other users.   The returned list is ordered by priority (emergency passwords / rescue keys are returned first). There is an enforced limit of **100** items per request. A total value greater than limit signals that there are more entries but does not necessarily reflect the precise number of total items. 

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let opts = {
  'offset': 56, // Number | Range offset
  'limit': 56, // Number | Range limit.  Maximum 500.   For more results please use paging (`offset` + `limit`).
  'roomId': 789, // Number | Room ID
  'fileId': 789, // Number | File ID
  'userId': 789, // Number | User ID
  'useKey': "useKey_example", // String | Determines which key should be used (NEW)
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestMissingFileKeys(opts, (error, data, response) => {
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
 **offset** | **Number**| Range offset | [optional] 
 **limit** | **Number**| Range limit.  Maximum 500.   For more results please use paging (&#x60;offset&#x60; + &#x60;limit&#x60;). | [optional] 
 **roomId** | **Number**| Room ID | [optional] 
 **fileId** | **Number**| File ID | [optional] 
 **userId** | **Number**| User ID | [optional] 
 **useKey** | **String**| Determines which key should be used (NEW) | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**MissingKeysResponse**](MissingKeysResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestNode

> Node requestNode(nodeId, opts)

Request node

### Description:   Get node (room, folder or file).  ### Precondition: User has &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read&lt;/span&gt; permissions in auth parent room.  ### Postcondition: Requested node is returned.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let nodeId = 789; // Number | Node ID
let opts = {
  'xSdsDateFormat': "xSdsDateFormat_example", // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestNode(nodeId, opts, (error, data, response) => {
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
 **nodeId** | **Number**| Node ID | 
 **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**Node**](Node.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestNodeComments

> CommentList requestNodeComments(nodeId, opts)

Request list of node comments

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.10.0&lt;/h3&gt;  ### Description: Get comments for a specific node.  ### Precondition: User has &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read&lt;/span&gt; permissions on the node.  ### Postcondition: List with comments (sorted by &#x60;createdAt&#x60; timestamp) is returned.  ### Further Information: An empty list is returned if no comments were found.   Output is limited to **500** entries.   For more results please use filter criteria and paging (&#x60;offset&#x60; + &#x60;limit&#x60;).  

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let nodeId = 789; // Number | Node ID
let opts = {
  'xSdsDateFormat': "xSdsDateFormat_example", // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
  'offset': 56, // Number | Range offset
  'limit': 56, // Number | Range limit.  Maximum 500.   For more results please use paging (`offset` + `limit`).
  'hideDeleted': true, // Boolean | Hide deleted comments (default: false)
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestNodeComments(nodeId, opts, (error, data, response) => {
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
 **nodeId** | **Number**| Node ID | 
 **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] 
 **offset** | **Number**| Range offset | [optional] 
 **limit** | **Number**| Range limit.  Maximum 500.   For more results please use paging (&#x60;offset&#x60; + &#x60;limit&#x60;). | [optional] 
 **hideDeleted** | **Boolean**| Hide deleted comments (default: false) | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**CommentList**](CommentList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestNodeParents

> NodeParentList requestNodeParents(nodeId, opts)

Request list of parent nodes

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.10.0&lt;/h3&gt;  ### Description:   Requests a list of node ancestors, sorted from root node to the node&#39;s direct parent node.  ### Precondition: User is allowed to browse through the node tree until the requested node.  ### Postcondition: List of parent nodes is returned.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let nodeId = 789; // Number | Node ID
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestNodeParents(nodeId, opts, (error, data, response) => {
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
 **nodeId** | **Number**| Node ID | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**NodeParentList**](NodeParentList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestNodes

> NodeList requestNodes(opts)

Request list of nodes

### Description:   Provides a hierarchical list of file system nodes (rooms, folders or files) of a given parent that are accessible by the current user.  ### Precondition: Authenticated user.  ### Postcondition: List of nodes is returned.  ### Further Information: &#x60;EncryptionInfo&#x60; is **NOT** provided.  ### Filtering: All filter fields are connected via logical conjunction (**AND**)   Filter string syntax: &#x60;FIELD_NAME:OPERATOR:VALUE[:VALUE...]&#x60;    &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;type:eq:room:folder|perm:eq:read&#x60;   Get nodes where type equals (&#x60;room&#x60; **OR** &#x60;folder&#x60;) **AND** user has &#x60;read&#x60; permissions.  &lt;/details&gt;  ### Filtering options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Filter Description | &#x60;OPERATOR&#x60; | Operator Description | &#x60;VALUE&#x60; | | :--- | :--- | :--- | :--- | :--- | | &#x60;type&#x60; | Node type filter | &#x60;eq&#x60; | Node type equals value.&lt;br&gt;Multiple values are allowed and will be connected via logical disjunction (**OR**).&lt;br&gt;e.g. &#x60;type:eq:room:folder&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;room&#x60;&lt;/li&gt;&lt;li&gt;&#x60;folder&#x60;&lt;/li&gt;&lt;li&gt;&#x60;file&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;perm&#x60; | Permission filter | &#x60;eq&#x60; | Permission equals value.&lt;br&gt;Multiple values are allowed and will be connected via logical disjunction (**OR**).&lt;br&gt;e.g. &#x60;perm:eq:read:create:delete&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;manage&#x60;&lt;/li&gt;&lt;li&gt;&#x60;read&#x60;&lt;/li&gt;&lt;li&gt;&#x60;change&#x60;&lt;/li&gt;&lt;li&gt;&#x60;create&#x60;&lt;/li&gt;&lt;li&gt;&#x60;delete&#x60;&lt;/li&gt;&lt;li&gt;&#x60;manageDownloadShare&#x60;&lt;/li&gt;&lt;li&gt;&#x60;manageUploadShare&#x60;&lt;/li&gt;&lt;li&gt;&#x60;canReadRecycleBin&#x60;&lt;/li&gt;&lt;li&gt;&#x60;canRestoreRecycleBin&#x60;&lt;/li&gt;&lt;li&gt;&#x60;canDeleteRecycleBin&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;childPerm&#x60; | Same as &#x60;perm&#x60;, but less restrictive (applies to child nodes only).&lt;br&gt;Child nodes of the parent node which do not meet the filter condition&lt;br&gt;are **NOT** returned. | &#x60;eq&#x60; | cf. &#x60;perm&#x60; | cf. &#x60;perm&#x60; | | &#x60;name&#x60; | Node name filter | &#x60;cn, eq&#x60; | Node name contains / equals value. | &#x60;search String&#x60; | | &#x60;encrypted&#x60; | Node encryption status filter | &#x60;eq&#x60; |  | &#x60;true or false&#x60; | | &#x60;branchVersion&#x60; | Node branch version filter | &#x60;ge, le&#x60; | Branch version is greater / less equals than value.&lt;br&gt;Multiple operator values are allowed and will be connected via logical conjunction (**AND**).&lt;br&gt;e.g. &#x60;branchVersion:ge:1423280937404&#x60;&amp;#124;&#x60;branchVersion:le:1523280937404&#x60; | &#x60;version number&#x60; | | &#x60;timestampCreation&#x60; | Creation timestamp filter | &#x60;ge, le&#x60; | Creation timestamp is greater / less equals than value.&lt;br&gt;Multiple operator values are allowed and will be connected via logical conjunction (**AND**).&lt;br&gt;e.g. &#x60;timestampCreation:ge:2016-12-31T23:00:00.123&#x60;&amp;#124;&lt;br&gt;&#x60;timestampCreation:le:2018-01-01T11:00:00.540&#x60; | &#x60;Date (yyyy-MM-dd)&#x60; | | &#x60;timestampModification&#x60; | Modification timestamp filter | &#x60;ge, le&#x60; | Modification timestamp is greater / less equals than value.&lt;br&gt;Multiple operator values are allowed and will be connected via logical conjunction (**AND**).&lt;br&gt;e.g. &#x60;timestampModification:ge:2016-12-31T23:00:00.123&#x60;&amp;#124;&lt;br&gt;&#x60;timestampModification:le:2018-01-01T11:00:00.540&#x60; | &#x60;Date (yyyy-MM-dd)&#x60; | | &#x60;referenceId&#x60;           | Reference ID filter               | &#x60;eq&#x60; | Reference ID equals value.   | &#x60;Integer &#x60; | &lt;/details&gt;  ---  ### Sorting: Sort string syntax: &#x60;FIELD_NAME:ORDER&#x60;   &#x60;ORDER&#x60; can be &#x60;asc&#x60; or &#x60;desc&#x60;.   Multiple sort criteria are possible.   Fields are connected via logical conjunction **AND**.   Nodes are sorted by type first, then by sent sort string.    &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;name:desc|fileType:asc&#x60;   Sort by &#x60;name&#x60; descending **AND** &#x60;fileType&#x60; ascending.  &lt;/details&gt;  ### Sorting options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Description | | :--- | :--- | | &#x60;name&#x60; | Node name | | &#x60;createdAt&#x60; | Creation date | | &#x60;createdBy&#x60; | Creator first name, last name | | &#x60;updatedAt&#x60; | Last modification date | | &#x60;updatedBy&#x60; | Last modifier first name, last name | | &#x60;fileType&#x60; | File type (extension) | | &#x60;classification&#x60; | Classification ID:&lt;ul&gt;&lt;li&gt;1 - public&lt;/li&gt;&lt;li&gt;2 - internal&lt;/li&gt;&lt;li&gt;3 - confidential&lt;/li&gt;&lt;li&gt;4 - strictly confidential&lt;/li&gt;&lt;/ul&gt; | | &#x60;size&#x60; | Node size | | &#x60;cntDeletedVersions&#x60; | Number of deleted versions of this file / folder (**NOT** recursive; for files and folders only) | | &#x60;timestampCreation&#x60; | Creation timestamp | | &#x60;timestampModification&#x60; | Modification timestamp |  &lt;/details&gt;  ### Deprecated sorting options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Description | | :--- | :--- | | &lt;del&gt;&#x60;cntChildren&#x60;&lt;/del&gt; | Number of direct children (**NOT** recursive; for rooms and folders only) |  &lt;/details&gt;

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let opts = {
  'xSdsDateFormat': "xSdsDateFormat_example", // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
  'depthLevel': 56, // Number | * `0` - top level nodes only  * `n` (any positive number) - include `n` levels starting from the current node
  'parentId': 789, // Number | Parent node ID.  Only rooms and folders can be parents.  Parent ID `0` or empty is the root node.
  'roomManager': true, // Boolean | Show all rooms for management perspective.  Only possible for _Rooms Managers_ / _Room Admins_.  For all other users, it will be ignored.
  'filter': "filter_example", // String | Filter string
  'sort': "sort_example", // String | Sort string
  'offset': 56, // Number | Range offset
  'limit': 56, // Number | Range limit.  Maximum 500.   For more results please use paging (`offset` + `limit`).
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestNodes(opts, (error, data, response) => {
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
 **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] 
 **depthLevel** | **Number**| * &#x60;0&#x60; - top level nodes only  * &#x60;n&#x60; (any positive number) - include &#x60;n&#x60; levels starting from the current node | [optional] 
 **parentId** | **Number**| Parent node ID.  Only rooms and folders can be parents.  Parent ID &#x60;0&#x60; or empty is the root node. | [optional] 
 **roomManager** | **Boolean**| Show all rooms for management perspective.  Only possible for _Rooms Managers_ / _Room Admins_.  For all other users, it will be ignored. | [optional] 
 **filter** | **String**| Filter string | [optional] 
 **sort** | **String**| Sort string | [optional] 
 **offset** | **Number**| Range offset | [optional] 
 **limit** | **Number**| Range limit.  Maximum 500.   For more results please use paging (&#x60;offset&#x60; + &#x60;limit&#x60;). | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**NodeList**](NodeList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestPendingAssignments

> PendingAssignmentList requestPendingAssignments(opts)

Request user-room assignments per group

### Description:   Requests a list of user-room assignments by groups that have **NOT** been approved yet   These can have the state: * **WAITING**   * **DENIED**   * **ACCEPTED**    **ACCEPTED** assignments are already removed from the list.  ### Precondition: None.  ### Postcondition: List of user-room assignments is returned.  ### Further Information: Room administrators **SHOULD** regularly request pending assingments to provide access to rooms for other users.  ### Filtering: All filter fields are connected via logical conjunction (**AND**)   Filter string syntax: &#x60;FIELD_NAME:OPERATOR:VALUE&#x60;    &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;state:eq:WAITING&#x60;   Filter assignments by state &#x60;WAITING&#x60;.  &lt;/details&gt;  ### Filtering options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Filter Description | &#x60;OPERATOR&#x60; | Operator Description | &#x60;VALUE&#x60; | | :--- | :--- | :--- | :--- | :--- | | &#x60;userId&#x60; | User ID filter | &#x60;eq&#x60; | User ID equals value. | &#x60;positive Integer&#x60; | | &#x60;groupId&#x60; | Group ID filter | &#x60;eq&#x60; | Group ID equals value. | &#x60;positive Integer&#x60; | | &#x60;roomId&#x60; | Room ID filter | &#x60;eq&#x60; | Room ID equals value. | &#x60;positive Integer&#x60; | | &#x60;state&#x60; | Assignment state | &#x60;eq&#x60; | Assignment state equals value. | &#x60;WAITING or DENIED&#x60; |  &lt;/details&gt;  ---  ### Sorting: Sort string syntax: &#x60;FIELD_NAME:ORDER&#x60;   &#x60;ORDER&#x60; can be &#x60;asc&#x60; or &#x60;desc&#x60;.   Multiple sort criteria are possible.   Fields are connected via logical conjunction **AND**.  &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;userId:desc|state:asc&#x60;   Sort by &#x60;userId&#x60; descending **AND** &#x60;state&#x60; ascending.  &lt;/details&gt;  ### Sorting options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Description | | :--- | :--- | | &#x60;userId&#x60; | User ID | | &#x60;groupId&#x60; | Group ID | | &#x60;roomId&#x60; | Room ID | | &#x60;state&#x60; | State |  &lt;/details&gt;

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let opts = {
  'offset': 56, // Number | Range offset
  'limit': 56, // Number | Range limit.  Maximum 500.   For more results please use paging (`offset` + `limit`).
  'filter': "filter_example", // String | Filter string
  'sort': "sort_example", // String | Sort string
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestPendingAssignments(opts, (error, data, response) => {
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
 **offset** | **Number**| Range offset | [optional] 
 **limit** | **Number**| Range limit.  Maximum 500.   For more results please use paging (&#x60;offset&#x60; + &#x60;limit&#x60;). | [optional] 
 **filter** | **String**| Filter string | [optional] 
 **sort** | **String**| Sort string | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**PendingAssignmentList**](PendingAssignmentList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestRoomActivitiesLogAsJson

> LogEventList requestRoomActivitiesLogAsJson(roomId, opts)

Request events of a room

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.3.0&lt;/h3&gt;  ### Description: Retrieve syslog (audit log) events related to a room.  ### Precondition: Requires &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read&lt;/span&gt; permissions on that room.  ### Postcondition: List of events is returned.  ### Further Information: Output may be limited to a certain number of entries.   Please use filter criteria and paging.  Sort string syntax: &#x60;FIELD_NAME:ORDER&#x60;   &#x60;ORDER&#x60; can be &#x60;asc&#x60; or &#x60;desc&#x60;.   Multiple sort fields are supported.    &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;time:desc&#x60;   Sort by &#x60;time&#x60; descending (default sort option).  &lt;/details&gt;  ### Sorting options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Description | | :--- | :--- | | &#x60;time&#x60; | Event timestamp |  &lt;/details&gt;

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let roomId = 789; // Number | Room ID
let opts = {
  'xSdsDateFormat': "xSdsDateFormat_example", // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
  'sort': "sort_example", // String | Sort string
  'offset': 56, // Number | Range offset
  'limit': 56, // Number | Range limit.  Maximum 500.   For more results please use paging (`offset` + `limit`).
  'dateStart': "dateStart_example", // String | Filter events from given date   e.g. `2015-12-31T23:59:00`
  'dateEnd': "dateEnd_example", // String | Filter events until given date   e.g. `2015-12-31T23:59:00`
  'type': 56, // Number | Operation ID   cf. `GET /eventlog/operations`
  'userId': 789, // Number | User ID
  'status': 56, // Number | Operation status:  * `0` - Success  * `2` - Error
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestRoomActivitiesLogAsJson(roomId, opts, (error, data, response) => {
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
 **roomId** | **Number**| Room ID | 
 **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] 
 **sort** | **String**| Sort string | [optional] 
 **offset** | **Number**| Range offset | [optional] 
 **limit** | **Number**| Range limit.  Maximum 500.   For more results please use paging (&#x60;offset&#x60; + &#x60;limit&#x60;). | [optional] 
 **dateStart** | **String**| Filter events from given date   e.g. &#x60;2015-12-31T23:59:00&#x60; | [optional] 
 **dateEnd** | **String**| Filter events until given date   e.g. &#x60;2015-12-31T23:59:00&#x60; | [optional] 
 **type** | **Number**| Operation ID   cf. &#x60;GET /eventlog/operations&#x60; | [optional] 
 **userId** | **Number**| User ID | [optional] 
 **status** | **Number**| Operation status:  * &#x60;0&#x60; - Success  * &#x60;2&#x60; - Error | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**LogEventList**](LogEventList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestRoomGroups

> RoomGroupList requestRoomGroups(roomId, opts)

Request room granted group(s) or / and group(s) that can be granted

### Description:   Retrieve a list of groups that are and / or can be granted to the room.  ### Precondition: Any permissions on target room.  ### Postcondition: List of groups is returned.  ### Further Information:  ### Filtering: All filter fields are connected via logical conjunction (**AND**)   Filter string syntax: &#x60;FIELD_NAME:OPERATOR:VALUE&#x60;    &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;isGranted:eq:false|name:cn:searchString&#x60;   Get all groups that are **NOT** granted to this room **AND** whose name is like &#x60;searchString&#x60;.  &lt;/details&gt;  ### Filtering options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Filter Description | &#x60;OPERATOR&#x60; | Operator Description | &#x60;VALUE&#x60; | | :--- | :--- | :--- | :--- | :--- | | &#x60;name&#x60; | Group name filter | &#x60;cn&#x60; | Group name contains value. | &#x60;search String&#x60; | | &#x60;groupId&#x60; | Group ID filter | &#x60;eq&#x60; | Group ID equals value. | &#x60;positive Integer&#x60; | | &#x60;isGranted&#x60; | Filter the groups that have (no) access to this room.&lt;br&gt;**This filter is only available for room administrators.**&lt;br&gt;**Other users can only look for groups in their rooms, so this filter is &#x60;true&#x60; and **CANNOT** be overridden.** | &#x60;eq&#x60; |  | &lt;ul&gt;&lt;li&gt;&#x60;true&#x60;&lt;/li&gt;&lt;li&gt;&#x60;false&#x60;&lt;/li&gt;&lt;li&gt;&#x60;any&#x60;&lt;/li&gt;&lt;/ul&gt;default: &#x60;true&#x60; | | &#x60;permissionsManage&#x60; | Filter the groups that do (not) have &#x60;manage&#x60; permissions in this room. | &#x60;eq&#x60; |  | &#x60;true or false&#x60; | | &#x60;effectivePerm&#x60; | Filter groups with DIRECT or DIRECT **AND** EFFECTIVE permissions&lt;ul&gt;&lt;li&gt;&#x60;false&#x60;: DIRECT permissions&lt;/li&gt;&lt;li&gt;&#x60;true&#x60;: DIRECT **AND** EFFECTIVE permissions&lt;/li&gt;&lt;/ul&gt;DIRECT means: e.g. room administrator grants &#x60;read&#x60; permissions to group of users **directly** on desired room.&lt;br&gt;EFFECTIVE means: e.g. group of users gets &#x60;read&#x60; permissions on desired room through **inheritance**. | &#x60;eq&#x60; |  | &#x60;true or false&#x60;&lt;br&gt;default: &#x60;false&#x60; |  &lt;/details&gt;  ---  ### Sorting: Sort string syntax: &#x60;FIELD_NAME:ORDER&#x60;   &#x60;ORDER&#x60; can be &#x60;asc&#x60; or &#x60;desc&#x60;.   Multiple sort criteria are possible.   Fields are connected via logical conjunction **AND**.  &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;name:desc&#x60;   Sort by &#x60;name&#x60; descending.  &lt;/details&gt;  ### Sorting options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Description | | :--- | :--- | | &#x60;name&#x60; | Group name |  &lt;/details&gt;

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let roomId = 789; // Number | Room ID
let opts = {
  'offset': 56, // Number | Range offset
  'limit': 56, // Number | Range limit.  Maximum 500.   For more results please use paging (`offset` + `limit`).
  'filter': "filter_example", // String | Filter string
  'sort': "sort_example", // String | Sort string
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestRoomGroups(roomId, opts, (error, data, response) => {
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
 **roomId** | **Number**| Room ID | 
 **offset** | **Number**| Range offset | [optional] 
 **limit** | **Number**| Range limit.  Maximum 500.   For more results please use paging (&#x60;offset&#x60; + &#x60;limit&#x60;). | [optional] 
 **filter** | **String**| Filter string | [optional] 
 **sort** | **String**| Sort string | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**RoomGroupList**](RoomGroupList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestRoomPolicies

> RoomPolicies requestRoomPolicies(roomId, opts)

Request Room Policies

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.32.0&lt;/h3&gt;  ### Description:   Retrieve the room policies: * &#x60;defaultExpirationPeriod&#x60;  ### Precondition: User has &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read&lt;/span&gt; permissions in that room.  ### Postcondition: Room Policies returned.  ### Further Information: &#x60;defaultExpirationPeriod&#x60;: Default policy room expiration period in seconds. All existing and future files in a room will have their expiration date set to this period after their respective upload. Existing files can be set to expire earlier afterwards. &#x60;0&#x60; means no default expiration policy will be enforced.    

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let roomId = 789; // Number | Room ID
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestRoomPolicies(roomId, opts, (error, data, response) => {
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
 **roomId** | **Number**| Room ID | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**RoomPolicies**](RoomPolicies.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestRoomRescueKey

> FileKey requestRoomRescueKey(fileId, opts)

Request room rescue key

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128679; Deprecated since v4.24.0&lt;/h3&gt;  ### Description:   Returns the file key for the room emergency password / rescue key of a certain file (if available).  ### Precondition: User with &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read&lt;/span&gt; permissions in parent room.  ### Postcondition: File key is returned.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let fileId = 789; // Number | File ID
let opts = {
  'version': "version_example", // String | Version (NEW)
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestRoomRescueKey(fileId, opts, (error, data, response) => {
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
 **fileId** | **Number**| File ID | 
 **version** | **String**| Version (NEW) | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**FileKey**](FileKey.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestRoomRescueKeyPair

> UserKeyPairContainer requestRoomRescueKeyPair(roomId, opts)

Request room rescue key

### Description:   Retrieve the room rescue key pair.  ### Precondition: User has &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read&lt;/span&gt; permissions in that room.  ### Postcondition: Key pair is returned.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let roomId = 789; // Number | Room ID
let opts = {
  'xSdsDateFormat': "xSdsDateFormat_example", // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
  'version': "version_example", // String | Version (NEW)
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestRoomRescueKeyPair(roomId, opts, (error, data, response) => {
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
 **roomId** | **Number**| Room ID | 
 **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] 
 **version** | **String**| Version (NEW) | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**UserKeyPairContainer**](UserKeyPairContainer.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestRoomRescueKeyPairs

> [UserKeyPairContainer] requestRoomRescueKeyPairs(roomId, opts)

Request all room rescue key pairs

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.24.0&lt;/h3&gt;  ### Description:   Retrieve all room rescue key pairs to allow migrating room-rescue-key-encrypted file keys.  ### Precondition: User has &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read&lt;/span&gt; permissions in that room.  ### Postcondition: List of key pairs is returned.  ### Further Information: In the case of an algorithm migration to a room rescue key pair, one should create the new key pair before deleting the old one. This allows re-encrypting file keys with the new key pair, using the old one.  This API allows to retrieve both key pairs, in contrast to &#x60;GET /nodes/rooms/{room_id}/keypair&#x60;, which only delivers the preferred one. 

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let roomId = 789; // Number | Room ID
let opts = {
  'xSdsDateFormat': "xSdsDateFormat_example", // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestRoomRescueKeyPairs(roomId, opts, (error, data, response) => {
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
 **roomId** | **Number**| Room ID | 
 **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**[UserKeyPairContainer]**](UserKeyPairContainer.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestRoomS3Tags

> S3TagList requestRoomS3Tags(roomId, opts)

Request list of all assigned S3 tags to the room

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.9.0&lt;/h3&gt;  ### Description:   Retrieve a list of S3 tags assigned to a room.  ### Precondition: User needs to be a &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Room Administrator&lt;/span&gt;.  ### Postcondition: List of assigned S3 tags is returned.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let roomId = 789; // Number | Room ID
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestRoomS3Tags(roomId, opts, (error, data, response) => {
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
 **roomId** | **Number**| Room ID | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**S3TagList**](S3TagList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestRoomUsers

> RoomUserList requestRoomUsers(roomId, opts)

Request room granted user(s) or / and user(s) that can be granted

### Description:   Retrieve a list of users that are and / or can be granted to the room.  ### Precondition: Any permissions on target room.  ### Postcondition: None.  ### Further Information: List of users is returned.  ### Filtering: All filter fields are connected via logical conjunction (**AND**)   Filter string syntax: &#x60;FIELD_NAME:OPERATOR:VALUE&#x60;    &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &gt; &#x60;permissionsManage:eq:true|user:cn:searchString&#x60;   Get all users that have &#x60;manage&#x60; permissions to this room **AND** whose (&#x60;firstName&#x60; **OR** &#x60;lastName&#x60; **OR** &#x60;email&#x60; **OR** &#x60;username&#x60;) is like &#x60;searchString&#x60;.  &lt;/details&gt;  ### Filtering options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Filter Description | &#x60;OPERATOR&#x60; | Operator Description | &#x60;VALUE&#x60; | | :--- | :--- | :--- | :--- | :--- | | &#x60;user&#x60; | User filter | &#x60;cn&#x60; | User contains value (&#x60;firstName&#x60; **OR** &#x60;lastName&#x60; **OR** &#x60;email&#x60; **OR** &#x60;username&#x60;). | &#x60;search String&#x60; | | &#x60;userId&#x60; | User ID filter | &#x60;eq&#x60; | User ID equals value. | &#x60;positive Integer&#x60; | | &#x60;isGranted&#x60; | Filter the users that have (no) access to this room.&lt;br&gt;**This filter is only available for room administrators.**&lt;br&gt;**Other users can only look for users in their rooms, so this filter is &#x60;true&#x60; and **CANNOT** be overridden.** | &#x60;eq&#x60; |  | &lt;ul&gt;&lt;li&gt;&#x60;true&#x60;&lt;/li&gt;&lt;li&gt;&#x60;false&#x60;&lt;/li&gt;&lt;li&gt;&#x60;any&#x60;&lt;/li&gt;&lt;/ul&gt;default: &#x60;true&#x60; | | &#x60;permissionsManage&#x60; | Filter the users that do (not) have &#x60;manage&#x60; permissions in this room. | &#x60;eq&#x60; |  | &#x60;true or false&#x60; | | &#x60;effectivePerm&#x60; | Filter users with DIRECT or DIRECT **AND** EFFECTIVE permissions&lt;ul&gt;&lt;li&gt;&#x60;false&#x60;: DIRECT permissions&lt;/li&gt;&lt;li&gt;&#x60;true&#x60;: DIRECT **AND** EFFECTIVE permissions&lt;/li&gt;&lt;li&gt;&#x60;any&#x60;: DIRECT **AND** EFFECTIVE **AND** OVER GROUP permissions&lt;/li&gt;&lt;/ul&gt;DIRECT means: e.g. room administrator grants &#x60;read&#x60; permissions to group of users **directly** on desired room.&lt;br&gt;EFFECTIVE means: e.g. group of users gets &#x60;read&#x60; permissions on desired room through **inheritance**.&lt;br&gt;OVER GROUP means: e.g. user gets &#x60;read&#x60; permissions on desired room through **group membership**. | &#x60;eq&#x60; |  | &lt;ul&gt;&lt;li&gt;&#x60;true&#x60;&lt;/li&gt;&lt;li&gt;&#x60;false&#x60;&lt;/li&gt;&lt;li&gt;&#x60;any&#x60;&lt;/li&gt;&lt;/ul&gt;default: &#x60;false&#x60; | | &#x60;hasRole&#x60; | User role filter&lt;br&gt;For more Roles information please call &#x60;GET /roles API&#x60; | &#x60;eq&#x60;, &#x60;neq&#x60; | User role  equals value. | &lt;ul&gt;&lt;li&gt;&#x60;CONFIG_MANAGER&#x60; - Manage global configs&lt;/li&gt;&lt;li&gt;&#x60;USER_MANAGER&#x60; - Manage Users&lt;/li&gt;&lt;li&gt;&#x60;GROUP_MANAGER&#x60; - Manage User-Groups&lt;/li&gt;&lt;li&gt;&#x60;ROOM_MANAGER&#x60; - Manage top level Data Rooms&lt;/li&gt;&lt;li&gt;&#x60;LOG_AUDITOR&#x60; - Read logs&lt;/li&gt;&lt;li&gt;&#x60;NONMEMBER_VIEWER&#x60; - View users and groups when having room manage permission&lt;/li&gt;&lt;li&gt;&#x60;USER&#x60; - Regular User role&lt;/li&gt;&lt;li&gt;&#x60;GUEST_USER&#x60; - Guest User role&lt;/li&gt;&lt;/ul&gt; |  &lt;/details&gt;  ### Deprecated filtering options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Filter Description | &#x60;OPERATOR&#x60; | Operator Description | &#x60;VALUE&#x60; | | :--- | :--- | :--- | :--- | :--- | | &lt;del&gt;&#x60;displayName&#x60;&lt;/del&gt; | User display name filter (use &#x60;user&#x60; filter) | &#x60;cn&#x60; | User display name contains value (&#x60;firstName&#x60; **OR** &#x60;lastName&#x60; **OR** &#x60;email&#x60;). | &#x60;search String&#x60; |  &lt;/details&gt;  ---  ### Sorting: Sort string syntax: &#x60;FIELD_NAME:ORDER&#x60;   &#x60;ORDER&#x60; can be &#x60;asc&#x60; or &#x60;desc&#x60;.   Multiple sort criteria are possible.   Fields are connected via logical conjunction **AND**.  &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;user:desc&#x60;   Sort by &#x60;user&#x60; descending.  &lt;/details&gt;  ### Sorting options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Description | | :--- | :--- | | **&#x60;user&#x60;** | User - sort by &#x60;firstName&#x60;, &#x60;lastName&#x60;, &#x60;username&#x60;, &#x60;email&#x60; (in this order) |  &lt;/details&gt;

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let roomId = 789; // Number | Room ID
let opts = {
  'offset': 56, // Number | Range offset
  'limit': 56, // Number | Range limit.  Maximum 500.   For more results please use paging (`offset` + `limit`).
  'filter': "filter_example", // String | Filter string
  'sort': "sort_example", // String | Sort string
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestRoomUsers(roomId, opts, (error, data, response) => {
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
 **roomId** | **Number**| Room ID | 
 **offset** | **Number**| Range offset | [optional] 
 **limit** | **Number**| Range limit.  Maximum 500.   For more results please use paging (&#x60;offset&#x60; + &#x60;limit&#x60;). | [optional] 
 **filter** | **String**| Filter string | [optional] 
 **sort** | **String**| Sort string | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**RoomUserList**](RoomUserList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestSystemRescueKey

> FileKey requestSystemRescueKey(fileId, opts)

Request system rescue key

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128679; Deprecated since v4.24.0&lt;/h3&gt;  ### Description:   Returns the file key for the system emergency password / rescue key of a certain file (if available).  ### Precondition: User with &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read&lt;/span&gt; permissions in parent room.  ### Postcondition: File key is returned.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let fileId = 789; // Number | File ID
let opts = {
  'version': "version_example", // String | Version (NEW)
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestSystemRescueKey(fileId, opts, (error, data, response) => {
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
 **fileId** | **Number**| File ID | 
 **version** | **String**| Version (NEW) | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**FileKey**](FileKey.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestUploadStatusFiles

> S3FileUploadStatus requestUploadStatusFiles(uploadId, opts)

Request status of S3 file upload

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.15.0&lt;/h3&gt;  ### Description: Request status of a S3 file upload.  ### Precondition: An upload channel has been created and user has to be the creator of the upload channel.  ### Postcondition: Status of S3 multipart upload request is returned.  ### Further Information: None.  ### Possible errors: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | Http Status | Error Code | Description | | :--- | :--- | :--- | | &#x60;400 Bad Request&#x60; | &#x60;-80000&#x60; | Mandatory fields cannot be empty | | &#x60;400 Bad Request&#x60; | &#x60;-80001&#x60; | Invalid positive number | | &#x60;400 Bad Request&#x60; | &#x60;-80002&#x60; | Invalid number | | &#x60;400 Bad Request&#x60; | &#x60;-40001&#x60; | (Target) room is not encrypted | | &#x60;400 Bad Request&#x60; | &#x60;-40755&#x60; | Bad file name | | &#x60;400 Bad Request&#x60; | &#x60;-40763&#x60; | File key must be set for an upload into encrypted room | | &#x60;400 Bad Request&#x60; | &#x60;-50506&#x60; | Exceeds the number of files for this Upload Share | | &#x60;403 Forbidden&#x60; |  | Access denied | | &#x60;404 Not Found&#x60; | &#x60;-20501&#x60; | Upload not found | | &#x60;404 Not Found&#x60; | &#x60;-40000&#x60; | Container not found | | &#x60;404 Not Found&#x60; | &#x60;-41000&#x60; | Node not found | | &#x60;404 Not Found&#x60; | &#x60;-70501&#x60; | User not found | | &#x60;409 Conflict&#x60; | &#x60;-40010&#x60; | Container cannot be overwritten | | &#x60;409 Conflict&#x60; |  | File cannot be overwritten | | &#x60;500 Internal Server Error&#x60; |  | System Error | | &#x60;502 Bad Gateway&#x60; |  | S3 Error | | &#x60;502 Insufficient Storage&#x60; | &#x60;-50504&#x60; | Exceeds the quota for this Upload Share | | &#x60;502 Insufficient Storage&#x60; | &#x60;-40200&#x60; | Exceeds the free node quota in room | | &#x60;502 Insufficient Storage&#x60; | &#x60;-90200&#x60; | Exceeds the free customer quota | | &#x60;502 Insufficient Storage&#x60; | &#x60;-90201&#x60; | Exceeds the free customer physical disk space |  &lt;/details&gt;

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let uploadId = "uploadId_example"; // String | Upload channel ID
let opts = {
  'xSdsDateFormat': "xSdsDateFormat_example", // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestUploadStatusFiles(uploadId, opts, (error, data, response) => {
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
 **uploadId** | **String**| Upload channel ID | 
 **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**S3FileUploadStatus**](S3FileUploadStatus.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestUserFileKey

> FileKey requestUserFileKey(fileId, opts)

Request user&#39;s file key

### Description:   Returns the file key for the current user (if available).  ### Precondition: User with one of the following permissions in parent room: &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage&lt;/span&gt;, &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read&lt;/span&gt;, &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage download share&lt;/span&gt;  ### Postcondition: File key is returned.  ### Further Information: The symmetric file key is encrypted with the user&#39;s public key.   File keys are generated with the workflow _\&quot;Generate file keys\&quot;_ that starts at &#x60;GET /nodes/missingFileKeys&#x60;.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let fileId = 789; // Number | File ID
let opts = {
  'version': "version_example", // String | Version (NEW)
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestUserFileKey(fileId, opts, (error, data, response) => {
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
 **fileId** | **Number**| File ID | 
 **version** | **String**| Version (NEW) | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**FileKey**](FileKey.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## restoreNodes

> restoreNodes(restoreDeletedNodesRequest, opts)

Restore deleted nodes

### Description:   Restore a list of deleted nodes.  ### Precondition: User has &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; create&lt;/span&gt; permissions in parent room and &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; restore recycle bin&lt;/span&gt; permissions.  ### Postcondition: The selected files are moved from the recycle bin to the chosen productive container.  ### Further Information: If no parent ID is provided, the node is restored to its previous location.   The default resolution strategy is &#x60;autorename&#x60; that adds numbers to the file name until the conflict is solved.   If an existing file is overwritten, it is moved to the recycle bin instead of the restored one.  Download share id (if exists) gets changed if: - node with the same name exists in the target container - &#x60;resolutionStrategy&#x60; is &#x60;overwrite&#x60; - &#x60;keepShareLinks&#x60; is &#x60;true&#x60;

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let restoreDeletedNodesRequest = new DracoonApi.RestoreDeletedNodesRequest(); // RestoreDeletedNodesRequest | 
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.restoreNodes(restoreDeletedNodesRequest, opts, (error, data, response) => {
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
 **restoreDeletedNodesRequest** | [**RestoreDeletedNodesRequest**](RestoreDeletedNodesRequest.md)|  | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## revokeRoomGroups

> revokeRoomGroups(roomId, roomGroupsDeleteBatchRequest, opts)

Revoke granted group(s) from room

### Description:   Revoke granted groups from room.  ### Precondition: User needs to be a &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Room Administrator&lt;/span&gt;.  ### Postcondition: Group&#39;s permissions are revoked.  ### Further Information: Batch function.  

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let roomId = 789; // Number | Room ID
let roomGroupsDeleteBatchRequest = new DracoonApi.RoomGroupsDeleteBatchRequest(); // RoomGroupsDeleteBatchRequest | 
let opts = {
  'xSdsDateFormat': "xSdsDateFormat_example", // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.revokeRoomGroups(roomId, roomGroupsDeleteBatchRequest, opts, (error, data, response) => {
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
 **roomId** | **Number**| Room ID | 
 **roomGroupsDeleteBatchRequest** | [**RoomGroupsDeleteBatchRequest**](RoomGroupsDeleteBatchRequest.md)|  | 
 **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## revokeRoomUsers

> revokeRoomUsers(roomId, roomUsersDeleteBatchRequest, opts)

Revoke granted user(s) from room

### Description:   Revoke granted users from room.  ### Precondition: User needs to be a &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Room Administrator&lt;/span&gt;.  ### Postcondition: User&#39;s permissions are revoked.  ### Further Information: Batch function.  

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let roomId = 789; // Number | Room ID
let roomUsersDeleteBatchRequest = new DracoonApi.RoomUsersDeleteBatchRequest(); // RoomUsersDeleteBatchRequest | 
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.revokeRoomUsers(roomId, roomUsersDeleteBatchRequest, opts, (error, data, response) => {
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
 **roomId** | **Number**| Room ID | 
 **roomUsersDeleteBatchRequest** | [**RoomUsersDeleteBatchRequest**](RoomUsersDeleteBatchRequest.md)|  | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## searchNodes

> NodeList searchNodes(searchString, opts)

Search nodes

### Description:   Provides a flat list of file system nodes (rooms, folders or files) of a given parent that are accessible by the current user.  ### Precondition: Authenticated user is allowed to &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128065; see&lt;/span&gt; nodes (i.e. &#x60;isBrowsable &#x3D; true&#x60;).  ### Postcondition: List of nodes is returned.  ### Further Information:   Output is limited to **500** entries.   For more results please use filter criteria and paging (&#x60;offset&#x60; + &#x60;limit&#x60;).   &#x60;EncryptionInfo&#x60; is **NOT** provided.   Wildcard character is the asterisk character: &#x60;*&#x60;  ### Filtering: All filter fields are connected via logical conjunction (**AND**)   Filter string syntax: &#x60;FIELD_NAME:OPERATOR:VALUE[:VALUE...]&#x60;    &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;type:eq:file|createdAt:ge:2015-01-01&#x60;   Get nodes where type equals &#x60;file&#x60; **AND** file creation date is **&gt;&#x3D;** &#x60;2015-01-01&#x60;.  &lt;/details&gt;  ### Filtering options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60;            | Filter Description                | &#x60;OPERATOR&#x60; | Operator Description                                                                                                                                                                                                                                                                | &#x60;VALUE&#x60; | |:------------------------|:----------------------------------| :--- |:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| :--- | | &#x60;type&#x60;                  | Node type filter                  | &#x60;eq&#x60; | Node type equals value.&lt;br&gt;Multiple values are allowed and will be connected via logical disjunction (**OR**).&lt;br&gt;e.g. &#x60;type:eq:room:folder&#x60;                                                                                                                                        | &lt;ul&gt;&lt;li&gt;&#x60;room&#x60;&lt;/li&gt;&lt;li&gt;&#x60;folder&#x60;&lt;/li&gt;&lt;li&gt;&#x60;file&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;fileType&#x60;              | File type filter (file extension) | &#x60;cn, eq&#x60; | File type contains / equals value.                                                                                                                                                                                                                                                  | &#x60;search String&#x60; | | &#x60;classification&#x60;        | Classification filter             | &#x60;eq&#x60; | Classification equals value.                                                                                                                                                                                                                                                        | &lt;ul&gt;&lt;li&gt;&#x60;1&#x60; - public&lt;/li&gt;&lt;li&gt;&#x60;2&#x60; - internal&lt;/li&gt;&lt;li&gt;&#x60;3&#x60; - confidential&lt;/li&gt;&lt;li&gt;&#x60;4&#x60; - strictly confidential&lt;/li&gt;&lt;/ul&gt; | | &#x60;createdBy&#x60;             | Creator login filter              | &#x60;cn, eq&#x60; | Creator login contains / equals value (&#x60;firstName&#x60; **OR** &#x60;lastName&#x60; **OR** &#x60;email&#x60; **OR** &#x60;username&#x60;).                                                                                                                                                                             | &#x60;search String&#x60; | | &#x60;createdById&#x60;           | Creator ID filter                 | &#x60;eq&#x60; | Creator ID equals value.                                                                                                                                                                                                                                                            | &#x60;positive Integer  or -1 for external user&#x60; | | &#x60;createdAt&#x60;             | Creation date filter              | &#x60;ge, le&#x60; | Creation date is greater / less equals than value.&lt;br&gt;Multiple operator values are allowed and will be connected via logical conjunction (**AND**).&lt;br&gt;e.g. &#x60;createdAt:ge:2016-12-31&#x60;&amp;#124;&#x60;createdAt:le:2018-01-01&#x60;                                                                | &#x60;Date (yyyy-MM-dd)&#x60; | | &#x60;updatedBy&#x60;             | Last modifier login filter        | &#x60;cn, eq&#x60; | Last modifier login contains / equals value (&#x60;firstName&#x60; **OR** &#x60;lastName&#x60; **OR** &#x60;email&#x60; **OR** &#x60;username&#x60;).                                                                                                                                                                       | &#x60;search String&#x60; | | &#x60;updatedById&#x60;           | Last modifier ID filter           | &#x60;eq&#x60; | Modifier ID equals value.                                                                                                                                                                                                                                                           | &#x60;positive Integer or -1 for external user&#x60; | | &#x60;updatedAt&#x60;             | Last modification date filter     | &#x60;ge, le&#x60; | Last modification date is greater / less equals than value.&lt;br&gt;Multiple operator values are allowed and will be connected via logical conjunction (**AND**).&lt;br&gt;e.g. &#x60;updatedAt:ge:2016-12-31&#x60;&amp;#124;&#x60;updatedAt:le:2018-01-01&#x60;                                                       | &#x60;Date (yyyy-MM-dd)&#x60; | | &#x60;expireAt&#x60;              | Expiration date filter            | &#x60;ge, le&#x60; | Expiration date is greater / less equals than value.&lt;br&gt;Multiple operator values are allowed and will be connected via logical conjunction (**AND**).&lt;br&gt;e.g. &#x60;expireAt:ge:2016-12-31&#x60;&amp;#124;&#x60;expireAt:le:2018-01-01&#x60;                                                                | &#x60;Date (yyyy-MM-dd)&#x60; | | &#x60;size&#x60;                  | Node size filter                  | &#x60;ge, le&#x60; | Node size is greater / less equals than value.&lt;br&gt;Multiple operator values are allowed and will be connected via logical conjunction (**AND**).&lt;br&gt;e.g. &#x60;size:ge:5&#x60;&amp;#124;&#x60;size:le:10&#x60;                                                                                               | &#x60;size in bytes&#x60; | | &#x60;isFavorite&#x60;            | Favorite filter                   | &#x60;eq&#x60; |                                                                                                                                                                                                                                                                                     | &#x60;true or false&#x60; | | &#x60;branchVersion&#x60;         | Node branch version filter        | &#x60;ge, le&#x60; | Branch version is greater / less equals than value.&lt;br&gt;Multiple operator values are allowed and will be connected via logical conjunction (**AND**).&lt;br&gt;e.g. &#x60;branchVersion:ge:1423280937404&#x60;&amp;#124;&#x60;branchVersion:le:1523280937404&#x60;                                                 | &#x60;version number&#x60; | | &#x60;parentPath&#x60;            | Parent path                       | &#x60;cn, eq&#x60; | Parent path contains / equals  value.                                                                                                                                                                                                                                               | &#x60;search String&#x60; | | &#x60;timestampCreation&#x60;     | Creation timestamp filter         | &#x60;ge, le&#x60; | Creation timestamp is greater / less equals than value.&lt;br&gt;Multiple operator values are allowed and will be connected via logical conjunction (**AND**).&lt;br&gt;e.g. &#x60;timestampCreation:ge:2016-12-31T23:00:00.123&#x60;&amp;#124;&lt;br&gt;&#x60;timestampCreation:le:2018-01-01T11:00:00.540&#x60;             | &#x60;Date (yyyy-MM-dd)&#x60; | | &#x60;timestampModification&#x60; | Modification timestamp filter     | &#x60;ge, le&#x60; | Modification timestamp is greater / less equals than value.&lt;br&gt;Multiple operator values are allowed and will be connected via logical conjunction (**AND**).&lt;br&gt;e.g. &#x60;timestampModification:ge:2016-12-31T23:00:00.123&#x60;&amp;#124;&lt;br&gt;&#x60;timestampModification:le:2018-01-01T11:00:00.540&#x60; | &#x60;Date (yyyy-MM-dd)&#x60; | | &#x60;referenceId&#x60;           | Reference ID filter               | &#x60;eq&#x60; | Reference ID equals value.                                                                                                                                                                                                                                                          | &#x60;Integer &#x60; | &lt;/details&gt;  ---  ### Sorting: Sort string syntax: &#x60;FIELD_NAME:ORDER&#x60;   &#x60;ORDER&#x60; can be &#x60;asc&#x60; or &#x60;desc&#x60;.   Multiple sort criteria are possible.   Fields are connected via logical conjunction **AND**.  &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;name:desc|size:asc&#x60;   Sort by &#x60;name&#x60; descending **AND** &#x60;size&#x60; ascending.  &lt;/details&gt;  ### Sorting options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Description | | :--- | :--- | | &#x60;name&#x60; | Node name | | &#x60;createdAt&#x60; | Creation date | | &#x60;createdBy&#x60; | Creator first name, last name | | &#x60;updatedAt&#x60; | Last modification date | | &#x60;updatedBy&#x60; | Last modifier first name, last name | | &#x60;fileType&#x60; | File type (extension) | | &#x60;classification&#x60; | Classification ID:&lt;ul&gt;&lt;li&gt;1 - public&lt;/li&gt;&lt;li&gt;2 - internal&lt;/li&gt;&lt;li&gt;3 - confidential&lt;/li&gt;&lt;li&gt;4 - strictly confidential&lt;/li&gt;&lt;/ul&gt; | | &#x60;size&#x60; | Node size | | &#x60;cntDeletedVersions&#x60; | Number of deleted versions of this file / folder (**NOT** recursive; for files and folders only) | | &#x60;type&#x60; | Node type (room, folder, file) | | &#x60;parentPath&#x60; | Parent path | | &#x60;timestampCreation&#x60; | Creation timestamp | | &#x60;timestampModification&#x60; | Modification timestamp |  &lt;/details&gt;  ### Deprecated sorting options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Description | | :--- | :--- | | &lt;del&gt;&#x60;cntChildren&#x60;&lt;/del&gt; | Number of direct children (**NOT** recursive; for rooms and folders only) |  &lt;/details&gt;

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let searchString = "searchString_example"; // String | Search string
let opts = {
  'xSdsDateFormat': "xSdsDateFormat_example", // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
  'depthLevel': 56, // Number | * `0` - top level nodes only (default)  * `-1` - full tree  * `n` (any positive number) - include `n` levels starting from the current node
  'parentId': 789, // Number | Parent node ID.  Only rooms and folders can be parents.  Parent ID `0` or empty is the root node.
  'filter': "filter_example", // String | Filter string
  'sort': "sort_example", // String | Sort string
  'offset': 56, // Number | Range offset
  'limit': 56, // Number | Range limit.  Maximum 500.   For more results please use paging (`offset` + `limit`).
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.searchNodes(searchString, opts, (error, data, response) => {
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
 **searchString** | **String**| Search string | 
 **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] 
 **depthLevel** | **Number**| * &#x60;0&#x60; - top level nodes only (default)  * &#x60;-1&#x60; - full tree  * &#x60;n&#x60; (any positive number) - include &#x60;n&#x60; levels starting from the current node | [optional] 
 **parentId** | **Number**| Parent node ID.  Only rooms and folders can be parents.  Parent ID &#x60;0&#x60; or empty is the root node. | [optional] 
 **filter** | **String**| Filter string | [optional] 
 **sort** | **String**| Sort string | [optional] 
 **offset** | **Number**| Range offset | [optional] 
 **limit** | **Number**| Range limit.  Maximum 500.   For more results please use paging (&#x60;offset&#x60; + &#x60;limit&#x60;). | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**NodeList**](NodeList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setRoomPolicies

> setRoomPolicies(roomId, roomPoliciesRequest, opts)

Set room policies

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.32.0&lt;/h3&gt;  ### Description:   Retrieve the room policies: * &#x60;defaultExpirationPeriod&#x60;  ### Precondition: User needs to be a &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Room Administrator&lt;/span&gt;.  ### Postcondition: Room policy is set.  ### Further Information: &#x60;defaultExpirationPeriod&#x60;: Default policy room expiration period in seconds. All existing and future files in a room will have their expiration date set to this period after their respective upload. Existing files can be set to expire earlier afterwards. &#x60;0&#x60; means no default expiration policy will be enforced. This removes all expiration dates from existing files.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let roomId = 789; // Number | Room ID
let roomPoliciesRequest = new DracoonApi.RoomPoliciesRequest(); // RoomPoliciesRequest | 
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.setRoomPolicies(roomId, roomPoliciesRequest, opts, (error, data, response) => {
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
 **roomId** | **Number**| Room ID | 
 **roomPoliciesRequest** | [**RoomPoliciesRequest**](RoomPoliciesRequest.md)|  | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## setRoomRescueKeyPair

> setRoomRescueKeyPair(roomId, userKeyPairContainer, opts)

Set room&#39;s rescue key pair

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.24.0&lt;/h3&gt;  ### Description:   Set room rescue key pair.  ### Precondition: User needs to be a &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Room Administrator&lt;/span&gt;.  ### Postcondition: Key pair is set.  ### Further Information: Room rescue key pair can be used to upgrade algorithm.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let roomId = 789; // Number | Room ID
let userKeyPairContainer = new DracoonApi.UserKeyPairContainer(); // UserKeyPairContainer | 
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.setRoomRescueKeyPair(roomId, userKeyPairContainer, opts, (error, data, response) => {
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
 **roomId** | **Number**| Room ID | 
 **userKeyPairContainer** | [**UserKeyPairContainer**](UserKeyPairContainer.md)|  | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## setRoomS3Tags

> S3TagList setRoomS3Tags(roomId, s3TagIds, opts)

Set S3 tags for a room

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.9.0&lt;/h3&gt;  ### Description:   Set S3 tags to a room.  ### Precondition: User needs to be a &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Room Administrator&lt;/span&gt;.  ### Postcondition: Provided S3 tags are assigned to a room.  ### Further Information: Every request overrides current S3 tags.   Mandatory S3 tag IDs **MUST** be sent.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let roomId = 789; // Number | Room ID
let s3TagIds = new DracoonApi.S3TagIds(); // S3TagIds | 
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.setRoomS3Tags(roomId, s3TagIds, opts, (error, data, response) => {
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
 **roomId** | **Number**| Room ID | 
 **s3TagIds** | [**S3TagIds**](S3TagIds.md)|  | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**S3TagList**](S3TagList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## setUserFileKeys

> setUserFileKeys(userFileKeySetBatchRequest, opts)

Set file keys for a list of users and files

### Description:   Sets symmetric file keys for several users and files.  ### Precondition: User has file keys for the files.   Only settable by users that own one of the following permissions: &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage&lt;/span&gt;, &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read&lt;/span&gt;, &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage download share&lt;/span&gt;, &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change config&lt;/span&gt;  ### Postcondition: Stores new file keys for other users.  ### Further Information: Only users with copies of the file key (encrypted with their public keys) can access a certain file.   This endpoint is used for the distribution of file keys amongst an authorized user base.   User can set file key for himself.   The users who already have a file key are ignored and keep the distributed file key 

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let userFileKeySetBatchRequest = new DracoonApi.UserFileKeySetBatchRequest(); // UserFileKeySetBatchRequest | 
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.setUserFileKeys(userFileKeySetBatchRequest, opts, (error, data, response) => {
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
 **userFileKeySetBatchRequest** | [**UserFileKeySetBatchRequest**](UserFileKeySetBatchRequest.md)|  | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateFavorites

> updateFavorites(updateFavoritesBulkRequest, opts)

Mark or unmark a list of nodes (room, folder or file) as favorite

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.25.0&lt;/h3&gt;  ### Description:   Marks or unmarks a list of nodes (room, folder or file) as favorite.  ### Precondition: Authenticated user is allowed to &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128065; see&lt;/span&gt; the node (i.e. &#x60;isBrowsable &#x3D; true&#x60;).  ### Postcondition: Nodes gets marked as favorite.  ### Further Information: Maximum number of nodes is 200.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let updateFavoritesBulkRequest = new DracoonApi.UpdateFavoritesBulkRequest(); // UpdateFavoritesBulkRequest | 
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.updateFavorites(updateFavoritesBulkRequest, opts, (error, data, response) => {
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
 **updateFavoritesBulkRequest** | [**UpdateFavoritesBulkRequest**](UpdateFavoritesBulkRequest.md)|  | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## updateFile

> Node updateFile(fileId, updateFileRequest, opts)

Updates a file’s metadata

### Description: Updates a list of file’s metadata.  ### Precondition: User has &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change&lt;/span&gt; permissions in parent room.  ### Postcondition: File&#39;s metadata is changed.   

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let fileId = 789; // Number | File ID
let updateFileRequest = new DracoonApi.UpdateFileRequest(); // UpdateFileRequest | 
let opts = {
  'xSdsDateFormat': "xSdsDateFormat_example", // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.updateFile(fileId, updateFileRequest, opts, (error, data, response) => {
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
 **fileId** | **Number**| File ID | 
 **updateFileRequest** | [**UpdateFileRequest**](UpdateFileRequest.md)|  | 
 **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**Node**](Node.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateFiles

> updateFiles(updateFilesBulkRequest, opts)

Updates a list of  file’s metadata

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.25.0&lt;/h3&gt;  ### Description:   Updates a list of file’s metadata.  ### Precondition: User has &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change&lt;/span&gt; permissions in parent room.  ### Postcondition: File&#39;s metadata is changed.  ### Further Information: Maximum number of files is 200 

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let updateFilesBulkRequest = new DracoonApi.UpdateFilesBulkRequest(); // UpdateFilesBulkRequest | 
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.updateFiles(updateFilesBulkRequest, opts, (error, data, response) => {
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
 **updateFilesBulkRequest** | [**UpdateFilesBulkRequest**](UpdateFilesBulkRequest.md)|  | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## updateFolder

> Node updateFolder(folderId, updateFolderRequest, opts)

Updates folder’s metadata

### Description:   Updates folder’s metadata.  ### Precondition: User has &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change&lt;/span&gt; permissions in parent room.  ### Postcondition: Folder&#39;s metadata is changed.  ### Further Information: Notes are limited to **255** characters.  ### Node naming convention: * Node (room, folder, file) names are limited to **150** characters. * Illegal names:   &#x60;&#39;CON&#39;, &#39;PRN&#39;, &#39;AUX&#39;, &#39;NUL&#39;, &#39;COM1&#39;, &#39;COM2&#39;, &#39;COM3&#39;, &#39;COM4&#39;, &#39;COM5&#39;, &#39;COM6&#39;, &#39;COM7&#39;, &#39;COM8&#39;, &#39;COM9&#39;, &#39;LPT1&#39;, &#39;LPT2&#39;, &#39;LPT3&#39;, &#39;LPT4&#39;, &#39;LPT5&#39;, &#39;LPT6&#39;, &#39;LPT7&#39;, &#39;LPT8&#39;, &#39;LPT9&#39;, (and any of those with an extension)&#x60; * Illegal characters in names:   &#x60;&#39;\\\\&#39;, &#39;&lt;&#39;,&#39;&gt;&#39;, &#39;:&#39;, &#39;\\\&quot;&#39;, &#39;|&#39;, &#39;?&#39;, &#39;*&#39;, &#39;/&#39;, leading &#39;-&#39;, trailing &#39;.&#39; &#x60; 

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let folderId = 789; // Number | Folder ID
let updateFolderRequest = new DracoonApi.UpdateFolderRequest(); // UpdateFolderRequest | 
let opts = {
  'xSdsDateFormat': "xSdsDateFormat_example", // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.updateFolder(folderId, updateFolderRequest, opts, (error, data, response) => {
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
 **folderId** | **Number**| Folder ID | 
 **updateFolderRequest** | [**UpdateFolderRequest**](UpdateFolderRequest.md)|  | 
 **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**Node**](Node.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNodeComment

> Comment updateNodeComment(commentId, changeNodeCommentRequest, opts)

Edit node comment

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.10.0&lt;/h3&gt;  ### Description: Edit the text of an existing comment for a specific node.  ### Precondition: User has &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read&lt;/span&gt; permissions on the node and is the creator of the comment.  ### Postcondition: Comments text gets changed.  ### Further Information: Maximum allowed text length: **65535** characters.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let commentId = 789; // Number | Comment ID
let changeNodeCommentRequest = new DracoonApi.ChangeNodeCommentRequest(); // ChangeNodeCommentRequest | 
let opts = {
  'xSdsDateFormat': "xSdsDateFormat_example", // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.updateNodeComment(commentId, changeNodeCommentRequest, opts, (error, data, response) => {
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
 **commentId** | **Number**| Comment ID | 
 **changeNodeCommentRequest** | [**ChangeNodeCommentRequest**](ChangeNodeCommentRequest.md)|  | 
 **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**Comment**](Comment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateRoom

> Node updateRoom(roomId, updateRoomRequest, opts)

Updates room’s metadata

### Description:   Updates room’s metadata.  ### Precondition: User is a &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Room Administrator&lt;/span&gt; at superordinated level.  ### Postcondition: Room&#39;s metadata is changed.  ### Further Information: Notes are limited to **255** characters.  ### Node naming convention: * Node (room, folder, file) names are limited to **150** characters. * Illegal names:   &#x60;&#39;CON&#39;, &#39;PRN&#39;, &#39;AUX&#39;, &#39;NUL&#39;, &#39;COM1&#39;, &#39;COM2&#39;, &#39;COM3&#39;, &#39;COM4&#39;, &#39;COM5&#39;, &#39;COM6&#39;, &#39;COM7&#39;, &#39;COM8&#39;, &#39;COM9&#39;, &#39;LPT1&#39;, &#39;LPT2&#39;, &#39;LPT3&#39;, &#39;LPT4&#39;, &#39;LPT5&#39;, &#39;LPT6&#39;, &#39;LPT7&#39;, &#39;LPT8&#39;, &#39;LPT9&#39;, (and any of those with an extension)&#x60; * Illegal characters in names:   &#x60;&#39;\\\\&#39;, &#39;&lt;&#39;,&#39;&gt;&#39;, &#39;:&#39;, &#39;\\\&quot;&#39;, &#39;|&#39;, &#39;?&#39;, &#39;*&#39;, &#39;/&#39;, leading &#39;-&#39;, trailing &#39;.&#39; &#x60;

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let roomId = 789; // Number | Room ID
let updateRoomRequest = new DracoonApi.UpdateRoomRequest(); // UpdateRoomRequest | 
let opts = {
  'xSdsDateFormat': "xSdsDateFormat_example", // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.updateRoom(roomId, updateRoomRequest, opts, (error, data, response) => {
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
 **roomId** | **Number**| Room ID | 
 **updateRoomRequest** | [**UpdateRoomRequest**](UpdateRoomRequest.md)|  | 
 **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**Node**](Node.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateRoomGroups

> updateRoomGroups(roomId, roomGroupsAddBatchRequest, opts)

Add or change room granted group(s)

### Description: All existing group permissions will be overwritten.  ### Precondition: User needs to be a &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Room Administrator&lt;/span&gt;. To add new members, the user needs the right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; non-members add&lt;/span&gt;, which is included in any role.  ### Postcondition: Group&#39;s permissions are changed.  ### Further Information: Batch function.   

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let roomId = 789; // Number | Room ID
let roomGroupsAddBatchRequest = new DracoonApi.RoomGroupsAddBatchRequest(); // RoomGroupsAddBatchRequest | 
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.updateRoomGroups(roomId, roomGroupsAddBatchRequest, opts, (error, data, response) => {
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
 **roomId** | **Number**| Room ID | 
 **roomGroupsAddBatchRequest** | [**RoomGroupsAddBatchRequest**](RoomGroupsAddBatchRequest.md)|  | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateRoomUsers

> updateRoomUsers(roomId, roomUsersAddBatchRequest, opts)

Add or change room granted user(s)

### Description: All existing user permissions will be overwritten.  ### Precondition: User needs to be a &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Room Administrator&lt;/span&gt;. To add new members, the user needs the right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; non-members add&lt;/span&gt;, which is included in any role.  ### Postcondition: User&#39;s permissions are changed.  ### Further Information: Batch function.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let roomId = 789; // Number | Room ID
let roomUsersAddBatchRequest = new DracoonApi.RoomUsersAddBatchRequest(); // RoomUsersAddBatchRequest | 
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.updateRoomUsers(roomId, roomUsersAddBatchRequest, opts, (error, data, response) => {
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
 **roomId** | **Number**| Room ID | 
 **roomUsersAddBatchRequest** | [**RoomUsersAddBatchRequest**](RoomUsersAddBatchRequest.md)|  | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## uploadFileAsMultipart

> ChunkUploadResponse uploadFileAsMultipart(uploadId, file, opts)

Upload file

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128679; Deprecated since v4.9.0&lt;/h3&gt;  ### Use &#x60;uploads&#x60; API  ### Description:   Uploads a file or parts of it in an active upload channel.  ### Precondition: An upload channel has been created.  ### Postcondition: A file or parts of it are uploaded to a temporary location.  ### Further Information: This endpoints supports chunked upload.    Following &#x60;Content-Types&#x60; are supported by this API: * &#x60;multipart/form-data&#x60; * provided &#x60;Content-Type&#x60;     For both file upload types set the correct &#x60;Content-Type&#x60; header and body.    ### Examples:    * &#x60;multipart/form-data&#x60; &#x60;&#x60;&#x60; POST /api/v4/nodes/files/uploads/{upload_id} HTTP/1.1  Header: ... Content-Type: multipart/form-data; boundary&#x3D;----WebKitFormBoundary7MA4YWxkTrZu0gW ...  Body: ------WebKitFormBoundary7MA4YWxkTrZu0gW Content-Disposition: form-data; name&#x3D;\&quot;file\&quot;; filename&#x3D;\&quot;file.txt\&quot; Content-Type: text/plain  Content of file.txt ------WebKitFormBoundary7MA4YWxkTrZu0gW-- &#x60;&#x60;&#x60;  * any other &#x60;Content-Type&#x60;   &#x60;&#x60;&#x60; POST /api/v4/nodes/files/uploads/{upload_id}  HTTP/1.1  Header: ... Content-Type: { ... } ...  Body: raw content &#x60;&#x60;&#x60;

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.NodesApi();
let uploadId = "uploadId_example"; // String | Upload channel ID
let file = "/path/to/file"; // File | File
let opts = {
  'contentRange': "contentRange_example", // String | Content-Range   e.g. `bytes 0-999/3980`
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.uploadFileAsMultipart(uploadId, file, opts, (error, data, response) => {
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
 **uploadId** | **String**| Upload channel ID | 
 **file** | **File**| File | 
 **contentRange** | **String**| Content-Range   e.g. &#x60;bytes 0-999/3980&#x60; | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**ChunkUploadResponse**](ChunkUploadResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

