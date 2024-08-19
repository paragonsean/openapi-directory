# ThreatJammerComUserApi.UserAgentApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**parseUserAgentV1UaUserAgentUrlencodedGet**](UserAgentApi.md#parseUserAgentV1UaUserAgentUrlencodedGet) | **GET** /v1/ua/{user_agent_urlencoded} | Get the information found in an User Agent.
[**parseUserAgentsCsvV1UaCsvPost**](UserAgentApi.md#parseUserAgentsCsvV1UaCsvPost) | **POST** /v1/ua/csv | Get the information found in the set of User Agents uploaded.
[**parseUserAgentsV1UaPost**](UserAgentApi.md#parseUserAgentsV1UaPost) | **POST** /v1/ua | Get the information found in a set of User Agents.
[**queryDeviceByCodeV1UaDeviceCodeGet**](UserAgentApi.md#queryDeviceByCodeV1UaDeviceCodeGet) | **GET** /v1/ua/device/{code} | Get the information of the device of a user agent.
[**queryFamilyByCodeV1UaFamilyCodeGet**](UserAgentApi.md#queryFamilyByCodeV1UaFamilyCodeGet) | **GET** /v1/ua/family/{code} | Get the information of the family of a user agent.
[**queryOsByCodeV1UaOsCodeGet**](UserAgentApi.md#queryOsByCodeV1UaOsCodeGet) | **GET** /v1/ua/os/{code} | Get the information of the Operating System of a user agent.
[**queryTypeByCodeV1UaTypeCodeGet**](UserAgentApi.md#queryTypeByCodeV1UaTypeCodeGet) | **GET** /v1/ua/type/{code} | Get the information of the type of a user agent.
[**queryVendorByCodeV1UaVendorCodeGet**](UserAgentApi.md#queryVendorByCodeV1UaVendorCodeGet) | **GET** /v1/ua/vendor/{code} | Get the information of the vendor of a user agent.



## parseUserAgentV1UaUserAgentUrlencodedGet

> UAOutput parseUserAgentV1UaUserAgentUrlencodedGet(userAgentUrlencoded)

Get the information found in an User Agent.

### What Get the information found in the User Agent passed as argument. This information includes: - Type - Render Engine - Version - Vendor - Operating System - Device - How common is the agent worldwide   ### Parameters The only argument accepted in the query string is an URL encoded User Agent string.  ### Result The result contains the following set of data:  The result is a JSON object with the following structure: - &#x60;&#x60;self&#x60;&#x60;: the URI of the API call - &#x60;&#x60;string&#x60;&#x60;:  The full user agent string passed as argument. - &#x60;&#x60;classification&#x60;&#x60;: The classification of the user agent. It can be one of the following: &#x60;&#x60;CRAWLER&#x60;&#x60;, &#x60;&#x60;CLIENT&#x60;&#x60;, &#x60;&#x60;UNKNOWN&#x60;&#x60;. - &#x60;&#x60;type&#x60;&#x60;: An URI to the type of user agent used to identify the client (browser, bot, crawler, etc.). - &#x60;&#x60;agent&#x60;&#x60;: Name of the agent and the version, if any. - &#x60;&#x60;engine&#x60;&#x60;: Agent render engine. - &#x60;&#x60;version&#x60;&#x60;: Version of the agent. - &#x60;&#x60;latest&#x60;&#x60;: Latests known version of the agent. - &#x60;&#x60;family&#x60;&#x60;: URI to the family of the agent. - &#x60;&#x60;vendor&#x60;&#x60;: URI to the vendor or company that produces the agent. - &#x60;&#x60;os&#x60;&#x60;: URI to the operating system used by the agent. - &#x60;&#x60;device&#x60;&#x60;: URI to the device used by the agent. - &#x60;&#x60;frequent&#x60;&#x60;: If the agent is frequently used worlwide or not. The values are &#x60;&#x60;COMMON&#x60;&#x60;, &#x60;&#x60;RARE&#x60;&#x60;, and &#x60;&#x60;UNKNOWN&#x60;&#x60;.   ### Errors The endpoint will return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.UserAgentApi();
let userAgentUrlencoded = "userAgentUrlencoded_example"; // String | 
apiInstance.parseUserAgentV1UaUserAgentUrlencodedGet(userAgentUrlencoded, (error, data, response) => {
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
 **userAgentUrlencoded** | **String**|  | 

### Return type

[**UAOutput**](UAOutput.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## parseUserAgentsCsvV1UaCsvPost

> UACollectionOutput parseUserAgentsCsvV1UaCsvPost(csvFile)

Get the information found in the set of User Agents uploaded.

### What Get the information found in the list of User Agents uploaded as a CSV file. This information includes: - Type - Render Engine - Version - Vendor - Operating System - Device - How common is the agent worldwide  ### Parameters - A text file with a list of User Agents. - A header &#x60;Content-Type: multipart/form-data&#x60; is required.  Example: &#x60;&#x60;&#x60; curl -X &#39;POST&#39; \\   &#39;https://dublin.api.threatjammer.com/v1/ua/csv&#39; \\   -H &#39;accept: application/json&#39; \\   -H &#39;Authorization: Bearer YOUR_API_KEY&#39; \\   -H &#39;Content-Type: multipart/form-data&#39; \\   -F &#39;csv_file&#x3D;@YOUR_TEXT_FILE;type&#x3D;text/csv&#39; &#x60;&#x60;&#x60;  ### Result The result contains a list of the result for each User Agent, with the following data set:  The result is a JSON object with the following structure: - &#x60;&#x60;self&#x60;&#x60;: the URI of the API call - &#x60;&#x60;string&#x60;&#x60;:  The full user agent string passed as argument. - &#x60;&#x60;classification&#x60;&#x60;: The classification of the user agent. It can be one of the following: &#x60;&#x60;CRAWLER&#x60;&#x60;, &#x60;&#x60;CLIENT&#x60;&#x60;, &#x60;&#x60;UNKNOWN&#x60;&#x60;. - &#x60;&#x60;type&#x60;&#x60;: An URI to the type of user agent used to identify the client (browser, bot, crawler, etc.). - &#x60;&#x60;agent&#x60;&#x60;: Name of the agent and the version, if any. - &#x60;&#x60;engine&#x60;&#x60;: Agent render engine. - &#x60;&#x60;version&#x60;&#x60;: Version of the agent. - &#x60;&#x60;latest&#x60;&#x60;: Latests known version of the agent. - &#x60;&#x60;family&#x60;&#x60;: URI to the family of the agent. - &#x60;&#x60;vendor&#x60;&#x60;: URI to the vendor or company that produces the agent. - &#x60;&#x60;os&#x60;&#x60;: URI to the operating system used by the agent. - &#x60;&#x60;device&#x60;&#x60;: URI to the device used by the agent. - &#x60;&#x60;frequent&#x60;&#x60;: If the agent is frequently used worlwide or not. The values are &#x60;&#x60;COMMON&#x60;&#x60;, &#x60;&#x60;RARE&#x60;&#x60;, and &#x60;&#x60;UNKNOWN&#x60;&#x60;.   ### Errors The endpoint will return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.UserAgentApi();
let csvFile = "/path/to/file"; // File | The CSV file with the User Agents to parse
apiInstance.parseUserAgentsCsvV1UaCsvPost(csvFile, (error, data, response) => {
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
 **csvFile** | **File**| The CSV file with the User Agents to parse | 

### Return type

[**UACollectionOutput**](UACollectionOutput.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## parseUserAgentsV1UaPost

> UACollectionOutput parseUserAgentsV1UaPost(requestBody)

Get the information found in a set of User Agents.

### What Get the information found in the list of User Agents passed as argument. This information includes: - Type - Render Engine - Version - Vendor - Operating System - Device - How common is the agent worldwide  ### Parameters A list of User Agents are required in the body of the request.  ### Result The result contains a list of the result for each User Agent, with the following data set:  The result is a JSON object with the following structure: - &#x60;&#x60;self&#x60;&#x60;: the URI of the API call - &#x60;&#x60;string&#x60;&#x60;:  The full user agent string passed as argument. - &#x60;&#x60;classification&#x60;&#x60;: The classification of the user agent. It can be one of the following: &#x60;&#x60;CRAWLER&#x60;&#x60;, &#x60;&#x60;CLIENT&#x60;&#x60;, &#x60;&#x60;UNKNOWN&#x60;&#x60;. - &#x60;&#x60;type&#x60;&#x60;: An URI to the type of user agent used to identify the client (browser, bot, crawler, etc.). - &#x60;&#x60;agent&#x60;&#x60;: Name of the agent and the version, if any. - &#x60;&#x60;engine&#x60;&#x60;: Agent render engine. - &#x60;&#x60;version&#x60;&#x60;: Version of the agent. - &#x60;&#x60;latest&#x60;&#x60;: Latests known version of the agent. - &#x60;&#x60;family&#x60;&#x60;: URI to the family of the agent. - &#x60;&#x60;vendor&#x60;&#x60;: URI to the vendor or company that produces the agent. - &#x60;&#x60;os&#x60;&#x60;: URI to the operating system used by the agent. - &#x60;&#x60;device&#x60;&#x60;: URI to the device used by the agent. - &#x60;&#x60;frequent&#x60;&#x60;: If the agent is frequently used worlwide or not. The values are &#x60;&#x60;COMMON&#x60;&#x60;, &#x60;&#x60;RARE&#x60;&#x60;, and &#x60;&#x60;UNKNOWN&#x60;&#x60;.   ### Errors The endpoint will return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.UserAgentApi();
let requestBody = ["null"]; // [String] | 
apiInstance.parseUserAgentsV1UaPost(requestBody, (error, data, response) => {
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
 **requestBody** | [**[String]**](String.md)|  | 

### Return type

[**UACollectionOutput**](UACollectionOutput.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## queryDeviceByCodeV1UaDeviceCodeGet

> DeviceOutput queryDeviceByCodeV1UaDeviceCodeGet(code)

Get the information of the device of a user agent.

### What Obtain the details of a device of a User Agent.  ### Parameters The endpoint accepts only the following parameter in the path: - &#x60;&#x60;code&#x60;&#x60;: (Mandatory) The code that identifies uniquely the device origin of a User Agent. The value must be an alphanumeric upper case string.   ### Result The result is a JSON object with the following structure: - &#x60;&#x60;self&#x60;&#x60;: the URI to the device. - &#x60;&#x60;description&#x60;&#x60;: the human readable description of the device. - &#x60;&#x60;code&#x60;&#x60;: the internal code of the device in the system.  ### Errors - a &#x60;422 Unprocessable Entity&#x60; error if the code is not one of the available.  It will also return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.UserAgentApi();
let code = "code_example"; // String | 
apiInstance.queryDeviceByCodeV1UaDeviceCodeGet(code, (error, data, response) => {
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
 **code** | **String**|  | 

### Return type

[**DeviceOutput**](DeviceOutput.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryFamilyByCodeV1UaFamilyCodeGet

> FamilyOutput queryFamilyByCodeV1UaFamilyCodeGet(code)

Get the information of the family of a user agent.

### What Obtain the details of a family of a User Agent.  ### Parameters The endpoint accepts only the following parameter in the path: - &#x60;&#x60;code&#x60;&#x60;: (Mandatory) The code that identifies uniquely the family of a User Agent. The value must be an alphanumeric upper case string.   ### Result The result is a JSON object with the following structure: - &#x60;&#x60;self&#x60;&#x60;: the URI to the family. - &#x60;&#x60;description&#x60;&#x60;: the human readable description of the famly. - &#x60;&#x60;code&#x60;&#x60;: the internal code of the family in the system.  ### Errors - a &#x60;422 Unprocessable Entity&#x60; error if the code is not one of the available.  It will also return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.UserAgentApi();
let code = "code_example"; // String | 
apiInstance.queryFamilyByCodeV1UaFamilyCodeGet(code, (error, data, response) => {
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
 **code** | **String**|  | 

### Return type

[**FamilyOutput**](FamilyOutput.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryOsByCodeV1UaOsCodeGet

> OSOutput queryOsByCodeV1UaOsCodeGet(code)

Get the information of the Operating System of a user agent.

### What Obtain the details of the Operating System of a User Agent.  ### Parameters The endpoint accepts only the following parameter in the path: - &#x60;&#x60;code&#x60;&#x60;: (Mandatory) The code that identifies uniquely the Operating System at the origin of a User Agent. The value must be an alphanumeric upper case string.   ### Result The result is a JSON object with the following structure: - &#x60;&#x60;self&#x60;&#x60;: the URI to the OS. - &#x60;&#x60;description&#x60;&#x60;: the human readable description of the OS. - &#x60;&#x60;code&#x60;&#x60;: the internal code of the OS in the system. - &#x60;&#x60;family&#x60;&#x60;: the family of the OS. - &#x60;&#x60;vendor&#x60;&#x60;: the vendor or manufacturer of the OS.  ### Errors - a &#x60;422 Unprocessable Entity&#x60; error if the code is not one of the available.  It will also return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.UserAgentApi();
let code = "code_example"; // String | 
apiInstance.queryOsByCodeV1UaOsCodeGet(code, (error, data, response) => {
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
 **code** | **String**|  | 

### Return type

[**OSOutput**](OSOutput.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryTypeByCodeV1UaTypeCodeGet

> TypeOutput queryTypeByCodeV1UaTypeCodeGet(code)

Get the information of the type of a user agent.

### What Obtain the details of a type of a User Agent.  ### Parameters The endpoint accepts only the following parameter in the path: - &#x60;&#x60;code&#x60;&#x60;: (Mandatory) The code that identifies uniquely the type of a User Agent. The value must be an alphanumeric upper case string.   ### Result The result is a JSON object with the following structure: - &#x60;&#x60;self&#x60;&#x60;: the URI to the type. - &#x60;&#x60;description&#x60;&#x60;: the human readable description of the type. - &#x60;&#x60;code&#x60;&#x60;: the internal code of the type in the system. - &#x60;&#x60;type&#x60;&#x60;: the type of the User Agent. Can be &#x60;&#x60;INTERACTIVE&#x60;&#x60;, &#x60;&#x60;CRAWLER&#x60;&#x60; or &#x60;&#x60;UNKNOWN&#x60;&#x60; if the type is not known.  ### Errors - a &#x60;422 Unprocessable Entity&#x60; error if the code is not one of the available.  It will also return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.UserAgentApi();
let code = "code_example"; // String | 
apiInstance.queryTypeByCodeV1UaTypeCodeGet(code, (error, data, response) => {
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
 **code** | **String**|  | 

### Return type

[**TypeOutput**](TypeOutput.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryVendorByCodeV1UaVendorCodeGet

> VendorOutput queryVendorByCodeV1UaVendorCodeGet(code)

Get the information of the vendor of a user agent.

### What Obtain the details of a vendor of a User Agent.  ### Parameters The endpoint accepts only the following parameter in the path: - &#x60;&#x60;code&#x60;&#x60;: (Mandatory) The code that identifies uniquely the vendor or manufacurer of a User Agent. The value must be an alphanumeric upper case string.   ### Result The result is a JSON object with the following structure: - &#x60;&#x60;self&#x60;&#x60;: the URI to the vendor. - &#x60;&#x60;description&#x60;&#x60;: the human readable description of the vendor. - &#x60;&#x60;code&#x60;&#x60;: the internal code of the vendor in the system.  ### Errors - a &#x60;422 Unprocessable Entity&#x60; error if the code is not one of the available.  It will also return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.UserAgentApi();
let code = "code_example"; // String | 
apiInstance.queryVendorByCodeV1UaVendorCodeGet(code, (error, data, response) => {
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
 **code** | **String**|  | 

### Return type

[**VendorOutput**](VendorOutput.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

