# AccountApi.CustomPolicyApi

All URIs are relative to *https://api.ebay.com/sell/account/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createCustomPolicy**](CustomPolicyApi.md#createCustomPolicy) | **POST** /custom_policy/ | 
[**getCustomPolicies**](CustomPolicyApi.md#getCustomPolicies) | **GET** /custom_policy/ | 
[**getCustomPolicy**](CustomPolicyApi.md#getCustomPolicy) | **GET** /custom_policy/{custom_policy_id} | 
[**updateCustomPolicy**](CustomPolicyApi.md#updateCustomPolicy) | **PUT** /custom_policy/{custom_policy_id} | 



## createCustomPolicy

> Object createCustomPolicy(X_EBAY_C_MARKETPLACE_ID, customPolicyCreateRequest)



This method creates a new custom policy in which a seller specifies their terms for complying with local governmental regulations. &lt;br/&gt;&lt;br/&gt;Two Custom Policy types are supported: &lt;ul&gt;&lt;li&gt;Product Compliance (PRODUCT_COMPLIANCE)&lt;/li&gt; &lt;li&gt;Takeback (TAKE_BACK)&lt;/li&gt;&lt;/ul&gt;Each Custom Policy targets a &lt;b&gt;policyType&lt;/b&gt; and &lt;b&gt;eBay marketplace&lt;/b&gt; combination. Multiple policies may be created as follows: &lt;ul&gt;&lt;li&gt;&lt;b&gt;Product Compliance&lt;/b&gt;: a maximum of 10 policies per eBay marketplace may be created&lt;/li&gt; &lt;li&gt;&lt;b&gt;Takeback&lt;/b&gt;: a maximum of 3 policies per eBay marketplace may be created&lt;/li&gt;&lt;/ul&gt;A successful create policy call returns an HTTP status code of &lt;b&gt;201 Created&lt;/b&gt; with the system-generated policy ID included in the &lt;b&gt;Location&lt;/b&gt; response header.&lt;br/&gt;&lt;br/&gt;&lt;b&gt;Product Compliance Policy&lt;/b&gt;&lt;br/&gt;&lt;br/&gt;Product Compliance policies disclose product information as required for regulatory compliance.&lt;br/&gt;&lt;br/&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt; A maximum of 10 Product Compliance policies per eBay marketplace may be created.&lt;/span&gt; &lt;br/&gt;&lt;br/&gt; &lt;b&gt;Takeback Policy&lt;/b&gt;&lt;br/&gt;&lt;br/&gt;Takeback policies describe the seller&#39;s legal obligation to take back a previously purchased item when the buyer purchases a new one.&lt;br/&gt;&lt;br/&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt; A maximum of 3 Takeback policies per eBay marketplace may be created.&lt;/span&gt;&lt;br/&gt;&lt;div class&#x3D;\&quot;msgbox_important\&quot;&gt;&lt;p class&#x3D;\&quot;msgbox_importantInDiv\&quot; data-mc-autonum&#x3D;\&quot;&amp;lt;b&amp;gt;&amp;lt;span style&#x3D;&amp;quot;color: #dd1e31;&amp;quot; class&#x3D;&amp;quot;mcFormatColor&amp;quot;&amp;gt;Important! &amp;lt;/span&amp;gt;&amp;lt;/b&amp;gt;\&quot;&gt;&lt;span class&#x3D;\&quot;autonumber\&quot;&gt;&lt;span&gt;&lt;b&gt;&lt;span style&#x3D;\&quot;color: #dd1e31;\&quot; class&#x3D;\&quot;mcFormatColor\&quot;&gt;Important!&lt;/span&gt;&lt;/b&gt;&lt;/span&gt;&lt;/span&gt;As a part of Digital Services Act (DSA) requirements, all custom policies will become global (and no longer marketplace-specific) on April 3, 2023. A seller will be able to apply any custom policy to listings on any eBay marketplace where they sell.&lt;br/&gt;&lt;br/&gt;Due to this change, the X-EBAY-C-MARKETPLACE-ID request header is no longer relevant. If this header is passed in after April 3, it will just be ignored in all four methods.&lt;/p&gt;&lt;/div&gt;

### Example

```javascript
import AccountApi from 'account_api';
let defaultClient = AccountApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: api_auth
let api_auth = defaultClient.authentications['api_auth'];
api_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AccountApi.CustomPolicyApi();
let X_EBAY_C_MARKETPLACE_ID = "X_EBAY_C_MARKETPLACE_ID_example"; // String | This header parameter specifies the eBay marketplace for the custom policy that is being created. Supported values for this header can be found in the <a href=\"/api-docs/sell/account/types/ba:MarketplaceIdEnum\" target=\"_blank\">MarketplaceIdEnum</a> type definition.<br/> <br/> <span class=\"tablenote\"><strong>Note:</strong> The following eBay marketplaces support Custom Policies: <ul><li>Germany (EBAY_DE)</li> <li>Canada (EBAY_CA)</li> <li>Australia (EBAY_AU)</li> <li>United States (EBAY_US)</li> <li>France (EBAY_FR)</li></ul></span><br/><div class=\"msgbox_important\"><p class=\"msgbox_importantInDiv\" data-mc-autonum=\"&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;\"><span class=\"autonumber\"><span><b><span style=\"color: #dd1e31;\" class=\"mcFormatColor\">Important!</span></b></span></span>As a part of Digital Services Act (DSA) requirements, all custom policies will become global (and no longer marketplace-specific) on April 3, 2023. A seller will be able to apply any custom policy to listings on any eBay marketplace where they sell.<br/><br/>Due to this change, the X-EBAY-C-MARKETPLACE-ID request header is no longer relevant. If this header is passed in after April 3, it will just be ignored in all four methods.</p></div>
let customPolicyCreateRequest = new AccountApi.CustomPolicyCreateRequest(); // CustomPolicyCreateRequest | Request to create a new Custom Policy.
apiInstance.createCustomPolicy(X_EBAY_C_MARKETPLACE_ID, customPolicyCreateRequest, (error, data, response) => {
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
 **X_EBAY_C_MARKETPLACE_ID** | **String**| This header parameter specifies the eBay marketplace for the custom policy that is being created. Supported values for this header can be found in the &lt;a href&#x3D;\&quot;/api-docs/sell/account/types/ba:MarketplaceIdEnum\&quot; target&#x3D;\&quot;_blank\&quot;&gt;MarketplaceIdEnum&lt;/a&gt; type definition.&lt;br/&gt; &lt;br/&gt; &lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt; The following eBay marketplaces support Custom Policies: &lt;ul&gt;&lt;li&gt;Germany (EBAY_DE)&lt;/li&gt; &lt;li&gt;Canada (EBAY_CA)&lt;/li&gt; &lt;li&gt;Australia (EBAY_AU)&lt;/li&gt; &lt;li&gt;United States (EBAY_US)&lt;/li&gt; &lt;li&gt;France (EBAY_FR)&lt;/li&gt;&lt;/ul&gt;&lt;/span&gt;&lt;br/&gt;&lt;div class&#x3D;\&quot;msgbox_important\&quot;&gt;&lt;p class&#x3D;\&quot;msgbox_importantInDiv\&quot; data-mc-autonum&#x3D;\&quot;&amp;lt;b&amp;gt;&amp;lt;span style&#x3D;&amp;quot;color: #dd1e31;&amp;quot; class&#x3D;&amp;quot;mcFormatColor&amp;quot;&amp;gt;Important! &amp;lt;/span&amp;gt;&amp;lt;/b&amp;gt;\&quot;&gt;&lt;span class&#x3D;\&quot;autonumber\&quot;&gt;&lt;span&gt;&lt;b&gt;&lt;span style&#x3D;\&quot;color: #dd1e31;\&quot; class&#x3D;\&quot;mcFormatColor\&quot;&gt;Important!&lt;/span&gt;&lt;/b&gt;&lt;/span&gt;&lt;/span&gt;As a part of Digital Services Act (DSA) requirements, all custom policies will become global (and no longer marketplace-specific) on April 3, 2023. A seller will be able to apply any custom policy to listings on any eBay marketplace where they sell.&lt;br/&gt;&lt;br/&gt;Due to this change, the X-EBAY-C-MARKETPLACE-ID request header is no longer relevant. If this header is passed in after April 3, it will just be ignored in all four methods.&lt;/p&gt;&lt;/div&gt; | 
 **customPolicyCreateRequest** | [**CustomPolicyCreateRequest**](CustomPolicyCreateRequest.md)| Request to create a new Custom Policy. | 

### Return type

**Object**

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getCustomPolicies

> CustomPolicyResponse getCustomPolicies(X_EBAY_C_MARKETPLACE_ID, opts)



This method retrieves the list of custom policies specified by the &lt;b&gt;policy_types&lt;/b&gt; query parameter for the selected eBay marketplace.&lt;br/&gt; &lt;br/&gt; &lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt; The following eBay marketplaces support Custom Policies: &lt;ul&gt;&lt;li&gt;Germany (EBAY_DE)&lt;/li&gt; &lt;li&gt;Canada (EBAY_CA)&lt;/li&gt; &lt;li&gt;Australia (EBAY_AU)&lt;/li&gt; &lt;li&gt;United States (EBAY_US)&lt;/li&gt; &lt;li&gt;France (EBAY_FR)&lt;/li&gt;&lt;/ul&gt;&lt;/span&gt;&lt;br/&gt;&lt;div class&#x3D;\&quot;msgbox_important\&quot;&gt;&lt;p class&#x3D;\&quot;msgbox_importantInDiv\&quot; data-mc-autonum&#x3D;\&quot;&amp;lt;b&amp;gt;&amp;lt;span style&#x3D;&amp;quot;color: #dd1e31;&amp;quot; class&#x3D;&amp;quot;mcFormatColor&amp;quot;&amp;gt;Important! &amp;lt;/span&amp;gt;&amp;lt;/b&amp;gt;\&quot;&gt;&lt;span class&#x3D;\&quot;autonumber\&quot;&gt;&lt;span&gt;&lt;b&gt;&lt;span style&#x3D;\&quot;color: #dd1e31;\&quot; class&#x3D;\&quot;mcFormatColor\&quot;&gt;Important!&lt;/span&gt;&lt;/b&gt;&lt;/span&gt;&lt;/span&gt;As a part of Digital Services Act (DSA) requirements, all custom policies will become global (and no longer marketplace-specific) on April 3, 2023. A seller will be able to apply any custom policy to listings on any eBay marketplace where they sell.&lt;br/&gt;&lt;br/&gt;Due to this change, the X-EBAY-C-MARKETPLACE-ID request header is no longer relevant. If this header is passed in after April 3, it will just be ignored in all four methods.&lt;/p&gt;&lt;/div&gt;&lt;br/&gt;&lt;br/&gt;For details on header values, see &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot; target&#x3D;\&quot;_blank\&quot;&gt;HTTP request headers&lt;/a&gt;.

### Example

```javascript
import AccountApi from 'account_api';
let defaultClient = AccountApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: api_auth
let api_auth = defaultClient.authentications['api_auth'];
api_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AccountApi.CustomPolicyApi();
let X_EBAY_C_MARKETPLACE_ID = "X_EBAY_C_MARKETPLACE_ID_example"; // String | This header parameter specifies the eBay marketplace for the custom policy that is being created. Supported values for this header can be found in the <a href=\"/api-docs/sell/account/types/ba:MarketplaceIdEnum\" target=\"_blank\">MarketplaceIdEnum</a> type definition.<br/> <br/> <span class=\"tablenote\"><strong>Note:</strong> The following eBay marketplaces support Custom Policies: <ul><li>Germany (EBAY_DE)</li> <li>Canada (EBAY_CA)</li> <li>Australia (EBAY_AU)</li> <li>United States (EBAY_US)</li> <li>France (EBAY_FR)</li></ul></span></br><div class=\"msgbox_important\"><p class=\"msgbox_importantInDiv\" data-mc-autonum=\"&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;\"><span class=\"autonumber\"><span><b><span style=\"color: #dd1e31;\" class=\"mcFormatColor\">Important!</span></b></span></span>As a part of Digital Services Act (DSA) requirements, all custom policies will become global (and no longer marketplace-specific) on April 3, 2023. A seller will be able to apply any custom policy to listings on any eBay marketplace where they sell.<br/><br/>Due to this change, the X-EBAY-C-MARKETPLACE-ID request header is no longer relevant. If this header is passed in after April 3, it will just be ignored in all four methods.</p></div>
let opts = {
  'policyTypes': "policyTypes_example" // String | This query parameter specifies the type of custom policies to be returned.<br /><br />Multiple policy types may be requested in a single call by providing a comma-delimited set of all policy types to be returned.<br/><br/><span class=\"tablenote\"><strong>Note:</strong> Omitting this query parameter from a request will also return policies of all policy types.</span><br/><br/>Two Custom Policy types are supported: <ul><li>Product Compliance (PRODUCT_COMPLIANCE)</li> <li>Takeback (TAKE_BACK)</li></ul>
};
apiInstance.getCustomPolicies(X_EBAY_C_MARKETPLACE_ID, opts, (error, data, response) => {
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
 **X_EBAY_C_MARKETPLACE_ID** | **String**| This header parameter specifies the eBay marketplace for the custom policy that is being created. Supported values for this header can be found in the &lt;a href&#x3D;\&quot;/api-docs/sell/account/types/ba:MarketplaceIdEnum\&quot; target&#x3D;\&quot;_blank\&quot;&gt;MarketplaceIdEnum&lt;/a&gt; type definition.&lt;br/&gt; &lt;br/&gt; &lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt; The following eBay marketplaces support Custom Policies: &lt;ul&gt;&lt;li&gt;Germany (EBAY_DE)&lt;/li&gt; &lt;li&gt;Canada (EBAY_CA)&lt;/li&gt; &lt;li&gt;Australia (EBAY_AU)&lt;/li&gt; &lt;li&gt;United States (EBAY_US)&lt;/li&gt; &lt;li&gt;France (EBAY_FR)&lt;/li&gt;&lt;/ul&gt;&lt;/span&gt;&lt;/br&gt;&lt;div class&#x3D;\&quot;msgbox_important\&quot;&gt;&lt;p class&#x3D;\&quot;msgbox_importantInDiv\&quot; data-mc-autonum&#x3D;\&quot;&amp;lt;b&amp;gt;&amp;lt;span style&#x3D;&amp;quot;color: #dd1e31;&amp;quot; class&#x3D;&amp;quot;mcFormatColor&amp;quot;&amp;gt;Important! &amp;lt;/span&amp;gt;&amp;lt;/b&amp;gt;\&quot;&gt;&lt;span class&#x3D;\&quot;autonumber\&quot;&gt;&lt;span&gt;&lt;b&gt;&lt;span style&#x3D;\&quot;color: #dd1e31;\&quot; class&#x3D;\&quot;mcFormatColor\&quot;&gt;Important!&lt;/span&gt;&lt;/b&gt;&lt;/span&gt;&lt;/span&gt;As a part of Digital Services Act (DSA) requirements, all custom policies will become global (and no longer marketplace-specific) on April 3, 2023. A seller will be able to apply any custom policy to listings on any eBay marketplace where they sell.&lt;br/&gt;&lt;br/&gt;Due to this change, the X-EBAY-C-MARKETPLACE-ID request header is no longer relevant. If this header is passed in after April 3, it will just be ignored in all four methods.&lt;/p&gt;&lt;/div&gt; | 
 **policyTypes** | **String**| This query parameter specifies the type of custom policies to be returned.&lt;br /&gt;&lt;br /&gt;Multiple policy types may be requested in a single call by providing a comma-delimited set of all policy types to be returned.&lt;br/&gt;&lt;br/&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt; Omitting this query parameter from a request will also return policies of all policy types.&lt;/span&gt;&lt;br/&gt;&lt;br/&gt;Two Custom Policy types are supported: &lt;ul&gt;&lt;li&gt;Product Compliance (PRODUCT_COMPLIANCE)&lt;/li&gt; &lt;li&gt;Takeback (TAKE_BACK)&lt;/li&gt;&lt;/ul&gt; | [optional] 

### Return type

[**CustomPolicyResponse**](CustomPolicyResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCustomPolicy

> CustomPolicy getCustomPolicy(customPolicyId, X_EBAY_C_MARKETPLACE_ID)



This method retrieves the custom policy specified by the &lt;b&gt;custom_policy_id&lt;/b&gt; path parameter for the selected eBay marketplace.&lt;br/&gt; &lt;br/&gt; &lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt; The following eBay marketplaces support Custom Policies: &lt;ul&gt;&lt;li&gt;Germany (EBAY_DE)&lt;/li&gt; &lt;li&gt;Canada (EBAY_CA)&lt;/li&gt; &lt;li&gt;Australia (EBAY_AU)&lt;/li&gt; &lt;li&gt;United States (EBAY_US)&lt;/li&gt; &lt;li&gt;France (EBAY_FR)&lt;/li&gt;&lt;/ul&gt;&lt;/span&gt;&lt;br/&gt;&lt;div class&#x3D;\&quot;msgbox_important\&quot;&gt;&lt;p class&#x3D;\&quot;msgbox_importantInDiv\&quot; data-mc-autonum&#x3D;\&quot;&amp;lt;b&amp;gt;&amp;lt;span style&#x3D;&amp;quot;color: #dd1e31;&amp;quot; class&#x3D;&amp;quot;mcFormatColor&amp;quot;&amp;gt;Important! &amp;lt;/span&amp;gt;&amp;lt;/b&amp;gt;\&quot;&gt;&lt;span class&#x3D;\&quot;autonumber\&quot;&gt;&lt;span&gt;&lt;b&gt;&lt;span style&#x3D;\&quot;color: #dd1e31;\&quot; class&#x3D;\&quot;mcFormatColor\&quot;&gt;Important!&lt;/span&gt;&lt;/b&gt;&lt;/span&gt;&lt;/span&gt;As a part of Digital Services Act (DSA) requirements, all custom policies will become global (and no longer marketplace-specific) on April 3, 2023. A seller will be able to apply any custom policy to listings on any eBay marketplace where they sell.&lt;br/&gt;&lt;br/&gt;Due to this change, the X-EBAY-C-MARKETPLACE-ID request header is no longer relevant. If this header is passed in after April 3, it will just be ignored in all four methods.&lt;/p&gt;&lt;/div&gt;&lt;br/&gt;&lt;br/&gt;For details on header values, see &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot; target&#x3D;\&quot;_blank\&quot;&gt;HTTP request headers&lt;/a&gt;.

### Example

```javascript
import AccountApi from 'account_api';
let defaultClient = AccountApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: api_auth
let api_auth = defaultClient.authentications['api_auth'];
api_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AccountApi.CustomPolicyApi();
let customPolicyId = "customPolicyId_example"; // String | This path parameter is the unique custom policy identifier for the policy to be returned.<br/><br/><span class=\"tablenote\"><strong>Note:</strong> This value is automatically assigned by the system when the policy is created.</span>
let X_EBAY_C_MARKETPLACE_ID = "X_EBAY_C_MARKETPLACE_ID_example"; // String | This header parameter specifies the eBay marketplace for the custom policy that is being created. Supported values for this header can be found in the <a href=\"/api-docs/sell/account/types/ba:MarketplaceIdEnum\" target=\"_blank\">MarketplaceIdEnum</a> type definition.<br/> <br/> <span class=\"tablenote\"><strong>Note:</strong> The following eBay marketplaces support Custom Policies: <ul><li>Germany (EBAY_DE)</li> <li>Canada (EBAY_CA)</li> <li>Australia (EBAY_AU)</li> <li>United States (EBAY_US)</li> <li>France (EBAY_FR)</li></ul></span><br/><div class=\"msgbox_important\"><p class=\"msgbox_importantInDiv\" data-mc-autonum=\"&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;\"><span class=\"autonumber\"><span><b><span style=\"color: #dd1e31;\" class=\"mcFormatColor\">Important!</span></b></span></span>As a part of Digital Services Act (DSA) requirements, all custom policies will become global (and no longer marketplace-specific) on April 3, 2023. A seller will be able to apply any custom policy to listings on any eBay marketplace where they sell.<br/><br/>Due to this change, the X-EBAY-C-MARKETPLACE-ID request header is no longer relevant. If this header is passed in after April 3, it will just be ignored in all four methods.</p></div>
apiInstance.getCustomPolicy(customPolicyId, X_EBAY_C_MARKETPLACE_ID, (error, data, response) => {
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
 **customPolicyId** | **String**| This path parameter is the unique custom policy identifier for the policy to be returned.&lt;br/&gt;&lt;br/&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt; This value is automatically assigned by the system when the policy is created.&lt;/span&gt; | 
 **X_EBAY_C_MARKETPLACE_ID** | **String**| This header parameter specifies the eBay marketplace for the custom policy that is being created. Supported values for this header can be found in the &lt;a href&#x3D;\&quot;/api-docs/sell/account/types/ba:MarketplaceIdEnum\&quot; target&#x3D;\&quot;_blank\&quot;&gt;MarketplaceIdEnum&lt;/a&gt; type definition.&lt;br/&gt; &lt;br/&gt; &lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt; The following eBay marketplaces support Custom Policies: &lt;ul&gt;&lt;li&gt;Germany (EBAY_DE)&lt;/li&gt; &lt;li&gt;Canada (EBAY_CA)&lt;/li&gt; &lt;li&gt;Australia (EBAY_AU)&lt;/li&gt; &lt;li&gt;United States (EBAY_US)&lt;/li&gt; &lt;li&gt;France (EBAY_FR)&lt;/li&gt;&lt;/ul&gt;&lt;/span&gt;&lt;br/&gt;&lt;div class&#x3D;\&quot;msgbox_important\&quot;&gt;&lt;p class&#x3D;\&quot;msgbox_importantInDiv\&quot; data-mc-autonum&#x3D;\&quot;&amp;lt;b&amp;gt;&amp;lt;span style&#x3D;&amp;quot;color: #dd1e31;&amp;quot; class&#x3D;&amp;quot;mcFormatColor&amp;quot;&amp;gt;Important! &amp;lt;/span&amp;gt;&amp;lt;/b&amp;gt;\&quot;&gt;&lt;span class&#x3D;\&quot;autonumber\&quot;&gt;&lt;span&gt;&lt;b&gt;&lt;span style&#x3D;\&quot;color: #dd1e31;\&quot; class&#x3D;\&quot;mcFormatColor\&quot;&gt;Important!&lt;/span&gt;&lt;/b&gt;&lt;/span&gt;&lt;/span&gt;As a part of Digital Services Act (DSA) requirements, all custom policies will become global (and no longer marketplace-specific) on April 3, 2023. A seller will be able to apply any custom policy to listings on any eBay marketplace where they sell.&lt;br/&gt;&lt;br/&gt;Due to this change, the X-EBAY-C-MARKETPLACE-ID request header is no longer relevant. If this header is passed in after April 3, it will just be ignored in all four methods.&lt;/p&gt;&lt;/div&gt; | 

### Return type

[**CustomPolicy**](CustomPolicy.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateCustomPolicy

> updateCustomPolicy(customPolicyId, X_EBAY_C_MARKETPLACE_ID, customPolicyRequest)



This method updates an existing custom policy specified by the &lt;b&gt;custom_policy_id&lt;/b&gt; path parameter for the selected marketplace. This method overwrites the policy&#39;s &lt;b&gt;Name&lt;/b&gt;, &lt;b&gt;Label&lt;/b&gt;, and &lt;b&gt;Description&lt;/b&gt; fields. Therefore, the complete, current text of all three policy fields must be included in the request payload even when one or two of these fields will not actually be updated.&lt;br/&gt; &lt;br/&gt;For example, the value for the &lt;b&gt;Label&lt;/b&gt; field is to be updated, but the &lt;b&gt;Name&lt;/b&gt; and &lt;b&gt;Description&lt;/b&gt; values will remain unchanged. The existing &lt;b&gt;Name&lt;/b&gt; and &lt;b&gt;Description&lt;/b&gt; values, as they are defined in the current policy, must also be passed in. &lt;br/&gt;&lt;br/&gt;A successful policy update call returns an HTTP status code of &lt;b&gt;204 No Content&lt;/b&gt;.&lt;br/&gt;&lt;br/&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt; The following eBay marketplaces support Custom Policies: &lt;ul&gt;&lt;li&gt;Germany (EBAY_DE)&lt;/li&gt; &lt;li&gt;Canada (EBAY_CA)&lt;/li&gt; &lt;li&gt;Australia (EBAY_AU)&lt;/li&gt; &lt;li&gt;United States (EBAY_US)&lt;/li&gt; &lt;li&gt;France (EBAY_FR)&lt;/li&gt;&lt;/ul&gt;&lt;/span&gt;&lt;br/&gt;&lt;div class&#x3D;\&quot;msgbox_important\&quot;&gt;&lt;p class&#x3D;\&quot;msgbox_importantInDiv\&quot; data-mc-autonum&#x3D;\&quot;&amp;lt;b&amp;gt;&amp;lt;span style&#x3D;&amp;quot;color: #dd1e31;&amp;quot; class&#x3D;&amp;quot;mcFormatColor&amp;quot;&amp;gt;Important! &amp;lt;/span&amp;gt;&amp;lt;/b&amp;gt;\&quot;&gt;&lt;span class&#x3D;\&quot;autonumber\&quot;&gt;&lt;span&gt;&lt;b&gt;&lt;span style&#x3D;\&quot;color: #dd1e31;\&quot; class&#x3D;\&quot;mcFormatColor\&quot;&gt;Important!&lt;/span&gt;&lt;/b&gt;&lt;/span&gt;&lt;/span&gt;As a part of Digital Services Act (DSA) requirements, all custom policies will become global (and no longer marketplace-specific) on April 3, 2023. A seller will be able to apply any custom policy to listings on any eBay marketplace where they sell.&lt;br/&gt;&lt;br/&gt;Due to this change, the X-EBAY-C-MARKETPLACE-ID request header is no longer relevant. If this header is passed in after April 3, it will just be ignored in all four methods.&lt;/p&gt;&lt;/div&gt;&lt;br/&gt;&lt;br/&gt;For details on header values, see &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot;&gt;HTTP request headers&lt;/a&gt;.

### Example

```javascript
import AccountApi from 'account_api';
let defaultClient = AccountApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: api_auth
let api_auth = defaultClient.authentications['api_auth'];
api_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AccountApi.CustomPolicyApi();
let customPolicyId = "customPolicyId_example"; // String | This path parameter is the unique custom policy identifier for the policy to be returned.<br/><br/><span class=\"tablenote\"><strong>Note:</strong> This value is automatically assigned by the system when the policy is created.</span>
let X_EBAY_C_MARKETPLACE_ID = "X_EBAY_C_MARKETPLACE_ID_example"; // String | This header parameter specifies the eBay marketplace for the custom policy that is being created. Supported values for this header can be found in the <a href=\"/api-docs/sell/account/types/ba:MarketplaceIdEnum\" target=\"_blank\">MarketplaceIdEnum</a> type definition.<br/> <br/> <span class=\"tablenote\"><strong>Note:</strong> The following eBay marketplaces support Custom Policies: <ul><li>Germany (EBAY_DE)</li> <li>Canada (EBAY_CA)</li> <li>Australia (EBAY_AU)</li> <li>United States (EBAY_US)</li> <li>France (EBAY_FR)</li></ul></span><br/><div class=\"msgbox_important\"><p class=\"msgbox_importantInDiv\" data-mc-autonum=\"&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;\"><span class=\"autonumber\"><span><b><span style=\"color: #dd1e31;\" class=\"mcFormatColor\">Important!</span></b></span></span>As a part of Digital Services Act (DSA) requirements, all custom policies will become global (and no longer marketplace-specific) on April 3, 2023. A seller will be able to apply any custom policy to listings on any eBay marketplace where they sell.<br/><br/>Due to this change, the X-EBAY-C-MARKETPLACE-ID request header is no longer relevant. If this header is passed in after April 3, it will just be ignored in all four methods.</p></div>
let customPolicyRequest = new AccountApi.CustomPolicyRequest(); // CustomPolicyRequest | Request to update a current custom policy.
apiInstance.updateCustomPolicy(customPolicyId, X_EBAY_C_MARKETPLACE_ID, customPolicyRequest, (error, data, response) => {
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
 **customPolicyId** | **String**| This path parameter is the unique custom policy identifier for the policy to be returned.&lt;br/&gt;&lt;br/&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt; This value is automatically assigned by the system when the policy is created.&lt;/span&gt; | 
 **X_EBAY_C_MARKETPLACE_ID** | **String**| This header parameter specifies the eBay marketplace for the custom policy that is being created. Supported values for this header can be found in the &lt;a href&#x3D;\&quot;/api-docs/sell/account/types/ba:MarketplaceIdEnum\&quot; target&#x3D;\&quot;_blank\&quot;&gt;MarketplaceIdEnum&lt;/a&gt; type definition.&lt;br/&gt; &lt;br/&gt; &lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt; The following eBay marketplaces support Custom Policies: &lt;ul&gt;&lt;li&gt;Germany (EBAY_DE)&lt;/li&gt; &lt;li&gt;Canada (EBAY_CA)&lt;/li&gt; &lt;li&gt;Australia (EBAY_AU)&lt;/li&gt; &lt;li&gt;United States (EBAY_US)&lt;/li&gt; &lt;li&gt;France (EBAY_FR)&lt;/li&gt;&lt;/ul&gt;&lt;/span&gt;&lt;br/&gt;&lt;div class&#x3D;\&quot;msgbox_important\&quot;&gt;&lt;p class&#x3D;\&quot;msgbox_importantInDiv\&quot; data-mc-autonum&#x3D;\&quot;&amp;lt;b&amp;gt;&amp;lt;span style&#x3D;&amp;quot;color: #dd1e31;&amp;quot; class&#x3D;&amp;quot;mcFormatColor&amp;quot;&amp;gt;Important! &amp;lt;/span&amp;gt;&amp;lt;/b&amp;gt;\&quot;&gt;&lt;span class&#x3D;\&quot;autonumber\&quot;&gt;&lt;span&gt;&lt;b&gt;&lt;span style&#x3D;\&quot;color: #dd1e31;\&quot; class&#x3D;\&quot;mcFormatColor\&quot;&gt;Important!&lt;/span&gt;&lt;/b&gt;&lt;/span&gt;&lt;/span&gt;As a part of Digital Services Act (DSA) requirements, all custom policies will become global (and no longer marketplace-specific) on April 3, 2023. A seller will be able to apply any custom policy to listings on any eBay marketplace where they sell.&lt;br/&gt;&lt;br/&gt;Due to this change, the X-EBAY-C-MARKETPLACE-ID request header is no longer relevant. If this header is passed in after April 3, it will just be ignored in all four methods.&lt;/p&gt;&lt;/div&gt; | 
 **customPolicyRequest** | [**CustomPolicyRequest**](CustomPolicyRequest.md)| Request to update a current custom policy. | 

### Return type

null (empty response body)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

