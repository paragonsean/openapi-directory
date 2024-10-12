# MarketingApi.AdReportMetadataApi

All URIs are relative to *https://api.ebay.com/sell/marketing/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getReportMetadata**](AdReportMetadataApi.md#getReportMetadata) | **GET** /ad_report_metadata | 
[**getReportMetadataForReportType**](AdReportMetadataApi.md#getReportMetadataForReportType) | **GET** /ad_report_metadata/{report_type} | 



## getReportMetadata

> ReportMetadatas getReportMetadata()



This call retrieves information that details the fields used in each of the Promoted Listings reports. Use the returned information to configure the different types of Promoted Listings reports.&lt;/br&gt;&lt;/br&gt;The request for this method does not use a payload or any URI parameters.&lt;br/&gt;&lt;br/&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; The reporting of some data related to sales and ad-fees may require a 72-hour (&lt;b&gt;maximum&lt;/b&gt;) adjustment period which is often referred to as the &lt;i&gt;Reconciliation Period&lt;/i&gt;. Such adjustment periods should, on average, be minimal. However, at any given time, the &lt;b&gt;payments&lt;/b&gt; tab may be used to view those amounts that have actually been charged.&lt;/span&gt;

### Example

```javascript
import MarketingApi from 'marketing_api';
let defaultClient = MarketingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: api_auth
let api_auth = defaultClient.authentications['api_auth'];
api_auth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: api_auth
let api_auth = defaultClient.authentications['api_auth'];
api_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MarketingApi.AdReportMetadataApi();
apiInstance.getReportMetadata((error, data, response) => {
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

[**ReportMetadatas**](ReportMetadatas.md)

### Authorization

[api_auth](../README.md#api_auth), [api_auth](../README.md#api_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getReportMetadataForReportType

> ReportMetadata getReportMetadataForReportType(reportType)



This call retrieves metadata that details the fields used by a specific Promoted Listings report type. Use the &lt;b&gt;report_type&lt;/b&gt; path parameter to indicate metadata to retrieve.&lt;br/&gt;&lt;br/&gt;This method does not use a request payload.&lt;br/&gt;&lt;br/&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; The reporting of some data related to sales and ad-fees may require a 72-hour (&lt;b&gt;maximum&lt;/b&gt;) adjustment period which is often referred to as the &lt;i&gt;Reconciliation Period&lt;/i&gt;. Such adjustment periods should, on average, be minimal. However, at any given time, the &lt;b&gt;payments&lt;/b&gt; tab may be used to view those amounts that have actually been charged.&lt;/span&gt;

### Example

```javascript
import MarketingApi from 'marketing_api';
let defaultClient = MarketingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: api_auth
let api_auth = defaultClient.authentications['api_auth'];
api_auth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: api_auth
let api_auth = defaultClient.authentications['api_auth'];
api_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MarketingApi.AdReportMetadataApi();
let reportType = "reportType_example"; // String | The name of the report type whose metadata you want to retrieve.<br /><br /><span class=\"tablenote\"><b>Tip:</b> For details about available report types and their descriptions, refer to the <a href=\"/api-docs/sell/marketing/types/plr:ReportTypeEnum\">ReportTypeEnum</a>.</span>
apiInstance.getReportMetadataForReportType(reportType, (error, data, response) => {
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
 **reportType** | **String**| The name of the report type whose metadata you want to retrieve.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Tip:&lt;/b&gt; For details about available report types and their descriptions, refer to the &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/types/plr:ReportTypeEnum\&quot;&gt;ReportTypeEnum&lt;/a&gt;.&lt;/span&gt; | 

### Return type

[**ReportMetadata**](ReportMetadata.md)

### Authorization

[api_auth](../README.md#api_auth), [api_auth](../README.md#api_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

