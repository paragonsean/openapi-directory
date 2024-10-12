/**
 *  API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-08-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The DeploymentLocationsHostingEnvironmentsInnerVipMappingsInner model module.
 * @module model/DeploymentLocationsHostingEnvironmentsInnerVipMappingsInner
 * @version 2019-08-01
 */
class DeploymentLocationsHostingEnvironmentsInnerVipMappingsInner {
    /**
     * Constructs a new <code>DeploymentLocationsHostingEnvironmentsInnerVipMappingsInner</code>.
     * Virtual IP mapping.
     * @alias module:model/DeploymentLocationsHostingEnvironmentsInnerVipMappingsInner
     */
    constructor() { 
        
        DeploymentLocationsHostingEnvironmentsInnerVipMappingsInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>DeploymentLocationsHostingEnvironmentsInnerVipMappingsInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/DeploymentLocationsHostingEnvironmentsInnerVipMappingsInner} obj Optional instance to populate.
     * @return {module:model/DeploymentLocationsHostingEnvironmentsInnerVipMappingsInner} The populated <code>DeploymentLocationsHostingEnvironmentsInnerVipMappingsInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new DeploymentLocationsHostingEnvironmentsInnerVipMappingsInner();

            if (data.hasOwnProperty('inUse')) {
                obj['inUse'] = ApiClient.convertToType(data['inUse'], 'Boolean');
            }
            if (data.hasOwnProperty('internalHttpPort')) {
                obj['internalHttpPort'] = ApiClient.convertToType(data['internalHttpPort'], 'Number');
            }
            if (data.hasOwnProperty('internalHttpsPort')) {
                obj['internalHttpsPort'] = ApiClient.convertToType(data['internalHttpsPort'], 'Number');
            }
            if (data.hasOwnProperty('serviceName')) {
                obj['serviceName'] = ApiClient.convertToType(data['serviceName'], 'String');
            }
            if (data.hasOwnProperty('virtualIP')) {
                obj['virtualIP'] = ApiClient.convertToType(data['virtualIP'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>DeploymentLocationsHostingEnvironmentsInnerVipMappingsInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>DeploymentLocationsHostingEnvironmentsInnerVipMappingsInner</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['serviceName'] && !(typeof data['serviceName'] === 'string' || data['serviceName'] instanceof String)) {
            throw new Error("Expected the field `serviceName` to be a primitive type in the JSON string but got " + data['serviceName']);
        }
        // ensure the json data is a string
        if (data['virtualIP'] && !(typeof data['virtualIP'] === 'string' || data['virtualIP'] instanceof String)) {
            throw new Error("Expected the field `virtualIP` to be a primitive type in the JSON string but got " + data['virtualIP']);
        }

        return true;
    }


}



/**
 * Is virtual IP mapping in use.
 * @member {Boolean} inUse
 */
DeploymentLocationsHostingEnvironmentsInnerVipMappingsInner.prototype['inUse'] = undefined;

/**
 * Internal HTTP port.
 * @member {Number} internalHttpPort
 */
DeploymentLocationsHostingEnvironmentsInnerVipMappingsInner.prototype['internalHttpPort'] = undefined;

/**
 * Internal HTTPS port.
 * @member {Number} internalHttpsPort
 */
DeploymentLocationsHostingEnvironmentsInnerVipMappingsInner.prototype['internalHttpsPort'] = undefined;

/**
 * name of the service that virtual IP is assigned to
 * @member {String} serviceName
 */
DeploymentLocationsHostingEnvironmentsInnerVipMappingsInner.prototype['serviceName'] = undefined;

/**
 * Virtual IP address.
 * @member {String} virtualIP
 */
DeploymentLocationsHostingEnvironmentsInnerVipMappingsInner.prototype['virtualIP'] = undefined;






export default DeploymentLocationsHostingEnvironmentsInnerVipMappingsInner;

