/**
 * Travel Recommendations API
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.
 *
 * The version of the OpenAPI document: 1.0.3
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import Links from './Links';

/**
 * The Meta model module.
 * @module model/Meta
 * @version 1.0.3
 */
class Meta {
    /**
     * Constructs a new <code>Meta</code>.
     * Meta information about the returned object(s) in \&quot;data\&quot;
     * @alias module:model/Meta
     */
    constructor() { 
        
        Meta.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Meta</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Meta} obj Optional instance to populate.
     * @return {module:model/Meta} The populated <code>Meta</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Meta();

            if (data.hasOwnProperty('count')) {
                obj['count'] = ApiClient.convertToType(data['count'], 'Number');
            }
            if (data.hasOwnProperty('links')) {
                obj['links'] = Links.constructFromObject(data['links']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Meta</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Meta</code>.
     */
    static validateJSON(data) {
        // validate the optional field `links`
        if (data['links']) { // data not null
          Links.validateJSON(data['links']);
        }

        return true;
    }


}



/**
 * Total number of object(s) retrieved
 * @member {Number} count
 */
Meta.prototype['count'] = undefined;

/**
 * @member {module:model/Links} links
 */
Meta.prototype['links'] = undefined;






export default Meta;

