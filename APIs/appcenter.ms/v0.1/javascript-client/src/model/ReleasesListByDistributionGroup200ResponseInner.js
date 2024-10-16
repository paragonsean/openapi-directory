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
 * The ReleasesListByDistributionGroup200ResponseInner model module.
 * @module model/ReleasesListByDistributionGroup200ResponseInner
 * @version v0.1
 */
class ReleasesListByDistributionGroup200ResponseInner {
    /**
     * Constructs a new <code>ReleasesListByDistributionGroup200ResponseInner</code>.
     * Response for getting a list of releases in a distribution group
     * @alias module:model/ReleasesListByDistributionGroup200ResponseInner
     * @param enabled {Boolean} This value determines the whether a release currently is enabled or disabled.
     * @param id {Number} ID identifying this unique release.
     * @param mandatoryUpdate {Boolean} A boolean which determines whether the release is a mandatory update or not.
     * @param shortVersion {String} The release's short version.<br> For iOS: CFBundleShortVersionString from info.plist.<br> For Android: android:versionName from AppManifest.xml. 
     * @param uploadedAt {String} UTC time in ISO 8601 format of the uploaded time.
     * @param version {String} The release's version.<br> For iOS: CFBundleVersion from info.plist.<br> For Android: android:versionCode from AppManifest.xml. 
     */
    constructor(enabled, id, mandatoryUpdate, shortVersion, uploadedAt, version) { 
        
        ReleasesListByDistributionGroup200ResponseInner.initialize(this, enabled, id, mandatoryUpdate, shortVersion, uploadedAt, version);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, enabled, id, mandatoryUpdate, shortVersion, uploadedAt, version) { 
        obj['enabled'] = enabled;
        obj['id'] = id;
        obj['mandatory_update'] = mandatoryUpdate;
        obj['short_version'] = shortVersion;
        obj['uploaded_at'] = uploadedAt;
        obj['version'] = version;
    }

    /**
     * Constructs a <code>ReleasesListByDistributionGroup200ResponseInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ReleasesListByDistributionGroup200ResponseInner} obj Optional instance to populate.
     * @return {module:model/ReleasesListByDistributionGroup200ResponseInner} The populated <code>ReleasesListByDistributionGroup200ResponseInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ReleasesListByDistributionGroup200ResponseInner();

            if (data.hasOwnProperty('enabled')) {
                obj['enabled'] = ApiClient.convertToType(data['enabled'], 'Boolean');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('is_external_build')) {
                obj['is_external_build'] = ApiClient.convertToType(data['is_external_build'], 'Boolean');
            }
            if (data.hasOwnProperty('mandatory_update')) {
                obj['mandatory_update'] = ApiClient.convertToType(data['mandatory_update'], 'Boolean');
            }
            if (data.hasOwnProperty('origin')) {
                obj['origin'] = ApiClient.convertToType(data['origin'], 'String');
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
     * Validates the JSON data with respect to <code>ReleasesListByDistributionGroup200ResponseInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ReleasesListByDistributionGroup200ResponseInner</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of ReleasesListByDistributionGroup200ResponseInner.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['origin'] && !(typeof data['origin'] === 'string' || data['origin'] instanceof String)) {
            throw new Error("Expected the field `origin` to be a primitive type in the JSON string but got " + data['origin']);
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

ReleasesListByDistributionGroup200ResponseInner.RequiredProperties = ["enabled", "id", "mandatory_update", "short_version", "uploaded_at", "version"];

/**
 * This value determines the whether a release currently is enabled or disabled.
 * @member {Boolean} enabled
 */
ReleasesListByDistributionGroup200ResponseInner.prototype['enabled'] = undefined;

/**
 * ID identifying this unique release.
 * @member {Number} id
 */
ReleasesListByDistributionGroup200ResponseInner.prototype['id'] = undefined;

/**
 * This value determines if a release is external or not.
 * @member {Boolean} is_external_build
 */
ReleasesListByDistributionGroup200ResponseInner.prototype['is_external_build'] = undefined;

/**
 * A boolean which determines whether the release is a mandatory update or not.
 * @member {Boolean} mandatory_update
 */
ReleasesListByDistributionGroup200ResponseInner.prototype['mandatory_update'] = undefined;

/**
 * The release's origin
 * @member {module:model/ReleasesListByDistributionGroup200ResponseInner.OriginEnum} origin
 */
ReleasesListByDistributionGroup200ResponseInner.prototype['origin'] = undefined;

/**
 * The release's short version.<br> For iOS: CFBundleShortVersionString from info.plist.<br> For Android: android:versionName from AppManifest.xml. 
 * @member {String} short_version
 */
ReleasesListByDistributionGroup200ResponseInner.prototype['short_version'] = undefined;

/**
 * UTC time in ISO 8601 format of the uploaded time.
 * @member {String} uploaded_at
 */
ReleasesListByDistributionGroup200ResponseInner.prototype['uploaded_at'] = undefined;

/**
 * The release's version.<br> For iOS: CFBundleVersion from info.plist.<br> For Android: android:versionCode from AppManifest.xml. 
 * @member {String} version
 */
ReleasesListByDistributionGroup200ResponseInner.prototype['version'] = undefined;





/**
 * Allowed values for the <code>origin</code> property.
 * @enum {String}
 * @readonly
 */
ReleasesListByDistributionGroup200ResponseInner['OriginEnum'] = {

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



export default ReleasesListByDistributionGroup200ResponseInner;

