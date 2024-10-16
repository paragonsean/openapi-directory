/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The ManagementReleaseDetailsResponse model module.
 * @module model/ManagementReleaseDetailsResponse
 * @version v0.1
 */
class ManagementReleaseDetailsResponse {
    /**
     * Constructs a new <code>ManagementReleaseDetailsResponse</code>.
     * Details of an uploaded release
     * @alias module:model/ManagementReleaseDetailsResponse
     */
    constructor() { 
        
        ManagementReleaseDetailsResponse.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ManagementReleaseDetailsResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ManagementReleaseDetailsResponse} obj Optional instance to populate.
     * @return {module:model/ManagementReleaseDetailsResponse} The populated <code>ManagementReleaseDetailsResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ManagementReleaseDetailsResponse();

            if (data.hasOwnProperty('buildVersion')) {
                obj['buildVersion'] = ApiClient.convertToType(data['buildVersion'], 'String');
            }
            if (data.hasOwnProperty('createdAt')) {
                obj['createdAt'] = ApiClient.convertToType(data['createdAt'], 'String');
            }
            if (data.hasOwnProperty('deletedAt')) {
                obj['deletedAt'] = ApiClient.convertToType(data['deletedAt'], 'String');
            }
            if (data.hasOwnProperty('distinctId')) {
                obj['distinctId'] = ApiClient.convertToType(data['distinctId'], 'Number');
            }
            if (data.hasOwnProperty('enabled')) {
                obj['enabled'] = ApiClient.convertToType(data['enabled'], 'Boolean');
            }
            if (data.hasOwnProperty('origin')) {
                obj['origin'] = ApiClient.convertToType(data['origin'], 'String');
            }
            if (data.hasOwnProperty('sortVersion')) {
                obj['sortVersion'] = ApiClient.convertToType(data['sortVersion'], 'String');
            }
            if (data.hasOwnProperty('version')) {
                obj['version'] = ApiClient.convertToType(data['version'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ManagementReleaseDetailsResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ManagementReleaseDetailsResponse</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['buildVersion'] && !(typeof data['buildVersion'] === 'string' || data['buildVersion'] instanceof String)) {
            throw new Error("Expected the field `buildVersion` to be a primitive type in the JSON string but got " + data['buildVersion']);
        }
        // ensure the json data is a string
        if (data['createdAt'] && !(typeof data['createdAt'] === 'string' || data['createdAt'] instanceof String)) {
            throw new Error("Expected the field `createdAt` to be a primitive type in the JSON string but got " + data['createdAt']);
        }
        // ensure the json data is a string
        if (data['deletedAt'] && !(typeof data['deletedAt'] === 'string' || data['deletedAt'] instanceof String)) {
            throw new Error("Expected the field `deletedAt` to be a primitive type in the JSON string but got " + data['deletedAt']);
        }
        // ensure the json data is a string
        if (data['origin'] && !(typeof data['origin'] === 'string' || data['origin'] instanceof String)) {
            throw new Error("Expected the field `origin` to be a primitive type in the JSON string but got " + data['origin']);
        }
        // ensure the json data is a string
        if (data['sortVersion'] && !(typeof data['sortVersion'] === 'string' || data['sortVersion'] instanceof String)) {
            throw new Error("Expected the field `sortVersion` to be a primitive type in the JSON string but got " + data['sortVersion']);
        }
        // ensure the json data is a string
        if (data['version'] && !(typeof data['version'] === 'string' || data['version'] instanceof String)) {
            throw new Error("Expected the field `version` to be a primitive type in the JSON string but got " + data['version']);
        }

        return true;
    }


}



/**
 * The release's buildVersion.<br> For iOS: CFBundleVersion from info.plist.<br> For Android: android:versionCode from AppManifest.xml. 
 * @member {String} buildVersion
 */
ManagementReleaseDetailsResponse.prototype['buildVersion'] = undefined;

/**
 * UTC time the release was created in ISO 8601 format.
 * @member {String} createdAt
 */
ManagementReleaseDetailsResponse.prototype['createdAt'] = undefined;

/**
 * UTC time the release was created in ISO 8601 format.
 * @member {String} deletedAt
 */
ManagementReleaseDetailsResponse.prototype['deletedAt'] = undefined;

/**
 * ID identifying this unique release.
 * @member {Number} distinctId
 */
ManagementReleaseDetailsResponse.prototype['distinctId'] = undefined;

/**
 * This value determines the whether a release currently is enabled or disabled.
 * @member {Boolean} enabled
 */
ManagementReleaseDetailsResponse.prototype['enabled'] = undefined;

/**
 * The release's origin
 * @member {module:model/ManagementReleaseDetailsResponse.OriginEnum} origin
 */
ManagementReleaseDetailsResponse.prototype['origin'] = undefined;

/**
 * The release's sortVersion.
 * @member {String} sortVersion
 */
ManagementReleaseDetailsResponse.prototype['sortVersion'] = undefined;

/**
 * The release's short version.<br> For iOS: CFBundleShortVersionString from info.plist.<br> For Android: android:versionName from AppManifest.xml. 
 * @member {String} version
 */
ManagementReleaseDetailsResponse.prototype['version'] = undefined;





/**
 * Allowed values for the <code>origin</code> property.
 * @enum {String}
 * @readonly
 */
ManagementReleaseDetailsResponse['OriginEnum'] = {

    /**
     * value: "hockeyapp"
     * @const
     */
    "hockeyapp": "hockeyapp",

    /**
     * value: "appcenter"
     * @const
     */
    "appcenter": "appcenter"
};



export default ManagementReleaseDetailsResponse;

