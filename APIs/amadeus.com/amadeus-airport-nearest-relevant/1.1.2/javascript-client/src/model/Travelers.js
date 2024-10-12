/**
 * Airport Nearest Relevant
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.  Please also be aware that our test environment is based on a subset of the production, this API in test only returns a few selected cities. You can find the list in our **[data collection](https://github.com/amadeus4dev/data-collection)**.
 *
 * The version of the OpenAPI document: 1.1.2
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The Travelers model module.
 * @module model/Travelers
 * @version 1.1.2
 */
class Travelers {
    /**
     * Constructs a new <code>Travelers</code>.
     * @alias module:model/Travelers
     */
    constructor() { 
        
        Travelers.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Travelers</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Travelers} obj Optional instance to populate.
     * @return {module:model/Travelers} The populated <code>Travelers</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Travelers();

            if (data.hasOwnProperty('score')) {
                obj['score'] = ApiClient.convertToType(data['score'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Travelers</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Travelers</code>.
     */
    static validateJSON(data) {

        return true;
    }


}



/**
 * Approximate score for ranking purposes calculated based on number of travelers in the location.
 * @member {Number} score
 */
Travelers.prototype['score'] = undefined;






export default Travelers;

