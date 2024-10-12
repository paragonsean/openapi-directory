# pims

Pims - JavaScript client for pims

Hereafter is the documentation of the private API of [Pims: Pointages Intelligents pour le Monde du Spectacle](https://pims.io). This API is designed for 3rd-party softwares, editors and partners. Its main purpose is to give access the core data of a Pims customer (i.e. events, ticket counts and promotions).

## Authentication
The API uses [basic access authentication](https://en.wikipedia.org/wiki/Basic_access_authentication), meaning you will need a username and password to get authorized.

As each customer in Pims has its own domain (e.g. caramba.pims.io, gdp.pims.io...), each credentials will be valid for one domain/customer only. If you need dedicated credentials for one domain, please contact us. (In any case, we will need an explicit agreement from the customer before we create these credentials.)

<div class=\"info\">
To make your life easy, you can try all endpoints with the public credentials below, pointing to our [demo domain](https://demo.pims.io):
  <ul>
    <li>Base path: `https://demo.pims.io/api`</li>
    <li>Username: `demo`</li>
    <li>Password: `q83792db2GCvgYVdKpU3yG3R`</li>
  </ul>
</div>

## Response format
The API returns JSON and matches the [HAL specification](http://stateless.co/hal_specification.html). The `Content-Type` of each response will be `application/hal+json`, unless an error occurs.

Please note that this documentation describes all responses “as if” they were plain JSON. The specificities of HAL are ignored on purpose, in order to remain compact and avoid repetition.
<div style=\"-webkit-column-count: 2; -moz-column-count: 2; column-count: 2; -webkit-column-rule: 1px dotted #e0e0e0; -moz-column-rule: 1px dotted #e0e0e0; column-rule: 1px dotted #e0e0e0;\">
 <div style=\"display: inline-block; width:100%;\">
  <strong>So when you read in the doc:</strong>
<pre><code class=\"lang-json\">{
 <span class=\"token string\">\"id\"</span>: <span class=\"token number\">123</span>,
 <span class=\"token string\">\"property1\"</span>: <span class=\"token string\">\"Lorem ipsum\"</span>,
 <span class=\"token string\">\"object\"</span>: {
  <span class=\"token string\">\"id\"</span>: <span class=\"token number\">456</span>,
  <span class=\"token string\">\"property2\"</span>: <span class=\"token number\">7.89</span>
 }
}</code></pre>
 </div>
 <div style=\"display: inline-block; width:100%;\">
  <strong>... you'll get in the Real World®:</strong>
<pre><code class=\"lang-json\">{
 <span class=\"token string\">\"id\"</span>: <span class=\"token number\">123</span>,
 <span class=\"token string\">\"property2\"</span>: <span class=\"token string\">\"Lorem ipsum\"</span>,
 <span class=\"token string\">\"_embedded\"</span>: {
  <span class=\"token string\">\"object\"</span>: {
   <span class=\"token string\">\"id\"</span>: <span class=\"token number\">456</span>,
   <span class=\"token string\">\"property2\"</span>: <span class=\"token number\">7.89</span>,
   <span class=\"token string\">\"_links\"</span>: {
    <span class=\"token string\">\"self\"</span>: {
     <span class=\"token string\">\"href\"</span>: <span class=\"token string\">\"https://api.mydomain.com/other-item/456\"</span>
    }
   }
  }
 }
 <span class=\"token string\">\"_links\"</span>: {
  <span class=\"token string\">\"self\"</span>: {
   <span class=\"token string\">\"href\"</span>: <span class=\"token string\">\"https://api.mydomain.com/item/123\"</span>
  }
 }
}</code></pre>
 </div>
</div>

### Errors
Errors return JSON too and tries to match the [Problem Details for HTTP APIs specification](https://tools.ietf.org/html/rfc7807). If it does not match this spec, that's either a bug or a compatibility issue. Please contact us to solve the problem.

The `Content-Type` of errors will be `application/problem+json`. The content will match the following JSON:
```json
{
 \"type\": \"https://tools.ietf.org/html/rfc2616#section-10\",
    \"title\": \"Not Found\",
 \"status\": 404,
    \"detail\": \"Entity not found\"
}
```

## Versioning
The API is fully versionned, using an URL-versioning scheme: `https://demo.pims.io/api/v1/events`, `https://demo.pims.io/api/v2/events`,...

The version part of the URL is optional, and will be completed with the last stable version if omitted.

## Pagination
All responses corresponding to a collection of resources (e.g. `/venues` or `/series/:id/events`) are paginated. When so, you will only get the first 25 resources you asked for.

If you need to get more resources in one call, you can use the `page_size` query parameter. E.g. `/venues?page_size=50` to get the 50 first venues.

Also note that with HAL, the navigation in paginated responses is a piece of cake, as you can see below:
```json
{
 \"_links\": {
  \"self\": {
   \"href\": \"https://demo.pims.io/api/v1/events?page=1\"
  },
  \"first\": {
   \"href\": \"https://demo.pims.io/api/v1/events\"
  },
  \"last\": {
   \"href\": \"https://demo.pims.io/api/v1/events?page=14\"
  },
  \"next\": {
   \"href\": \"https://demo.pims.io/api/v1/events?page=2\"
  }
 },
 \"_embedded\": {
   ... // data content goes here
 },
 \"page_count\": 14,
 \"page_size\": 25,
 \"total_items\": 331,
 \"page\": 1
}
```

## Filtering and sorting
Every textual filter (e.g. `/events?label=U2`) and/or sort (e.g. `/events?sort=label`) performed with the API uses UTF8_UNICODE_CI collation, meaning it is:
- Case insensitive: “Chloé” will be considered the same as “CHLOÉ”;
- Diacritic insensitive: “Chloé” will be considered the same as “Chloe”.

When performing a sort, it will always be *ascending* by default. To make it *descending*, just use a minus sign (`-`) in front of the parameter value (e.g. `/events?sort=-label`).

## I18n
In responses, some labels can be translated (e.g. promotion types, event input types, etc.). These translatable labels are clearly indicated in the documentation below.

By default, they will be displayed in English, but you can change this behaviour via the `Accept-Language` header. E.g., use `fr` as a value for French.

## PHP SDK
We provide a simple yet convenient SDK for the PHP language, see [the Github page of the project](https://github.com/pimssas/pims-api-client-php).

## And now?
Generaly, you will start by [fetching one or more events](#tag/Events). An <span class=\"definition\">event</span> can be anything that occurs in one venue at one given date and time: a concert, a play, a match, a conference, etc. Additionnally, you can explore the [series](#tag/Series): a <span class=\"definition\">series</span> is just a group of events (e.g. a tour or a festival).

Once you retrieved the events you were interested in, you can look for the sales (<span class=\"definition\">ticket counts</span>):
- Get a quick overview with [`/events/:id/ticket-counts`](#operation/fetchAllTicketCounts)
- Or get a full insight by calling these endpoints:
    1. [`/events/:id/categories`](#operation/fetchAllEventsCategories)
    2. [`/events/:id/channels`](#operation/fetchAllEventsChannels)
    3. [`/events/:id/ticket-counts/detailed`](#operation/fetchAllDetailedTicketCounts)

Eventually, you may also want to fetch the [promotions](#tag/Promotions). A <span class=\"definition\">promotion</span> can be anything meant to leverage the sales: ads, marketing campaigns, buzz or news around the event, etc. A promotion can be linked to any combination of events and/or series.
This SDK is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0
- Package version: 1.0
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.JavascriptClientCodegen

## Installation

### For [Node.js](https://nodejs.org/)

#### npm

To publish the library as a [npm](https://www.npmjs.com/), please follow the procedure in ["Publishing npm packages"](https://docs.npmjs.com/getting-started/publishing-npm-packages).

Then install it via:

```shell
npm install pims --save
```

Finally, you need to build the module:

```shell
npm run build
```

##### Local development

To use the library locally without publishing to a remote npm registry, first install the dependencies by changing into the directory containing `package.json` (and this README). Let's call this `JAVASCRIPT_CLIENT_DIR`. Then run:

```shell
npm install
```

Next, [link](https://docs.npmjs.com/cli/link) it globally in npm with the following, also from `JAVASCRIPT_CLIENT_DIR`:

```shell
npm link
```

To use the link you just defined in your project, switch to the directory you want to use your pims from, and run:

```shell
npm link /path/to/<JAVASCRIPT_CLIENT_DIR>
```

Finally, you need to build the module:

```shell
npm run build
```

#### git

If the library is hosted at a git repository, e.g.https://github.com/GIT_USER_ID/GIT_REPO_ID
then install it via:

```shell
    npm install GIT_USER_ID/GIT_REPO_ID --save
```

### For browser

The library also works in the browser environment via npm and [browserify](http://browserify.org/). After following
the above steps with Node.js and installing browserify with `npm install -g browserify`,
perform the following (assuming *main.js* is your entry file):

```shell
browserify main.js > bundle.js
```

Then include *bundle.js* in the HTML pages.

### Webpack Configuration

Using Webpack you may encounter the following error: "Module not found: Error:
Cannot resolve module", most certainly you should disable AMD loader. Add/merge
the following section to your webpack config:

```javascript
module: {
  rules: [
    {
      parser: {
        amd: false
      }
    }
  ]
}
```

## Getting Started

Please follow the [installation](#installation) instruction and execute the following JS code:

```javascript
var Pims = require('pims');

var defaultClient = Pims.ApiClient.instance;
// Configure HTTP basic authorization: Basic Auth
var Basic Auth = defaultClient.authentications['Basic Auth'];
Basic Auth.username = 'YOUR USERNAME'
Basic Auth.password = 'YOUR PASSWORD'

var api = new Pims.CapacitiesApi()
var eventId = 56; // {Number} ID of the targeted event.
var opts = {
  'showIgnored': false, // {Boolean} If set to `false`, show only the [event-]categories which are not ignored. If set to `true`, show everything.
  'sort': "'date'", // {String} Sort the capacities in the corresponding order.
  'pageSize': 25 // {Number} Pagination size, i.e. maximum number of items to be displayed in the response.
};
var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
api.fetchAllEventsCapacities(eventId, opts, callback);

```

## Documentation for API Endpoints

All URIs are relative to *https://demo.pims.io/api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*Pims.CapacitiesApi* | [**fetchAllEventsCapacities**](docs/CapacitiesApi.md#fetchAllEventsCapacities) | **GET** /events/{event_id}/capacities | Find all capacities for one event
*Pims.CapacitiesApi* | [**fetchOneEventCapacity**](docs/CapacitiesApi.md#fetchOneEventCapacity) | **GET** /events/{event_id}/capacities/{capacity_id} | Get one capacity by ID
*Pims.CategoriesApi* | [**fetchAllCategories**](docs/CategoriesApi.md#fetchAllCategories) | **GET** /categories | Find all categories
*Pims.CategoriesApi* | [**fetchAllEventsCategories**](docs/CategoriesApi.md#fetchAllEventsCategories) | **GET** /events/{event_id}/categories | Find all categories for one event
*Pims.CategoriesApi* | [**fetchOneCategory**](docs/CategoriesApi.md#fetchOneCategory) | **GET** /categories/{category_id} | Get one category by ID
*Pims.CategoriesApi* | [**fetchOneEventCategory**](docs/CategoriesApi.md#fetchOneEventCategory) | **GET** /events/{event_id}/categories/{category_id} | Get one event category by ID
*Pims.ChannelsApi* | [**fetchAllChannels**](docs/ChannelsApi.md#fetchAllChannels) | **GET** /channels | Find all channels
*Pims.ChannelsApi* | [**fetchAllEventsChannels**](docs/ChannelsApi.md#fetchAllEventsChannels) | **GET** /events/{event_id}/channels | Find all channels for one event
*Pims.ChannelsApi* | [**fetchOneChannel**](docs/ChannelsApi.md#fetchOneChannel) | **GET** /channels/{channel_id} | Get one channel by ID
*Pims.ChannelsApi* | [**fetchOneEventChannel**](docs/ChannelsApi.md#fetchOneEventChannel) | **GET** /events/{event_id}/channels/{channel_id} | Get one event channel by ID
*Pims.CountsApi* | [**fetchAllDetailedTicketCounts**](docs/CountsApi.md#fetchAllDetailedTicketCounts) | **GET** /events/{event_id}/ticket-counts/detailed | Find all detailed ticket counts for one event
*Pims.CountsApi* | [**fetchAllTicketCounts**](docs/CountsApi.md#fetchAllTicketCounts) | **GET** /events/{event_id}/ticket-counts | Find all ticket counts for one event
*Pims.CountsApi* | [**fetchOneDetailedTicketCount**](docs/CountsApi.md#fetchOneDetailedTicketCount) | **GET** /events/{event_id}/ticket-counts/detailed/{ticket_count_id} | Get one detailed ticket count by ID
*Pims.CountsApi* | [**fetchOneTicketCount**](docs/CountsApi.md#fetchOneTicketCount) | **GET** /events/{event_id}/ticket-counts/{ticket_count_id} | Get one ticket count by ID
*Pims.EventsApi* | [**fetchAllEvents**](docs/EventsApi.md#fetchAllEvents) | **GET** /events | Find all events
*Pims.EventsApi* | [**fetchAllSeriesEvents**](docs/EventsApi.md#fetchAllSeriesEvents) | **GET** /series/{series_id}/events | Find all events for one series
*Pims.EventsApi* | [**fetchAllVenuesEvents**](docs/EventsApi.md#fetchAllVenuesEvents) | **GET** /venues/{venue_id}/events | Find all events for one venue
*Pims.EventsApi* | [**fetchOneEvent**](docs/EventsApi.md#fetchOneEvent) | **GET** /events/{event_id} | Get one event by ID
*Pims.PriceRangesApi* | [**fetchAllPriceRanges**](docs/PriceRangesApi.md#fetchAllPriceRanges) | **GET** /price-ranges | Find all price ranges
*Pims.PriceRangesApi* | [**fetchOnePriceRange**](docs/PriceRangesApi.md#fetchOnePriceRange) | **GET** /price-ranges/{price_range_id} | Get one price range by ID
*Pims.PromotionsApi* | [**fetchAllEventsPromotions**](docs/PromotionsApi.md#fetchAllEventsPromotions) | **GET** /events/{event_id}/promotions | Find all promotions for one event
*Pims.PromotionsApi* | [**fetchAllPromotions**](docs/PromotionsApi.md#fetchAllPromotions) | **GET** /promotions | Find all promotions
*Pims.PromotionsApi* | [**fetchAllSeriesPromotions**](docs/PromotionsApi.md#fetchAllSeriesPromotions) | **GET** /series/{series_id}/promotions | Find all promotions for one series
*Pims.PromotionsApi* | [**fetchOnePromotion**](docs/PromotionsApi.md#fetchOnePromotion) | **GET** /promotions/{promotion_id} | Get one promotion by ID
*Pims.SeriesApi* | [**fetchAllSeries**](docs/SeriesApi.md#fetchAllSeries) | **GET** /series | Find all series
*Pims.SeriesApi* | [**fetchOneSeries**](docs/SeriesApi.md#fetchOneSeries) | **GET** /series/{series_id} | Get one series by ID
*Pims.VenuesApi* | [**fetchAllVenues**](docs/VenuesApi.md#fetchAllVenues) | **GET** /venues | Find all venues
*Pims.VenuesApi* | [**fetchOneVenue**](docs/VenuesApi.md#fetchOneVenue) | **GET** /venues/{venue_id} | Get one venue by ID


## Documentation for Models

 - [Pims.CategoriesEntity](docs/CategoriesEntity.md)
 - [Pims.ChannelsEntity](docs/ChannelsEntity.md)
 - [Pims.Error401](docs/Error401.md)
 - [Pims.Error403](docs/Error403.md)
 - [Pims.Error404](docs/Error404.md)
 - [Pims.Error422](docs/Error422.md)
 - [Pims.Error500](docs/Error500.md)
 - [Pims.EventsCapacitiesEntity](docs/EventsCapacitiesEntity.md)
 - [Pims.EventsCapacitiesEntityEventCategoriesInner](docs/EventsCapacitiesEntityEventCategoriesInner.md)
 - [Pims.EventsCategoriesEntity](docs/EventsCategoriesEntity.md)
 - [Pims.EventsCategoriesEntityEventPriceRangesInner](docs/EventsCategoriesEntityEventPriceRangesInner.md)
 - [Pims.EventsChannelsEntity](docs/EventsChannelsEntity.md)
 - [Pims.EventsEntity](docs/EventsEntity.md)
 - [Pims.EventsEntityContract](docs/EventsEntityContract.md)
 - [Pims.EventsEntityContractPartner](docs/EventsEntityContractPartner.md)
 - [Pims.EventsEntityContractType](docs/EventsEntityContractType.md)
 - [Pims.EventsEntityInputType](docs/EventsEntityInputType.md)
 - [Pims.PriceRangesEntity](docs/PriceRangesEntity.md)
 - [Pims.PromotionsEntity](docs/PromotionsEntity.md)
 - [Pims.PromotionsEntityAppliedToInner](docs/PromotionsEntityAppliedToInner.md)
 - [Pims.PromotionsEntityCost](docs/PromotionsEntityCost.md)
 - [Pims.PromotionsEntityCostState](docs/PromotionsEntityCostState.md)
 - [Pims.PromotionsEntityCostType](docs/PromotionsEntityCostType.md)
 - [Pims.PromotionsEntitySupplier](docs/PromotionsEntitySupplier.md)
 - [Pims.PromotionsEntityType](docs/PromotionsEntityType.md)
 - [Pims.PromotionsEntityTypeFamily](docs/PromotionsEntityTypeFamily.md)
 - [Pims.SeriesEntity](docs/SeriesEntity.md)
 - [Pims.SeriesEntityContract](docs/SeriesEntityContract.md)
 - [Pims.SeriesEntityContractPartner](docs/SeriesEntityContractPartner.md)
 - [Pims.SeriesEntityContractType](docs/SeriesEntityContractType.md)
 - [Pims.SeriesEntityType](docs/SeriesEntityType.md)
 - [Pims.TicketCountsDetailedEntity](docs/TicketCountsDetailedEntity.md)
 - [Pims.TicketCountsDetailedEntityEventChannelsInner](docs/TicketCountsDetailedEntityEventChannelsInner.md)
 - [Pims.TicketCountsDetailedEntityEventChannelsInnerEventCategoriesInner](docs/TicketCountsDetailedEntityEventChannelsInnerEventCategoriesInner.md)
 - [Pims.TicketCountsDetailedEntityEventChannelsInnerEventCategoriesInnerEventPriceRangesInner](docs/TicketCountsDetailedEntityEventChannelsInnerEventCategoriesInnerEventPriceRangesInner.md)
 - [Pims.TicketCountsEntity](docs/TicketCountsEntity.md)
 - [Pims.VenuesEntity](docs/VenuesEntity.md)
 - [Pims.VenuesEntityType](docs/VenuesEntityType.md)


## Documentation for Authorization


Authentication schemes defined for the API:
### Basic Auth

- **Type**: HTTP basic authentication

