# SellerServiceMetricsApi.SellerStandardsProfileApi

All URIs are relative to *https://api.ebay.com/sell/analytics/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**findSellerStandardsProfiles**](SellerStandardsProfileApi.md#findSellerStandardsProfiles) | **GET** /seller_standards_profile | 
[**getSellerStandardsProfile**](SellerStandardsProfileApi.md#getSellerStandardsProfile) | **GET** /seller_standards_profile/{program}/{cycle} | 



## findSellerStandardsProfiles

> FindSellerStandardsProfilesResponse findSellerStandardsProfiles()



This call retrieves all the standards profiles for the associated seller. A standards profile is a set of eBay seller metrics and the seller&#39;s associated compliance values (either TOP_RATED, ABOVE_STANDARD, or BELOW_STANDARD). A seller&#39;s multiple profiles are distinguished by two criteria, a &amp;quot;program&amp;quot; and a &amp;quot;cycle.&amp;quot; A profile&#39;s program is one of three regions where the seller may have done business, or PROGRAM_GLOBAL to indicate all marketplaces where the seller has done business. The cycle value specifies whether the standards compliance values were determined at the last official eBay evaluation or at the time of the request.

### Example

```javascript
import SellerServiceMetricsApi from '_seller_service_metrics_api_';
let defaultClient = SellerServiceMetricsApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: api_auth
let api_auth = defaultClient.authentications['api_auth'];
api_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SellerServiceMetricsApi.SellerStandardsProfileApi();
apiInstance.findSellerStandardsProfiles((error, data, response) => {
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

[**FindSellerStandardsProfilesResponse**](FindSellerStandardsProfilesResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSellerStandardsProfile

> StandardsProfile getSellerStandardsProfile(cycle, program)



This call retrieves a single standards profile for the associated seller. A standards profile is a set of eBay seller metrics and the seller&#39;s associated compliance values (either TOP_RATED, ABOVE_STANDARD, or BELOW_STANDARD). A seller can have multiple profiles distinguished by two criteria, a &amp;quot;program&amp;quot; and a &amp;quot;cycle.&amp;quot; A profile&#39;s program is one of three regions where the seller may have done business, or PROGRAM_GLOBAL to indicate all marketplaces where the seller has done business. The cycle value specifies whether the standards compliance values were determined at the last official eBay evaluation (CURRENT) or at the time of the request (PROJECTED). Both cycle and a program values are required URI parameters for this method.

### Example

```javascript
import SellerServiceMetricsApi from '_seller_service_metrics_api_';
let defaultClient = SellerServiceMetricsApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: api_auth
let api_auth = defaultClient.authentications['api_auth'];
api_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SellerServiceMetricsApi.SellerStandardsProfileApi();
let cycle = "cycle_example"; // String | The period covered by the returned standards profile evaluation. Supply one of two values, CURRENT means the response reflects eBay's most recent monthly standards evaluation and PROJECTED means the response reflect the seller's projected monthly evaluation, as calculated at the time of the request.
let program = "program_example"; // String | This input value specifies the region used to determine the seller's standards profile. Supply one of the four following values, PROGRAM_DE, PROGRAM_UK, PROGRAM_US, or PROGRAM_GLOBAL.
apiInstance.getSellerStandardsProfile(cycle, program, (error, data, response) => {
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
 **cycle** | **String**| The period covered by the returned standards profile evaluation. Supply one of two values, CURRENT means the response reflects eBay&#39;s most recent monthly standards evaluation and PROJECTED means the response reflect the seller&#39;s projected monthly evaluation, as calculated at the time of the request. | 
 **program** | **String**| This input value specifies the region used to determine the seller&#39;s standards profile. Supply one of the four following values, PROGRAM_DE, PROGRAM_UK, PROGRAM_US, or PROGRAM_GLOBAL. | 

### Return type

[**StandardsProfile**](StandardsProfile.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

