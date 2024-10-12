/**
 * Gateway
 * Gateway is the hub that routes/orchestrates the interaction between consent managers and API bridges. There are 5 categories of APIs; discovery, link, consent flow, data flow and  monitoring. To reflect the consumers of APIs, the above apis are also categorized under cm facing, hiu facing and hip facing  
 *
 * The version of the OpenAPI document: 0.5
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import OrganizationReference from './OrganizationReference';

/**
 * The HIPConsentNotificationNotificationConsentDetailConsentManager model module.
 * @module model/HIPConsentNotificationNotificationConsentDetailConsentManager
 * @version 0.5
 */
class HIPConsentNotificationNotificationConsentDetailConsentManager {
    /**
     * Constructs a new <code>HIPConsentNotificationNotificationConsentDetailConsentManager</code>.
     * @alias module:model/HIPConsentNotificationNotificationConsentDetailConsentManager
     * @implements module:model/OrganizationReference
     * @param id {String} 
     */
    constructor(id) { 
        OrganizationReference.initialize(this, id);
        HIPConsentNotificationNotificationConsentDetailConsentManager.initialize(this, id);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, id) { 
        obj['id'] = id;
    }

    /**
     * Constructs a <code>HIPConsentNotificationNotificationConsentDetailConsentManager</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/HIPConsentNotificationNotificationConsentDetailConsentManager} obj Optional instance to populate.
     * @return {module:model/HIPConsentNotificationNotificationConsentDetailConsentManager} The populated <code>HIPConsentNotificationNotificationConsentDetailConsentManager</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new HIPConsentNotificationNotificationConsentDetailConsentManager();
            OrganizationReference.constructFromObject(data, obj);

            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>HIPConsentNotificationNotificationConsentDetailConsentManager</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>HIPConsentNotificationNotificationConsentDetailConsentManager</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of HIPConsentNotificationNotificationConsentDetailConsentManager.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }

        return true;
    }


}

HIPConsentNotificationNotificationConsentDetailConsentManager.RequiredProperties = ["id"];

/**
 * @member {String} id
 */
HIPConsentNotificationNotificationConsentDetailConsentManager.prototype['id'] = undefined;


// Implement OrganizationReference interface:
/**
 * @member {String} id
 */
OrganizationReference.prototype['id'] = undefined;




export default HIPConsentNotificationNotificationConsentDetailConsentManager;

