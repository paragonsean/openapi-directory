# ApiV1.DefaultApi

All URIs are relative to *http://change.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV1DonationsCarbonCalculateGet**](DefaultApi.md#apiV1DonationsCarbonCalculateGet) | **GET** /api/v1/donations/carbon_calculate | Calculate shipping carbon offset
[**apiV1DonationsCarbonStatsGet**](DefaultApi.md#apiV1DonationsCarbonStatsGet) | **GET** /api/v1/donations/carbon_stats | Retrieve carbon offset stats
[**apiV1DonationsCreatePost**](DefaultApi.md#apiV1DonationsCreatePost) | **POST** /api/v1/donations/create | Create a donation
[**apiV1DonationsCryptoCalculateGet**](DefaultApi.md#apiV1DonationsCryptoCalculateGet) | **GET** /api/v1/donations/crypto_calculate | Calculate crypto carbon offset
[**apiV1DonationsIndexGet**](DefaultApi.md#apiV1DonationsIndexGet) | **GET** /api/v1/donations/index | List your donations
[**apiV1DonationsShowGet**](DefaultApi.md#apiV1DonationsShowGet) | **GET** /api/v1/donations/show | Retrieve a donation
[**apiV1NonprofitsListGet**](DefaultApi.md#apiV1NonprofitsListGet) | **GET** /api/v1/nonprofits/list | Search a nonprofit
[**apiV1NonprofitsShowGet**](DefaultApi.md#apiV1NonprofitsShowGet) | **GET** /api/v1/nonprofits/show | Show a nonprofit



## apiV1DonationsCarbonCalculateGet

> apiV1DonationsCarbonCalculateGet(weightLb, opts)

Calculate shipping carbon offset

Calculates the donation amount (to CarbonFund 501\\(c\\)3) needed to offset a physical shipment. This calculation depends on the weight, primary transportation method, and distance of the shipment. Provide the distance of the shipment using the origin and destination address, or directly with the number of miles. For convenience, this endpoint also returns the id of the nonprofit CarbonFund, for making a subsequent donation to. See the [Carbon offsets guide](/recipes/carbon-offsets/) for more on using this endpoint.

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure HTTP basic authorization: basic_auth
let basic_auth = defaultClient.authentications['basic_auth'];
basic_auth.username = 'YOUR USERNAME';
basic_auth.password = 'YOUR PASSWORD';

let apiInstance = new ApiV1.DefaultApi();
let weightLb = 3.5; // Number | The total weight (in pounds) of the shipment.
let opts = {
  'originAddress': 60148, // Number | The origin zip code (US only) of the shipment. If you send this parameter, also send `destination_address`.
  'destinationAddress': 94133, // Number | The destination zip code (US only) of the shipment. If you send this parameter, also send `origin_address`.
  'distanceMi': 3.4, // Number | The total distance (in miles) of the shipment. You can use this parameter in place of `origin_address` and `destination_address`.
  'transportationMethod': "air" // String | The primary transportation method of the shipment.
};
apiInstance.apiV1DonationsCarbonCalculateGet(weightLb, opts, (error, data, response) => {
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
 **weightLb** | **Number**| The total weight (in pounds) of the shipment. | 
 **originAddress** | **Number**| The origin zip code (US only) of the shipment. If you send this parameter, also send &#x60;destination_address&#x60;. | [optional] 
 **destinationAddress** | **Number**| The destination zip code (US only) of the shipment. If you send this parameter, also send &#x60;origin_address&#x60;. | [optional] 
 **distanceMi** | **Number**| The total distance (in miles) of the shipment. You can use this parameter in place of &#x60;origin_address&#x60; and &#x60;destination_address&#x60;. | [optional] 
 **transportationMethod** | **String**| The primary transportation method of the shipment. | [optional] 

### Return type

null (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV1DonationsCarbonStatsGet

> apiV1DonationsCarbonStatsGet(opts)

Retrieve carbon offset stats

Measures your carbon offset impact in relatable terms. Provide the id of a donation to CarbonFund to see stats about that specific donation. If you omit the donation id, this endpoint returns aggregate stats for all of your CarbonFund donations.

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure HTTP basic authorization: basic_auth
let basic_auth = defaultClient.authentications['basic_auth'];
basic_auth.username = 'YOUR USERNAME';
basic_auth.password = 'YOUR PASSWORD';

let apiInstance = new ApiV1.DefaultApi();
let opts = {
  'id': d_NuYL6M2C1kjecXpWzKVODw7W // Number | The id of a donation to the CarbonFund nonprofit. Ids are returned when a donation is created. If an ID is not provided, the total stats for all donations to CarbonFund are returned.
};
apiInstance.apiV1DonationsCarbonStatsGet(opts, (error, data, response) => {
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
 **id** | **Number**| The id of a donation to the CarbonFund nonprofit. Ids are returned when a donation is created. If an ID is not provided, the total stats for all donations to CarbonFund are returned. | [optional] 

### Return type

null (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV1DonationsCreatePost

> apiV1DonationsCreatePost(amount, nonprofitId, fundingSource, opts)

Create a donation

Creates a donation to any nonprofit. CHANGE keeps track of your donations, bills you at the end of the month, and handles the nonprofit payouts for you.

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure HTTP basic authorization: basic_auth
let basic_auth = defaultClient.authentications['basic_auth'];
basic_auth.username = 'YOUR USERNAME';
basic_auth.password = 'YOUR PASSWORD';

let apiInstance = new ApiV1.DefaultApi();
let amount = "500"; // String | The amount of the donation in cents.
let nonprofitId = "n_IfEoPCaPqVsFAUI5xl0CBUOx"; // String | The id of a nonprofit from the CHANGE network.
let fundingSource = "customer"; // String | Source of the donation funds. If you are collecting payment from your customer for the donation, use `customer`.
let opts = {
  'zipCode': "94104" // String | The customer's zip code. Provide this to unlock geographic insights.
};
apiInstance.apiV1DonationsCreatePost(amount, nonprofitId, fundingSource, opts, (error, data, response) => {
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
 **amount** | **String**| The amount of the donation in cents. | 
 **nonprofitId** | **String**| The id of a nonprofit from the CHANGE network. | 
 **fundingSource** | **String**| Source of the donation funds. If you are collecting payment from your customer for the donation, use &#x60;customer&#x60;. | 
 **zipCode** | **String**| The customer&#39;s zip code. Provide this to unlock geographic insights. | [optional] 

### Return type

null (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV1DonationsCryptoCalculateGet

> apiV1DonationsCryptoCalculateGet(currency, opts)

Calculate crypto carbon offset

Calculates the donation amount (to CarbonFund 501\\(c\\)3) needed to offset a cryptocurrency transaction. For convenience, this endpoint also returns the id of the nonprofit CarbonFund, for making a subsequent donation to. See the [Carbon offsets guide](/recipes/carbon-offsets/) for more on using this endpoint.

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure HTTP basic authorization: basic_auth
let basic_auth = defaultClient.authentications['basic_auth'];
basic_auth.username = 'YOUR USERNAME';
basic_auth.password = 'YOUR PASSWORD';

let apiInstance = new ApiV1.DefaultApi();
let currency = "eth"; // String | The currency of the transaction.
let opts = {
  'count': 2 // Number | The number of transactions to offset.
};
apiInstance.apiV1DonationsCryptoCalculateGet(currency, opts, (error, data, response) => {
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
 **currency** | **String**| The currency of the transaction. | 
 **count** | **Number**| The number of transactions to offset. | [optional] 

### Return type

null (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV1DonationsIndexGet

> apiV1DonationsIndexGet(opts)

List your donations

Retrieves a list of donations you&#39;ve previously made. The donations are returned in order of creation, with the most recent donations appearing first. This endpoint is paginated.

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure HTTP basic authorization: basic_auth
let basic_auth = defaultClient.authentications['basic_auth'];
basic_auth.username = 'YOUR USERNAME';
basic_auth.password = 'YOUR PASSWORD';

let apiInstance = new ApiV1.DefaultApi();
let opts = {
  'page': 1 // Number | Which page to return. This endpoint is paginated, and returns maximum 30 donations per page.
};
apiInstance.apiV1DonationsIndexGet(opts, (error, data, response) => {
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
 **page** | **Number**| Which page to return. This endpoint is paginated, and returns maximum 30 donations per page. | [optional] 

### Return type

null (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV1DonationsShowGet

> apiV1DonationsShowGet(id)

Retrieve a donation

Retrieves the details of a donation you&#39;ve previously made.

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure HTTP basic authorization: basic_auth
let basic_auth = defaultClient.authentications['basic_auth'];
basic_auth.username = 'YOUR USERNAME';
basic_auth.password = 'YOUR PASSWORD';

let apiInstance = new ApiV1.DefaultApi();
let id = "d_NuYL6M2C1kjecXpWzKVODw7W"; // String | The id of a donation. Ids are returned when a donation is created.
apiInstance.apiV1DonationsShowGet(id, (error, data, response) => {
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
 **id** | **String**| The id of a donation. Ids are returned when a donation is created. | 

### Return type

null (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV1NonprofitsListGet

> apiV1NonprofitsListGet(opts)

Search a nonprofit

Retrieves a list of nonprofits whose names match the provided name. This endpoint is paginated.

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure HTTP basic authorization: basic_auth
let basic_auth = defaultClient.authentications['basic_auth'];
basic_auth.username = 'YOUR USERNAME';
basic_auth.password = 'YOUR PASSWORD';

let apiInstance = new ApiV1.DefaultApi();
let opts = {
  'name': "Some Nonprofit", // String | A string to search.
  'page': 1 // Number | The page to return. This endpoint is paginated, and returns up to 30 nonprofits at a time.
};
apiInstance.apiV1NonprofitsListGet(opts, (error, data, response) => {
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
 **name** | **String**| A string to search. | [optional] 
 **page** | **Number**| The page to return. This endpoint is paginated, and returns up to 30 nonprofits at a time. | [optional] 

### Return type

null (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV1NonprofitsShowGet

> apiV1NonprofitsShowGet(id)

Show a nonprofit

Retrieves information for a nonprofit.

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure HTTP basic authorization: basic_auth
let basic_auth = defaultClient.authentications['basic_auth'];
basic_auth.username = 'YOUR USERNAME';
basic_auth.password = 'YOUR PASSWORD';

let apiInstance = new ApiV1.DefaultApi();
let id = "n_IfEoPCaPqVsFAUI5xl0CBUOx"; // String | The id of a nonprofit from the CHANGE network.
apiInstance.apiV1NonprofitsShowGet(id, (error, data, response) => {
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
 **id** | **String**| The id of a nonprofit from the CHANGE network. | 

### Return type

null (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

