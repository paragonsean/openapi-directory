/**
 * eNanoMapper database
 * AMBIT REST web services [eNanoMapper profile] with free text & faceted search
 *
 * The version of the OpenAPI document: 4.0.0
 * Contact: support@ideaconsult.net
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The Substance model module.
 * @module model/Substance
 * @version 4.0.0
 */
class Substance {
    /**
     * Constructs a new <code>Substance</code>.
     * @alias module:model/Substance
     */
    constructor() { 
        
        Substance.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Substance</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Substance} obj Optional instance to populate.
     * @return {module:model/Substance} The populated <code>Substance</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Substance();

            if (data.hasOwnProperty('substance')) {
                obj['substance'] = ApiClient.convertToType(data['substance'], Object);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Substance</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Substance</code>.
     */
    static validateJSON(data) {

        return true;
    }


}



/**
 * @member {Object} substance
 */
Substance.prototype['substance'] = undefined;






export default Substance;

