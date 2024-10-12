/**
 * Flight Check-in Links
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.  Please also be aware that our test environment is based on a subset of the production, to see what is included in test please refer to our **[data collection](https://github.com/amadeus4dev/data-collection)**.
 *
 * The version of the OpenAPI document: 2.1.2
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import CollectionLinks from './CollectionLinks';

/**
 * The CollectionMeta model module.
 * @module model/CollectionMeta
 * @version 2.1.2
 */
class CollectionMeta {
    /**
     * Constructs a new <code>CollectionMeta</code>.
     * @alias module:model/CollectionMeta
     */
    constructor() { 
        
        CollectionMeta.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>CollectionMeta</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CollectionMeta} obj Optional instance to populate.
     * @return {module:model/CollectionMeta} The populated <code>CollectionMeta</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CollectionMeta();

            if (data.hasOwnProperty('count')) {
                obj['count'] = ApiClient.convertToType(data['count'], 'Number');
            }
            if (data.hasOwnProperty('links')) {
                obj['links'] = CollectionLinks.constructFromObject(data['links']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CollectionMeta</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CollectionMeta</code>.
     */
    static validateJSON(data) {
        // validate the optional field `links`
        if (data['links']) { // data not null
          CollectionLinks.validateJSON(data['links']);
        }

        return true;
    }


}



/**
 * @member {Number} count
 */
CollectionMeta.prototype['count'] = undefined;

/**
 * @member {module:model/CollectionLinks} links
 */
CollectionMeta.prototype['links'] = undefined;






export default CollectionMeta;

