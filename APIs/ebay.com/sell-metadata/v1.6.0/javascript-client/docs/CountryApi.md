# MetadataApi.CountryApi

All URIs are relative to *https://api.ebay.com/sell/metadata/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSalesTaxJurisdictions**](CountryApi.md#getSalesTaxJurisdictions) | **GET** /country/{countryCode}/sales_tax_jurisdiction | 



## getSalesTaxJurisdictions

> SalesTaxJurisdictions getSalesTaxJurisdictions(countryCode)



This method retrieves all the sales tax jurisdictions for the country that you specify in the &lt;b&gt;countryCode&lt;/b&gt; path parameter. Countries with valid sales tax jurisdictions are Canada and the US.  &lt;br/&gt;&lt;br/&gt;The response from this call tells you the jurisdictions for which a seller can configure tax tables. Although setting up tax tables is optional, you can use the &lt;b&gt;createOrReplaceSalesTax&lt;/b&gt; in the &lt;b&gt;Account API&lt;/b&gt; call to configure the tax tables for the jurisdictions you sell to.

### Example

```javascript
import MetadataApi from 'metadata_api';
let defaultClient = MetadataApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: api_auth
let api_auth = defaultClient.authentications['api_auth'];
api_auth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: api_auth
let api_auth = defaultClient.authentications['api_auth'];
api_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MetadataApi.CountryApi();
let countryCode = "countryCode_example"; // String | This path parameter specifies the two-letter <a href=\"https://www.iso.org/iso-3166-country-codes.html \" title=\"https://www.iso.org \" target=\"_blank\">ISO 3166</a> country code for the country whose jurisdictions you want to retrieve. eBay provides sales tax jurisdiction information for Canada and the United States.Valid values for this path parameter are <code>CA</code> and <code>US</code>.
apiInstance.getSalesTaxJurisdictions(countryCode, (error, data, response) => {
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
 **countryCode** | **String**| This path parameter specifies the two-letter &lt;a href&#x3D;\&quot;https://www.iso.org/iso-3166-country-codes.html \&quot; title&#x3D;\&quot;https://www.iso.org \&quot; target&#x3D;\&quot;_blank\&quot;&gt;ISO 3166&lt;/a&gt; country code for the country whose jurisdictions you want to retrieve. eBay provides sales tax jurisdiction information for Canada and the United States.Valid values for this path parameter are &lt;code&gt;CA&lt;/code&gt; and &lt;code&gt;US&lt;/code&gt;. | 

### Return type

[**SalesTaxJurisdictions**](SalesTaxJurisdictions.md)

### Authorization

[api_auth](../README.md#api_auth), [api_auth](../README.md#api_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

