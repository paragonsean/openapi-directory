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
import PlayedInLinksPlayedIn from './PlayedInLinksPlayedIn';

/**
 * The PlayedInLinks model module.
 * @module model/PlayedInLinks
 * @version 1.0.0
 */
class PlayedInLinks {
    /**
     * Constructs a new <code>PlayedInLinks</code>.
     * @alias module:model/PlayedInLinks
     */
    constructor() { 
        
        PlayedInLinks.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PlayedInLinks</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PlayedInLinks} obj Optional instance to populate.
     * @return {module:model/PlayedInLinks} The populated <code>PlayedInLinks</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PlayedInLinks();

            if (data.hasOwnProperty('played_in')) {
                obj['played_in'] = PlayedInLinksPlayedIn.constructFromObject(data['played_in']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PlayedInLinks</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PlayedInLinks</code>.
     */
    static validateJSON(data) {
        // validate the optional field `played_in`
        if (data['played_in']) { // data not null
          PlayedInLinksPlayedIn.validateJSON(data['played_in']);
        }

        return true;
    }


}



/**
 * @member {module:model/PlayedInLinksPlayedIn} played_in
 */
PlayedInLinks.prototype['played_in'] = undefined;






export default PlayedInLinks;

