/**
 * NaviPlan API
 * An API for accessing NaviPlan plan data for a client.
 *
 * The version of the OpenAPI document: v1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import Year from './Year';

/**
 * The IOptionalFieldYear model module.
 * @module model/IOptionalFieldYear
 * @version v1
 */
class IOptionalFieldYear {
    /**
     * Constructs a new <code>IOptionalFieldYear</code>.
     * @alias module:model/IOptionalFieldYear
     */
    constructor() { 
        
        IOptionalFieldYear.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>IOptionalFieldYear</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/IOptionalFieldYear} obj Optional instance to populate.
     * @return {module:model/IOptionalFieldYear} The populated <code>IOptionalFieldYear</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new IOptionalFieldYear();

            if (data.hasOwnProperty('enabled')) {
                obj['enabled'] = ApiClient.convertToType(data['enabled'], 'Boolean');
            }
            if (data.hasOwnProperty('populated')) {
                obj['populated'] = ApiClient.convertToType(data['populated'], 'Boolean');
            }
            if (data.hasOwnProperty('value')) {
                obj['value'] = Year.constructFromObject(data['value']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>IOptionalFieldYear</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>IOptionalFieldYear</code>.
     */
    static validateJSON(data) {
        // validate the optional field `value`
        if (data['value']) { // data not null
          Year.validateJSON(data['value']);
        }

        return true;
    }


}



/**
 * @member {Boolean} enabled
 */
IOptionalFieldYear.prototype['enabled'] = undefined;

/**
 * @member {Boolean} populated
 */
IOptionalFieldYear.prototype['populated'] = undefined;

/**
 * @member {module:model/Year} value
 */
IOptionalFieldYear.prototype['value'] = undefined;






export default IOptionalFieldYear;

