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
import SeriesEntityContract from './SeriesEntityContract';
import SeriesEntityType from './SeriesEntityType';
import VenuesEntity from './VenuesEntity';

/**
 * The SeriesEntity model module.
 * @module model/SeriesEntity
 * @version 1.0
 */
class SeriesEntity {
    /**
     * Constructs a new <code>SeriesEntity</code>.
     * @alias module:model/SeriesEntity
     * @param creationTimestamp {Number} Timestamp for when the series was created in the customer's database.
     * @param firstDate {Date} Date of the first event in the series.
     * @param id {Number} Unique ID of the series.
     * @param label {String} Label of the series.
     * @param lastDate {Date} Date of the last event in the series.
     * @param lastUpdateTimestamp {Number} Timestamp for when the series was last updated in the customer's database.
     * @param type {module:model/SeriesEntityType} 
     */
    constructor(creationTimestamp, firstDate, id, label, lastDate, lastUpdateTimestamp, type) { 
        
        SeriesEntity.initialize(this, creationTimestamp, firstDate, id, label, lastDate, lastUpdateTimestamp, type);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, creationTimestamp, firstDate, id, label, lastDate, lastUpdateTimestamp, type) { 
        obj['creation_timestamp'] = creationTimestamp;
        obj['first_date'] = firstDate;
        obj['id'] = id;
        obj['label'] = label;
        obj['last_date'] = lastDate;
        obj['last_update_timestamp'] = lastUpdateTimestamp;
        obj['type'] = type;
    }

    /**
     * Constructs a <code>SeriesEntity</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SeriesEntity} obj Optional instance to populate.
     * @return {module:model/SeriesEntity} The populated <code>SeriesEntity</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SeriesEntity();

            if (data.hasOwnProperty('contract')) {
                obj['contract'] = SeriesEntityContract.constructFromObject(data['contract']);
            }
            if (data.hasOwnProperty('costing_capacity')) {
                obj['costing_capacity'] = ApiClient.convertToType(data['costing_capacity'], 'Number');
            }
            if (data.hasOwnProperty('creation_timestamp')) {
                obj['creation_timestamp'] = ApiClient.convertToType(data['creation_timestamp'], 'Number');
            }
            if (data.hasOwnProperty('first_date')) {
                obj['first_date'] = ApiClient.convertToType(data['first_date'], 'Date');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('label')) {
                obj['label'] = ApiClient.convertToType(data['label'], 'String');
            }
            if (data.hasOwnProperty('last_date')) {
                obj['last_date'] = ApiClient.convertToType(data['last_date'], 'Date');
            }
            if (data.hasOwnProperty('last_update_timestamp')) {
                obj['last_update_timestamp'] = ApiClient.convertToType(data['last_update_timestamp'], 'Number');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = SeriesEntityType.constructFromObject(data['type']);
            }
            if (data.hasOwnProperty('venue')) {
                obj['venue'] = VenuesEntity.constructFromObject(data['venue']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>SeriesEntity</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>SeriesEntity</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of SeriesEntity.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `contract`
        if (data['contract']) { // data not null
          SeriesEntityContract.validateJSON(data['contract']);
        }
        // ensure the json data is a string
        if (data['label'] && !(typeof data['label'] === 'string' || data['label'] instanceof String)) {
            throw new Error("Expected the field `label` to be a primitive type in the JSON string but got " + data['label']);
        }
        // validate the optional field `type`
        if (data['type']) { // data not null
          SeriesEntityType.validateJSON(data['type']);
        }
        // validate the optional field `venue`
        if (data['venue']) { // data not null
          VenuesEntity.validateJSON(data['venue']);
        }

        return true;
    }


}

SeriesEntity.RequiredProperties = ["creation_timestamp", "first_date", "id", "label", "last_date", "last_update_timestamp", "type"];

/**
 * @member {module:model/SeriesEntityContract} contract
 */
SeriesEntity.prototype['contract'] = undefined;

/**
 * Value of the costing capacity.
 * @member {Number} costing_capacity
 */
SeriesEntity.prototype['costing_capacity'] = undefined;

/**
 * Timestamp for when the series was created in the customer's database.
 * @member {Number} creation_timestamp
 */
SeriesEntity.prototype['creation_timestamp'] = undefined;

/**
 * Date of the first event in the series.
 * @member {Date} first_date
 */
SeriesEntity.prototype['first_date'] = undefined;

/**
 * Unique ID of the series.
 * @member {Number} id
 */
SeriesEntity.prototype['id'] = undefined;

/**
 * Label of the series.
 * @member {String} label
 */
SeriesEntity.prototype['label'] = undefined;

/**
 * Date of the last event in the series.
 * @member {Date} last_date
 */
SeriesEntity.prototype['last_date'] = undefined;

/**
 * Timestamp for when the series was last updated in the customer's database.
 * @member {Number} last_update_timestamp
 */
SeriesEntity.prototype['last_update_timestamp'] = undefined;

/**
 * @member {module:model/SeriesEntityType} type
 */
SeriesEntity.prototype['type'] = undefined;

/**
 * @member {module:model/VenuesEntity} venue
 */
SeriesEntity.prototype['venue'] = undefined;






export default SeriesEntity;

