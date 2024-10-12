/**
 * Hotel Booking
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production for this API it may change dynamically. For your tests, use big cities like LON (London) or NYC (New-York).   **Warning: Do not perform test booking in production**. All requests are sent and processed by hotel providers. An excessive amount of fake/canceled reservation will make you blacklisted by hotel providers. 
 *
 * The version of the OpenAPI document: 1.1.3
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import HotelBookingQuery from './HotelBookingQuery';

/**
 * The BookingSchema model module.
 * @module model/BookingSchema
 * @version 1.1.3
 */
class BookingSchema {
    /**
     * Constructs a new <code>BookingSchema</code>.
     * @alias module:model/BookingSchema
     * @param data {module:model/HotelBookingQuery} 
     */
    constructor(data) { 
        
        BookingSchema.initialize(this, data);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, data) { 
        obj['data'] = data;
    }

    /**
     * Constructs a <code>BookingSchema</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/BookingSchema} obj Optional instance to populate.
     * @return {module:model/BookingSchema} The populated <code>BookingSchema</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new BookingSchema();

            if (data.hasOwnProperty('data')) {
                obj['data'] = HotelBookingQuery.constructFromObject(data['data']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>BookingSchema</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>BookingSchema</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of BookingSchema.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `data`
        if (data['data']) { // data not null
          HotelBookingQuery.validateJSON(data['data']);
        }

        return true;
    }


}

BookingSchema.RequiredProperties = ["data"];

/**
 * @member {module:model/HotelBookingQuery} data
 */
BookingSchema.prototype['data'] = undefined;






export default BookingSchema;

