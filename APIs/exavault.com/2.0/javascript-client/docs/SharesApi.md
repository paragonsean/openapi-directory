# ExaVault.SharesApi

All URIs are relative to *https://accountname.exavault.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addShare**](SharesApi.md#addShare) | **POST** /shares | Creates a share
[**completeDirectSend**](SharesApi.md#completeDirectSend) | **POST** /shares/complete-send/{id} | Complete send files
[**deleteShareById**](SharesApi.md#deleteShareById) | **DELETE** /shares/{id} | Deactivate a share
[**getShareById**](SharesApi.md#getShareById) | **GET** /shares/{id} | Get a share
[**listShares**](SharesApi.md#listShares) | **GET** /shares | Get a list of shares
[**updateShareById**](SharesApi.md#updateShareById) | **PATCH** /shares/{id} | Update a share



## addShare

> ShareResponse addShare(evApiKey, evAccessToken, opts)

Creates a share

Creates a new share object for the given path in your account. We support three types of shares:    - A **shared folder** allows you to let outside parties access a folder in your account (including any files and nested subfolders) using just a link. Shared folders can be restricted; e.g. with an expiration date, password, download-only, etc. Shared folders are &#39;live&#39;; if someone makes a change to a file in your shared folder, it will be immediately reflected in your account, and vice-versa.   - A file **send** lets you send one or more files via an easy download link. File sends are different than shared folders because file sends are &#39;point in time&#39; -- the recipient will get the files as you sent them. If you later make a change to the source file, it will not be updated for the recipient.   - A **receive** folder lets you receive files into your account. You can either send users a link, or optionally [embed a customized form](/docs/account/05-file-sharing/05-upload-widget) on your website.    **How to send files from your computer using the API**:  In order to use the API to send files which are not already stored in your account, you&#39;ll need to follow a three-step process:  1. Use the [POST /shares](#operation/addShare) endpoint to set up your send, including password, recipients, expiration, etc. You must include **upload** among the permissions in the &#x60;accessMode&#x60; and set the &#x60;sendingLocalFiles&#x60; parameter to **true**. The response that is returned will include a \&quot;meta\&quot; attribute, which contains an **accessToken** attribute. This new access token is valid only for the send. 2. Use the [POST /resources/upload](#operation/uploadFile) endpoint to upload your files to the send you&#39;ve created. The \&quot;/\&quot; path represents the root of the share, not your home directory. **You must send the access token that you received from the first step in the &#x60;ev-access-token&#x60; header** 3. Use the [POST /shares/complete-send/{id}](#operation/completeDirectSend) endpoint to indicate that you have finished uploading files to your send. This will trigger the system to remove the **upload** permission from the share and send any invitation emails you set up in the first step of the process. **You must send YOUR access token in the &#x60;ev-access-token&#x60; header, not the temporary access token**  **Setting the Share Permissions**  Only 5 different combinations of permissions are valid for the &#x60;accessMode&#x60; object:  - **Upload Only**: This allows share visitors to upload to a share but do nothing else to the contained files. To use this mode, set &#x60;upload&#x60; to **true** and all other permissions to **false** - **Download Only**: This allows share visitors to download files from a share but do nothing else to the contained files. To use this mode, set &#x60;download&#x60; to **true** and all other permissions to **false** - **Upload and Download**: This allows share visitors to upload new files to the share or download files within the share, but not make any other changes to the share contents. To use this mode, set &#x60;upload&#x60; and &#x60;download&#x60; to **true** and set both &#x60;modify&#x60; and &#x60;delete&#x60; to **false** - **All but Delete**: This allows share visitors to make any changes to the contents of a share except deleting files. To use this mode, set &#x60;upload&#x60;, &#x60;download&#x60;, and &#x60;modify&#x60; to **true** and set &#x60;delete&#x60; to **false** - **Full Access**: This allows share visitors to make any changes to the contents of a share. To use this mode, set all 4 permissions &#x60;upload&#x60;, &#x60;download&#x60;, &#x60;modify&#x60;, and &#x60;delete&#x60; to **true**  Any other combination of permissions provided as the &#x60;accessMode&#x60; will be rejected as a bad request.  **Notes:**  Authenticated user requires [share permission](/docs/account/04-users/00-introduction#managing-user-roles-and-permissions).

### Example

```javascript
import ExaVault from 'exa_vault';

let apiInstance = new ExaVault.SharesApi();
let evApiKey = "exampleaccount-zwSuWUZ8S38h33qPS8v0s"; // String | API Key required to make the API call.
let evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
let opts = {
  'addShareRequestBody': {"accessMode":{"delete":true,"download":true,"modify":true,"upload":true},"embed":false,"expiration":"2017-09-25T14:12:10Z","fileDropCreateFolders":false,"hasNotification":false,"isPublic":true,"messageBody":null,"messageSubject":"Invitation to a shared folder","name":"Shared Folder","notificationEmails":["notify@example.com","notify2@example.com"],"password":null,"recipients":[{"email":"user@example.com","type":"string"}],"requireEmail":false,"resources":["/testfolder"],"sendingLocalFiles":true,"type":"shared_folder"} // AddShareRequestBody | 
};
apiInstance.addShare(evApiKey, evAccessToken, opts, (error, data, response) => {
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
 **evApiKey** | **String**| API Key required to make the API call. | 
 **evAccessToken** | **String**| Access token required to make the API call. | 
 **addShareRequestBody** | [**AddShareRequestBody**](AddShareRequestBody.md)|  | [optional] 

### Return type

[**ShareResponse**](ShareResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## completeDirectSend

> ShareResponse completeDirectSend(evApiKey, evAccessToken, id)

Complete send files

After uploading the file(s) to be sent, this method will trigger invitation emails and finish the send files setup. If you are not sending files from your own computer in a send, you will not need this step.    **How to send files from your computer using the API**:  In order to use the API to send files which are not already stored in your account, you&#39;ll need to follow a three-step process:  1. Use the [POST /shares](#operation/addShare) endpoint to set up your send, including password, recipients, expiration, etc. You must include **upload** among the permissions in the &#x60;accessMode&#x60; and set the &#x60;sendingLocalFiles&#x60; paramter to **true**. The response that is returned will include a \&quot;meta\&quot; attribute, which contains an **accessToken** attribute. This new access token is valid only for the send. 2. Use the [POST /resources/upload](#operation/uploadFile) endpoint to upload your files to the send you&#39;ve created. The \&quot;/\&quot; path represents the root of the share, not your home directory. **You must send the access token that you received from the first step in the &#x60;ev-access-token&#x60; header** 3. Use the [POST /shares/complete-send/{id}](#operation/completeDirectSend) endpoint to indicate that you have finished uploading files to your send. This will trigger the system to remove the **upload** permission from the share and send any invitation emails you set up in the first step of the process. **You must send YOUR access token in the &#x60;ev-access-token&#x60; header, not the temporary access token** 

### Example

```javascript
import ExaVault from 'exa_vault';

let apiInstance = new ExaVault.SharesApi();
let evApiKey = "exampleaccount-zwSuWUZ8S38h33qPS8v0s"; // String | API Key
let evAccessToken = "19853ef63a0bc348024a9e4cfd4a92520d2dfd04e88d8679fb1ed6bc551593d1"; // String | Access Token
let id = 56; // Number | ID of the share to trigger invitations for.
apiInstance.completeDirectSend(evApiKey, evAccessToken, id, (error, data, response) => {
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
 **evApiKey** | **String**| API Key | 
 **evAccessToken** | **String**| Access Token | 
 **id** | **Number**| ID of the share to trigger invitations for. | 

### Return type

[**ShareResponse**](ShareResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteShareById

> EmptyResponse deleteShareById(id, evApiKey, evAccessToken)

Deactivate a share

Deactivate a share. Deactivating a share does not remove the underlying files for **shared_folder** and **receive** share types; it merely removes the access URL. Deleting a **send** share type does remove the associated files, as files that have been sent are only associated with the share, and aren&#39;t stored anywhere else in the account.  **Notes:**  - You must have [sharing permissons](/docs/account/04-users/00-introduction#managing-user-roles-and-permissions) to use this. - You must have [admin-level access](/docs/account/04-users/01-admin-users), or you must be the owner of the specified share you wish to delete.

### Example

```javascript
import ExaVault from 'exa_vault';

let apiInstance = new ExaVault.SharesApi();
let id = 23241; // Number | ID of the share entry
let evApiKey = "exampleaccount-zwSuWUZ8S38h33qPS8v0s"; // String | API Key required to make the API call.
let evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
apiInstance.deleteShareById(id, evApiKey, evAccessToken, (error, data, response) => {
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
 **id** | **Number**| ID of the share entry | 
 **evApiKey** | **String**| API Key required to make the API call. | 
 **evAccessToken** | **String**| Access token required to make the API call. | 

### Return type

[**EmptyResponse**](EmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getShareById

> ShareResponse getShareById(id, evApiKey, evAccessToken, opts)

Get a share

Get the details for a specific share entry. You can use the &#x60;include&#x60; parameter to also get the details of related records, such as the owning user or the resources involved in the share.  **Notes:**  - Authenticated user requires [share permission](/docs/account/04-users/00-introduction#managing-user-roles-and-permissions). - To get share objects with type send, authenticated user&#39;s role must be admin or master.

### Example

```javascript
import ExaVault from 'exa_vault';

let apiInstance = new ExaVault.SharesApi();
let id = 23241; // Number | ID of the share entry
let evApiKey = "exampleaccount-zwSuWUZ8S38h33qPS8v0s"; // String | API Key
let evAccessToken = "19853ef63a0bc348024a9e4cfd4a92520d2dfd04e88d8679fb1ed6bc551593d1"; // String | Access Token
let opts = {
  'include': "owner,notifications" // String | Comma separated list of relationships to include in response. Possible values are **owner**, **resources**, **notifications**, **activity**.
};
apiInstance.getShareById(id, evApiKey, evAccessToken, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the share entry | 
 **evApiKey** | **String**| API Key | 
 **evAccessToken** | **String**| Access Token | 
 **include** | **String**| Comma separated list of relationships to include in response. Possible values are **owner**, **resources**, **notifications**, **activity**. | [optional] 

### Return type

[**ShareResponse**](ShareResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listShares

> ShareCollectionResponse listShares(evApiKey, evAccessToken, opts)

Get a list of shares

Get a list of shares that you would have access to view through the web interface. You can limit which results are returned by specifying specific types of shares you wish to view, finding things shared with a specific email address, as well as finding shares for specific folder names.   **Notes:**  - Authenticated user requires [share permission](/docs/account/04-users/00-introduction#managing-user-roles-and-permissions). - To get share objects with type send, authenticated user&#39;s role must be admin or master.

### Example

```javascript
import ExaVault from 'exa_vault';

let apiInstance = new ExaVault.SharesApi();
let evApiKey = "exampleaccount-zwSuWUZ8S38h33qPS8v0s"; // String | API Key required to make the API call.
let evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
let opts = {
  'offset': 100, // Number | Current offset of records (for pagination)
  'limit': 10, // Number | Limit of records to be returned (for pagination)
  'scope': "active", // String | Set of shares to return. (**all**=all of them, **active**=shares that are currently active, **curentUser**=shares created by you)
  'sort': "created", // String | What order the list of matches should be in.
  'type': "receive", // String | Limit the list of matches to only certain types of shares.
  'include': "owner,notifications", // String | Comma separated list of relationships to include in response. Possible values are **owner**, **resources**, **notifications**, **activity**.
  'name': "Customer*", // String | When provided, only shares whose names include this value will be in the list. Supports wildcards, such as **send\\*** to return everything starting with \"send\".  Use this parameter if you are searching for shares or receives for a specific folder name. For example **_/Clients/ACME/To Be Processed**.
  'recipient': "test@example.com", // String | Filter the results to include only shares that invited a certain email address. Supports wildcard matching so that **\\*@example.com** will give back entries shared with addresses ending in \"@example.com\". 
  'message': "submitted", // String | When provided, only shares with a message that contains the text will be included in the list of matches. Both the subject and the body of all messages will be checked for matches. This will always be a wildcard match, so that searching for **taxes** will return any shares with a message that contains the word \"taxes\".
  'username': "example", // String | When provided, only shares created by the user with that `username` will be included in the list. Does not support wildcard searching.
  'search': "search_example" // String | Searches the share name, username, recipients, share messages fields for the provided value. Supports wildcard searches.
};
apiInstance.listShares(evApiKey, evAccessToken, opts, (error, data, response) => {
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
 **evApiKey** | **String**| API Key required to make the API call. | 
 **evAccessToken** | **String**| Access token required to make the API call. | 
 **offset** | **Number**| Current offset of records (for pagination) | [optional] 
 **limit** | **Number**| Limit of records to be returned (for pagination) | [optional] [default to 100]
 **scope** | **String**| Set of shares to return. (**all**&#x3D;all of them, **active**&#x3D;shares that are currently active, **curentUser**&#x3D;shares created by you) | [optional] 
 **sort** | **String**| What order the list of matches should be in. | [optional] 
 **type** | **String**| Limit the list of matches to only certain types of shares. | [optional] 
 **include** | **String**| Comma separated list of relationships to include in response. Possible values are **owner**, **resources**, **notifications**, **activity**. | [optional] 
 **name** | **String**| When provided, only shares whose names include this value will be in the list. Supports wildcards, such as **send\\*** to return everything starting with \&quot;send\&quot;.  Use this parameter if you are searching for shares or receives for a specific folder name. For example **_/Clients/ACME/To Be Processed**. | [optional] 
 **recipient** | **String**| Filter the results to include only shares that invited a certain email address. Supports wildcard matching so that **\\*@example.com** will give back entries shared with addresses ending in \&quot;@example.com\&quot;.  | [optional] 
 **message** | **String**| When provided, only shares with a message that contains the text will be included in the list of matches. Both the subject and the body of all messages will be checked for matches. This will always be a wildcard match, so that searching for **taxes** will return any shares with a message that contains the word \&quot;taxes\&quot;. | [optional] 
 **username** | **String**| When provided, only shares created by the user with that &#x60;username&#x60; will be included in the list. Does not support wildcard searching. | [optional] 
 **search** | **String**| Searches the share name, username, recipients, share messages fields for the provided value. Supports wildcard searches. | [optional] 

### Return type

[**ShareCollectionResponse**](ShareCollectionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateShareById

> ShareResponse updateShareById(id, evApiKey, evAccessToken, updateShareRequestBody)

Update a share

Change the settings on an active share. Any changes made will affect all users that have access to the share.   When updating invitees, pass the &#x60;recipients&#x60; body paramater with the full list of people who should be included on the share. If you resend the list without an existing recipient, they will be removed from the share.  **Setting the Share Permissions**  Only 5 different combinations of permissions are valid for the &#x60;accessMode&#x60; object:  - **Upload Only**: This allows share visitors to upload to a share but do nothing else to the contained files. To use this mode, set &#x60;upload&#x60; to **true** and all other permissions to **false** - **Download Only**: This allows share visitors to download files from a share but do nothing else to the contained files. To use this mode, set &#x60;download&#x60; to **true** and all other permissions to **false** - **Upload and Download**: This allows share visitors to upload new files to the share or download files within the share, but not make any other changes to the share contents. To use this mode, set &#x60;upload&#x60; and &#x60;download&#x60; to **true** and set both &#x60;modify&#x60; and &#x60;delete&#x60; to **false** - **All but Delete**: This allows share visitors to make any changes to the contents of a share except deleting files. To use this mode, set &#x60;upload&#x60;, &#x60;download&#x60;, and &#x60;modify&#x60; to **true** and set &#x60;delete&#x60; to **false** - **Full Access**: This allows share visitors to make any changes to the contents of a share. To use this mode, set all 4 permissions &#x60;upload&#x60;, &#x60;download&#x60;, &#x60;modify&#x60;, and &#x60;delete&#x60; to **true**  Any other combination of permissions provided as the &#x60;accessMode&#x60; will be rejected as a bad request.  **Notes:**    - Authenticated user should be the owner of the specified share.

### Example

```javascript
import ExaVault from 'exa_vault';

let apiInstance = new ExaVault.SharesApi();
let id = 23241; // Number | ID of the share entry
let evApiKey = "exampleaccount-zwSuWUZ8S38h33qPS8v0s"; // String | API Key
let evAccessToken = "19853ef63a0bc348024a9e4cfd4a92520d2dfd04e88d8679fb1ed6bc551593d1"; // String | Access Token
let updateShareRequestBody = {"accessMode":{"delete":true,"download":true,"modify":true,"upload":true},"embed":false,"expiration":"2017-09-25T14:12:10Z","fileDropCreateFolders":false,"hasNotification":false,"isPublic":true,"messageBody":null,"messageSubject":"Invitation to a shared folder","name":"Shared Folder","notificationEmails":["notify@example.com","notify2@example.com"],"password":null,"recipients":[{"email":"user@example.com","type":"string"}],"requireEmail":false,"resources":["/testfolder"],"status":0}; // UpdateShareRequestBody | 
apiInstance.updateShareById(id, evApiKey, evAccessToken, updateShareRequestBody, (error, data, response) => {
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
 **id** | **Number**| ID of the share entry | 
 **evApiKey** | **String**| API Key | 
 **evAccessToken** | **String**| Access Token | 
 **updateShareRequestBody** | [**UpdateShareRequestBody**](UpdateShareRequestBody.md)|  | 

### Return type

[**ShareResponse**](ShareResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

