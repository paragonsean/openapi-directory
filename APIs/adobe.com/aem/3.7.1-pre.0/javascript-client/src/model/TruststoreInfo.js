/**
 * Adobe Experience Manager (AEM) API
 * Swagger AEM is an OpenAPI specification for Adobe Experience Manager (AEM) API
 *
 * The version of the OpenAPI document: 3.7.1-pre.0
 * Contact: opensource@shinesolutions.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import TruststoreItems from './TruststoreItems';

/**
 * The TruststoreInfo model module.
 * @module model/TruststoreInfo
 * @version 3.7.1-pre.0
 */
class TruststoreInfo {
    /**
     * Constructs a new <code>TruststoreInfo</code>.
     * @alias module:model/TruststoreInfo
     */
    constructor() { 
        
        TruststoreInfo.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>TruststoreInfo</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TruststoreInfo} obj Optional instance to populate.
     * @return {module:model/TruststoreInfo} The populated <code>TruststoreInfo</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TruststoreInfo();

            if (data.hasOwnProperty('aliases')) {
                obj['aliases'] = ApiClient.convertToType(data['aliases'], [TruststoreItems]);
            }
            if (data.hasOwnProperty('exists')) {
                obj['exists'] = ApiClient.convertToType(data['exists'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>TruststoreInfo</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>TruststoreInfo</code>.
     */
    static validateJSON(data) {
        if (data['aliases']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['aliases'])) {
                throw new Error("Expected the field `aliases` to be an array in the JSON data but got " + data['aliases']);
            }
            // validate the optional field `aliases` (array)
            for (const item of data['aliases']) {
                TruststoreItems.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {Array.<module:model/TruststoreItems>} aliases
 */
TruststoreInfo.prototype['aliases'] = undefined;

/**
 * False if truststore don't exist
 * @member {Boolean} exists
 */
TruststoreInfo.prototype['exists'] = undefined;






export default TruststoreInfo;

