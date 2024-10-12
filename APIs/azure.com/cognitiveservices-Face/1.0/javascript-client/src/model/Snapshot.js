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
 * The Snapshot model module.
 * @module model/Snapshot
 * @version 1.0
 */
class Snapshot {
    /**
     * Constructs a new <code>Snapshot</code>.
     * Snapshot object.
     * @alias module:model/Snapshot
     * @param account {String} Azure Cognitive Service Face account id of the subscriber who created the snapshot by Snapshot - Take.
     * @param applyScope {Array.<String>} Array of the target Face subscription ids for the snapshot, specified by the user who created the snapshot when calling Snapshot - Take. For each snapshot, only subscriptions included in the applyScope of Snapshot - Take can apply it.
     * @param createdTime {Date} A combined UTC date and time string that describes the created time of the snapshot. E.g. 2018-12-25T11:41:02.2331413Z.
     * @param id {String} Snapshot id.
     * @param lastUpdateTime {Date} A combined UTC date and time string that describes the last time when the snapshot was created or updated by Snapshot - Update. E.g. 2018-12-25T11:51:27.8705696Z.
     * @param type {module:model/Snapshot.TypeEnum} Type of the source object in the snapshot, specified by the subscriber who created the snapshot when calling Snapshot - Take. Currently FaceList, PersonGroup, LargeFaceList and LargePersonGroup are supported.
     */
    constructor(account, applyScope, createdTime, id, lastUpdateTime, type) { 
        
        Snapshot.initialize(this, account, applyScope, createdTime, id, lastUpdateTime, type);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, account, applyScope, createdTime, id, lastUpdateTime, type) { 
        obj['account'] = account;
        obj['applyScope'] = applyScope;
        obj['createdTime'] = createdTime;
        obj['id'] = id;
        obj['lastUpdateTime'] = lastUpdateTime;
        obj['type'] = type;
    }

    /**
     * Constructs a <code>Snapshot</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Snapshot} obj Optional instance to populate.
     * @return {module:model/Snapshot} The populated <code>Snapshot</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Snapshot();

            if (data.hasOwnProperty('account')) {
                obj['account'] = ApiClient.convertToType(data['account'], 'String');
            }
            if (data.hasOwnProperty('applyScope')) {
                obj['applyScope'] = ApiClient.convertToType(data['applyScope'], ['String']);
            }
            if (data.hasOwnProperty('createdTime')) {
                obj['createdTime'] = ApiClient.convertToType(data['createdTime'], 'Date');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('lastUpdateTime')) {
                obj['lastUpdateTime'] = ApiClient.convertToType(data['lastUpdateTime'], 'Date');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
            if (data.hasOwnProperty('userData')) {
                obj['userData'] = ApiClient.convertToType(data['userData'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Snapshot</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Snapshot</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Snapshot.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['account'] && !(typeof data['account'] === 'string' || data['account'] instanceof String)) {
            throw new Error("Expected the field `account` to be a primitive type in the JSON string but got " + data['account']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['applyScope'])) {
            throw new Error("Expected the field `applyScope` to be an array in the JSON data but got " + data['applyScope']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }
        // ensure the json data is a string
        if (data['userData'] && !(typeof data['userData'] === 'string' || data['userData'] instanceof String)) {
            throw new Error("Expected the field `userData` to be a primitive type in the JSON string but got " + data['userData']);
        }

        return true;
    }


}

Snapshot.RequiredProperties = ["account", "applyScope", "createdTime", "id", "lastUpdateTime", "type"];

/**
 * Azure Cognitive Service Face account id of the subscriber who created the snapshot by Snapshot - Take.
 * @member {String} account
 */
Snapshot.prototype['account'] = undefined;

/**
 * Array of the target Face subscription ids for the snapshot, specified by the user who created the snapshot when calling Snapshot - Take. For each snapshot, only subscriptions included in the applyScope of Snapshot - Take can apply it.
 * @member {Array.<String>} applyScope
 */
Snapshot.prototype['applyScope'] = undefined;

/**
 * A combined UTC date and time string that describes the created time of the snapshot. E.g. 2018-12-25T11:41:02.2331413Z.
 * @member {Date} createdTime
 */
Snapshot.prototype['createdTime'] = undefined;

/**
 * Snapshot id.
 * @member {String} id
 */
Snapshot.prototype['id'] = undefined;

/**
 * A combined UTC date and time string that describes the last time when the snapshot was created or updated by Snapshot - Update. E.g. 2018-12-25T11:51:27.8705696Z.
 * @member {Date} lastUpdateTime
 */
Snapshot.prototype['lastUpdateTime'] = undefined;

/**
 * Type of the source object in the snapshot, specified by the subscriber who created the snapshot when calling Snapshot - Take. Currently FaceList, PersonGroup, LargeFaceList and LargePersonGroup are supported.
 * @member {module:model/Snapshot.TypeEnum} type
 */
Snapshot.prototype['type'] = undefined;

/**
 * User specified data about the snapshot for any purpose. Length should not exceed 16KB.
 * @member {String} userData
 */
Snapshot.prototype['userData'] = undefined;





/**
 * Allowed values for the <code>type</code> property.
 * @enum {String}
 * @readonly
 */
Snapshot['TypeEnum'] = {

    /**
     * value: "FaceList"
     * @const
     */
    "FaceList": "FaceList",

    /**
     * value: "LargeFaceList"
     * @const
     */
    "LargeFaceList": "LargeFaceList",

    /**
     * value: "LargePersonGroup"
     * @const
     */
    "LargePersonGroup": "LargePersonGroup",

    /**
     * value: "PersonGroup"
     * @const
     */
    "PersonGroup": "PersonGroup"
};



export default Snapshot;

