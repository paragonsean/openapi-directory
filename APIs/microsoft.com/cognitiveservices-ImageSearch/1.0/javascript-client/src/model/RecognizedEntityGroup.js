/**
 * Image Search Client
 * The Image Search API lets you send a search query to Bing and get back a list of relevant images. This section provides technical details about the query parameters and headers that you use to request images and the JSON response objects that contain them. For examples that show how to make requests, see [Searching the Web for Images](https://docs.microsoft.com/azure/cognitive-services/bing-image-search/search-the-web).
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import RecognizedEntityRegion from './RecognizedEntityRegion';

/**
 * The RecognizedEntityGroup model module.
 * @module model/RecognizedEntityGroup
 * @version 1.0
 */
class RecognizedEntityGroup {
    /**
     * Constructs a new <code>RecognizedEntityGroup</code>.
     * Defines a group of previously recognized entities.
     * @alias module:model/RecognizedEntityGroup
     * @param name {String} The name of the group where images of the entity were also found. The following are possible groups. CelebRecognitionAnnotations: Similar to CelebrityAnnotations but provides a higher probability of an accurate match. CelebrityAnnotations: Contains celebrities such as actors, politicians, athletes, and historical figures.
     * @param recognizedEntityRegions {Array.<module:model/RecognizedEntityRegion>} The regions of the image that contain entities.
     */
    constructor(name, recognizedEntityRegions) { 
        
        RecognizedEntityGroup.initialize(this, name, recognizedEntityRegions);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, name, recognizedEntityRegions) { 
        obj['name'] = name;
        obj['recognizedEntityRegions'] = recognizedEntityRegions;
    }

    /**
     * Constructs a <code>RecognizedEntityGroup</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/RecognizedEntityGroup} obj Optional instance to populate.
     * @return {module:model/RecognizedEntityGroup} The populated <code>RecognizedEntityGroup</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new RecognizedEntityGroup();

            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('recognizedEntityRegions')) {
                obj['recognizedEntityRegions'] = ApiClient.convertToType(data['recognizedEntityRegions'], [RecognizedEntityRegion]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>RecognizedEntityGroup</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>RecognizedEntityGroup</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of RecognizedEntityGroup.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        if (data['recognizedEntityRegions']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['recognizedEntityRegions'])) {
                throw new Error("Expected the field `recognizedEntityRegions` to be an array in the JSON data but got " + data['recognizedEntityRegions']);
            }
            // validate the optional field `recognizedEntityRegions` (array)
            for (const item of data['recognizedEntityRegions']) {
                RecognizedEntityRegion.validateJSON(item);
            };
        }

        return true;
    }


}

RecognizedEntityGroup.RequiredProperties = ["name", "recognizedEntityRegions"];

/**
 * The name of the group where images of the entity were also found. The following are possible groups. CelebRecognitionAnnotations: Similar to CelebrityAnnotations but provides a higher probability of an accurate match. CelebrityAnnotations: Contains celebrities such as actors, politicians, athletes, and historical figures.
 * @member {String} name
 */
RecognizedEntityGroup.prototype['name'] = undefined;

/**
 * The regions of the image that contain entities.
 * @member {Array.<module:model/RecognizedEntityRegion>} recognizedEntityRegions
 */
RecognizedEntityGroup.prototype['recognizedEntityRegions'] = undefined;






export default RecognizedEntityGroup;

