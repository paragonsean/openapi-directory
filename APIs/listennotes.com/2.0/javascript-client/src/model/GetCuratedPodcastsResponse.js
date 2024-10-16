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
import CuratedListSimple from './CuratedListSimple';

/**
 * The GetCuratedPodcastsResponse model module.
 * @module model/GetCuratedPodcastsResponse
 * @version 2.0
 */
class GetCuratedPodcastsResponse {
    /**
     * Constructs a new <code>GetCuratedPodcastsResponse</code>.
     * @alias module:model/GetCuratedPodcastsResponse
     * @param curatedLists {Array.<module:model/CuratedListSimple>} 
     * @param hasNext {Boolean} 
     * @param hasPrevious {Boolean} 
     * @param nextPageNumber {Number} 
     * @param pageNumber {Number} 
     * @param previousPageNumber {Number} 
     * @param total {Number} 
     */
    constructor(curatedLists, hasNext, hasPrevious, nextPageNumber, pageNumber, previousPageNumber, total) { 
        
        GetCuratedPodcastsResponse.initialize(this, curatedLists, hasNext, hasPrevious, nextPageNumber, pageNumber, previousPageNumber, total);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, curatedLists, hasNext, hasPrevious, nextPageNumber, pageNumber, previousPageNumber, total) { 
        obj['curated_lists'] = curatedLists;
        obj['has_next'] = hasNext;
        obj['has_previous'] = hasPrevious;
        obj['next_page_number'] = nextPageNumber;
        obj['page_number'] = pageNumber;
        obj['previous_page_number'] = previousPageNumber;
        obj['total'] = total;
    }

    /**
     * Constructs a <code>GetCuratedPodcastsResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetCuratedPodcastsResponse} obj Optional instance to populate.
     * @return {module:model/GetCuratedPodcastsResponse} The populated <code>GetCuratedPodcastsResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetCuratedPodcastsResponse();

            if (data.hasOwnProperty('curated_lists')) {
                obj['curated_lists'] = ApiClient.convertToType(data['curated_lists'], [CuratedListSimple]);
            }
            if (data.hasOwnProperty('has_next')) {
                obj['has_next'] = ApiClient.convertToType(data['has_next'], 'Boolean');
            }
            if (data.hasOwnProperty('has_previous')) {
                obj['has_previous'] = ApiClient.convertToType(data['has_previous'], 'Boolean');
            }
            if (data.hasOwnProperty('next_page_number')) {
                obj['next_page_number'] = ApiClient.convertToType(data['next_page_number'], 'Number');
            }
            if (data.hasOwnProperty('page_number')) {
                obj['page_number'] = ApiClient.convertToType(data['page_number'], 'Number');
            }
            if (data.hasOwnProperty('previous_page_number')) {
                obj['previous_page_number'] = ApiClient.convertToType(data['previous_page_number'], 'Number');
            }
            if (data.hasOwnProperty('total')) {
                obj['total'] = ApiClient.convertToType(data['total'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GetCuratedPodcastsResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetCuratedPodcastsResponse</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of GetCuratedPodcastsResponse.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        if (data['curated_lists']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['curated_lists'])) {
                throw new Error("Expected the field `curated_lists` to be an array in the JSON data but got " + data['curated_lists']);
            }
            // validate the optional field `curated_lists` (array)
            for (const item of data['curated_lists']) {
                CuratedListSimple.validateJSON(item);
            };
        }

        return true;
    }


}

GetCuratedPodcastsResponse.RequiredProperties = ["curated_lists", "has_next", "has_previous", "next_page_number", "page_number", "previous_page_number", "total"];

/**
 * @member {Array.<module:model/CuratedListSimple>} curated_lists
 */
GetCuratedPodcastsResponse.prototype['curated_lists'] = undefined;

/**
 * @member {Boolean} has_next
 */
GetCuratedPodcastsResponse.prototype['has_next'] = undefined;

/**
 * @member {Boolean} has_previous
 */
GetCuratedPodcastsResponse.prototype['has_previous'] = undefined;

/**
 * @member {Number} next_page_number
 */
GetCuratedPodcastsResponse.prototype['next_page_number'] = undefined;

/**
 * @member {Number} page_number
 */
GetCuratedPodcastsResponse.prototype['page_number'] = undefined;

/**
 * @member {Number} previous_page_number
 */
GetCuratedPodcastsResponse.prototype['previous_page_number'] = undefined;

/**
 * @member {Number} total
 */
GetCuratedPodcastsResponse.prototype['total'] = undefined;






export default GetCuratedPodcastsResponse;

