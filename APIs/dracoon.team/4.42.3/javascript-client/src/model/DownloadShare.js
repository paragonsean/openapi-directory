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
import UserInfo from './UserInfo';

/**
 * The DownloadShare model module.
 * @module model/DownloadShare
 * @version 4.42.3
 */
class DownloadShare {
    /**
     * Constructs a new <code>DownloadShare</code>.
     * Download Share information
     * @alias module:model/DownloadShare
     * @param accessKey {String} Share access key to generate secure link
     * @param cntDownloads {Number} Downloads counter (incremented on each download)
     * @param createdAt {Date} Creation date
     * @param createdBy {module:model/UserInfo} 
     * @param id {Number} Share ID
     * @param name {String} Alias name
     * @param nodeId {Number} Source node ID
     * @param notifyCreator {Boolean} &#128679; Deprecated since v4.20.0  Notify creator on every download.
     */
    constructor(accessKey, cntDownloads, createdAt, createdBy, id, name, nodeId, notifyCreator) { 
        
        DownloadShare.initialize(this, accessKey, cntDownloads, createdAt, createdBy, id, name, nodeId, notifyCreator);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, accessKey, cntDownloads, createdAt, createdBy, id, name, nodeId, notifyCreator) { 
        obj['accessKey'] = accessKey;
        obj['cntDownloads'] = cntDownloads;
        obj['createdAt'] = createdAt;
        obj['createdBy'] = createdBy;
        obj['id'] = id;
        obj['name'] = name;
        obj['nodeId'] = nodeId;
        obj['notifyCreator'] = notifyCreator;
    }

    /**
     * Constructs a <code>DownloadShare</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/DownloadShare} obj Optional instance to populate.
     * @return {module:model/DownloadShare} The populated <code>DownloadShare</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new DownloadShare();

            if (data.hasOwnProperty('accessKey')) {
                obj['accessKey'] = ApiClient.convertToType(data['accessKey'], 'String');
            }
            if (data.hasOwnProperty('classification')) {
                obj['classification'] = ApiClient.convertToType(data['classification'], 'Number');
            }
            if (data.hasOwnProperty('cntDownloads')) {
                obj['cntDownloads'] = ApiClient.convertToType(data['cntDownloads'], 'Number');
            }
            if (data.hasOwnProperty('createdAt')) {
                obj['createdAt'] = ApiClient.convertToType(data['createdAt'], 'Date');
            }
            if (data.hasOwnProperty('createdBy')) {
                obj['createdBy'] = UserInfo.constructFromObject(data['createdBy']);
            }
            if (data.hasOwnProperty('dataUrl')) {
                obj['dataUrl'] = ApiClient.convertToType(data['dataUrl'], 'String');
            }
            if (data.hasOwnProperty('expireAt')) {
                obj['expireAt'] = ApiClient.convertToType(data['expireAt'], 'Date');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('internalNotes')) {
                obj['internalNotes'] = ApiClient.convertToType(data['internalNotes'], 'String');
            }
            if (data.hasOwnProperty('isEncrypted')) {
                obj['isEncrypted'] = ApiClient.convertToType(data['isEncrypted'], 'Boolean');
            }
            if (data.hasOwnProperty('isProtected')) {
                obj['isProtected'] = ApiClient.convertToType(data['isProtected'], 'Boolean');
            }
            if (data.hasOwnProperty('maxDownloads')) {
                obj['maxDownloads'] = ApiClient.convertToType(data['maxDownloads'], 'Number');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('nodeId')) {
                obj['nodeId'] = ApiClient.convertToType(data['nodeId'], 'Number');
            }
            if (data.hasOwnProperty('nodePath')) {
                obj['nodePath'] = ApiClient.convertToType(data['nodePath'], 'String');
            }
            if (data.hasOwnProperty('nodeType')) {
                obj['nodeType'] = ApiClient.convertToType(data['nodeType'], 'String');
            }
            if (data.hasOwnProperty('notes')) {
                obj['notes'] = ApiClient.convertToType(data['notes'], 'String');
            }
            if (data.hasOwnProperty('notifyCreator')) {
                obj['notifyCreator'] = ApiClient.convertToType(data['notifyCreator'], 'Boolean');
            }
            if (data.hasOwnProperty('recipients')) {
                obj['recipients'] = ApiClient.convertToType(data['recipients'], 'String');
            }
            if (data.hasOwnProperty('showCreatorName')) {
                obj['showCreatorName'] = ApiClient.convertToType(data['showCreatorName'], 'Boolean');
            }
            if (data.hasOwnProperty('showCreatorUsername')) {
                obj['showCreatorUsername'] = ApiClient.convertToType(data['showCreatorUsername'], 'Boolean');
            }
            if (data.hasOwnProperty('smsRecipients')) {
                obj['smsRecipients'] = ApiClient.convertToType(data['smsRecipients'], 'String');
            }
            if (data.hasOwnProperty('updatedAt')) {
                obj['updatedAt'] = ApiClient.convertToType(data['updatedAt'], 'Date');
            }
            if (data.hasOwnProperty('updatedBy')) {
                obj['updatedBy'] = UserInfo.constructFromObject(data['updatedBy']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>DownloadShare</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>DownloadShare</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of DownloadShare.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['accessKey'] && !(typeof data['accessKey'] === 'string' || data['accessKey'] instanceof String)) {
            throw new Error("Expected the field `accessKey` to be a primitive type in the JSON string but got " + data['accessKey']);
        }
        // validate the optional field `createdBy`
        if (data['createdBy']) { // data not null
          UserInfo.validateJSON(data['createdBy']);
        }
        // ensure the json data is a string
        if (data['dataUrl'] && !(typeof data['dataUrl'] === 'string' || data['dataUrl'] instanceof String)) {
            throw new Error("Expected the field `dataUrl` to be a primitive type in the JSON string but got " + data['dataUrl']);
        }
        // ensure the json data is a string
        if (data['internalNotes'] && !(typeof data['internalNotes'] === 'string' || data['internalNotes'] instanceof String)) {
            throw new Error("Expected the field `internalNotes` to be a primitive type in the JSON string but got " + data['internalNotes']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['nodePath'] && !(typeof data['nodePath'] === 'string' || data['nodePath'] instanceof String)) {
            throw new Error("Expected the field `nodePath` to be a primitive type in the JSON string but got " + data['nodePath']);
        }
        // ensure the json data is a string
        if (data['nodeType'] && !(typeof data['nodeType'] === 'string' || data['nodeType'] instanceof String)) {
            throw new Error("Expected the field `nodeType` to be a primitive type in the JSON string but got " + data['nodeType']);
        }
        // ensure the json data is a string
        if (data['notes'] && !(typeof data['notes'] === 'string' || data['notes'] instanceof String)) {
            throw new Error("Expected the field `notes` to be a primitive type in the JSON string but got " + data['notes']);
        }
        // ensure the json data is a string
        if (data['recipients'] && !(typeof data['recipients'] === 'string' || data['recipients'] instanceof String)) {
            throw new Error("Expected the field `recipients` to be a primitive type in the JSON string but got " + data['recipients']);
        }
        // ensure the json data is a string
        if (data['smsRecipients'] && !(typeof data['smsRecipients'] === 'string' || data['smsRecipients'] instanceof String)) {
            throw new Error("Expected the field `smsRecipients` to be a primitive type in the JSON string but got " + data['smsRecipients']);
        }
        // validate the optional field `updatedBy`
        if (data['updatedBy']) { // data not null
          UserInfo.validateJSON(data['updatedBy']);
        }

        return true;
    }


}

DownloadShare.RequiredProperties = ["accessKey", "cntDownloads", "createdAt", "createdBy", "id", "name", "nodeId", "notifyCreator"];

/**
 * Share access key to generate secure link
 * @member {String} accessKey
 */
DownloadShare.prototype['accessKey'] = undefined;

/**
 * &#128679; Deprecated since v4.11.0  Classification ID:  * `1` - public  * `2` - internal  * `3` - confidential  * `4` - strictly confidential    (default: classification from parent room)
 * @member {module:model/DownloadShare.ClassificationEnum} classification
 */
DownloadShare.prototype['classification'] = undefined;

/**
 * Downloads counter (incremented on each download)
 * @member {Number} cntDownloads
 */
DownloadShare.prototype['cntDownloads'] = undefined;

/**
 * Creation date
 * @member {Date} createdAt
 */
DownloadShare.prototype['createdAt'] = undefined;

/**
 * @member {module:model/UserInfo} createdBy
 */
DownloadShare.prototype['createdBy'] = undefined;

/**
 * Path to shared download node
 * @member {String} dataUrl
 */
DownloadShare.prototype['dataUrl'] = undefined;

/**
 * Expiration date
 * @member {Date} expireAt
 */
DownloadShare.prototype['expireAt'] = undefined;

/**
 * Share ID
 * @member {Number} id
 */
DownloadShare.prototype['id'] = undefined;

/**
 * &#128640; Since v4.11.0  Internal notes
 * @member {String} internalNotes
 */
DownloadShare.prototype['internalNotes'] = undefined;

/**
 * Encrypted share  (this only applies to shared files, not folders)
 * @member {Boolean} isEncrypted
 */
DownloadShare.prototype['isEncrypted'] = undefined;

/**
 * Is share protected by password
 * @member {Boolean} isProtected
 */
DownloadShare.prototype['isProtected'] = undefined;

/**
 * Max allowed downloads
 * @member {Number} maxDownloads
 */
DownloadShare.prototype['maxDownloads'] = undefined;

/**
 * Alias name
 * @member {String} name
 */
DownloadShare.prototype['name'] = undefined;

/**
 * Source node ID
 * @member {Number} nodeId
 */
DownloadShare.prototype['nodeId'] = undefined;

/**
 * Path to shared download node
 * @member {String} nodePath
 */
DownloadShare.prototype['nodePath'] = undefined;

/**
 * Node type
 * @member {String} nodeType
 */
DownloadShare.prototype['nodeType'] = undefined;

/**
 * User notes
 * @member {String} notes
 */
DownloadShare.prototype['notes'] = undefined;

/**
 * &#128679; Deprecated since v4.20.0  Notify creator on every download.
 * @member {Boolean} notifyCreator
 */
DownloadShare.prototype['notifyCreator'] = undefined;

/**
 * &#128679; Deprecated since v4.11.0  CSV string of recipient email addresses
 * @member {String} recipients
 */
DownloadShare.prototype['recipients'] = undefined;

/**
 * Show creator first and last name.
 * @member {Boolean} showCreatorName
 */
DownloadShare.prototype['showCreatorName'] = undefined;

/**
 * Show creator email address.
 * @member {Boolean} showCreatorUsername
 */
DownloadShare.prototype['showCreatorUsername'] = undefined;

/**
 * &#128679; Deprecated since v4.11.0  CSV string of recipient MSISDNs
 * @member {String} smsRecipients
 */
DownloadShare.prototype['smsRecipients'] = undefined;

/**
 * Modification date
 * @member {Date} updatedAt
 */
DownloadShare.prototype['updatedAt'] = undefined;

/**
 * @member {module:model/UserInfo} updatedBy
 */
DownloadShare.prototype['updatedBy'] = undefined;





/**
 * Allowed values for the <code>classification</code> property.
 * @enum {Number}
 * @readonly
 */
DownloadShare['ClassificationEnum'] = {

    /**
     * value: 1
     * @const
     */
    "1": 1,

    /**
     * value: 2
     * @const
     */
    "2": 2,

    /**
     * value: 3
     * @const
     */
    "3": 3,

    /**
     * value: 4
     * @const
     */
    "4": 4
};



export default DownloadShare;

