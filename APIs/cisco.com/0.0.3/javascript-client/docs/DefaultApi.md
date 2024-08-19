# CiscoPsirtOpenVulnApi.DefaultApi

All URIs are relative to *https://api.cisco.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**securityAdvisoriesCvrfAdvisoryAdvisoryIdGet**](DefaultApi.md#securityAdvisoriesCvrfAdvisoryAdvisoryIdGet) | **GET** /security/advisories/cvrf/advisory/{advisory_id} | 
[**securityAdvisoriesCvrfAllGet**](DefaultApi.md#securityAdvisoriesCvrfAllGet) | **GET** /security/advisories/cvrf/all | 
[**securityAdvisoriesCvrfCveCveIdGet**](DefaultApi.md#securityAdvisoriesCvrfCveCveIdGet) | **GET** /security/advisories/cvrf/cve/{cve_id} | 
[**securityAdvisoriesCvrfLatestNumberGet**](DefaultApi.md#securityAdvisoriesCvrfLatestNumberGet) | **GET** /security/advisories/cvrf/latest/{number} | 
[**securityAdvisoriesCvrfProductGet**](DefaultApi.md#securityAdvisoriesCvrfProductGet) | **GET** /security/advisories/cvrf/product | 
[**securityAdvisoriesCvrfSeveritySeverityFirstpublishedGet**](DefaultApi.md#securityAdvisoriesCvrfSeveritySeverityFirstpublishedGet) | **GET** /security/advisories/cvrf/severity/{severity}/firstpublished | 
[**securityAdvisoriesCvrfSeveritySeverityGet**](DefaultApi.md#securityAdvisoriesCvrfSeveritySeverityGet) | **GET** /security/advisories/cvrf/severity/{severity} | 
[**securityAdvisoriesCvrfSeveritySeverityLastpublishedGet**](DefaultApi.md#securityAdvisoriesCvrfSeveritySeverityLastpublishedGet) | **GET** /security/advisories/cvrf/severity/{severity}/lastpublished | 
[**securityAdvisoriesCvrfYearYearGet**](DefaultApi.md#securityAdvisoriesCvrfYearYearGet) | **GET** /security/advisories/cvrf/year/{year} | 
[**securityAdvisoriesIosGet**](DefaultApi.md#securityAdvisoriesIosGet) | **GET** /security/advisories/ios | 
[**securityAdvisoriesIosxeGet**](DefaultApi.md#securityAdvisoriesIosxeGet) | **GET** /security/advisories/iosxe | 
[**securityAdvisoriesOvalAdvisoryAdvisoryIdGet**](DefaultApi.md#securityAdvisoriesOvalAdvisoryAdvisoryIdGet) | **GET** /security/advisories/oval/advisory/{advisory_id} | 
[**securityAdvisoriesOvalAllGet**](DefaultApi.md#securityAdvisoriesOvalAllGet) | **GET** /security/advisories/oval/all | 
[**securityAdvisoriesOvalCveCveIdGet**](DefaultApi.md#securityAdvisoriesOvalCveCveIdGet) | **GET** /security/advisories/oval/cve/{cve_id} | 
[**securityAdvisoriesOvalLatestNumberGet**](DefaultApi.md#securityAdvisoriesOvalLatestNumberGet) | **GET** /security/advisories/oval/latest/{number} | 
[**securityAdvisoriesOvalProductGet**](DefaultApi.md#securityAdvisoriesOvalProductGet) | **GET** /security/advisories/oval/product | 
[**securityAdvisoriesOvalSeveritySeverityFirstpublishedGet**](DefaultApi.md#securityAdvisoriesOvalSeveritySeverityFirstpublishedGet) | **GET** /security/advisories/oval/severity/{severity}/firstpublished | 
[**securityAdvisoriesOvalSeveritySeverityGet**](DefaultApi.md#securityAdvisoriesOvalSeveritySeverityGet) | **GET** /security/advisories/oval/severity/{severity} | 
[**securityAdvisoriesOvalSeveritySeverityLastpublishedGet**](DefaultApi.md#securityAdvisoriesOvalSeveritySeverityLastpublishedGet) | **GET** /security/advisories/oval/severity/{severity}/lastpublished | 



## securityAdvisoriesCvrfAdvisoryAdvisoryIdGet

> securityAdvisoriesCvrfAdvisoryAdvisoryIdGet(advisoryId)



Used to obtain an advisory in CVRF format for a given advisory ID &#x60;advisory_id&#x60; (i.e., cisco-sa-20150819-pcp) 

### Example

```javascript
import CiscoPsirtOpenVulnApi from 'cisco_psirt_open_vuln_api';
let defaultClient = CiscoPsirtOpenVulnApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
let psirt_openvuln_api_auth = defaultClient.authentications['psirt_openvuln_api_auth'];
psirt_openvuln_api_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CiscoPsirtOpenVulnApi.DefaultApi();
let advisoryId = "advisoryId_example"; // String | advisory ID
apiInstance.securityAdvisoriesCvrfAdvisoryAdvisoryIdGet(advisoryId, (error, data, response) => {
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
 **advisoryId** | **String**| advisory ID | 

### Return type

null (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## securityAdvisoriesCvrfAllGet

> securityAdvisoriesCvrfAllGet()



Used to obtain all advisories in Common Vulnerability Reporting Format (CVRF). For more information about CVRF go to https://communities.cisco.com/docs/DOC-63156 . By default the output is in JSON. To obtain the output in XML use the .xml extension. For example, /advisories/cvrf/all.xml 

### Example

```javascript
import CiscoPsirtOpenVulnApi from 'cisco_psirt_open_vuln_api';
let defaultClient = CiscoPsirtOpenVulnApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
let psirt_openvuln_api_auth = defaultClient.authentications['psirt_openvuln_api_auth'];
psirt_openvuln_api_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CiscoPsirtOpenVulnApi.DefaultApi();
apiInstance.securityAdvisoriesCvrfAllGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## securityAdvisoriesCvrfCveCveIdGet

> securityAdvisoriesCvrfCveCveIdGet(cveId)



Used to obtain an advisory in CVRF format for a given Common Vulnerability Enumerator (CVE). The &#x60;cve_id&#x60; format is CVE-YYYY-NNNN. For more information about CVE visit http://cve.mitre.org/ 

### Example

```javascript
import CiscoPsirtOpenVulnApi from 'cisco_psirt_open_vuln_api';
let defaultClient = CiscoPsirtOpenVulnApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
let psirt_openvuln_api_auth = defaultClient.authentications['psirt_openvuln_api_auth'];
psirt_openvuln_api_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CiscoPsirtOpenVulnApi.DefaultApi();
let cveId = "cveId_example"; // String | CVE Identifier (i.e., CVE-YYYY-NNNN)
apiInstance.securityAdvisoriesCvrfCveCveIdGet(cveId, (error, data, response) => {
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
 **cveId** | **String**| CVE Identifier (i.e., CVE-YYYY-NNNN) | 

### Return type

null (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## securityAdvisoriesCvrfLatestNumberGet

> securityAdvisoriesCvrfLatestNumberGet(number)



Used to obtain all the latest security advisories in CVRF format given an absolute number. For instance, the latest 10 or latest 5. 

### Example

```javascript
import CiscoPsirtOpenVulnApi from 'cisco_psirt_open_vuln_api';
let defaultClient = CiscoPsirtOpenVulnApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
let psirt_openvuln_api_auth = defaultClient.authentications['psirt_openvuln_api_auth'];
psirt_openvuln_api_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CiscoPsirtOpenVulnApi.DefaultApi();
let number = 56; // Number | An absolute number to obtain the latest security advisories.
apiInstance.securityAdvisoriesCvrfLatestNumberGet(number, (error, data, response) => {
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
 **number** | **Number**| An absolute number to obtain the latest security advisories. | 

### Return type

null (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## securityAdvisoriesCvrfProductGet

> securityAdvisoriesCvrfProductGet(product)



Used to obtain all the advisories that affects the given product name. 

### Example

```javascript
import CiscoPsirtOpenVulnApi from 'cisco_psirt_open_vuln_api';
let defaultClient = CiscoPsirtOpenVulnApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
let psirt_openvuln_api_auth = defaultClient.authentications['psirt_openvuln_api_auth'];
psirt_openvuln_api_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CiscoPsirtOpenVulnApi.DefaultApi();
let product = "product_example"; // String | An product name to obtain security advisories that matches given product name.
apiInstance.securityAdvisoriesCvrfProductGet(product, (error, data, response) => {
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
 **product** | **String**| An product name to obtain security advisories that matches given product name. | 

### Return type

null (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## securityAdvisoriesCvrfSeveritySeverityFirstpublishedGet

> securityAdvisoriesCvrfSeveritySeverityFirstpublishedGet(severity, startDate, endDate)



Used to obtain all security advisories for a given security impact rating (critical, high, medium, or low) in CVRF format and additionally filter based of firstpublished start date and enddate 

### Example

```javascript
import CiscoPsirtOpenVulnApi from 'cisco_psirt_open_vuln_api';
let defaultClient = CiscoPsirtOpenVulnApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
let psirt_openvuln_api_auth = defaultClient.authentications['psirt_openvuln_api_auth'];
psirt_openvuln_api_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CiscoPsirtOpenVulnApi.DefaultApi();
let severity = "severity_example"; // String | Used to obtain all advisories that have a security impact rating of critical
let startDate = new Date("2013-10-20"); // Date | 
let endDate = new Date("2013-10-20"); // Date | 
apiInstance.securityAdvisoriesCvrfSeveritySeverityFirstpublishedGet(severity, startDate, endDate, (error, data, response) => {
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
 **severity** | **String**| Used to obtain all advisories that have a security impact rating of critical | 
 **startDate** | **Date**|  | 
 **endDate** | **Date**|  | 

### Return type

null (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## securityAdvisoriesCvrfSeveritySeverityGet

> securityAdvisoriesCvrfSeveritySeverityGet(severity)



Used to obtain all security advisories for a given security impact rating (critical, high, medium, or low) in CVRF format. 

### Example

```javascript
import CiscoPsirtOpenVulnApi from 'cisco_psirt_open_vuln_api';
let defaultClient = CiscoPsirtOpenVulnApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
let psirt_openvuln_api_auth = defaultClient.authentications['psirt_openvuln_api_auth'];
psirt_openvuln_api_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CiscoPsirtOpenVulnApi.DefaultApi();
let severity = "severity_example"; // String | Critical, High, Medium, Low
apiInstance.securityAdvisoriesCvrfSeveritySeverityGet(severity, (error, data, response) => {
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
 **severity** | **String**| Critical, High, Medium, Low | 

### Return type

null (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## securityAdvisoriesCvrfSeveritySeverityLastpublishedGet

> securityAdvisoriesCvrfSeveritySeverityLastpublishedGet(severity, startDate, endDate)



Used to obtain all security advisories for a given security impact rating (critical, high, medium, or low) in CVRF format. 

### Example

```javascript
import CiscoPsirtOpenVulnApi from 'cisco_psirt_open_vuln_api';
let defaultClient = CiscoPsirtOpenVulnApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
let psirt_openvuln_api_auth = defaultClient.authentications['psirt_openvuln_api_auth'];
psirt_openvuln_api_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CiscoPsirtOpenVulnApi.DefaultApi();
let severity = "severity_example"; // String | Used to obtain all advisories that have a security impact rating of critical
let startDate = new Date("2013-10-20"); // Date | 
let endDate = new Date("2013-10-20"); // Date | 
apiInstance.securityAdvisoriesCvrfSeveritySeverityLastpublishedGet(severity, startDate, endDate, (error, data, response) => {
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
 **severity** | **String**| Used to obtain all advisories that have a security impact rating of critical | 
 **startDate** | **Date**|  | 
 **endDate** | **Date**|  | 

### Return type

null (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## securityAdvisoriesCvrfYearYearGet

> securityAdvisoriesCvrfYearYearGet(year)



Used to obtain all security advisories that have were orginally published in a specific year &#x60;YYYY&#x60;. 

### Example

```javascript
import CiscoPsirtOpenVulnApi from 'cisco_psirt_open_vuln_api';
let defaultClient = CiscoPsirtOpenVulnApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
let psirt_openvuln_api_auth = defaultClient.authentications['psirt_openvuln_api_auth'];
psirt_openvuln_api_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CiscoPsirtOpenVulnApi.DefaultApi();
let year = "year_example"; // String | The four digit year.
apiInstance.securityAdvisoriesCvrfYearYearGet(year, (error, data, response) => {
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
 **year** | **String**| The four digit year. | 

### Return type

null (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## securityAdvisoriesIosGet

> securityAdvisoriesIosGet(version)



Used to obtain all advisories that affects the given ios version 

### Example

```javascript
import CiscoPsirtOpenVulnApi from 'cisco_psirt_open_vuln_api';
let defaultClient = CiscoPsirtOpenVulnApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
let psirt_openvuln_api_auth = defaultClient.authentications['psirt_openvuln_api_auth'];
psirt_openvuln_api_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CiscoPsirtOpenVulnApi.DefaultApi();
let version = "version_example"; // String | IOS version to obtain security advisories
apiInstance.securityAdvisoriesIosGet(version, (error, data, response) => {
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
 **version** | **String**| IOS version to obtain security advisories | 

### Return type

null (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## securityAdvisoriesIosxeGet

> securityAdvisoriesIosxeGet(version)



Used to obtain all advisories that affects the given ios version 

### Example

```javascript
import CiscoPsirtOpenVulnApi from 'cisco_psirt_open_vuln_api';
let defaultClient = CiscoPsirtOpenVulnApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
let psirt_openvuln_api_auth = defaultClient.authentications['psirt_openvuln_api_auth'];
psirt_openvuln_api_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CiscoPsirtOpenVulnApi.DefaultApi();
let version = "version_example"; // String | IOS version to obtain security advisories
apiInstance.securityAdvisoriesIosxeGet(version, (error, data, response) => {
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
 **version** | **String**| IOS version to obtain security advisories | 

### Return type

null (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## securityAdvisoriesOvalAdvisoryAdvisoryIdGet

> securityAdvisoriesOvalAdvisoryAdvisoryIdGet(advisoryId)



Used to obtain OVAL definitions for a given advisory ID &#x60;advisory_id&#x60; (i.e., cisco-sa-20150819-pcp) 

### Example

```javascript
import CiscoPsirtOpenVulnApi from 'cisco_psirt_open_vuln_api';
let defaultClient = CiscoPsirtOpenVulnApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
let psirt_openvuln_api_auth = defaultClient.authentications['psirt_openvuln_api_auth'];
psirt_openvuln_api_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CiscoPsirtOpenVulnApi.DefaultApi();
let advisoryId = "advisoryId_example"; // String | advisory ID
apiInstance.securityAdvisoriesOvalAdvisoryAdvisoryIdGet(advisoryId, (error, data, response) => {
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
 **advisoryId** | **String**| advisory ID | 

### Return type

null (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## securityAdvisoriesOvalAllGet

> securityAdvisoriesOvalAllGet()



Used to obtain all Open Vulnerability and Assessment Language (OVAL) definitions available for Cisco security vulnerabilities. For more information about OVAL go to https://communities.cisco.com/docs/DOC-63158 . By default the output is in JSON. To obtain the output in XML use the .xml extension. For example, /advisories/oval/all.xml 

### Example

```javascript
import CiscoPsirtOpenVulnApi from 'cisco_psirt_open_vuln_api';
let defaultClient = CiscoPsirtOpenVulnApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
let psirt_openvuln_api_auth = defaultClient.authentications['psirt_openvuln_api_auth'];
psirt_openvuln_api_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CiscoPsirtOpenVulnApi.DefaultApi();
apiInstance.securityAdvisoriesOvalAllGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## securityAdvisoriesOvalCveCveIdGet

> securityAdvisoriesOvalCveCveIdGet(cveId)



Used to obtain OVAL definitions for a given CVE Identifier. The &#x60;cve_id&#x60; format is CVE-YYYY-NNNN. 

### Example

```javascript
import CiscoPsirtOpenVulnApi from 'cisco_psirt_open_vuln_api';
let defaultClient = CiscoPsirtOpenVulnApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
let psirt_openvuln_api_auth = defaultClient.authentications['psirt_openvuln_api_auth'];
psirt_openvuln_api_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CiscoPsirtOpenVulnApi.DefaultApi();
let cveId = "cveId_example"; // String | CVE Identifier (i.e., CVE-YYYY-NNNN)
apiInstance.securityAdvisoriesOvalCveCveIdGet(cveId, (error, data, response) => {
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
 **cveId** | **String**| CVE Identifier (i.e., CVE-YYYY-NNNN) | 

### Return type

null (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## securityAdvisoriesOvalLatestNumberGet

> securityAdvisoriesOvalLatestNumberGet(number)



Used to obtain all the latest OVAL definitions given an absolute number. For instance, the latest 10 or latest 5. 

### Example

```javascript
import CiscoPsirtOpenVulnApi from 'cisco_psirt_open_vuln_api';
let defaultClient = CiscoPsirtOpenVulnApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
let psirt_openvuln_api_auth = defaultClient.authentications['psirt_openvuln_api_auth'];
psirt_openvuln_api_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CiscoPsirtOpenVulnApi.DefaultApi();
let number = 56; // Number | The latest OVAL definitions (absolute number).
apiInstance.securityAdvisoriesOvalLatestNumberGet(number, (error, data, response) => {
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
 **number** | **Number**| The latest OVAL definitions (absolute number). | 

### Return type

null (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## securityAdvisoriesOvalProductGet

> securityAdvisoriesOvalProductGet(product)



Used to obtain all the oval advisories that affects the given product name. 

### Example

```javascript
import CiscoPsirtOpenVulnApi from 'cisco_psirt_open_vuln_api';
let defaultClient = CiscoPsirtOpenVulnApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
let psirt_openvuln_api_auth = defaultClient.authentications['psirt_openvuln_api_auth'];
psirt_openvuln_api_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CiscoPsirtOpenVulnApi.DefaultApi();
let product = "product_example"; // String | An product name to obtain security advisories that matches given product name.
apiInstance.securityAdvisoriesOvalProductGet(product, (error, data, response) => {
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
 **product** | **String**| An product name to obtain security advisories that matches given product name. | 

### Return type

null (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## securityAdvisoriesOvalSeveritySeverityFirstpublishedGet

> securityAdvisoriesOvalSeveritySeverityFirstpublishedGet(severity, startDate, endDate)



Used to obtain all security advisories for a given security impact rating (critical, high, medium, or low) in OVAL format. 

### Example

```javascript
import CiscoPsirtOpenVulnApi from 'cisco_psirt_open_vuln_api';
let defaultClient = CiscoPsirtOpenVulnApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
let psirt_openvuln_api_auth = defaultClient.authentications['psirt_openvuln_api_auth'];
psirt_openvuln_api_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CiscoPsirtOpenVulnApi.DefaultApi();
let severity = "severity_example"; // String | Critical, High, Medium, Low
let startDate = new Date("2013-10-20"); // Date | 
let endDate = new Date("2013-10-20"); // Date | 
apiInstance.securityAdvisoriesOvalSeveritySeverityFirstpublishedGet(severity, startDate, endDate, (error, data, response) => {
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
 **severity** | **String**| Critical, High, Medium, Low | 
 **startDate** | **Date**|  | 
 **endDate** | **Date**|  | 

### Return type

null (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## securityAdvisoriesOvalSeveritySeverityGet

> securityAdvisoriesOvalSeveritySeverityGet(severity)



Used to obtain all OVAL definitions for a given security impact rating (critical, high, medium, or low). 

### Example

```javascript
import CiscoPsirtOpenVulnApi from 'cisco_psirt_open_vuln_api';
let defaultClient = CiscoPsirtOpenVulnApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
let psirt_openvuln_api_auth = defaultClient.authentications['psirt_openvuln_api_auth'];
psirt_openvuln_api_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CiscoPsirtOpenVulnApi.DefaultApi();
let severity = "severity_example"; // String | Used to obtain all OVAL definitions for advisories that have a security impact rating of critical
apiInstance.securityAdvisoriesOvalSeveritySeverityGet(severity, (error, data, response) => {
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
 **severity** | **String**| Used to obtain all OVAL definitions for advisories that have a security impact rating of critical | 

### Return type

null (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## securityAdvisoriesOvalSeveritySeverityLastpublishedGet

> securityAdvisoriesOvalSeveritySeverityLastpublishedGet(severity, startDate, endDate)



Used to obtain all security advisories for a given security impact rating (critical, high, medium, or low) in OVAL format. 

### Example

```javascript
import CiscoPsirtOpenVulnApi from 'cisco_psirt_open_vuln_api';
let defaultClient = CiscoPsirtOpenVulnApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
let psirt_openvuln_api_auth = defaultClient.authentications['psirt_openvuln_api_auth'];
psirt_openvuln_api_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CiscoPsirtOpenVulnApi.DefaultApi();
let severity = "severity_example"; // String | Critical, High, Medium, Low
let startDate = new Date("2013-10-20"); // Date | 
let endDate = new Date("2013-10-20"); // Date | 
apiInstance.securityAdvisoriesOvalSeveritySeverityLastpublishedGet(severity, startDate, endDate, (error, data, response) => {
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
 **severity** | **String**| Critical, High, Medium, Low | 
 **startDate** | **Date**|  | 
 **endDate** | **Date**|  | 

### Return type

null (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

