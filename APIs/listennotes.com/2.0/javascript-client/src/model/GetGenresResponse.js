/**
 * Listen API: Podcast Search, Directory, and Insights API
 * Simple & no-nonsense podcast search & directory API. Search all podcasts and episodes by people, places, or topics. 
 *
 * The version of the OpenAPI document: 2.0
 * Contact: hello@listennotes.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import Genre from './Genre';

/**
 * The GetGenresResponse model module.
 * @module model/GetGenresResponse
 * @version 2.0
 */
class GetGenresResponse {
    /**
     * Constructs a new <code>GetGenresResponse</code>.
     * @alias module:model/GetGenresResponse
     * @param genres {Array.<module:model/Genre>} 
     */
    constructor(genres) { 
        
        GetGenresResponse.initialize(this, genres);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, genres) { 
        obj['genres'] = genres;
    }

    /**
     * Constructs a <code>GetGenresResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetGenresResponse} obj Optional instance to populate.
     * @return {module:model/GetGenresResponse} The populated <code>GetGenresResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetGenresResponse();

            if (data.hasOwnProperty('genres')) {
                obj['genres'] = ApiClient.convertToType(data['genres'], [Genre]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GetGenresResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetGenresResponse</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of GetGenresResponse.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        if (data['genres']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['genres'])) {
                throw new Error("Expected the field `genres` to be an array in the JSON data but got " + data['genres']);
            }
            // validate the optional field `genres` (array)
            for (const item of data['genres']) {
                Genre.validateJSON(item);
            };
        }

        return true;
    }


}

GetGenresResponse.RequiredProperties = ["genres"];

/**
 * @member {Array.<module:model/Genre>} genres
 */
GetGenresResponse.prototype['genres'] = undefined;






export default GetGenresResponse;

