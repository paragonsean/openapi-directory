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
 * The BackupFilter model module.
 * @module model/BackupFilter
 * @version 2017-06-01
 */
class BackupFilter {
    /**
     * Constructs a new <code>BackupFilter</code>.
     * The OData filters to be used for backups.
     * @alias module:model/BackupFilter
     */
    constructor() { 
        
        BackupFilter.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>BackupFilter</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/BackupFilter} obj Optional instance to populate.
     * @return {module:model/BackupFilter} The populated <code>BackupFilter</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new BackupFilter();

            if (data.hasOwnProperty('backupPolicyId')) {
                obj['backupPolicyId'] = ApiClient.convertToType(data['backupPolicyId'], 'String');
            }
            if (data.hasOwnProperty('createdTime')) {
                obj['createdTime'] = ApiClient.convertToType(data['createdTime'], 'Date');
            }
            if (data.hasOwnProperty('volumeId')) {
                obj['volumeId'] = ApiClient.convertToType(data['volumeId'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>BackupFilter</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>BackupFilter</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['backupPolicyId'] && !(typeof data['backupPolicyId'] === 'string' || data['backupPolicyId'] instanceof String)) {
            throw new Error("Expected the field `backupPolicyId` to be a primitive type in the JSON string but got " + data['backupPolicyId']);
        }
        // ensure the json data is a string
        if (data['volumeId'] && !(typeof data['volumeId'] === 'string' || data['volumeId'] instanceof String)) {
            throw new Error("Expected the field `volumeId` to be a primitive type in the JSON string but got " + data['volumeId']);
        }

        return true;
    }


}



/**
 * Specifies the backupPolicyId of the backups to be filtered. Only 'Equality' operator is supported for this property.
 * @member {String} backupPolicyId
 */
BackupFilter.prototype['backupPolicyId'] = undefined;

/**
 * Specifies the creation time of the backups to be filtered. Only 'Greater Than or Equal To' and 'Lesser Than or Equal To' operators are supported for this property.
 * @member {Date} createdTime
 */
BackupFilter.prototype['createdTime'] = undefined;

/**
 * Specifies the volumeId of the backups to be filtered. Only 'Equality' operator is supported for this property.
 * @member {String} volumeId
 */
BackupFilter.prototype['volumeId'] = undefined;






export default BackupFilter;

