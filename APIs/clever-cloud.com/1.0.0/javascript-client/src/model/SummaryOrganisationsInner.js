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
import SummaryOrganisationsInnerAddonsInner from './SummaryOrganisationsInnerAddonsInner';
import SummaryOrganisationsInnerApplicationsInner from './SummaryOrganisationsInnerApplicationsInner';
import SummaryOrganisationsInnerConsumersInner from './SummaryOrganisationsInnerConsumersInner';

/**
 * The SummaryOrganisationsInner model module.
 * @module model/SummaryOrganisationsInner
 * @version 1.0.0
 */
class SummaryOrganisationsInner {
    /**
     * Constructs a new <code>SummaryOrganisationsInner</code>.
     * @alias module:model/SummaryOrganisationsInner
     */
    constructor() { 
        
        SummaryOrganisationsInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>SummaryOrganisationsInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SummaryOrganisationsInner} obj Optional instance to populate.
     * @return {module:model/SummaryOrganisationsInner} The populated <code>SummaryOrganisationsInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SummaryOrganisationsInner();

            if (data.hasOwnProperty('addons')) {
                obj['addons'] = ApiClient.convertToType(data['addons'], [SummaryOrganisationsInnerAddonsInner]);
            }
            if (data.hasOwnProperty('applications')) {
                obj['applications'] = ApiClient.convertToType(data['applications'], [SummaryOrganisationsInnerApplicationsInner]);
            }
            if (data.hasOwnProperty('avatar')) {
                obj['avatar'] = ApiClient.convertToType(data['avatar'], 'String');
            }
            if (data.hasOwnProperty('consumers')) {
                obj['consumers'] = ApiClient.convertToType(data['consumers'], [SummaryOrganisationsInnerConsumersInner]);
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('providers')) {
                obj['providers'] = ApiClient.convertToType(data['providers'], ['String']);
            }
            if (data.hasOwnProperty('role')) {
                obj['role'] = ApiClient.convertToType(data['role'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>SummaryOrganisationsInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>SummaryOrganisationsInner</code>.
     */
    static validateJSON(data) {
        if (data['addons']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['addons'])) {
                throw new Error("Expected the field `addons` to be an array in the JSON data but got " + data['addons']);
            }
            // validate the optional field `addons` (array)
            for (const item of data['addons']) {
                SummaryOrganisationsInnerAddonsInner.validateJSON(item);
            };
        }
        if (data['applications']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['applications'])) {
                throw new Error("Expected the field `applications` to be an array in the JSON data but got " + data['applications']);
            }
            // validate the optional field `applications` (array)
            for (const item of data['applications']) {
                SummaryOrganisationsInnerApplicationsInner.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['avatar'] && !(typeof data['avatar'] === 'string' || data['avatar'] instanceof String)) {
            throw new Error("Expected the field `avatar` to be a primitive type in the JSON string but got " + data['avatar']);
        }
        if (data['consumers']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['consumers'])) {
                throw new Error("Expected the field `consumers` to be an array in the JSON data but got " + data['consumers']);
            }
            // validate the optional field `consumers` (array)
            for (const item of data['consumers']) {
                SummaryOrganisationsInnerConsumersInner.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['providers'])) {
            throw new Error("Expected the field `providers` to be an array in the JSON data but got " + data['providers']);
        }
        // ensure the json data is a string
        if (data['role'] && !(typeof data['role'] === 'string' || data['role'] instanceof String)) {
            throw new Error("Expected the field `role` to be a primitive type in the JSON string but got " + data['role']);
        }

        return true;
    }


}



/**
 * @member {Array.<module:model/SummaryOrganisationsInnerAddonsInner>} addons
 */
SummaryOrganisationsInner.prototype['addons'] = undefined;

/**
 * @member {Array.<module:model/SummaryOrganisationsInnerApplicationsInner>} applications
 */
SummaryOrganisationsInner.prototype['applications'] = undefined;

/**
 * @member {String} avatar
 */
SummaryOrganisationsInner.prototype['avatar'] = undefined;

/**
 * @member {Array.<module:model/SummaryOrganisationsInnerConsumersInner>} consumers
 */
SummaryOrganisationsInner.prototype['consumers'] = undefined;

/**
 * @member {String} id
 */
SummaryOrganisationsInner.prototype['id'] = undefined;

/**
 * @member {String} name
 */
SummaryOrganisationsInner.prototype['name'] = undefined;

/**
 * @member {Array.<String>} providers
 */
SummaryOrganisationsInner.prototype['providers'] = undefined;

/**
 * @member {String} role
 */
SummaryOrganisationsInner.prototype['role'] = undefined;






export default SummaryOrganisationsInner;

