/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 23 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 0.0.0-streaming
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV63X model module.
 * @module model/CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV63X
 * @version 0.0.0-streaming
 */
class CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV63X {
    /**
     * Constructs a new <code>CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV63X</code>.
     * Quality and resolution for MV63X camera models.
     * @alias module:model/CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV63X
     * @param quality {module:model/CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV63X.QualityEnum} Quality of the camera. Can be one of 'Standard', 'Enhanced' or 'High'.
     * @param resolution {module:model/CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV63X.ResolutionEnum} Resolution of the camera. Can be one of '1920x1080', '2688x1512' or '3840x2160'.
     */
    constructor(quality, resolution) { 
        
        CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV63X.initialize(this, quality, resolution);
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
     * Constructs a <code>CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV63X</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV63X} obj Optional instance to populate.
     * @return {module:model/CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV63X} The populated <code>CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV63X</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV63X();

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
     * Validates the JSON data with respect to <code>CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV63X</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV63X</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV63X.RequiredProperties) {
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

CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV63X.RequiredProperties = ["quality", "resolution"];

/**
 * Quality of the camera. Can be one of 'Standard', 'Enhanced' or 'High'.
 * @member {module:model/CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV63X.QualityEnum} quality
 */
CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV63X.prototype['quality'] = undefined;

/**
 * Resolution of the camera. Can be one of '1920x1080', '2688x1512' or '3840x2160'.
 * @member {module:model/CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV63X.ResolutionEnum} resolution
 */
CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV63X.prototype['resolution'] = undefined;





/**
 * Allowed values for the <code>quality</code> property.
 * @enum {String}
 * @readonly
 */
CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV63X['QualityEnum'] = {

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
CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV63X['ResolutionEnum'] = {

    /**
     * value: "1920x1080"
     * @const
     */
    "1920x1080": "1920x1080",

    /**
     * value: "2688x1512"
     * @const
     */
    "2688x1512": "2688x1512",

    /**
     * value: "3840x2160"
     * @const
     */
    "3840x2160": "3840x2160"
};



export default CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV63X;

