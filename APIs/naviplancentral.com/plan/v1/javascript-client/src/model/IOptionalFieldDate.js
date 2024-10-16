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
import ModelDate from './ModelDate';

/**
 * The IOptionalFieldDate model module.
 * @module model/IOptionalFieldDate
 * @version v1
 */
class IOptionalFieldDate {
    /**
     * Constructs a new <code>IOptionalFieldDate</code>.
     * @alias module:model/IOptionalFieldDate
     */
    constructor() { 
        
        IOptionalFieldDate.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>IOptionalFieldDate</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/IOptionalFieldDate} obj Optional instance to populate.
     * @return {module:model/IOptionalFieldDate} The populated <code>IOptionalFieldDate</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new IOptionalFieldDate();

            if (data.hasOwnProperty('enabled')) {
                obj['enabled'] = ApiClient.convertToType(data['enabled'], 'Boolean');
            }
            if (data.hasOwnProperty('populated')) {
                obj['populated'] = ApiClient.convertToType(data['populated'], 'Boolean');
            }
            if (data.hasOwnProperty('value')) {
                obj['value'] = ModelDate.constructFromObject(data['value']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>IOptionalFieldDate</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>IOptionalFieldDate</code>.
     */
    static validateJSON(data) {
        // validate the optional field `value`
        if (data['value']) { // data not null
          ModelDate.validateJSON(data['value']);
        }

        return true;
    }


}



/**
 * @member {Boolean} enabled
 */
IOptionalFieldDate.prototype['enabled'] = undefined;

/**
 * @member {Boolean} populated
 */
IOptionalFieldDate.prototype['populated'] = undefined;

/**
 * @member {module:model/ModelDate} value
 */
IOptionalFieldDate.prototype['value'] = undefined;






export default IOptionalFieldDate;

