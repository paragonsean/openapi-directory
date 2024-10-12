/**
 * LinQR
 * This is LinQR QR Code API documentation. This API allows you to generate custom, visually attractive QR Codes. The cloud infrastructure guarantees high availability and autoscalability of the service. You can generate hundreds of thousands of images this way and use them however you like.  We realize that your API use case may require custom solutions, and perhaps we lack functionality that is very important to you. In that case feel free to write an email to our support and tell us about it. We have repeatedly added new functions of our service directly after the requests of our users.  **General remarks:**  - maximum request size is fixed at 32MB.  - request timeout is fixed at 180 seconds.
 *
 * The version of the OpenAPI document: 2.0
 * Contact: support@linqr.app
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import GeolocationUriFormat from './GeolocationUriFormat';

/**
 * The GeolocationData model module.
 * @module model/GeolocationData
 * @version 2.0
 */
class GeolocationData {
    /**
     * Constructs a new <code>GeolocationData</code>.
     * @alias module:model/GeolocationData
     * @param latitude {Number} Location latitude.
     * @param longitude {Number} Location longitude.
     */
    constructor(latitude, longitude) { 
        
        GeolocationData.initialize(this, latitude, longitude);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, latitude, longitude) { 
        obj['latitude'] = latitude;
        obj['longitude'] = longitude;
    }

    /**
     * Constructs a <code>GeolocationData</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GeolocationData} obj Optional instance to populate.
     * @return {module:model/GeolocationData} The populated <code>GeolocationData</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GeolocationData();

            if (data.hasOwnProperty('format')) {
                obj['format'] = ApiClient.convertToType(data['format'], GeolocationUriFormat);
            }
            if (data.hasOwnProperty('latitude')) {
                obj['latitude'] = ApiClient.convertToType(data['latitude'], 'Number');
            }
            if (data.hasOwnProperty('longitude')) {
                obj['longitude'] = ApiClient.convertToType(data['longitude'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GeolocationData</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GeolocationData</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of GeolocationData.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }

        return true;
    }


}

GeolocationData.RequiredProperties = ["latitude", "longitude"];

/**
 * URI format.  - `rfc5870` data encoded according to <a href=\"https://datatracker.ietf.org/doc/html/rfc5870\" rel=\"noopener noreferrer\" target=\"_blank\" >RFC5870 standard</a>  - `google` data encoded according to <a href=\"https://developers.google.com/maps/documentation/urls/android-intents\" rel=\"noopener noreferrer\" target=\"_blank\" >Google Maps standard</a>
 * @member {module:model/GeolocationUriFormat} format
 */
GeolocationData.prototype['format'] = undefined;

/**
 * Location latitude.
 * @member {Number} latitude
 */
GeolocationData.prototype['latitude'] = undefined;

/**
 * Location longitude.
 * @member {Number} longitude
 */
GeolocationData.prototype['longitude'] = undefined;






export default GeolocationData;

