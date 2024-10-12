# SelfServiceDeveloperApi.DefaultApi

All URIs are relative to *https://api.peoplefinderspro.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addressAutocompletePost**](DefaultApi.md#addressAutocompletePost) | **POST** /address/autocomplete | Search
[**contactEnrichPost**](DefaultApi.md#contactEnrichPost) | **POST** /contact/enrich | Search
[**emailEnrichPost**](DefaultApi.md#emailEnrichPost) | **POST** /email/enrich | Search
[**phoneEnrichPost**](DefaultApi.md#phoneEnrichPost) | **POST** /phone/enrich | Search
[**search**](DefaultApi.md#search) | **POST** /identity/verify_id | Search



## addressAutocompletePost

> addressAutocompletePost(opts)

Search

###### *Click on the grey search box above, to view sample request/response objects for Address Autocomplete Search*  Perform a search:  1. Add your key and key secret to the request headers.     + galaxy-ap-name: [Key]     + galaxy-ap-password: [Secret]     + galaxy-search-type: DevAPIAddressAutoComplete  2.  Add search criteria to your request.     ~~~html             {                 \&quot;Input\&quot;:\&quot;1821 Q\&quot;             }     ~~~  3.  Submit your search  The JSON request should have parts of the address.  + &lt;code&gt;Input&lt;/code&gt; &#x3D; null (optional, string) ... address.

### Example

```javascript
import SelfServiceDeveloperApi from 'self_service_developer_api';

let apiInstance = new SelfServiceDeveloperApi.DefaultApi();
let opts = {
  'galaxyApName': "Key", // String | e.g. Key
  'galaxyApPassword': "Secret", // String | e.g. Secret
  'galaxySearchType': "DevAPIAddressAutoComplete", // String | e.g. DevAPIAddressAutoComplete
  'addressAutocompletePostRequest': new SelfServiceDeveloperApi.AddressAutocompletePostRequest() // AddressAutocompletePostRequest | 
};
apiInstance.addressAutocompletePost(opts, (error, data, response) => {
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
 **galaxyApName** | **String**| e.g. Key | [optional] 
 **galaxyApPassword** | **String**| e.g. Secret | [optional] 
 **galaxySearchType** | **String**| e.g. DevAPIAddressAutoComplete | [optional] 
 **addressAutocompletePostRequest** | [**AddressAutocompletePostRequest**](AddressAutocompletePostRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## contactEnrichPost

> contactEnrichPost(opts)

Search

###### *Click on the grey search box above, to view sample request/response objects for Contact Enrichment Search*  Perform a search:  1. Add your key and key secret to the request headers.     + galaxy-ap-name: [Key]     + galaxy-ap-password: [Secret]     + galaxy-search-type: DevAPIContactEnrich  2.  Add search criteria to your request. At least two are required: Name, Phone, Address, or Email.     ~~~html             {                 \&quot;FirstName\&quot;: \&quot;John\&quot;,                 \&quot;MiddleName\&quot;: \&quot;T\&quot;,                 \&quot;LastName\&quot;: \&quot;Lawrence\&quot;,                 \&quot;Dob\&quot;:\&quot;\&quot;,                 \&quot;Age\&quot;: 0,                 \&quot;Address\&quot;: {                     \&quot;addressLine1\&quot;:\&quot;123 Q Street\&quot;,                     \&quot;addressLine2\&quot;:\&quot;Sacramento, CA\&quot;                 },                 \&quot;PhoneNumber\&quot;:\&quot;\&quot;,                 \&quot;Email\&quot;:\&quot;\&quot;             }     ~~~  3.  Submit your search  A complete list of JSON request properties follows.  + &lt;code&gt;FirstName&lt;/code&gt;&#x3D; null (optional, string) ... First name.  + &lt;code&gt;MiddleName&lt;/code&gt; &#x3D; null (optional, string) ... Middle name or middle initial.  + &lt;code&gt;LastName&lt;/code&gt; &#x3D; null (optional, string) ... Last name.  + &lt;code&gt;Dob&lt;/code&gt; &#x3D; null (optional, string) ... Date of birth (format: MM/DD/YYYY).  + &lt;code&gt;Age&lt;/code&gt; &#x3D; null (optional, int) ... Age.  + &lt;code&gt;Addresses&lt;/code&gt; &#x3D; null (optional, Addresses[]) ... List of addresses.     + &lt;code&gt;Members&lt;/code&gt;         + &lt;code&gt;AddressLine1&lt;/code&gt; &#x3D; null (optional, string) ... House number, street name and Unit number (i.e. 123 Q Street, Unit 102) or PO Box (i.e. 1821 Q Street).         + &lt;code&gt;AddressLine2&lt;/code&gt; &#x3D; null (optional, string) ... State or City and State or Zip (i.e. Sacramento, CA).  + &lt;code&gt;Phone&lt;/code&gt; &#x3D; null (optional, string) ... Phone number (formats: ###-###-####, (###) ###-####).  + &lt;code&gt;Email&lt;/code&gt; &#x3D; null (optional, string) ... E-mail address.

### Example

```javascript
import SelfServiceDeveloperApi from 'self_service_developer_api';

let apiInstance = new SelfServiceDeveloperApi.DefaultApi();
let opts = {
  'galaxyApName': "Key", // String | e.g. Key
  'galaxyApPassword': "Secret", // String | e.g. Secret
  'galaxySearchType': "DevAPIContactEnrich", // String | e.g. DevAPIContactEnrich
  'contactEnrichPostRequest': new SelfServiceDeveloperApi.ContactEnrichPostRequest() // ContactEnrichPostRequest | 
};
apiInstance.contactEnrichPost(opts, (error, data, response) => {
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
 **galaxyApName** | **String**| e.g. Key | [optional] 
 **galaxyApPassword** | **String**| e.g. Secret | [optional] 
 **galaxySearchType** | **String**| e.g. DevAPIContactEnrich | [optional] 
 **contactEnrichPostRequest** | [**ContactEnrichPostRequest**](ContactEnrichPostRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## emailEnrichPost

> emailEnrichPost(opts)

Search

###### *Click on the grey search box above, to view sample request/response objects for Email Enrichment Search*  Perform a search:  1. Add your Access Profile username and password to the request headers.     + galaxy-ap-name: [Key]     + galaxy-ap-password: [Secret]     + galaxy-search-type: DevAPIEmailID  2.  Add search criteria to your request.     ~~~html             {                 \&quot;Email\&quot;:\&quot;johnsmith@somedomain\&quot;             }     ~~~  3.  Submit your search  The JSON request should have an email.  + &lt;code&gt;Email&lt;/code&gt; &#x3D; null (optional, string) ... E-mail address.

### Example

```javascript
import SelfServiceDeveloperApi from 'self_service_developer_api';

let apiInstance = new SelfServiceDeveloperApi.DefaultApi();
let opts = {
  'galaxyApName': "Key", // String | e.g. Key
  'galaxyApPassword': "Secret", // String | e.g. Secret
  'galaxySearchType': "DevAPIEmailID", // String | e.g. DevAPIEmailID
  'emailEnrichPostRequest': new SelfServiceDeveloperApi.EmailEnrichPostRequest() // EmailEnrichPostRequest | 
};
apiInstance.emailEnrichPost(opts, (error, data, response) => {
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
 **galaxyApName** | **String**| e.g. Key | [optional] 
 **galaxyApPassword** | **String**| e.g. Secret | [optional] 
 **galaxySearchType** | **String**| e.g. DevAPIEmailID | [optional] 
 **emailEnrichPostRequest** | [**EmailEnrichPostRequest**](EmailEnrichPostRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## phoneEnrichPost

> phoneEnrichPost(opts)

Search

###### *Click on the grey search box above, to view sample request/response objects for Phone Enrichment Search*  Perform a search:  1. Add your key and key secret to the request headers.     + galaxy-ap-name: [Key]     + galaxy-ap-password: [Secret]     + galaxy-search-type: DevAPICallerID  2.  Add search criteria to your request.     ~~~html             {                 \&quot;Phone\&quot;:\&quot;(123) 456-7890\&quot;             }     ~~~  3.  Submit your search  The JSON request should have a phone number.  + &lt;code&gt;Phone&lt;/code&gt; &#x3D; null (optional, string) ... Phone number (formats: ###-###-####, (###) ###-####).

### Example

```javascript
import SelfServiceDeveloperApi from 'self_service_developer_api';

let apiInstance = new SelfServiceDeveloperApi.DefaultApi();
let opts = {
  'galaxyApName': "Key", // String | e.g. Key
  'galaxyApPassword': "Secret", // String | e.g. Secret
  'galaxySearchType': "DevAPICallerID", // String | e.g. DevAPICallerID
  'phoneEnrichPostRequest': new SelfServiceDeveloperApi.PhoneEnrichPostRequest() // PhoneEnrichPostRequest | 
};
apiInstance.phoneEnrichPost(opts, (error, data, response) => {
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
 **galaxyApName** | **String**| e.g. Key | [optional] 
 **galaxyApPassword** | **String**| e.g. Secret | [optional] 
 **galaxySearchType** | **String**| e.g. DevAPICallerID | [optional] 
 **phoneEnrichPostRequest** | [**PhoneEnrichPostRequest**](PhoneEnrichPostRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## search

> search(opts)

Search

###### *Click on the grey search box above, to view sample request/response objects for the Identity Verification Search*  Perform a search:  1. Add your key and key secret to the request headers.     + galaxy-ap-name: [Key]     + galaxy-ap-password: [Secret]     + galaxy-search-type: DevAPIIDVerification  2.  Add search criteria to your request. At least two are required: SSN, Name, Phone, Address or Email.     ~~~html             {                 \&quot;FirstName\&quot;: \&quot;John\&quot;,                 \&quot;MiddleName\&quot;: \&quot;T\&quot;,                 \&quot;LastName\&quot;: \&quot;Lawrence\&quot;,                 \&quot;Dob\&quot;:\&quot;\&quot;,                 \&quot;Age\&quot;: 0,                 \&quot;Address\&quot;: {                     \&quot;addressLine1\&quot;:\&quot;123 Q Street, Unit 102\&quot;,                     \&quot;addressLine2\&quot;:\&quot;Sacramento, CA\&quot;                 },                 \&quot;PhoneNumber\&quot;:\&quot;\&quot;,                 \&quot;Email\&quot;:\&quot;\&quot;             }     ~~~  3.  Submit your search  A complete list of JSON request properties follows.  + &lt;code&gt;FirstName&lt;/code&gt;&#x3D; null (optional, string) ... First name.  + &lt;code&gt;MiddleName&lt;/code&gt; &#x3D; null (optional, string) ... Middle name or middle initial.  + &lt;code&gt;LastName&lt;/code&gt; &#x3D; null (optional, string) ... Last name.  + &lt;code&gt;Dob&lt;/code&gt; &#x3D; null (optional, string) ... Date of birth (format: MM/DD/YYYY).  + &lt;code&gt;Age&lt;/code&gt; &#x3D; null (optional, int) ... Age.  + &lt;code&gt;Addresses&lt;/code&gt; &#x3D; null (optional, Addresses[]) ... List of addresses.     + &lt;code&gt;Members&lt;/code&gt;         + &lt;code&gt;AddressLine1&lt;/code&gt; &#x3D; null (optional, string) ... House number, street name and Unit number (i.e. 123 Q Street, Unit 102) or PO Box (i.e. 1821 Q Street).         + &lt;code&gt;AddressLine2&lt;/code&gt; &#x3D; null (optional, string) ... State or City and State or Zip (i.e. Sacramento, CA).  + &lt;code&gt;Phone&lt;/code&gt; &#x3D; null (optional, string) ... Phone number (formats: ###-###-####, (###) ###-####).  + &lt;code&gt;Email&lt;/code&gt; &#x3D; null (optional, string) ... E-mail address.

### Example

```javascript
import SelfServiceDeveloperApi from 'self_service_developer_api';

let apiInstance = new SelfServiceDeveloperApi.DefaultApi();
let opts = {
  'galaxyApName': "Key", // String | e.g. Key
  'galaxyApPassword': "Secret", // String | e.g. Secret
  'galaxySearchType': "DevAPIIDVerification", // String | e.g. DevAPIIDVerification
  'contactEnrichPostRequest': new SelfServiceDeveloperApi.ContactEnrichPostRequest() // ContactEnrichPostRequest | 
};
apiInstance.search(opts, (error, data, response) => {
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
 **galaxyApName** | **String**| e.g. Key | [optional] 
 **galaxyApPassword** | **String**| e.g. Secret | [optional] 
 **galaxySearchType** | **String**| e.g. DevAPIIDVerification | [optional] 
 **contactEnrichPostRequest** | [**ContactEnrichPostRequest**](ContactEnrichPostRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

