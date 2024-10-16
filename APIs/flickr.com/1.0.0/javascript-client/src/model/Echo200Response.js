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
 * The Echo200Response model module.
 * @module model/Echo200Response
 * @version 1.0.0
 */
class Echo200Response {
    /**
     * Constructs a new <code>Echo200Response</code>.
     * @alias module:model/Echo200Response
     */
    constructor() { 
        
        Echo200Response.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Echo200Response</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Echo200Response} obj Optional instance to populate.
     * @return {module:model/Echo200Response} The populated <code>Echo200Response</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Echo200Response();

            if (data.hasOwnProperty('echo')) {
                obj['echo'] = GetFavoritesContextByID200ResponseCount.constructFromObject(data['echo']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Echo200Response</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Echo200Response</code>.
     */
    static validateJSON(data) {
        // validate the optional field `echo`
        if (data['echo']) { // data not null
          GetFavoritesContextByID200ResponseCount.validateJSON(data['echo']);
        }

        return true;
    }


}



/**
 * @member {module:model/GetFavoritesContextByID200ResponseCount} echo
 */
Echo200Response.prototype['echo'] = undefined;






export default Echo200Response;

