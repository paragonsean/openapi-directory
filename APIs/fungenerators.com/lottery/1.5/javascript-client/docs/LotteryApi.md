# RandomLotteryNumberGeneratorApi.LotteryApi

All URIs are relative to *https://api.fungenerators.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lotteryCountriesGet**](LotteryApi.md#lotteryCountriesGet) | **GET** /lottery/countries | 
[**lotteryDrawGet**](LotteryApi.md#lotteryDrawGet) | **GET** /lottery/draw | 
[**lotterySupportedGet**](LotteryApi.md#lotterySupportedGet) | **GET** /lottery/supported | 



## lotteryCountriesGet

> lotteryCountriesGet()



Get the complete list of countries supported in the number generation API.

### Example

```javascript
import RandomLotteryNumberGeneratorApi from 'random_lottery_number_generator_api';
let defaultClient = RandomLotteryNumberGeneratorApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new RandomLotteryNumberGeneratorApi.LotteryApi();
apiInstance.lotteryCountriesGet((error, data, response) => {
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

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## lotteryDrawGet

> lotteryDrawGet(game, opts)



Generate random draw for a given lottery game.

### Example

```javascript
import RandomLotteryNumberGeneratorApi from 'random_lottery_number_generator_api';
let defaultClient = RandomLotteryNumberGeneratorApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new RandomLotteryNumberGeneratorApi.LotteryApi();
let game = "game_example"; // String | Lottery Game Name
let opts = {
  'count': 56 // Number | Number of draws (max 5 per request)
};
apiInstance.lotteryDrawGet(game, opts, (error, data, response) => {
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
 **game** | **String**| Lottery Game Name | 
 **count** | **Number**| Number of draws (max 5 per request) | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## lotterySupportedGet

> lotterySupportedGet(country)



Get the list of supported lottery games supported in the given country.

### Example

```javascript
import RandomLotteryNumberGeneratorApi from 'random_lottery_number_generator_api';
let defaultClient = RandomLotteryNumberGeneratorApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new RandomLotteryNumberGeneratorApi.LotteryApi();
let country = "country_example"; // String | Country Name
apiInstance.lotterySupportedGet(country, (error, data, response) => {
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
 **country** | **String**| Country Name | 

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

