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
import Response from './Response';
import Thing from './Thing';

/**
 * The RecognizedEntity model module.
 * @module model/RecognizedEntity
 * @version 1.0
 */
class RecognizedEntity {
    /**
     * Constructs a new <code>RecognizedEntity</code>.
     * Defines a recognized entity.
     * @alias module:model/RecognizedEntity
     * @extends module:model/Response
     * @implements module:model/Response
     * @param type {String} 
     */
    constructor(type) { 
        Response.initialize(this, type);
        RecognizedEntity.initialize(this, type);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, type) { 
    }

    /**
     * Constructs a <code>RecognizedEntity</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/RecognizedEntity} obj Optional instance to populate.
     * @return {module:model/RecognizedEntity} The populated <code>RecognizedEntity</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new RecognizedEntity();
            Response.constructFromObject(data, obj);
            Response.constructFromObject(data, obj);

            if (data.hasOwnProperty('entity')) {
                obj['entity'] = Thing.constructFromObject(data['entity']);
            }
            if (data.hasOwnProperty('matchConfidence')) {
                obj['matchConfidence'] = ApiClient.convertToType(data['matchConfidence'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>RecognizedEntity</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>RecognizedEntity</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of RecognizedEntity.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `entity`
        if (data['entity']) { // data not null
          Thing.validateJSON(data['entity']);
        }

        return true;
    }


}

RecognizedEntity.RequiredProperties = ["_type"];

/**
 * @member {module:model/Thing} entity
 */
RecognizedEntity.prototype['entity'] = undefined;

/**
 * The confidence that Bing has that the entity in the image matches this entity. The confidence ranges from 0.0 through 1.0 with 1.0 being very confident.
 * @member {Number} matchConfidence
 */
RecognizedEntity.prototype['matchConfidence'] = undefined;


// Implement Response interface:
/**
 * A String identifier.
 * @member {String} id
 */
Response.prototype['id'] = undefined;
/**
 * @member {String} _type
 */
Response.prototype['_type'] = undefined;




export default RecognizedEntity;

