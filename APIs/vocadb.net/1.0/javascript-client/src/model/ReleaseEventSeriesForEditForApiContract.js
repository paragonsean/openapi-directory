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
import ContentLanguageSelection from './ContentLanguageSelection';
import EntryStatus from './EntryStatus';
import EntryThumbForApiContract from './EntryThumbForApiContract';
import EventCategory from './EventCategory';
import LocalizedStringWithIdContract from './LocalizedStringWithIdContract';
import WebLinkForApiContract from './WebLinkForApiContract';

/**
 * The ReleaseEventSeriesForEditForApiContract model module.
 * @module model/ReleaseEventSeriesForEditForApiContract
 * @version 1.0
 */
class ReleaseEventSeriesForEditForApiContract {
    /**
     * Constructs a new <code>ReleaseEventSeriesForEditForApiContract</code>.
     * @alias module:model/ReleaseEventSeriesForEditForApiContract
     */
    constructor() { 
        
        ReleaseEventSeriesForEditForApiContract.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ReleaseEventSeriesForEditForApiContract</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ReleaseEventSeriesForEditForApiContract} obj Optional instance to populate.
     * @return {module:model/ReleaseEventSeriesForEditForApiContract} The populated <code>ReleaseEventSeriesForEditForApiContract</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ReleaseEventSeriesForEditForApiContract();

            if (data.hasOwnProperty('category')) {
                obj['category'] = EventCategory.constructFromObject(data['category']);
            }
            if (data.hasOwnProperty('defaultNameLanguage')) {
                obj['defaultNameLanguage'] = ContentLanguageSelection.constructFromObject(data['defaultNameLanguage']);
            }
            if (data.hasOwnProperty('deleted')) {
                obj['deleted'] = ApiClient.convertToType(data['deleted'], 'Boolean');
            }
            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
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
            if (data.hasOwnProperty('names')) {
                obj['names'] = ApiClient.convertToType(data['names'], [LocalizedStringWithIdContract]);
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = EntryStatus.constructFromObject(data['status']);
            }
            if (data.hasOwnProperty('webLinks')) {
                obj['webLinks'] = ApiClient.convertToType(data['webLinks'], [WebLinkForApiContract]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ReleaseEventSeriesForEditForApiContract</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ReleaseEventSeriesForEditForApiContract</code>.
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
        if (data['names']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['names'])) {
                throw new Error("Expected the field `names` to be an array in the JSON data but got " + data['names']);
            }
            // validate the optional field `names` (array)
            for (const item of data['names']) {
                LocalizedStringWithIdContract.validateJSON(item);
            };
        }
        if (data['webLinks']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['webLinks'])) {
                throw new Error("Expected the field `webLinks` to be an array in the JSON data but got " + data['webLinks']);
            }
            // validate the optional field `webLinks` (array)
            for (const item of data['webLinks']) {
                WebLinkForApiContract.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {module:model/EventCategory} category
 */
ReleaseEventSeriesForEditForApiContract.prototype['category'] = undefined;

/**
 * @member {module:model/ContentLanguageSelection} defaultNameLanguage
 */
ReleaseEventSeriesForEditForApiContract.prototype['defaultNameLanguage'] = undefined;

/**
 * @member {Boolean} deleted
 */
ReleaseEventSeriesForEditForApiContract.prototype['deleted'] = undefined;

/**
 * @member {String} description
 */
ReleaseEventSeriesForEditForApiContract.prototype['description'] = undefined;

/**
 * @member {Number} id
 */
ReleaseEventSeriesForEditForApiContract.prototype['id'] = undefined;

/**
 * @member {module:model/EntryThumbForApiContract} mainPicture
 */
ReleaseEventSeriesForEditForApiContract.prototype['mainPicture'] = undefined;

/**
 * @member {String} name
 */
ReleaseEventSeriesForEditForApiContract.prototype['name'] = undefined;

/**
 * @member {Array.<module:model/LocalizedStringWithIdContract>} names
 */
ReleaseEventSeriesForEditForApiContract.prototype['names'] = undefined;

/**
 * @member {module:model/EntryStatus} status
 */
ReleaseEventSeriesForEditForApiContract.prototype['status'] = undefined;

/**
 * @member {Array.<module:model/WebLinkForApiContract>} webLinks
 */
ReleaseEventSeriesForEditForApiContract.prototype['webLinks'] = undefined;






export default ReleaseEventSeriesForEditForApiContract;

