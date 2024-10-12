# ThreatJammerComUserApi.DataSourcesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAllSourcesV1SourceIpGet**](DataSourcesApi.md#getAllSourcesV1SourceIpGet) | **GET** /v1/source/ip | Get the full information of all the source lists for the subscription level given.
[**getSourceAndTimerangeInfoV1SourceIpSourceRangeTimeRangeGet**](DataSourcesApi.md#getSourceAndTimerangeInfoV1SourceIpSourceRangeTimeRangeGet) | **GET** /v1/source/ip/{source}/range/{time_range} | Get the information of the source list given for a specific time range.
[**getSourceInfoV1SourceIpSourceGet**](DataSourcesApi.md#getSourceInfoV1SourceIpSourceGet) | **GET** /v1/source/ip/{source} | Get the full information of the source list given as argument.



## getAllSourcesV1SourceIpGet

> SourceCollectionOutput getAllSourcesV1SourceIpGet()

Get the full information of all the source lists for the subscription level given.

### What Obtain the full meta information of all the source lists available for the subscription level of the user. A source list is a collection of resources combined together with other sources to create a dataset.   A source list has some unique properties. The most relevant ones are the score and risk. The score is a number **between 0 and 99** describing the probability of the IP address being a malicious one, being **0** means that the IP address is not malicious and is not a threat. Being **99** means that the service behind the IP address is probably malicious an certainly a threat.   Each source list groups several collections of resource by the lapse of time or time range that they are related to according to their age. Each group by time range has a score and a risk.  ### Parameters The endpoint does not accept any parameter. The subscription level is obtained from the token provided in the header.  ### Result The result is a JSON object with a self reference and a list of JSON objects with the following fields: - &#x60;&#x60;self&#x60;&#x60;: the URI to individual source list information. - &#x60;&#x60;dataset&#x60;&#x60;: the URI to the dataset that aggregates the resources of this list. - &#x60;&#x60;name&#x60;&#x60;: the unique name of the source list. Must be uppercase letters, numbers and underscores. - &#x60;&#x60;description&#x60;&#x60;: a human readable long description of the source list. - &#x60;&#x60;source&#x60;&#x60;: Origin of the list. - &#x60;&#x60;url&#x60;&#x60;: The URL where the source list was found. - &#x60;&#x60;refresh&#x60;&#x60;: The refresh period of the source list. - &#x60;&#x60;minimum_score&#x60;&#x60;: The minimum score found in the different source list time ranges. Is in the range 0-99. - &#x60;&#x60;maximum_score&#x60;&#x60;: The maximum score found in the different source list time ranges. Is in the range 0-99. - &#x60;&#x60;minimum_risk&#x60;&#x60;: The minimum human readable risk score found in the different source list time ranges. Can be UNKNOWN, LOW, MEDIUM or HIGH. - &#x60;&#x60;maximum_risk&#x60;&#x60;: The maximum human readable risk score found in the different source list time ranges. Can be UNKNOWN, LOW, MEDIUM or HIGH. - &#x60;&#x60;time_range&#x60;&#x60;: the list of URIs pointing to the different source list time ranges information. - &#x60;&#x60;updated_at&#x60;&#x60;: The UNIX timestamp in milliseconds of last update of the source list. - &#x60;&#x60;subscriptions&#x60;&#x60;: The list of subscription levels that can access this source list.   ### Errors It will return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.DataSourcesApi();
apiInstance.getAllSourcesV1SourceIpGet((error, data, response) => {
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

[**SourceCollectionOutput**](SourceCollectionOutput.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSourceAndTimerangeInfoV1SourceIpSourceRangeTimeRangeGet

> SourceTimeRangeOutput getSourceAndTimerangeInfoV1SourceIpSourceRangeTimeRangeGet(source, timeRange)

Get the information of the source list given for a specific time range.

### What Obtain the meta information of the source list and the time range given as arguments. A source list is a collection of resources combined together with other sources to create a dataset. A source list has some unique properties. The most relevant ones are the score and risk. The score is a number **between 0 and 99** describing the probability of the IP address being a malicious one, being **0** means that the IP address is not malicious and is not a threat. Being **99** means that the service behind the IP address is probably malicious an certainly a threat.   The time ranges or lapse of time of each source are how the resources are stored according to their age. Each group by time range has a score and a risk.  ### Parameters The endpoint accepts the following two parameters in the path: - &#x60;&#x60;source&#x60;&#x60;: (Mandatory) The code name that identifies uniquely the source list in the platform. It must be composed of uppercase letters, numbers and underscores. - &#x60;&#x60;time_range&#x60;&#x60;: (Mandatory) The code name that identifies uniquely the time ranges. Must be: 1H, 6H, 12H, 1D, 7D, 30D, 90D, 180D y 365D.  ### Result The result is a JSON object with the following fields: - &#x60;&#x60;self&#x60;&#x60;: the URI to individual source list and time range information. - &#x60;&#x60;source&#x60;&#x60;: the URI to individual source list information. - &#x60;&#x60;items&#x60;&#x60;: Number of elements in the source list in the time range given. - &#x60;&#x60;lapse&#x60;&#x60;: The lapse of time or time range of the specific source list. Can be 1H, 6H, 12H, 1D, 7D, 30D, 90D, 180D or 365D. - &#x60;&#x60;score&#x60;&#x60;: The score found in the source list time range. Is in the range 0-99. - &#x60;&#x60;risk&#x60;&#x60;: The human readable risk score found in the source list time range. Can be UNKNOWN, LOW, MEDIUM or HIGH. - &#x60;&#x60;updated_at&#x60;&#x60;: The UNIX timestamp in milliseconds of last update of the source list.  ### Errors - a &#x60;404 Not Found&#x60; error if the source list code name was not found. - a &#x60;404 Not Found&#x60; error if the time range was not found. - a &#x60;422 Unprocessable Entity&#x60; error if source list code name or time ranges does not follow the naming convention.  It will return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.DataSourcesApi();
let source = "source_example"; // String | 
let timeRange = "timeRange_example"; // String | 
apiInstance.getSourceAndTimerangeInfoV1SourceIpSourceRangeTimeRangeGet(source, timeRange, (error, data, response) => {
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
 **source** | **String**|  | 
 **timeRange** | **String**|  | 

### Return type

[**SourceTimeRangeOutput**](SourceTimeRangeOutput.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSourceInfoV1SourceIpSourceGet

> V1ModelsSourceSourceOutput getSourceInfoV1SourceIpSourceGet(source)

Get the full information of the source list given as argument.

### What Obtain the full meta information of the source list given as argument. A source list is a collection of resources combined together with other sources to create a dataset. A source list has some unique properties. The most relevant ones are the score and risk. The score is a number **between 0 and 99** describing the probability of the IP address being a malicious one, being **0** means that the IP address is not malicious and is not a threat. Being **99** means that the service behind the IP address is probably malicious an certainly a threat.   Each source list groups several collections of resource by the lapse of time or time range that they are related to according to their age. Each group by time range has a score and a risk.  ### Parameters The endpoint accepts only the following parameter in the path: - &#x60;&#x60;source&#x60;&#x60;: (Mandatory) The code name that identifies uniquely the source list in the platform. It must be composed of uppercase letters, numbers and underscores.  ### Result The result is a JSON object with the following fields: - &#x60;&#x60;self&#x60;&#x60;: the URI to individual source list information. - &#x60;&#x60;dataset&#x60;&#x60;: the URI to the dataset that aggregates the resources of this list. - &#x60;&#x60;name&#x60;&#x60;: the unique name of the source list. Must be uppercase letters, numbers and underscores. - &#x60;&#x60;description&#x60;&#x60;: a human readable long description of the source list. - &#x60;&#x60;source&#x60;&#x60;: Origin of the list. - &#x60;&#x60;url&#x60;&#x60;: The URL where the source list was found. - &#x60;&#x60;refresh&#x60;&#x60;: The refresh period of the source list. - &#x60;&#x60;minimum_score&#x60;&#x60;: The minimum score found in the different source list time ranges. Is in the range 0-99. - &#x60;&#x60;maximum_score&#x60;&#x60;: The maximum score found in the different source list time ranges. Is in the range 0-99. - &#x60;&#x60;minimum_risk&#x60;&#x60;: The minimum human readable risk score found in the different source list time ranges. Can be UNKNOWN, LOW, MEDIUM or HIGH. - &#x60;&#x60;maximum_risk&#x60;&#x60;: The maximum human readable risk score found in the different source list time ranges. Can be UNKNOWN, LOW, MEDIUM or HIGH. - &#x60;&#x60;time_range&#x60;&#x60;: the list of URIs pointing to the different source list time ranges information. - &#x60;&#x60;updated_at&#x60;&#x60;: The UNIX timestamp in milliseconds of last update of the source list. - &#x60;&#x60;subscriptions&#x60;&#x60;: The list of subscription levels that can access this source list.  ### Errors - a &#x60;404 Not Found&#x60; error if the source list code name was not found. - a &#x60;422 Unprocessable Entity&#x60; error if source list code name does not follow the naming convention.  It will return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.DataSourcesApi();
let source = "source_example"; // String | 
apiInstance.getSourceInfoV1SourceIpSourceGet(source, (error, data, response) => {
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
 **source** | **String**|  | 

### Return type

[**V1ModelsSourceSourceOutput**](V1ModelsSourceSourceOutput.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

