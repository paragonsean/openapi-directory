/**
 * groov View Public API
 * #### Revised: 2019-11-21  ### Overview groov View Public API revision 1. 
 *
 * The version of the OpenAPI document: R4.2a
 * Contact: developer@opto22.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The TagReference model module.
 * @module model/TagReference
 * @version R4.2a
 */
class TagReference {
    /**
     * Constructs a new <code>TagReference</code>.
     * @alias module:model/TagReference
     * @param id {Number} Unique id for the tag.
     */
    constructor(id) { 
        
        TagReference.initialize(this, id);
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
     * Constructs a <code>TagReference</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TagReference} obj Optional instance to populate.
     * @return {module:model/TagReference} The populated <code>TagReference</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TagReference();

            if (data.hasOwnProperty('count')) {
                obj['count'] = ApiClient.convertToType(data['count'], 'Number');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('index')) {
                obj['index'] = ApiClient.convertToType(data['index'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>TagReference</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>TagReference</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of TagReference.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }

        return true;
    }


}

TagReference.RequiredProperties = ["id"];

/**
 * For array tags, the number of elements to read, starting at index.
 * @member {Number} count
 */
TagReference.prototype['count'] = undefined;

/**
 * Unique id for the tag.
 * @member {Number} id
 */
TagReference.prototype['id'] = undefined;

/**
 * For array tags, the index to start reading at.
 * @member {Number} index
 */
TagReference.prototype['index'] = undefined;






export default TagReference;

