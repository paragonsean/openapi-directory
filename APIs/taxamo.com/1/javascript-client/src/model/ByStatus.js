/**
 * Taxamo
 * Taxamo’s elegant suite of APIs and comprehensive reporting dashboard enables digital merchants to easily comply with EU regulatory requirements on tax calculation, evidence collection, tax return creation and data storage.
 *
 * The version of the OpenAPI document: 1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import C from './C';
import N from './N';

/**
 * The ByStatus model module.
 * @module model/ByStatus
 * @version 1
 */
class ByStatus {
    /**
     * Constructs a new <code>ByStatus</code>.
     * @alias module:model/ByStatus
     */
    constructor() { 
        
        ByStatus.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ByStatus</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ByStatus} obj Optional instance to populate.
     * @return {module:model/ByStatus} The populated <code>ByStatus</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ByStatus();

            if (data.hasOwnProperty('C')) {
                obj['C'] = ApiClient.convertToType(data['C'], [C]);
            }
            if (data.hasOwnProperty('N')) {
                obj['N'] = ApiClient.convertToType(data['N'], [N]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ByStatus</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ByStatus</code>.
     */
    static validateJSON(data) {
        if (data['C']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['C'])) {
                throw new Error("Expected the field `C` to be an array in the JSON data but got " + data['C']);
            }
            // validate the optional field `C` (array)
            for (const item of data['C']) {
                C.validateJSON(item);
            };
        }
        if (data['N']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['N'])) {
                throw new Error("Expected the field `N` to be an array in the JSON data but got " + data['N']);
            }
            // validate the optional field `N` (array)
            for (const item of data['N']) {
                N.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * Confirmed transactions
 * @member {Array.<module:model/C>} C
 */
ByStatus.prototype['C'] = undefined;

/**
 * New transactions
 * @member {Array.<module:model/N>} N
 */
ByStatus.prototype['N'] = undefined;






export default ByStatus;

