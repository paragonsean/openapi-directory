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
 * The EncryptionInfo model module.
 * @module model/EncryptionInfo
 * @version 4.42.3
 */
class EncryptionInfo {
    /**
     * Constructs a new <code>EncryptionInfo</code>.
     * Encryption states
     * @alias module:model/EncryptionInfo
     * @param dataSpaceKeyState {module:model/EncryptionInfo.DataSpaceKeyStateEnum} DRACOON key state
     * @param roomKeyState {module:model/EncryptionInfo.RoomKeyStateEnum} Room key state
     * @param userKeyState {module:model/EncryptionInfo.UserKeyStateEnum} User key state
     */
    constructor(dataSpaceKeyState, roomKeyState, userKeyState) { 
        
        EncryptionInfo.initialize(this, dataSpaceKeyState, roomKeyState, userKeyState);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, dataSpaceKeyState, roomKeyState, userKeyState) { 
        obj['dataSpaceKeyState'] = dataSpaceKeyState;
        obj['roomKeyState'] = roomKeyState;
        obj['userKeyState'] = userKeyState;
    }

    /**
     * Constructs a <code>EncryptionInfo</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/EncryptionInfo} obj Optional instance to populate.
     * @return {module:model/EncryptionInfo} The populated <code>EncryptionInfo</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new EncryptionInfo();

            if (data.hasOwnProperty('dataSpaceKeyState')) {
                obj['dataSpaceKeyState'] = ApiClient.convertToType(data['dataSpaceKeyState'], 'String');
            }
            if (data.hasOwnProperty('roomKeyState')) {
                obj['roomKeyState'] = ApiClient.convertToType(data['roomKeyState'], 'String');
            }
            if (data.hasOwnProperty('userKeyState')) {
                obj['userKeyState'] = ApiClient.convertToType(data['userKeyState'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>EncryptionInfo</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>EncryptionInfo</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of EncryptionInfo.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['dataSpaceKeyState'] && !(typeof data['dataSpaceKeyState'] === 'string' || data['dataSpaceKeyState'] instanceof String)) {
            throw new Error("Expected the field `dataSpaceKeyState` to be a primitive type in the JSON string but got " + data['dataSpaceKeyState']);
        }
        // ensure the json data is a string
        if (data['roomKeyState'] && !(typeof data['roomKeyState'] === 'string' || data['roomKeyState'] instanceof String)) {
            throw new Error("Expected the field `roomKeyState` to be a primitive type in the JSON string but got " + data['roomKeyState']);
        }
        // ensure the json data is a string
        if (data['userKeyState'] && !(typeof data['userKeyState'] === 'string' || data['userKeyState'] instanceof String)) {
            throw new Error("Expected the field `userKeyState` to be a primitive type in the JSON string but got " + data['userKeyState']);
        }

        return true;
    }


}

EncryptionInfo.RequiredProperties = ["dataSpaceKeyState", "roomKeyState", "userKeyState"];

/**
 * DRACOON key state
 * @member {module:model/EncryptionInfo.DataSpaceKeyStateEnum} dataSpaceKeyState
 */
EncryptionInfo.prototype['dataSpaceKeyState'] = undefined;

/**
 * Room key state
 * @member {module:model/EncryptionInfo.RoomKeyStateEnum} roomKeyState
 */
EncryptionInfo.prototype['roomKeyState'] = undefined;

/**
 * User key state
 * @member {module:model/EncryptionInfo.UserKeyStateEnum} userKeyState
 */
EncryptionInfo.prototype['userKeyState'] = undefined;





/**
 * Allowed values for the <code>dataSpaceKeyState</code> property.
 * @enum {String}
 * @readonly
 */
EncryptionInfo['DataSpaceKeyStateEnum'] = {

    /**
     * value: "none"
     * @const
     */
    "none": "none",

    /**
     * value: "available"
     * @const
     */
    "available": "available",

    /**
     * value: "pending"
     * @const
     */
    "pending": "pending"
};


/**
 * Allowed values for the <code>roomKeyState</code> property.
 * @enum {String}
 * @readonly
 */
EncryptionInfo['RoomKeyStateEnum'] = {

    /**
     * value: "none"
     * @const
     */
    "none": "none",

    /**
     * value: "available"
     * @const
     */
    "available": "available",

    /**
     * value: "pending"
     * @const
     */
    "pending": "pending"
};


/**
 * Allowed values for the <code>userKeyState</code> property.
 * @enum {String}
 * @readonly
 */
EncryptionInfo['UserKeyStateEnum'] = {

    /**
     * value: "none"
     * @const
     */
    "none": "none",

    /**
     * value: "available"
     * @const
     */
    "available": "available",

    /**
     * value: "pending"
     * @const
     */
    "pending": "pending"
};



export default EncryptionInfo;

