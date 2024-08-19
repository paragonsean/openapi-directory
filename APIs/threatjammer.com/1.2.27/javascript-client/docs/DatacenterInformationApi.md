# ThreatJammerComUserApi.DatacenterInformationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**queryDatacenterPrefixInformationV1DatacenterPrefixPost**](DatacenterInformationApi.md#queryDatacenterPrefixInformationV1DatacenterPrefixPost) | **POST** /v1/datacenter/prefix | Get the IPv4 or IPv6 prefix of the CIDR given.
[**queryDatacenterPrefixesListV1DatacenterDatacenterIdPrefixesGet**](DatacenterInformationApi.md#queryDatacenterPrefixesListV1DatacenterDatacenterIdPrefixesGet) | **GET** /v1/datacenter/{datacenter_id}/prefixes | Get the list of IPv4 and IPv6 prefixes of the Datacenter given.
[**queryDatacenterV1DatacenterDatacenterIdGet**](DatacenterInformationApi.md#queryDatacenterV1DatacenterDatacenterIdGet) | **GET** /v1/datacenter/{datacenter_id} | Get the Datacenter details of datacente given.
[**queryIPAddressNetworkInformationV1DatacenterIpIpAddressGet**](DatacenterInformationApi.md#queryIPAddressNetworkInformationV1DatacenterIpIpAddressGet) | **GET** /v1/datacenter/ip/{ip_address} | Get the IPv4 or IPv6 prefix of the IP address given.



## queryDatacenterPrefixInformationV1DatacenterPrefixPost

> DatacenterPrefixOutput queryDatacenterPrefixInformationV1DatacenterPrefixPost(bodyQueryDatacenterPrefixInformationV1DatacenterPrefixPost)

Get the IPv4 or IPv6 prefix of the CIDR given.

### What Obtain the IPv4 or IPv6 prefix and the Datacenter information of the CIDR passed in the body as a POST method. This endpoint works around the problem of passing &#39;/&#39; addresses in the URI.  ### Parameters The endpoint accepts only the following parameter in the body as a JSON object: - &#x60;&#x60;prefix&#x60;&#x60;: (Mandatory) The CIDR v4 or v6 to be queried.  ### Result - The result is a JSON object with the following structure:     - &#x60;&#x60;self&#x60;&#x60;: the URI to individual IPv4 prefix.     - &#x60;&#x60;datacenter_id&#x60;&#x60;: the URI to query the full details of the Datacenter.     - &#x60;&#x60;score&#x60;&#x60;: The risk score of the prefix. It ranges from 0 to 99.     - &#x60;&#x60;risk&#x60;&#x60;: The risk of the prefix. The allowed values are: LOW, MEDIUM, HIGH. It&#39;s a human readable representation of the score.     - &#x60;&#x60;min_score&#x60;&#x60;: The minimum risk score of the prefix. It ranges from 0 to 99.     - &#x60;&#x60;max_score&#x60;&#x60;: The maximum risk score of the prefix. It ranges from 0 to 99.     - &#x60;&#x60;ip_abuse_total&#x60;&#x60;: The total number of IPs that have been reported as abuse in the range.   ### Errors The endpoint will return the following errors: - a &#x60;404 Not Found&#x60; error if the prefix information was not found. - a &#x60;422 Unprocessable Entity&#x60; error if the CIDR is malformed.  It will also return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.DatacenterInformationApi();
let bodyQueryDatacenterPrefixInformationV1DatacenterPrefixPost = new ThreatJammerComUserApi.BodyQueryDatacenterPrefixInformationV1DatacenterPrefixPost(); // BodyQueryDatacenterPrefixInformationV1DatacenterPrefixPost | 
apiInstance.queryDatacenterPrefixInformationV1DatacenterPrefixPost(bodyQueryDatacenterPrefixInformationV1DatacenterPrefixPost, (error, data, response) => {
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
 **bodyQueryDatacenterPrefixInformationV1DatacenterPrefixPost** | [**BodyQueryDatacenterPrefixInformationV1DatacenterPrefixPost**](BodyQueryDatacenterPrefixInformationV1DatacenterPrefixPost.md)|  | 

### Return type

[**DatacenterPrefixOutput**](DatacenterPrefixOutput.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## queryDatacenterPrefixesListV1DatacenterDatacenterIdPrefixesGet

> DatacenterPrefixesOutput queryDatacenterPrefixesListV1DatacenterDatacenterIdPrefixesGet(datacenterId)

Get the list of IPv4 and IPv6 prefixes of the Datacenter given.

### What Obtain the full list of IPv4 and IPv6 prefixes of the Datacenter passed as a parameter.  ### Parameters The endpoint accepts only the following parameter in the path: - &#x60;&#x60;datacenter_id&#x60;&#x60;: (Mandatory) The internal Datacenter ID to be queried.  ### Result The result is a JSON object with the following structure: - &#x60;&#x60;self&#x60;&#x60;: the URI of the API call - &#x60;&#x60;datacenter_id&#x60;&#x60;: the URI to query the full details of the Datacenter. - &#x60;&#x60;prefixes_v4&#x60;&#x60;: the list of IPv4 prefixes that belong to the Datacenter. Each element of the list is a JSON object with the following structure:      - &#x60;&#x60;self&#x60;&#x60;: the URI to individual IPv4 prefix.     - &#x60;&#x60;datacenter_id&#x60;&#x60;: the URI to query the full details of the Datacenter.     - &#x60;&#x60;score&#x60;&#x60;: The risk score of the prefix. It ranges from 0 to 99.     - &#x60;&#x60;risk&#x60;&#x60;: The risk of the prefix. The allowed values are: LOW, MEDIUM, HIGH. It&#39;s a human readable representation of the score.     - &#x60;&#x60;min_score&#x60;&#x60;: The minimum risk score of the prefix. It ranges from 0 to 99.     - &#x60;&#x60;max_score&#x60;&#x60;: The maximum risk score of the prefix. It ranges from 0 to 99.     - &#x60;&#x60;ip_abuse_total&#x60;&#x60;: The total number of IPs that have been reported as abuse in the range.  - &#x60;&#x60;prefixes_v6&#x60;&#x60;: the list of IPv6 prefixes that belong to the Datacenter. Each element of the list is a JSON object with the following structure:      - &#x60;&#x60;self&#x60;&#x60;: the URI to individual IPv4 prefix.     - &#x60;&#x60;datacenter_id&#x60;&#x60;: the URI to query the full details of the Datacenter.     - &#x60;&#x60;score&#x60;&#x60;: The risk score of the prefix. It ranges from 0 to 99.     - &#x60;&#x60;risk&#x60;&#x60;: The risk of the prefix. The allowed values are: LOW, MEDIUM, HIGH. It&#39;s a human readable representation of the score.     - &#x60;&#x60;min_score&#x60;&#x60;: The minimum risk score of the prefix. It ranges from 0 to 99.     - &#x60;&#x60;max_score&#x60;&#x60;: The maximum risk score of the prefix. It ranges from 0 to 99.     - &#x60;&#x60;ip_abuse_total&#x60;&#x60;: The total number of IPs that have been reported as abuse in the range.   ### Errors The endpoint will return the following errors: - a &#x60;404 Not Found&#x60; error if the Datacenter was not found. - a &#x60;422 Unprocessable Entity&#x60; error if the Datacenter number is malformed.  It will also return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.DatacenterInformationApi();
let datacenterId = "datacenterId_example"; // String | 
apiInstance.queryDatacenterPrefixesListV1DatacenterDatacenterIdPrefixesGet(datacenterId, (error, data, response) => {
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
 **datacenterId** | **String**|  | 

### Return type

[**DatacenterPrefixesOutput**](DatacenterPrefixesOutput.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryDatacenterV1DatacenterDatacenterIdGet

> DatacenterOutput queryDatacenterV1DatacenterDatacenterIdGet(datacenterId)

Get the Datacenter details of datacente given.

### What Obtain the details of the Datacenter ID passed as a parameter.  ### Parameters The endpoint accepts only the following parameter in the path: - &#x60;&#x60;datacenter_id&#x60;&#x60;: (Mandatory) The internal Datacenter ID to be queried.  ### Result The result is a JSON object with the following structure: - &#x60;&#x60;self&#x60;&#x60;: the URI of the API call - &#x60;&#x60;name&#x60;&#x60;: the generic name of the Datacenter. The database takes the name from different sources, so it may be different from the real name. - &#x60;&#x60;description&#x60;&#x60;: a full name of the Datacenter. It contains more details about the Datacenter. - &#x60;&#x60;source&#x60;&#x60;: website of the company that owns the Datacenter. - &#x60;&#x60;asn&#x60;&#x60;: the URI to the ASN of the Datacenter. - &#x60;&#x60;status&#x60;&#x60;: the status of the Datacenter. It can be: &#x60;enabled&#x60; or &#x60;disabled&#x60;. - &#x60;&#x60;prefixes&#x60;&#x60;: the URI to the list of prefixes that belong to the Datacenter. - &#x60;&#x60;score&#x60;&#x60;: The risk score of the Datacenter. It ranges from 0 to 99. - &#x60;&#x60;risk&#x60;&#x60;: The risk of the Datacenter. The allowed values are: LOW, MEDIUM, HIGH. It&#39;s a human readable representation of the score.   ### Errors The endpoint will return the following errors: - a &#x60;404 Not Found&#x60; error if the Datacenter was not found. - a &#x60;422 Unprocessable Entity&#x60; error if the Datacenter is malformed.  It will also return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.DatacenterInformationApi();
let datacenterId = "datacenterId_example"; // String | 
apiInstance.queryDatacenterV1DatacenterDatacenterIdGet(datacenterId, (error, data, response) => {
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
 **datacenterId** | **String**|  | 

### Return type

[**DatacenterOutput**](DatacenterOutput.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryIPAddressNetworkInformationV1DatacenterIpIpAddressGet

> DatacenterPrefixOutput queryIPAddressNetworkInformationV1DatacenterIpIpAddressGet(ipAddress)

Get the IPv4 or IPv6 prefix of the IP address given.

### What Obtain the IPv4 or IPv6 prefix and the Datacenter information of the IP address passed as a parameter.  ### Parameters The endpoint accepts only the following parameter in the path: - &#x60;&#x60;ip_address&#x60;&#x60;: (Mandatory) The IPv4 or IPv6 address to be queried.  ### Result - The result is a JSON object with the following structure:     - &#x60;&#x60;self&#x60;&#x60;: the URI to individual IPv4 prefix.     - &#x60;&#x60;datacenter_id&#x60;&#x60;: the URI to query the full details of the Datacenter.     - &#x60;&#x60;score&#x60;&#x60;: The risk score of the prefix. It ranges from 0 to 99.     - &#x60;&#x60;risk&#x60;&#x60;: The risk of the prefix. The allowed values are: LOW, MEDIUM, HIGH. It&#39;s a human readable representation of the score.     - &#x60;&#x60;min_score&#x60;&#x60;: The minimum risk score of the prefix. It ranges from 0 to 99.     - &#x60;&#x60;max_score&#x60;&#x60;: The maximum risk score of the prefix. It ranges from 0 to 99.     - &#x60;&#x60;ip_abuse_total&#x60;&#x60;: The total number of IPs that have been reported as abuse in the range.   ### Errors The endpoint will return the following errors: - a &#x60;404 Not Found&#x60; error if the prefix information was not found. - a &#x60;422 Unprocessable Entity&#x60; error if the IP address is malformed.  It will also return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.DatacenterInformationApi();
let ipAddress = "ipAddress_example"; // String | 
apiInstance.queryIPAddressNetworkInformationV1DatacenterIpIpAddressGet(ipAddress, (error, data, response) => {
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
 **ipAddress** | **String**|  | 

### Return type

[**DatacenterPrefixOutput**](DatacenterPrefixOutput.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

