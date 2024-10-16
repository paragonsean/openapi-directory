/**
 * Clever-Cloud API
 * Public API for managing Clever-Cloud data and products
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The OrganisationsIdAddonsAddonIdMigrationsPostRequest model module.
 * @module model/OrganisationsIdAddonsAddonIdMigrationsPostRequest
 * @version 1.0.0
 */
class OrganisationsIdAddonsAddonIdMigrationsPostRequest {
    /**
     * Constructs a new <code>OrganisationsIdAddonsAddonIdMigrationsPostRequest</code>.
     * @alias module:model/OrganisationsIdAddonsAddonIdMigrationsPostRequest
     */
    constructor() { 
        
        OrganisationsIdAddonsAddonIdMigrationsPostRequest.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>OrganisationsIdAddonsAddonIdMigrationsPostRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/OrganisationsIdAddonsAddonIdMigrationsPostRequest} obj Optional instance to populate.
     * @return {module:model/OrganisationsIdAddonsAddonIdMigrationsPostRequest} The populated <code>OrganisationsIdAddonsAddonIdMigrationsPostRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new OrganisationsIdAddonsAddonIdMigrationsPostRequest();

            if (data.hasOwnProperty('planId')) {
                obj['planId'] = ApiClient.convertToType(data['planId'], 'String');
            }
            if (data.hasOwnProperty('region')) {
                obj['region'] = ApiClient.convertToType(data['region'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>OrganisationsIdAddonsAddonIdMigrationsPostRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>OrganisationsIdAddonsAddonIdMigrationsPostRequest</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['planId'] && !(typeof data['planId'] === 'string' || data['planId'] instanceof String)) {
            throw new Error("Expected the field `planId` to be a primitive type in the JSON string but got " + data['planId']);
        }
        // ensure the json data is a string
        if (data['region'] && !(typeof data['region'] === 'string' || data['region'] instanceof String)) {
            throw new Error("Expected the field `region` to be a primitive type in the JSON string but got " + data['region']);
        }

        return true;
    }


}



/**
 * Id of the new plan. E.g. \"plan_acddc485-79c2-4c6b-a617-c92a06c0cb0b\"
 * @member {String} planId
 */
OrganisationsIdAddonsAddonIdMigrationsPostRequest.prototype['planId'] = undefined;

/**
 * New region. E.g. \"EU\", \"US\", \"Par2\"
 * @member {String} region
 */
OrganisationsIdAddonsAddonIdMigrationsPostRequest.prototype['region'] = undefined;






export default OrganisationsIdAddonsAddonIdMigrationsPostRequest;

