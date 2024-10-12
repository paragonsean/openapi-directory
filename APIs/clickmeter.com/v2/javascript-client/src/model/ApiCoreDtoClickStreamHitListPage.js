/**
 * ClickMeter API
 * Api dashboard for ClickMeter API
 *
 * The version of the OpenAPI document: v2
 * Contact: api@clickmeter.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import ApiCoreDtoClickStreamHit from './ApiCoreDtoClickStreamHit';

/**
 * The ApiCoreDtoClickStreamHitListPage model module.
 * @module model/ApiCoreDtoClickStreamHitListPage
 * @version v2
 */
class ApiCoreDtoClickStreamHitListPage {
    /**
     * Constructs a new <code>ApiCoreDtoClickStreamHitListPage</code>.
     * @alias module:model/ApiCoreDtoClickStreamHitListPage
     */
    constructor() { 
        
        ApiCoreDtoClickStreamHitListPage.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ApiCoreDtoClickStreamHitListPage</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ApiCoreDtoClickStreamHitListPage} obj Optional instance to populate.
     * @return {module:model/ApiCoreDtoClickStreamHitListPage} The populated <code>ApiCoreDtoClickStreamHitListPage</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ApiCoreDtoClickStreamHitListPage();

            if (data.hasOwnProperty('hits')) {
                obj['hits'] = ApiClient.convertToType(data['hits'], [ApiCoreDtoClickStreamHit]);
            }
            if (data.hasOwnProperty('lastKey')) {
                obj['lastKey'] = ApiClient.convertToType(data['lastKey'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ApiCoreDtoClickStreamHitListPage</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ApiCoreDtoClickStreamHitListPage</code>.
     */
    static validateJSON(data) {
        if (data['hits']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['hits'])) {
                throw new Error("Expected the field `hits` to be an array in the JSON data but got " + data['hits']);
            }
            // validate the optional field `hits` (array)
            for (const item of data['hits']) {
                ApiCoreDtoClickStreamHit.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['lastKey'] && !(typeof data['lastKey'] === 'string' || data['lastKey'] instanceof String)) {
            throw new Error("Expected the field `lastKey` to be a primitive type in the JSON string but got " + data['lastKey']);
        }

        return true;
    }


}



/**
 * @member {Array.<module:model/ApiCoreDtoClickStreamHit>} hits
 */
ApiCoreDtoClickStreamHitListPage.prototype['hits'] = undefined;

/**
 * @member {String} lastKey
 */
ApiCoreDtoClickStreamHitListPage.prototype['lastKey'] = undefined;






export default ApiCoreDtoClickStreamHitListPage;

