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
import StoreReleasesGetLatest200ResponseInnerDistributionStoresInner from './StoreReleasesGetLatest200ResponseInnerDistributionStoresInner';

/**
 * The StoreReleasesGetLatest200ResponseInner model module.
 * @module model/StoreReleasesGetLatest200ResponseInner
 * @version v0.1
 */
class StoreReleasesGetLatest200ResponseInner {
    /**
     * Constructs a new <code>StoreReleasesGetLatest200ResponseInner</code>.
     * Details of an uploaded release
     * @alias module:model/StoreReleasesGetLatest200ResponseInner
     */
    constructor() { 
        
        StoreReleasesGetLatest200ResponseInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>StoreReleasesGetLatest200ResponseInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/StoreReleasesGetLatest200ResponseInner} obj Optional instance to populate.
     * @return {module:model/StoreReleasesGetLatest200ResponseInner} The populated <code>StoreReleasesGetLatest200ResponseInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new StoreReleasesGetLatest200ResponseInner();

            if (data.hasOwnProperty('android_min_api_level')) {
                obj['android_min_api_level'] = ApiClient.convertToType(data['android_min_api_level'], 'String');
            }
            if (data.hasOwnProperty('app_display_name')) {
                obj['app_display_name'] = ApiClient.convertToType(data['app_display_name'], 'String');
            }
            if (data.hasOwnProperty('app_name')) {
                obj['app_name'] = ApiClient.convertToType(data['app_name'], 'String');
            }
            if (data.hasOwnProperty('bundle_identifier')) {
                obj['bundle_identifier'] = ApiClient.convertToType(data['bundle_identifier'], 'String');
            }
            if (data.hasOwnProperty('distribution_stores')) {
                obj['distribution_stores'] = ApiClient.convertToType(data['distribution_stores'], [StoreReleasesGetLatest200ResponseInnerDistributionStoresInner]);
            }
            if (data.hasOwnProperty('download_url')) {
                obj['download_url'] = ApiClient.convertToType(data['download_url'], 'String');
            }
            if (data.hasOwnProperty('fingerprint')) {
                obj['fingerprint'] = ApiClient.convertToType(data['fingerprint'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('install_url')) {
                obj['install_url'] = ApiClient.convertToType(data['install_url'], 'String');
            }
            if (data.hasOwnProperty('min_os')) {
                obj['min_os'] = ApiClient.convertToType(data['min_os'], 'String');
            }
            if (data.hasOwnProperty('release_notes')) {
                obj['release_notes'] = ApiClient.convertToType(data['release_notes'], 'String');
            }
            if (data.hasOwnProperty('short_version')) {
                obj['short_version'] = ApiClient.convertToType(data['short_version'], 'String');
            }
            if (data.hasOwnProperty('size')) {
                obj['size'] = ApiClient.convertToType(data['size'], 'Number');
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
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
     * Validates the JSON data with respect to <code>StoreReleasesGetLatest200ResponseInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>StoreReleasesGetLatest200ResponseInner</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['android_min_api_level'] && !(typeof data['android_min_api_level'] === 'string' || data['android_min_api_level'] instanceof String)) {
            throw new Error("Expected the field `android_min_api_level` to be a primitive type in the JSON string but got " + data['android_min_api_level']);
        }
        // ensure the json data is a string
        if (data['app_display_name'] && !(typeof data['app_display_name'] === 'string' || data['app_display_name'] instanceof String)) {
            throw new Error("Expected the field `app_display_name` to be a primitive type in the JSON string but got " + data['app_display_name']);
        }
        // ensure the json data is a string
        if (data['app_name'] && !(typeof data['app_name'] === 'string' || data['app_name'] instanceof String)) {
            throw new Error("Expected the field `app_name` to be a primitive type in the JSON string but got " + data['app_name']);
        }
        // ensure the json data is a string
        if (data['bundle_identifier'] && !(typeof data['bundle_identifier'] === 'string' || data['bundle_identifier'] instanceof String)) {
            throw new Error("Expected the field `bundle_identifier` to be a primitive type in the JSON string but got " + data['bundle_identifier']);
        }
        if (data['distribution_stores']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['distribution_stores'])) {
                throw new Error("Expected the field `distribution_stores` to be an array in the JSON data but got " + data['distribution_stores']);
            }
            // validate the optional field `distribution_stores` (array)
            for (const item of data['distribution_stores']) {
                StoreReleasesGetLatest200ResponseInnerDistributionStoresInner.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['download_url'] && !(typeof data['download_url'] === 'string' || data['download_url'] instanceof String)) {
            throw new Error("Expected the field `download_url` to be a primitive type in the JSON string but got " + data['download_url']);
        }
        // ensure the json data is a string
        if (data['fingerprint'] && !(typeof data['fingerprint'] === 'string' || data['fingerprint'] instanceof String)) {
            throw new Error("Expected the field `fingerprint` to be a primitive type in the JSON string but got " + data['fingerprint']);
        }
        // ensure the json data is a string
        if (data['install_url'] && !(typeof data['install_url'] === 'string' || data['install_url'] instanceof String)) {
            throw new Error("Expected the field `install_url` to be a primitive type in the JSON string but got " + data['install_url']);
        }
        // ensure the json data is a string
        if (data['min_os'] && !(typeof data['min_os'] === 'string' || data['min_os'] instanceof String)) {
            throw new Error("Expected the field `min_os` to be a primitive type in the JSON string but got " + data['min_os']);
        }
        // ensure the json data is a string
        if (data['release_notes'] && !(typeof data['release_notes'] === 'string' || data['release_notes'] instanceof String)) {
            throw new Error("Expected the field `release_notes` to be a primitive type in the JSON string but got " + data['release_notes']);
        }
        // ensure the json data is a string
        if (data['short_version'] && !(typeof data['short_version'] === 'string' || data['short_version'] instanceof String)) {
            throw new Error("Expected the field `short_version` to be a primitive type in the JSON string but got " + data['short_version']);
        }
        // ensure the json data is a string
        if (data['status'] && !(typeof data['status'] === 'string' || data['status'] instanceof String)) {
            throw new Error("Expected the field `status` to be a primitive type in the JSON string but got " + data['status']);
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
 * The release's minimum required Android API level.
 * @member {String} android_min_api_level
 */
StoreReleasesGetLatest200ResponseInner.prototype['android_min_api_level'] = undefined;

/**
 * The app's display name.
 * @member {String} app_display_name
 */
StoreReleasesGetLatest200ResponseInner.prototype['app_display_name'] = undefined;

/**
 * The app's name (extracted from the uploaded release).
 * @member {String} app_name
 */
StoreReleasesGetLatest200ResponseInner.prototype['app_name'] = undefined;

/**
 * The identifier of the apps bundle.
 * @member {String} bundle_identifier
 */
StoreReleasesGetLatest200ResponseInner.prototype['bundle_identifier'] = undefined;

/**
 * a list of distribution stores that are associated with this release.
 * @member {Array.<module:model/StoreReleasesGetLatest200ResponseInnerDistributionStoresInner>} distribution_stores
 */
StoreReleasesGetLatest200ResponseInner.prototype['distribution_stores'] = undefined;

/**
 * The URL that hosts the binary for this release.
 * @member {String} download_url
 */
StoreReleasesGetLatest200ResponseInner.prototype['download_url'] = undefined;

/**
 * MD5 checksum of the release binary.
 * @member {String} fingerprint
 */
StoreReleasesGetLatest200ResponseInner.prototype['fingerprint'] = undefined;

/**
 * ID identifying this unique release.
 * @member {Number} id
 */
StoreReleasesGetLatest200ResponseInner.prototype['id'] = undefined;

/**
 * The href required to install a release on a mobile device. On iOS devices will be prefixed with `itms-services://?action=download-manifest&url=`
 * @member {module:model/StoreReleasesGetLatest200ResponseInner.InstallUrlEnum} install_url
 */
StoreReleasesGetLatest200ResponseInner.prototype['install_url'] = undefined;

/**
 * The release's minimum required operating system.
 * @member {String} min_os
 */
StoreReleasesGetLatest200ResponseInner.prototype['min_os'] = undefined;

/**
 * The release's release notes.
 * @member {String} release_notes
 */
StoreReleasesGetLatest200ResponseInner.prototype['release_notes'] = undefined;

/**
 * The release's short version.<br> For iOS: CFBundleShortVersionString from info.plist. For Android: android:versionName from AppManifest.xml. 
 * @member {String} short_version
 */
StoreReleasesGetLatest200ResponseInner.prototype['short_version'] = undefined;

/**
 * The release's size in bytes.
 * @member {Number} size
 */
StoreReleasesGetLatest200ResponseInner.prototype['size'] = undefined;

/**
 * OBSOLETE. Will be removed in next version. The availability concept is now replaced with distributed. Any 'available' release will be associated with the default distribution group of an app.</br> The release state.<br> <b>available</b>: The uploaded release has been distributed.<br> <b>unavailable</b>: The uploaded release is not visible to the user. <br> 
 * @member {module:model/StoreReleasesGetLatest200ResponseInner.StatusEnum} status
 */
StoreReleasesGetLatest200ResponseInner.prototype['status'] = undefined;

/**
 * UTC time in ISO 8601 format of the uploaded time.
 * @member {String} uploaded_at
 */
StoreReleasesGetLatest200ResponseInner.prototype['uploaded_at'] = undefined;

/**
 * The release's version.<br> For iOS: CFBundleVersion from info.plist. For Android: android:versionCode from AppManifest.xml. 
 * @member {String} version
 */
StoreReleasesGetLatest200ResponseInner.prototype['version'] = undefined;





/**
 * Allowed values for the <code>install_url</code> property.
 * @enum {String}
 * @readonly
 */
StoreReleasesGetLatest200ResponseInner['InstallUrlEnum'] = {

    /**
     * value: "group"
     * @const
     */
    "group": "group",

    /**
     * value: "store"
     * @const
     */
    "store": "store"
};


/**
 * Allowed values for the <code>status</code> property.
 * @enum {String}
 * @readonly
 */
StoreReleasesGetLatest200ResponseInner['StatusEnum'] = {

    /**
     * value: "available"
     * @const
     */
    "available": "available",

    /**
     * value: "unavailable"
     * @const
     */
    "unavailable": "unavailable"
};



export default StoreReleasesGetLatest200ResponseInner;

