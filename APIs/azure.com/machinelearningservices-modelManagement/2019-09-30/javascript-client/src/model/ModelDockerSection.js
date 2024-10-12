/**
 * Azure Machine Learning Model Management Service
 * These APIs allow end users to manage Azure Machine Learning Models, Images, Profiles, and Services.
 *
 * The version of the OpenAPI document: 2019-09-30
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import ContainerRegistry from './ContainerRegistry';

/**
 * The ModelDockerSection model module.
 * @module model/ModelDockerSection
 * @version 2019-09-30
 */
class ModelDockerSection {
    /**
     * Constructs a new <code>ModelDockerSection</code>.
     * @alias module:model/ModelDockerSection
     */
    constructor() { 
        
        ModelDockerSection.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ModelDockerSection</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ModelDockerSection} obj Optional instance to populate.
     * @return {module:model/ModelDockerSection} The populated <code>ModelDockerSection</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ModelDockerSection();

            if (data.hasOwnProperty('arguments')) {
                obj['arguments'] = ApiClient.convertToType(data['arguments'], ['String']);
            }
            if (data.hasOwnProperty('baseDockerfile')) {
                obj['baseDockerfile'] = ApiClient.convertToType(data['baseDockerfile'], 'String');
            }
            if (data.hasOwnProperty('baseImage')) {
                obj['baseImage'] = ApiClient.convertToType(data['baseImage'], 'String');
            }
            if (data.hasOwnProperty('baseImageRegistry')) {
                obj['baseImageRegistry'] = ContainerRegistry.constructFromObject(data['baseImageRegistry']);
            }
            if (data.hasOwnProperty('enabled')) {
                obj['enabled'] = ApiClient.convertToType(data['enabled'], 'Boolean');
            }
            if (data.hasOwnProperty('gpuSupport')) {
                obj['gpuSupport'] = ApiClient.convertToType(data['gpuSupport'], 'Boolean');
            }
            if (data.hasOwnProperty('sharedVolumes')) {
                obj['sharedVolumes'] = ApiClient.convertToType(data['sharedVolumes'], 'Boolean');
            }
            if (data.hasOwnProperty('shmSize')) {
                obj['shmSize'] = ApiClient.convertToType(data['shmSize'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ModelDockerSection</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ModelDockerSection</code>.
     */
    static validateJSON(data) {
        // ensure the json data is an array
        if (!Array.isArray(data['arguments'])) {
            throw new Error("Expected the field `arguments` to be an array in the JSON data but got " + data['arguments']);
        }
        // ensure the json data is a string
        if (data['baseDockerfile'] && !(typeof data['baseDockerfile'] === 'string' || data['baseDockerfile'] instanceof String)) {
            throw new Error("Expected the field `baseDockerfile` to be a primitive type in the JSON string but got " + data['baseDockerfile']);
        }
        // ensure the json data is a string
        if (data['baseImage'] && !(typeof data['baseImage'] === 'string' || data['baseImage'] instanceof String)) {
            throw new Error("Expected the field `baseImage` to be a primitive type in the JSON string but got " + data['baseImage']);
        }
        // validate the optional field `baseImageRegistry`
        if (data['baseImageRegistry']) { // data not null
          ContainerRegistry.validateJSON(data['baseImageRegistry']);
        }
        // ensure the json data is a string
        if (data['shmSize'] && !(typeof data['shmSize'] === 'string' || data['shmSize'] instanceof String)) {
            throw new Error("Expected the field `shmSize` to be a primitive type in the JSON string but got " + data['shmSize']);
        }

        return true;
    }


}



/**
 * Extra arguments to the Docker run command.
 * @member {Array.<String>} arguments
 */
ModelDockerSection.prototype['arguments'] = undefined;

/**
 * Base Dockerfile used for Docker-based runs. Mutually exclusive with BaseImage.
 * @member {String} baseDockerfile
 */
ModelDockerSection.prototype['baseDockerfile'] = undefined;

/**
 * Base image used for Docker-based runs. Mutually exclusive with BaseDockerfile.
 * @member {String} baseImage
 */
ModelDockerSection.prototype['baseImage'] = undefined;

/**
 * @member {module:model/ContainerRegistry} baseImageRegistry
 */
ModelDockerSection.prototype['baseImageRegistry'] = undefined;

/**
 * Set True to perform this run inside a Docker container.
 * @member {Boolean} enabled
 */
ModelDockerSection.prototype['enabled'] = undefined;

/**
 * Run with NVidia Docker extension to support GPUs.
 * @member {Boolean} gpuSupport
 */
ModelDockerSection.prototype['gpuSupport'] = undefined;

/**
 * Set False if necessary to work around shared volume bugs on Windows.
 * @member {Boolean} sharedVolumes
 */
ModelDockerSection.prototype['sharedVolumes'] = undefined;

/**
 * The shared memory size setting for NVidia GPUs.
 * @member {String} shmSize
 */
ModelDockerSection.prototype['shmSize'] = undefined;






export default ModelDockerSection;

