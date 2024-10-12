/**
 *  API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-02-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The HostingEnvironmentDeploymentInfo model module.
 * @module model/HostingEnvironmentDeploymentInfo
 * @version 2018-02-01
 */
class HostingEnvironmentDeploymentInfo {
    /**
     * Constructs a new <code>HostingEnvironmentDeploymentInfo</code>.
     * Information needed to create resources on an App Service Environment.
     * @alias module:model/HostingEnvironmentDeploymentInfo
     */
    constructor() { 
        
        HostingEnvironmentDeploymentInfo.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>HostingEnvironmentDeploymentInfo</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/HostingEnvironmentDeploymentInfo} obj Optional instance to populate.
     * @return {module:model/HostingEnvironmentDeploymentInfo} The populated <code>HostingEnvironmentDeploymentInfo</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new HostingEnvironmentDeploymentInfo();

            if (data.hasOwnProperty('location')) {
                obj['location'] = ApiClient.convertToType(data['location'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>HostingEnvironmentDeploymentInfo</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>HostingEnvironmentDeploymentInfo</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['location'] && !(typeof data['location'] === 'string' || data['location'] instanceof String)) {
            throw new Error("Expected the field `location` to be a primitive type in the JSON string but got " + data['location']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }

        return true;
    }


}



/**
 * Location of the App Service Environment.
 * @member {String} location
 */
HostingEnvironmentDeploymentInfo.prototype['location'] = undefined;

/**
 * Name of the App Service Environment.
 * @member {String} name
 */
HostingEnvironmentDeploymentInfo.prototype['name'] = undefined;






export default HostingEnvironmentDeploymentInfo;

