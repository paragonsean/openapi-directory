/**
 * Pims
 *  Hereafter is the documentation of the private API of [Pims: Pointages Intelligents pour le Monde du Spectacle](https://pims.io). This API is designed for 3rd-party softwares, editors and partners. Its main purpose is to give access the core data of a Pims customer (i.e. events, ticket counts and promotions).  ## Authentication The API uses [basic access authentication](https://en.wikipedia.org/wiki/Basic_access_authentication), meaning you will need a username and password to get authorized.  As each customer in Pims has its own domain (e.g. caramba.pims.io, gdp.pims.io...), each credentials will be valid for one domain/customer only. If you need dedicated credentials for one domain, please contact us. (In any case, we will need an explicit agreement from the customer before we create these credentials.)  <div class=\"info\"> To make your life easy, you can try all endpoints with the public credentials below, pointing to our [demo domain](https://demo.pims.io):   <ul>     <li>Base path: `https://demo.pims.io/api`</li>     <li>Username: `demo`</li>     <li>Password: `q83792db2GCvgYVdKpU3yG3R`</li>   </ul> </div>  ## Response format The API returns JSON and matches the [HAL specification](http://stateless.co/hal_specification.html). The `Content-Type` of each response will be `application/hal+json`, unless an error occurs.  Please note that this documentation describes all responses “as if” they were plain JSON. The specificities of HAL are ignored on purpose, in order to remain compact and avoid repetition. <div style=\"-webkit-column-count: 2; -moz-column-count: 2; column-count: 2; -webkit-column-rule: 1px dotted #e0e0e0; -moz-column-rule: 1px dotted #e0e0e0; column-rule: 1px dotted #e0e0e0;\">  <div style=\"display: inline-block; width:100%;\">   <strong>So when you read in the doc:</strong> <pre><code class=\"lang-json\">{  <span class=\"token string\">\"id\"</span>: <span class=\"token number\">123</span>,  <span class=\"token string\">\"property1\"</span>: <span class=\"token string\">\"Lorem ipsum\"</span>,  <span class=\"token string\">\"object\"</span>: {   <span class=\"token string\">\"id\"</span>: <span class=\"token number\">456</span>,   <span class=\"token string\">\"property2\"</span>: <span class=\"token number\">7.89</span>  } }</code></pre>  </div>  <div style=\"display: inline-block; width:100%;\">   <strong>... you'll get in the Real World®:</strong> <pre><code class=\"lang-json\">{  <span class=\"token string\">\"id\"</span>: <span class=\"token number\">123</span>,  <span class=\"token string\">\"property2\"</span>: <span class=\"token string\">\"Lorem ipsum\"</span>,  <span class=\"token string\">\"_embedded\"</span>: {   <span class=\"token string\">\"object\"</span>: {    <span class=\"token string\">\"id\"</span>: <span class=\"token number\">456</span>,    <span class=\"token string\">\"property2\"</span>: <span class=\"token number\">7.89</span>,    <span class=\"token string\">\"_links\"</span>: {     <span class=\"token string\">\"self\"</span>: {      <span class=\"token string\">\"href\"</span>: <span class=\"token string\">\"https://api.mydomain.com/other-item/456\"</span>     }    }   }  }  <span class=\"token string\">\"_links\"</span>: {   <span class=\"token string\">\"self\"</span>: {    <span class=\"token string\">\"href\"</span>: <span class=\"token string\">\"https://api.mydomain.com/item/123\"</span>   }  } }</code></pre>  </div> </div>  ### Errors Errors return JSON too and tries to match the [Problem Details for HTTP APIs specification](https://tools.ietf.org/html/rfc7807). If it does not match this spec, that's either a bug or a compatibility issue. Please contact us to solve the problem.  The `Content-Type` of errors will be `application/problem+json`. The content will match the following JSON: ```json {  \"type\": \"https://tools.ietf.org/html/rfc2616#section-10\",     \"title\": \"Not Found\",  \"status\": 404,     \"detail\": \"Entity not found\" } ```  ## Versioning The API is fully versionned, using an URL-versioning scheme: `https://demo.pims.io/api/v1/events`, `https://demo.pims.io/api/v2/events`,...  The version part of the URL is optional, and will be completed with the last stable version if omitted.  ## Pagination All responses corresponding to a collection of resources (e.g. `/venues` or `/series/:id/events`) are paginated. When so, you will only get the first 25 resources you asked for.  If you need to get more resources in one call, you can use the `page_size` query parameter. E.g. `/venues?page_size=50` to get the 50 first venues.  Also note that with HAL, the navigation in paginated responses is a piece of cake, as you can see below: ```json {  \"_links\": {   \"self\": {    \"href\": \"https://demo.pims.io/api/v1/events?page=1\"   },   \"first\": {    \"href\": \"https://demo.pims.io/api/v1/events\"   },   \"last\": {    \"href\": \"https://demo.pims.io/api/v1/events?page=14\"   },   \"next\": {    \"href\": \"https://demo.pims.io/api/v1/events?page=2\"   }  },  \"_embedded\": {    ... // data content goes here  },  \"page_count\": 14,  \"page_size\": 25,  \"total_items\": 331,  \"page\": 1 } ```  ## Filtering and sorting Every textual filter (e.g. `/events?label=U2`) and/or sort (e.g. `/events?sort=label`) performed with the API uses UTF8_UNICODE_CI collation, meaning it is: - Case insensitive: “Chloé” will be considered the same as “CHLOÉ”; - Diacritic insensitive: “Chloé” will be considered the same as “Chloe”.  When performing a sort, it will always be *ascending* by default. To make it *descending*, just use a minus sign (`-`) in front of the parameter value (e.g. `/events?sort=-label`).  ## I18n In responses, some labels can be translated (e.g. promotion types, event input types, etc.). These translatable labels are clearly indicated in the documentation below.  By default, they will be displayed in English, but you can change this behaviour via the `Accept-Language` header. E.g., use `fr` as a value for French.  ## PHP SDK We provide a simple yet convenient SDK for the PHP language, see [the Github page of the project](https://github.com/pimssas/pims-api-client-php).  ## And now? Generaly, you will start by [fetching one or more events](#tag/Events). An <span class=\"definition\">event</span> can be anything that occurs in one venue at one given date and time: a concert, a play, a match, a conference, etc. Additionnally, you can explore the [series](#tag/Series): a <span class=\"definition\">series</span> is just a group of events (e.g. a tour or a festival).  Once you retrieved the events you were interested in, you can look for the sales (<span class=\"definition\">ticket counts</span>): - Get a quick overview with [`/events/:id/ticket-counts`](#operation/fetchAllTicketCounts) - Or get a full insight by calling these endpoints:     1. [`/events/:id/categories`](#operation/fetchAllEventsCategories)     2. [`/events/:id/channels`](#operation/fetchAllEventsChannels)     3. [`/events/:id/ticket-counts/detailed`](#operation/fetchAllDetailedTicketCounts)  Eventually, you may also want to fetch the [promotions](#tag/Promotions). A <span class=\"definition\">promotion</span> can be anything meant to leverage the sales: ads, marketing campaigns, buzz or news around the event, etc. A promotion can be linked to any combination of events and/or series.
 *
 * The version of the OpenAPI document: 1.0
 * Contact: support@pims.io
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import CategoriesEntity from './model/CategoriesEntity';
import ChannelsEntity from './model/ChannelsEntity';
import Error401 from './model/Error401';
import Error403 from './model/Error403';
import Error404 from './model/Error404';
import Error422 from './model/Error422';
import Error500 from './model/Error500';
import EventsCapacitiesEntity from './model/EventsCapacitiesEntity';
import EventsCapacitiesEntityEventCategoriesInner from './model/EventsCapacitiesEntityEventCategoriesInner';
import EventsCategoriesEntity from './model/EventsCategoriesEntity';
import EventsCategoriesEntityEventPriceRangesInner from './model/EventsCategoriesEntityEventPriceRangesInner';
import EventsChannelsEntity from './model/EventsChannelsEntity';
import EventsEntity from './model/EventsEntity';
import EventsEntityContract from './model/EventsEntityContract';
import EventsEntityContractPartner from './model/EventsEntityContractPartner';
import EventsEntityContractType from './model/EventsEntityContractType';
import EventsEntityInputType from './model/EventsEntityInputType';
import PriceRangesEntity from './model/PriceRangesEntity';
import PromotionsEntity from './model/PromotionsEntity';
import PromotionsEntityAppliedToInner from './model/PromotionsEntityAppliedToInner';
import PromotionsEntityCost from './model/PromotionsEntityCost';
import PromotionsEntityCostState from './model/PromotionsEntityCostState';
import PromotionsEntityCostType from './model/PromotionsEntityCostType';
import PromotionsEntitySupplier from './model/PromotionsEntitySupplier';
import PromotionsEntityType from './model/PromotionsEntityType';
import PromotionsEntityTypeFamily from './model/PromotionsEntityTypeFamily';
import SeriesEntity from './model/SeriesEntity';
import SeriesEntityContract from './model/SeriesEntityContract';
import SeriesEntityContractPartner from './model/SeriesEntityContractPartner';
import SeriesEntityContractType from './model/SeriesEntityContractType';
import SeriesEntityType from './model/SeriesEntityType';
import TicketCountsDetailedEntity from './model/TicketCountsDetailedEntity';
import TicketCountsDetailedEntityEventChannelsInner from './model/TicketCountsDetailedEntityEventChannelsInner';
import TicketCountsDetailedEntityEventChannelsInnerEventCategoriesInner from './model/TicketCountsDetailedEntityEventChannelsInnerEventCategoriesInner';
import TicketCountsDetailedEntityEventChannelsInnerEventCategoriesInnerEventPriceRangesInner from './model/TicketCountsDetailedEntityEventChannelsInnerEventCategoriesInnerEventPriceRangesInner';
import TicketCountsEntity from './model/TicketCountsEntity';
import VenuesEntity from './model/VenuesEntity';
import VenuesEntityType from './model/VenuesEntityType';
import CapacitiesApi from './api/CapacitiesApi';
import CategoriesApi from './api/CategoriesApi';
import ChannelsApi from './api/ChannelsApi';
import CountsApi from './api/CountsApi';
import EventsApi from './api/EventsApi';
import PriceRangesApi from './api/PriceRangesApi';
import PromotionsApi from './api/PromotionsApi';
import SeriesApi from './api/SeriesApi';
import VenuesApi from './api/VenuesApi';


/**
*  Hereafter is the documentation of the private API of [Pims: Pointages Intelligents pour le Monde du Spectacle](https://pims.io). This API is designed for 3rd-party softwares, editors and partners. Its main purpose is to give access the core data of a Pims customer (i.e. events, ticket counts and promotions).  ## Authentication The API uses [basic access authentication](https://en.wikipedia.org/wiki/Basic_access_authentication), meaning you will need a username and password to get authorized.  As each customer in Pims has its own domain (e.g. caramba.pims.io, gdp.pims.io...), each credentials will be valid for one domain/customer only. If you need dedicated credentials for one domain, please contact us. (In any case, we will need an explicit agreement from the customer before we create these credentials.)  &lt;div class&#x3D;\&quot;info\&quot;&gt; To make your life easy, you can try all endpoints with the public credentials below, pointing to our [demo domain](https://demo.pims.io):   &lt;ul&gt;     &lt;li&gt;Base path: &#x60;https://demo.pims.io/api&#x60;&lt;/li&gt;     &lt;li&gt;Username: &#x60;demo&#x60;&lt;/li&gt;     &lt;li&gt;Password: &#x60;q83792db2GCvgYVdKpU3yG3R&#x60;&lt;/li&gt;   &lt;/ul&gt; &lt;/div&gt;  ## Response format The API returns JSON and matches the [HAL specification](http://stateless.co/hal_specification.html). The &#x60;Content-Type&#x60; of each response will be &#x60;application/hal+json&#x60;, unless an error occurs.  Please note that this documentation describes all responses “as if” they were plain JSON. The specificities of HAL are ignored on purpose, in order to remain compact and avoid repetition. &lt;div style&#x3D;\&quot;-webkit-column-count: 2; -moz-column-count: 2; column-count: 2; -webkit-column-rule: 1px dotted #e0e0e0; -moz-column-rule: 1px dotted #e0e0e0; column-rule: 1px dotted #e0e0e0;\&quot;&gt;  &lt;div style&#x3D;\&quot;display: inline-block; width:100%;\&quot;&gt;   &lt;strong&gt;So when you read in the doc:&lt;/strong&gt; &lt;pre&gt;&lt;code class&#x3D;\&quot;lang-json\&quot;&gt;{  &lt;span class&#x3D;\&quot;token string\&quot;&gt;\&quot;id\&quot;&lt;/span&gt;: &lt;span class&#x3D;\&quot;token number\&quot;&gt;123&lt;/span&gt;,  &lt;span class&#x3D;\&quot;token string\&quot;&gt;\&quot;property1\&quot;&lt;/span&gt;: &lt;span class&#x3D;\&quot;token string\&quot;&gt;\&quot;Lorem ipsum\&quot;&lt;/span&gt;,  &lt;span class&#x3D;\&quot;token string\&quot;&gt;\&quot;object\&quot;&lt;/span&gt;: {   &lt;span class&#x3D;\&quot;token string\&quot;&gt;\&quot;id\&quot;&lt;/span&gt;: &lt;span class&#x3D;\&quot;token number\&quot;&gt;456&lt;/span&gt;,   &lt;span class&#x3D;\&quot;token string\&quot;&gt;\&quot;property2\&quot;&lt;/span&gt;: &lt;span class&#x3D;\&quot;token number\&quot;&gt;7.89&lt;/span&gt;  } }&lt;/code&gt;&lt;/pre&gt;  &lt;/div&gt;  &lt;div style&#x3D;\&quot;display: inline-block; width:100%;\&quot;&gt;   &lt;strong&gt;... you&#39;ll get in the Real World®:&lt;/strong&gt; &lt;pre&gt;&lt;code class&#x3D;\&quot;lang-json\&quot;&gt;{  &lt;span class&#x3D;\&quot;token string\&quot;&gt;\&quot;id\&quot;&lt;/span&gt;: &lt;span class&#x3D;\&quot;token number\&quot;&gt;123&lt;/span&gt;,  &lt;span class&#x3D;\&quot;token string\&quot;&gt;\&quot;property2\&quot;&lt;/span&gt;: &lt;span class&#x3D;\&quot;token string\&quot;&gt;\&quot;Lorem ipsum\&quot;&lt;/span&gt;,  &lt;span class&#x3D;\&quot;token string\&quot;&gt;\&quot;_embedded\&quot;&lt;/span&gt;: {   &lt;span class&#x3D;\&quot;token string\&quot;&gt;\&quot;object\&quot;&lt;/span&gt;: {    &lt;span class&#x3D;\&quot;token string\&quot;&gt;\&quot;id\&quot;&lt;/span&gt;: &lt;span class&#x3D;\&quot;token number\&quot;&gt;456&lt;/span&gt;,    &lt;span class&#x3D;\&quot;token string\&quot;&gt;\&quot;property2\&quot;&lt;/span&gt;: &lt;span class&#x3D;\&quot;token number\&quot;&gt;7.89&lt;/span&gt;,    &lt;span class&#x3D;\&quot;token string\&quot;&gt;\&quot;_links\&quot;&lt;/span&gt;: {     &lt;span class&#x3D;\&quot;token string\&quot;&gt;\&quot;self\&quot;&lt;/span&gt;: {      &lt;span class&#x3D;\&quot;token string\&quot;&gt;\&quot;href\&quot;&lt;/span&gt;: &lt;span class&#x3D;\&quot;token string\&quot;&gt;\&quot;https://api.mydomain.com/other-item/456\&quot;&lt;/span&gt;     }    }   }  }  &lt;span class&#x3D;\&quot;token string\&quot;&gt;\&quot;_links\&quot;&lt;/span&gt;: {   &lt;span class&#x3D;\&quot;token string\&quot;&gt;\&quot;self\&quot;&lt;/span&gt;: {    &lt;span class&#x3D;\&quot;token string\&quot;&gt;\&quot;href\&quot;&lt;/span&gt;: &lt;span class&#x3D;\&quot;token string\&quot;&gt;\&quot;https://api.mydomain.com/item/123\&quot;&lt;/span&gt;   }  } }&lt;/code&gt;&lt;/pre&gt;  &lt;/div&gt; &lt;/div&gt;  ### Errors Errors return JSON too and tries to match the [Problem Details for HTTP APIs specification](https://tools.ietf.org/html/rfc7807). If it does not match this spec, that&#39;s either a bug or a compatibility issue. Please contact us to solve the problem.  The &#x60;Content-Type&#x60; of errors will be &#x60;application/problem+json&#x60;. The content will match the following JSON: &#x60;&#x60;&#x60;json {  \&quot;type\&quot;: \&quot;https://tools.ietf.org/html/rfc2616#section-10\&quot;,     \&quot;title\&quot;: \&quot;Not Found\&quot;,  \&quot;status\&quot;: 404,     \&quot;detail\&quot;: \&quot;Entity not found\&quot; } &#x60;&#x60;&#x60;  ## Versioning The API is fully versionned, using an URL-versioning scheme: &#x60;https://demo.pims.io/api/v1/events&#x60;, &#x60;https://demo.pims.io/api/v2/events&#x60;,...  The version part of the URL is optional, and will be completed with the last stable version if omitted.  ## Pagination All responses corresponding to a collection of resources (e.g. &#x60;/venues&#x60; or &#x60;/series/:id/events&#x60;) are paginated. When so, you will only get the first 25 resources you asked for.  If you need to get more resources in one call, you can use the &#x60;page_size&#x60; query parameter. E.g. &#x60;/venues?page_size&#x3D;50&#x60; to get the 50 first venues.  Also note that with HAL, the navigation in paginated responses is a piece of cake, as you can see below: &#x60;&#x60;&#x60;json {  \&quot;_links\&quot;: {   \&quot;self\&quot;: {    \&quot;href\&quot;: \&quot;https://demo.pims.io/api/v1/events?page&#x3D;1\&quot;   },   \&quot;first\&quot;: {    \&quot;href\&quot;: \&quot;https://demo.pims.io/api/v1/events\&quot;   },   \&quot;last\&quot;: {    \&quot;href\&quot;: \&quot;https://demo.pims.io/api/v1/events?page&#x3D;14\&quot;   },   \&quot;next\&quot;: {    \&quot;href\&quot;: \&quot;https://demo.pims.io/api/v1/events?page&#x3D;2\&quot;   }  },  \&quot;_embedded\&quot;: {    ... // data content goes here  },  \&quot;page_count\&quot;: 14,  \&quot;page_size\&quot;: 25,  \&quot;total_items\&quot;: 331,  \&quot;page\&quot;: 1 } &#x60;&#x60;&#x60;  ## Filtering and sorting Every textual filter (e.g. &#x60;/events?label&#x3D;U2&#x60;) and/or sort (e.g. &#x60;/events?sort&#x3D;label&#x60;) performed with the API uses UTF8_UNICODE_CI collation, meaning it is: - Case insensitive: “Chloé” will be considered the same as “CHLOÉ”; - Diacritic insensitive: “Chloé” will be considered the same as “Chloe”.  When performing a sort, it will always be *ascending* by default. To make it *descending*, just use a minus sign (&#x60;-&#x60;) in front of the parameter value (e.g. &#x60;/events?sort&#x3D;-label&#x60;).  ## I18n In responses, some labels can be translated (e.g. promotion types, event input types, etc.). These translatable labels are clearly indicated in the documentation below.  By default, they will be displayed in English, but you can change this behaviour via the &#x60;Accept-Language&#x60; header. E.g., use &#x60;fr&#x60; as a value for French.  ## PHP SDK We provide a simple yet convenient SDK for the PHP language, see [the Github page of the project](https://github.com/pimssas/pims-api-client-php).  ## And now? Generaly, you will start by [fetching one or more events](#tag/Events). An &lt;span class&#x3D;\&quot;definition\&quot;&gt;event&lt;/span&gt; can be anything that occurs in one venue at one given date and time: a concert, a play, a match, a conference, etc. Additionnally, you can explore the [series](#tag/Series): a &lt;span class&#x3D;\&quot;definition\&quot;&gt;series&lt;/span&gt; is just a group of events (e.g. a tour or a festival).  Once you retrieved the events you were interested in, you can look for the sales (&lt;span class&#x3D;\&quot;definition\&quot;&gt;ticket counts&lt;/span&gt;): - Get a quick overview with [&#x60;/events/:id/ticket-counts&#x60;](#operation/fetchAllTicketCounts) - Or get a full insight by calling these endpoints:     1. [&#x60;/events/:id/categories&#x60;](#operation/fetchAllEventsCategories)     2. [&#x60;/events/:id/channels&#x60;](#operation/fetchAllEventsChannels)     3. [&#x60;/events/:id/ticket-counts/detailed&#x60;](#operation/fetchAllDetailedTicketCounts)  Eventually, you may also want to fetch the [promotions](#tag/Promotions). A &lt;span class&#x3D;\&quot;definition\&quot;&gt;promotion&lt;/span&gt; can be anything meant to leverage the sales: ads, marketing campaigns, buzz or news around the event, etc. A promotion can be linked to any combination of events and/or series..<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var Pims = require('index'); // See note below*.
* var xxxSvc = new Pims.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new Pims.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* <em>*NOTE: For a top-level AMD script, use require(['index'], function(){...})
* and put the application logic within the callback function.</em>
* </p>
* <p>
* A non-AMD browser application (discouraged) might do something like this:
* <pre>
* var xxxSvc = new Pims.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new Pims.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 1.0
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The CategoriesEntity model constructor.
     * @property {module:model/CategoriesEntity}
     */
    CategoriesEntity,

    /**
     * The ChannelsEntity model constructor.
     * @property {module:model/ChannelsEntity}
     */
    ChannelsEntity,

    /**
     * The Error401 model constructor.
     * @property {module:model/Error401}
     */
    Error401,

    /**
     * The Error403 model constructor.
     * @property {module:model/Error403}
     */
    Error403,

    /**
     * The Error404 model constructor.
     * @property {module:model/Error404}
     */
    Error404,

    /**
     * The Error422 model constructor.
     * @property {module:model/Error422}
     */
    Error422,

    /**
     * The Error500 model constructor.
     * @property {module:model/Error500}
     */
    Error500,

    /**
     * The EventsCapacitiesEntity model constructor.
     * @property {module:model/EventsCapacitiesEntity}
     */
    EventsCapacitiesEntity,

    /**
     * The EventsCapacitiesEntityEventCategoriesInner model constructor.
     * @property {module:model/EventsCapacitiesEntityEventCategoriesInner}
     */
    EventsCapacitiesEntityEventCategoriesInner,

    /**
     * The EventsCategoriesEntity model constructor.
     * @property {module:model/EventsCategoriesEntity}
     */
    EventsCategoriesEntity,

    /**
     * The EventsCategoriesEntityEventPriceRangesInner model constructor.
     * @property {module:model/EventsCategoriesEntityEventPriceRangesInner}
     */
    EventsCategoriesEntityEventPriceRangesInner,

    /**
     * The EventsChannelsEntity model constructor.
     * @property {module:model/EventsChannelsEntity}
     */
    EventsChannelsEntity,

    /**
     * The EventsEntity model constructor.
     * @property {module:model/EventsEntity}
     */
    EventsEntity,

    /**
     * The EventsEntityContract model constructor.
     * @property {module:model/EventsEntityContract}
     */
    EventsEntityContract,

    /**
     * The EventsEntityContractPartner model constructor.
     * @property {module:model/EventsEntityContractPartner}
     */
    EventsEntityContractPartner,

    /**
     * The EventsEntityContractType model constructor.
     * @property {module:model/EventsEntityContractType}
     */
    EventsEntityContractType,

    /**
     * The EventsEntityInputType model constructor.
     * @property {module:model/EventsEntityInputType}
     */
    EventsEntityInputType,

    /**
     * The PriceRangesEntity model constructor.
     * @property {module:model/PriceRangesEntity}
     */
    PriceRangesEntity,

    /**
     * The PromotionsEntity model constructor.
     * @property {module:model/PromotionsEntity}
     */
    PromotionsEntity,

    /**
     * The PromotionsEntityAppliedToInner model constructor.
     * @property {module:model/PromotionsEntityAppliedToInner}
     */
    PromotionsEntityAppliedToInner,

    /**
     * The PromotionsEntityCost model constructor.
     * @property {module:model/PromotionsEntityCost}
     */
    PromotionsEntityCost,

    /**
     * The PromotionsEntityCostState model constructor.
     * @property {module:model/PromotionsEntityCostState}
     */
    PromotionsEntityCostState,

    /**
     * The PromotionsEntityCostType model constructor.
     * @property {module:model/PromotionsEntityCostType}
     */
    PromotionsEntityCostType,

    /**
     * The PromotionsEntitySupplier model constructor.
     * @property {module:model/PromotionsEntitySupplier}
     */
    PromotionsEntitySupplier,

    /**
     * The PromotionsEntityType model constructor.
     * @property {module:model/PromotionsEntityType}
     */
    PromotionsEntityType,

    /**
     * The PromotionsEntityTypeFamily model constructor.
     * @property {module:model/PromotionsEntityTypeFamily}
     */
    PromotionsEntityTypeFamily,

    /**
     * The SeriesEntity model constructor.
     * @property {module:model/SeriesEntity}
     */
    SeriesEntity,

    /**
     * The SeriesEntityContract model constructor.
     * @property {module:model/SeriesEntityContract}
     */
    SeriesEntityContract,

    /**
     * The SeriesEntityContractPartner model constructor.
     * @property {module:model/SeriesEntityContractPartner}
     */
    SeriesEntityContractPartner,

    /**
     * The SeriesEntityContractType model constructor.
     * @property {module:model/SeriesEntityContractType}
     */
    SeriesEntityContractType,

    /**
     * The SeriesEntityType model constructor.
     * @property {module:model/SeriesEntityType}
     */
    SeriesEntityType,

    /**
     * The TicketCountsDetailedEntity model constructor.
     * @property {module:model/TicketCountsDetailedEntity}
     */
    TicketCountsDetailedEntity,

    /**
     * The TicketCountsDetailedEntityEventChannelsInner model constructor.
     * @property {module:model/TicketCountsDetailedEntityEventChannelsInner}
     */
    TicketCountsDetailedEntityEventChannelsInner,

    /**
     * The TicketCountsDetailedEntityEventChannelsInnerEventCategoriesInner model constructor.
     * @property {module:model/TicketCountsDetailedEntityEventChannelsInnerEventCategoriesInner}
     */
    TicketCountsDetailedEntityEventChannelsInnerEventCategoriesInner,

    /**
     * The TicketCountsDetailedEntityEventChannelsInnerEventCategoriesInnerEventPriceRangesInner model constructor.
     * @property {module:model/TicketCountsDetailedEntityEventChannelsInnerEventCategoriesInnerEventPriceRangesInner}
     */
    TicketCountsDetailedEntityEventChannelsInnerEventCategoriesInnerEventPriceRangesInner,

    /**
     * The TicketCountsEntity model constructor.
     * @property {module:model/TicketCountsEntity}
     */
    TicketCountsEntity,

    /**
     * The VenuesEntity model constructor.
     * @property {module:model/VenuesEntity}
     */
    VenuesEntity,

    /**
     * The VenuesEntityType model constructor.
     * @property {module:model/VenuesEntityType}
     */
    VenuesEntityType,

    /**
    * The CapacitiesApi service constructor.
    * @property {module:api/CapacitiesApi}
    */
    CapacitiesApi,

    /**
    * The CategoriesApi service constructor.
    * @property {module:api/CategoriesApi}
    */
    CategoriesApi,

    /**
    * The ChannelsApi service constructor.
    * @property {module:api/ChannelsApi}
    */
    ChannelsApi,

    /**
    * The CountsApi service constructor.
    * @property {module:api/CountsApi}
    */
    CountsApi,

    /**
    * The EventsApi service constructor.
    * @property {module:api/EventsApi}
    */
    EventsApi,

    /**
    * The PriceRangesApi service constructor.
    * @property {module:api/PriceRangesApi}
    */
    PriceRangesApi,

    /**
    * The PromotionsApi service constructor.
    * @property {module:api/PromotionsApi}
    */
    PromotionsApi,

    /**
    * The SeriesApi service constructor.
    * @property {module:api/SeriesApi}
    */
    SeriesApi,

    /**
    * The VenuesApi service constructor.
    * @property {module:api/VenuesApi}
    */
    VenuesApi
};
