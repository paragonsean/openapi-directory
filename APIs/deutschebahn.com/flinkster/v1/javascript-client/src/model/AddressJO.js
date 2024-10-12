/**
 * Flinkster_API_NG
 * This REST-API enables you to query for private transport sharing offers provided by companies and cities in Germany, Netherland and Austria.  You can search for informations about the rental stations (points or areas) where you can find the rentals by utilizing the /areas/ ressource.  With the help of the proximity search in the /bookingproposals/ URI you can request the availabilities of the rentalobjects for spontaneous or planed usage in the future.   Feel free to browse through data by setting the parameter 'providernetwork' to the value:   1: Search for car sharing offers provided by the Flinkster platform (http://www.flinkster.de) 2: Finding bike rental offers from Call a Bike (http://www.callabike.de)   You can find more details in the documentation section (Unfortunately only available in german language).  Have lots of fun and we are lucky to take notice of your products or getting your feedback.
 *
 * The version of the OpenAPI document: v1
 * Contact: partner@flinkster.de
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The AddressJO model module.
 * @module model/AddressJO
 * @version v1
 */
class AddressJO {
    /**
     * Constructs a new <code>AddressJO</code>.
     * @alias module:model/AddressJO
     */
    constructor() { 
        
        AddressJO.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>AddressJO</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AddressJO} obj Optional instance to populate.
     * @return {module:model/AddressJO} The populated <code>AddressJO</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AddressJO();

            if (data.hasOwnProperty('city')) {
                obj['city'] = ApiClient.convertToType(data['city'], 'String');
            }
            if (data.hasOwnProperty('district')) {
                obj['district'] = ApiClient.convertToType(data['district'], 'String');
            }
            if (data.hasOwnProperty('isoCountryCode')) {
                obj['isoCountryCode'] = ApiClient.convertToType(data['isoCountryCode'], 'String');
            }
            if (data.hasOwnProperty('number')) {
                obj['number'] = ApiClient.convertToType(data['number'], 'String');
            }
            if (data.hasOwnProperty('street')) {
                obj['street'] = ApiClient.convertToType(data['street'], 'String');
            }
            if (data.hasOwnProperty('zip')) {
                obj['zip'] = ApiClient.convertToType(data['zip'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AddressJO</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AddressJO</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['city'] && !(typeof data['city'] === 'string' || data['city'] instanceof String)) {
            throw new Error("Expected the field `city` to be a primitive type in the JSON string but got " + data['city']);
        }
        // ensure the json data is a string
        if (data['district'] && !(typeof data['district'] === 'string' || data['district'] instanceof String)) {
            throw new Error("Expected the field `district` to be a primitive type in the JSON string but got " + data['district']);
        }
        // ensure the json data is a string
        if (data['isoCountryCode'] && !(typeof data['isoCountryCode'] === 'string' || data['isoCountryCode'] instanceof String)) {
            throw new Error("Expected the field `isoCountryCode` to be a primitive type in the JSON string but got " + data['isoCountryCode']);
        }
        // ensure the json data is a string
        if (data['number'] && !(typeof data['number'] === 'string' || data['number'] instanceof String)) {
            throw new Error("Expected the field `number` to be a primitive type in the JSON string but got " + data['number']);
        }
        // ensure the json data is a string
        if (data['street'] && !(typeof data['street'] === 'string' || data['street'] instanceof String)) {
            throw new Error("Expected the field `street` to be a primitive type in the JSON string but got " + data['street']);
        }
        // ensure the json data is a string
        if (data['zip'] && !(typeof data['zip'] === 'string' || data['zip'] instanceof String)) {
            throw new Error("Expected the field `zip` to be a primitive type in the JSON string but got " + data['zip']);
        }

        return true;
    }


}



/**
 * @member {String} city
 */
AddressJO.prototype['city'] = undefined;

/**
 * @member {String} district
 */
AddressJO.prototype['district'] = undefined;

/**
 * @member {String} isoCountryCode
 */
AddressJO.prototype['isoCountryCode'] = undefined;

/**
 * @member {String} number
 */
AddressJO.prototype['number'] = undefined;

/**
 * @member {String} street
 */
AddressJO.prototype['street'] = undefined;

/**
 * @member {String} zip
 */
AddressJO.prototype['zip'] = undefined;






export default AddressJO;

