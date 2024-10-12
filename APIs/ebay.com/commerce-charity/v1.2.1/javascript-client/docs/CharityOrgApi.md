# CharityApi.CharityOrgApi

All URIs are relative to *https://api.ebay.com/commerce/charity/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCharityOrg**](CharityOrgApi.md#getCharityOrg) | **GET** /charity_org/{charity_org_id} | 
[**getCharityOrgs**](CharityOrgApi.md#getCharityOrgs) | **GET** /charity_org | 



## getCharityOrg

> CharityOrg getCharityOrg(charityOrgId, X_EBAY_C_MARKETPLACE_ID)



This call is used to retrieve detailed information about supported charitable organizations. It allows users to retrieve the details for a specific charitable organization using its charity organization ID.

### Example

```javascript
import CharityApi from 'charity_api';
let defaultClient = CharityApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: api_auth
let api_auth = defaultClient.authentications['api_auth'];
api_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CharityApi.CharityOrgApi();
let charityOrgId = "charityOrgId_example"; // String | The unique ID of the charitable organization.
let X_EBAY_C_MARKETPLACE_ID = "X_EBAY_C_MARKETPLACE_ID_example"; // String | A header used to specify the eBay marketplace ID.<br /><br /><b>Valid Values:</b> <code>EBAY_GB</code> and <code>EBAY_US</code>
apiInstance.getCharityOrg(charityOrgId, X_EBAY_C_MARKETPLACE_ID, (error, data, response) => {
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
 **charityOrgId** | **String**| The unique ID of the charitable organization. | 
 **X_EBAY_C_MARKETPLACE_ID** | **String**| A header used to specify the eBay marketplace ID.&lt;br /&gt;&lt;br /&gt;&lt;b&gt;Valid Values:&lt;/b&gt; &lt;code&gt;EBAY_GB&lt;/code&gt; and &lt;code&gt;EBAY_US&lt;/code&gt; | 

### Return type

[**CharityOrg**](CharityOrg.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCharityOrgs

> CharitySearchResponse getCharityOrgs(X_EBAY_C_MARKETPLACE_ID, opts)



This call is used to search for supported charitable organizations. It allows users to search for a specific charitable organization, or for multiple charitable organizations, from a particular charitable domain and/or geographical region, or by using search criteria.&lt;br /&gt;&lt;br /&gt;The call returns paginated search results containing the charitable organizations that match the specified criteria.

### Example

```javascript
import CharityApi from 'charity_api';
let defaultClient = CharityApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: api_auth
let api_auth = defaultClient.authentications['api_auth'];
api_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CharityApi.CharityOrgApi();
let X_EBAY_C_MARKETPLACE_ID = "X_EBAY_C_MARKETPLACE_ID_example"; // String | A header used to specify the eBay marketplace ID.<br /><br /><b>Valid Values:</b> <code>EBAY_GB</code> and <code>EBAY_US</code>
let opts = {
  'limit': "limit_example", // String | The number of items, from the result set, returned in a single page.<br /><br /><b>Valid Values:</b> <code>1-100</code><br /><br /><b>Default:</b> <code>20</code>
  'offset': "offset_example", // String | The number of items that will be skipped in the result set. This is used with the <b>limit</b> field to control the pagination of the output.<br /><br />For example, if the <b>offset</b> is set to <code>0</code> and the <b>limit</b> is set to <code>10</code>, the method will retrieve items 1 through 10 from the list of items returned. If the <b>offset</b> is set to <code>10</code> and the <b>limit</b> is set to <code>10</code>, the method will retrieve items 11 through 20 from the list of items returned.<br /><br /><b>Valid Values:</b> <code>0-10,000</code><br /><br /><b>Default:</b> <code>0</code>
  'q': "q_example", // String | A query string that matches the keywords in name, mission statement, or description.
  'registrationIds': "registrationIds_example" // String | A comma-separated list of charitable organization registration IDs.<br /><br /><span class=\"tablenote\"><b>Note: </b>Do not specify this parameter for query-based searches. Specify either the <b>q</b> or <b>registration_ids</b> parameter, but not both.</span><br /><br /><b>Maximum Limit:</b> <code>20</code>
};
apiInstance.getCharityOrgs(X_EBAY_C_MARKETPLACE_ID, opts, (error, data, response) => {
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
 **X_EBAY_C_MARKETPLACE_ID** | **String**| A header used to specify the eBay marketplace ID.&lt;br /&gt;&lt;br /&gt;&lt;b&gt;Valid Values:&lt;/b&gt; &lt;code&gt;EBAY_GB&lt;/code&gt; and &lt;code&gt;EBAY_US&lt;/code&gt; | 
 **limit** | **String**| The number of items, from the result set, returned in a single page.&lt;br /&gt;&lt;br /&gt;&lt;b&gt;Valid Values:&lt;/b&gt; &lt;code&gt;1-100&lt;/code&gt;&lt;br /&gt;&lt;br /&gt;&lt;b&gt;Default:&lt;/b&gt; &lt;code&gt;20&lt;/code&gt; | [optional] 
 **offset** | **String**| The number of items that will be skipped in the result set. This is used with the &lt;b&gt;limit&lt;/b&gt; field to control the pagination of the output.&lt;br /&gt;&lt;br /&gt;For example, if the &lt;b&gt;offset&lt;/b&gt; is set to &lt;code&gt;0&lt;/code&gt; and the &lt;b&gt;limit&lt;/b&gt; is set to &lt;code&gt;10&lt;/code&gt;, the method will retrieve items 1 through 10 from the list of items returned. If the &lt;b&gt;offset&lt;/b&gt; is set to &lt;code&gt;10&lt;/code&gt; and the &lt;b&gt;limit&lt;/b&gt; is set to &lt;code&gt;10&lt;/code&gt;, the method will retrieve items 11 through 20 from the list of items returned.&lt;br /&gt;&lt;br /&gt;&lt;b&gt;Valid Values:&lt;/b&gt; &lt;code&gt;0-10,000&lt;/code&gt;&lt;br /&gt;&lt;br /&gt;&lt;b&gt;Default:&lt;/b&gt; &lt;code&gt;0&lt;/code&gt; | [optional] 
 **q** | **String**| A query string that matches the keywords in name, mission statement, or description. | [optional] 
 **registrationIds** | **String**| A comma-separated list of charitable organization registration IDs.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note: &lt;/b&gt;Do not specify this parameter for query-based searches. Specify either the &lt;b&gt;q&lt;/b&gt; or &lt;b&gt;registration_ids&lt;/b&gt; parameter, but not both.&lt;/span&gt;&lt;br /&gt;&lt;br /&gt;&lt;b&gt;Maximum Limit:&lt;/b&gt; &lt;code&gt;20&lt;/code&gt; | [optional] 

### Return type

[**CharitySearchResponse**](CharitySearchResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

