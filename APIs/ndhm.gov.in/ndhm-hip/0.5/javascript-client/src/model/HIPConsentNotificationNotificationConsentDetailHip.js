/**
 * Health Repository Provider Specifications for HIP
 * The following are the specifications for the APIs to be implemented at the Health Repository end if an entity is only serving the role of a HIP. The specs are essentially duplicates from the Gateway and Health Repository, but put together so as to make it clear to *HIPs* which set of APIs they should implement to participate in the network.  
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
import OrganizationRepresentation from './OrganizationRepresentation';

/**
 * The HIPConsentNotificationNotificationConsentDetailHip model module.
 * @module model/HIPConsentNotificationNotificationConsentDetailHip
 * @version 0.5
 */
class HIPConsentNotificationNotificationConsentDetailHip {
    /**
     * Constructs a new <code>HIPConsentNotificationNotificationConsentDetailHip</code>.
     * @alias module:model/HIPConsentNotificationNotificationConsentDetailHip
     * @implements module:model/OrganizationRepresentation
     * @param id {String} 
     */
    constructor(id) { 
        OrganizationRepresentation.initialize(this, id);
        HIPConsentNotificationNotificationConsentDetailHip.initialize(this, id);
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
     * Constructs a <code>HIPConsentNotificationNotificationConsentDetailHip</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/HIPConsentNotificationNotificationConsentDetailHip} obj Optional instance to populate.
     * @return {module:model/HIPConsentNotificationNotificationConsentDetailHip} The populated <code>HIPConsentNotificationNotificationConsentDetailHip</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new HIPConsentNotificationNotificationConsentDetailHip();
            OrganizationRepresentation.constructFromObject(data, obj);

            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>HIPConsentNotificationNotificationConsentDetailHip</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>HIPConsentNotificationNotificationConsentDetailHip</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of HIPConsentNotificationNotificationConsentDetailHip.RequiredProperties) {
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

HIPConsentNotificationNotificationConsentDetailHip.RequiredProperties = ["id"];

/**
 * @member {String} id
 */
HIPConsentNotificationNotificationConsentDetailHip.prototype['id'] = undefined;


// Implement OrganizationRepresentation interface:
/**
 * @member {String} id
 */
OrganizationRepresentation.prototype['id'] = undefined;




export default HIPConsentNotificationNotificationConsentDetailHip;

