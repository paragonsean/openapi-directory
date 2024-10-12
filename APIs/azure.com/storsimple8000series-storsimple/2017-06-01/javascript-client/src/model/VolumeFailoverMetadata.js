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
 * The VolumeFailoverMetadata model module.
 * @module model/VolumeFailoverMetadata
 * @version 2017-06-01
 */
class VolumeFailoverMetadata {
    /**
     * Constructs a new <code>VolumeFailoverMetadata</code>.
     * The metadata of a volume that has valid cloud snapshot.
     * @alias module:model/VolumeFailoverMetadata
     */
    constructor() { 
        
        VolumeFailoverMetadata.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>VolumeFailoverMetadata</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/VolumeFailoverMetadata} obj Optional instance to populate.
     * @return {module:model/VolumeFailoverMetadata} The populated <code>VolumeFailoverMetadata</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new VolumeFailoverMetadata();

            if (data.hasOwnProperty('backupCreatedDate')) {
                obj['backupCreatedDate'] = ApiClient.convertToType(data['backupCreatedDate'], 'Date');
            }
            if (data.hasOwnProperty('backupElementId')) {
                obj['backupElementId'] = ApiClient.convertToType(data['backupElementId'], 'String');
            }
            if (data.hasOwnProperty('backupId')) {
                obj['backupId'] = ApiClient.convertToType(data['backupId'], 'String');
            }
            if (data.hasOwnProperty('backupPolicyId')) {
                obj['backupPolicyId'] = ApiClient.convertToType(data['backupPolicyId'], 'String');
            }
            if (data.hasOwnProperty('sizeInBytes')) {
                obj['sizeInBytes'] = ApiClient.convertToType(data['sizeInBytes'], 'Number');
            }
            if (data.hasOwnProperty('volumeId')) {
                obj['volumeId'] = ApiClient.convertToType(data['volumeId'], 'String');
            }
            if (data.hasOwnProperty('volumeType')) {
                obj['volumeType'] = ApiClient.convertToType(data['volumeType'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>VolumeFailoverMetadata</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>VolumeFailoverMetadata</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['backupElementId'] && !(typeof data['backupElementId'] === 'string' || data['backupElementId'] instanceof String)) {
            throw new Error("Expected the field `backupElementId` to be a primitive type in the JSON string but got " + data['backupElementId']);
        }
        // ensure the json data is a string
        if (data['backupId'] && !(typeof data['backupId'] === 'string' || data['backupId'] instanceof String)) {
            throw new Error("Expected the field `backupId` to be a primitive type in the JSON string but got " + data['backupId']);
        }
        // ensure the json data is a string
        if (data['backupPolicyId'] && !(typeof data['backupPolicyId'] === 'string' || data['backupPolicyId'] instanceof String)) {
            throw new Error("Expected the field `backupPolicyId` to be a primitive type in the JSON string but got " + data['backupPolicyId']);
        }
        // ensure the json data is a string
        if (data['volumeId'] && !(typeof data['volumeId'] === 'string' || data['volumeId'] instanceof String)) {
            throw new Error("Expected the field `volumeId` to be a primitive type in the JSON string but got " + data['volumeId']);
        }
        // ensure the json data is a string
        if (data['volumeType'] && !(typeof data['volumeType'] === 'string' || data['volumeType'] instanceof String)) {
            throw new Error("Expected the field `volumeType` to be a primitive type in the JSON string but got " + data['volumeType']);
        }

        return true;
    }


}



/**
 * The date at which the snapshot was taken.
 * @member {Date} backupCreatedDate
 */
VolumeFailoverMetadata.prototype['backupCreatedDate'] = undefined;

/**
 * The path ID of the backup-element for this volume, inside the backup set.
 * @member {String} backupElementId
 */
VolumeFailoverMetadata.prototype['backupElementId'] = undefined;

/**
 * The path ID of the backup set.
 * @member {String} backupId
 */
VolumeFailoverMetadata.prototype['backupId'] = undefined;

/**
 * The path ID of the backup policy using which the snapshot was taken.
 * @member {String} backupPolicyId
 */
VolumeFailoverMetadata.prototype['backupPolicyId'] = undefined;

/**
 * The size of the volume in bytes at the time the snapshot was taken.
 * @member {Number} sizeInBytes
 */
VolumeFailoverMetadata.prototype['sizeInBytes'] = undefined;

/**
 * The path ID of the volume.
 * @member {String} volumeId
 */
VolumeFailoverMetadata.prototype['volumeId'] = undefined;

/**
 * The type of the volume.
 * @member {module:model/VolumeFailoverMetadata.VolumeTypeEnum} volumeType
 */
VolumeFailoverMetadata.prototype['volumeType'] = undefined;





/**
 * Allowed values for the <code>volumeType</code> property.
 * @enum {String}
 * @readonly
 */
VolumeFailoverMetadata['VolumeTypeEnum'] = {

    /**
     * value: "Tiered"
     * @const
     */
    "Tiered": "Tiered",

    /**
     * value: "Archival"
     * @const
     */
    "Archival": "Archival",

    /**
     * value: "LocallyPinned"
     * @const
     */
    "LocallyPinned": "LocallyPinned"
};



export default VolumeFailoverMetadata;

