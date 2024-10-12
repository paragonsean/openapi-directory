/**
 * Azure Alerts Management Service Resource Provider
 * APIs for Azure Smart Detector Alert Rules CRUD operations.
 *
 * The version of the OpenAPI document: 2019-03-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The Detector model module.
 * @module model/Detector
 * @version 2019-03-01
 */
class Detector {
    /**
     * Constructs a new <code>Detector</code>.
     * The detector information. By default this is not populated, unless it&#39;s specified in expandDetector
     * @alias module:model/Detector
     * @param id {String} The detector id.
     */
    constructor(id) { 
        
        Detector.initialize(this, id);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, id) { 
        obj['id'] = id;
    }

    /**
     * Constructs a <code>Detector</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Detector} obj Optional instance to populate.
     * @return {module:model/Detector} The populated <code>Detector</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Detector();

            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('imagePaths')) {
                obj['imagePaths'] = ApiClient.convertToType(data['imagePaths'], ['String']);
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('parameters')) {
                obj['parameters'] = ApiClient.convertToType(data['parameters'], {'String': Object});
            }
            if (data.hasOwnProperty('supportedResourceTypes')) {
                obj['supportedResourceTypes'] = ApiClient.convertToType(data['supportedResourceTypes'], ['String']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Detector</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Detector</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Detector.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['description'] && !(typeof data['description'] === 'string' || data['description'] instanceof String)) {
            throw new Error("Expected the field `description` to be a primitive type in the JSON string but got " + data['description']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['imagePaths'])) {
            throw new Error("Expected the field `imagePaths` to be an array in the JSON data but got " + data['imagePaths']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['supportedResourceTypes'])) {
            throw new Error("Expected the field `supportedResourceTypes` to be an array in the JSON data but got " + data['supportedResourceTypes']);
        }

        return true;
    }


}

Detector.RequiredProperties = ["id"];

/**
 * The Smart Detector description. By default this is not populated, unless it's specified in expandDetector
 * @member {String} description
 */
Detector.prototype['description'] = undefined;

/**
 * The detector id.
 * @member {String} id
 */
Detector.prototype['id'] = undefined;

/**
 * The Smart Detector image path. By default this is not populated, unless it's specified in expandDetector
 * @member {Array.<String>} imagePaths
 */
Detector.prototype['imagePaths'] = undefined;

/**
 * The Smart Detector name. By default this is not populated, unless it's specified in expandDetector
 * @member {String} name
 */
Detector.prototype['name'] = undefined;

/**
 * The detector's parameters.'
 * @member {Object.<String, Object>} parameters
 */
Detector.prototype['parameters'] = undefined;

/**
 * The Smart Detector supported resource types. By default this is not populated, unless it's specified in expandDetector
 * @member {Array.<String>} supportedResourceTypes
 */
Detector.prototype['supportedResourceTypes'] = undefined;






export default Detector;

