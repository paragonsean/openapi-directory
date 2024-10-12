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
import AuthMethod from './AuthMethod';

/**
 * The SystemInfo model module.
 * @module model/SystemInfo
 * @version 4.42.3
 */
class SystemInfo {
    /**
     * Constructs a new <code>SystemInfo</code>.
     * System information (default language and authentication methods)
     * @alias module:model/SystemInfo
     * @param authMethods {Array.<module:model/AuthMethod>} &#128679; Deprecated since v4.13.0  Authentication methods:  * `sql`  * `active_directory`  * `radius`  * `openid`  use `authData` instead
     * @param hideLoginInputFields {Boolean} &#128679; Deprecated since v4.42.0  Defines if login fields should be hidden
     * @param languageDefault {String} System default language  cf. [RFC 5646](https://tools.ietf.org/html/rfc5646)
     * @param s3EnforceDirectUpload {Boolean} &#128640; Since v4.15.0  Determines whether S3 direct upload is enforced or not
     * @param s3Hosts {Array.<String>} &#128640; Since v4.14.0  List of S3 Hosts for CSP header
     * @param useS3Storage {Boolean} &#128640; Since v4.21.0  Defines if S3 is used as storage backend
     */
    constructor(authMethods, hideLoginInputFields, languageDefault, s3EnforceDirectUpload, s3Hosts, useS3Storage) { 
        
        SystemInfo.initialize(this, authMethods, hideLoginInputFields, languageDefault, s3EnforceDirectUpload, s3Hosts, useS3Storage);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, authMethods, hideLoginInputFields, languageDefault, s3EnforceDirectUpload, s3Hosts, useS3Storage) { 
        obj['authMethods'] = authMethods;
        obj['hideLoginInputFields'] = hideLoginInputFields;
        obj['languageDefault'] = languageDefault;
        obj['s3EnforceDirectUpload'] = s3EnforceDirectUpload;
        obj['s3Hosts'] = s3Hosts;
        obj['useS3Storage'] = useS3Storage;
    }

    /**
     * Constructs a <code>SystemInfo</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SystemInfo} obj Optional instance to populate.
     * @return {module:model/SystemInfo} The populated <code>SystemInfo</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SystemInfo();

            if (data.hasOwnProperty('authMethods')) {
                obj['authMethods'] = ApiClient.convertToType(data['authMethods'], [AuthMethod]);
            }
            if (data.hasOwnProperty('hideLoginInputFields')) {
                obj['hideLoginInputFields'] = ApiClient.convertToType(data['hideLoginInputFields'], 'Boolean');
            }
            if (data.hasOwnProperty('languageDefault')) {
                obj['languageDefault'] = ApiClient.convertToType(data['languageDefault'], 'String');
            }
            if (data.hasOwnProperty('s3EnforceDirectUpload')) {
                obj['s3EnforceDirectUpload'] = ApiClient.convertToType(data['s3EnforceDirectUpload'], 'Boolean');
            }
            if (data.hasOwnProperty('s3Hosts')) {
                obj['s3Hosts'] = ApiClient.convertToType(data['s3Hosts'], ['String']);
            }
            if (data.hasOwnProperty('useS3Storage')) {
                obj['useS3Storage'] = ApiClient.convertToType(data['useS3Storage'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>SystemInfo</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>SystemInfo</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of SystemInfo.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        if (data['authMethods']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['authMethods'])) {
                throw new Error("Expected the field `authMethods` to be an array in the JSON data but got " + data['authMethods']);
            }
            // validate the optional field `authMethods` (array)
            for (const item of data['authMethods']) {
                AuthMethod.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['languageDefault'] && !(typeof data['languageDefault'] === 'string' || data['languageDefault'] instanceof String)) {
            throw new Error("Expected the field `languageDefault` to be a primitive type in the JSON string but got " + data['languageDefault']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['s3Hosts'])) {
            throw new Error("Expected the field `s3Hosts` to be an array in the JSON data but got " + data['s3Hosts']);
        }

        return true;
    }


}

SystemInfo.RequiredProperties = ["authMethods", "hideLoginInputFields", "languageDefault", "s3EnforceDirectUpload", "s3Hosts", "useS3Storage"];

/**
 * &#128679; Deprecated since v4.13.0  Authentication methods:  * `sql`  * `active_directory`  * `radius`  * `openid`  use `authData` instead
 * @member {Array.<module:model/AuthMethod>} authMethods
 */
SystemInfo.prototype['authMethods'] = undefined;

/**
 * &#128679; Deprecated since v4.42.0  Defines if login fields should be hidden
 * @member {Boolean} hideLoginInputFields
 */
SystemInfo.prototype['hideLoginInputFields'] = undefined;

/**
 * System default language  cf. [RFC 5646](https://tools.ietf.org/html/rfc5646)
 * @member {String} languageDefault
 */
SystemInfo.prototype['languageDefault'] = undefined;

/**
 * &#128640; Since v4.15.0  Determines whether S3 direct upload is enforced or not
 * @member {Boolean} s3EnforceDirectUpload
 */
SystemInfo.prototype['s3EnforceDirectUpload'] = undefined;

/**
 * &#128640; Since v4.14.0  List of S3 Hosts for CSP header
 * @member {Array.<String>} s3Hosts
 */
SystemInfo.prototype['s3Hosts'] = undefined;

/**
 * &#128640; Since v4.21.0  Defines if S3 is used as storage backend
 * @member {Boolean} useS3Storage
 */
SystemInfo.prototype['useS3Storage'] = undefined;






export default SystemInfo;

