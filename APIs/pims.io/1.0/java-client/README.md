# openapi-java-client

Pims
- API version: 1.0
  - Build date: 2024-10-12T10:12:11.901875-04:00[America/New_York]
  - Generator version: 7.9.0


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


*Automatically generated by the [OpenAPI Generator](https://openapi-generator.tech)*


## Requirements

Building the API client library requires:
1. Java 1.8+
2. Maven (3.8.3+)/Gradle (7.2+)

## Installation

To install the API client library to your local Maven repository, simply execute:

```shell
mvn clean install
```

To deploy it to a remote Maven repository instead, configure the settings of the repository and execute:

```shell
mvn clean deploy
```

Refer to the [OSSRH Guide](http://central.sonatype.org/pages/ossrh-guide.html) for more information.

### Maven users

Add this dependency to your project's POM:

```xml
<dependency>
  <groupId>org.openapitools</groupId>
  <artifactId>openapi-java-client</artifactId>
  <version>1.0</version>
  <scope>compile</scope>
</dependency>
```

### Gradle users

Add this dependency to your project's build file:

```groovy
  repositories {
    mavenCentral()     // Needed if the 'openapi-java-client' jar has been published to maven central.
    mavenLocal()       // Needed if the 'openapi-java-client' jar has been published to the local maven repo.
  }

  dependencies {
     implementation "org.openapitools:openapi-java-client:1.0"
  }
```

### Others

At first generate the JAR by executing:

```shell
mvn clean package
```

Then manually install the following JARs:

* `target/openapi-java-client-1.0.jar`
* `target/lib/*.jar`

## Getting Started

Please follow the [installation](#installation) instruction and execute the following Java code:

```java

// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.model.*;
import org.openapitools.client.api.CapacitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.pims.io/api/v1");
    
    // Configure HTTP basic authorization: Basic Auth
    HttpBasicAuth Basic Auth = (HttpBasicAuth) defaultClient.getAuthentication("Basic Auth");
    Basic Auth.setUsername("YOUR USERNAME");
    Basic Auth.setPassword("YOUR PASSWORD");

    CapacitiesApi apiInstance = new CapacitiesApi(defaultClient);
    Integer eventId = 56; // Integer | ID of the targeted event.
    Boolean showIgnored = false; // Boolean | If set to `false`, show only the [event-]categories which are not ignored. If set to `true`, show everything.
    String sort = "date"; // String | Sort the capacities in the corresponding order.
    Integer pageSize = 25; // Integer | Pagination size, i.e. maximum number of items to be displayed in the response.
    try {
      List<EventsCapacitiesEntity> result = apiInstance.fetchAllEventsCapacities(eventId, showIgnored, sort, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CapacitiesApi#fetchAllEventsCapacities");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

## Documentation for API Endpoints

All URIs are relative to *https://demo.pims.io/api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CapacitiesApi* | [**fetchAllEventsCapacities**](docs/CapacitiesApi.md#fetchAllEventsCapacities) | **GET** /events/{event_id}/capacities | Find all capacities for one event
*CapacitiesApi* | [**fetchOneEventCapacity**](docs/CapacitiesApi.md#fetchOneEventCapacity) | **GET** /events/{event_id}/capacities/{capacity_id} | Get one capacity by ID
*CategoriesApi* | [**fetchAllCategories**](docs/CategoriesApi.md#fetchAllCategories) | **GET** /categories | Find all categories
*CategoriesApi* | [**fetchAllEventsCategories**](docs/CategoriesApi.md#fetchAllEventsCategories) | **GET** /events/{event_id}/categories | Find all categories for one event
*CategoriesApi* | [**fetchOneCategory**](docs/CategoriesApi.md#fetchOneCategory) | **GET** /categories/{category_id} | Get one category by ID
*CategoriesApi* | [**fetchOneEventCategory**](docs/CategoriesApi.md#fetchOneEventCategory) | **GET** /events/{event_id}/categories/{category_id} | Get one event category by ID
*ChannelsApi* | [**fetchAllChannels**](docs/ChannelsApi.md#fetchAllChannels) | **GET** /channels | Find all channels
*ChannelsApi* | [**fetchAllEventsChannels**](docs/ChannelsApi.md#fetchAllEventsChannels) | **GET** /events/{event_id}/channels | Find all channels for one event
*ChannelsApi* | [**fetchOneChannel**](docs/ChannelsApi.md#fetchOneChannel) | **GET** /channels/{channel_id} | Get one channel by ID
*ChannelsApi* | [**fetchOneEventChannel**](docs/ChannelsApi.md#fetchOneEventChannel) | **GET** /events/{event_id}/channels/{channel_id} | Get one event channel by ID
*CountsApi* | [**fetchAllDetailedTicketCounts**](docs/CountsApi.md#fetchAllDetailedTicketCounts) | **GET** /events/{event_id}/ticket-counts/detailed | Find all detailed ticket counts for one event
*CountsApi* | [**fetchAllTicketCounts**](docs/CountsApi.md#fetchAllTicketCounts) | **GET** /events/{event_id}/ticket-counts | Find all ticket counts for one event
*CountsApi* | [**fetchOneDetailedTicketCount**](docs/CountsApi.md#fetchOneDetailedTicketCount) | **GET** /events/{event_id}/ticket-counts/detailed/{ticket_count_id} | Get one detailed ticket count by ID
*CountsApi* | [**fetchOneTicketCount**](docs/CountsApi.md#fetchOneTicketCount) | **GET** /events/{event_id}/ticket-counts/{ticket_count_id} | Get one ticket count by ID
*EventsApi* | [**fetchAllEvents**](docs/EventsApi.md#fetchAllEvents) | **GET** /events | Find all events
*EventsApi* | [**fetchAllSeriesEvents**](docs/EventsApi.md#fetchAllSeriesEvents) | **GET** /series/{series_id}/events | Find all events for one series
*EventsApi* | [**fetchAllVenuesEvents**](docs/EventsApi.md#fetchAllVenuesEvents) | **GET** /venues/{venue_id}/events | Find all events for one venue
*EventsApi* | [**fetchOneEvent**](docs/EventsApi.md#fetchOneEvent) | **GET** /events/{event_id} | Get one event by ID
*PriceRangesApi* | [**fetchAllPriceRanges**](docs/PriceRangesApi.md#fetchAllPriceRanges) | **GET** /price-ranges | Find all price ranges
*PriceRangesApi* | [**fetchOnePriceRange**](docs/PriceRangesApi.md#fetchOnePriceRange) | **GET** /price-ranges/{price_range_id} | Get one price range by ID
*PromotionsApi* | [**fetchAllEventsPromotions**](docs/PromotionsApi.md#fetchAllEventsPromotions) | **GET** /events/{event_id}/promotions | Find all promotions for one event
*PromotionsApi* | [**fetchAllPromotions**](docs/PromotionsApi.md#fetchAllPromotions) | **GET** /promotions | Find all promotions
*PromotionsApi* | [**fetchAllSeriesPromotions**](docs/PromotionsApi.md#fetchAllSeriesPromotions) | **GET** /series/{series_id}/promotions | Find all promotions for one series
*PromotionsApi* | [**fetchOnePromotion**](docs/PromotionsApi.md#fetchOnePromotion) | **GET** /promotions/{promotion_id} | Get one promotion by ID
*SeriesApi* | [**fetchAllSeries**](docs/SeriesApi.md#fetchAllSeries) | **GET** /series | Find all series
*SeriesApi* | [**fetchOneSeries**](docs/SeriesApi.md#fetchOneSeries) | **GET** /series/{series_id} | Get one series by ID
*VenuesApi* | [**fetchAllVenues**](docs/VenuesApi.md#fetchAllVenues) | **GET** /venues | Find all venues
*VenuesApi* | [**fetchOneVenue**](docs/VenuesApi.md#fetchOneVenue) | **GET** /venues/{venue_id} | Get one venue by ID


## Documentation for Models

 - [CategoriesEntity](docs/CategoriesEntity.md)
 - [ChannelsEntity](docs/ChannelsEntity.md)
 - [Error401](docs/Error401.md)
 - [Error403](docs/Error403.md)
 - [Error404](docs/Error404.md)
 - [Error422](docs/Error422.md)
 - [Error500](docs/Error500.md)
 - [EventsCapacitiesEntity](docs/EventsCapacitiesEntity.md)
 - [EventsCapacitiesEntityEventCategoriesInner](docs/EventsCapacitiesEntityEventCategoriesInner.md)
 - [EventsCategoriesEntity](docs/EventsCategoriesEntity.md)
 - [EventsCategoriesEntityEventPriceRangesInner](docs/EventsCategoriesEntityEventPriceRangesInner.md)
 - [EventsChannelsEntity](docs/EventsChannelsEntity.md)
 - [EventsEntity](docs/EventsEntity.md)
 - [EventsEntityContract](docs/EventsEntityContract.md)
 - [EventsEntityContractPartner](docs/EventsEntityContractPartner.md)
 - [EventsEntityContractType](docs/EventsEntityContractType.md)
 - [EventsEntityInputType](docs/EventsEntityInputType.md)
 - [PriceRangesEntity](docs/PriceRangesEntity.md)
 - [PromotionsEntity](docs/PromotionsEntity.md)
 - [PromotionsEntityAppliedToInner](docs/PromotionsEntityAppliedToInner.md)
 - [PromotionsEntityCost](docs/PromotionsEntityCost.md)
 - [PromotionsEntityCostState](docs/PromotionsEntityCostState.md)
 - [PromotionsEntityCostType](docs/PromotionsEntityCostType.md)
 - [PromotionsEntitySupplier](docs/PromotionsEntitySupplier.md)
 - [PromotionsEntityType](docs/PromotionsEntityType.md)
 - [PromotionsEntityTypeFamily](docs/PromotionsEntityTypeFamily.md)
 - [SeriesEntity](docs/SeriesEntity.md)
 - [SeriesEntityContract](docs/SeriesEntityContract.md)
 - [SeriesEntityContractPartner](docs/SeriesEntityContractPartner.md)
 - [SeriesEntityContractType](docs/SeriesEntityContractType.md)
 - [SeriesEntityType](docs/SeriesEntityType.md)
 - [TicketCountsDetailedEntity](docs/TicketCountsDetailedEntity.md)
 - [TicketCountsDetailedEntityEventChannelsInner](docs/TicketCountsDetailedEntityEventChannelsInner.md)
 - [TicketCountsDetailedEntityEventChannelsInnerEventCategoriesInner](docs/TicketCountsDetailedEntityEventChannelsInnerEventCategoriesInner.md)
 - [TicketCountsDetailedEntityEventChannelsInnerEventCategoriesInnerEventPriceRangesInner](docs/TicketCountsDetailedEntityEventChannelsInnerEventCategoriesInnerEventPriceRangesInner.md)
 - [TicketCountsEntity](docs/TicketCountsEntity.md)
 - [VenuesEntity](docs/VenuesEntity.md)
 - [VenuesEntityType](docs/VenuesEntityType.md)


<a id="documentation-for-authorization"></a>
## Documentation for Authorization


Authentication schemes defined for the API:
<a id="Basic Auth"></a>
### Basic Auth

- **Type**: HTTP basic authentication


## Recommendation

It's recommended to create an instance of `ApiClient` per thread in a multithreaded environment to avoid any potential issues.

## Author

support@pims.io

