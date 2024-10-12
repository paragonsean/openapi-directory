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
import GetFavoritesContextByID200ResponseCount from './GetFavoritesContextByID200ResponseCount';

/**
 * The PersonPhotos model module.
 * @module model/PersonPhotos
 * @version 1.0.0
 */
class PersonPhotos {
    /**
     * Constructs a new <code>PersonPhotos</code>.
     * @alias module:model/PersonPhotos
     */
    constructor() { 
        
        PersonPhotos.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PersonPhotos</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PersonPhotos} obj Optional instance to populate.
     * @return {module:model/PersonPhotos} The populated <code>PersonPhotos</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PersonPhotos();

            if (data.hasOwnProperty('count')) {
                obj['count'] = GetFavoritesContextByID200ResponseCount.constructFromObject(data['count']);
            }
            if (data.hasOwnProperty('firstdate')) {
                obj['firstdate'] = GetFavoritesContextByID200ResponseCount.constructFromObject(data['firstdate']);
            }
            if (data.hasOwnProperty('firstdatetaken')) {
                obj['firstdatetaken'] = GetFavoritesContextByID200ResponseCount.constructFromObject(data['firstdatetaken']);
            }
            if (data.hasOwnProperty('views')) {
                obj['views'] = GetFavoritesContextByID200ResponseCount.constructFromObject(data['views']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PersonPhotos</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PersonPhotos</code>.
     */
    static validateJSON(data) {
        // validate the optional field `count`
        if (data['count']) { // data not null
          GetFavoritesContextByID200ResponseCount.validateJSON(data['count']);
        }
        // validate the optional field `firstdate`
        if (data['firstdate']) { // data not null
          GetFavoritesContextByID200ResponseCount.validateJSON(data['firstdate']);
        }
        // validate the optional field `firstdatetaken`
        if (data['firstdatetaken']) { // data not null
          GetFavoritesContextByID200ResponseCount.validateJSON(data['firstdatetaken']);
        }
        // validate the optional field `views`
        if (data['views']) { // data not null
          GetFavoritesContextByID200ResponseCount.validateJSON(data['views']);
        }

        return true;
    }


}



/**
 * @member {module:model/GetFavoritesContextByID200ResponseCount} count
 */
PersonPhotos.prototype['count'] = undefined;

/**
 * @member {module:model/GetFavoritesContextByID200ResponseCount} firstdate
 */
PersonPhotos.prototype['firstdate'] = undefined;

/**
 * @member {module:model/GetFavoritesContextByID200ResponseCount} firstdatetaken
 */
PersonPhotos.prototype['firstdatetaken'] = undefined;

/**
 * @member {module:model/GetFavoritesContextByID200ResponseCount} views
 */
PersonPhotos.prototype['views'] = undefined;






export default PersonPhotos;

