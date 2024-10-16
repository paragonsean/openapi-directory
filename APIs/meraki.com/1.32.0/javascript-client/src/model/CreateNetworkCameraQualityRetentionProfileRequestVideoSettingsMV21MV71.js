/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV21MV71 model module.
 * @module model/CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV21MV71
 * @version 1.32.0
 */
class CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV21MV71 {
    /**
     * Constructs a new <code>CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV21MV71</code>.
     * Quality and resolution for MV21/MV71 camera models.
     * @alias module:model/CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV21MV71
     * @param quality {module:model/CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV21MV71.QualityEnum} Quality of the camera. Can be one of 'Standard', 'Enhanced' or 'High'.
     * @param resolution {module:model/CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV21MV71.ResolutionEnum} Resolution of the camera. Can be one of '1280x720'.
     */
    constructor(quality, resolution) { 
        
        CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV21MV71.initialize(this, quality, resolution);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, quality, resolution) { 
        obj['quality'] = quality;
        obj['resolution'] = resolution;
    }

    /**
     * Constructs a <code>CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV21MV71</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV21MV71} obj Optional instance to populate.
     * @return {module:model/CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV21MV71} The populated <code>CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV21MV71</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV21MV71();

            if (data.hasOwnProperty('quality')) {
                obj['quality'] = ApiClient.convertToType(data['quality'], 'String');
            }
            if (data.hasOwnProperty('resolution')) {
                obj['resolution'] = ApiClient.convertToType(data['resolution'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV21MV71</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV21MV71</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV21MV71.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['quality'] && !(typeof data['quality'] === 'string' || data['quality'] instanceof String)) {
            throw new Error("Expected the field `quality` to be a primitive type in the JSON string but got " + data['quality']);
        }
        // ensure the json data is a string
        if (data['resolution'] && !(typeof data['resolution'] === 'string' || data['resolution'] instanceof String)) {
            throw new Error("Expected the field `resolution` to be a primitive type in the JSON string but got " + data['resolution']);
        }

        return true;
    }


}

CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV21MV71.RequiredProperties = ["quality", "resolution"];

/**
 * Quality of the camera. Can be one of 'Standard', 'Enhanced' or 'High'.
 * @member {module:model/CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV21MV71.QualityEnum} quality
 */
CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV21MV71.prototype['quality'] = undefined;

/**
 * Resolution of the camera. Can be one of '1280x720'.
 * @member {module:model/CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV21MV71.ResolutionEnum} resolution
 */
CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV21MV71.prototype['resolution'] = undefined;





/**
 * Allowed values for the <code>quality</code> property.
 * @enum {String}
 * @readonly
 */
CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV21MV71['QualityEnum'] = {

    /**
     * value: "Enhanced"
     * @const
     */
    "Enhanced": "Enhanced",

    /**
     * value: "High"
     * @const
     */
    "High": "High",

    /**
     * value: "Standard"
     * @const
     */
    "Standard": "Standard"
};


/**
 * Allowed values for the <code>resolution</code> property.
 * @enum {String}
 * @readonly
 */
CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV21MV71['ResolutionEnum'] = {

    /**
     * value: "1280x720"
     * @const
     */
    "1280x720": "1280x720"
};



export default CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV21MV71;

