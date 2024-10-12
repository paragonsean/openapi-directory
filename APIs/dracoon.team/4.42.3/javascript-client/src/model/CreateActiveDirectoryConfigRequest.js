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
 * The CreateActiveDirectoryConfigRequest model module.
 * @module model/CreateActiveDirectoryConfigRequest
 * @version 4.42.3
 */
class CreateActiveDirectoryConfigRequest {
    /**
     * Constructs a new <code>CreateActiveDirectoryConfigRequest</code>.
     * Request model for creating an Active Directory configuration
     * @alias module:model/CreateActiveDirectoryConfigRequest
     * @param alias {String} Unique name for an Active Directory configuration
     * @param ldapUsersDomain {String} Search scope of Active Directory; only users below this node can log on.
     * @param serverAdminName {String} Distinguished Name (DN) of Active Directory administrative account
     * @param serverAdminPassword {String} Password of Active Directory administrative account
     * @param serverIp {String} IPv4 or IPv6 address or host name
     * @param serverPort {Number} Port
     * @param userFilter {String} Name of Active Directory attribute that is used as login name.
     */
    constructor(alias, ldapUsersDomain, serverAdminName, serverAdminPassword, serverIp, serverPort, userFilter) { 
        
        CreateActiveDirectoryConfigRequest.initialize(this, alias, ldapUsersDomain, serverAdminName, serverAdminPassword, serverIp, serverPort, userFilter);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, alias, ldapUsersDomain, serverAdminName, serverAdminPassword, serverIp, serverPort, userFilter) { 
        obj['alias'] = alias;
        obj['createHomeFolder'] = false;
        obj['ldapUsersDomain'] = ldapUsersDomain;
        obj['serverAdminName'] = serverAdminName;
        obj['serverAdminPassword'] = serverAdminPassword;
        obj['serverIp'] = serverIp;
        obj['serverPort'] = serverPort;
        obj['useLdaps'] = false;
        obj['userFilter'] = userFilter;
        obj['userImport'] = false;
    }

    /**
     * Constructs a <code>CreateActiveDirectoryConfigRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CreateActiveDirectoryConfigRequest} obj Optional instance to populate.
     * @return {module:model/CreateActiveDirectoryConfigRequest} The populated <code>CreateActiveDirectoryConfigRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CreateActiveDirectoryConfigRequest();

            if (data.hasOwnProperty('adExportGroup')) {
                obj['adExportGroup'] = ApiClient.convertToType(data['adExportGroup'], 'String');
            }
            if (data.hasOwnProperty('alias')) {
                obj['alias'] = ApiClient.convertToType(data['alias'], 'String');
            }
            if (data.hasOwnProperty('createHomeFolder')) {
                obj['createHomeFolder'] = ApiClient.convertToType(data['createHomeFolder'], 'Boolean');
            }
            if (data.hasOwnProperty('homeFolderParent')) {
                obj['homeFolderParent'] = ApiClient.convertToType(data['homeFolderParent'], 'Number');
            }
            if (data.hasOwnProperty('ldapUsersDomain')) {
                obj['ldapUsersDomain'] = ApiClient.convertToType(data['ldapUsersDomain'], 'String');
            }
            if (data.hasOwnProperty('sdsImportGroup')) {
                obj['sdsImportGroup'] = ApiClient.convertToType(data['sdsImportGroup'], 'Number');
            }
            if (data.hasOwnProperty('serverAdminName')) {
                obj['serverAdminName'] = ApiClient.convertToType(data['serverAdminName'], 'String');
            }
            if (data.hasOwnProperty('serverAdminPassword')) {
                obj['serverAdminPassword'] = ApiClient.convertToType(data['serverAdminPassword'], 'String');
            }
            if (data.hasOwnProperty('serverIp')) {
                obj['serverIp'] = ApiClient.convertToType(data['serverIp'], 'String');
            }
            if (data.hasOwnProperty('serverPort')) {
                obj['serverPort'] = ApiClient.convertToType(data['serverPort'], 'Number');
            }
            if (data.hasOwnProperty('sslFingerPrint')) {
                obj['sslFingerPrint'] = ApiClient.convertToType(data['sslFingerPrint'], 'String');
            }
            if (data.hasOwnProperty('useLdaps')) {
                obj['useLdaps'] = ApiClient.convertToType(data['useLdaps'], 'Boolean');
            }
            if (data.hasOwnProperty('userFilter')) {
                obj['userFilter'] = ApiClient.convertToType(data['userFilter'], 'String');
            }
            if (data.hasOwnProperty('userImport')) {
                obj['userImport'] = ApiClient.convertToType(data['userImport'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CreateActiveDirectoryConfigRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CreateActiveDirectoryConfigRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of CreateActiveDirectoryConfigRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['adExportGroup'] && !(typeof data['adExportGroup'] === 'string' || data['adExportGroup'] instanceof String)) {
            throw new Error("Expected the field `adExportGroup` to be a primitive type in the JSON string but got " + data['adExportGroup']);
        }
        // ensure the json data is a string
        if (data['alias'] && !(typeof data['alias'] === 'string' || data['alias'] instanceof String)) {
            throw new Error("Expected the field `alias` to be a primitive type in the JSON string but got " + data['alias']);
        }
        // ensure the json data is a string
        if (data['ldapUsersDomain'] && !(typeof data['ldapUsersDomain'] === 'string' || data['ldapUsersDomain'] instanceof String)) {
            throw new Error("Expected the field `ldapUsersDomain` to be a primitive type in the JSON string but got " + data['ldapUsersDomain']);
        }
        // ensure the json data is a string
        if (data['serverAdminName'] && !(typeof data['serverAdminName'] === 'string' || data['serverAdminName'] instanceof String)) {
            throw new Error("Expected the field `serverAdminName` to be a primitive type in the JSON string but got " + data['serverAdminName']);
        }
        // ensure the json data is a string
        if (data['serverAdminPassword'] && !(typeof data['serverAdminPassword'] === 'string' || data['serverAdminPassword'] instanceof String)) {
            throw new Error("Expected the field `serverAdminPassword` to be a primitive type in the JSON string but got " + data['serverAdminPassword']);
        }
        // ensure the json data is a string
        if (data['serverIp'] && !(typeof data['serverIp'] === 'string' || data['serverIp'] instanceof String)) {
            throw new Error("Expected the field `serverIp` to be a primitive type in the JSON string but got " + data['serverIp']);
        }
        // ensure the json data is a string
        if (data['sslFingerPrint'] && !(typeof data['sslFingerPrint'] === 'string' || data['sslFingerPrint'] instanceof String)) {
            throw new Error("Expected the field `sslFingerPrint` to be a primitive type in the JSON string but got " + data['sslFingerPrint']);
        }
        // ensure the json data is a string
        if (data['userFilter'] && !(typeof data['userFilter'] === 'string' || data['userFilter'] instanceof String)) {
            throw new Error("Expected the field `userFilter` to be a primitive type in the JSON string but got " + data['userFilter']);
        }

        return true;
    }


}

CreateActiveDirectoryConfigRequest.RequiredProperties = ["alias", "ldapUsersDomain", "serverAdminName", "serverAdminPassword", "serverIp", "serverPort", "userFilter"];

/**
 * If `userImport` is set to `true`,  the user must be member of this Active Directory group to receive a newly created DRACOON account.
 * @member {String} adExportGroup
 */
CreateActiveDirectoryConfigRequest.prototype['adExportGroup'] = undefined;

/**
 * Unique name for an Active Directory configuration
 * @member {String} alias
 */
CreateActiveDirectoryConfigRequest.prototype['alias'] = undefined;

/**
 * DEPRECATED, will be ignored  Determines whether a room is created for each user that is created by automatic import (like a home folder).  Room's name will equal the user's login name.
 * @member {Boolean} createHomeFolder
 * @default false
 */
CreateActiveDirectoryConfigRequest.prototype['createHomeFolder'] = false;

/**
 * DEPRECATED, will be ignored  ID of the room in which the individual rooms for users will be created.
 * @member {Number} homeFolderParent
 */
CreateActiveDirectoryConfigRequest.prototype['homeFolderParent'] = undefined;

/**
 * Search scope of Active Directory; only users below this node can log on.
 * @member {String} ldapUsersDomain
 */
CreateActiveDirectoryConfigRequest.prototype['ldapUsersDomain'] = undefined;

/**
 * User group that is assigned to users who are created by automatic import.  Reset with `0`
 * @member {Number} sdsImportGroup
 */
CreateActiveDirectoryConfigRequest.prototype['sdsImportGroup'] = undefined;

/**
 * Distinguished Name (DN) of Active Directory administrative account
 * @member {String} serverAdminName
 */
CreateActiveDirectoryConfigRequest.prototype['serverAdminName'] = undefined;

/**
 * Password of Active Directory administrative account
 * @member {String} serverAdminPassword
 */
CreateActiveDirectoryConfigRequest.prototype['serverAdminPassword'] = undefined;

/**
 * IPv4 or IPv6 address or host name
 * @member {String} serverIp
 */
CreateActiveDirectoryConfigRequest.prototype['serverIp'] = undefined;

/**
 * Port
 * @member {Number} serverPort
 */
CreateActiveDirectoryConfigRequest.prototype['serverPort'] = undefined;

/**
 * SSL finger print of Active Directory server.  Mandatory for LDAPS connections.  Format: `Algorithm/Fingerprint`
 * @member {String} sslFingerPrint
 */
CreateActiveDirectoryConfigRequest.prototype['sslFingerPrint'] = undefined;

/**
 * Determines whether LDAPS should be used instead of plain LDAP.
 * @member {Boolean} useLdaps
 * @default false
 */
CreateActiveDirectoryConfigRequest.prototype['useLdaps'] = false;

/**
 * Name of Active Directory attribute that is used as login name.
 * @member {String} userFilter
 */
CreateActiveDirectoryConfigRequest.prototype['userFilter'] = undefined;

/**
 * Determines if a DRACOON account is automatically created for a new user  who successfully logs on with his / her AD / IDP account.
 * @member {Boolean} userImport
 * @default false
 */
CreateActiveDirectoryConfigRequest.prototype['userImport'] = false;






export default CreateActiveDirectoryConfigRequest;

