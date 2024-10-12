# LhPartnerApi.OffersApi

All URIs are relative to *https://api.lufthansa.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**allFares**](OffersApi.md#allFares) | **GET** /offers/fares/allfares | All Fares
[**bestFares**](OffersApi.md#bestFares) | **GET** /offers/fares/bestfares | Best Fares
[**deepLinks**](OffersApi.md#deepLinks) | **GET** /offers/fares/deeplink | Deep Links
[**fares**](OffersApi.md#fares) | **GET** /offers/fares/fares | Fares
[**faresSubscriptions**](OffersApi.md#faresSubscriptions) | **GET** /offers/fares/subscriptions | Fares Subscriptions
[**lHDeepLinksFFP**](OffersApi.md#lHDeepLinksFFP) | **GET** /offers/fares/deeplink/ffp | LH Deep Links - FFP
[**lHDeepLinksITCO**](OffersApi.md#lHDeepLinksITCO) | **GET** /offers/fares/deeplink/itco | LH Deep Links - ITCO
[**lowestFares**](OffersApi.md#lowestFares) | **GET** /offers/fares/lowestfares | Lowest Fares
[**oNDRoute**](OffersApi.md#oNDRoute) | **GET** /offers/ond/route/{origin}/{destination} | OND Route
[**oNDStatus**](OffersApi.md#oNDStatus) | **GET** /offers/ond/status | OND Status
[**topOND**](OffersApi.md#topOND) | **GET** /offers/ond/top | Top OND



## allFares

> String allFares(catalogues, origin, destination, travelDate, opts)

All Fares

Retrieves all available fares for a specific Origin &amp; Destination pair on a given date. Available fares are: One-way and Return for 4U. Return only for OS

### Example

```javascript
import LhPartnerApi from 'lh_partner_api';
let defaultClient = LhPartnerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: auth
let auth = defaultClient.authentications['auth'];
auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LhPartnerApi.OffersApi();
let catalogues = "catalogues_example"; // String | Specifies in which catalogue the fares need to be searched (e.g.'4U;OS').
let origin = "origin_example"; // String | Enter journey origin (e.g 'FRA').
let destination = "destination_example"; // String | Enter journey destination (e.g 'MAD').
let travelDate = "travelDate_example"; // String | Enter journey travel-date (e.g 2016-10-20)
let opts = {
  'returnDate': "returnDate_example", // String | Enter journey return-date (e.g 2016-10-31)'.
  'cabinClass': "'economy'", // String | Enter the required cabin class (e.g econonmy, business etc.). (Acceptable values are: \"\", \"economy\", \"premium economy\", \"business\", \"first\")
  'travelers': "travelers_example", // String | Specifies the type and number of travelers (e.g. '(adult=2;child=2;infant=1)') For LH only (adult=1) possible.
  'fareFamily': "'smart'", // String | Mandatory for 4U. Specifies, which fares to be returned, such as basic, smart, best, smartflex, bestflex . (Acceptable values are: \"\", \"basic\", \"smart\", \"best\", \"smartflex\", \"bestflex\")
  'trackingid': "trackingid_example", // String | Austrian Airlines only - specify the web tracking id to be used in OS Deep link.
  'accept': "'application/json'" // String | Mandatory http header:  application/xml or application/json
};
apiInstance.allFares(catalogues, origin, destination, travelDate, opts, (error, data, response) => {
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
 **catalogues** | **String**| Specifies in which catalogue the fares need to be searched (e.g.&#39;4U;OS&#39;). | 
 **origin** | **String**| Enter journey origin (e.g &#39;FRA&#39;). | 
 **destination** | **String**| Enter journey destination (e.g &#39;MAD&#39;). | 
 **travelDate** | **String**| Enter journey travel-date (e.g 2016-10-20) | 
 **returnDate** | **String**| Enter journey return-date (e.g 2016-10-31)&#39;. | [optional] 
 **cabinClass** | **String**| Enter the required cabin class (e.g econonmy, business etc.). (Acceptable values are: \&quot;\&quot;, \&quot;economy\&quot;, \&quot;premium economy\&quot;, \&quot;business\&quot;, \&quot;first\&quot;) | [optional] [default to &#39;economy&#39;]
 **travelers** | **String**| Specifies the type and number of travelers (e.g. &#39;(adult&#x3D;2;child&#x3D;2;infant&#x3D;1)&#39;) For LH only (adult&#x3D;1) possible. | [optional] 
 **fareFamily** | **String**| Mandatory for 4U. Specifies, which fares to be returned, such as basic, smart, best, smartflex, bestflex . (Acceptable values are: \&quot;\&quot;, \&quot;basic\&quot;, \&quot;smart\&quot;, \&quot;best\&quot;, \&quot;smartflex\&quot;, \&quot;bestflex\&quot;) | [optional] [default to &#39;smart&#39;]
 **trackingid** | **String**| Austrian Airlines only - specify the web tracking id to be used in OS Deep link. | [optional] 
 **accept** | **String**| Mandatory http header:  application/xml or application/json | [optional] [default to &#39;application/json&#39;]

### Return type

**String**

### Authorization

[auth](../README.md#auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## bestFares

> String bestFares(catalogues, origin, destination, travelDate, tripDuration, range, accept, opts)

Best Fares

Retrieve best fares for the requested journey across multiple days or multiple months.

### Example

```javascript
import LhPartnerApi from 'lh_partner_api';
let defaultClient = LhPartnerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: auth
let auth = defaultClient.authentications['auth'];
auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LhPartnerApi.OffersApi();
let catalogues = "catalogues_example"; // String | Search fares from these carriers' catalogues (e.g. '4U;OS;LH')
let origin = "origin_example"; // String | Journey origin. 3-letter IATA airport code (e.g. 'FRA')
let destination = "destination_example"; // String | Journey destination. 3-letter IATA airport code (e.g. 'MAD')
let travelDate = "travelDate_example"; // String | Journey travel-date (YYYY-MM-DD)
let tripDuration = "tripDuration_example"; // String | Trip duration in days (e.g. '7')
let range = "range_example"; // String | Fare range: 'byday' or 'bymonth' (Acceptable values are: \"byday\", \"bymonth\")
let accept = "accept_example"; // String | http header: application/json or application/xml (Acceptable values are: \"application/json\", \"application/xml\")
let opts = {
  'cabinClass': "cabinClass_example", // String | Cabin class: 'economy', 'premium_economy', 'business', 'first' (Acceptable values are: \"\", \"economy\", \"premium_economy\", \"business\", \"first\")
  'country': "country_example", // String | Country code of requestor. 2-letter ISO 3166-1 country code (e.g. 'de')
  'trackingid': "trackingid_example", // String | Austrian Airlines only - specify the web tracking id to be used in OS Deep link.
  'fareFamily': "fareFamily_example" // String | Fare family: basic, smart, best, smartflex, bestflex - Germanwings only (Acceptable values are: \"\", \"basic\", \"smart\", \"best\", \"smartflex\", \"bestflex\")
};
apiInstance.bestFares(catalogues, origin, destination, travelDate, tripDuration, range, accept, opts, (error, data, response) => {
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
 **catalogues** | **String**| Search fares from these carriers&#39; catalogues (e.g. &#39;4U;OS;LH&#39;) | 
 **origin** | **String**| Journey origin. 3-letter IATA airport code (e.g. &#39;FRA&#39;) | 
 **destination** | **String**| Journey destination. 3-letter IATA airport code (e.g. &#39;MAD&#39;) | 
 **travelDate** | **String**| Journey travel-date (YYYY-MM-DD) | 
 **tripDuration** | **String**| Trip duration in days (e.g. &#39;7&#39;) | 
 **range** | **String**| Fare range: &#39;byday&#39; or &#39;bymonth&#39; (Acceptable values are: \&quot;byday\&quot;, \&quot;bymonth\&quot;) | 
 **accept** | **String**| http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;) | 
 **cabinClass** | **String**| Cabin class: &#39;economy&#39;, &#39;premium_economy&#39;, &#39;business&#39;, &#39;first&#39; (Acceptable values are: \&quot;\&quot;, \&quot;economy\&quot;, \&quot;premium_economy\&quot;, \&quot;business\&quot;, \&quot;first\&quot;) | [optional] 
 **country** | **String**| Country code of requestor. 2-letter ISO 3166-1 country code (e.g. &#39;de&#39;) | [optional] 
 **trackingid** | **String**| Austrian Airlines only - specify the web tracking id to be used in OS Deep link. | [optional] 
 **fareFamily** | **String**| Fare family: basic, smart, best, smartflex, bestflex - Germanwings only (Acceptable values are: \&quot;\&quot;, \&quot;basic\&quot;, \&quot;smart\&quot;, \&quot;best\&quot;, \&quot;smartflex\&quot;, \&quot;bestflex\&quot;) | [optional] 

### Return type

**String**

### Authorization

[auth](../README.md#auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deepLinks

> String deepLinks(catalogues, trackingid, country, lang, accept, opts)

Deep Links

Returns valid deep links for the provided input parameters

### Example

```javascript
import LhPartnerApi from 'lh_partner_api';
let defaultClient = LhPartnerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: auth
let auth = defaultClient.authentications['auth'];
auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LhPartnerApi.OffersApi();
let catalogues = "catalogues_example"; // String | Carrier for which the deep link will be created (e.g. 'LH')
let trackingid = "trackingid_example"; // String | Deep link tracking ID
let country = "country_example"; // String | 2-letter ISO 3166-1 country code
let lang = "lang_example"; // String | 2-letter ISO 3166-1 language code
let accept = "accept_example"; // String | http header: application/json or application/xml (Acceptable values are: \"application/json\", \"application/xml\")
let opts = {
  'origin': "origin_example", // String | Journey origin. 3-letter IATA airport or city code (e.g. 'FRA')
  'originName': "originName_example", // String | Journey origin airport or city name (e.g. 'frankfurt')
  'destination': "destination_example", // String | Journey destination. 3-letter IATA airport or city code (e.g. 'MAD')
  'destinationName': "destinationName_example", // String | Journey destination airport or city name (e.g. 'madrid')
  'travelDate': "travelDate_example", // String | Journey travel-date (YYYY-MM-DD)
  'returnDate': "returnDate_example", // String | Journey return-date (YYYY-MM-DD)
  'cabinClass': "cabinClass_example", // String | Cabin class: 'economy', 'premium_economy', 'business', 'first' (Acceptable values are: \"\", \"economy\", \"premium_economy\", \"business\", \"first\")
  'outboundSegments': "outboundSegments_example", // String | Outbound flight segments in the sequence of travel (e.g. 'LH096;LH480')
  'returnSegments': "returnSegments_example", // String | Flight segments in the sequence of travel (e.g. 'LH7465;LH431')
  'travelers': "travelers_example", // String | Type and number of travelers (e.g. '(adult=2;child=2;infant=1)')
  'fare': "fare_example", // String | Travel fare (e.g. '1341.45')
  'netFare': "netFare_example", // String | Travel net fare. Total fare less taxes and charges (e.g. '1140')
  'fareCurrency': "fareCurrency_example", // String | Fare currency (e.g. 'EUR')
  'partnerid': "partnerid_example", // String | Deep link partner id (e.g. '1247')
  'encryptionKey': "encryptionKey_example" // String | Deep link encryption-key
};
apiInstance.deepLinks(catalogues, trackingid, country, lang, accept, opts, (error, data, response) => {
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
 **catalogues** | **String**| Carrier for which the deep link will be created (e.g. &#39;LH&#39;) | 
 **trackingid** | **String**| Deep link tracking ID | 
 **country** | **String**| 2-letter ISO 3166-1 country code | 
 **lang** | **String**| 2-letter ISO 3166-1 language code | 
 **accept** | **String**| http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;) | 
 **origin** | **String**| Journey origin. 3-letter IATA airport or city code (e.g. &#39;FRA&#39;) | [optional] 
 **originName** | **String**| Journey origin airport or city name (e.g. &#39;frankfurt&#39;) | [optional] 
 **destination** | **String**| Journey destination. 3-letter IATA airport or city code (e.g. &#39;MAD&#39;) | [optional] 
 **destinationName** | **String**| Journey destination airport or city name (e.g. &#39;madrid&#39;) | [optional] 
 **travelDate** | **String**| Journey travel-date (YYYY-MM-DD) | [optional] 
 **returnDate** | **String**| Journey return-date (YYYY-MM-DD) | [optional] 
 **cabinClass** | **String**| Cabin class: &#39;economy&#39;, &#39;premium_economy&#39;, &#39;business&#39;, &#39;first&#39; (Acceptable values are: \&quot;\&quot;, \&quot;economy\&quot;, \&quot;premium_economy\&quot;, \&quot;business\&quot;, \&quot;first\&quot;) | [optional] 
 **outboundSegments** | **String**| Outbound flight segments in the sequence of travel (e.g. &#39;LH096;LH480&#39;) | [optional] 
 **returnSegments** | **String**| Flight segments in the sequence of travel (e.g. &#39;LH7465;LH431&#39;) | [optional] 
 **travelers** | **String**| Type and number of travelers (e.g. &#39;(adult&#x3D;2;child&#x3D;2;infant&#x3D;1)&#39;) | [optional] 
 **fare** | **String**| Travel fare (e.g. &#39;1341.45&#39;) | [optional] 
 **netFare** | **String**| Travel net fare. Total fare less taxes and charges (e.g. &#39;1140&#39;) | [optional] 
 **fareCurrency** | **String**| Fare currency (e.g. &#39;EUR&#39;) | [optional] 
 **partnerid** | **String**| Deep link partner id (e.g. &#39;1247&#39;) | [optional] 
 **encryptionKey** | **String**| Deep link encryption-key | [optional] 

### Return type

**String**

### Authorization

[auth](../README.md#auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fares

> String fares(catalogues, segments, carriers, accept, opts)

Fares

Retrieve all available fares per fare family for a specific Origin &amp; Destination on a given date

### Example

```javascript
import LhPartnerApi from 'lh_partner_api';
let defaultClient = LhPartnerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: auth
let auth = defaultClient.authentications['auth'];
auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LhPartnerApi.OffersApi();
let catalogues = "catalogues_example"; // String | Search fares from these carriers' catalogues - currently active for Germanwings only  (4U)
let segments = "segments_example"; // String | Journey details  e.g. (origin=TXL;destination=CGN;travel-date=2016-12-15;return-date=2016-12-20;cabin=Economy)
let carriers = "carriers_example"; // String | Include fares for these carriers e.g. ('4U;LH')
let accept = "accept_example"; // String | http header: application/json or application/xml (Acceptable values are: \"application/json\", \"application/xml\")
let opts = {
  'travelers': "travelers_example", // String | Type and number of travelers e.g. (adult=1;child=1;infant=1)
  'fareTypes': "'basic'" // String | Fares family: basic,smart, best, smartflex, bestflex - Germanwings only (Acceptable values are: \"\", \"basic\", \"smart\", \"best\", \"smartflex\", \"bestflex\")
};
apiInstance.fares(catalogues, segments, carriers, accept, opts, (error, data, response) => {
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
 **catalogues** | **String**| Search fares from these carriers&#39; catalogues - currently active for Germanwings only  (4U) | 
 **segments** | **String**| Journey details  e.g. (origin&#x3D;TXL;destination&#x3D;CGN;travel-date&#x3D;2016-12-15;return-date&#x3D;2016-12-20;cabin&#x3D;Economy) | 
 **carriers** | **String**| Include fares for these carriers e.g. (&#39;4U;LH&#39;) | 
 **accept** | **String**| http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;) | 
 **travelers** | **String**| Type and number of travelers e.g. (adult&#x3D;1;child&#x3D;1;infant&#x3D;1) | [optional] 
 **fareTypes** | **String**| Fares family: basic,smart, best, smartflex, bestflex - Germanwings only (Acceptable values are: \&quot;\&quot;, \&quot;basic\&quot;, \&quot;smart\&quot;, \&quot;best\&quot;, \&quot;smartflex\&quot;, \&quot;bestflex\&quot;) | [optional] [default to &#39;basic&#39;]

### Return type

**String**

### Authorization

[auth](../README.md#auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## faresSubscriptions

> String faresSubscriptions(origin, destination, cabinClass, tripDuration, email, lang, accept, opts)

Fares Subscriptions

Create a subscription for best price O&amp;D. Receive regular updates on lowest fares

### Example

```javascript
import LhPartnerApi from 'lh_partner_api';
let defaultClient = LhPartnerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: auth
let auth = defaultClient.authentications['auth'];
auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LhPartnerApi.OffersApi();
let origin = "origin_example"; // String | Journey origin. 3-leter IATA airport code (e.g. 'FRA')
let destination = "destination_example"; // String | Journey destination. 3-letter IATA airport code (e.g. 'MAD')
let cabinClass = "cabinClass_example"; // String | Cabin class: 'economy', 'premium_economy', 'business', 'first' (Acceptable values are: \"\", \"economy\", \"premium_economy\", \"business\", \"first\")
let tripDuration = "tripDuration_example"; // String | Trip duration in days (e.g. '7')
let email = "email_example"; // String | Email Address')
let lang = "lang_example"; // String | 2-letter ISO 3166-1 language code
let accept = "accept_example"; // String | http header: application/json or application/xml (Acceptable values are: \"application/json\", \"application/xml\")
let opts = {
  'country': "country_example", // String | 2-letter ISO 3166-1 country code
  'trackingid': "trackingid_example" // String | Tracking parameter
};
apiInstance.faresSubscriptions(origin, destination, cabinClass, tripDuration, email, lang, accept, opts, (error, data, response) => {
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
 **origin** | **String**| Journey origin. 3-leter IATA airport code (e.g. &#39;FRA&#39;) | 
 **destination** | **String**| Journey destination. 3-letter IATA airport code (e.g. &#39;MAD&#39;) | 
 **cabinClass** | **String**| Cabin class: &#39;economy&#39;, &#39;premium_economy&#39;, &#39;business&#39;, &#39;first&#39; (Acceptable values are: \&quot;\&quot;, \&quot;economy\&quot;, \&quot;premium_economy\&quot;, \&quot;business\&quot;, \&quot;first\&quot;) | 
 **tripDuration** | **String**| Trip duration in days (e.g. &#39;7&#39;) | 
 **email** | **String**| Email Address&#39;) | 
 **lang** | **String**| 2-letter ISO 3166-1 language code | 
 **accept** | **String**| http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;) | 
 **country** | **String**| 2-letter ISO 3166-1 country code | [optional] 
 **trackingid** | **String**| Tracking parameter | [optional] 

### Return type

**String**

### Authorization

[auth](../README.md#auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## lHDeepLinksFFP

> String lHDeepLinksFFP(catalogues, origin, destination, travelDate, trackingid, country, lang, accept, opts)

LH Deep Links - FFP

Returns valid LH deep links (FFP - links to flight selection screen on LH.COM)

### Example

```javascript
import LhPartnerApi from 'lh_partner_api';
let defaultClient = LhPartnerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: auth
let auth = defaultClient.authentications['auth'];
auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LhPartnerApi.OffersApi();
let catalogues = "catalogues_example"; // String | Carrier for which the deep link will be created (e.g. 'LH')
let origin = "origin_example"; // String | Journey origin. 3-letter IATA airport or city code (e.g. 'FRA')
let destination = "destination_example"; // String | Journey destination. 3-letter IATA airport or city code (e.g. 'MAD')
let travelDate = "travelDate_example"; // String | Journey travel-date (YYYY-MM-DD)
let trackingid = "trackingid_example"; // String | Deep link tracking ID
let country = "country_example"; // String | 2-letter ISO 3166-1 country code
let lang = "lang_example"; // String | 2-letter ISO 3166-1 language code
let accept = "accept_example"; // String | http header: application/json or application/xml (Acceptable values are: \"application/json\", \"application/xml\")
let opts = {
  'returnDate': "returnDate_example", // String | Journey return-date (YYYY-MM-DD)
  'cabinClass': "cabinClass_example", // String | Cabin class: 'economy', 'premium_economy', 'business', 'first' (Acceptable values are: \"\", \"economy\", \"premium_economy\", \"business\", \"first\")
  'travelers': "travelers_example", // String | Type and number of travelers (e.g. '(adult=2;child=2;infant=1)')
  'partnerid': "partnerid_example", // String | Deep link partner id (e.g. '1247')
  'encryptionKey': "encryptionKey_example" // String | Deep link encryption-key
};
apiInstance.lHDeepLinksFFP(catalogues, origin, destination, travelDate, trackingid, country, lang, accept, opts, (error, data, response) => {
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
 **catalogues** | **String**| Carrier for which the deep link will be created (e.g. &#39;LH&#39;) | 
 **origin** | **String**| Journey origin. 3-letter IATA airport or city code (e.g. &#39;FRA&#39;) | 
 **destination** | **String**| Journey destination. 3-letter IATA airport or city code (e.g. &#39;MAD&#39;) | 
 **travelDate** | **String**| Journey travel-date (YYYY-MM-DD) | 
 **trackingid** | **String**| Deep link tracking ID | 
 **country** | **String**| 2-letter ISO 3166-1 country code | 
 **lang** | **String**| 2-letter ISO 3166-1 language code | 
 **accept** | **String**| http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;) | 
 **returnDate** | **String**| Journey return-date (YYYY-MM-DD) | [optional] 
 **cabinClass** | **String**| Cabin class: &#39;economy&#39;, &#39;premium_economy&#39;, &#39;business&#39;, &#39;first&#39; (Acceptable values are: \&quot;\&quot;, \&quot;economy\&quot;, \&quot;premium_economy\&quot;, \&quot;business\&quot;, \&quot;first\&quot;) | [optional] 
 **travelers** | **String**| Type and number of travelers (e.g. &#39;(adult&#x3D;2;child&#x3D;2;infant&#x3D;1)&#39;) | [optional] 
 **partnerid** | **String**| Deep link partner id (e.g. &#39;1247&#39;) | [optional] 
 **encryptionKey** | **String**| Deep link encryption-key | [optional] 

### Return type

**String**

### Authorization

[auth](../README.md#auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## lHDeepLinksITCO

> String lHDeepLinksITCO(catalogues, origin, destination, travelDate, outboundSegments, fare, fareCurrency, trackingid, country, lang, accept, opts)

LH Deep Links - ITCO

Returns valid LH deep links (ITCO - links to shopping cart on LH.COM)

### Example

```javascript
import LhPartnerApi from 'lh_partner_api';
let defaultClient = LhPartnerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: auth
let auth = defaultClient.authentications['auth'];
auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LhPartnerApi.OffersApi();
let catalogues = "catalogues_example"; // String | Carrier for which the deep link will be created (e.g. 'LH')
let origin = "origin_example"; // String | Journey origin. 3-letter IATA airport or city code (e.g. 'FRA')
let destination = "destination_example"; // String | Journey destination. 3-letter IATA airport or city code (e.g. 'MAD')
let travelDate = "travelDate_example"; // String | Journey travel-date (YYYY-MM-DD)
let outboundSegments = "outboundSegments_example"; // String | Outbound flight segments in the sequence of travel (e.g. 'LH096;LH480')
let fare = "fare_example"; // String | Travel fare (e.g. '1341.45')
let fareCurrency = "fareCurrency_example"; // String | Fare currency (e.g. 'EUR')
let trackingid = "trackingid_example"; // String | Deep link tracking ID
let country = "country_example"; // String | 2-letter ISO 3166-1 country code
let lang = "lang_example"; // String | 2-letter ISO 3166-1 language code
let accept = "accept_example"; // String | http header: application/json or application/xml (Acceptable values are: \"application/json\", \"application/xml\")
let opts = {
  'returnDate': "returnDate_example", // String | Journey return-date (YYYY-MM-DD)
  'cabinClass': "cabinClass_example", // String | Cabin class: 'economy', 'premium_economy', 'business', 'first' (Acceptable values are: \"\", \"economy\", \"premium_economy\", \"business\", \"first\")
  'returnSegments': "returnSegments_example", // String | Flight segments in the sequence of travel (e.g. 'LH7465;LH431')
  'travelers': "travelers_example", // String | Type and number of travelers (e.g. '(adult=2;child=2;infant=1)')
  'netFare': "netFare_example", // String | Travel net fare. Total fare less taxes and charges (e.g. '1140')
  'partnerid': "partnerid_example", // String | Deep link partner id (e.g. '1247')
  'encryptionKey': "encryptionKey_example" // String | Deep link encryption-key
};
apiInstance.lHDeepLinksITCO(catalogues, origin, destination, travelDate, outboundSegments, fare, fareCurrency, trackingid, country, lang, accept, opts, (error, data, response) => {
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
 **catalogues** | **String**| Carrier for which the deep link will be created (e.g. &#39;LH&#39;) | 
 **origin** | **String**| Journey origin. 3-letter IATA airport or city code (e.g. &#39;FRA&#39;) | 
 **destination** | **String**| Journey destination. 3-letter IATA airport or city code (e.g. &#39;MAD&#39;) | 
 **travelDate** | **String**| Journey travel-date (YYYY-MM-DD) | 
 **outboundSegments** | **String**| Outbound flight segments in the sequence of travel (e.g. &#39;LH096;LH480&#39;) | 
 **fare** | **String**| Travel fare (e.g. &#39;1341.45&#39;) | 
 **fareCurrency** | **String**| Fare currency (e.g. &#39;EUR&#39;) | 
 **trackingid** | **String**| Deep link tracking ID | 
 **country** | **String**| 2-letter ISO 3166-1 country code | 
 **lang** | **String**| 2-letter ISO 3166-1 language code | 
 **accept** | **String**| http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;) | 
 **returnDate** | **String**| Journey return-date (YYYY-MM-DD) | [optional] 
 **cabinClass** | **String**| Cabin class: &#39;economy&#39;, &#39;premium_economy&#39;, &#39;business&#39;, &#39;first&#39; (Acceptable values are: \&quot;\&quot;, \&quot;economy\&quot;, \&quot;premium_economy\&quot;, \&quot;business\&quot;, \&quot;first\&quot;) | [optional] 
 **returnSegments** | **String**| Flight segments in the sequence of travel (e.g. &#39;LH7465;LH431&#39;) | [optional] 
 **travelers** | **String**| Type and number of travelers (e.g. &#39;(adult&#x3D;2;child&#x3D;2;infant&#x3D;1)&#39;) | [optional] 
 **netFare** | **String**| Travel net fare. Total fare less taxes and charges (e.g. &#39;1140&#39;) | [optional] 
 **partnerid** | **String**| Deep link partner id (e.g. &#39;1247&#39;) | [optional] 
 **encryptionKey** | **String**| Deep link encryption-key | [optional] 

### Return type

**String**

### Authorization

[auth](../README.md#auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## lowestFares

> String lowestFares(catalogues, origin, destination, travelDate, accept, opts)

Lowest Fares

Retrieve lowest fare for a specific Origin &amp; Destination pair on a given date. Available fares are: One-way and Return for 4U. Return only for OS &amp; LH

### Example

```javascript
import LhPartnerApi from 'lh_partner_api';
let defaultClient = LhPartnerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: auth
let auth = defaultClient.authentications['auth'];
auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LhPartnerApi.OffersApi();
let catalogues = "catalogues_example"; // String | Search fares from these carriers' catalogues e.g. '4U;OS;LH'
let origin = "origin_example"; // String | Journey origin. 3-letter IATA aiport code e.g. 'FRA'
let destination = "destination_example"; // String | Journey destination. 3-letter IATA airport code e.g. 'MAD'
let travelDate = "travelDate_example"; // String | Journey travel-date YYYY-MM-DD
let accept = "accept_example"; // String | http header: application/json or application/xml (Acceptable values are: \"application/json\", \"application/xml\")
let opts = {
  'returnDate': "returnDate_example", // String | Journey return-date - mandatory for OS and LH searches YYYY-MM-DD
  'cabinClass': "cabinClass_example", // String | Cabin class: 'economy', 'premium_economy', 'business', 'first' (Acceptable values are: \"\", \"economy\", \"premium_economy\", \"business\", \"first\")
  'travelers': "travelers_example", // String | Type and number of travelers e.g. '(adult=2;child=2;infant=1)'. For LH only (adult=1) possible
  'fareFamily': "'basic'", // String | Fare family: basic, smart, best, smartflex, bestflex - Germanwings only (Acceptable values are: \"\", \"basic\", \"smart\", \"best\", \"smartflex\", \"bestflex\")
  'country': "country_example" // String | Country code of requestor. 2-letter ISO 3166-1 country code (e.g. 'de')
};
apiInstance.lowestFares(catalogues, origin, destination, travelDate, accept, opts, (error, data, response) => {
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
 **catalogues** | **String**| Search fares from these carriers&#39; catalogues e.g. &#39;4U;OS;LH&#39; | 
 **origin** | **String**| Journey origin. 3-letter IATA aiport code e.g. &#39;FRA&#39; | 
 **destination** | **String**| Journey destination. 3-letter IATA airport code e.g. &#39;MAD&#39; | 
 **travelDate** | **String**| Journey travel-date YYYY-MM-DD | 
 **accept** | **String**| http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;) | 
 **returnDate** | **String**| Journey return-date - mandatory for OS and LH searches YYYY-MM-DD | [optional] 
 **cabinClass** | **String**| Cabin class: &#39;economy&#39;, &#39;premium_economy&#39;, &#39;business&#39;, &#39;first&#39; (Acceptable values are: \&quot;\&quot;, \&quot;economy\&quot;, \&quot;premium_economy\&quot;, \&quot;business\&quot;, \&quot;first\&quot;) | [optional] 
 **travelers** | **String**| Type and number of travelers e.g. &#39;(adult&#x3D;2;child&#x3D;2;infant&#x3D;1)&#39;. For LH only (adult&#x3D;1) possible | [optional] 
 **fareFamily** | **String**| Fare family: basic, smart, best, smartflex, bestflex - Germanwings only (Acceptable values are: \&quot;\&quot;, \&quot;basic\&quot;, \&quot;smart\&quot;, \&quot;best\&quot;, \&quot;smartflex\&quot;, \&quot;bestflex\&quot;) | [optional] [default to &#39;basic&#39;]
 **country** | **String**| Country code of requestor. 2-letter ISO 3166-1 country code (e.g. &#39;de&#39;) | [optional] 

### Return type

**String**

### Authorization

[auth](../README.md#auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## oNDRoute

> String oNDRoute(origin, destination, accept, opts)

OND Route

Returns LH route origin &amp; destination information

### Example

```javascript
import LhPartnerApi from 'lh_partner_api';
let defaultClient = LhPartnerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: auth
let auth = defaultClient.authentications['auth'];
auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LhPartnerApi.OffersApi();
let origin = "origin_example"; // String | Enter either the orgin city or orgin country code (e.g 'FRA' or 'DE'). Enter '*' for all
let destination = "destination_example"; // String | Enter either the destination city or country code (e.g 'MAD' or 'ES'). Enter '*' for all
let accept = "accept_example"; // String | Mandatory http header:  application/xml or application/json
let opts = {
  'catalogues': "'LH'", // String | Carrier for which the OND will be retrieved (e.g. 'LH')
  'limit': "limit_example", // String | Number of records returned per request. Defaults to 20, maximum is 100 (if a value bigger than 100 is given, 100 will be taken)
  'offset': "offset_example" // String | Number of records skipped. Defaults to 0
};
apiInstance.oNDRoute(origin, destination, accept, opts, (error, data, response) => {
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
 **origin** | **String**| Enter either the orgin city or orgin country code (e.g &#39;FRA&#39; or &#39;DE&#39;). Enter &#39;*&#39; for all | 
 **destination** | **String**| Enter either the destination city or country code (e.g &#39;MAD&#39; or &#39;ES&#39;). Enter &#39;*&#39; for all | 
 **accept** | **String**| Mandatory http header:  application/xml or application/json | 
 **catalogues** | **String**| Carrier for which the OND will be retrieved (e.g. &#39;LH&#39;) | [optional] [default to &#39;LH&#39;]
 **limit** | **String**| Number of records returned per request. Defaults to 20, maximum is 100 (if a value bigger than 100 is given, 100 will be taken) | [optional] 
 **offset** | **String**| Number of records skipped. Defaults to 0 | [optional] 

### Return type

**String**

### Authorization

[auth](../README.md#auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## oNDStatus

> String oNDStatus(accept, opts)

OND Status

Returns LH network route status information. Search for recently added or retired routes

### Example

```javascript
import LhPartnerApi from 'lh_partner_api';
let defaultClient = LhPartnerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: auth
let auth = defaultClient.authentications['auth'];
auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LhPartnerApi.OffersApi();
let accept = "accept_example"; // String | Mandatory http header:  application/xml or application/json
let opts = {
  'catalogues': "'LH'", // String | Carrier for which the OND will be retrieved (e.g. 'LH')
  'newRoutes': "newRoutes_example", // String | Enter if newly added routes should be returned in the response. (Acceptable values are: \"\", \"true\", \"false\")
  'oldRoutes': "oldRoutes_example" // String | Enter if old (deleted) routes should be returned in the response. (Acceptable values are: \"\", \"true\", \"false\")
};
apiInstance.oNDStatus(accept, opts, (error, data, response) => {
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
 **accept** | **String**| Mandatory http header:  application/xml or application/json | 
 **catalogues** | **String**| Carrier for which the OND will be retrieved (e.g. &#39;LH&#39;) | [optional] [default to &#39;LH&#39;]
 **newRoutes** | **String**| Enter if newly added routes should be returned in the response. (Acceptable values are: \&quot;\&quot;, \&quot;true\&quot;, \&quot;false\&quot;) | [optional] 
 **oldRoutes** | **String**| Enter if old (deleted) routes should be returned in the response. (Acceptable values are: \&quot;\&quot;, \&quot;true\&quot;, \&quot;false\&quot;) | [optional] 

### Return type

**String**

### Authorization

[auth](../README.md#auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## topOND

> String topOND(accept, opts)

Top OND

Returns LH Top routes per country or across all countries

### Example

```javascript
import LhPartnerApi from 'lh_partner_api';
let defaultClient = LhPartnerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: auth
let auth = defaultClient.authentications['auth'];
auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LhPartnerApi.OffersApi();
let accept = "accept_example"; // String | Mandatory http header:  application/xml or application/json
let opts = {
  'catalogues': "'LH'", // String | Carrier for which the OND will be retrieved (e.g. 'LH')
  'origin': "origin_example" // String | Enter the origin country code (e.g. 'DE'). Leave empty to search Top OND across all countries
};
apiInstance.topOND(accept, opts, (error, data, response) => {
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
 **accept** | **String**| Mandatory http header:  application/xml or application/json | 
 **catalogues** | **String**| Carrier for which the OND will be retrieved (e.g. &#39;LH&#39;) | [optional] [default to &#39;LH&#39;]
 **origin** | **String**| Enter the origin country code (e.g. &#39;DE&#39;). Leave empty to search Top OND across all countries | [optional] 

### Return type

**String**

### Authorization

[auth](../README.md#auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

