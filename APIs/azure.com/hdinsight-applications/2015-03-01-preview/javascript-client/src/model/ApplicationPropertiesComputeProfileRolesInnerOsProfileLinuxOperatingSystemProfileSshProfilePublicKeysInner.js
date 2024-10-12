/**
 * HDInsightManagementClient
 * The HDInsight Management Client.
 *
 * The version of the OpenAPI document: 2015-03-01-preview
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The ApplicationPropertiesComputeProfileRolesInnerOsProfileLinuxOperatingSystemProfileSshProfilePublicKeysInner model module.
 * @module model/ApplicationPropertiesComputeProfileRolesInnerOsProfileLinuxOperatingSystemProfileSshProfilePublicKeysInner
 * @version 2015-03-01-preview
 */
class ApplicationPropertiesComputeProfileRolesInnerOsProfileLinuxOperatingSystemProfileSshProfilePublicKeysInner {
    /**
     * Constructs a new <code>ApplicationPropertiesComputeProfileRolesInnerOsProfileLinuxOperatingSystemProfileSshProfilePublicKeysInner</code>.
     * The SSH public key for the cluster nodes.
     * @alias module:model/ApplicationPropertiesComputeProfileRolesInnerOsProfileLinuxOperatingSystemProfileSshProfilePublicKeysInner
     */
    constructor() { 
        
        ApplicationPropertiesComputeProfileRolesInnerOsProfileLinuxOperatingSystemProfileSshProfilePublicKeysInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ApplicationPropertiesComputeProfileRolesInnerOsProfileLinuxOperatingSystemProfileSshProfilePublicKeysInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ApplicationPropertiesComputeProfileRolesInnerOsProfileLinuxOperatingSystemProfileSshProfilePublicKeysInner} obj Optional instance to populate.
     * @return {module:model/ApplicationPropertiesComputeProfileRolesInnerOsProfileLinuxOperatingSystemProfileSshProfilePublicKeysInner} The populated <code>ApplicationPropertiesComputeProfileRolesInnerOsProfileLinuxOperatingSystemProfileSshProfilePublicKeysInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ApplicationPropertiesComputeProfileRolesInnerOsProfileLinuxOperatingSystemProfileSshProfilePublicKeysInner();

            if (data.hasOwnProperty('certificateData')) {
                obj['certificateData'] = ApiClient.convertToType(data['certificateData'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ApplicationPropertiesComputeProfileRolesInnerOsProfileLinuxOperatingSystemProfileSshProfilePublicKeysInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ApplicationPropertiesComputeProfileRolesInnerOsProfileLinuxOperatingSystemProfileSshProfilePublicKeysInner</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['certificateData'] && !(typeof data['certificateData'] === 'string' || data['certificateData'] instanceof String)) {
            throw new Error("Expected the field `certificateData` to be a primitive type in the JSON string but got " + data['certificateData']);
        }

        return true;
    }


}



/**
 * The certificate for SSH.
 * @member {String} certificateData
 */
ApplicationPropertiesComputeProfileRolesInnerOsProfileLinuxOperatingSystemProfileSshProfilePublicKeysInner.prototype['certificateData'] = undefined;






export default ApplicationPropertiesComputeProfileRolesInnerOsProfileLinuxOperatingSystemProfileSshProfilePublicKeysInner;

