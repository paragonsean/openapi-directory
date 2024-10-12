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
import EntryStatus from './EntryStatus';
import EntryThumbForApiContract from './EntryThumbForApiContract';
import SongInListEditContract from './SongInListEditContract';
import SongListFeaturedCategory from './SongListFeaturedCategory';

/**
 * The SongListForEditForApiContract model module.
 * @module model/SongListForEditForApiContract
 * @version 1.0
 */
class SongListForEditForApiContract {
    /**
     * Constructs a new <code>SongListForEditForApiContract</code>.
     * @alias module:model/SongListForEditForApiContract
     */
    constructor() { 
        
        SongListForEditForApiContract.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>SongListForEditForApiContract</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SongListForEditForApiContract} obj Optional instance to populate.
     * @return {module:model/SongListForEditForApiContract} The populated <code>SongListForEditForApiContract</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SongListForEditForApiContract();

            if (data.hasOwnProperty('deleted')) {
                obj['deleted'] = ApiClient.convertToType(data['deleted'], 'Boolean');
            }
            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('eventDate')) {
                obj['eventDate'] = ApiClient.convertToType(data['eventDate'], 'Date');
            }
            if (data.hasOwnProperty('featuredCategory')) {
                obj['featuredCategory'] = SongListFeaturedCategory.constructFromObject(data['featuredCategory']);
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('mainPicture')) {
                obj['mainPicture'] = EntryThumbForApiContract.constructFromObject(data['mainPicture']);
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('songLinks')) {
                obj['songLinks'] = ApiClient.convertToType(data['songLinks'], [SongInListEditContract]);
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = EntryStatus.constructFromObject(data['status']);
            }
            if (data.hasOwnProperty('updateNotes')) {
                obj['updateNotes'] = ApiClient.convertToType(data['updateNotes'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>SongListForEditForApiContract</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>SongListForEditForApiContract</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['description'] && !(typeof data['description'] === 'string' || data['description'] instanceof String)) {
            throw new Error("Expected the field `description` to be a primitive type in the JSON string but got " + data['description']);
        }
        // validate the optional field `mainPicture`
        if (data['mainPicture']) { // data not null
          EntryThumbForApiContract.validateJSON(data['mainPicture']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        if (data['songLinks']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['songLinks'])) {
                throw new Error("Expected the field `songLinks` to be an array in the JSON data but got " + data['songLinks']);
            }
            // validate the optional field `songLinks` (array)
            for (const item of data['songLinks']) {
                SongInListEditContract.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['updateNotes'] && !(typeof data['updateNotes'] === 'string' || data['updateNotes'] instanceof String)) {
            throw new Error("Expected the field `updateNotes` to be a primitive type in the JSON string but got " + data['updateNotes']);
        }

        return true;
    }


}



/**
 * @member {Boolean} deleted
 */
SongListForEditForApiContract.prototype['deleted'] = undefined;

/**
 * @member {String} description
 */
SongListForEditForApiContract.prototype['description'] = undefined;

/**
 * @member {Date} eventDate
 */
SongListForEditForApiContract.prototype['eventDate'] = undefined;

/**
 * @member {module:model/SongListFeaturedCategory} featuredCategory
 */
SongListForEditForApiContract.prototype['featuredCategory'] = undefined;

/**
 * @member {Number} id
 */
SongListForEditForApiContract.prototype['id'] = undefined;

/**
 * @member {module:model/EntryThumbForApiContract} mainPicture
 */
SongListForEditForApiContract.prototype['mainPicture'] = undefined;

/**
 * @member {String} name
 */
SongListForEditForApiContract.prototype['name'] = undefined;

/**
 * @member {Array.<module:model/SongInListEditContract>} songLinks
 */
SongListForEditForApiContract.prototype['songLinks'] = undefined;

/**
 * @member {module:model/EntryStatus} status
 */
SongListForEditForApiContract.prototype['status'] = undefined;

/**
 * @member {String} updateNotes
 */
SongListForEditForApiContract.prototype['updateNotes'] = undefined;






export default SongListForEditForApiContract;

