/**
 * Meshery API.
 * the purpose of this application is to provide an application that is using plain go code to define an API  This should demonstrate all the possible comment annotations that are available to turn go code into a fully compliant swagger 2.0 spec
 *
 * The version of the OpenAPI document: 0.4.27
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The PanelScopedVarsValue model module.
 * @module model/PanelScopedVarsValue
 * @version 0.4.27
 */
class PanelScopedVarsValue {
    /**
     * Constructs a new <code>PanelScopedVarsValue</code>.
     * @alias module:model/PanelScopedVarsValue
     */
    constructor() { 
        
        PanelScopedVarsValue.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PanelScopedVarsValue</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PanelScopedVarsValue} obj Optional instance to populate.
     * @return {module:model/PanelScopedVarsValue} The populated <code>PanelScopedVarsValue</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PanelScopedVarsValue();

            if (data.hasOwnProperty('selected')) {
                obj['selected'] = ApiClient.convertToType(data['selected'], 'Boolean');
            }
            if (data.hasOwnProperty('text')) {
                obj['text'] = ApiClient.convertToType(data['text'], 'String');
            }
            if (data.hasOwnProperty('value')) {
                obj['value'] = ApiClient.convertToType(data['value'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PanelScopedVarsValue</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PanelScopedVarsValue</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['text'] && !(typeof data['text'] === 'string' || data['text'] instanceof String)) {
            throw new Error("Expected the field `text` to be a primitive type in the JSON string but got " + data['text']);
        }
        // ensure the json data is a string
        if (data['value'] && !(typeof data['value'] === 'string' || data['value'] instanceof String)) {
            throw new Error("Expected the field `value` to be a primitive type in the JSON string but got " + data['value']);
        }

        return true;
    }


}



/**
 * @member {Boolean} selected
 */
PanelScopedVarsValue.prototype['selected'] = undefined;

/**
 * @member {String} text
 */
PanelScopedVarsValue.prototype['text'] = undefined;

/**
 * @member {String} value
 */
PanelScopedVarsValue.prototype['value'] = undefined;






export default PanelScopedVarsValue;

