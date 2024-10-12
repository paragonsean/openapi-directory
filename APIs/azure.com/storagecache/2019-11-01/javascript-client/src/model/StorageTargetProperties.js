/**
 * Storage Cache Mgmt Client
 * A Storage Cache provides scalable caching service for NAS clients, serving data from either NFSv3 or Blob at-rest storage (referred to as \"Storage Targets\"). These operations allow you to manage Caches.
 *
 * The version of the OpenAPI document: 2019-11-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import ClfsTarget from './ClfsTarget';
import NamespaceJunction from './NamespaceJunction';
import Nfs3Target from './Nfs3Target';
import UnknownTarget from './UnknownTarget';

/**
 * The StorageTargetProperties model module.
 * @module model/StorageTargetProperties
 * @version 2019-11-01
 */
class StorageTargetProperties {
    /**
     * Constructs a new <code>StorageTargetProperties</code>.
     * Properties of the Storage Target.
     * @alias module:model/StorageTargetProperties
     */
    constructor() { 
        
        StorageTargetProperties.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>StorageTargetProperties</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/StorageTargetProperties} obj Optional instance to populate.
     * @return {module:model/StorageTargetProperties} The populated <code>StorageTargetProperties</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new StorageTargetProperties();

            if (data.hasOwnProperty('clfs')) {
                obj['clfs'] = ClfsTarget.constructFromObject(data['clfs']);
            }
            if (data.hasOwnProperty('junctions')) {
                obj['junctions'] = ApiClient.convertToType(data['junctions'], [NamespaceJunction]);
            }
            if (data.hasOwnProperty('nfs3')) {
                obj['nfs3'] = Nfs3Target.constructFromObject(data['nfs3']);
            }
            if (data.hasOwnProperty('provisioningState')) {
                obj['provisioningState'] = ApiClient.convertToType(data['provisioningState'], 'String');
            }
            if (data.hasOwnProperty('targetType')) {
                obj['targetType'] = ApiClient.convertToType(data['targetType'], 'String');
            }
            if (data.hasOwnProperty('unknown')) {
                obj['unknown'] = UnknownTarget.constructFromObject(data['unknown']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>StorageTargetProperties</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>StorageTargetProperties</code>.
     */
    static validateJSON(data) {
        // validate the optional field `clfs`
        if (data['clfs']) { // data not null
          ClfsTarget.validateJSON(data['clfs']);
        }
        if (data['junctions']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['junctions'])) {
                throw new Error("Expected the field `junctions` to be an array in the JSON data but got " + data['junctions']);
            }
            // validate the optional field `junctions` (array)
            for (const item of data['junctions']) {
                NamespaceJunction.validateJSON(item);
            };
        }
        // validate the optional field `nfs3`
        if (data['nfs3']) { // data not null
          Nfs3Target.validateJSON(data['nfs3']);
        }
        // ensure the json data is a string
        if (data['provisioningState'] && !(typeof data['provisioningState'] === 'string' || data['provisioningState'] instanceof String)) {
            throw new Error("Expected the field `provisioningState` to be a primitive type in the JSON string but got " + data['provisioningState']);
        }
        // ensure the json data is a string
        if (data['targetType'] && !(typeof data['targetType'] === 'string' || data['targetType'] instanceof String)) {
            throw new Error("Expected the field `targetType` to be a primitive type in the JSON string but got " + data['targetType']);
        }
        // validate the optional field `unknown`
        if (data['unknown']) { // data not null
          UnknownTarget.validateJSON(data['unknown']);
        }

        return true;
    }


}



/**
 * @member {module:model/ClfsTarget} clfs
 */
StorageTargetProperties.prototype['clfs'] = undefined;

/**
 * List of Cache namespace junctions to target for namespace associations.
 * @member {Array.<module:model/NamespaceJunction>} junctions
 */
StorageTargetProperties.prototype['junctions'] = undefined;

/**
 * @member {module:model/Nfs3Target} nfs3
 */
StorageTargetProperties.prototype['nfs3'] = undefined;

/**
 * ARM provisioning state, see https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/Addendum.md#provisioningstate-property
 * @member {module:model/StorageTargetProperties.ProvisioningStateEnum} provisioningState
 */
StorageTargetProperties.prototype['provisioningState'] = undefined;

/**
 * Type of the Storage Target.
 * @member {module:model/StorageTargetProperties.TargetTypeEnum} targetType
 */
StorageTargetProperties.prototype['targetType'] = undefined;

/**
 * @member {module:model/UnknownTarget} unknown
 */
StorageTargetProperties.prototype['unknown'] = undefined;





/**
 * Allowed values for the <code>provisioningState</code> property.
 * @enum {String}
 * @readonly
 */
StorageTargetProperties['ProvisioningStateEnum'] = {

    /**
     * value: "Succeeded"
     * @const
     */
    "Succeeded": "Succeeded",

    /**
     * value: "Failed"
     * @const
     */
    "Failed": "Failed",

    /**
     * value: "Cancelled"
     * @const
     */
    "Cancelled": "Cancelled",

    /**
     * value: "Creating"
     * @const
     */
    "Creating": "Creating",

    /**
     * value: "Deleting"
     * @const
     */
    "Deleting": "Deleting",

    /**
     * value: "Updating"
     * @const
     */
    "Updating": "Updating"
};


/**
 * Allowed values for the <code>targetType</code> property.
 * @enum {String}
 * @readonly
 */
StorageTargetProperties['TargetTypeEnum'] = {

    /**
     * value: "nfs3"
     * @const
     */
    "nfs3": "nfs3",

    /**
     * value: "clfs"
     * @const
     */
    "clfs": "clfs",

    /**
     * value: "unknown"
     * @const
     */
    "unknown": "unknown"
};



export default StorageTargetProperties;

