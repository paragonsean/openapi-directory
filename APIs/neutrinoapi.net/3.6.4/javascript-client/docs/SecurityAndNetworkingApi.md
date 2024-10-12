# NeutrinoApi.SecurityAndNetworkingApi

All URIs are relative to *https://neutrinoapi.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**domainLookup**](SecurityAndNetworkingApi.md#domainLookup) | **GET** /domain-lookup | Domain Lookup
[**emailVerify**](SecurityAndNetworkingApi.md#emailVerify) | **GET** /email-verify | Email Verify
[**hostReputation**](SecurityAndNetworkingApi.md#hostReputation) | **GET** /host-reputation | Host Reputation
[**iPBlocklist**](SecurityAndNetworkingApi.md#iPBlocklist) | **GET** /ip-blocklist | IP Blocklist
[**iPBlocklistDownload**](SecurityAndNetworkingApi.md#iPBlocklistDownload) | **GET** /ip-blocklist-download | IP Blocklist Download
[**iPProbe**](SecurityAndNetworkingApi.md#iPProbe) | **GET** /ip-probe | IP Probe



## domainLookup

> DomainLookupResponse domainLookup(host, opts)

Domain Lookup

Retrieve domain name details and detect potentially malicious or dangerous domains

### Example

```javascript
import NeutrinoApi from 'neutrino_api';
let defaultClient = NeutrinoApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: user-id
let user-id = defaultClient.authentications['user-id'];
user-id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user-id.apiKeyPrefix = 'Token';

let apiInstance = new NeutrinoApi.SecurityAndNetworkingApi();
let host = "host_example"; // String | A domain name, hostname, FQDN, URL, HTML link or email address to lookup
let opts = {
  'live': true // Boolean | For domains that we have never seen before then perform various live checks and realtime reconnaissance. <br>NOTE: this option may add additional non-deterministic delay to the request, if you require consistently fast API response times or just want to check our domain blocklists then you can disable this option
};
apiInstance.domainLookup(host, opts, (error, data, response) => {
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
 **host** | **String**| A domain name, hostname, FQDN, URL, HTML link or email address to lookup | 
 **live** | **Boolean**| For domains that we have never seen before then perform various live checks and realtime reconnaissance. &lt;br&gt;NOTE: this option may add additional non-deterministic delay to the request, if you require consistently fast API response times or just want to check our domain blocklists then you can disable this option | [optional] [default to true]

### Return type

[**DomainLookupResponse**](DomainLookupResponse.md)

### Authorization

[api-key](../README.md#api-key), [user-id](../README.md#user-id)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## emailVerify

> EmailVerifyResponse emailVerify(email, opts)

Email Verify

SMTP based email address verification

### Example

```javascript
import NeutrinoApi from 'neutrino_api';
let defaultClient = NeutrinoApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: user-id
let user-id = defaultClient.authentications['user-id'];
user-id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user-id.apiKeyPrefix = 'Token';

let apiInstance = new NeutrinoApi.SecurityAndNetworkingApi();
let email = "email_example"; // String | An email address
let opts = {
  'fixTypos': false // Boolean | Automatically attempt to fix typos in the address
};
apiInstance.emailVerify(email, opts, (error, data, response) => {
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
 **email** | **String**| An email address | 
 **fixTypos** | **Boolean**| Automatically attempt to fix typos in the address | [optional] [default to false]

### Return type

[**EmailVerifyResponse**](EmailVerifyResponse.md)

### Authorization

[api-key](../README.md#api-key), [user-id](../README.md#user-id)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## hostReputation

> HostReputationResponse hostReputation(host, opts)

Host Reputation

Check the reputation of an IP address, domain name or URL against a comprehensive list of blacklists and blocklists

### Example

```javascript
import NeutrinoApi from 'neutrino_api';
let defaultClient = NeutrinoApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: user-id
let user-id = defaultClient.authentications['user-id'];
user-id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user-id.apiKeyPrefix = 'Token';

let apiInstance = new NeutrinoApi.SecurityAndNetworkingApi();
let host = "host_example"; // String | An IP address, domain name, FQDN or URL. <br>If you supply a domain/URL it will be checked against the URI DNSBL lists
let opts = {
  'listRating': 3, // Number | Only check lists with this rating or better
  'zones': "zones_example" // String | Only check these DNSBL zones/hosts. Multiple zones can be supplied as comma-separated values
};
apiInstance.hostReputation(host, opts, (error, data, response) => {
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
 **host** | **String**| An IP address, domain name, FQDN or URL. &lt;br&gt;If you supply a domain/URL it will be checked against the URI DNSBL lists | 
 **listRating** | **Number**| Only check lists with this rating or better | [optional] [default to 3]
 **zones** | **String**| Only check these DNSBL zones/hosts. Multiple zones can be supplied as comma-separated values | [optional] 

### Return type

[**HostReputationResponse**](HostReputationResponse.md)

### Authorization

[api-key](../README.md#api-key), [user-id](../README.md#user-id)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## iPBlocklist

> IPBlocklistResponse iPBlocklist(ip, opts)

IP Blocklist

The IP Blocklist API will detect potentially malicious or dangerous IP addresses

### Example

```javascript
import NeutrinoApi from 'neutrino_api';
let defaultClient = NeutrinoApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: user-id
let user-id = defaultClient.authentications['user-id'];
user-id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user-id.apiKeyPrefix = 'Token';

let apiInstance = new NeutrinoApi.SecurityAndNetworkingApi();
let ip = "ip_example"; // String | An IPv4 or IPv6 address. Accepts standard IP notation (with or without port number), CIDR notation and IPv6 compressed notation. If multiple IPs are passed using comma-separated values the first non-bogon address on the list will be checked
let opts = {
  'vpnLookup': false // Boolean | Include public VPN provider IP addresses. <br><b>NOTE</b>: For more advanced VPN detection including the ability to identify private and stealth VPNs use the <a href=\"https://www.neutrinoapi.com/api/ip-probe/\">IP Probe API</a>
};
apiInstance.iPBlocklist(ip, opts, (error, data, response) => {
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
 **ip** | **String**| An IPv4 or IPv6 address. Accepts standard IP notation (with or without port number), CIDR notation and IPv6 compressed notation. If multiple IPs are passed using comma-separated values the first non-bogon address on the list will be checked | 
 **vpnLookup** | **Boolean**| Include public VPN provider IP addresses. &lt;br&gt;&lt;b&gt;NOTE&lt;/b&gt;: For more advanced VPN detection including the ability to identify private and stealth VPNs use the &lt;a href&#x3D;\&quot;https://www.neutrinoapi.com/api/ip-probe/\&quot;&gt;IP Probe API&lt;/a&gt; | [optional] [default to false]

### Return type

[**IPBlocklistResponse**](IPBlocklistResponse.md)

### Authorization

[api-key](../README.md#api-key), [user-id](../README.md#user-id)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## iPBlocklistDownload

> File iPBlocklistDownload(opts)

IP Blocklist Download

This API is a direct feed to our IP blocklist data

### Example

```javascript
import NeutrinoApi from 'neutrino_api';
let defaultClient = NeutrinoApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: user-id
let user-id = defaultClient.authentications['user-id'];
user-id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user-id.apiKeyPrefix = 'Token';

let apiInstance = new NeutrinoApi.SecurityAndNetworkingApi();
let opts = {
  'format': "'csv'", // String | The data format. Can be either CSV or TXT
  'includeVpn': false, // Boolean | Include public VPN provider addresses, this option is only available for Tier 3 or higher accounts. Adds any IPs which are solely listed as VPN providers, IPs that are listed on multiple sensors will still be included without enabling this option. <br><b>WARNING</b>: This adds at least an additional 8 million IP addresses to the download if not using CIDR notation
  'cidr': false, // Boolean | Output IPs using CIDR notation. This option should be preferred but is off by default for backwards compatibility
  'ip6': false // Boolean | Output the IPv6 version of the blocklist, the default is to output IPv4 only. Note that this option enables CIDR notation too as this is the only notation currently supported for IPv6
};
apiInstance.iPBlocklistDownload(opts, (error, data, response) => {
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
 **format** | **String**| The data format. Can be either CSV or TXT | [optional] [default to &#39;csv&#39;]
 **includeVpn** | **Boolean**| Include public VPN provider addresses, this option is only available for Tier 3 or higher accounts. Adds any IPs which are solely listed as VPN providers, IPs that are listed on multiple sensors will still be included without enabling this option. &lt;br&gt;&lt;b&gt;WARNING&lt;/b&gt;: This adds at least an additional 8 million IP addresses to the download if not using CIDR notation | [optional] [default to false]
 **cidr** | **Boolean**| Output IPs using CIDR notation. This option should be preferred but is off by default for backwards compatibility | [optional] [default to false]
 **ip6** | **Boolean**| Output the IPv6 version of the blocklist, the default is to output IPv4 only. Note that this option enables CIDR notation too as this is the only notation currently supported for IPv6 | [optional] [default to false]

### Return type

**File**

### Authorization

[api-key](../README.md#api-key), [user-id](../README.md#user-id)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## iPProbe

> IPProbeResponse iPProbe(ip)

IP Probe

Execute a realtime network probe against an IPv4 or IPv6 address

### Example

```javascript
import NeutrinoApi from 'neutrino_api';
let defaultClient = NeutrinoApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: user-id
let user-id = defaultClient.authentications['user-id'];
user-id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user-id.apiKeyPrefix = 'Token';

let apiInstance = new NeutrinoApi.SecurityAndNetworkingApi();
let ip = "ip_example"; // String | IPv4 or IPv6 address
apiInstance.iPProbe(ip, (error, data, response) => {
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
 **ip** | **String**| IPv4 or IPv6 address | 

### Return type

[**IPProbeResponse**](IPProbeResponse.md)

### Authorization

[api-key](../README.md#api-key), [user-id](../README.md#user-id)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

