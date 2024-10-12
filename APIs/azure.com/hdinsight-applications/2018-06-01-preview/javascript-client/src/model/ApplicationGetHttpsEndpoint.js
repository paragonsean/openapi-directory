/**
 * HDInsightManagementClient
 * The HDInsight Management Client.
 *
 * The version of the OpenAPI document: 2018-06-01-preview
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The ApplicationGetHttpsEndpoint model module.
 * @module model/ApplicationGetHttpsEndpoint
 * @version 2018-06-01-preview
 */
class ApplicationGetHttpsEndpoint {
    /**
     * Constructs a new <code>ApplicationGetHttpsEndpoint</code>.
     * Gets the application HTTP endpoints.
     * @alias module:model/ApplicationGetHttpsEndpoint
     */
    constructor() { 
        
        ApplicationGetHttpsEndpoint.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ApplicationGetHttpsEndpoint</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ApplicationGetHttpsEndpoint} obj Optional instance to populate.
     * @return {module:model/ApplicationGetHttpsEndpoint} The populated <code>ApplicationGetHttpsEndpoint</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ApplicationGetHttpsEndpoint();

            if (data.hasOwnProperty('accessModes')) {
                obj['accessModes'] = ApiClient.convertToType(data['accessModes'], ['String']);
            }
            if (data.hasOwnProperty('destinationPort')) {
                obj['destinationPort'] = ApiClient.convertToType(data['destinationPort'], 'Number');
            }
            if (data.hasOwnProperty('disableGatewayAuth')) {
                obj['disableGatewayAuth'] = ApiClient.convertToType(data['disableGatewayAuth'], 'Boolean');
            }
            if (data.hasOwnProperty('location')) {
                obj['location'] = ApiClient.convertToType(data['location'], 'String');
            }
            if (data.hasOwnProperty('publicPort')) {
                obj['publicPort'] = ApiClient.convertToType(data['publicPort'], 'Number');
            }
            if (data.hasOwnProperty('subDomainSuffix')) {
                obj['subDomainSuffix'] = ApiClient.convertToType(data['subDomainSuffix'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ApplicationGetHttpsEndpoint</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ApplicationGetHttpsEndpoint</code>.
     */
    static validateJSON(data) {
        // ensure the json data is an array
        if (!Array.isArray(data['accessModes'])) {
            throw new Error("Expected the field `accessModes` to be an array in the JSON data but got " + data['accessModes']);
        }
        // ensure the json data is a string
        if (data['location'] && !(typeof data['location'] === 'string' || data['location'] instanceof String)) {
            throw new Error("Expected the field `location` to be a primitive type in the JSON string but got " + data['location']);
        }
        // ensure the json data is a string
        if (data['subDomainSuffix'] && !(typeof data['subDomainSuffix'] === 'string' || data['subDomainSuffix'] instanceof String)) {
            throw new Error("Expected the field `subDomainSuffix` to be a primitive type in the JSON string but got " + data['subDomainSuffix']);
        }

        return true;
    }


}



/**
 * The list of access modes for the application.
 * @member {Array.<String>} accessModes
 */
ApplicationGetHttpsEndpoint.prototype['accessModes'] = undefined;

/**
 * The destination port to connect to.
 * @member {Number} destinationPort
 */
ApplicationGetHttpsEndpoint.prototype['destinationPort'] = undefined;

/**
 * The value indicates whether to disable GatewayAuth.
 * @member {Boolean} disableGatewayAuth
 */
ApplicationGetHttpsEndpoint.prototype['disableGatewayAuth'] = undefined;

/**
 * The location of the endpoint.
 * @member {String} location
 */
ApplicationGetHttpsEndpoint.prototype['location'] = undefined;

/**
 * The public port to connect to.
 * @member {Number} publicPort
 */
ApplicationGetHttpsEndpoint.prototype['publicPort'] = undefined;

/**
 * The subdomain suffix of the application.
 * @member {String} subDomainSuffix
 */
ApplicationGetHttpsEndpoint.prototype['subDomainSuffix'] = undefined;






export default ApplicationGetHttpsEndpoint;

