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
 * The ApplicationGetEndpoint model module.
 * @module model/ApplicationGetEndpoint
 * @version 2018-06-01-preview
 */
class ApplicationGetEndpoint {
    /**
     * Constructs a new <code>ApplicationGetEndpoint</code>.
     * Gets the application SSH endpoint
     * @alias module:model/ApplicationGetEndpoint
     */
    constructor() { 
        
        ApplicationGetEndpoint.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ApplicationGetEndpoint</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ApplicationGetEndpoint} obj Optional instance to populate.
     * @return {module:model/ApplicationGetEndpoint} The populated <code>ApplicationGetEndpoint</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ApplicationGetEndpoint();

            if (data.hasOwnProperty('destinationPort')) {
                obj['destinationPort'] = ApiClient.convertToType(data['destinationPort'], 'Number');
            }
            if (data.hasOwnProperty('location')) {
                obj['location'] = ApiClient.convertToType(data['location'], 'String');
            }
            if (data.hasOwnProperty('publicPort')) {
                obj['publicPort'] = ApiClient.convertToType(data['publicPort'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ApplicationGetEndpoint</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ApplicationGetEndpoint</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['location'] && !(typeof data['location'] === 'string' || data['location'] instanceof String)) {
            throw new Error("Expected the field `location` to be a primitive type in the JSON string but got " + data['location']);
        }

        return true;
    }


}



/**
 * The destination port to connect to.
 * @member {Number} destinationPort
 */
ApplicationGetEndpoint.prototype['destinationPort'] = undefined;

/**
 * The location of the endpoint.
 * @member {String} location
 */
ApplicationGetEndpoint.prototype['location'] = undefined;

/**
 * The public port to connect to.
 * @member {Number} publicPort
 */
ApplicationGetEndpoint.prototype['publicPort'] = undefined;






export default ApplicationGetEndpoint;

