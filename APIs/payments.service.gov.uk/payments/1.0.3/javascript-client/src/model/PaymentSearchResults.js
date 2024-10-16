/**
 * GOV.UK Pay API
 * GOV.UK Pay API (This version is no longer maintained. See openapi/publicapi_spec.json for latest API specification)
 *
 * The version of the OpenAPI document: 1.0.3
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import PaymentDetailForSearch from './PaymentDetailForSearch';
import SearchNavigationLinks from './SearchNavigationLinks';

/**
 * The PaymentSearchResults model module.
 * @module model/PaymentSearchResults
 * @version 1.0.3
 */
class PaymentSearchResults {
    /**
     * Constructs a new <code>PaymentSearchResults</code>.
     * @alias module:model/PaymentSearchResults
     */
    constructor() { 
        
        PaymentSearchResults.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PaymentSearchResults</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PaymentSearchResults} obj Optional instance to populate.
     * @return {module:model/PaymentSearchResults} The populated <code>PaymentSearchResults</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PaymentSearchResults();

            if (data.hasOwnProperty('_links')) {
                obj['_links'] = SearchNavigationLinks.constructFromObject(data['_links']);
            }
            if (data.hasOwnProperty('count')) {
                obj['count'] = ApiClient.convertToType(data['count'], 'Number');
            }
            if (data.hasOwnProperty('page')) {
                obj['page'] = ApiClient.convertToType(data['page'], 'Number');
            }
            if (data.hasOwnProperty('results')) {
                obj['results'] = ApiClient.convertToType(data['results'], [PaymentDetailForSearch]);
            }
            if (data.hasOwnProperty('total')) {
                obj['total'] = ApiClient.convertToType(data['total'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PaymentSearchResults</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PaymentSearchResults</code>.
     */
    static validateJSON(data) {
        // validate the optional field `_links`
        if (data['_links']) { // data not null
          SearchNavigationLinks.validateJSON(data['_links']);
        }
        if (data['results']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['results'])) {
                throw new Error("Expected the field `results` to be an array in the JSON data but got " + data['results']);
            }
            // validate the optional field `results` (array)
            for (const item of data['results']) {
                PaymentDetailForSearch.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {module:model/SearchNavigationLinks} _links
 */
PaymentSearchResults.prototype['_links'] = undefined;

/**
 * @member {Number} count
 */
PaymentSearchResults.prototype['count'] = undefined;

/**
 * @member {Number} page
 */
PaymentSearchResults.prototype['page'] = undefined;

/**
 * @member {Array.<module:model/PaymentDetailForSearch>} results
 */
PaymentSearchResults.prototype['results'] = undefined;

/**
 * @member {Number} total
 */
PaymentSearchResults.prototype['total'] = undefined;






export default PaymentSearchResults;

