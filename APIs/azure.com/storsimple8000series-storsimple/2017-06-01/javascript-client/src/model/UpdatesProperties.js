/**
 * StorSimple8000SeriesManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-06-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The UpdatesProperties model module.
 * @module model/UpdatesProperties
 * @version 2017-06-01
 */
class UpdatesProperties {
    /**
     * Constructs a new <code>UpdatesProperties</code>.
     * The properties of the updates profile.
     * @alias module:model/UpdatesProperties
     */
    constructor() { 
        
        UpdatesProperties.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>UpdatesProperties</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UpdatesProperties} obj Optional instance to populate.
     * @return {module:model/UpdatesProperties} The populated <code>UpdatesProperties</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UpdatesProperties();

            if (data.hasOwnProperty('isUpdateInProgress')) {
                obj['isUpdateInProgress'] = ApiClient.convertToType(data['isUpdateInProgress'], 'Boolean');
            }
            if (data.hasOwnProperty('lastUpdatedTime')) {
                obj['lastUpdatedTime'] = ApiClient.convertToType(data['lastUpdatedTime'], 'Date');
            }
            if (data.hasOwnProperty('maintenanceModeUpdatesAvailable')) {
                obj['maintenanceModeUpdatesAvailable'] = ApiClient.convertToType(data['maintenanceModeUpdatesAvailable'], 'Boolean');
            }
            if (data.hasOwnProperty('regularUpdatesAvailable')) {
                obj['regularUpdatesAvailable'] = ApiClient.convertToType(data['regularUpdatesAvailable'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UpdatesProperties</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UpdatesProperties</code>.
     */
    static validateJSON(data) {

        return true;
    }


}



/**
 * Indicates whether an update is in progress or not.
 * @member {Boolean} isUpdateInProgress
 */
UpdatesProperties.prototype['isUpdateInProgress'] = undefined;

/**
 * The time when the last update was completed.
 * @member {Date} lastUpdatedTime
 */
UpdatesProperties.prototype['lastUpdatedTime'] = undefined;

/**
 * Set to 'true' if maintenance mode update available.
 * @member {Boolean} maintenanceModeUpdatesAvailable
 */
UpdatesProperties.prototype['maintenanceModeUpdatesAvailable'] = undefined;

/**
 * Set to 'true' if regular updates are available for the device.
 * @member {Boolean} regularUpdatesAvailable
 */
UpdatesProperties.prototype['regularUpdatesAvailable'] = undefined;






export default UpdatesProperties;

