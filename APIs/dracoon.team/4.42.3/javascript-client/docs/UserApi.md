# DracoonApi.UserApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**changeUserPassword**](UserApi.md#changeUserPassword) | **PUT** /v4/user/account/password | Change user&#39;s password
[**confirmTotpSetup**](UserApi.md#confirmTotpSetup) | **POST** /v4/user/account/mfa/totp | Confirm second factor TOTP setup with a generated OTP
[**createAndPreserveUserKeyPair**](UserApi.md#createAndPreserveUserKeyPair) | **POST** /v4/user/account/keypairs | Create key pair and preserve copy of old private key
[**deleteMfaTotpSetup**](UserApi.md#deleteMfaTotpSetup) | **DELETE** /v4/user/account/mfa/totp/{id} | Disable a MFA TOTP setup with generated OTP
[**enableCustomerEncryption**](UserApi.md#enableCustomerEncryption) | **PUT** /v4/user/account/customer | Activate client-side encryption for customer
[**getMfaStatusForUser**](UserApi.md#getMfaStatusForUser) | **GET** /v4/user/account/mfa | Request information about the user&#39;s mfa status
[**getTotpSetupInformation**](UserApi.md#getTotpSetupInformation) | **GET** /v4/user/account/mfa/totp | Request information to setup TOTP as second authentication factor
[**listDownloadShareSubscriptions**](UserApi.md#listDownloadShareSubscriptions) | **GET** /v4/user/subscriptions/download_shares | List Download Share subscriptions
[**listNodeSubscriptions**](UserApi.md#listNodeSubscriptions) | **GET** /v4/user/subscriptions/nodes | List node subscriptions
[**listUploadShareSubscriptions**](UserApi.md#listUploadShareSubscriptions) | **GET** /v4/user/subscriptions/upload_shares | List Upload Share subscriptions
[**logout**](UserApi.md#logout) | **POST** /v4/user/logout | Invalidate authentication token
[**pingUser**](UserApi.md#pingUser) | **GET** /v4/user/ping | (authenticated) Ping
[**removeOAuthApproval**](UserApi.md#removeOAuthApproval) | **DELETE** /v4/user/oauth/approvals/{client_id} | Remove OAuth client approval
[**removeOAuthAuthorization**](UserApi.md#removeOAuthAuthorization) | **DELETE** /v4/user/oauth/authorizations/{client_id}/{authorization_id} | Remove a OAuth authorization
[**removeOAuthAuthorizations**](UserApi.md#removeOAuthAuthorizations) | **DELETE** /v4/user/oauth/authorizations/{client_id} | Remove all OAuth authorizations of a client
[**removeProfileAttribute**](UserApi.md#removeProfileAttribute) | **DELETE** /v4/user/profileAttributes/{key} | Remove user profile attribute
[**removeUserKeyPair**](UserApi.md#removeUserKeyPair) | **DELETE** /v4/user/account/keypair | Remove user&#39;s key pair
[**requestAvatar**](UserApi.md#requestAvatar) | **GET** /v4/user/account/avatar | Request avatar
[**requestCustomerInfo**](UserApi.md#requestCustomerInfo) | **GET** /v4/user/account/customer | Request customer information for user
[**requestCustomerKeyPair**](UserApi.md#requestCustomerKeyPair) | **GET** /v4/user/account/customer/keypair | Request customer&#39;s key pair
[**requestListOfNotificationConfigs**](UserApi.md#requestListOfNotificationConfigs) | **GET** /v4/user/notifications/config | Request list of notification configurations
[**requestOAuthApprovals**](UserApi.md#requestOAuthApprovals) | **GET** /v4/user/oauth/approvals | Request list of OAuth client approvals
[**requestOAuthAuthorizations**](UserApi.md#requestOAuthAuthorizations) | **GET** /v4/user/oauth/authorizations | Request list of OAuth client authorizations
[**requestProfileAttributes**](UserApi.md#requestProfileAttributes) | **GET** /v4/user/profileAttributes | Request user profile attributes
[**requestUserInfo**](UserApi.md#requestUserInfo) | **GET** /v4/user/account | Request user account information
[**requestUserKeyPair**](UserApi.md#requestUserKeyPair) | **GET** /v4/user/account/keypair | Request user&#39;s key pair
[**requestUserKeyPairs**](UserApi.md#requestUserKeyPairs) | **GET** /v4/user/account/keypairs | Request all user key pairs
[**resetAvatar**](UserApi.md#resetAvatar) | **DELETE** /v4/user/account/avatar | Reset avatar
[**setProfileAttributes**](UserApi.md#setProfileAttributes) | **POST** /v4/user/profileAttributes | Set user profile attributes
[**setUserKeyPair**](UserApi.md#setUserKeyPair) | **POST** /v4/user/account/keypair | Set user&#39;s key pair
[**subscribeDownloadShare**](UserApi.md#subscribeDownloadShare) | **POST** /v4/user/subscriptions/download_shares/{share_id} | Subscribe Download Share for notifications
[**subscribeDownloadShares**](UserApi.md#subscribeDownloadShares) | **PUT** /v4/user/subscriptions/download_shares | Subscribe or Unsubscribe a List of Download Shares for notifications
[**subscribeNode**](UserApi.md#subscribeNode) | **POST** /v4/user/subscriptions/nodes/{node_id} | Subscribe node for notifications
[**subscribeUploadShare**](UserApi.md#subscribeUploadShare) | **POST** /v4/user/subscriptions/upload_shares/{share_id} | Subscribe Upload Share for notifications
[**subscribeUploadShares**](UserApi.md#subscribeUploadShares) | **PUT** /v4/user/subscriptions/upload_shares | Subscribe or Unsubscribe a List of Upload Shares for notifications
[**unsubscribeDownloadShare**](UserApi.md#unsubscribeDownloadShare) | **DELETE** /v4/user/subscriptions/download_shares/{share_id} | Unsubscribe Download Share from notifications
[**unsubscribeNode**](UserApi.md#unsubscribeNode) | **DELETE** /v4/user/subscriptions/nodes/{node_id} | Unsubscribe node from notifications
[**unsubscribeUploadShare**](UserApi.md#unsubscribeUploadShare) | **DELETE** /v4/user/subscriptions/upload_shares/{share_id} | Unsubscribe Upload Share from notifications
[**updateNodeSubscriptions**](UserApi.md#updateNodeSubscriptions) | **PUT** /v4/user/subscriptions/nodes | Subscribe or Unsubscribe a List of nodes for notifications
[**updateNotificationConfig**](UserApi.md#updateNotificationConfig) | **PUT** /v4/user/notifications/config/{id} | Update notification configuration
[**updateProfileAttributes**](UserApi.md#updateProfileAttributes) | **PUT** /v4/user/profileAttributes | Add or edit user profile attributes
[**updateUserAccount**](UserApi.md#updateUserAccount) | **PUT** /v4/user/account | Update user account
[**uploadAvatarAsMultipart**](UserApi.md#uploadAvatarAsMultipart) | **POST** /v4/user/account/avatar | Change avatar
[**useEmergencyCode**](UserApi.md#useEmergencyCode) | **DELETE** /v4/user/account/mfa | Using emergency-code



## changeUserPassword

> changeUserPassword(changeUserPasswordRequest, opts)

Change user&#39;s password

### Description: Change the user&#39;s password.  ### Precondition: Authenticated user.  ### Postcondition: User&#39;s password is changed.  ### Further Information: The password **MUST** comply to configured password policies.    Forbidden characters in passwords: [&#x60;&amp;&#x60;, &#x60;&#39;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;]

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.UserApi();
let changeUserPasswordRequest = new DracoonApi.ChangeUserPasswordRequest(); // ChangeUserPasswordRequest | 
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.changeUserPassword(changeUserPasswordRequest, opts, (error, data, response) => {
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
 **changeUserPasswordRequest** | [**ChangeUserPasswordRequest**](ChangeUserPasswordRequest.md)|  | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## confirmTotpSetup

> confirmTotpSetup(mfaTotpConfirmationRequest, opts)

Confirm second factor TOTP setup with a generated OTP

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.37.0&lt;/h3&gt;  ### Description: Confirm second factor TOTP setup with a generated OTP.  ### Precondition: Authenticated user    ### Postcondition: Second factor TOTP is enabled.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.UserApi();
let mfaTotpConfirmationRequest = new DracoonApi.MfaTotpConfirmationRequest(); // MfaTotpConfirmationRequest | 
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.confirmTotpSetup(mfaTotpConfirmationRequest, opts, (error, data, response) => {
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
 **mfaTotpConfirmationRequest** | [**MfaTotpConfirmationRequest**](MfaTotpConfirmationRequest.md)|  | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createAndPreserveUserKeyPair

> createAndPreserveUserKeyPair(createKeyPairRequest, opts)

Create key pair and preserve copy of old private key

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.24.0&lt;/h3&gt;  ### Description:   Create user key pair and preserve copy of old private key.  ### Precondition: Authenticated user.  ### Postcondition: Key pair is created.   Copy of old private key is preserved.  ### Further Information: You can submit your old private key, encrypted with your current password.   This allows migrating file keys encrypted with your old key pair to the new one.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.UserApi();
let createKeyPairRequest = new DracoonApi.CreateKeyPairRequest(); // CreateKeyPairRequest | 
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.createAndPreserveUserKeyPair(createKeyPairRequest, opts, (error, data, response) => {
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
 **createKeyPairRequest** | [**CreateKeyPairRequest**](CreateKeyPairRequest.md)|  | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteMfaTotpSetup

> deleteMfaTotpSetup(id, validOtp, opts)

Disable a MFA TOTP setup with generated OTP

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.37.0&lt;/h3&gt;  ### Description:   Delete multi-factor authentication TOTP setup with a valid OTP code.  ### Precondition: Authenticated user   Multi-factor authentication is **NOT** enforced  ### Postcondition: Second factor TOTP is disabled.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.UserApi();
let id = 789; // Number | 
let validOtp = "validOtp_example"; // String | 
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.deleteMfaTotpSetup(id, validOtp, opts, (error, data, response) => {
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
 **id** | **Number**|  | 
 **validOtp** | **String**|  | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## enableCustomerEncryption

> CustomerData enableCustomerEncryption(enableCustomerEncryptionRequest, opts)

Activate client-side encryption for customer

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128679; Deprecated since v4.24.0&lt;/h3&gt;  ### Use &#x60;POST /settings/keypair&#x60; API  ### Description:   Activate client-side encryption for according customer.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change config&lt;/span&gt; required.  ### Postcondition: Client-side encryption is enabled.  ### Further Information: Sets the ability for this customer to encrypt rooms.   Once enabled on customer level, it **CANNOT** be unset.   On activation, a customer rescue key pair **MUST** be set.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.UserApi();
let enableCustomerEncryptionRequest = new DracoonApi.EnableCustomerEncryptionRequest(); // EnableCustomerEncryptionRequest | 
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.enableCustomerEncryption(enableCustomerEncryptionRequest, opts, (error, data, response) => {
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
 **enableCustomerEncryptionRequest** | [**EnableCustomerEncryptionRequest**](EnableCustomerEncryptionRequest.md)|  | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**CustomerData**](CustomerData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getMfaStatusForUser

> UserMfaStatusResponse getMfaStatusForUser(opts)

Request information about the user&#39;s mfa status

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.37.0&lt;/h3&gt;  ### Description: Request information about the user&#39;s mfa status  ### Precondition: Authenticated user.  ### Postcondition: None.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.UserApi();
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.getMfaStatusForUser(opts, (error, data, response) => {
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
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**UserMfaStatusResponse**](UserMfaStatusResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTotpSetupInformation

> TotpSetupResponse getTotpSetupInformation(opts)

Request information to setup TOTP as second authentication factor

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.37.0&lt;/h3&gt;  ### Description:   Get setup information for multi-factor authentication (TOTP).  ### Precondition: Authenticated user.  ### Postcondition: None.   ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.UserApi();
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.getTotpSetupInformation(opts, (error, data, response) => {
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
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**TotpSetupResponse**](TotpSetupResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listDownloadShareSubscriptions

> SubscribedDownloadShareList listDownloadShareSubscriptions(opts)

List Download Share subscriptions

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.20.0&lt;/h3&gt;  ### Description:   Retrieve a list of subscribed Download Shares for current user.   ### Precondition: Authenticated user.  ### Postcondition: List of subscribed Download Shares is returned.  ### Further Information: None.  ### Filtering All filter fields are connected via logical conjunction (**AND**)   Filter string syntax: &#x60;FIELD_NAME:OPERATOR:VALUE[:VALUE...]&#x60;    &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;authParentId:eq:#&#x60;   Get download shares where &#x60;authParentId&#x60; equals &#x60;#&#x60;.  &lt;/details&gt;  ### Filtering options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Filter Description | &#x60;OPERATOR&#x60; | Operator Description | &#x60;VALUE&#x60; | | :--- | :--- | :--- | :--- | :--- | | **&#x60;downloadShareId&#x60;** | Download Share ID filter | &#x60;eq&#x60; | Download Share ID equals value. | &#x60;long value&#x60; | | **&#x60;authParentId&#x60;** | Auth parent ID filter | &#x60;eq&#x60; | Auth parent ID equals value. | &#x60;long value&#x60; |  &lt;/details&gt;  ---  ### Sorting: Sort string syntax: &#x60;FIELD_NAME:ORDER&#x60;   &#x60;ORDER&#x60; can be &#x60;asc&#x60; or &#x60;desc&#x60;.   Multiple sort criteria are possible.   Fields are connected via logical conjunction **AND**.  &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;downloadShareId:desc|authParentId:asc&#x60;   Sort by &#x60;downloadShareId&#x60; descending **AND** &#x60;authParentId&#x60; ascending.  &lt;/details&gt;  ### Sorting options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Description | | :--- | :--- | | **&#x60;downloadShareId&#x60;** | Download Share ID | | **&#x60;authParentId&#x60;** | Auth parent ID |  &lt;/details&gt;

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.UserApi();
let opts = {
  'filter': "filter_example", // String | Filter string
  'limit': 56, // Number | Range limit.  Maximum 500.   For more results please use paging (`offset` + `limit`).
  'offset': 56, // Number | Range offset
  'sort': "sort_example", // String | Sort string
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.listDownloadShareSubscriptions(opts, (error, data, response) => {
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
 **filter** | **String**| Filter string | [optional] 
 **limit** | **Number**| Range limit.  Maximum 500.   For more results please use paging (&#x60;offset&#x60; + &#x60;limit&#x60;). | [optional] 
 **offset** | **Number**| Range offset | [optional] 
 **sort** | **String**| Sort string | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**SubscribedDownloadShareList**](SubscribedDownloadShareList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listNodeSubscriptions

> SubscribedNodeList listNodeSubscriptions(opts)

List node subscriptions

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.20.0&lt;/h3&gt;  ### Description:   Retrieve a list of subscribed nodes for current user.   ### Precondition: Authenticated user.  ### Postcondition: List of subscribed nodes is returned.  ### Further Information: None.  ### Filtering: All filter fields are connected via logical conjunction (**AND**)   Filter string syntax: &#x60;FIELD_NAME:OPERATOR:VALUE[:VALUE...]&#x60;    &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;authParentId:eq:#&#x60;   Get nodes where &#x60;authParentId&#x60; equals &#x60;#&#x60;.  &lt;/details&gt;  ### Filtering options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Filter Description | &#x60;OPERATOR&#x60; | Operator Description | &#x60;VALUE&#x60; | | :--- | :--- | :--- | :--- | :--- | | **&#x60;nodeId&#x60;** | Node ID filter | &#x60;eq&#x60; | Node ID equals value. | &#x60;long value&#x60; | | **&#x60;authParentId&#x60;** | Auth parent ID filter | &#x60;eq&#x60; | Auth parent ID equals value. | &#x60;long value&#x60; |  &lt;/details&gt;  ---  ### Sorting: Sort string syntax: &#x60;FIELD_NAME:ORDER&#x60;   &#x60;ORDER&#x60; can be &#x60;asc&#x60; or &#x60;desc&#x60;.   Multiple sort criteria are possible.   Fields are connected via logical conjunction **AND**.  &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;nodeId:desc|authParentId:asc&#x60;   Sort by &#x60;nodeId&#x60; descending **AND** &#x60;authParentId&#x60; ascending.  &lt;/details&gt;  ### Sorting options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Description | | :--- | :--- | | **&#x60;nodeId&#x60;** | Node ID | | **&#x60;authParentId&#x60;** | Auth parent ID |  &lt;/details&gt;

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.UserApi();
let opts = {
  'filter': "filter_example", // String | Filter string
  'limit': 56, // Number | Range limit.  Maximum 500.   For more results please use paging (`offset` + `limit`).
  'offset': 56, // Number | Range offset
  'sort': "sort_example", // String | Sort string
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.listNodeSubscriptions(opts, (error, data, response) => {
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
 **filter** | **String**| Filter string | [optional] 
 **limit** | **Number**| Range limit.  Maximum 500.   For more results please use paging (&#x60;offset&#x60; + &#x60;limit&#x60;). | [optional] 
 **offset** | **Number**| Range offset | [optional] 
 **sort** | **String**| Sort string | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**SubscribedNodeList**](SubscribedNodeList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listUploadShareSubscriptions

> SubscribedUploadShareList listUploadShareSubscriptions(opts)

List Upload Share subscriptions

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.24.0&lt;/h3&gt;  ### Description:   Retrieve a list of subscribed Upload Shares for current user.   ### Precondition: Authenticated user.  ### Postcondition: List of subscribed Upload Shares is returned.  ### Further Information: None.  ### Filtering All filter fields are connected via logical conjunction (**AND**)   Filter string syntax: &#x60;FIELD_NAME:OPERATOR:VALUE[:VALUE...]&#x60;    &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;targetNodeId:eq:#&#x60;   Get upload shares where &#x60;targetNodeId&#x60; equals &#x60;#&#x60;.  &lt;/details&gt;  ### Filtering options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Filter Description | &#x60;OPERATOR&#x60; | Operator Description | &#x60;VALUE&#x60; | | :--- | :--- | :--- | :--- | :--- | | **&#x60;uploadShareId&#x60;** | Upload Share ID filter | &#x60;eq&#x60; | Upload Share ID equals value. | &#x60;long value&#x60; | | **&#x60;targetNodeId&#x60;** | Target node ID filter | &#x60;eq&#x60; | Target node ID equals value. | &#x60;long value&#x60; |  &lt;/details&gt;  ---  ### Sorting: Sort string syntax: &#x60;FIELD_NAME:ORDER&#x60;   &#x60;ORDER&#x60; can be &#x60;asc&#x60; or &#x60;desc&#x60;.   Multiple sort criteria are possible.   Fields are connected via logical conjunction **AND**.  &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;uploadShareId:desc|targetNodeId:asc&#x60;   Sort by &#x60;uploadShareId&#x60; descending **AND** &#x60;targetNodeId&#x60; ascending.  &lt;/details&gt;  ### Sorting options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Description | | :--- | :--- | | **&#x60;uploadShareId&#x60;** | Upload Share ID | | **&#x60;targetNodeId&#x60;** | Target node ID |  &lt;/details&gt;

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.UserApi();
let opts = {
  'filter': "filter_example", // String | Filter string
  'limit': 56, // Number | Range limit.  Maximum 500.   For more results please use paging (`offset` + `limit`).
  'offset': 56, // Number | Range offset
  'sort': "sort_example", // String | Sort string
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.listUploadShareSubscriptions(opts, (error, data, response) => {
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
 **filter** | **String**| Filter string | [optional] 
 **limit** | **Number**| Range limit.  Maximum 500.   For more results please use paging (&#x60;offset&#x60; + &#x60;limit&#x60;). | [optional] 
 **offset** | **Number**| Range offset | [optional] 
 **sort** | **String**| Sort string | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**SubscribedUploadShareList**](SubscribedUploadShareList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## logout

> logout(opts)

Invalidate authentication token

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128679; Deprecated since v4.12.0&lt;/h3&gt;  ### Description:   Log out a user.  ### Precondition: Authenticated user.  ### Postcondition: * User is logged out   * Authentication token gets invalidated.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.UserApi();
let opts = {
  'everywhere': true, // Boolean | Invalidate all tokens
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.logout(opts, (error, data, response) => {
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
 **everywhere** | **Boolean**| Invalidate all tokens | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## pingUser

> String pingUser(opts)

(authenticated) Ping

### Description: Test connection to DRACOON Server (while authenticated).  ### Precondition: Authenticated user.  ### Postcondition: &#x60;200 OK&#x60; with principal information is returned if successful.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.UserApi();
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.pingUser(opts, (error, data, response) => {
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
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

**String**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain


## removeOAuthApproval

> removeOAuthApproval(clientId, opts)

Remove OAuth client approval

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.22.0&lt;/h3&gt;  ### Functional Description: Delete an OAuth client approval.  ### Precondition: Authenticated user and valid client ID  ### Postcondition: OAuth Client approval is revoked.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.UserApi();
let clientId = "clientId_example"; // String | OAuth client ID
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.removeOAuthApproval(clientId, opts, (error, data, response) => {
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
 **clientId** | **String**| OAuth client ID | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## removeOAuthAuthorization

> removeOAuthAuthorization(clientId, authorizationId, opts)

Remove a OAuth authorization

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.12.0&lt;/h3&gt;  ### Description: Delete an authorization.  ### Precondition: Authenticated user and valid client ID, authorization ID  ### Postcondition: Authorization is revoked.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.UserApi();
let clientId = "clientId_example"; // String | OAuth client ID
let authorizationId = 789; // Number | OAuth authorization ID
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.removeOAuthAuthorization(clientId, authorizationId, opts, (error, data, response) => {
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
 **clientId** | **String**| OAuth client ID | 
 **authorizationId** | **Number**| OAuth authorization ID | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## removeOAuthAuthorizations

> removeOAuthAuthorizations(clientId, opts)

Remove all OAuth authorizations of a client

### Description: Delete all authorizations of a client.  ### Precondition: Authenticated user and valid client ID  ### Postcondition: All authorizations for the client are revoked.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.UserApi();
let clientId = "clientId_example"; // String | OAuth client ID
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.removeOAuthAuthorizations(clientId, opts, (error, data, response) => {
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
 **clientId** | **String**| OAuth client ID | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## removeProfileAttribute

> removeProfileAttribute(key, opts)

Remove user profile attribute

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.7.0&lt;/h3&gt;  ### Description:   Delete custom user profile attribute.  ### Precondition: None.  ### Postcondition: Custom user profile attribute is deleted.  ### Further Information: Allowed characters for keys are: &#x60;[a-zA-Z0-9_-]&#x60;

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.UserApi();
let key = "key_example"; // String | Key
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.removeProfileAttribute(key, opts, (error, data, response) => {
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
 **key** | **String**| Key | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## removeUserKeyPair

> removeUserKeyPair(opts)

Remove user&#39;s key pair

### Description:   Delete user key pair.  ### Precondition: Authenticated user.  ### Postcondition: Key pair is deleted.  ### Further Information: If parameter &#x60;version&#x60; is not set and two key versions exist, this API deletes version A.       If two keys with the same version are set, this API deletes the older one.  This will also remove all file keys that were encrypted with the user public key. If the user had exclusive access to some files, those are removed as well since decrypting them became impossible.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.UserApi();
let opts = {
  'version': "version_example", // String | Version (NEW)
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.removeUserKeyPair(opts, (error, data, response) => {
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
 **version** | **String**| Version (NEW) | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestAvatar

> Avatar requestAvatar(opts)

Request avatar

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.11.0&lt;/h3&gt;  ### Description: Get the avatar.  ### Precondition: Authenticated user.  ### Postcondition: Avatar is returned.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.UserApi();
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestAvatar(opts, (error, data, response) => {
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
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**Avatar**](Avatar.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestCustomerInfo

> CustomerData requestCustomerInfo(opts)

Request customer information for user

### Description:   Use this API to get:  * customer name * used / free space * used / available * user account info  of the according customer.  ### Precondition: Authenticated user.  ### Postcondition: Customer information is returned.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.UserApi();
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestCustomerInfo(opts, (error, data, response) => {
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
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**CustomerData**](CustomerData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestCustomerKeyPair

> UserKeyPairContainer requestCustomerKeyPair(opts)

Request customer&#39;s key pair

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128679; Deprecated since v4.24.0&lt;/h3&gt;  ### Use &#x60;GET /settings/keypair&#x60; API  ### Description:   Retrieve the customer rescue key pair.  ### Precondition: Authenticated user.  ### Postcondition: Key pair is returned.  ### Further Information: The private key is password-based encrypted with &#x60;AES256&#x60; / &#x60;PBKDF2&#x60;.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.UserApi();
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestCustomerKeyPair(opts, (error, data, response) => {
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
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**UserKeyPairContainer**](UserKeyPairContainer.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestListOfNotificationConfigs

> NotificationConfigList requestListOfNotificationConfigs(opts)

Request list of notification configurations

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.20.0&lt;/h3&gt;  ### Description:   Retrieve a list of notification configurations for current user.   ### Precondition: Authenticated user.  ### Postcondition: List of available notification configurations is returned.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.UserApi();
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestListOfNotificationConfigs(opts, (error, data, response) => {
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
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**NotificationConfigList**](NotificationConfigList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestOAuthApprovals

> [OAuthApproval] requestOAuthApprovals(opts)

Request list of OAuth client approvals

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.22.0&lt;/h3&gt;  ### Functional Description:   Retrieve information about all OAuth client approvals.  ### Precondition: Authenticated user.  ### Postcondition: None.  ### Further Information: None.  ### Sorting: Sort string syntax: &#x60;FIELD_NAME:ORDER&#x60;   &#x60;ORDER&#x60; can be &#x60;asc&#x60; or &#x60;desc&#x60;.   Multiple sort criteria are possible.   Fields are connected via logical conjunction **AND**.  &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;clientName:desc&#x60;   Sort by &#x60;clientName&#x60; descending.  &lt;/details&gt;  ### Sorting options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Description | | :--- | :--- | | &#x60;clientName&#x60; | Client name |  &lt;/details&gt;

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.UserApi();
let opts = {
  'xSdsDateFormat': "xSdsDateFormat_example", // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
  'sort': "sort_example", // String | Sort string
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestOAuthApprovals(opts, (error, data, response) => {
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
 **sort** | **String**| Sort string | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**[OAuthApproval]**](OAuthApproval.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestOAuthAuthorizations

> [OAuthAuthorization] requestOAuthAuthorizations(opts)

Request list of OAuth client authorizations

### Description:   Retrieve information about all OAuth client authorizations.  ### Precondition: Authenticated user.  ### Postcondition: List of OAuth client authorizations is returned.  ### Further Information:  ### Filtering: Filter string syntax: &#x60;FIELD_NAME:OPERATOR:VALUE[:VALUE...]&#x60;    &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;isStandard:eq:true&#x60;   Get standard OAuth clients.  &lt;/details&gt;  ### Filtering options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Filter Description | &#x60;OPERATOR&#x60; | Operator Description | &#x60;VALUE&#x60; | | :--- | :--- | :--- | :--- | :--- | | &#x60;isStandard&#x60; | Standard client filter | &#x60;eq&#x60; |  | &#x60;true or false&#x60; |  &lt;/details&gt;  ---  ### Sorting: Sort string syntax: &#x60;FIELD_NAME:ORDER&#x60;   &#x60;ORDER&#x60; can be &#x60;asc&#x60; or &#x60;desc&#x60;.   Multiple sort criteria are possible.   Fields are connected via logical conjunction **AND**.  &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;clientName:desc&#x60;   Sort by &#x60;clientName&#x60; descending.  &lt;/details&gt;  ### Sorting options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Description | | :--- | :--- | | &#x60;clientName&#x60; | Client name |  &lt;/details&gt;

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.UserApi();
let opts = {
  'xSdsDateFormat': "xSdsDateFormat_example", // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
  'filter': "filter_example", // String | Filter string
  'sort': "sort_example", // String | Sort string
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestOAuthAuthorizations(opts, (error, data, response) => {
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
 **filter** | **String**| Filter string | [optional] 
 **sort** | **String**| Sort string | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**[OAuthAuthorization]**](OAuthAuthorization.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestProfileAttributes

> AttributesResponse requestProfileAttributes(opts)

Request user profile attributes

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.7.0&lt;/h3&gt;  ### Description:   Retrieve a list of user profile attributes.  ### Precondition: None.  ### Postcondition: List of attributes is returned.  ### Further Information:  ### Filtering: All filter fields are connected via logical conjunction (**AND**)   Filter string syntax: &#x60;FIELD_NAME:OPERATOR:VALUE[:VALUE...]&#x60;    &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;key:cn:searchString_1|value:cn:searchString_2&#x60;   Filter by attribute key contains &#x60;searchString_1&#x60; **AND** attribute value contains &#x60;searchString_2&#x60;.  &lt;/details&gt;  ### Filtering options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Filter Description | &#x60;OPERATOR&#x60; | Operator Description | &#x60;VALUE&#x60; | | :--- | :--- | :--- | :--- | :--- | | &#x60;key&#x60; | User profile attribute key filter | &#x60;cn, eq, sw&#x60; | Attribute key contains / equals / starts with value. | &#x60;search String&#x60; | | &#x60;value&#x60; | User profile attribute value filter | &#x60;cn, eq, sw&#x60; | Attribute value contains / equals / starts with value. | &#x60;search String&#x60; |  &lt;/details&gt;  ---  ### Sorting: Sort string syntax: &#x60;FIELD_NAME:ORDER&#x60;   &#x60;ORDER&#x60; can be &#x60;asc&#x60; or &#x60;desc&#x60;.   Multiple sort fields are supported.    &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;key:asc|value:desc&#x60;   Sort by &#x60;key&#x60; ascending **AND** by &#x60;value&#x60; descending.  &lt;/details&gt;  ### Sorting options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Description | | :--- | :--- | | &#x60;key&#x60; | User profile attribute key | | &#x60;value&#x60; | User profile attribute value |  &lt;/details&gt;

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.UserApi();
let opts = {
  'offset': 56, // Number | Range offset
  'limit': 56, // Number | Range limit.  Maximum 500.   For more results please use paging (`offset` + `limit`).
  'filter': "filter_example", // String | Filter string
  'sort': "sort_example", // String | Sort string
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestProfileAttributes(opts, (error, data, response) => {
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

[**AttributesResponse**](AttributesResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestUserInfo

> UserAccount requestUserInfo(opts)

Request user account information

### Description:   Retrieves all information regarding the current user&#39;s account.  ### Precondition: Authenticated user.  ### Postcondition: User information is returned.  ### Further Information: Setting the query parameter &#x60;more_info&#x60; to &#x60;true&#x60;, causes the API to return more details e.g. the user&#39;s groups.    &#x60;customer&#x60; (&#x60;CustomerData&#x60;) attribute in &#x60;UserAccount&#x60; response model is deprecated. Please use response from &#x60;GET /user/account/customer&#x60; instead.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.UserApi();
let opts = {
  'xSdsDateFormat': "xSdsDateFormat_example", // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
  'moreInfo': true, // Boolean | Get more info for this user  e.g. list of user groups
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestUserInfo(opts, (error, data, response) => {
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
 **moreInfo** | **Boolean**| Get more info for this user  e.g. list of user groups | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**UserAccount**](UserAccount.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestUserKeyPair

> UserKeyPairContainer requestUserKeyPair(opts)

Request user&#39;s key pair

### Description:   Retrieve the user key pair.  ### Precondition: Authenticated user.  ### Postcondition: Key pair is returned.   ### Further Information: The private key is password-based encrypted with &#x60;AES256&#x60; / &#x60;PBKDF2&#x60;.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.UserApi();
let opts = {
  'xSdsDateFormat': "xSdsDateFormat_example", // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
  'version': "version_example", // String | Version (NEW)
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestUserKeyPair(opts, (error, data, response) => {
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
 **version** | **String**| Version (NEW) | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**UserKeyPairContainer**](UserKeyPairContainer.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestUserKeyPairs

> [UserKeyPairContainer] requestUserKeyPairs(opts)

Request all user key pairs

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.24.0&lt;/h3&gt;  ### Description:   Retrieve all user key pairs to allow re-encrypting file keys without need for a second distributor.  ### Precondition: Authenticated user.  ### Postcondition: List of key pairs is returned.   ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.UserApi();
let opts = {
  'xSdsDateFormat': "xSdsDateFormat_example", // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestUserKeyPairs(opts, (error, data, response) => {
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
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**[UserKeyPairContainer]**](UserKeyPairContainer.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resetAvatar

> Avatar resetAvatar(opts)

Reset avatar

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.11.0&lt;/h3&gt;  ### Description:   Reset (custom) avatar to default avatar.  ### Precondition: Authenticated user.  ### Postcondition: * User&#39;s avatar gets deleted.   * Default avatar is set.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.UserApi();
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.resetAvatar(opts, (error, data, response) => {
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
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**Avatar**](Avatar.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setProfileAttributes

> ProfileAttributes setProfileAttributes(profileAttributesRequest, opts)

Set user profile attributes

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128679; Deprecated since v4.12.0&lt;/h3&gt;  ### Description:   Set custom user profile attributes.  ### Precondition: None.  ### Postcondition: Custom user profile attributes are set.  ### Further Information: Batch function.   All existing user profile attributes will be deleted.    * Allowed characters for keys are: &#x60;[a-zA-Z0-9_-]&#x60;   * Characters are **case-insensitive**   * Maximum key length is **255**   * Maximum value length is **4096**

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.UserApi();
let profileAttributesRequest = new DracoonApi.ProfileAttributesRequest(); // ProfileAttributesRequest | 
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.setProfileAttributes(profileAttributesRequest, opts, (error, data, response) => {
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
 **profileAttributesRequest** | [**ProfileAttributesRequest**](ProfileAttributesRequest.md)|  | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**ProfileAttributes**](ProfileAttributes.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## setUserKeyPair

> setUserKeyPair(userKeyPairContainer, opts)

Set user&#39;s key pair

### Description:   Set the user key pair.  ### Precondition: Authenticated user.  ### Postcondition: Key pair is set.  ### Further Information: Overwriting an existing key pair is **NOT** possible.   Please delete the existing key pair first.   The private key is password-based encrypted with &#x60;AES256&#x60; / &#x60;PBKDF2&#x60;.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.UserApi();
let userKeyPairContainer = new DracoonApi.UserKeyPairContainer(); // UserKeyPairContainer | 
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.setUserKeyPair(userKeyPairContainer, opts, (error, data, response) => {
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
 **userKeyPairContainer** | [**UserKeyPairContainer**](UserKeyPairContainer.md)|  | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## subscribeDownloadShare

> SubscribedDownloadShare subscribeDownloadShare(shareId, opts)

Subscribe Download Share for notifications

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.20.0&lt;/h3&gt;  ### Description:   Subscribe Download Share for notifications.  ### Precondition: User with _\&quot;manage download share\&quot;_ permissions on target node.  ### Postcondition: Download Share is subscribed.   Notifications for this Download Share will be triggered in the future.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.UserApi();
let shareId = 789; // Number | Share ID
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.subscribeDownloadShare(shareId, opts, (error, data, response) => {
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
 **shareId** | **Number**| Share ID | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**SubscribedDownloadShare**](SubscribedDownloadShare.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## subscribeDownloadShares

> subscribeDownloadShares(updateSubscriptionsBulkRequest, opts)

Subscribe or Unsubscribe a List of Download Shares for notifications

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.25.0&lt;/h3&gt;  ### Description:   Subscribe/Unsubscribe download shares for notifications.  ### Precondition: User with _\&quot;manage download share\&quot;_ permissions on target node.    ### Postcondition: Download shares are subscribed or unsubscribed. Notifications for these download shares will be triggered in the future.  ### Further Information: Maximum number of subscriptions is 200.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.UserApi();
let updateSubscriptionsBulkRequest = new DracoonApi.UpdateSubscriptionsBulkRequest(); // UpdateSubscriptionsBulkRequest | 
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.subscribeDownloadShares(updateSubscriptionsBulkRequest, opts, (error, data, response) => {
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
 **updateSubscriptionsBulkRequest** | [**UpdateSubscriptionsBulkRequest**](UpdateSubscriptionsBulkRequest.md)|  | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## subscribeNode

> SubscribedNode subscribeNode(nodeId, opts)

Subscribe node for notifications

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.20.0&lt;/h3&gt;  ### Description: Subscribe node for notifications.  ### Precondition: User has _\&quot;read\&quot;_ permissions in auth parent room.  ### Postcondition: Node is subscribed. Notifications for this node will be triggered in the future.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.UserApi();
let nodeId = 789; // Number | Node ID
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.subscribeNode(nodeId, opts, (error, data, response) => {
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

[**SubscribedNode**](SubscribedNode.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## subscribeUploadShare

> SubscribedUploadShare subscribeUploadShare(shareId, opts)

Subscribe Upload Share for notifications

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.24.0&lt;/h3&gt;  ### Description:   Subscribe Upload Share for notifications.  ### Precondition: User with _\&quot;manage upload share\&quot;_ permissions on target node.  ### Postcondition: Upload Share is subscribed.   Notifications for this Upload Share will be triggered in the future.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.UserApi();
let shareId = 789; // Number | Share ID
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.subscribeUploadShare(shareId, opts, (error, data, response) => {
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
 **shareId** | **Number**| Share ID | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**SubscribedUploadShare**](SubscribedUploadShare.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## subscribeUploadShares

> subscribeUploadShares(updateSubscriptionsBulkRequest, opts)

Subscribe or Unsubscribe a List of Upload Shares for notifications

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.25.0&lt;/h3&gt;  ### Description:   Subscribe/Unsubscribe upload shares for notifications.  ### Precondition: User with _\&quot;manage upload share\&quot;_ permissions on target node.    ### Postcondition: Upload shares are subscribed or unsubscribed. Notifications for these upload shares will be triggered in the future.  ### Further Information: Maximum number of subscriptions is 200.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.UserApi();
let updateSubscriptionsBulkRequest = new DracoonApi.UpdateSubscriptionsBulkRequest(); // UpdateSubscriptionsBulkRequest | 
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.subscribeUploadShares(updateSubscriptionsBulkRequest, opts, (error, data, response) => {
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
 **updateSubscriptionsBulkRequest** | [**UpdateSubscriptionsBulkRequest**](UpdateSubscriptionsBulkRequest.md)|  | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## unsubscribeDownloadShare

> unsubscribeDownloadShare(shareId, opts)

Unsubscribe Download Share from notifications

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.20.0&lt;/h3&gt;  ### Description:   Unsubscribe Download Share from notifications.  ### Precondition: User with _\&quot;manage download share\&quot;_ permissions on target node.  ### Postcondition: Download Share is unsubscribed.   Notifications for this Download Share are disabled.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.UserApi();
let shareId = 789; // Number | Share ID
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.unsubscribeDownloadShare(shareId, opts, (error, data, response) => {
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
 **shareId** | **Number**| Share ID | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## unsubscribeNode

> unsubscribeNode(nodeId, opts)

Unsubscribe node from notifications

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.20.0&lt;/h3&gt;  ### Description:   Unsubscribe node from notifications.  ### Precondition: User has _\&quot;read\&quot;_ permissions in auth parent room.  ### Postcondition: Node is unsubscribed.   Notifications for this node are disabled.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.UserApi();
let nodeId = 789; // Number | Node ID
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.unsubscribeNode(nodeId, opts, (error, data, response) => {
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


## unsubscribeUploadShare

> unsubscribeUploadShare(shareId, opts)

Unsubscribe Upload Share from notifications

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.24.0&lt;/h3&gt;  ### Description:   Unsubscribe Upload Share from notifications.  ### Precondition: User with _\&quot;manage upload share\&quot;_ permissions on target node.  ### Postcondition: Upload Share is unsubscribed.   Notifications for this Upload Share are disabled.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.UserApi();
let shareId = 789; // Number | Share ID
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.unsubscribeUploadShare(shareId, opts, (error, data, response) => {
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
 **shareId** | **Number**| Share ID | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateNodeSubscriptions

> updateNodeSubscriptions(updateSubscriptionsBulkRequest, opts)

Subscribe or Unsubscribe a List of nodes for notifications

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.25.0&lt;/h3&gt;  ### Description:   Subscribe/Unsubscribe nodes for notifications.  ### Precondition: User has _\&quot;read\&quot;_ permissions in auth parent room.  ### Postcondition: Nodes are subscribed or unsubscribed. Notifications for these nodes will be triggered in the future.  ### Further Information: Maximum number of subscriptions is 200.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.UserApi();
let updateSubscriptionsBulkRequest = new DracoonApi.UpdateSubscriptionsBulkRequest(); // UpdateSubscriptionsBulkRequest | 
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.updateNodeSubscriptions(updateSubscriptionsBulkRequest, opts, (error, data, response) => {
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
 **updateSubscriptionsBulkRequest** | [**UpdateSubscriptionsBulkRequest**](UpdateSubscriptionsBulkRequest.md)|  | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## updateNotificationConfig

> NotificationConfig updateNotificationConfig(id, notificationConfigChangeRequest, opts)

Update notification configuration

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.20.0&lt;/h3&gt;  ### Description:   Update notification configuration for current user.   ### Precondition: Authenticated user.  ### Postcondition: Notification configuration is updated.  ### Further Information: Leave &#x60;channelIds&#x60; empty to disable notifications.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.UserApi();
let id = 789; // Number | Unique identifier for a notification configuration
let notificationConfigChangeRequest = new DracoonApi.NotificationConfigChangeRequest(); // NotificationConfigChangeRequest | 
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.updateNotificationConfig(id, notificationConfigChangeRequest, opts, (error, data, response) => {
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
 **id** | **Number**| Unique identifier for a notification configuration | 
 **notificationConfigChangeRequest** | [**NotificationConfigChangeRequest**](NotificationConfigChangeRequest.md)|  | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**NotificationConfig**](NotificationConfig.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateProfileAttributes

> ProfileAttributes updateProfileAttributes(profileAttributesRequest, opts)

Add or edit user profile attributes

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.7.0&lt;/h3&gt;  ### Description:   Add or edit custom user profile attributes. &lt;br/&gt;&lt;br/&gt;&lt;span style&#x3D;\&quot;font-weight: bold; color: red;\&quot;&gt; &amp;#128679; **Warning: Please note that the response with HTTP status code 200 (OK) is deprecated and will be replaced with HTTP status code 204 (No content)!**&lt;/span&gt;&lt;br/&gt;  ### Precondition: None.  ### Postcondition: Custom user profile attributes are added or edited.  ### Further Information: Batch function.   If an entry existed before, it will be overwritten.   Range submodel is never returned.  * Allowed characters for keys are: &#x60;[a-zA-Z0-9_-]&#x60;   * Characters are **case-insensitive**   * Maximum key length is **255**   * Maximum value length is **4096**

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.UserApi();
let profileAttributesRequest = new DracoonApi.ProfileAttributesRequest(); // ProfileAttributesRequest | 
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.updateProfileAttributes(profileAttributesRequest, opts, (error, data, response) => {
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
 **profileAttributesRequest** | [**ProfileAttributesRequest**](ProfileAttributesRequest.md)|  | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**ProfileAttributes**](ProfileAttributes.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateUserAccount

> UserAccount updateUserAccount(updateUserAccountRequest, opts)

Update user account

### Description:   Update current user&#39;s account.  ### Precondition: Authenticated user.  ### Postcondition: User&#39;s account is updated.  ### Further Information: * All input fields are limited to **150** characters.   * **All** characters are allowed.    &#x60;customer&#x60; (&#x60;CustomerData&#x60;) attribute in &#x60;UserAccount&#x60; response model is deprecated. Please use response from &#x60;GET /user/account/customer&#x60; instead.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.UserApi();
let updateUserAccountRequest = new DracoonApi.UpdateUserAccountRequest(); // UpdateUserAccountRequest | 
let opts = {
  'xSdsDateFormat': "xSdsDateFormat_example", // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.updateUserAccount(updateUserAccountRequest, opts, (error, data, response) => {
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
 **updateUserAccountRequest** | [**UpdateUserAccountRequest**](UpdateUserAccountRequest.md)|  | 
 **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**UserAccount**](UserAccount.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## uploadAvatarAsMultipart

> Avatar uploadAvatarAsMultipart(file, opts)

Change avatar

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.11.0&lt;/h3&gt;  ### Description: Change the avatar.  ### Precondition: Authenticated user.  ### Postcondition: Avatar is changed.  ### Further Information: * Media type **MUST** be &#x60;jpeg&#x60; or &#x60;png&#x60; * File size **MUST** bei less than &#x60;5 MB&#x60; * Dimensions **MUST** be &#x60;256x256 px&#x60;

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.UserApi();
let file = "/path/to/file"; // File | File
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.uploadAvatarAsMultipart(file, opts, (error, data, response) => {
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
 **file** | **File**| File | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**Avatar**](Avatar.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## useEmergencyCode

> useEmergencyCode(emergencyCode, opts)

Using emergency-code

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.37.0&lt;/h3&gt;  ### Description: Using emergency code for login  ### Precondition: User has MFA enabled and is already logged in with account/pw (aka pre-Auth-Role)  ### Postcondition: All MFA-setups for the user are deleted.  ### Further Information:   

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.UserApi();
let emergencyCode = "emergencyCode_example"; // String | 
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.useEmergencyCode(emergencyCode, opts, (error, data, response) => {
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
 **emergencyCode** | **String**|  | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

