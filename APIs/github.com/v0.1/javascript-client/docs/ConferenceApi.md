# EqivoApi.ConferenceApi

All URIs are relative to *https://raw.github.com/rtckit/media/master/eqivo/readme-splash.png*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v01ConferenceDeafPost**](ConferenceApi.md#v01ConferenceDeafPost) | **POST** /v0.1/ConferenceDeaf/ | /v0.1/ConferenceDeaf/
[**v01ConferenceHangupPost**](ConferenceApi.md#v01ConferenceHangupPost) | **POST** /v0.1/ConferenceHangup/ | /v0.1/ConferenceHangup/
[**v01ConferenceKickPost**](ConferenceApi.md#v01ConferenceKickPost) | **POST** /v0.1/ConferenceKick/ | /v0.1/ConferenceKick/
[**v01ConferenceListMembersPost**](ConferenceApi.md#v01ConferenceListMembersPost) | **POST** /v0.1/ConferenceListMembers/ | /v0.1/ConferenceListMembers/
[**v01ConferenceListPost**](ConferenceApi.md#v01ConferenceListPost) | **POST** /v0.1/ConferenceList/ | /v0.1/ConferenceList/
[**v01ConferenceMutePost**](ConferenceApi.md#v01ConferenceMutePost) | **POST** /v0.1/ConferenceMute/ | /v0.1/ConferenceMute/
[**v01ConferencePlayPost**](ConferenceApi.md#v01ConferencePlayPost) | **POST** /v0.1/ConferencePlay/ | /v0.1/ConferencePlay/
[**v01ConferenceRecordStartPost**](ConferenceApi.md#v01ConferenceRecordStartPost) | **POST** /v0.1/ConferenceRecordStart/ | /v0.1/ConferenceRecordStart/
[**v01ConferenceRecordStopPost**](ConferenceApi.md#v01ConferenceRecordStopPost) | **POST** /v0.1/ConferenceRecordStop/ | /v0.1/ConferenceRecordStop/
[**v01ConferenceSpeakPost**](ConferenceApi.md#v01ConferenceSpeakPost) | **POST** /v0.1/ConferenceSpeak/ | /v0.1/ConferenceSpeak/
[**v01ConferenceUndeafPost**](ConferenceApi.md#v01ConferenceUndeafPost) | **POST** /v0.1/ConferenceUndeaf/ | /v0.1/ConferenceUndeaf/
[**v01ConferenceUnmutePost**](ConferenceApi.md#v01ConferenceUnmutePost) | **POST** /v0.1/ConferenceUnmute/ | /v0.1/ConferenceUnmute/



## v01ConferenceDeafPost

> ConferenceDeafResponse v01ConferenceDeafPost(conferenceName, memberID)

/v0.1/ConferenceDeaf/

Blocks audio to one or more conference members

### Example

```javascript
import EqivoApi from 'eqivo_api';
let defaultClient = EqivoApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new EqivoApi.ConferenceApi();
let conferenceName = "conferenceName_example"; // String | Name of the conference in question
let memberID = "memberID_example"; // String | List of comma separated member IDs to be affected; `all` shorthand is available too.
apiInstance.v01ConferenceDeafPost(conferenceName, memberID, (error, data, response) => {
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
 **conferenceName** | **String**| Name of the conference in question | 
 **memberID** | **String**| List of comma separated member IDs to be affected; &#x60;all&#x60; shorthand is available too. | 

### Return type

[**ConferenceDeafResponse**](ConferenceDeafResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## v01ConferenceHangupPost

> ConferenceHangupResponse v01ConferenceHangupPost(conferenceName, memberID)

/v0.1/ConferenceHangup/

Kicks one or more conference members, without playing the kick sound

### Example

```javascript
import EqivoApi from 'eqivo_api';
let defaultClient = EqivoApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new EqivoApi.ConferenceApi();
let conferenceName = "conferenceName_example"; // String | Name of the conference in question
let memberID = "memberID_example"; // String | List of comma separated member IDs to be affected; `all` shorthand is available too.
apiInstance.v01ConferenceHangupPost(conferenceName, memberID, (error, data, response) => {
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
 **conferenceName** | **String**| Name of the conference in question | 
 **memberID** | **String**| List of comma separated member IDs to be affected; &#x60;all&#x60; shorthand is available too. | 

### Return type

[**ConferenceHangupResponse**](ConferenceHangupResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## v01ConferenceKickPost

> ConferenceKickResponse v01ConferenceKickPost(conferenceName, memberID)

/v0.1/ConferenceKick/

Kicks one or more conference members

### Example

```javascript
import EqivoApi from 'eqivo_api';
let defaultClient = EqivoApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new EqivoApi.ConferenceApi();
let conferenceName = "conferenceName_example"; // String | Name of the conference in question
let memberID = "memberID_example"; // String | List of comma separated member IDs to be affected; `all` shorthand is available too.
apiInstance.v01ConferenceKickPost(conferenceName, memberID, (error, data, response) => {
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
 **conferenceName** | **String**| Name of the conference in question | 
 **memberID** | **String**| List of comma separated member IDs to be affected; &#x60;all&#x60; shorthand is available too. | 

### Return type

[**ConferenceKickResponse**](ConferenceKickResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## v01ConferenceListMembersPost

> ConferenceListMembersResponse v01ConferenceListMembersPost(conferenceName, opts)

/v0.1/ConferenceListMembers/

Retrieves the member list for a given conference

### Example

```javascript
import EqivoApi from 'eqivo_api';
let defaultClient = EqivoApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new EqivoApi.ConferenceApi();
let conferenceName = "conferenceName_example"; // String | Name of the conference
let opts = {
  'callUUIDFilter': "callUUIDFilter_example", // String | Restricts listed calls to the provided values (comma separated call UUID list)
  'deafFilter': false, // Boolean | Restricts listed members to deaf ones
  'memberFilter': "memberFilter_example", // String | Restricts listed members to the provided values (comma separated member ID list)
  'mutedFilter': false // Boolean | Restricts listed members to muted ones
};
apiInstance.v01ConferenceListMembersPost(conferenceName, opts, (error, data, response) => {
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
 **conferenceName** | **String**| Name of the conference | 
 **callUUIDFilter** | **String**| Restricts listed calls to the provided values (comma separated call UUID list) | [optional] 
 **deafFilter** | **Boolean**| Restricts listed members to deaf ones | [optional] [default to false]
 **memberFilter** | **String**| Restricts listed members to the provided values (comma separated member ID list) | [optional] 
 **mutedFilter** | **Boolean**| Restricts listed members to muted ones | [optional] [default to false]

### Return type

[**ConferenceListMembersResponse**](ConferenceListMembersResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## v01ConferenceListPost

> ConferenceListResponse v01ConferenceListPost(opts)

/v0.1/ConferenceList/

Returns a list of all established conferences

### Example

```javascript
import EqivoApi from 'eqivo_api';
let defaultClient = EqivoApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new EqivoApi.ConferenceApi();
let opts = {
  'callUUIDFilter': "callUUIDFilter_example", // String | Restricts listed calls to the provided values (comma separated call UUID list)
  'deafFilter': false, // Boolean | Restricts listed members to deaf ones
  'memberFilter': "memberFilter_example", // String | Restricts listed members to the provided values (comma separated member ID list)
  'mutedFilter': false // Boolean | Restricts listed members to muted ones
};
apiInstance.v01ConferenceListPost(opts, (error, data, response) => {
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
 **callUUIDFilter** | **String**| Restricts listed calls to the provided values (comma separated call UUID list) | [optional] 
 **deafFilter** | **Boolean**| Restricts listed members to deaf ones | [optional] [default to false]
 **memberFilter** | **String**| Restricts listed members to the provided values (comma separated member ID list) | [optional] 
 **mutedFilter** | **Boolean**| Restricts listed members to muted ones | [optional] [default to false]

### Return type

[**ConferenceListResponse**](ConferenceListResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## v01ConferenceMutePost

> ConferenceMuteResponse v01ConferenceMutePost(conferenceName, memberID)

/v0.1/ConferenceMute/

Blocks audio from one or more conference members

### Example

```javascript
import EqivoApi from 'eqivo_api';
let defaultClient = EqivoApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new EqivoApi.ConferenceApi();
let conferenceName = "conferenceName_example"; // String | Name of the conference in question
let memberID = "memberID_example"; // String | List of comma separated member IDs to be affected; `all` shorthand is available too.
apiInstance.v01ConferenceMutePost(conferenceName, memberID, (error, data, response) => {
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
 **conferenceName** | **String**| Name of the conference in question | 
 **memberID** | **String**| List of comma separated member IDs to be affected; &#x60;all&#x60; shorthand is available too. | 

### Return type

[**ConferenceMuteResponse**](ConferenceMuteResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## v01ConferencePlayPost

> ConferencePlayResponse v01ConferencePlayPost(conferenceName, filePath, memberID)

/v0.1/ConferencePlay/

Plays media to one or more conference members

### Example

```javascript
import EqivoApi from 'eqivo_api';
let defaultClient = EqivoApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new EqivoApi.ConferenceApi();
let conferenceName = "conferenceName_example"; // String | Name of the conference in question
let filePath = "filePath_example"; // String | Path/URI of the media file to be played
let memberID = "memberID_example"; // String | List of comma separated member IDs to be affected; `all` shorthand is available too.
apiInstance.v01ConferencePlayPost(conferenceName, filePath, memberID, (error, data, response) => {
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
 **conferenceName** | **String**| Name of the conference in question | 
 **filePath** | **String**| Path/URI of the media file to be played | 
 **memberID** | **String**| List of comma separated member IDs to be affected; &#x60;all&#x60; shorthand is available too. | 

### Return type

[**ConferencePlayResponse**](ConferencePlayResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## v01ConferenceRecordStartPost

> ConferenceRecordStartResponse v01ConferenceRecordStartPost(conferenceName, opts)

/v0.1/ConferenceRecordStart/

Initiates a conference recording

### Example

```javascript
import EqivoApi from 'eqivo_api';
let defaultClient = EqivoApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new EqivoApi.ConferenceApi();
let conferenceName = "conferenceName_example"; // String | Name of the conference in question
let opts = {
  'fileFormat': "'mp3'", // String | File format (extension)
  'fileName': "''", // String | Recording file name (without extension); if empty, a timestamp based file name will be generated
  'filePath': "''" // String | Directory path/URI where the recording file will be saved
};
apiInstance.v01ConferenceRecordStartPost(conferenceName, opts, (error, data, response) => {
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
 **conferenceName** | **String**| Name of the conference in question | 
 **fileFormat** | **String**| File format (extension) | [optional] [default to &#39;mp3&#39;]
 **fileName** | **String**| Recording file name (without extension); if empty, a timestamp based file name will be generated | [optional] [default to &#39;&#39;]
 **filePath** | **String**| Directory path/URI where the recording file will be saved | [optional] [default to &#39;&#39;]

### Return type

[**ConferenceRecordStartResponse**](ConferenceRecordStartResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## v01ConferenceRecordStopPost

> ConferenceRecordStopResponse v01ConferenceRecordStopPost(conferenceName, recordFile)

/v0.1/ConferenceRecordStop/

Stops a conference recording

### Example

```javascript
import EqivoApi from 'eqivo_api';
let defaultClient = EqivoApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new EqivoApi.ConferenceApi();
let conferenceName = "conferenceName_example"; // String | Name of the conference in question
let recordFile = "recordFile_example"; // String | Full path to recording file, as returned by ConferenceRecordStart; `all` shorthand is also available
apiInstance.v01ConferenceRecordStopPost(conferenceName, recordFile, (error, data, response) => {
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
 **conferenceName** | **String**| Name of the conference in question | 
 **recordFile** | **String**| Full path to recording file, as returned by ConferenceRecordStart; &#x60;all&#x60; shorthand is also available | 

### Return type

[**ConferenceRecordStopResponse**](ConferenceRecordStopResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## v01ConferenceSpeakPost

> ConferenceSpeakResponse v01ConferenceSpeakPost(conferenceName, memberID, text)

/v0.1/ConferenceSpeak/

Plays synthesized speech into a conference

### Example

```javascript
import EqivoApi from 'eqivo_api';
let defaultClient = EqivoApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new EqivoApi.ConferenceApi();
let conferenceName = "conferenceName_example"; // String | Name of the conference in question
let memberID = "memberID_example"; // String | List of comma separated member IDs to be affected; `all` shorthand is available too.
let text = "text_example"; // String | Text to be synthesized
apiInstance.v01ConferenceSpeakPost(conferenceName, memberID, text, (error, data, response) => {
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
 **conferenceName** | **String**| Name of the conference in question | 
 **memberID** | **String**| List of comma separated member IDs to be affected; &#x60;all&#x60; shorthand is available too. | 
 **text** | **String**| Text to be synthesized | 

### Return type

[**ConferenceSpeakResponse**](ConferenceSpeakResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## v01ConferenceUndeafPost

> ConferenceUndeafResponse v01ConferenceUndeafPost(conferenceName, memberID)

/v0.1/ConferenceUndeaf/

Restores audio to one or more conference members

### Example

```javascript
import EqivoApi from 'eqivo_api';
let defaultClient = EqivoApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new EqivoApi.ConferenceApi();
let conferenceName = "conferenceName_example"; // String | Name of the conference in question
let memberID = "memberID_example"; // String | List of comma separated member IDs to be affected; `all` shorthand is available too.
apiInstance.v01ConferenceUndeafPost(conferenceName, memberID, (error, data, response) => {
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
 **conferenceName** | **String**| Name of the conference in question | 
 **memberID** | **String**| List of comma separated member IDs to be affected; &#x60;all&#x60; shorthand is available too. | 

### Return type

[**ConferenceUndeafResponse**](ConferenceUndeafResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## v01ConferenceUnmutePost

> ConferenceUnmuteResponse v01ConferenceUnmutePost(conferenceName, memberID)

/v0.1/ConferenceUnmute/

Restores audio from one or more conference members

### Example

```javascript
import EqivoApi from 'eqivo_api';
let defaultClient = EqivoApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new EqivoApi.ConferenceApi();
let conferenceName = "conferenceName_example"; // String | Name of the conference in question
let memberID = "memberID_example"; // String | List of comma separated member IDs to be affected; `all` shorthand is available too.
apiInstance.v01ConferenceUnmutePost(conferenceName, memberID, (error, data, response) => {
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
 **conferenceName** | **String**| Name of the conference in question | 
 **memberID** | **String**| List of comma separated member IDs to be affected; &#x60;all&#x60; shorthand is available too. | 

### Return type

[**ConferenceUnmuteResponse**](ConferenceUnmuteResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

