/**
 * Meshery API.
 * the purpose of this application is to provide an application that is using plain go code to define an API  This should demonstrate all the possible comment annotations that are available to turn go code into a fully compliant swagger 2.0 spec
 *
 * The version of the OpenAPI document: 0.4.27
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import Volume from './Volume';

/**
 * The VolumeListOKBody model module.
 * @module model/VolumeListOKBody
 * @version 0.4.27
 */
class VolumeListOKBody {
    /**
     * Constructs a new <code>VolumeListOKBody</code>.
     * VolumeListOKBody Volume list response
     * @alias module:model/VolumeListOKBody
     * @param volumes {Array.<module:model/Volume>} List of volumes
     * @param warnings {Array.<String>} Warnings that occurred when fetching the list of volumes
     */
    constructor(volumes, warnings) { 
        
        VolumeListOKBody.initialize(this, volumes, warnings);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, volumes, warnings) { 
        obj['Volumes'] = volumes;
        obj['Warnings'] = warnings;
    }

    /**
     * Constructs a <code>VolumeListOKBody</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/VolumeListOKBody} obj Optional instance to populate.
     * @return {module:model/VolumeListOKBody} The populated <code>VolumeListOKBody</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new VolumeListOKBody();

            if (data.hasOwnProperty('Volumes')) {
                obj['Volumes'] = ApiClient.convertToType(data['Volumes'], [Volume]);
            }
            if (data.hasOwnProperty('Warnings')) {
                obj['Warnings'] = ApiClient.convertToType(data['Warnings'], ['String']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>VolumeListOKBody</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>VolumeListOKBody</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of VolumeListOKBody.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        if (data['Volumes']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['Volumes'])) {
                throw new Error("Expected the field `Volumes` to be an array in the JSON data but got " + data['Volumes']);
            }
            // validate the optional field `Volumes` (array)
            for (const item of data['Volumes']) {
                Volume.validateJSON(item);
            };
        }
        // ensure the json data is an array
        if (!Array.isArray(data['Warnings'])) {
            throw new Error("Expected the field `Warnings` to be an array in the JSON data but got " + data['Warnings']);
        }

        return true;
    }


}

VolumeListOKBody.RequiredProperties = ["Volumes", "Warnings"];

/**
 * List of volumes
 * @member {Array.<module:model/Volume>} Volumes
 */
VolumeListOKBody.prototype['Volumes'] = undefined;

/**
 * Warnings that occurred when fetching the list of volumes
 * @member {Array.<String>} Warnings
 */
VolumeListOKBody.prototype['Warnings'] = undefined;






export default VolumeListOKBody;

