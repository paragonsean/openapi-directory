/**
 * MicrosoftSerialConsoleClient
 * The Azure Serial Console allows you to access the serial console of a Virtual Machine or VM scale set instance
 *
 * The version of the OpenAPI document: 2018-05-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The SerialConsoleOperationsValueInnerDisplay model module.
 * @module model/SerialConsoleOperationsValueInnerDisplay
 * @version 2018-05-01
 */
class SerialConsoleOperationsValueInnerDisplay {
    /**
     * Constructs a new <code>SerialConsoleOperationsValueInnerDisplay</code>.
     * @alias module:model/SerialConsoleOperationsValueInnerDisplay
     */
    constructor() { 
        
        SerialConsoleOperationsValueInnerDisplay.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>SerialConsoleOperationsValueInnerDisplay</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SerialConsoleOperationsValueInnerDisplay} obj Optional instance to populate.
     * @return {module:model/SerialConsoleOperationsValueInnerDisplay} The populated <code>SerialConsoleOperationsValueInnerDisplay</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SerialConsoleOperationsValueInnerDisplay();

            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('operation')) {
                obj['operation'] = ApiClient.convertToType(data['operation'], 'String');
            }
            if (data.hasOwnProperty('provider')) {
                obj['provider'] = ApiClient.convertToType(data['provider'], 'String');
            }
            if (data.hasOwnProperty('resource')) {
                obj['resource'] = ApiClient.convertToType(data['resource'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>SerialConsoleOperationsValueInnerDisplay</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>SerialConsoleOperationsValueInnerDisplay</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['description'] && !(typeof data['description'] === 'string' || data['description'] instanceof String)) {
            throw new Error("Expected the field `description` to be a primitive type in the JSON string but got " + data['description']);
        }
        // ensure the json data is a string
        if (data['operation'] && !(typeof data['operation'] === 'string' || data['operation'] instanceof String)) {
            throw new Error("Expected the field `operation` to be a primitive type in the JSON string but got " + data['operation']);
        }
        // ensure the json data is a string
        if (data['provider'] && !(typeof data['provider'] === 'string' || data['provider'] instanceof String)) {
            throw new Error("Expected the field `provider` to be a primitive type in the JSON string but got " + data['provider']);
        }
        // ensure the json data is a string
        if (data['resource'] && !(typeof data['resource'] === 'string' || data['resource'] instanceof String)) {
            throw new Error("Expected the field `resource` to be a primitive type in the JSON string but got " + data['resource']);
        }

        return true;
    }


}



/**
 * @member {String} description
 */
SerialConsoleOperationsValueInnerDisplay.prototype['description'] = undefined;

/**
 * @member {String} operation
 */
SerialConsoleOperationsValueInnerDisplay.prototype['operation'] = undefined;

/**
 * @member {String} provider
 */
SerialConsoleOperationsValueInnerDisplay.prototype['provider'] = undefined;

/**
 * @member {String} resource
 */
SerialConsoleOperationsValueInnerDisplay.prototype['resource'] = undefined;






export default SerialConsoleOperationsValueInnerDisplay;

