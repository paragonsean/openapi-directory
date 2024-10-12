/**
 * OpenFEC
 * This application programming interface (API) allows you to explore the way candidates and committees fund their campaigns.    The Federal Election Commission (FEC) API is a RESTful web service supporting full-text and field-specific searches on FEC data. [Bulk downloads](https://www.fec.gov/data/advanced/?tab=bulk-data) are available on the current site. Information is tied to the underlying forms by file ID and image ID. Data is updated nightly.    There are a lot of data, and a good place to start is to use search to find interesting candidates and committees. Then, you can use their IDs to find report or line item details with the other endpoints. If you are interested in individual donors, check out contributor information in the `/schedule_a/` endpoints.    <b class=\"body\" id=\"getting_started_head\">Getting started with the openFEC API</b><br>    If you would like to use the FEC's API programmatically, you can sign up for your own API key using our form. Alternatively, you can still try out our API without an API key by using the web interface and using DEMO_KEY. Note that when you use the openFEC API you are subject to the [Terms of Service](https://github.com/fecgov/FEC/blob/master/TERMS-OF-SERVICE.md) and [Acceptable Use policy](https://github.com/fecgov/FEC/blob/master/ACCEPTABLE-USE-POLICY.md).    Signing up for an API key will enable you to place up to 1,000 calls an hour. Each call is limited to 100 results per page. You can email questions, comments or a request to get a key for 7,200 calls an hour (120 calls per minute) to <a href=\"mailto:APIinfo@fec.gov\">APIinfo@fec.gov</a>. You can also ask questions and discuss the data in a community led [group](https://groups.google.com/forum/#!forum/fec-data).    The model definitions and schema are available at [/swagger](/swagger/). This is useful for making wrappers and exploring the data.    A few restrictions limit the way you can use FEC data. For example, you can’t use contributor lists for commercial purposes or to solicit donations. [Learn more here](https://www.fec.gov/updates/sale-or-use-contributor-information/).    [Inspect our source code](https://github.com/fecgov/openFEC). We welcome issues and pull requests!    <p><br></p> <h2 class=\"title\" id=\"signup_head\">Sign up for an API key</h2> <div id=\"apidatagov_signup\">Loading signup form...</div>
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The ScheduleABySize model module.
 * @module model/ScheduleABySize
 * @version 1.0
 */
class ScheduleABySize {
    /**
     * Constructs a new <code>ScheduleABySize</code>.
     * @alias module:model/ScheduleABySize
     * @param committeeId {String}  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
     * @param cycle {Number}  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
     * @param size {Number} 
     */
    constructor(committeeId, cycle, size) { 
        
        ScheduleABySize.initialize(this, committeeId, cycle, size);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, committeeId, cycle, size) { 
        obj['committee_id'] = committeeId;
        obj['cycle'] = cycle;
        obj['size'] = size;
    }

    /**
     * Constructs a <code>ScheduleABySize</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ScheduleABySize} obj Optional instance to populate.
     * @return {module:model/ScheduleABySize} The populated <code>ScheduleABySize</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ScheduleABySize();

            if (data.hasOwnProperty('committee_id')) {
                obj['committee_id'] = ApiClient.convertToType(data['committee_id'], 'String');
            }
            if (data.hasOwnProperty('count')) {
                obj['count'] = ApiClient.convertToType(data['count'], 'Number');
            }
            if (data.hasOwnProperty('cycle')) {
                obj['cycle'] = ApiClient.convertToType(data['cycle'], 'Number');
            }
            if (data.hasOwnProperty('size')) {
                obj['size'] = ApiClient.convertToType(data['size'], 'Number');
            }
            if (data.hasOwnProperty('total')) {
                obj['total'] = ApiClient.convertToType(data['total'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ScheduleABySize</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ScheduleABySize</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of ScheduleABySize.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['committee_id'] && !(typeof data['committee_id'] === 'string' || data['committee_id'] instanceof String)) {
            throw new Error("Expected the field `committee_id` to be a primitive type in the JSON string but got " + data['committee_id']);
        }

        return true;
    }


}

ScheduleABySize.RequiredProperties = ["committee_id", "cycle", "size"];

/**
 *  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
 * @member {String} committee_id
 */
ScheduleABySize.prototype['committee_id'] = undefined;

/**
 *  Number of records making up the total. 
 * @member {Number} count
 */
ScheduleABySize.prototype['count'] = undefined;

/**
 *  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
 * @member {Number} cycle
 */
ScheduleABySize.prototype['cycle'] = undefined;

/**
 * @member {Number} size
 */
ScheduleABySize.prototype['size'] = undefined;

/**
 * Sum of transactions
 * @member {Number} total
 */
ScheduleABySize.prototype['total'] = undefined;






export default ScheduleABySize;

