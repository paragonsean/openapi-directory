/**
 * Face Client
 * An API for face detection, verification, and identification.
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The ApplySnapshotRequest model module.
 * @module model/ApplySnapshotRequest
 * @version 1.0
 */
class ApplySnapshotRequest {
    /**
     * Constructs a new <code>ApplySnapshotRequest</code>.
     * Request body for applying snapshot operation.
     * @alias module:model/ApplySnapshotRequest
     * @param objectId {String} User specified target object id to be created from the snapshot.
     */
    constructor(objectId) { 
        
        ApplySnapshotRequest.initialize(this, objectId);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, objectId) { 
        obj['mode'] = 'CreateNew';
        obj['objectId'] = objectId;
    }

    /**
     * Constructs a <code>ApplySnapshotRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ApplySnapshotRequest} obj Optional instance to populate.
     * @return {module:model/ApplySnapshotRequest} The populated <code>ApplySnapshotRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ApplySnapshotRequest();

            if (data.hasOwnProperty('mode')) {
                obj['mode'] = ApiClient.convertToType(data['mode'], 'String');
            }
            if (data.hasOwnProperty('objectId')) {
                obj['objectId'] = ApiClient.convertToType(data['objectId'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ApplySnapshotRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ApplySnapshotRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of ApplySnapshotRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['mode'] && !(typeof data['mode'] === 'string' || data['mode'] instanceof String)) {
            throw new Error("Expected the field `mode` to be a primitive type in the JSON string but got " + data['mode']);
        }
        // ensure the json data is a string
        if (data['objectId'] && !(typeof data['objectId'] === 'string' || data['objectId'] instanceof String)) {
            throw new Error("Expected the field `objectId` to be a primitive type in the JSON string but got " + data['objectId']);
        }

        return true;
    }


}

ApplySnapshotRequest.RequiredProperties = ["objectId"];

/**
 * Snapshot applying mode. Currently only CreateNew is supported, which means the apply operation will fail if target subscription already contains an object of same type and using the same objectId. Users can specify the \"objectId\" in request body to avoid such conflicts.
 * @member {module:model/ApplySnapshotRequest.ModeEnum} mode
 * @default 'CreateNew'
 */
ApplySnapshotRequest.prototype['mode'] = 'CreateNew';

/**
 * User specified target object id to be created from the snapshot.
 * @member {String} objectId
 */
ApplySnapshotRequest.prototype['objectId'] = undefined;





/**
 * Allowed values for the <code>mode</code> property.
 * @enum {String}
 * @readonly
 */
ApplySnapshotRequest['ModeEnum'] = {

    /**
     * value: "CreateNew"
     * @const
     */
    "CreateNew": "CreateNew"
};



export default ApplySnapshotRequest;

