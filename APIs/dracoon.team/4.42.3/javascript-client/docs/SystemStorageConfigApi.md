# DracoonApi.SystemStorageConfigApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createS3Config**](SystemStorageConfigApi.md#createS3Config) | **POST** /v4/system/config/storage/s3 | Create S3 storage configuration
[**createS3Tag**](SystemStorageConfigApi.md#createS3Tag) | **POST** /v4/system/config/storage/s3/tags | Create S3 tag
[**removeS3Tag**](SystemStorageConfigApi.md#removeS3Tag) | **DELETE** /v4/system/config/storage/s3/tags/{id} | Remove S3 tag
[**request3Config**](SystemStorageConfigApi.md#request3Config) | **GET** /v4/system/config/storage/s3 | Request S3 storage configuration
[**requestS3Tag**](SystemStorageConfigApi.md#requestS3Tag) | **GET** /v4/system/config/storage/s3/tags/{id} | Request S3 tag
[**requestS3TagList**](SystemStorageConfigApi.md#requestS3TagList) | **GET** /v4/system/config/storage/s3/tags | Request list of configured S3 tags
[**updateS3Config**](SystemStorageConfigApi.md#updateS3Config) | **PUT** /v4/system/config/storage/s3 | Update S3 storage configuration



## createS3Config

> S3Config createS3Config(s3ConfigCreateRequest, opts)

Create S3 storage configuration

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.3.0&lt;/h3&gt;  ### Description:   Create new S3 configuration.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: New S3 configuration is created.  ### Further Information: Forbidden characters in bucket names: [&#x60;.&#x60;]   &#x60;bucketName&#x60; and &#x60;endpointUrl&#x60; are deprecated, use &#x60;bucketUrl&#x60; instead.  ### Virtual hosted style access  Example: https://&lt;span style&#x3D;\&quot;color:red;\&quot;&gt;bucket-name&lt;/span&gt;.s3.&lt;span style&#x3D;\&quot;color:red;\&quot;&gt;region&lt;/span&gt;.amazonaws.com/&lt;span style&#x3D;\&quot;color:red;\&quot;&gt;key-name&lt;/span&gt; 

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.SystemStorageConfigApi();
let s3ConfigCreateRequest = new DracoonApi.S3ConfigCreateRequest(); // S3ConfigCreateRequest | 
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.createS3Config(s3ConfigCreateRequest, opts, (error, data, response) => {
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
 **s3ConfigCreateRequest** | [**S3ConfigCreateRequest**](S3ConfigCreateRequest.md)|  | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**S3Config**](S3Config.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createS3Tag

> S3Tag createS3Tag(s3TagCreateRequest, opts)

Create S3 tag

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.9.0&lt;/h3&gt;  ### Description:   Create new S3 tag.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: New S3 tag is created.  ### Further Information: * Maximum key length: **128** characters.   * Maximum value length: **256** characters.   * Both S3 tag key and value are **case-sensitive** strings.   * Maximum of **20 mandatory S3 tags** is allowed.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.SystemStorageConfigApi();
let s3TagCreateRequest = new DracoonApi.S3TagCreateRequest(); // S3TagCreateRequest | 
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.createS3Tag(s3TagCreateRequest, opts, (error, data, response) => {
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
 **s3TagCreateRequest** | [**S3TagCreateRequest**](S3TagCreateRequest.md)|  | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**S3Tag**](S3Tag.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## removeS3Tag

> removeS3Tag(id, opts)

Remove S3 tag

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.9.0&lt;/h3&gt;  ### Description:   Delete S3 tag.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: S3 tag gets deleted.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.SystemStorageConfigApi();
let id = 789; // Number | S3 tag ID
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.removeS3Tag(id, opts, (error, data, response) => {
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
 **id** | **Number**| S3 tag ID | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## request3Config

> S3Config request3Config(opts)

Request S3 storage configuration

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.3.0&lt;/h3&gt;  ### Description:   Retrieve S3 configuration.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: S3 configuration is returned.  ### Further Information: None.  ### Virtual hosted style access  Example: https://&lt;span style&#x3D;\&quot;color:red;\&quot;&gt;bucket-name&lt;/span&gt;.s3.&lt;span style&#x3D;\&quot;color:red;\&quot;&gt;region&lt;/span&gt;.amazonaws.com/&lt;span style&#x3D;\&quot;color:red;\&quot;&gt;key-name&lt;/span&gt; 

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.SystemStorageConfigApi();
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.request3Config(opts, (error, data, response) => {
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

[**S3Config**](S3Config.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestS3Tag

> S3Tag requestS3Tag(id, opts)

Request S3 tag

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.9.0&lt;/h3&gt;  ### Description:   Retrieve single S3 tag.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: S3 tag is returned.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.SystemStorageConfigApi();
let id = 789; // Number | S3 tag ID
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestS3Tag(id, opts, (error, data, response) => {
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
 **id** | **Number**| S3 tag ID | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**S3Tag**](S3Tag.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestS3TagList

> S3TagList requestS3TagList(opts)

Request list of configured S3 tags

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.9.0&lt;/h3&gt;  ### Description:   Retrieve all configured S3 tags.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: S3 tags are returned.  ### Further Information: An empty list is returned if no S3 tags are found / configured.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.SystemStorageConfigApi();
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestS3TagList(opts, (error, data, response) => {
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

[**S3TagList**](S3TagList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateS3Config

> S3Config updateS3Config(s3ConfigUpdateRequest, opts)

Update S3 storage configuration

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.3.0&lt;/h3&gt;  ### Description:   Update existing S3 configuration.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: S3 configuration is updated.  ### Further Information: Forbidden characters in bucket names: [&#x60;.&#x60;]   &#x60;bucketName&#x60; and &#x60;endpointUrl&#x60; are deprecated, use &#x60;bucketUrl&#x60; instead.  ### Virtual hosted style access  Example: https://&lt;span style&#x3D;\&quot;color:red;\&quot;&gt;bucket-name&lt;/span&gt;.s3.&lt;span style&#x3D;\&quot;color:red;\&quot;&gt;region&lt;/span&gt;.amazonaws.com/&lt;span style&#x3D;\&quot;color:red;\&quot;&gt;key-name&lt;/span&gt; 

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.SystemStorageConfigApi();
let s3ConfigUpdateRequest = new DracoonApi.S3ConfigUpdateRequest(); // S3ConfigUpdateRequest | 
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.updateS3Config(s3ConfigUpdateRequest, opts, (error, data, response) => {
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
 **s3ConfigUpdateRequest** | [**S3ConfigUpdateRequest**](S3ConfigUpdateRequest.md)|  | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**S3Config**](S3Config.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

