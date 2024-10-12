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

import ApiClient from '../ApiClient';
import EventsEntityContract from './EventsEntityContract';
import EventsEntityInputType from './EventsEntityInputType';
import VenuesEntity from './VenuesEntity';

/**
 * The EventsEntity model module.
 * @module model/EventsEntity
 * @version 1.0
 */
class EventsEntity {
    /**
     * Constructs a new <code>EventsEntity</code>.
     * @alias module:model/EventsEntity
     * @param contract {module:model/EventsEntityContract} 
     * @param creationTimestamp {Number} Timestamp for when the venue was created in the customer's database.
     * @param datetime {String} Datetime of the event (relative to the timezone of the venue).
     * @param free {Boolean} Whether this event is free or not.
     * @param id {Number} Unique ID of the event.
     * @param inputType {module:model/EventsEntityInputType} 
     * @param label {String} Label of the event.
     * @param lastUpdateTimestamp {Number} Timestamp for when the venue was last updated in the customer's database.
     * @param seriesId {Number} ID of the series the event belongs to.
     * @param venue {module:model/VenuesEntity} 
     */
    constructor(contract, creationTimestamp, datetime, free, id, inputType, label, lastUpdateTimestamp, seriesId, venue) { 
        
        EventsEntity.initialize(this, contract, creationTimestamp, datetime, free, id, inputType, label, lastUpdateTimestamp, seriesId, venue);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, contract, creationTimestamp, datetime, free, id, inputType, label, lastUpdateTimestamp, seriesId, venue) { 
        obj['contract'] = contract;
        obj['creation_timestamp'] = creationTimestamp;
        obj['datetime'] = datetime;
        obj['free'] = free;
        obj['id'] = id;
        obj['input_type'] = inputType;
        obj['label'] = label;
        obj['last_update_timestamp'] = lastUpdateTimestamp;
        obj['series_id'] = seriesId;
        obj['venue'] = venue;
    }

    /**
     * Constructs a <code>EventsEntity</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/EventsEntity} obj Optional instance to populate.
     * @return {module:model/EventsEntity} The populated <code>EventsEntity</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new EventsEntity();

            if (data.hasOwnProperty('break_even')) {
                obj['break_even'] = ApiClient.convertToType(data['break_even'], 'Number');
            }
            if (data.hasOwnProperty('cancellation_date')) {
                obj['cancellation_date'] = ApiClient.convertToType(data['cancellation_date'], 'Date');
            }
            if (data.hasOwnProperty('contract')) {
                obj['contract'] = EventsEntityContract.constructFromObject(data['contract']);
            }
            if (data.hasOwnProperty('costing_capacity')) {
                obj['costing_capacity'] = ApiClient.convertToType(data['costing_capacity'], 'Number');
            }
            if (data.hasOwnProperty('creation_timestamp')) {
                obj['creation_timestamp'] = ApiClient.convertToType(data['creation_timestamp'], 'Number');
            }
            if (data.hasOwnProperty('currency')) {
                obj['currency'] = ApiClient.convertToType(data['currency'], 'String');
            }
            if (data.hasOwnProperty('datetime')) {
                obj['datetime'] = ApiClient.convertToType(data['datetime'], 'String');
            }
            if (data.hasOwnProperty('free')) {
                obj['free'] = ApiClient.convertToType(data['free'], 'Boolean');
            }
            if (data.hasOwnProperty('general_sales_date')) {
                obj['general_sales_date'] = ApiClient.convertToType(data['general_sales_date'], 'Date');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('input_type')) {
                obj['input_type'] = EventsEntityInputType.constructFromObject(data['input_type']);
            }
            if (data.hasOwnProperty('label')) {
                obj['label'] = ApiClient.convertToType(data['label'], 'String');
            }
            if (data.hasOwnProperty('last_update_timestamp')) {
                obj['last_update_timestamp'] = ApiClient.convertToType(data['last_update_timestamp'], 'Number');
            }
            if (data.hasOwnProperty('max_capacity')) {
                obj['max_capacity'] = ApiClient.convertToType(data['max_capacity'], 'Number');
            }
            if (data.hasOwnProperty('presales_date')) {
                obj['presales_date'] = ApiClient.convertToType(data['presales_date'], 'Date');
            }
            if (data.hasOwnProperty('series_id')) {
                obj['series_id'] = ApiClient.convertToType(data['series_id'], 'Number');
            }
            if (data.hasOwnProperty('sold_out_date')) {
                obj['sold_out_date'] = ApiClient.convertToType(data['sold_out_date'], 'Date');
            }
            if (data.hasOwnProperty('venue')) {
                obj['venue'] = VenuesEntity.constructFromObject(data['venue']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>EventsEntity</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>EventsEntity</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of EventsEntity.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `contract`
        if (data['contract']) { // data not null
          EventsEntityContract.validateJSON(data['contract']);
        }
        // ensure the json data is a string
        if (data['currency'] && !(typeof data['currency'] === 'string' || data['currency'] instanceof String)) {
            throw new Error("Expected the field `currency` to be a primitive type in the JSON string but got " + data['currency']);
        }
        // ensure the json data is a string
        if (data['datetime'] && !(typeof data['datetime'] === 'string' || data['datetime'] instanceof String)) {
            throw new Error("Expected the field `datetime` to be a primitive type in the JSON string but got " + data['datetime']);
        }
        // validate the optional field `input_type`
        if (data['input_type']) { // data not null
          EventsEntityInputType.validateJSON(data['input_type']);
        }
        // ensure the json data is a string
        if (data['label'] && !(typeof data['label'] === 'string' || data['label'] instanceof String)) {
            throw new Error("Expected the field `label` to be a primitive type in the JSON string but got " + data['label']);
        }
        // validate the optional field `venue`
        if (data['venue']) { // data not null
          VenuesEntity.validateJSON(data['venue']);
        }

        return true;
    }


}

EventsEntity.RequiredProperties = ["contract", "creation_timestamp", "datetime", "free", "id", "input_type", "label", "last_update_timestamp", "series_id", "venue"];

/**
 * Value of the break-even for the event.
 * @member {Number} break_even
 */
EventsEntity.prototype['break_even'] = undefined;

/**
 * Date the event was canceled.
 * @member {Date} cancellation_date
 */
EventsEntity.prototype['cancellation_date'] = undefined;

/**
 * @member {module:model/EventsEntityContract} contract
 */
EventsEntity.prototype['contract'] = undefined;

/**
 * Costing capacity of the event.
 * @member {Number} costing_capacity
 */
EventsEntity.prototype['costing_capacity'] = undefined;

/**
 * Timestamp for when the venue was created in the customer's database.
 * @member {Number} creation_timestamp
 */
EventsEntity.prototype['creation_timestamp'] = undefined;

/**
 * Currency of the prices.
 * @member {String} currency
 */
EventsEntity.prototype['currency'] = undefined;

/**
 * Datetime of the event (relative to the timezone of the venue).
 * @member {String} datetime
 */
EventsEntity.prototype['datetime'] = undefined;

/**
 * Whether this event is free or not.
 * @member {Boolean} free
 */
EventsEntity.prototype['free'] = undefined;

/**
 * Date the event went on general sales (relative to the timezone of the venue).
 * @member {Date} general_sales_date
 */
EventsEntity.prototype['general_sales_date'] = undefined;

/**
 * Unique ID of the event.
 * @member {Number} id
 */
EventsEntity.prototype['id'] = undefined;

/**
 * @member {module:model/EventsEntityInputType} input_type
 */
EventsEntity.prototype['input_type'] = undefined;

/**
 * Label of the event.
 * @member {String} label
 */
EventsEntity.prototype['label'] = undefined;

/**
 * Timestamp for when the venue was last updated in the customer's database.
 * @member {Number} last_update_timestamp
 */
EventsEntity.prototype['last_update_timestamp'] = undefined;

/**
 * Maximum capacity for the venue in which the event occurs.
 * @member {Number} max_capacity
 */
EventsEntity.prototype['max_capacity'] = undefined;

/**
 * Date the event went on presales (relative to the timezone of the venue).
 * @member {Date} presales_date
 */
EventsEntity.prototype['presales_date'] = undefined;

/**
 * ID of the series the event belongs to.
 * @member {Number} series_id
 */
EventsEntity.prototype['series_id'] = undefined;

/**
 * Date the event was sold out.
 * @member {Date} sold_out_date
 */
EventsEntity.prototype['sold_out_date'] = undefined;

/**
 * @member {module:model/VenuesEntity} venue
 */
EventsEntity.prototype['venue'] = undefined;






export default EventsEntity;

