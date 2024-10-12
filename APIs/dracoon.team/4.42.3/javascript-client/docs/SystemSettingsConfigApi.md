# DracoonApi.SystemSettingsConfigApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**requestAuthConfig**](SystemSettingsConfigApi.md#requestAuthConfig) | **GET** /v4/system/config/settings/auth | Request authentication settings
[**requestEventlogConfig**](SystemSettingsConfigApi.md#requestEventlogConfig) | **GET** /v4/system/config/settings/eventlog | Request eventlog settings
[**requestGeneralSettings**](SystemSettingsConfigApi.md#requestGeneralSettings) | **GET** /v4/system/config/settings/general | Request general settings
[**requestInfrastructureProperties**](SystemSettingsConfigApi.md#requestInfrastructureProperties) | **GET** /v4/system/config/settings/infrastructure | Request infrastructure properties
[**requestSyslogConfig**](SystemSettingsConfigApi.md#requestSyslogConfig) | **GET** /v4/system/config/settings/syslog | Request syslog settings
[**requestSystemDefaults**](SystemSettingsConfigApi.md#requestSystemDefaults) | **GET** /v4/system/config/settings/defaults | Request system defaults
[**updateAuthConfig**](SystemSettingsConfigApi.md#updateAuthConfig) | **PUT** /v4/system/config/settings/auth | Update authentication settings
[**updateEventlogConfig**](SystemSettingsConfigApi.md#updateEventlogConfig) | **PUT** /v4/system/config/settings/eventlog | Update eventlog settings
[**updateGeneralSettings**](SystemSettingsConfigApi.md#updateGeneralSettings) | **PUT** /v4/system/config/settings/general | Update general settings
[**updateSyslogConfig**](SystemSettingsConfigApi.md#updateSyslogConfig) | **PUT** /v4/system/config/settings/syslog | Update syslog settings
[**updateSystemDefaults**](SystemSettingsConfigApi.md#updateSystemDefaults) | **PUT** /v4/system/config/settings/defaults | Update system defaults



## requestAuthConfig

> AuthConfig requestAuthConfig(opts)

Request authentication settings

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.6.0&lt;/h3&gt;  ### Description:   DRACOON authentication configuration entry point.    ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: Returns a list of configurable authentication methods.  ### Further Information: Authentication methods are sorted by priority attribute.   Smaller values have higher priority.   Authentication method with highest priority is considered as default.   Priority **MUST** be a positive value.  ### Configurable authentication settings: &lt;details open style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | Authentication Method | Description | | :--- | :--- | | &#x60;basic&#x60; | **Basic** authentication globally allowed.&lt;br&gt;This option **MUST** be activated to allow users to log in with their credentials stored in the database.&lt;br&gt;Formerly known as &#x60;sql&#x60;. | | &#x60;active_directory&#x60; | **Active Directory** authentication globally allowed.&lt;br&gt;This option **MUST** be activated to allow users to log in with their Active Directory credentials. | | &#x60;radius&#x60; | **RADIUS** authentication globally allowed.&lt;br&gt;This option **MUST** be activated to allow users to log in with their RADIUS username, their PIN and a token password. | | &#x60;openid&#x60; | **OpenID Connect** authentication globally allowed.This option **MUST** be activated to allow users to log in with their OpenID Connect identity. |  &lt;/details&gt;

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.SystemSettingsConfigApi();
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestAuthConfig(opts, (error, data, response) => {
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

[**AuthConfig**](AuthConfig.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestEventlogConfig

> EventlogConfig requestEventlogConfig(opts)

Request eventlog settings

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.6.0&lt;/h3&gt;  ### Description:   DRACOON eventlog configuration entry point.    ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: Returns a list of configurable eventlog settings.  ### Further Information: None.  ### Configurable eventlog settings: &lt;details open style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | Setting | Description | Value | | :--- | :--- | :--- | | &#x60;enabled&#x60; | Determines whether eventlog is enabled. | &#x60;true or false&#x60; | | &#x60;retentionPeriod&#x60; | Retention period (in _days_) of eventlog entries.&lt;br&gt;After that period, all entries are deleted. | &#x60;Integer between 0 and 9999&#x60;&lt;br&gt;If set to &#x60;0&#x60;: no logs are deleted | | &#x60;logIpEnabled&#x60; | Determines whether user’s IP address is logged. | &#x60;true or false&#x60; |  &lt;/details&gt;

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.SystemSettingsConfigApi();
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestEventlogConfig(opts, (error, data, response) => {
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

[**EventlogConfig**](EventlogConfig.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestGeneralSettings

> GeneralSettings requestGeneralSettings(opts)

Request general settings

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.6.0&lt;/h3&gt;  ### Description:   DRACOON general settings configuration entry point.    ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: Returns a list of configurable general settings.  ### Further Information:  ### Auth token restrictions:  A restriction is a lower bound for a token timeout and defines a duration after which a token is invalidated when it wasn&#39;t used.   The access/refresh token validity duration of the client is the upper bound. A token is invalidated - in any case - when it has passed.    Auth token restrictions are enabled by default.  * Default access token validity: **2 hours**   * Default refresh token validity: **30 days**  ### Configurable general settings: &lt;details open style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | Setting | Description | Value | | :--- | :--- | :--- | | &#x60;sharePasswordSmsEnabled&#x60; | Determines whether sending of share passwords via SMS is allowed. | &#x60;true or false&#x60; | | &#x60;cryptoEnabled&#x60; | Determines whether client-side encryption is enabled.&lt;br&gt;Can only be enabled once; disabling is **NOT** possible. | &#x60;true or false&#x60; | | &#x60;emailNotificationButtonEnabled&#x60; | Determines whether email notification button is enabled. | &#x60;true or false&#x60; | | &#x60;eulaEnabled&#x60; | Determines whether EULA is enabled.&lt;br&gt;Each user has to confirm the EULA at first login. | &#x60;true or false&#x60; | | &#x60;useS3Storage&#x60; | Defines if S3 is used as storage backend.&lt;br&gt;Can only be enabled once; disabling is **NOT** possible. | &#x60;true or false&#x60; | | &#x60;s3TagsEnabled&#x60; | Determines whether S3 tags are enabled | &#x60;true or false&#x60; | | &#x60;authTokenRestrictions&#x60; | Determines auth token restrictions. (e.g. restricted access token validity) | &#x60;object&#x60; |  &lt;/details&gt;  ### Deprecated configurable general settings: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | Setting                           | Description | Value | |:----------------------------------| :--- | :--- | | &lt;del&gt;&#x60;mediaServerEnabled&#x60;&lt;/del&gt;   | Determines whether media server is enabled.&lt;br&gt;Returns boolean value dependent on conjunction of &#x60;mediaServerConfigEnabled&#x60; AND &#x60;mediaServerEnabled&#x60; | &#x60;true or false&#x60; | | &lt;del&gt;&#x60;weakPasswordEnabled&#x60;&lt;/del&gt;  | Determines whether weak password is allowed.&lt;br&gt;Use &#x60;GET /system/config/policies/passwords&#x60; API to get configured password policies. | &#x60;true or false&#x60; | | &lt;del&gt;&#x60;hideLoginInputFields&#x60;&lt;/del&gt; | Determines whether input fields for login should be enabled | &#x60;true or false&#x60; |  &lt;/details&gt;

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.SystemSettingsConfigApi();
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestGeneralSettings(opts, (error, data, response) => {
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

[**GeneralSettings**](GeneralSettings.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestInfrastructureProperties

> InfrastructureProperties requestInfrastructureProperties(opts)

Request infrastructure properties

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.6.0&lt;/h3&gt;  ### Description:   DRACOON infrastructure properties entry point.    ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: Returns a list of read-only infrastructure properties.  ### Further Information: Source: &#x60;core-service.properties&#x60;  ### Read-only infrastructure properties: &lt;details open style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | Setting | Description | Value | | :--- | :--- | :--- | | &#x60;smsConfigEnabled&#x60; | Determines whether sending of share passwords via SMS is **system-wide** enabled. | &#x60;true or false&#x60; | | &#x60;mediaServerConfigEnabled&#x60; | Determines whether media server is **system-wide** enabled. | &#x60;true or false&#x60; | | &#x60;s3DefaultRegion&#x60; | Suggested S3 region | &#x60;Region name&#x60; | | &#x60;s3EnforceDirectUpload&#x60; | Enforce direct upload to S3 | &#x60;true or false&#x60; | | &#x60;dracoonCloud&#x60; | Determines if the **DRACOON Core** is deployed in the cloud environment | &#x60;true or false&#x60; | | &#x60;tenantUuid&#x60; | Current tenant UUID | &#x60;UUID&#x60; |  &lt;/details&gt;

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.SystemSettingsConfigApi();
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestInfrastructureProperties(opts, (error, data, response) => {
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

[**InfrastructureProperties**](InfrastructureProperties.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestSyslogConfig

> SyslogConfig requestSyslogConfig(opts)

Request syslog settings

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.6.0&lt;/h3&gt;  ### Description:   DRACOON syslog configuration entry point.    ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: Returns a list of configurable syslog settings.  ### Further Information: None.  ### Configurable syslog settings: &lt;details open style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | Setting | Description | Value | | :--- | :--- | :--- | | &#x60;enabled&#x60; | Determines whether syslog is enabled. | &#x60;true or false&#x60; | | &#x60;host&#x60; | Syslog server (IP or FQDN) | &#x60;DNS name or IPv4 of a syslog server&#x60; | | &#x60;port&#x60; | Syslog server port | &#x60;Valid port number&#x60; | | &#x60;protocol&#x60; | Protocol to connect to syslog server | &#x60;TCP or UDP&#x60; | | &#x60;logIpEnabled&#x60; | Determines whether user’s IP address is logged. | &#x60;true or false&#x60; |  &lt;/details&gt;

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.SystemSettingsConfigApi();
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestSyslogConfig(opts, (error, data, response) => {
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

[**SyslogConfig**](SyslogConfig.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestSystemDefaults

> SystemDefaults requestSystemDefaults(opts)

Request system defaults

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.6.0&lt;/h3&gt;  ### Description:   DRACOON system defaults configuration entry point.    ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: Returns a list of configurable system default values.  ### Further Information: None.  ### Configurable default values &lt;details open style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | Setting | Description | Value | | :--- | :--- | :--- | | &#x60;languageDefault&#x60; | Defines which language should be default. | &#x60;ISO 639-1 code&#x60; | | &#x60;downloadShareDefaultExpirationPeriod&#x60; | Default expiration period for Download Shares in _days_. | &#x60;Integer between 0 and 9999&#x60; | | &#x60;uploadShareDefaultExpirationPeriod&#x60; | Default expiration period for Upload Shares in _days_. | &#x60;Integer between 0 and 9999&#x60; | | &#x60;fileDefaultExpirationPeriod&#x60; | Default expiration period for all uploaded files in _days_. | &#x60;Integer between 0 and 9999&#x60; | | &#x60;nonmemberViewerDefault&#x60; | Defines if new users get the role _Non Member Viewer_ by default | &#x60;true or false&#x60; |  &lt;/details&gt;

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.SystemSettingsConfigApi();
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestSystemDefaults(opts, (error, data, response) => {
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

[**SystemDefaults**](SystemDefaults.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateAuthConfig

> AuthConfig updateAuthConfig(authConfig, opts)

Update authentication settings

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.6.0&lt;/h3&gt;  ### Description:   DRACOON authentication configuration entry point.   Change configurable authentication settings.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: One or more authentication methods gets changed.  ### Further Information: Authentication methods are sorted by priority attribute.   Smaller values have higher priority.   Authentication method with highest priority is considered as default.   Priority **MUST** be a positive value.  ### Configurable authentication settings: &lt;details open style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | Authentication Method | Description | | :--- | :--- | | &#x60;basic&#x60; | **Basic** authentication globally allowed.&lt;br&gt;This option **MUST** be activated to allow users to log in with their credentials stored in the database.&lt;br&gt;Formerly known as &#x60;sql&#x60;. | | &#x60;active_directory&#x60; | **Active Directory** authentication globally allowed.&lt;br&gt;This option **MUST** be activated to allow users to log in with their Active Directory credentials. | | &#x60;radius&#x60; | **RADIUS** authentication globally allowed.&lt;br&gt;This option **MUST** be activated to allow users to log in with their RADIUS username, their PIN and a token password. | | &#x60;openid&#x60; | **OpenID Connect** authentication globally allowed.This option **MUST** be activated to allow users to log in with their OpenID Connect identity. |  &lt;/details&gt;

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.SystemSettingsConfigApi();
let authConfig = new DracoonApi.AuthConfig(); // AuthConfig | 
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.updateAuthConfig(authConfig, opts, (error, data, response) => {
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
 **authConfig** | [**AuthConfig**](AuthConfig.md)|  | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**AuthConfig**](AuthConfig.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateEventlogConfig

> EventlogConfig updateEventlogConfig(updateEventlogConfig, opts)

Update eventlog settings

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.6.0&lt;/h3&gt;  ### Description:   DRACOON eventlog configuration entry point.   Change configurable eventlog settings.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: One or more eventlog settings gets changed.  ### Further Information: None.  ### Configurable eventlog settings: &lt;details open style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | Setting | Description | Value | | :--- | :--- | :--- | | &#x60;enabled&#x60; | Determines whether eventlog is enabled. | &#x60;true or false&#x60; | | &#x60;retentionPeriod&#x60; | Retention period (in _days_) of eventlog entries.&lt;br&gt;After that period, all entries are deleted. | &#x60;Integer between 0 and 9999&#x60;&lt;br&gt;If set to &#x60;0&#x60;: no logs are deleted&lt;br&gt;Recommended value: 7 | | &#x60;logIpEnabled&#x60; | Determines whether user’s IP address is logged. | &#x60;true or false&#x60; |  &lt;/details&gt;

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.SystemSettingsConfigApi();
let updateEventlogConfig = new DracoonApi.UpdateEventlogConfig(); // UpdateEventlogConfig | 
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.updateEventlogConfig(updateEventlogConfig, opts, (error, data, response) => {
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
 **updateEventlogConfig** | [**UpdateEventlogConfig**](UpdateEventlogConfig.md)|  | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**EventlogConfig**](EventlogConfig.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateGeneralSettings

> GeneralSettings updateGeneralSettings(updateGeneralSettings, opts)

Update general settings

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.6.0&lt;/h3&gt;  ### Description:   DRACOON general settings configuration entry point.   Change configurable general settings.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: One or more general settings gets changed.  ### Further Information: Auth token restrictions are enabled by default.      * Default access token validity: **2 hours**   * Default refresh token validity: **30 days**  ### Configurable general settings: &lt;details open style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | Setting | Description | Value | | :--- | :--- | :--- | | &#x60;sharePasswordSmsEnabled&#x60; | Determines whether sending of share passwords via SMS is allowed. | &#x60;true or false&#x60; | | &#x60;cryptoEnabled&#x60; | Determines whether client-side encryption is enabled.&lt;br&gt;Can only be enabled once; disabling is **NOT** possible. | &#x60;true or false&#x60; | | &#x60;emailNotificationButtonEnabled&#x60; | Determines whether email notification button is enabled. | &#x60;true or false&#x60; | | &#x60;eulaEnabled&#x60; | Determines whether EULA is enabled.&lt;br&gt;Each user has to confirm the EULA at first login. | &#x60;true or false&#x60; | | &#x60;s3TagsEnabled&#x60; | Determines whether S3 tags are enabled | &#x60;true or false&#x60; | | &#x60;authTokenRestrictions&#x60; | Determines auth token restrictions. (e.g. restricted access token validity) | &#x60;object&#x60; |  &lt;/details&gt;  ### Deprecated configurable general settings: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | Setting                           | Description | Value | |:----------------------------------| :--- | :--- | | &lt;del&gt;&#x60;mediaServerEnabled&#x60;&lt;/del&gt;   | Determines whether media server is enabled.&lt;br&gt;**CANNOT** be enabled if media server configuration is disabled in &#x60;core-service.properties&#x60;.&lt;br&gt;Check &#x60;mediaServerConfigEnabled&#x60; with &#x60;GET /system/config/settings/infrastructure&#x60;. | &#x60;true or false&#x60; | | &lt;del&gt;&#x60;weakPasswordEnabled&#x60;&lt;/del&gt;  | Determines whether weak password is allowed.&lt;br&gt;Use &#x60;PUT /system/config/policies/passwords&#x60; API to change configured password policies. | &#x60;true or false&#x60; | | &lt;del&gt;&#x60;hideLoginInputFields&#x60;&lt;/del&gt; | Determines whether input fields for login should be enabled | &#x60;true or false&#x60; |  &lt;/details&gt;

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.SystemSettingsConfigApi();
let updateGeneralSettings = new DracoonApi.UpdateGeneralSettings(); // UpdateGeneralSettings | 
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.updateGeneralSettings(updateGeneralSettings, opts, (error, data, response) => {
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
 **updateGeneralSettings** | [**UpdateGeneralSettings**](UpdateGeneralSettings.md)|  | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**GeneralSettings**](GeneralSettings.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateSyslogConfig

> SyslogConfig updateSyslogConfig(updateSyslogConfig, opts)

Update syslog settings

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.6.0&lt;/h3&gt;  ### Description:   DRACOON syslog configuration entry point.   Change configurable syslog settings.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: One or more syslog settings gets changed.  ### Further Information: None.  ### Configurable syslog settings: &lt;details open style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | Setting | Description | Value | | :--- | :--- | :--- | | &#x60;enabled&#x60; | Set &#x60;true&#x60; to enable syslog. | &#x60;true or false&#x60; | | &#x60;host&#x60; | Syslog server (IP or FQDN) | &#x60;DNS name or IPv4 of a syslog server&#x60; | | &#x60;port&#x60; | Syslog server port | &#x60;Valid port number&#x60; | | &#x60;protocol&#x60; | Protocol to connect to syslog server | &#x60;TCP or UDP&#x60; | | &#x60;logIpEnabled&#x60; | Determines whether user’s IP address is logged. | &#x60;true or false&#x60; |  &lt;/details&gt;

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.SystemSettingsConfigApi();
let updateSyslogConfig = new DracoonApi.UpdateSyslogConfig(); // UpdateSyslogConfig | 
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.updateSyslogConfig(updateSyslogConfig, opts, (error, data, response) => {
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
 **updateSyslogConfig** | [**UpdateSyslogConfig**](UpdateSyslogConfig.md)|  | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**SyslogConfig**](SyslogConfig.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateSystemDefaults

> SystemDefaults updateSystemDefaults(updateSystemDefaults, opts)

Update system defaults

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.6.0&lt;/h3&gt;  ### Description:   DRACOON system defaults configuration entry point.   Change configurable system default values.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: One or more system default values gets changed.  ### Further Information: None.  ### Configurable default values &lt;details open style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | Setting | Description | Value | | :--- | :--- | :--- | | &#x60;languageDefault&#x60; | Defines which language should be default. | &#x60;ISO 639-1 code&#x60; | | &#x60;downloadShareDefaultExpirationPeriod&#x60; | Default expiration period for Download Shares in _days_. | &#x60;Integer between 0 and 9999&#x60;&lt;br&gt;Set &#x60;0&#x60; to disable. | | &#x60;uploadShareDefaultExpirationPeriod&#x60; | Default expiration period for Upload Shares in _days_. | &#x60;Integer between 0 and 9999&#x60;&lt;br&gt;Set &#x60;0&#x60; to disable. | | &#x60;fileDefaultExpirationPeriod&#x60; | Default expiration period for all uploaded files in _days_. | &#x60;Integer between 0 and 9999&#x60;&lt;br&gt;Set &#x60;0&#x60; to disable. | | &#x60;nonmemberViewerDefault&#x60; | Defines if new users get the role _Non Member Viewer_ by default | &#x60;true or false&#x60; |  &lt;/details&gt;

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.SystemSettingsConfigApi();
let updateSystemDefaults = new DracoonApi.UpdateSystemDefaults(); // UpdateSystemDefaults | 
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.updateSystemDefaults(updateSystemDefaults, opts, (error, data, response) => {
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
 **updateSystemDefaults** | [**UpdateSystemDefaults**](UpdateSystemDefaults.md)|  | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**SystemDefaults**](SystemDefaults.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

