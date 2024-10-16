/**
 * AGCO API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The UpdateSystemModelsPriorityPackage model module.
 * @module model/UpdateSystemModelsPriorityPackage
 * @version v1
 */
class UpdateSystemModelsPriorityPackage {
    /**
     * Constructs a new <code>UpdateSystemModelsPriorityPackage</code>.
     * @alias module:model/UpdateSystemModelsPriorityPackage
     * @param clientID {String} The ID of the client to receive the priority package
     * @param packageID {String} The ID of the package to push as a priority package.
     */
    constructor(clientID, packageID) { 
        
        UpdateSystemModelsPriorityPackage.initialize(this, clientID, packageID);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, clientID, packageID) { 
        obj['ClientID'] = clientID;
        obj['PackageID'] = packageID;
    }

    /**
     * Constructs a <code>UpdateSystemModelsPriorityPackage</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UpdateSystemModelsPriorityPackage} obj Optional instance to populate.
     * @return {module:model/UpdateSystemModelsPriorityPackage} The populated <code>UpdateSystemModelsPriorityPackage</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UpdateSystemModelsPriorityPackage();

            if (data.hasOwnProperty('Autorun')) {
                obj['Autorun'] = ApiClient.convertToType(data['Autorun'], 'Boolean');
            }
            if (data.hasOwnProperty('CRC')) {
                obj['CRC'] = ApiClient.convertToType(data['CRC'], 'String');
            }
            if (data.hasOwnProperty('ClientID')) {
                obj['ClientID'] = ApiClient.convertToType(data['ClientID'], 'String');
            }
            if (data.hasOwnProperty('Description')) {
                obj['Description'] = ApiClient.convertToType(data['Description'], 'String');
            }
            if (data.hasOwnProperty('Notes')) {
                obj['Notes'] = ApiClient.convertToType(data['Notes'], 'String');
            }
            if (data.hasOwnProperty('PackageID')) {
                obj['PackageID'] = ApiClient.convertToType(data['PackageID'], 'String');
            }
            if (data.hasOwnProperty('PackageTypeID')) {
                obj['PackageTypeID'] = ApiClient.convertToType(data['PackageTypeID'], 'String');
            }
            if (data.hasOwnProperty('PreviousVersion')) {
                obj['PreviousVersion'] = ApiClient.convertToType(data['PreviousVersion'], 'Number');
            }
            if (data.hasOwnProperty('PriorityPackageID')) {
                obj['PriorityPackageID'] = ApiClient.convertToType(data['PriorityPackageID'], 'String');
            }
            if (data.hasOwnProperty('ReleaseDate')) {
                obj['ReleaseDate'] = ApiClient.convertToType(data['ReleaseDate'], 'Date');
            }
            if (data.hasOwnProperty('Released')) {
                obj['Released'] = ApiClient.convertToType(data['Released'], 'Boolean');
            }
            if (data.hasOwnProperty('RemoveOnSuccess')) {
                obj['RemoveOnSuccess'] = ApiClient.convertToType(data['RemoveOnSuccess'], 'Boolean');
            }
            if (data.hasOwnProperty('Size')) {
                obj['Size'] = ApiClient.convertToType(data['Size'], 'Number');
            }
            if (data.hasOwnProperty('Switches')) {
                obj['Switches'] = ApiClient.convertToType(data['Switches'], 'String');
            }
            if (data.hasOwnProperty('TimeStamp')) {
                obj['TimeStamp'] = ApiClient.convertToType(data['TimeStamp'], 'Date');
            }
            if (data.hasOwnProperty('Url')) {
                obj['Url'] = ApiClient.convertToType(data['Url'], 'String');
            }
            if (data.hasOwnProperty('Version')) {
                obj['Version'] = ApiClient.convertToType(data['Version'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UpdateSystemModelsPriorityPackage</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UpdateSystemModelsPriorityPackage</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of UpdateSystemModelsPriorityPackage.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['CRC'] && !(typeof data['CRC'] === 'string' || data['CRC'] instanceof String)) {
            throw new Error("Expected the field `CRC` to be a primitive type in the JSON string but got " + data['CRC']);
        }
        // ensure the json data is a string
        if (data['ClientID'] && !(typeof data['ClientID'] === 'string' || data['ClientID'] instanceof String)) {
            throw new Error("Expected the field `ClientID` to be a primitive type in the JSON string but got " + data['ClientID']);
        }
        // ensure the json data is a string
        if (data['Description'] && !(typeof data['Description'] === 'string' || data['Description'] instanceof String)) {
            throw new Error("Expected the field `Description` to be a primitive type in the JSON string but got " + data['Description']);
        }
        // ensure the json data is a string
        if (data['Notes'] && !(typeof data['Notes'] === 'string' || data['Notes'] instanceof String)) {
            throw new Error("Expected the field `Notes` to be a primitive type in the JSON string but got " + data['Notes']);
        }
        // ensure the json data is a string
        if (data['PackageID'] && !(typeof data['PackageID'] === 'string' || data['PackageID'] instanceof String)) {
            throw new Error("Expected the field `PackageID` to be a primitive type in the JSON string but got " + data['PackageID']);
        }
        // ensure the json data is a string
        if (data['PackageTypeID'] && !(typeof data['PackageTypeID'] === 'string' || data['PackageTypeID'] instanceof String)) {
            throw new Error("Expected the field `PackageTypeID` to be a primitive type in the JSON string but got " + data['PackageTypeID']);
        }
        // ensure the json data is a string
        if (data['PriorityPackageID'] && !(typeof data['PriorityPackageID'] === 'string' || data['PriorityPackageID'] instanceof String)) {
            throw new Error("Expected the field `PriorityPackageID` to be a primitive type in the JSON string but got " + data['PriorityPackageID']);
        }
        // ensure the json data is a string
        if (data['Switches'] && !(typeof data['Switches'] === 'string' || data['Switches'] instanceof String)) {
            throw new Error("Expected the field `Switches` to be a primitive type in the JSON string but got " + data['Switches']);
        }
        // ensure the json data is a string
        if (data['Url'] && !(typeof data['Url'] === 'string' || data['Url'] instanceof String)) {
            throw new Error("Expected the field `Url` to be a primitive type in the JSON string but got " + data['Url']);
        }

        return true;
    }


}

UpdateSystemModelsPriorityPackage.RequiredProperties = ["ClientID", "PackageID"];

/**
 * Read Only. From the package specified by package ID.              Value is true if package should run automatically. Default value is false.
 * @member {Boolean} Autorun
 */
UpdateSystemModelsPriorityPackage.prototype['Autorun'] = undefined;

/**
 * Read Only. From the package specified by package ID.
 * @member {String} CRC
 */
UpdateSystemModelsPriorityPackage.prototype['CRC'] = undefined;

/**
 * The ID of the client to receive the priority package
 * @member {String} ClientID
 */
UpdateSystemModelsPriorityPackage.prototype['ClientID'] = undefined;

/**
 * Read Only. From the package specified by package ID.
 * @member {String} Description
 */
UpdateSystemModelsPriorityPackage.prototype['Description'] = undefined;

/**
 * Read Only. From the package specified by package ID.
 * @member {String} Notes
 */
UpdateSystemModelsPriorityPackage.prototype['Notes'] = undefined;

/**
 * The ID of the package to push as a priority package.
 * @member {String} PackageID
 */
UpdateSystemModelsPriorityPackage.prototype['PackageID'] = undefined;

/**
 * Read Only. From the package specified by package ID.
 * @member {String} PackageTypeID
 */
UpdateSystemModelsPriorityPackage.prototype['PackageTypeID'] = undefined;

/**
 * Read Only. From the package specified by package ID.
 * @member {Number} PreviousVersion
 */
UpdateSystemModelsPriorityPackage.prototype['PreviousVersion'] = undefined;

/**
 * Read Only. The ID of the priority package.
 * @member {String} PriorityPackageID
 */
UpdateSystemModelsPriorityPackage.prototype['PriorityPackageID'] = undefined;

/**
 * Read Only. From the package specified by package ID.              The date the package was released
 * @member {Date} ReleaseDate
 */
UpdateSystemModelsPriorityPackage.prototype['ReleaseDate'] = undefined;

/**
 * Read Only. From the package specified by package ID.
 * @member {Boolean} Released
 */
UpdateSystemModelsPriorityPackage.prototype['Released'] = undefined;

/**
 * Read Only. From the package specified by package ID.
 * @member {Boolean} RemoveOnSuccess
 */
UpdateSystemModelsPriorityPackage.prototype['RemoveOnSuccess'] = undefined;

/**
 * Read Only. From the package specified by package ID.
 * @member {Number} Size
 */
UpdateSystemModelsPriorityPackage.prototype['Size'] = undefined;

/**
 * The command line arguments for the priority package.  Default value is an empty string.
 * @member {String} Switches
 */
UpdateSystemModelsPriorityPackage.prototype['Switches'] = undefined;

/**
 * Read Only. The timestamp of the priority package.
 * @member {Date} TimeStamp
 */
UpdateSystemModelsPriorityPackage.prototype['TimeStamp'] = undefined;

/**
 * Read Only. From the package specified by package ID.
 * @member {String} Url
 */
UpdateSystemModelsPriorityPackage.prototype['Url'] = undefined;

/**
 * Read Only. From the package specified by package ID.
 * @member {Number} Version
 */
UpdateSystemModelsPriorityPackage.prototype['Version'] = undefined;






export default UpdateSystemModelsPriorityPackage;

