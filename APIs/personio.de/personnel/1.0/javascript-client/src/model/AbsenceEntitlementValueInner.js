/**
 * Personnel Data
 * API for reading and writing personnel data incl. data about attendances and absences
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
import AbsenceEntitlementValueInnerAttributes from './AbsenceEntitlementValueInnerAttributes';

/**
 * The AbsenceEntitlementValueInner model module.
 * @module model/AbsenceEntitlementValueInner
 * @version 1.0
 */
class AbsenceEntitlementValueInner {
    /**
     * Constructs a new <code>AbsenceEntitlementValueInner</code>.
     * @alias module:model/AbsenceEntitlementValueInner
     */
    constructor() { 
        
        AbsenceEntitlementValueInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>AbsenceEntitlementValueInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AbsenceEntitlementValueInner} obj Optional instance to populate.
     * @return {module:model/AbsenceEntitlementValueInner} The populated <code>AbsenceEntitlementValueInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AbsenceEntitlementValueInner();

            if (data.hasOwnProperty('attributes')) {
                obj['attributes'] = AbsenceEntitlementValueInnerAttributes.constructFromObject(data['attributes']);
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AbsenceEntitlementValueInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AbsenceEntitlementValueInner</code>.
     */
    static validateJSON(data) {
        // validate the optional field `attributes`
        if (data['attributes']) { // data not null
          AbsenceEntitlementValueInnerAttributes.validateJSON(data['attributes']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}



/**
 * @member {module:model/AbsenceEntitlementValueInnerAttributes} attributes
 */
AbsenceEntitlementValueInner.prototype['attributes'] = undefined;

/**
 * @member {module:model/AbsenceEntitlementValueInner.TypeEnum} type
 */
AbsenceEntitlementValueInner.prototype['type'] = undefined;





/**
 * Allowed values for the <code>type</code> property.
 * @enum {String}
 * @readonly
 */
AbsenceEntitlementValueInner['TypeEnum'] = {

    /**
     * value: "TimeOffType"
     * @const
     */
    "TimeOffType": "TimeOffType"
};



export default AbsenceEntitlementValueInner;

