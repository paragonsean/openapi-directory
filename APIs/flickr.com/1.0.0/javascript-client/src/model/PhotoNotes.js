/**
 * Flickr API Schema
 * A subset of Flickr's API defined in Swagger format.
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import Note from './Note';

/**
 * The PhotoNotes model module.
 * @module model/PhotoNotes
 * @version 1.0.0
 */
class PhotoNotes {
    /**
     * Constructs a new <code>PhotoNotes</code>.
     * @alias module:model/PhotoNotes
     */
    constructor() { 
        
        PhotoNotes.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PhotoNotes</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PhotoNotes} obj Optional instance to populate.
     * @return {module:model/PhotoNotes} The populated <code>PhotoNotes</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PhotoNotes();

            if (data.hasOwnProperty('note')) {
                obj['note'] = ApiClient.convertToType(data['note'], [Note]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PhotoNotes</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PhotoNotes</code>.
     */
    static validateJSON(data) {
        if (data['note']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['note'])) {
                throw new Error("Expected the field `note` to be an array in the JSON data but got " + data['note']);
            }
            // validate the optional field `note` (array)
            for (const item of data['note']) {
                Note.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {Array.<module:model/Note>} note
 */
PhotoNotes.prototype['note'] = undefined;






export default PhotoNotes;

