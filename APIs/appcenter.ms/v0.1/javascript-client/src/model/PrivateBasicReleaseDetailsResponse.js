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
 * The PrivateBasicReleaseDetailsResponse model module.
 * @module model/PrivateBasicReleaseDetailsResponse
 * @version v0.1
 */
class PrivateBasicReleaseDetailsResponse {
    /**
     * Constructs a new <code>PrivateBasicReleaseDetailsResponse</code>.
     * Basic information on a release for private apis
     * @alias module:model/PrivateBasicReleaseDetailsResponse
     */
    constructor() { 
        
        PrivateBasicReleaseDetailsResponse.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PrivateBasicReleaseDetailsResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PrivateBasicReleaseDetailsResponse} obj Optional instance to populate.
     * @return {module:model/PrivateBasicReleaseDetailsResponse} The populated <code>PrivateBasicReleaseDetailsResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PrivateBasicReleaseDetailsResponse();

            if (data.hasOwnProperty('destination_type')) {
                obj['destination_type'] = ApiClient.convertToType(data['destination_type'], 'String');
            }
            if (data.hasOwnProperty('distribution_group_id')) {
                obj['distribution_group_id'] = ApiClient.convertToType(data['distribution_group_id'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('is_external_build')) {
                obj['is_external_build'] = ApiClient.convertToType(data['is_external_build'], 'Boolean');
            }
            if (data.hasOwnProperty('is_latest')) {
                obj['is_latest'] = ApiClient.convertToType(data['is_latest'], 'Boolean');
            }
            if (data.hasOwnProperty('mandatory_update')) {
                obj['mandatory_update'] = ApiClient.convertToType(data['mandatory_update'], 'Boolean');
            }
            if (data.hasOwnProperty('origin')) {
                obj['origin'] = ApiClient.convertToType(data['origin'], 'String');
            }
            if (data.hasOwnProperty('publishing_status')) {
                obj['publishing_status'] = ApiClient.convertToType(data['publishing_status'], 'String');
            }
            if (data.hasOwnProperty('short_version')) {
                obj['short_version'] = ApiClient.convertToType(data['short_version'], 'String');
            }
            if (data.hasOwnProperty('uploaded_at')) {
                obj['uploaded_at'] = ApiClient.convertToType(data['uploaded_at'], 'String');
            }
            if (data.hasOwnProperty('version')) {
                obj['version'] = ApiClient.convertToType(data['version'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PrivateBasicReleaseDetailsResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PrivateBasicReleaseDetailsResponse</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['destination_type'] && !(typeof data['destination_type'] === 'string' || data['destination_type'] instanceof String)) {
            throw new Error("Expected the field `destination_type` to be a primitive type in the JSON string but got " + data['destination_type']);
        }
        // ensure the json data is a string
        if (data['distribution_group_id'] && !(typeof data['distribution_group_id'] === 'string' || data['distribution_group_id'] instanceof String)) {
            throw new Error("Expected the field `distribution_group_id` to be a primitive type in the JSON string but got " + data['distribution_group_id']);
        }
        // ensure the json data is a string
        if (data['origin'] && !(typeof data['origin'] === 'string' || data['origin'] instanceof String)) {
            throw new Error("Expected the field `origin` to be a primitive type in the JSON string but got " + data['origin']);
        }
        // ensure the json data is a string
        if (data['publishing_status'] && !(typeof data['publishing_status'] === 'string' || data['publishing_status'] instanceof String)) {
            throw new Error("Expected the field `publishing_status` to be a primitive type in the JSON string but got " + data['publishing_status']);
        }
        // ensure the json data is a string
        if (data['short_version'] && !(typeof data['short_version'] === 'string' || data['short_version'] instanceof String)) {
            throw new Error("Expected the field `short_version` to be a primitive type in the JSON string but got " + data['short_version']);
        }
        // ensure the json data is a string
        if (data['uploaded_at'] && !(typeof data['uploaded_at'] === 'string' || data['uploaded_at'] instanceof String)) {
            throw new Error("Expected the field `uploaded_at` to be a primitive type in the JSON string but got " + data['uploaded_at']);
        }
        // ensure the json data is a string
        if (data['version'] && !(typeof data['version'] === 'string' || data['version'] instanceof String)) {
            throw new Error("Expected the field `version` to be a primitive type in the JSON string but got " + data['version']);
        }

        return true;
    }


}



/**
 * The destination type.<br> <b>group</b>: The release distributed to internal groups and distribution_groups details will be returned.<br> <b>store</b>: The release distributed to external stores and distribution_stores details will be returned. <br> 
 * @member {module:model/PrivateBasicReleaseDetailsResponse.DestinationTypeEnum} destination_type
 */
PrivateBasicReleaseDetailsResponse.prototype['destination_type'] = undefined;

/**
 * the destination id of release where it is distributed.
 * @member {String} distribution_group_id
 */
PrivateBasicReleaseDetailsResponse.prototype['distribution_group_id'] = undefined;

/**
 * ID identifying this unique release.
 * @member {Number} id
 */
PrivateBasicReleaseDetailsResponse.prototype['id'] = undefined;

/**
 * This value determines if a release is external or not.
 * @member {Boolean} is_external_build
 */
PrivateBasicReleaseDetailsResponse.prototype['is_external_build'] = undefined;

/**
 * Indicates if this is the latest release in the group.
 * @member {Boolean} is_latest
 */
PrivateBasicReleaseDetailsResponse.prototype['is_latest'] = undefined;

/**
 * A boolean which determines whether the release is a mandatory update or not.
 * @member {Boolean} mandatory_update
 */
PrivateBasicReleaseDetailsResponse.prototype['mandatory_update'] = undefined;

/**
 * The release's origin
 * @member {module:model/PrivateBasicReleaseDetailsResponse.OriginEnum} origin
 */
PrivateBasicReleaseDetailsResponse.prototype['origin'] = undefined;

/**
 * the publishing status of the distributed release
 * @member {String} publishing_status
 */
PrivateBasicReleaseDetailsResponse.prototype['publishing_status'] = undefined;

/**
 * The release's short version.<br> For iOS: CFBundleShortVersionString from info.plist.<br> For Android: android:versionName from AppManifest.xml. 
 * @member {String} short_version
 */
PrivateBasicReleaseDetailsResponse.prototype['short_version'] = undefined;

/**
 * UTC time in ISO 8601 format of the uploaded time.
 * @member {String} uploaded_at
 */
PrivateBasicReleaseDetailsResponse.prototype['uploaded_at'] = undefined;

/**
 * The release's version.<br> For iOS: CFBundleVersion from info.plist.<br> For Android: android:versionCode from AppManifest.xml. 
 * @member {String} version
 */
PrivateBasicReleaseDetailsResponse.prototype['version'] = undefined;





/**
 * Allowed values for the <code>destination_type</code> property.
 * @enum {String}
 * @readonly
 */
PrivateBasicReleaseDetailsResponse['DestinationTypeEnum'] = {

    /**
     * value: "group"
     * @const
     */
    "group": "group",

    /**
     * value: "store"
     * @const
     */
    "store": "store",

    /**
     * value: "tester"
     * @const
     */
    "tester": "tester"
};


/**
 * Allowed values for the <code>origin</code> property.
 * @enum {String}
 * @readonly
 */
PrivateBasicReleaseDetailsResponse['OriginEnum'] = {

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



export default PrivateBasicReleaseDetailsResponse;

