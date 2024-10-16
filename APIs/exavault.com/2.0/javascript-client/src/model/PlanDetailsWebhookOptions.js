/**
 * ExaVault
 * ExaVaults API allows you to incorporate ExaVaults suite of file transfer and user management tools into your own application.\\nExaVault supports both POST (recommended when requesting large data sets) and GET operations, and requires an API key in order to use.
 *
 * The version of the OpenAPI document: 2.0
 * Contact: support@exavault.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The PlanDetailsWebhookOptions model module.
 * @module model/PlanDetailsWebhookOptions
 * @version 2.0
 */
class PlanDetailsWebhookOptions {
    /**
     * Constructs a new <code>PlanDetailsWebhookOptions</code>.
     * @alias module:model/PlanDetailsWebhookOptions
     */
    constructor() { 
        
        PlanDetailsWebhookOptions.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PlanDetailsWebhookOptions</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PlanDetailsWebhookOptions} obj Optional instance to populate.
     * @return {module:model/PlanDetailsWebhookOptions} The populated <code>PlanDetailsWebhookOptions</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PlanDetailsWebhookOptions();

            if (data.hasOwnProperty('amount')) {
                obj['amount'] = ApiClient.convertToType(data['amount'], 'Number');
            }
            if (data.hasOwnProperty('includeTriggers')) {
                obj['includeTriggers'] = ApiClient.convertToType(data['includeTriggers'], 'String');
            }
            if (data.hasOwnProperty('restrictionTypes')) {
                obj['restrictionTypes'] = ApiClient.convertToType(data['restrictionTypes'], ['String']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PlanDetailsWebhookOptions</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PlanDetailsWebhookOptions</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['includeTriggers'] && !(typeof data['includeTriggers'] === 'string' || data['includeTriggers'] instanceof String)) {
            throw new Error("Expected the field `includeTriggers` to be a primitive type in the JSON string but got " + data['includeTriggers']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['restrictionTypes'])) {
            throw new Error("Expected the field `restrictionTypes` to be an array in the JSON data but got " + data['restrictionTypes']);
        }

        return true;
    }


}



/**
 * @member {Number} amount
 */
PlanDetailsWebhookOptions.prototype['amount'] = undefined;

/**
 * @member {String} includeTriggers
 */
PlanDetailsWebhookOptions.prototype['includeTriggers'] = undefined;

/**
 * @member {Array.<String>} restrictionTypes
 */
PlanDetailsWebhookOptions.prototype['restrictionTypes'] = undefined;






export default PlanDetailsWebhookOptions;

