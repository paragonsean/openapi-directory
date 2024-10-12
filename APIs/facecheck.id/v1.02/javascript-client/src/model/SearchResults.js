/**
 * Facial Recognition Reverse Image Face Search API
 * Let your users search the Internet by face! Integrate FaceCheck facial search seamlessly with your app, website or software platform.   FaceCheck's REST API is hassle-free and easy to use. For code examples visit <a href='https://facecheck.id/Face-Search/API'>https://facecheck.id/Face-Search/API</a>
 *
 * The version of the OpenAPI document: v1.02
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import SearchItem from './SearchItem';

/**
 * The SearchResults model module.
 * @module model/SearchResults
 * @version v1.02
 */
class SearchResults {
    /**
     * Constructs a new <code>SearchResults</code>.
     * @alias module:model/SearchResults
     */
    constructor() { 
        
        SearchResults.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>SearchResults</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SearchResults} obj Optional instance to populate.
     * @return {module:model/SearchResults} The populated <code>SearchResults</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SearchResults();

            if (data.hasOwnProperty('demo')) {
                obj['demo'] = ApiClient.convertToType(data['demo'], 'Boolean');
            }
            if (data.hasOwnProperty('face_per_sec')) {
                obj['face_per_sec'] = ApiClient.convertToType(data['face_per_sec'], 'Number');
            }
            if (data.hasOwnProperty('freeRam')) {
                obj['freeRam'] = ApiClient.convertToType(data['freeRam'], 'Number');
            }
            if (data.hasOwnProperty('images_in_bundle')) {
                obj['images_in_bundle'] = ApiClient.convertToType(data['images_in_bundle'], 'Number');
            }
            if (data.hasOwnProperty('items')) {
                obj['items'] = ApiClient.convertToType(data['items'], [SearchItem]);
            }
            if (data.hasOwnProperty('max_score')) {
                obj['max_score'] = ApiClient.convertToType(data['max_score'], 'Number');
            }
            if (data.hasOwnProperty('performance')) {
                obj['performance'] = ApiClient.convertToType(data['performance'], 'String');
            }
            if (data.hasOwnProperty('scaned_till_index')) {
                obj['scaned_till_index'] = ApiClient.convertToType(data['scaned_till_index'], 'Number');
            }
            if (data.hasOwnProperty('searchedFaces')) {
                obj['searchedFaces'] = ApiClient.convertToType(data['searchedFaces'], 'Number');
            }
            if (data.hasOwnProperty('tookSeconds')) {
                obj['tookSeconds'] = ApiClient.convertToType(data['tookSeconds'], 'Number');
            }
            if (data.hasOwnProperty('tookSecondsDownload')) {
                obj['tookSecondsDownload'] = ApiClient.convertToType(data['tookSecondsDownload'], 'Number');
            }
            if (data.hasOwnProperty('tookSecondsQueue')) {
                obj['tookSecondsQueue'] = ApiClient.convertToType(data['tookSecondsQueue'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>SearchResults</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>SearchResults</code>.
     */
    static validateJSON(data) {
        if (data['items']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['items'])) {
                throw new Error("Expected the field `items` to be an array in the JSON data but got " + data['items']);
            }
            // validate the optional field `items` (array)
            for (const item of data['items']) {
                SearchItem.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['performance'] && !(typeof data['performance'] === 'string' || data['performance'] instanceof String)) {
            throw new Error("Expected the field `performance` to be a primitive type in the JSON string but got " + data['performance']);
        }

        return true;
    }


}



/**
 * @member {Boolean} demo
 */
SearchResults.prototype['demo'] = undefined;

/**
 * @member {Number} face_per_sec
 */
SearchResults.prototype['face_per_sec'] = undefined;

/**
 * @member {Number} freeRam
 */
SearchResults.prototype['freeRam'] = undefined;

/**
 * @member {Number} images_in_bundle
 */
SearchResults.prototype['images_in_bundle'] = undefined;

/**
 * @member {Array.<module:model/SearchItem>} items
 */
SearchResults.prototype['items'] = undefined;

/**
 * @member {Number} max_score
 */
SearchResults.prototype['max_score'] = undefined;

/**
 * @member {String} performance
 */
SearchResults.prototype['performance'] = undefined;

/**
 * @member {Number} scaned_till_index
 */
SearchResults.prototype['scaned_till_index'] = undefined;

/**
 * @member {Number} searchedFaces
 */
SearchResults.prototype['searchedFaces'] = undefined;

/**
 * @member {Number} tookSeconds
 */
SearchResults.prototype['tookSeconds'] = undefined;

/**
 * @member {Number} tookSecondsDownload
 */
SearchResults.prototype['tookSecondsDownload'] = undefined;

/**
 * @member {Number} tookSecondsQueue
 */
SearchResults.prototype['tookSecondsQueue'] = undefined;






export default SearchResults;

