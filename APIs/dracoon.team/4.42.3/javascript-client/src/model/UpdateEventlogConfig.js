/**
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The UpdateEventlogConfig model module.
 * @module model/UpdateEventlogConfig
 * @version 4.42.3
 */
class UpdateEventlogConfig {
    /**
     * Constructs a new <code>UpdateEventlogConfig</code>.
     * Request model for updating eventlog settings
     * @alias module:model/UpdateEventlogConfig
     */
    constructor() { 
        
        UpdateEventlogConfig.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>UpdateEventlogConfig</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UpdateEventlogConfig} obj Optional instance to populate.
     * @return {module:model/UpdateEventlogConfig} The populated <code>UpdateEventlogConfig</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UpdateEventlogConfig();

            if (data.hasOwnProperty('enabled')) {
                obj['enabled'] = ApiClient.convertToType(data['enabled'], 'Boolean');
            }
            if (data.hasOwnProperty('logIpEnabled')) {
                obj['logIpEnabled'] = ApiClient.convertToType(data['logIpEnabled'], 'Boolean');
            }
            if (data.hasOwnProperty('retentionPeriod')) {
                obj['retentionPeriod'] = ApiClient.convertToType(data['retentionPeriod'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UpdateEventlogConfig</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UpdateEventlogConfig</code>.
     */
    static validateJSON(data) {

        return true;
    }


}



/**
 * Is eventlog enabled?
 * @member {Boolean} enabled
 */
UpdateEventlogConfig.prototype['enabled'] = undefined;

/**
 * Determines whether user’s IP address is logged.
 * @member {Boolean} logIpEnabled
 */
UpdateEventlogConfig.prototype['logIpEnabled'] = undefined;

/**
 * Retention period (in days) of event log entries.  After that period, all entries are deleted.  Recommended value: 7
 * @member {Number} retentionPeriod
 */
UpdateEventlogConfig.prototype['retentionPeriod'] = undefined;






export default UpdateEventlogConfig;

