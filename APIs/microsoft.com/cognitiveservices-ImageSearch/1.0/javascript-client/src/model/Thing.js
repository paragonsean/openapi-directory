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
import ImageObject from './ImageObject';
import Response from './Response';

/**
 * The Thing model module.
 * @module model/Thing
 * @version 1.0
 */
class Thing {
    /**
     * Constructs a new <code>Thing</code>.
     * Defines a thing.
     * @alias module:model/Thing
     * @extends module:model/Response
     * @implements module:model/Response
     * @param type {String} 
     */
    constructor(type) { 
        Response.initialize(this, type);
        Thing.initialize(this, type);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, type) { 
    }

    /**
     * Constructs a <code>Thing</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Thing} obj Optional instance to populate.
     * @return {module:model/Thing} The populated <code>Thing</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Thing();
            Response.constructFromObject(data, obj);
            Response.constructFromObject(data, obj);

            if (data.hasOwnProperty('alternateName')) {
                obj['alternateName'] = ApiClient.convertToType(data['alternateName'], 'String');
            }
            if (data.hasOwnProperty('bingId')) {
                obj['bingId'] = ApiClient.convertToType(data['bingId'], 'String');
            }
            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('image')) {
                obj['image'] = ImageObject.constructFromObject(data['image']);
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('url')) {
                obj['url'] = ApiClient.convertToType(data['url'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Thing</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Thing</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Thing.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['alternateName'] && !(typeof data['alternateName'] === 'string' || data['alternateName'] instanceof String)) {
            throw new Error("Expected the field `alternateName` to be a primitive type in the JSON string but got " + data['alternateName']);
        }
        // ensure the json data is a string
        if (data['bingId'] && !(typeof data['bingId'] === 'string' || data['bingId'] instanceof String)) {
            throw new Error("Expected the field `bingId` to be a primitive type in the JSON string but got " + data['bingId']);
        }
        // ensure the json data is a string
        if (data['description'] && !(typeof data['description'] === 'string' || data['description'] instanceof String)) {
            throw new Error("Expected the field `description` to be a primitive type in the JSON string but got " + data['description']);
        }
        // validate the optional field `image`
        if (data['image']) { // data not null
          ImageObject.validateJSON(data['image']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['url'] && !(typeof data['url'] === 'string' || data['url'] instanceof String)) {
            throw new Error("Expected the field `url` to be a primitive type in the JSON string but got " + data['url']);
        }

        return true;
    }


}

Thing.RequiredProperties = ["_type"];

/**
 * An alias for the item
 * @member {String} alternateName
 */
Thing.prototype['alternateName'] = undefined;

/**
 * An ID that uniquely identifies this item.
 * @member {String} bingId
 */
Thing.prototype['bingId'] = undefined;

/**
 * A short description of the item.
 * @member {String} description
 */
Thing.prototype['description'] = undefined;

/**
 * @member {module:model/ImageObject} image
 */
Thing.prototype['image'] = undefined;

/**
 * The name of the thing represented by this object.
 * @member {String} name
 */
Thing.prototype['name'] = undefined;

/**
 * The URL to get more information about the thing represented by this object.
 * @member {String} url
 */
Thing.prototype['url'] = undefined;


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




export default Thing;

