# DaniWebConnectApi.UsersApi

All URIs are relative to *https://www.daniweb.com/connect/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**usersGet**](UsersApi.md#usersGet) | **GET** /users | 
[**usersGet_0**](UsersApi.md#usersGet_0) | **GET** /users/~ | 
[**usersIDGet**](UsersApi.md#usersIDGet) | **GET** /users/{ID} | 
[**usersIDGroupsGet**](UsersApi.md#usersIDGroupsGet) | **GET** /users/{ID}/groups | 
[**usersIDGroupsMessagesGet**](UsersApi.md#usersIDGroupsMessagesGet) | **GET** /users/{ID}/groups/messages | 
[**usersIDMessagesPost**](UsersApi.md#usersIDMessagesPost) | **POST** /users/{ID}/messages | 
[**usersIDMetadataCollectionsGet**](UsersApi.md#usersIDMetadataCollectionsGet) | **GET** /users/{ID}/metadata/collections | 
[**usersIDMetadataGet**](UsersApi.md#usersIDMetadataGet) | **GET** /users/{ID}/metadata | 
[**usersIDMetadataPost**](UsersApi.md#usersIDMetadataPost) | **POST** /users/{ID}/metadata | 
[**usersIDPositionsGet**](UsersApi.md#usersIDPositionsGet) | **GET** /users/{ID}/positions | 
[**usersIDSynergiesGet**](UsersApi.md#usersIDSynergiesGet) | **GET** /users/{ID}/synergies | 
[**usersIDSynergiesPatch**](UsersApi.md#usersIDSynergiesPatch) | **PATCH** /users/{ID}/synergies | 
[**usersInvitesPost**](UsersApi.md#usersInvitesPost) | **POST** /users/invites | 
[**usersMetadataFiltersPost**](UsersApi.md#usersMetadataFiltersPost) | **POST** /users/metadata/filters | 
[**usersNearbyGet**](UsersApi.md#usersNearbyGet) | **GET** /users/nearby | 
[**usersPatch**](UsersApi.md#usersPatch) | **PATCH** /users/~ | 
[**usersSearchesPost**](UsersApi.md#usersSearchesPost) | **POST** /users/searches | 



## usersGet

> EndpointGetUsers usersGet(opts)



Fetch an array of users that you&#39;ve been matched with, connected with, skipped, or muted. You can only retrieve users existing within the current access token&#39;s bubble. This report may be limited to the last ~500-1000 users you&#39;ve communicated with within the access token&#39;s bubble. Matches are always ordered by synergy, and the order_by parameter is ignored. You can only retrieve bubbled users when retrieving matches, and the bubbled parameter is ignored otherwise. Your 100 best algorithmic matches are based on: Complementary data submitted to Profiles, CVs, and Metadata; Complementary data acquired from third-parties; Location information; Many behavioral data points, such as how responsive users are to connections; Degrees of separation (mutual connections); etc. You may connect with 3 of these algorithmic matches per day for free. However, new members are allowed a grace period of additional daily matches. Each time you choose to meet or mute one of your algorithmic matches, a new match is introduced.

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.UsersApi();
let opts = {
  'filter': "'connections'", // String | 
  'orderBy': "'id'", // String | 
  'bubbled': false, // Boolean | 
  'offset': 0, // Number | 
  'limit': 50 // Number | 
};
apiInstance.usersGet(opts, (error, data, response) => {
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
 **filter** | **String**|  | [optional] [default to &#39;connections&#39;]
 **orderBy** | **String**|  | [optional] [default to &#39;id&#39;]
 **bubbled** | **Boolean**|  | [optional] [default to false]
 **offset** | **Number**|  | [optional] [default to 0]
 **limit** | **Number**|  | [optional] [default to 50]

### Return type

[**EndpointGetUsers**](EndpointGetUsers.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersGet_0

> EndpointGetUsers usersGet_0()



Retrieve the currently OAuth&#39;ed end-user, based on the access token being used, including private information and settings such as their email address.

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.UsersApi();
apiInstance.usersGet_0((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**EndpointGetUsers**](EndpointGetUsers.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersIDGet

> EndpointGetUsersID usersIDGet(ID)



Fetch an array of users. You can only retrieve users existing within the current access token&#39;s bubble.

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.UsersApi();
let ID = [null]; // [Number] | 
apiInstance.usersIDGet(ID, (error, data, response) => {
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
 **ID** | [**[Number]**](Number.md)|  | 

### Return type

[**EndpointGetUsersID**](EndpointGetUsersID.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersIDGroupsGet

> EndpointGetUsersIDGroups usersIDGroupsGet(ID)



You can only retrieve groups that were created by users existing within the current access token&#39;s bubble.

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.UsersApi();
let ID = 56; // Number | 
apiInstance.usersIDGroupsGet(ID, (error, data, response) => {
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
 **ID** | **Number**|  | 

### Return type

[**EndpointGetUsersIDGroups**](EndpointGetUsersIDGroups.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersIDGroupsMessagesGet

> EndpointGetUsersIDGroupsMessages usersIDGroupsMessagesGet(ID, opts)



Paginated transcript of group messages authored by an individual user who exists within the current access token&#39;s bubble. Messages are sorted oldest to newest.

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.UsersApi();
let ID = 56; // Number | 
let opts = {
  'offset': 0, // Number | 
  'limit': 50 // Number | 
};
apiInstance.usersIDGroupsMessagesGet(ID, opts, (error, data, response) => {
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
 **ID** | **Number**|  | 
 **offset** | **Number**|  | [optional] [default to 0]
 **limit** | **Number**|  | [optional] [default to 50]

### Return type

[**EndpointGetUsersIDGroupsMessages**](EndpointGetUsersIDGroupsMessages.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersIDMessagesPost

> EndpointPostUsersIDMessages usersIDMessagesPost(ID, opts)



Initiate a conversation with a user who exists within the current access token&#39;s bubble by sending them an introductory message. If you aren&#39;t already in a conversation with them, this endpoint meets them first, and then sends the message. Note that if you aren&#39;t in an existing conversation, you still must meet the criteria to meet them, meaning the user must currently be free for you to meet. You will receive an error message unless it is currently free for you to meet the user. You can use the users/{:IDS}/synergies endpoint to first determine if the user isn&#39;t already in a conversation with you and is free for you to meet and, if they aren&#39;t, how to pay to meet them. If you don&#39;t specify a message, it defaults to your custom introductory message defined in your settings.

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.UsersApi();
let ID = 56; // Number | 
let opts = {
  'bubbled': false, // Boolean | 
  'metadata0Key': "metadata0Key_example", // String | 
  'metadata0Privacy': "metadata0Privacy_example", // String | 
  'metadata0Values': ["null"], // [String] | 
  'metadata1Key': "metadata1Key_example", // String | 
  'metadata1Privacy': "metadata1Privacy_example", // String | 
  'metadata1Values': ["null"], // [String] | 
  'metadata2Key': "metadata2Key_example", // String | 
  'metadata2Privacy': "metadata2Privacy_example", // String | 
  'metadata2Values': ["null"], // [String] | 
  'textEmoticons': false, // Boolean | 
  'textRaw': "textRaw_example" // String | 
};
apiInstance.usersIDMessagesPost(ID, opts, (error, data, response) => {
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
 **ID** | **Number**|  | 
 **bubbled** | **Boolean**|  | [optional] [default to false]
 **metadata0Key** | **String**|  | [optional] 
 **metadata0Privacy** | **String**|  | [optional] 
 **metadata0Values** | [**[String]**](String.md)|  | [optional] 
 **metadata1Key** | **String**|  | [optional] 
 **metadata1Privacy** | **String**|  | [optional] 
 **metadata1Values** | [**[String]**](String.md)|  | [optional] 
 **metadata2Key** | **String**|  | [optional] 
 **metadata2Privacy** | **String**|  | [optional] 
 **metadata2Values** | [**[String]**](String.md)|  | [optional] 
 **textEmoticons** | **Boolean**|  | [optional] [default to false]
 **textRaw** | **String**|  | [optional] 

### Return type

[**EndpointPostUsersIDMessages**](EndpointPostUsersIDMessages.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## usersIDMetadataCollectionsGet

> EndpointGetUsersIDMetadataCollections usersIDMetadataCollectionsGet(ID)



Retrieve all key/value pairs attached to the current user that you have access to, so long as the user exists within the current access token&#39;s bubble. This includes all public metadata, bubbled metadata that was created by an access token existing within the current bubble, user metadata that was created by you, or private metadata created by you from an access token existing within the current bubble. You will receive an error message unless either the current access token is bubbled, the user is an algorithmic match for you and you have not reached your quota of new introductions for the day, or you have paid to meet them. However, you can always use the /users/metadata/filters endpoint to filter across all users, including those that are unmatched, existing within the current access token&#39;s bubble based on preknown metadata key/value pairs. Metadata will be grouped by key.

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.UsersApi();
let ID = 56; // Number | 
apiInstance.usersIDMetadataCollectionsGet(ID, (error, data, response) => {
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
 **ID** | **Number**|  | 

### Return type

[**EndpointGetUsersIDMetadataCollections**](EndpointGetUsersIDMetadataCollections.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersIDMetadataGet

> EndpointGetUsersIDMetadata usersIDMetadataGet(ID, opts)



Retrieve all key/value pairs attached to the current user that you have access to, so long as the user exists within the current access token&#39;s bubble. This includes all public metadata, bubbled metadata that was created by an access token existing within the current bubble, user metadata that was created by you, or private metadata created by you from an access token existing within the current bubble. You will receive an error message unless either the current access token is bubbled, the user is an algorithmic match for you and you have not reached your quota of new introductions for the day, or you have paid to meet them. However, you can always use the /users/metadata/filters endpoint to filter across all users, including those that are unmatched, existing within the current access token&#39;s bubble based on preknown metadata key/value pairs.

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.UsersApi();
let ID = 56; // Number | 
let opts = {
  'offset': 0, // Number | 
  'limit': 50 // Number | 
};
apiInstance.usersIDMetadataGet(ID, opts, (error, data, response) => {
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
 **ID** | **Number**|  | 
 **offset** | **Number**|  | [optional] [default to 0]
 **limit** | **Number**|  | [optional] [default to 50]

### Return type

[**EndpointGetUsersIDMetadata**](EndpointGetUsersIDMetadata.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersIDMetadataPost

> EndpointPostUsersIDMetadata usersIDMetadataPost(ID, opts)



Attach one-to-many key/value pairs of metadata to a user, so long as the user exists within the current access token&#39;s bubble. You can set one key at a time, with one or many values. A key is unique for each author/bubble combination. Attaching metadata with an existing key that was previously created by you, from within the same bubble, overwrites the key with the new value or set of values. The privacy setting allows you to specify who will have access to the metadata: Public metadata by anyone using an access token which grants them access to the user; Bubbled metadata by anyone using an access token existing within the current bubble; User metadata by you, so long as you are using an access token which grants you access to the user; Private metadata by you, so long as you are using an access token existing within the current bubble.

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.UsersApi();
let ID = 56; // Number | 
let opts = {
  'metadata0Key': "metadata0Key_example", // String | 
  'metadata0Privacy': "metadata0Privacy_example", // String | 
  'metadata0Values': ["null"], // [String] | 
  'metadata1Key': "metadata1Key_example", // String | 
  'metadata1Privacy': "metadata1Privacy_example", // String | 
  'metadata1Values': ["null"], // [String] | 
  'metadata2Key': "metadata2Key_example", // String | 
  'metadata2Privacy': "metadata2Privacy_example", // String | 
  'metadata2Values': ["null"] // [String] | 
};
apiInstance.usersIDMetadataPost(ID, opts, (error, data, response) => {
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
 **ID** | **Number**|  | 
 **metadata0Key** | **String**|  | [optional] 
 **metadata0Privacy** | **String**|  | [optional] 
 **metadata0Values** | [**[String]**](String.md)|  | [optional] 
 **metadata1Key** | **String**|  | [optional] 
 **metadata1Privacy** | **String**|  | [optional] 
 **metadata1Values** | [**[String]**](String.md)|  | [optional] 
 **metadata2Key** | **String**|  | [optional] 
 **metadata2Privacy** | **String**|  | [optional] 
 **metadata2Values** | [**[String]**](String.md)|  | [optional] 

### Return type

[**EndpointPostUsersIDMetadata**](EndpointPostUsersIDMetadata.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## usersIDPositionsGet

> EndpointGetUsersIDPositions usersIDPositionsGet(ID, opts)



Retrieve the CV of a user who exists within the current access token&#39;s bubble. You will receive an error message unless either the current access token is bubbled, the user is an algorithmic match for you and you have not reached your quota of new introductions for the day, or you have paid to meet them. You can only record CV data to your own account. However, any app that you have OAuth&#39;ed against can do so. By default, you will receive CV data that all apps have recorded for the user. Optionally, you can choose to only receive data that the current access token&#39;s bubble has recorded.

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.UsersApi();
let ID = 56; // Number | 
let opts = {
  'bubbled': false // Boolean | 
};
apiInstance.usersIDPositionsGet(ID, opts, (error, data, response) => {
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
 **ID** | **Number**|  | 
 **bubbled** | **Boolean**|  | [optional] [default to false]

### Return type

[**EndpointGetUsersIDPositions**](EndpointGetUsersIDPositions.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersIDSynergiesGet

> EndpointGetUsersIDSynergies usersIDSynergiesGet(ID)



Determine your match relationship with one or more users who exist within the current access token&#39;s bubble. Under some conditions, the price to meet the user will be $0. However, if this is not the case, the PayPal URL payment method will be provided along with the price to meet the user. The PayPal API can be leveraged to send payments programatically, provided the parameters passed in remain the same to ensure that the payment is correctly recorded. Once the payment has been recorded via PayPal IPN, the price to meet the user changes to $0. You can then call the users/{:ID}/meet endpoint to meet the user.

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.UsersApi();
let ID = [null]; // [Number] | 
apiInstance.usersIDSynergiesGet(ID, (error, data, response) => {
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
 **ID** | [**[Number]**](Number.md)|  | 

### Return type

[**EndpointGetUsersIDSynergies**](EndpointGetUsersIDSynergies.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersIDSynergiesPatch

> EndpointPatchUsersIDSynergies usersIDSynergiesPatch(ID, opts)



Skip, mute or unmute a user you&#39;ve been matched with. Skipped matches are only presented as algorithmic matches after all other candidates have been exhausted. You cannot be matched with or meet muted users. You can only skip, mute or unmute users existing within the same bubble.

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.UsersApi();
let ID = 56; // Number | 
let opts = {
  'relationshipMuted': true, // Boolean | 
  'relationshipSkipped': true // Boolean | 
};
apiInstance.usersIDSynergiesPatch(ID, opts, (error, data, response) => {
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
 **ID** | **Number**|  | 
 **relationshipMuted** | **Boolean**|  | [optional] 
 **relationshipSkipped** | **Boolean**|  | [optional] 

### Return type

[**EndpointPatchUsersIDSynergies**](EndpointPatchUsersIDSynergies.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## usersInvitesPost

> EndpointPostUsersInvites usersInvitesPost(opts)



Invite users to into your current access token&#39;s bubble by having Dazah send out email invitations on your behalf. The invitation sends users to begin the OAuth flow for the current application (based on the settings specified in the application&#39;s profile), and therefore they will be redirected to the application upon signing up / logging in. Upon doing so, if they aren&#39;t already, they will automatically be connected with you as well. If your current access token does not escape the bubble, the invitation will specify you wish to connect within the application&#39;s name. If your current access token escapes the bubble, the invitation will specify you wish to connect within Dazah. Submit either a list of emails, or a LinkedIn or Outlook CSV file. You can retrieve your LinkedIn CSV file by exporting your LinkedIn Connections at https://www.linkedin.com/people/export-settings. You can retrieve your Outlook CSV file by using the Outlook Import and Export Wizard. This endpoint buckets the invitations into four categories: Existing invites are existing users who are already connected with you within the current bubble, and are therefore not emailed; Discovered invites are existing Dazah users who are available to be connected with within the current bubble, and are therefore not emailed. Now that they have been discovered, the users/{:ID}/meet API endpoint may be used to connect with them; Invalid invites are existing Dazah users who are unavailable to be connected with, because they have deactivated accounts, are muting you, etc., and are therefore not emailed; Emailed invites are queued to receive an invitation within approximately 1 hour. Note that if you are attempting to invite an existing Dazah user who does not currently exist within your current access token&#39;s bubble, they will fall within the Discovered bucket if your current access token escapes the bubble, but will be emailed an invitation to join the application if your current access token does not escape the bubble.

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.UsersApi();
let opts = {
  'csv': "/path/to/file", // File | 
  'emails': ["null"] // [String] | 
};
apiInstance.usersInvitesPost(opts, (error, data, response) => {
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
 **csv** | **File**|  | [optional] 
 **emails** | [**[String]**](String.md)|  | [optional] 

### Return type

[**EndpointPostUsersInvites**](EndpointPostUsersInvites.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## usersMetadataFiltersPost

> EndpointPostUsersMetadataFilters usersMetadataFiltersPost(opts)



Paginated listing of users filtered by arbitrary metadata criteria. Users must match on all key/value pairs passed in. Users may only match on one value of an array passed in. However, users are sorted based on how many distinct values they match on (most matches first).

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.UsersApi();
let opts = {
  'limit': 50, // Number | 
  'metadata0Key': "metadata0Key_example", // String | 
  'metadata0Values': ["null"], // [String] | 
  'metadata1Key': "metadata1Key_example", // String | 
  'metadata1Values': ["null"], // [String] | 
  'metadata2Key': "metadata2Key_example", // String | 
  'metadata2Values': ["null"], // [String] | 
  'offset': 0 // Number | 
};
apiInstance.usersMetadataFiltersPost(opts, (error, data, response) => {
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
 **limit** | **Number**|  | [optional] [default to 50]
 **metadata0Key** | **String**|  | [optional] 
 **metadata0Values** | [**[String]**](String.md)|  | [optional] 
 **metadata1Key** | **String**|  | [optional] 
 **metadata1Values** | [**[String]**](String.md)|  | [optional] 
 **metadata2Key** | **String**|  | [optional] 
 **metadata2Values** | [**[String]**](String.md)|  | [optional] 
 **offset** | **Number**|  | [optional] [default to 0]

### Return type

[**EndpointPostUsersMetadataFilters**](EndpointPostUsersMetadataFilters.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## usersNearbyGet

> EndpointGetUsersNearby usersNearbyGet(opts)



Fetch an array of users that are geographically close to a set of coordinates. You can only retrieve users existing within the current access token&#39;s bubble.

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.UsersApi();
let opts = {
  'latitude': 3.4, // Number | 
  'longitude': 3.4, // Number | 
  'offset': 0, // Number | 
  'limit': 50 // Number | 
};
apiInstance.usersNearbyGet(opts, (error, data, response) => {
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
 **latitude** | **Number**|  | [optional] 
 **longitude** | **Number**|  | [optional] 
 **offset** | **Number**|  | [optional] [default to 0]
 **limit** | **Number**|  | [optional] [default to 50]

### Return type

[**EndpointGetUsersNearby**](EndpointGetUsersNearby.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersPatch

> EndpointPatchUsers usersPatch(opts)



Update the OAuth&#39;ed end user&#39;s account profile. At this time, for anti-spam reasons, restrictions preclude the ability to update email address and some other settings via the API.

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.UsersApi();
let opts = {
  'company': "company_example", // String | 
  'companySize': "companySize_example", // String | 
  'firstName': "firstName_example", // String | 
  'goals': ["null"], // [String] | 
  'headline': "headline_example", // String | 
  'industry': "industry_example", // String | 
  'introduction': "introduction_example", // String | 
  'jobPosition': "jobPosition_example", // String | 
  'lastName': "lastName_example", // String | 
  'locationImportance': "locationImportance_example", // String | 
  'matchTags': ["null"], // [String] | 
  'pitch': "pitch_example", // String | 
  'tags': ["null"], // [String] | 
  'targetedIndustry': "targetedIndustry_example", // String | 
  'url': "url_example" // String | 
};
apiInstance.usersPatch(opts, (error, data, response) => {
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
 **company** | **String**|  | [optional] 
 **companySize** | **String**|  | [optional] 
 **firstName** | **String**|  | [optional] 
 **goals** | [**[String]**](String.md)|  | [optional] 
 **headline** | **String**|  | [optional] 
 **industry** | **String**|  | [optional] 
 **introduction** | **String**|  | [optional] 
 **jobPosition** | **String**|  | [optional] 
 **lastName** | **String**|  | [optional] 
 **locationImportance** | **String**|  | [optional] 
 **matchTags** | [**[String]**](String.md)|  | [optional] 
 **pitch** | **String**|  | [optional] 
 **tags** | [**[String]**](String.md)|  | [optional] 
 **targetedIndustry** | **String**|  | [optional] 
 **url** | **String**|  | [optional] 

### Return type

[**EndpointPatchUsers**](EndpointPatchUsers.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## usersSearchesPost

> EndpointPostUsersSearches usersSearchesPost(opts)



Filter and perform a weighted search against user profile fields, CV fields, and metadata by specifying a string to search on for each individual field. By default, results are filtered such that all words in the string must exist, unless you seprate the words with OR. To perform a weighted search (as opposed to filtering), specify the weight (from 0-100) the search algorithm should assign to the field. You can optionally exclude users who you are already in or not in conversations with, exclude users who you previously skipped, or exclude users who you are muting. By doing so, you can effectively customize your own matching algorithm. You can specify geo coordinates to only find users a certain distance away from a specific location, or only find users within a certain distance from the OAuth&#39;ed end-user&#39;s last known location. If your app utilizes multiple audience segments, you can specify which audiences you would like to search. You can also limit users to just those who have been recently active. You can also choose to only receive users originating from the current access token&#39;s bubble. Only users existing within the current access token&#39;s bubble will be matched, and you can only search within a group created by a bubbled user.

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.UsersApi();
let opts = {
  'activeWithinXDays': 56, // Number | 
  'audienceIds': [null], // [Number] | 
  'bubbled': false, // Boolean | 
  'excludeConnections': false, // Boolean | 
  'excludeMatches': false, // Boolean | 
  'excludeMuted': false, // Boolean | 
  'excludeSkipped': false, // Boolean | 
  'geoLatitude': 3.4, // Number | 
  'geoLongitude': 3.4, // Number | 
  'geoMilesAway': 3.4, // Number | 
  'groupId': 56, // Number | 
  'limit': 50, // Number | 
  'locationCityQuery': "locationCityQuery_example", // String | 
  'locationCityWeight': 56, // Number | 
  'locationCountryQuery': "locationCountryQuery_example", // String | 
  'locationCountryWeight': 56, // Number | 
  'locationRegionQuery': "locationRegionQuery_example", // String | 
  'locationRegionWeight': 56, // Number | 
  'metadata0Key': "metadata0Key_example", // String | 
  'metadata0Query': "metadata0Query_example", // String | 
  'metadata0Weight': 56, // Number | 
  'metadata1Key': "metadata1Key_example", // String | 
  'metadata1Query': "metadata1Query_example", // String | 
  'metadata1Weight': 56, // Number | 
  'metadata2Key': "metadata2Key_example", // String | 
  'metadata2Query': "metadata2Query_example", // String | 
  'metadata2Weight': 56, // Number | 
  'offset': 0, // Number | 
  'positionOrganizationQuery': "positionOrganizationQuery_example", // String | 
  'positionOrganizationWeight': 56, // Number | 
  'positionRoleQuery': "positionRoleQuery_example", // String | 
  'positionRoleWeight': 56, // Number | 
  'positionSummaryQuery': "positionSummaryQuery_example", // String | 
  'positionSummaryWeight': 56, // Number | 
  'profileFirstNameQuery': "profileFirstNameQuery_example", // String | 
  'profileFirstNameWeight': 56, // Number | 
  'profileGoalsQuery': "profileGoalsQuery_example", // String | 
  'profileGoalsWeight': "profileGoalsWeight_example", // String | 
  'profileHeadlineQuery': "profileHeadlineQuery_example", // String | 
  'profileHeadlineWeight': 56, // Number | 
  'profileIndustryQuery': "profileIndustryQuery_example", // String | 
  'profileIndustryWeight': 56, // Number | 
  'profileLastNameQuery': "profileLastNameQuery_example", // String | 
  'profileLastNameWeight': 56, // Number | 
  'profilePitchQuery': "profilePitchQuery_example", // String | 
  'profilePitchWeight': 56 // Number | 
};
apiInstance.usersSearchesPost(opts, (error, data, response) => {
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
 **activeWithinXDays** | **Number**|  | [optional] 
 **audienceIds** | [**[Number]**](Number.md)|  | [optional] 
 **bubbled** | **Boolean**|  | [optional] [default to false]
 **excludeConnections** | **Boolean**|  | [optional] [default to false]
 **excludeMatches** | **Boolean**|  | [optional] [default to false]
 **excludeMuted** | **Boolean**|  | [optional] [default to false]
 **excludeSkipped** | **Boolean**|  | [optional] [default to false]
 **geoLatitude** | **Number**|  | [optional] 
 **geoLongitude** | **Number**|  | [optional] 
 **geoMilesAway** | **Number**|  | [optional] 
 **groupId** | **Number**|  | [optional] 
 **limit** | **Number**|  | [optional] [default to 50]
 **locationCityQuery** | **String**|  | [optional] 
 **locationCityWeight** | **Number**|  | [optional] 
 **locationCountryQuery** | **String**|  | [optional] 
 **locationCountryWeight** | **Number**|  | [optional] 
 **locationRegionQuery** | **String**|  | [optional] 
 **locationRegionWeight** | **Number**|  | [optional] 
 **metadata0Key** | **String**|  | [optional] 
 **metadata0Query** | **String**|  | [optional] 
 **metadata0Weight** | **Number**|  | [optional] 
 **metadata1Key** | **String**|  | [optional] 
 **metadata1Query** | **String**|  | [optional] 
 **metadata1Weight** | **Number**|  | [optional] 
 **metadata2Key** | **String**|  | [optional] 
 **metadata2Query** | **String**|  | [optional] 
 **metadata2Weight** | **Number**|  | [optional] 
 **offset** | **Number**|  | [optional] [default to 0]
 **positionOrganizationQuery** | **String**|  | [optional] 
 **positionOrganizationWeight** | **Number**|  | [optional] 
 **positionRoleQuery** | **String**|  | [optional] 
 **positionRoleWeight** | **Number**|  | [optional] 
 **positionSummaryQuery** | **String**|  | [optional] 
 **positionSummaryWeight** | **Number**|  | [optional] 
 **profileFirstNameQuery** | **String**|  | [optional] 
 **profileFirstNameWeight** | **Number**|  | [optional] 
 **profileGoalsQuery** | **String**|  | [optional] 
 **profileGoalsWeight** | **String**|  | [optional] 
 **profileHeadlineQuery** | **String**|  | [optional] 
 **profileHeadlineWeight** | **Number**|  | [optional] 
 **profileIndustryQuery** | **String**|  | [optional] 
 **profileIndustryWeight** | **Number**|  | [optional] 
 **profileLastNameQuery** | **String**|  | [optional] 
 **profileLastNameWeight** | **Number**|  | [optional] 
 **profilePitchQuery** | **String**|  | [optional] 
 **profilePitchWeight** | **Number**|  | [optional] 

### Return type

[**EndpointPostUsersSearches**](EndpointPostUsersSearches.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

