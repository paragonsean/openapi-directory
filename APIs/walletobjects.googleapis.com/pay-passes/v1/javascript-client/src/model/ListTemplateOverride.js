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
import FirstRowOption from './FirstRowOption';

/**
 * The ListTemplateOverride model module.
 * @module model/ListTemplateOverride
 * @version v1
 */
class ListTemplateOverride {
    /**
     * Constructs a new <code>ListTemplateOverride</code>.
     * @alias module:model/ListTemplateOverride
     */
    constructor() { 
        
        ListTemplateOverride.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ListTemplateOverride</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ListTemplateOverride} obj Optional instance to populate.
     * @return {module:model/ListTemplateOverride} The populated <code>ListTemplateOverride</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ListTemplateOverride();

            if (data.hasOwnProperty('firstRowOption')) {
                obj['firstRowOption'] = FirstRowOption.constructFromObject(data['firstRowOption']);
            }
            if (data.hasOwnProperty('secondRowOption')) {
                obj['secondRowOption'] = FieldSelector.constructFromObject(data['secondRowOption']);
            }
            if (data.hasOwnProperty('thirdRowOption')) {
                obj['thirdRowOption'] = FieldSelector.constructFromObject(data['thirdRowOption']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ListTemplateOverride</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ListTemplateOverride</code>.
     */
    static validateJSON(data) {
        // validate the optional field `firstRowOption`
        if (data['firstRowOption']) { // data not null
          FirstRowOption.validateJSON(data['firstRowOption']);
        }
        // validate the optional field `secondRowOption`
        if (data['secondRowOption']) { // data not null
          FieldSelector.validateJSON(data['secondRowOption']);
        }
        // validate the optional field `thirdRowOption`
        if (data['thirdRowOption']) { // data not null
          FieldSelector.validateJSON(data['thirdRowOption']);
        }

        return true;
    }


}



/**
 * @member {module:model/FirstRowOption} firstRowOption
 */
ListTemplateOverride.prototype['firstRowOption'] = undefined;

/**
 * @member {module:model/FieldSelector} secondRowOption
 */
ListTemplateOverride.prototype['secondRowOption'] = undefined;

/**
 * @member {module:model/FieldSelector} thirdRowOption
 */
ListTemplateOverride.prototype['thirdRowOption'] = undefined;






export default ListTemplateOverride;

