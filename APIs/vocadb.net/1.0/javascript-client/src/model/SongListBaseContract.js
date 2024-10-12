/**
 * VocaDbWeb
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
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
import SongListFeaturedCategory from './SongListFeaturedCategory';

/**
 * The SongListBaseContract model module.
 * @module model/SongListBaseContract
 * @version 1.0
 */
class SongListBaseContract {
    /**
     * Constructs a new <code>SongListBaseContract</code>.
     * @alias module:model/SongListBaseContract
     */
    constructor() { 
        
        SongListBaseContract.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>SongListBaseContract</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SongListBaseContract} obj Optional instance to populate.
     * @return {module:model/SongListBaseContract} The populated <code>SongListBaseContract</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SongListBaseContract();

            if (data.hasOwnProperty('featuredCategory')) {
                obj['featuredCategory'] = SongListFeaturedCategory.constructFromObject(data['featuredCategory']);
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>SongListBaseContract</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>SongListBaseContract</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }

        return true;
    }


}



/**
 * @member {module:model/SongListFeaturedCategory} featuredCategory
 */
SongListBaseContract.prototype['featuredCategory'] = undefined;

/**
 * @member {Number} id
 */
SongListBaseContract.prototype['id'] = undefined;

/**
 * @member {String} name
 */
SongListBaseContract.prototype['name'] = undefined;






export default SongListBaseContract;

