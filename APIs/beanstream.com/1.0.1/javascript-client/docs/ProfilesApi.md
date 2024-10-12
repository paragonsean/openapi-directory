# BeanstreamPayments.ProfilesApi

All URIs are relative to *https://www.beanstream.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**profilesPost**](ProfilesApi.md#profilesPost) | **POST** /profiles | Create Profile
[**profilesProfileIdCardsCardIdDelete**](ProfilesApi.md#profilesProfileIdCardsCardIdDelete) | **DELETE** /profiles/{profileId}/cards/{cardId} | Delete card
[**profilesProfileIdCardsCardIdPut**](ProfilesApi.md#profilesProfileIdCardsCardIdPut) | **PUT** /profiles/{profileId}/cards/{cardId} | Update card
[**profilesProfileIdCardsGet**](ProfilesApi.md#profilesProfileIdCardsGet) | **GET** /profiles/{profileId}/cards | Get cards
[**profilesProfileIdCardsPost**](ProfilesApi.md#profilesProfileIdCardsPost) | **POST** /profiles/{profileId}/cards | Add card
[**profilesProfileIdDelete**](ProfilesApi.md#profilesProfileIdDelete) | **DELETE** /profiles/{profileId} | Delete profile
[**profilesProfileIdGet**](ProfilesApi.md#profilesProfileIdGet) | **GET** /profiles/{profileId} | Get profile
[**profilesProfileIdPut**](ProfilesApi.md#profilesProfileIdPut) | **PUT** /profiles/{profileId} | Update Profile



## profilesPost

> ProfileResponse profilesPost(createProfileBody)

Create Profile

Create a new Payment Profile using either a card or a Legato token. You must supply one of them.

### Example

```javascript
import BeanstreamPayments from 'beanstream_payments';

let apiInstance = new BeanstreamPayments.ProfilesApi();
let createProfileBody = new BeanstreamPayments.CreateProfileBody(); // CreateProfileBody | 
apiInstance.profilesPost(createProfileBody, (error, data, response) => {
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
 **createProfileBody** | [**CreateProfileBody**](CreateProfileBody.md)|  | 

### Return type

[**ProfileResponse**](ProfileResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## profilesProfileIdCardsCardIdDelete

> ProfileResponse profilesProfileIdCardsCardIdDelete(profileId, cardId)

Delete card

Delete a card on the profile.

### Example

```javascript
import BeanstreamPayments from 'beanstream_payments';

let apiInstance = new BeanstreamPayments.ProfilesApi();
let profileId = "profileId_example"; // String | The profile id. (aka CustomerCode)
let cardId = 3.4; // Number | The card id.
apiInstance.profilesProfileIdCardsCardIdDelete(profileId, cardId, (error, data, response) => {
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
 **profileId** | **String**| The profile id. (aka CustomerCode) | 
 **cardId** | **Number**| The card id. | 

### Return type

[**ProfileResponse**](ProfileResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## profilesProfileIdCardsCardIdPut

> ProfileResponse profilesProfileIdCardsCardIdPut(profileId, cardId, card)

Update card

Update the details of a card on the profile.

### Example

```javascript
import BeanstreamPayments from 'beanstream_payments';

let apiInstance = new BeanstreamPayments.ProfilesApi();
let profileId = "profileId_example"; // String | The profile id. (aka CustomerCode)
let cardId = 3.4; // Number | The card id.
let card = new BeanstreamPayments.ProfileCard(); // ProfileCard | The card that will be updated on the profile.
apiInstance.profilesProfileIdCardsCardIdPut(profileId, cardId, card, (error, data, response) => {
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
 **profileId** | **String**| The profile id. (aka CustomerCode) | 
 **cardId** | **Number**| The card id. | 
 **card** | [**ProfileCard**](ProfileCard.md)| The card that will be updated on the profile. | 

### Return type

[**ProfileResponse**](ProfileResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## profilesProfileIdCardsGet

> ProfileGetCards profilesProfileIdCardsGet(profileId)

Get cards

Get all of the cards on the profile.

### Example

```javascript
import BeanstreamPayments from 'beanstream_payments';

let apiInstance = new BeanstreamPayments.ProfilesApi();
let profileId = "profileId_example"; // String | The profile id. (aka CustomerCode)
apiInstance.profilesProfileIdCardsGet(profileId, (error, data, response) => {
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
 **profileId** | **String**| The profile id. (aka CustomerCode) | 

### Return type

[**ProfileGetCards**](ProfileGetCards.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## profilesProfileIdCardsPost

> ProfileResponse profilesProfileIdCardsPost(profileId, card)

Add card

Add a card to the profile. Note that there is a default limit of 1 card per profile. You can change this in your Profiles settings in the back office.

### Example

```javascript
import BeanstreamPayments from 'beanstream_payments';

let apiInstance = new BeanstreamPayments.ProfilesApi();
let profileId = "profileId_example"; // String | The profile id. (aka CustomerCode)
let card = new BeanstreamPayments.ProfileCard(); // ProfileCard | The card that will be added to the profile.
apiInstance.profilesProfileIdCardsPost(profileId, card, (error, data, response) => {
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
 **profileId** | **String**| The profile id. (aka CustomerCode) | 
 **card** | [**ProfileCard**](ProfileCard.md)| The card that will be added to the profile. | 

### Return type

[**ProfileResponse**](ProfileResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## profilesProfileIdDelete

> ProfileResponse profilesProfileIdDelete(profileId)

Delete profile

Delete a Payment Profile using the profile ID, also known as the Customer Code.

### Example

```javascript
import BeanstreamPayments from 'beanstream_payments';

let apiInstance = new BeanstreamPayments.ProfilesApi();
let profileId = "profileId_example"; // String | The profile id. (aka CustomerCode)
apiInstance.profilesProfileIdDelete(profileId, (error, data, response) => {
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
 **profileId** | **String**| The profile id. (aka CustomerCode) | 

### Return type

[**ProfileResponse**](ProfileResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## profilesProfileIdGet

> PaymentProfile profilesProfileIdGet(profileId)

Get profile

Get a Payment Profile using the profile ID, also known as the Customer Code.

### Example

```javascript
import BeanstreamPayments from 'beanstream_payments';

let apiInstance = new BeanstreamPayments.ProfilesApi();
let profileId = "profileId_example"; // String | The profile id. (aka CustomerCode)
apiInstance.profilesProfileIdGet(profileId, (error, data, response) => {
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
 **profileId** | **String**| The profile id. (aka CustomerCode) | 

### Return type

[**PaymentProfile**](PaymentProfile.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## profilesProfileIdPut

> ProfileResponse profilesProfileIdPut(profileId, updateProfileBody)

Update Profile

Create a new Payment Profile using either a card or a Legato token. You must supply one of them.

### Example

```javascript
import BeanstreamPayments from 'beanstream_payments';

let apiInstance = new BeanstreamPayments.ProfilesApi();
let profileId = "profileId_example"; // String | The profile id. (aka CustomerCode)
let updateProfileBody = new BeanstreamPayments.UpdateProfileBody(); // UpdateProfileBody | 
apiInstance.profilesProfileIdPut(profileId, updateProfileBody, (error, data, response) => {
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
 **profileId** | **String**| The profile id. (aka CustomerCode) | 
 **updateProfileBody** | [**UpdateProfileBody**](UpdateProfileBody.md)|  | 

### Return type

[**ProfileResponse**](ProfileResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

