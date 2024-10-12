/**
 * BBC Nitro API
 * BBC Nitro is the BBC's application programming interface (API) for BBC Programmes Metadata.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: nitro@bbc.co.uk
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import Deprecations from './Deprecations';
import Feed from './Feed';

/**
 * The Feeds model module.
 * @module model/Feeds
 * @version 1.0.0
 */
class Feeds {
    /**
     * Constructs a new <code>Feeds</code>.
     * @alias module:model/Feeds
     */
    constructor() { 
        
        Feeds.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Feeds</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Feeds} obj Optional instance to populate.
     * @return {module:model/Feeds} The populated <code>Feeds</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Feeds();

            if (data.hasOwnProperty('deployment_root')) {
                obj['deployment_root'] = ApiClient.convertToType(data['deployment_root'], 'String');
            }
            if (data.hasOwnProperty('deprecations')) {
                obj['deprecations'] = Deprecations.constructFromObject(data['deprecations']);
            }
            if (data.hasOwnProperty('feed')) {
                obj['feed'] = ApiClient.convertToType(data['feed'], [Feed]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Feeds</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Feeds</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['deployment_root'] && !(typeof data['deployment_root'] === 'string' || data['deployment_root'] instanceof String)) {
            throw new Error("Expected the field `deployment_root` to be a primitive type in the JSON string but got " + data['deployment_root']);
        }
        // validate the optional field `deprecations`
        if (data['deprecations']) { // data not null
          Deprecations.validateJSON(data['deprecations']);
        }
        if (data['feed']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['feed'])) {
                throw new Error("Expected the field `feed` to be an array in the JSON data but got " + data['feed']);
            }
            // validate the optional field `feed` (array)
            for (const item of data['feed']) {
                Feed.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {String} deployment_root
 */
Feeds.prototype['deployment_root'] = undefined;

/**
 * @member {module:model/Deprecations} deprecations
 */
Feeds.prototype['deprecations'] = undefined;

/**
 * @member {Array.<module:model/Feed>} feed
 */
Feeds.prototype['feed'] = undefined;






export default Feeds;

