/**
 * SqlManagementClient
 * The Azure SQL Database management API provides a RESTful set of web APIs that interact with Azure SQL Database services to manage your databases. The API enables users to create, retrieve, update, and delete databases, servers, and other entities.
 *
 * The version of the OpenAPI document: 2017-03-01-preview
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import ServerSecurityAlertPolicy from './ServerSecurityAlertPolicy';

/**
 * The LogicalServerSecurityAlertPolicyListResult model module.
 * @module model/LogicalServerSecurityAlertPolicyListResult
 * @version 2017-03-01-preview
 */
class LogicalServerSecurityAlertPolicyListResult {
    /**
     * Constructs a new <code>LogicalServerSecurityAlertPolicyListResult</code>.
     * A list of the server&#39;s security alert policies.
     * @alias module:model/LogicalServerSecurityAlertPolicyListResult
     */
    constructor() { 
        
        LogicalServerSecurityAlertPolicyListResult.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>LogicalServerSecurityAlertPolicyListResult</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/LogicalServerSecurityAlertPolicyListResult} obj Optional instance to populate.
     * @return {module:model/LogicalServerSecurityAlertPolicyListResult} The populated <code>LogicalServerSecurityAlertPolicyListResult</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new LogicalServerSecurityAlertPolicyListResult();

            if (data.hasOwnProperty('nextLink')) {
                obj['nextLink'] = ApiClient.convertToType(data['nextLink'], 'String');
            }
            if (data.hasOwnProperty('value')) {
                obj['value'] = ApiClient.convertToType(data['value'], [ServerSecurityAlertPolicy]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>LogicalServerSecurityAlertPolicyListResult</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>LogicalServerSecurityAlertPolicyListResult</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['nextLink'] && !(typeof data['nextLink'] === 'string' || data['nextLink'] instanceof String)) {
            throw new Error("Expected the field `nextLink` to be a primitive type in the JSON string but got " + data['nextLink']);
        }
        if (data['value']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['value'])) {
                throw new Error("Expected the field `value` to be an array in the JSON data but got " + data['value']);
            }
            // validate the optional field `value` (array)
            for (const item of data['value']) {
                ServerSecurityAlertPolicy.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * Link to retrieve next page of results.
 * @member {String} nextLink
 */
LogicalServerSecurityAlertPolicyListResult.prototype['nextLink'] = undefined;

/**
 * Array of results.
 * @member {Array.<module:model/ServerSecurityAlertPolicy>} value
 */
LogicalServerSecurityAlertPolicyListResult.prototype['value'] = undefined;






export default LogicalServerSecurityAlertPolicyListResult;

