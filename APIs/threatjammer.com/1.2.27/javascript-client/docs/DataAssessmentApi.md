# ThreatJammerComUserApi.DataAssessmentApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assessIpSetCsvV1AssessIpCsvPost**](DataAssessmentApi.md#assessIpSetCsvV1AssessIpCsvPost) | **POST** /v1/assess/ip/csv | Get the risk score of all IP address uploaded and other data signals.
[**assessIpSetV1AssessIpPost**](DataAssessmentApi.md#assessIpSetV1AssessIpPost) | **POST** /v1/assess/ip | Get the risk score of all IP address passed in the body and other data signals.
[**assessIpV1AssessIpIpAddressGet**](DataAssessmentApi.md#assessIpV1AssessIpIpAddressGet) | **GET** /v1/assess/ip/{ip_address} | Get a risk score of the IP address and different data signals.



## assessIpSetCsvV1AssessIpCsvPost

> IPAssessmentCollectionOutput assessIpSetCsvV1AssessIpCsvPost(csvFile, opts)

Get the risk score of all IP address uploaded and other data signals.

### What Obtain a numerical score and a risk assessment of all the IP addresses uploaded with a text file.  ### Parameters - A text file with a list of public IPv4 or IPv6 addresses. - A header &#x60;Content-Type: multipart/form-data&#x60; is required. - (optional) in the query string the parameeter &#x60;strict_parse&#x60;: If set to &#x60;true&#x60;, no malformed IP addresses allowed, returning an error. If set to &#x60;false&#x60;, malformed IP addresses will be ignored.  Example: &#x60;&#x60;&#x60; curl -X &#39;POST&#39; \\   &#39;https://dublin.api.threatjammer.com/v1/asses/ip/csv[?strict_parse&#x3D;true|false]&#39; \\   -H &#39;accept: application/json&#39; \\   -H &#39;Authorization: Bearer YOUR_API_KEY&#39; \\   -H &#39;Content-Type: multipart/form-data&#39; \\   -F &#39;csv_file&#x3D;@YOUR_TEXT_FILE;type&#x3D;text/csv&#39; &#x60;&#x60;&#x60;  ### Result The result contains a list of the result for each IP address, with two main sets of data: - The score is a number **between 0 and 99** describing the probability of the IP address being a malicious one, being **0** means that the IP address is not malicious and is not a threat. Being **99** means that the service behind the IP address is probably malicious an certainly a threat.  - The list of information gathered from the IP address to obtain the score.  The result is a JSON object with the following structure: - &#x60;&#x60;self&#x60;&#x60;: the URI of the API call - &#x60;&#x60;score&#x60;&#x60;: The score of the IP address. It ranges from 0 to 99. - &#x60;&#x60;risk&#x60;&#x60;: The risk of the IP address. The allowed values are: LOW, MEDIUM, HIGH. It&#39;s a human readable representation of the score. - &#x60;&#x60;reason&#x60;&#x60;: It&#39;s a human readable representation of the reason of the risk. - &#x60;&#x60;datasets&#x60;&#x60;: The IP address was found in the these lists of datasets used to obtain the risk score. Datasets are described as a list of URIs. - &#x60;&#x60;sources&#x60;&#x60;: The IP address was found in the these source lists at an specific time with a specific risk score. Sources are described as a list of URIs. - &#x60;&#x60;log&#x60;&#x60;: The activity of the IP address in the different datasets used to obtain the risk score. The log is a URI reference. - &#x60;&#x60;asn&#x60;&#x60;: The information about the Autonomous System (AS) of the IP address. The AS is described as an URI. - &#x60;&#x60;asn_prefix&#x60;&#x60;: The information about the Autonomous System (AS) network prefix of the IP address. The prefix is described as an URI. - &#x60;&#x60;datacenter&#x60;&#x60;: If the IP address is part of a datacenter pool, the information about the datacenter is described as an URI. - &#x60;&#x60;datacenter_prefix&#x60;&#x60;: The information about the Datacenter network prefix of the IP address. The &#x60;asn_prefix&#x60; and &#x60;datacenter_prefix&#x60; can be the same, but it is not mandatory. The prefix is described as an URI. - &#x60;&#x60;denylisted&#x60;&#x60;: If the IP address was denylisted by the user, the information about the denylisted IP address is described as an URI. - &#x60;&#x60;first_appearence&#x60;&#x60;: URI to the first appearance of the IP address in the different datasets used to obtain the risk score. - &#x60;&#x60;last_appearence&#x60;&#x60;: URI to the last appearance of the IP address in the different datasets used to obtain the risk score.  ### Errors The endpoint will return the following errors: - a &#x60;422 Unprocessable Entity&#x60; error if the IP address is malformed.  The private IP addresses will be ignored, if any.  When the &#x60;strict_parse&#x60; parameter is set to &#x60;true&#x60;, the endpoint will return the following errors: - a &#x60;400 Bad Request&#x60;.  It will also return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.DataAssessmentApi();
let csvFile = "/path/to/file"; // File | The CSV file with the IP addresses
let opts = {
  'strictParse': false // Boolean | When `true`, if any IP address entry in the file is malformed, the assessment is canceled. If `false`, the malformed IP addresses are ignored. Default is `false`.
};
apiInstance.assessIpSetCsvV1AssessIpCsvPost(csvFile, opts, (error, data, response) => {
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
 **csvFile** | **File**| The CSV file with the IP addresses | 
 **strictParse** | **Boolean**| When &#x60;true&#x60;, if any IP address entry in the file is malformed, the assessment is canceled. If &#x60;false&#x60;, the malformed IP addresses are ignored. Default is &#x60;false&#x60;. | [optional] [default to false]

### Return type

[**IPAssessmentCollectionOutput**](IPAssessmentCollectionOutput.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## assessIpSetV1AssessIpPost

> IPAssessmentCollectionOutput assessIpSetV1AssessIpPost(requestBody)

Get the risk score of all IP address passed in the body and other data signals.

### What Obtain a numerical score and a risk assessment of all the IP addresses passed as argument.  ### Parameters A list of public IPv4 or IPv6 addresses is required in the body of the request.  ### Result The result contains a list of the result for each IP address, with two main sets of data: - The score is a number **between 0 and 99** describing the probability of the IP address being a malicious one, being **0** means that the IP address is not malicious and is not a threat. Being **99** means that the service behind the IP address is probably malicious an certainly a threat.  - The list of information gathered from the IP address to obtain the score.  The result is a JSON object with the following structure: - &#x60;&#x60;self&#x60;&#x60;: the URI of the API call - &#x60;&#x60;score&#x60;&#x60;: The score of the IP address. It ranges from 0 to 99. - &#x60;&#x60;risk&#x60;&#x60;: The risk of the IP address. The allowed values are: LOW, MEDIUM, HIGH. It&#39;s a human readable representation of the score. - &#x60;&#x60;reason&#x60;&#x60;: It&#39;s a human readable representation of the reason of the risk. - &#x60;&#x60;datasets&#x60;&#x60;: The IP address was found in the these lists of datasets used to obtain the risk score. Datasets are described as a list of URIs. - &#x60;&#x60;sources&#x60;&#x60;: The IP address was found in the these source lists at an specific time with a specific risk score. Sources are described as a list of URIs. - &#x60;&#x60;log&#x60;&#x60;: The activity of the IP address in the different datasets used to obtain the risk score. The log is a URI reference. - &#x60;&#x60;asn&#x60;&#x60;: The information about the Autonomous System (AS) of the IP address. The AS is described as an URI. - &#x60;&#x60;asn_prefix&#x60;&#x60;: The information about the Autonomous System (AS) network prefix of the IP address. The prefix is described as an URI. - &#x60;&#x60;datacenter&#x60;&#x60;: If the IP address is part of a datacenter pool, the information about the datacenter is described as an URI. - &#x60;&#x60;datacenter_prefix&#x60;&#x60;: The information about the Datacenter network prefix of the IP address. The &#x60;asn_prefix&#x60; and &#x60;datacenter_prefix&#x60; can be the same, but it is not mandatory. The prefix is described as an URI. - &#x60;&#x60;denylisted&#x60;&#x60;: If the IP address was denylisted by the user, the information about the denylisted IP address is described as an URI. - &#x60;&#x60;first_appearence&#x60;&#x60;: URI to the first appearance of the IP address in the different datasets used to obtain the risk score. - &#x60;&#x60;last_appearence&#x60;&#x60;: URI to the last appearance of the IP address in the different datasets used to obtain the risk score.  ### Errors The endpoint will return the following errors: - a &#x60;422 Unprocessable Entity&#x60; error if the IP address is malformed.  The private IP addresses will be ignored, if any.  It will also return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.DataAssessmentApi();
let requestBody = ["null"]; // [String] | 
apiInstance.assessIpSetV1AssessIpPost(requestBody, (error, data, response) => {
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

[**IPAssessmentCollectionOutput**](IPAssessmentCollectionOutput.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## assessIpV1AssessIpIpAddressGet

> IPAssessmentOutput assessIpV1AssessIpIpAddressGet(ipAddress)

Get a risk score of the IP address and different data signals.

### What Obtain a numerical score and a risk assessment of the IP address passed as argument.  ### Parameters The only argument accepted in the query string is a public IPv4 or IPv6 addresses.  ### Result The result contains two main sets of data: - The score is a number **between 0 and 99** describing the probability of the IP address being a malicious one, being **0** means that the IP address is not malicious and is not a threat. Being **99** means that the service behind the IP address is probably malicious an certainly a threat.  - The list of information gathered from the IP address to obtain the score.  The result is a JSON object with the following structure: - &#x60;&#x60;self&#x60;&#x60;: the URI of the API call - &#x60;&#x60;score&#x60;&#x60;: The score of the IP address. It ranges from 0 to 99. - &#x60;&#x60;risk&#x60;&#x60;: The risk of the IP address. The allowed values are: LOW, MEDIUM, HIGH. It&#39;s a human readable representation of the score. - &#x60;&#x60;reason&#x60;&#x60;: It&#39;s a human readable representation of the reason of the risk. - &#x60;&#x60;datasets&#x60;&#x60;: The IP address was found in the these lists of datasets used to obtain the risk score. Datasets are described as a list of URIs. - &#x60;&#x60;sources&#x60;&#x60;: The IP address was found in the these source lists at an specific time with a specific risk score. Sources are described as a list of URIs. - &#x60;&#x60;log&#x60;&#x60;: The activity of the IP address in the different datasets used to obtain the risk score. The log is a URI reference. - &#x60;&#x60;asn&#x60;&#x60;: The information about the Autonomous System (AS) of the IP address. The AS is described as an URI. - &#x60;&#x60;asn_prefix&#x60;&#x60;: The information about the Autonomous System (AS) network prefix of the IP address. The prefix is described as an URI. - &#x60;&#x60;datacenter&#x60;&#x60;: If the IP address is part of a datacenter pool, the information about the datacenter is described as an URI. - &#x60;&#x60;datacenter_prefix&#x60;&#x60;: The information about the Datacenter network prefix of the IP address. The &#x60;asn_prefix&#x60; and &#x60;datacenter_prefix&#x60; can be the same, but it is not mandatory. The prefix is described as an URI. - &#x60;&#x60;denylisted&#x60;&#x60;: If the IP address was denylisted by the user, the information about the denylisted IP address is described as an URI. - &#x60;&#x60;first_appearence&#x60;&#x60;: URI to the first appearance of the IP address in the different datasets used to obtain the risk score. - &#x60;&#x60;last_appearence&#x60;&#x60;: URI to the last appearance of the IP address in the different datasets used to obtain the risk score.  ### Errors The endpoint will return the following errors: - a &#x60;400 Bad Request&#x60; error if the IP address is not public. - a &#x60;422 Unprocessable Entity&#x60; error if the IP address is malformed.  It will also return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.DataAssessmentApi();
let ipAddress = "ipAddress_example"; // String | 
apiInstance.assessIpV1AssessIpIpAddressGet(ipAddress, (error, data, response) => {
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

[**IPAssessmentOutput**](IPAssessmentOutput.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

