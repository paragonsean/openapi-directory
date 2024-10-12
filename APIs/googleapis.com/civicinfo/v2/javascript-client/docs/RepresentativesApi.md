# GoogleCivicInformationApi.RepresentativesApi

All URIs are relative to *https://civicinfo.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**civicinfoRepresentativesRepresentativeInfoByAddress**](RepresentativesApi.md#civicinfoRepresentativesRepresentativeInfoByAddress) | **GET** /civicinfo/v2/representatives | 
[**civicinfoRepresentativesRepresentativeInfoByDivision**](RepresentativesApi.md#civicinfoRepresentativesRepresentativeInfoByDivision) | **GET** /civicinfo/v2/representatives/{ocdId} | 



## civicinfoRepresentativesRepresentativeInfoByAddress

> RepresentativeInfoResponse civicinfoRepresentativesRepresentativeInfoByAddress(opts)



Looks up political geography and representative information for a single address.

### Example

```javascript
import GoogleCivicInformationApi from 'google_civic_information_api';

let apiInstance = new GoogleCivicInformationApi.RepresentativesApi();
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'address': "address_example", // String | The address to look up. May only be specified if the field ocdId is not given in the URL
  'includeOffices': true, // Boolean | Whether to return information about offices and officials. If false, only the top-level district information will be returned.
  'levels': ["null"], // [String] | A list of office levels to filter by. Only offices that serve at least one of these levels will be returned. Divisions that don't contain a matching office will not be returned.
  'roles': ["null"] // [String] | A list of office roles to filter by. Only offices fulfilling one of these roles will be returned. Divisions that don't contain a matching office will not be returned.
};
apiInstance.civicinfoRepresentativesRepresentativeInfoByAddress(opts, (error, data, response) => {
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
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **address** | **String**| The address to look up. May only be specified if the field ocdId is not given in the URL | [optional] 
 **includeOffices** | **Boolean**| Whether to return information about offices and officials. If false, only the top-level district information will be returned. | [optional] 
 **levels** | [**[String]**](String.md)| A list of office levels to filter by. Only offices that serve at least one of these levels will be returned. Divisions that don&#39;t contain a matching office will not be returned. | [optional] 
 **roles** | [**[String]**](String.md)| A list of office roles to filter by. Only offices fulfilling one of these roles will be returned. Divisions that don&#39;t contain a matching office will not be returned. | [optional] 

### Return type

[**RepresentativeInfoResponse**](RepresentativeInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## civicinfoRepresentativesRepresentativeInfoByDivision

> RepresentativeInfoData civicinfoRepresentativesRepresentativeInfoByDivision(ocdId, opts)



Looks up representative information for a single geographic division.

### Example

```javascript
import GoogleCivicInformationApi from 'google_civic_information_api';

let apiInstance = new GoogleCivicInformationApi.RepresentativesApi();
let ocdId = "ocdId_example"; // String | The Open Civic Data division identifier of the division to look up.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'levels': ["null"], // [String] | A list of office levels to filter by. Only offices that serve at least one of these levels will be returned. Divisions that don't contain a matching office will not be returned.
  'recursive': true, // Boolean | If true, information about all divisions contained in the division requested will be included as well. For example, if querying ocd-division/country:us/district:dc, this would also return all DC's wards and ANCs.
  'roles': ["null"] // [String] | A list of office roles to filter by. Only offices fulfilling one of these roles will be returned. Divisions that don't contain a matching office will not be returned.
};
apiInstance.civicinfoRepresentativesRepresentativeInfoByDivision(ocdId, opts, (error, data, response) => {
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
 **ocdId** | **String**| The Open Civic Data division identifier of the division to look up. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **levels** | [**[String]**](String.md)| A list of office levels to filter by. Only offices that serve at least one of these levels will be returned. Divisions that don&#39;t contain a matching office will not be returned. | [optional] 
 **recursive** | **Boolean**| If true, information about all divisions contained in the division requested will be included as well. For example, if querying ocd-division/country:us/district:dc, this would also return all DC&#39;s wards and ANCs. | [optional] 
 **roles** | [**[String]**](String.md)| A list of office roles to filter by. Only offices fulfilling one of these roles will be returned. Divisions that don&#39;t contain a matching office will not be returned. | [optional] 

### Return type

[**RepresentativeInfoData**](RepresentativeInfoData.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

