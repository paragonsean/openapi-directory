/**
 * Flight Most Traveled Destinations
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.  Please also be aware that our test environment is based on a subset of the production, this API in test only returns a few selected cities. You can find the list in our **[data collection](https://github.com/amadeus4dev/data-collection)**.
 *
 * The version of the OpenAPI document: 1.1.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import Flights from './Flights';
import Travelers from './Travelers';

/**
 * The Analytics model module.
 * @module model/Analytics
 * @version 1.1.1
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

            if (data.hasOwnProperty('flights')) {
                obj['flights'] = Flights.constructFromObject(data['flights']);
            }
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
        // validate the optional field `flights`
        if (data['flights']) { // data not null
          Flights.validateJSON(data['flights']);
        }
        // validate the optional field `travelers`
        if (data['travelers']) { // data not null
          Travelers.validateJSON(data['travelers']);
        }

        return true;
    }


}



/**
 * @member {module:model/Flights} flights
 */
Analytics.prototype['flights'] = undefined;

/**
 * @member {module:model/Travelers} travelers
 */
Analytics.prototype['travelers'] = undefined;






export default Analytics;

