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
 * The ExternallyHostedReleaseCreateRequest model module.
 * @module model/ExternallyHostedReleaseCreateRequest
 * @version v0.1
 */
class ExternallyHostedReleaseCreateRequest {
    /**
     * Constructs a new <code>ExternallyHostedReleaseCreateRequest</code>.
     * A request containing information for creating an externally hosted release.
     * @alias module:model/ExternallyHostedReleaseCreateRequest
     * @param buildVersion {String} The build version of the uploaded binary
     * @param externalDownloadUrl {String} The external URL to the release's binary.
     */
    constructor(buildVersion, externalDownloadUrl) { 
        
        ExternallyHostedReleaseCreateRequest.initialize(this, buildVersion, externalDownloadUrl);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, buildVersion, externalDownloadUrl) { 
        obj['build_version'] = buildVersion;
        obj['external_download_url'] = externalDownloadUrl;
    }

    /**
     * Constructs a <code>ExternallyHostedReleaseCreateRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ExternallyHostedReleaseCreateRequest} obj Optional instance to populate.
     * @return {module:model/ExternallyHostedReleaseCreateRequest} The populated <code>ExternallyHostedReleaseCreateRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ExternallyHostedReleaseCreateRequest();

            if (data.hasOwnProperty('build_number')) {
                obj['build_number'] = ApiClient.convertToType(data['build_number'], 'String');
            }
            if (data.hasOwnProperty('build_version')) {
                obj['build_version'] = ApiClient.convertToType(data['build_version'], 'String');
            }
            if (data.hasOwnProperty('external_download_url')) {
                obj['external_download_url'] = ApiClient.convertToType(data['external_download_url'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ExternallyHostedReleaseCreateRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ExternallyHostedReleaseCreateRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of ExternallyHostedReleaseCreateRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['build_number'] && !(typeof data['build_number'] === 'string' || data['build_number'] instanceof String)) {
            throw new Error("Expected the field `build_number` to be a primitive type in the JSON string but got " + data['build_number']);
        }
        // ensure the json data is a string
        if (data['build_version'] && !(typeof data['build_version'] === 'string' || data['build_version'] instanceof String)) {
            throw new Error("Expected the field `build_version` to be a primitive type in the JSON string but got " + data['build_version']);
        }
        // ensure the json data is a string
        if (data['external_download_url'] && !(typeof data['external_download_url'] === 'string' || data['external_download_url'] instanceof String)) {
            throw new Error("Expected the field `external_download_url` to be a primitive type in the JSON string but got " + data['external_download_url']);
        }

        return true;
    }


}

ExternallyHostedReleaseCreateRequest.RequiredProperties = ["build_version", "external_download_url"];

/**
 * The build number of the uploaded binary
 * @member {String} build_number
 */
ExternallyHostedReleaseCreateRequest.prototype['build_number'] = undefined;

/**
 * The build version of the uploaded binary
 * @member {String} build_version
 */
ExternallyHostedReleaseCreateRequest.prototype['build_version'] = undefined;

/**
 * The external URL to the release's binary.
 * @member {String} external_download_url
 */
ExternallyHostedReleaseCreateRequest.prototype['external_download_url'] = undefined;






export default ExternallyHostedReleaseCreateRequest;

