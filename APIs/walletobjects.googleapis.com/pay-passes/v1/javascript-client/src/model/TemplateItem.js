/**
 * Google Pay Passes API
 * API for issuers to save and manage Google Wallet Objects.
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
import FieldSelector from './FieldSelector';

/**
 * The TemplateItem model module.
 * @module model/TemplateItem
 * @version v1
 */
class TemplateItem {
    /**
     * Constructs a new <code>TemplateItem</code>.
     * @alias module:model/TemplateItem
     */
    constructor() { 
        
        TemplateItem.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>TemplateItem</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TemplateItem} obj Optional instance to populate.
     * @return {module:model/TemplateItem} The populated <code>TemplateItem</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TemplateItem();

            if (data.hasOwnProperty('firstValue')) {
                obj['firstValue'] = FieldSelector.constructFromObject(data['firstValue']);
            }
            if (data.hasOwnProperty('predefinedItem')) {
                obj['predefinedItem'] = ApiClient.convertToType(data['predefinedItem'], 'String');
            }
            if (data.hasOwnProperty('secondValue')) {
                obj['secondValue'] = FieldSelector.constructFromObject(data['secondValue']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>TemplateItem</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>TemplateItem</code>.
     */
    static validateJSON(data) {
        // validate the optional field `firstValue`
        if (data['firstValue']) { // data not null
          FieldSelector.validateJSON(data['firstValue']);
        }
        // ensure the json data is a string
        if (data['predefinedItem'] && !(typeof data['predefinedItem'] === 'string' || data['predefinedItem'] instanceof String)) {
            throw new Error("Expected the field `predefinedItem` to be a primitive type in the JSON string but got " + data['predefinedItem']);
        }
        // validate the optional field `secondValue`
        if (data['secondValue']) { // data not null
          FieldSelector.validateJSON(data['secondValue']);
        }

        return true;
    }


}



/**
 * @member {module:model/FieldSelector} firstValue
 */
TemplateItem.prototype['firstValue'] = undefined;

/**
 * A predefined item to display. Only one of `firstValue` or `predefinedItem` may be set.
 * @member {module:model/TemplateItem.PredefinedItemEnum} predefinedItem
 */
TemplateItem.prototype['predefinedItem'] = undefined;

/**
 * @member {module:model/FieldSelector} secondValue
 */
TemplateItem.prototype['secondValue'] = undefined;





/**
 * Allowed values for the <code>predefinedItem</code> property.
 * @enum {String}
 * @readonly
 */
TemplateItem['PredefinedItemEnum'] = {

    /**
     * value: "PREDEFINED_ITEM_UNSPECIFIED"
     * @const
     */
    "PREDEFINED_ITEM_UNSPECIFIED": "PREDEFINED_ITEM_UNSPECIFIED",

    /**
     * value: "FREQUENT_FLYER_PROGRAM_NAME_AND_NUMBER"
     * @const
     */
    "FREQUENT_FLYER_PROGRAM_NAME_AND_NUMBER": "FREQUENT_FLYER_PROGRAM_NAME_AND_NUMBER",

    /**
     * value: "frequentFlyerProgramNameAndNumber"
     * @const
     */
    "frequentFlyerProgramNameAndNumber": "frequentFlyerProgramNameAndNumber",

    /**
     * value: "FLIGHT_NUMBER_AND_OPERATING_FLIGHT_NUMBER"
     * @const
     */
    "FLIGHT_NUMBER_AND_OPERATING_FLIGHT_NUMBER": "FLIGHT_NUMBER_AND_OPERATING_FLIGHT_NUMBER",

    /**
     * value: "flightNumberAndOperatingFlightNumber"
     * @const
     */
    "flightNumberAndOperatingFlightNumber": "flightNumberAndOperatingFlightNumber"
};



export default TemplateItem;

