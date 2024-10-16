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

/**
 * The FormattedEnumTypePayOffOptionsType model module.
 * @module model/FormattedEnumTypePayOffOptionsType
 * @version v1
 */
class FormattedEnumTypePayOffOptionsType {
    /**
     * Constructs a new <code>FormattedEnumTypePayOffOptionsType</code>.
     * @alias module:model/FormattedEnumTypePayOffOptionsType
     */
    constructor() { 
        
        FormattedEnumTypePayOffOptionsType.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>FormattedEnumTypePayOffOptionsType</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/FormattedEnumTypePayOffOptionsType} obj Optional instance to populate.
     * @return {module:model/FormattedEnumTypePayOffOptionsType} The populated <code>FormattedEnumTypePayOffOptionsType</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new FormattedEnumTypePayOffOptionsType();

            if (data.hasOwnProperty('value')) {
                obj['value'] = ApiClient.convertToType(data['value'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>FormattedEnumTypePayOffOptionsType</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>FormattedEnumTypePayOffOptionsType</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['value'] && !(typeof data['value'] === 'string' || data['value'] instanceof String)) {
            throw new Error("Expected the field `value` to be a primitive type in the JSON string but got " + data['value']);
        }

        return true;
    }


}



/**
 * @member {module:model/FormattedEnumTypePayOffOptionsType.ValueEnum} value
 */
FormattedEnumTypePayOffOptionsType.prototype['value'] = undefined;





/**
 * Allowed values for the <code>value</code> property.
 * @enum {String}
 * @readonly
 */
FormattedEnumTypePayOffOptionsType['ValueEnum'] = {

    /**
     * value: "TransferToSurvivor"
     * @const
     */
    "TransferToSurvivor": "TransferToSurvivor",

    /**
     * value: "PayOffAtFirstDeath"
     * @const
     */
    "PayOffAtFirstDeath": "PayOffAtFirstDeath",

    /**
     * value: "PayOffAtOwnerDeath"
     * @const
     */
    "PayOffAtOwnerDeath": "PayOffAtOwnerDeath",

    /**
     * value: "InsuredForLife"
     * @const
     */
    "InsuredForLife": "InsuredForLife"
};



export default FormattedEnumTypePayOffOptionsType;

