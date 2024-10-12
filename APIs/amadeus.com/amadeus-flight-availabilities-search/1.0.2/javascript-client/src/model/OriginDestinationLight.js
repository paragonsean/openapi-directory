/**
 * Flight Availibilities Search
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.0.2
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The OriginDestinationLight model module.
 * @module model/OriginDestinationLight
 * @version 1.0.2
 */
class OriginDestinationLight {
    /**
     * Constructs a new <code>OriginDestinationLight</code>.
     * @alias module:model/OriginDestinationLight
     */
    constructor() { 
        
        OriginDestinationLight.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>OriginDestinationLight</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/OriginDestinationLight} obj Optional instance to populate.
     * @return {module:model/OriginDestinationLight} The populated <code>OriginDestinationLight</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new OriginDestinationLight();

            if (data.hasOwnProperty('destinationLocationCode')) {
                obj['destinationLocationCode'] = ApiClient.convertToType(data['destinationLocationCode'], 'String');
            }
            if (data.hasOwnProperty('excludedConnectionPoints')) {
                obj['excludedConnectionPoints'] = ApiClient.convertToType(data['excludedConnectionPoints'], ['String']);
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('includedConnectionPoints')) {
                obj['includedConnectionPoints'] = ApiClient.convertToType(data['includedConnectionPoints'], ['String']);
            }
            if (data.hasOwnProperty('originLocationCode')) {
                obj['originLocationCode'] = ApiClient.convertToType(data['originLocationCode'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>OriginDestinationLight</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>OriginDestinationLight</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['destinationLocationCode'] && !(typeof data['destinationLocationCode'] === 'string' || data['destinationLocationCode'] instanceof String)) {
            throw new Error("Expected the field `destinationLocationCode` to be a primitive type in the JSON string but got " + data['destinationLocationCode']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['excludedConnectionPoints'])) {
            throw new Error("Expected the field `excludedConnectionPoints` to be an array in the JSON data but got " + data['excludedConnectionPoints']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['includedConnectionPoints'])) {
            throw new Error("Expected the field `includedConnectionPoints` to be an array in the JSON data but got " + data['includedConnectionPoints']);
        }
        // ensure the json data is a string
        if (data['originLocationCode'] && !(typeof data['originLocationCode'] === 'string' || data['originLocationCode'] instanceof String)) {
            throw new Error("Expected the field `originLocationCode` to be a primitive type in the JSON string but got " + data['originLocationCode']);
        }

        return true;
    }


}



/**
 * Destination location, such as a city or an airport. Currently, only the locations defined in [IATA](http://www.iata.org/publications/Pages/code-search.aspx) are supported.
 * @member {String} destinationLocationCode
 */
OriginDestinationLight.prototype['destinationLocationCode'] = undefined;

/**
 * List of excluded connections points. Any FlightOffer with these connections points will be present in response. Currently, only the locations defined in IATA are supported. Used only by the AMADEUS provider
 * @member {Array.<String>} excludedConnectionPoints
 */
OriginDestinationLight.prototype['excludedConnectionPoints'] = undefined;

/**
 * @member {String} id
 */
OriginDestinationLight.prototype['id'] = undefined;

/**
 * List of included connections points. When an includedViaPoints option is specified, all FlightOffer returned must at least go via this Connecting Point. Currently, only the locations defined in IATA are supported. Used only by the AMADEUS provider
 * @member {Array.<String>} includedConnectionPoints
 */
OriginDestinationLight.prototype['includedConnectionPoints'] = undefined;

/**
 * Origin location, such as a city or an airport. Currently, only the locations defined in [IATA](http://www.iata.org/publications/Pages/code-search.aspx) are supported.
 * @member {String} originLocationCode
 */
OriginDestinationLight.prototype['originLocationCode'] = undefined;






export default OriginDestinationLight;

