/**
 * Zalando Shop
 * The shop API empowers developers to build amazing new apps or websites using Zalando shop data and services.
 *
 * The version of the OpenAPI document: v1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import Brand from './Brand';
import Page from './Page';

/**
 * The Brands model module.
 * @module model/Brands
 * @version v1.0
 */
class Brands {
    /**
     * Constructs a new <code>Brands</code>.
     * Zalando API Paged Brands Schema
     * @alias module:model/Brands
     * @extends module:model/Page
     * @implements module:model/Page
     * @param page {Number} page number
     * @param size {Number} total number of elements in a page
     * @param totalElements {Number} total elements in the response
     * @param totalPages {Number} total number of pages in the response
     */
    constructor(page, size, totalElements, totalPages) { 
        Page.initialize(this, content, page, size, totalElements, totalPages);
        Brands.initialize(this, page, size, totalElements, totalPages);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, page, size, totalElements, totalPages) { 
    }

    /**
     * Constructs a <code>Brands</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Brands} obj Optional instance to populate.
     * @return {module:model/Brands} The populated <code>Brands</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Brands();
            Page.constructFromObject(data, obj);
            Page.constructFromObject(data, obj);

            if (data.hasOwnProperty('content')) {
                obj['content'] = ApiClient.convertToType(data['content'], [Brand]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Brands</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Brands</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Brands.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        if (data['content']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['content'])) {
                throw new Error("Expected the field `content` to be an array in the JSON data but got " + data['content']);
            }
            // validate the optional field `content` (array)
            for (const item of data['content']) {
                Brand.validateJSON(item);
            };
        }

        return true;
    }


}

Brands.RequiredProperties = ["page", "size", "totalElements", "totalPages"];

/**
 * @member {Array.<module:model/Brand>} content
 */
Brands.prototype['content'] = undefined;


// Implement Page interface:
/**
 * page content
 * @member {Array.<Object>} content
 */
Page.prototype['content'] = undefined;
/**
 * page number
 * @member {Number} page
 */
Page.prototype['page'] = undefined;
/**
 * total number of elements in a page
 * @member {Number} size
 */
Page.prototype['size'] = undefined;
/**
 * total elements in the response
 * @member {Number} totalElements
 */
Page.prototype['totalElements'] = undefined;
/**
 * total number of pages in the response
 * @member {Number} totalPages
 */
Page.prototype['totalPages'] = undefined;




export default Brands;

