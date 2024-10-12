/**
 * FrontDoorManagementClient
 * Use these APIs to manage Azure Front Door resources through the Azure Resource Manager. You must make sure that requests made to these resources are secure.
 *
 * The version of the OpenAPI document: 2019-05-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The BackendPoolUpdateParametersHealthProbeSettings model module.
 * @module model/BackendPoolUpdateParametersHealthProbeSettings
 * @version 2019-05-01
 */
class BackendPoolUpdateParametersHealthProbeSettings {
    /**
     * Constructs a new <code>BackendPoolUpdateParametersHealthProbeSettings</code>.
     * Reference to another subresource.
     * @alias module:model/BackendPoolUpdateParametersHealthProbeSettings
     */
    constructor() { 
        
        BackendPoolUpdateParametersHealthProbeSettings.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>BackendPoolUpdateParametersHealthProbeSettings</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/BackendPoolUpdateParametersHealthProbeSettings} obj Optional instance to populate.
     * @return {module:model/BackendPoolUpdateParametersHealthProbeSettings} The populated <code>BackendPoolUpdateParametersHealthProbeSettings</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new BackendPoolUpdateParametersHealthProbeSettings();

            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>BackendPoolUpdateParametersHealthProbeSettings</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>BackendPoolUpdateParametersHealthProbeSettings</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }

        return true;
    }


}



/**
 * Resource ID.
 * @member {String} id
 */
BackendPoolUpdateParametersHealthProbeSettings.prototype['id'] = undefined;






export default BackendPoolUpdateParametersHealthProbeSettings;

