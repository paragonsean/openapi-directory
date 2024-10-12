/**
 * Airport & City Search
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, in test this API only contains data from the United States, Spain, United Kingdom, Germany and India. 
 *
 * The version of the OpenAPI document: 1.2.3
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import Travelers from './Travelers';

/**
 * The Analytics model module.
 * @module model/Analytics
 * @version 1.2.3
 */
class Analytics {
    /**
     * Constructs a new <code>Analytics</code>.
     * @alias module:model/Analytics
     */
    constructor() { 
        
        Analytics.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Analytics</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Analytics} obj Optional instance to populate.
     * @return {module:model/Analytics} The populated <code>Analytics</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Analytics();

            if (data.hasOwnProperty('travelers')) {
                obj['travelers'] = Travelers.constructFromObject(data['travelers']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Analytics</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Analytics</code>.
     */
    static validateJSON(data) {
        // validate the optional field `travelers`
        if (data['travelers']) { // data not null
          Travelers.validateJSON(data['travelers']);
        }

        return true;
    }


}



/**
 * @member {module:model/Travelers} travelers
 */
Analytics.prototype['travelers'] = undefined;






export default Analytics;

