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
 * The LegalSearchGetDefaultResponseAdvisoryOpinionsInnerAoCitationsInner model module.
 * @module model/LegalSearchGetDefaultResponseAdvisoryOpinionsInnerAoCitationsInner
 * @version 1.0
 */
class LegalSearchGetDefaultResponseAdvisoryOpinionsInnerAoCitationsInner {
    /**
     * Constructs a new <code>LegalSearchGetDefaultResponseAdvisoryOpinionsInnerAoCitationsInner</code>.
     * @alias module:model/LegalSearchGetDefaultResponseAdvisoryOpinionsInnerAoCitationsInner
     */
    constructor() { 
        
        LegalSearchGetDefaultResponseAdvisoryOpinionsInnerAoCitationsInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>LegalSearchGetDefaultResponseAdvisoryOpinionsInnerAoCitationsInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/LegalSearchGetDefaultResponseAdvisoryOpinionsInnerAoCitationsInner} obj Optional instance to populate.
     * @return {module:model/LegalSearchGetDefaultResponseAdvisoryOpinionsInnerAoCitationsInner} The populated <code>LegalSearchGetDefaultResponseAdvisoryOpinionsInnerAoCitationsInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new LegalSearchGetDefaultResponseAdvisoryOpinionsInnerAoCitationsInner();

            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('false')) {
                obj['false'] = ApiClient.convertToType(data['false'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>LegalSearchGetDefaultResponseAdvisoryOpinionsInnerAoCitationsInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>LegalSearchGetDefaultResponseAdvisoryOpinionsInnerAoCitationsInner</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['false'] && !(typeof data['false'] === 'string' || data['false'] instanceof String)) {
            throw new Error("Expected the field `false` to be a primitive type in the JSON string but got " + data['false']);
        }

        return true;
    }


}



/**
 * @member {String} name
 */
LegalSearchGetDefaultResponseAdvisoryOpinionsInnerAoCitationsInner.prototype['name'] = undefined;

/**
 * @member {String} false
 */
LegalSearchGetDefaultResponseAdvisoryOpinionsInnerAoCitationsInner.prototype['false'] = undefined;






export default LegalSearchGetDefaultResponseAdvisoryOpinionsInnerAoCitationsInner;

