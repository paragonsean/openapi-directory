/**
 * Cloud-RF API
 * Use this JSON API to build and test radio links for any radio, anywhere. Authenticate with your API2.0 key in the request header as key
 *
 * The version of the OpenAPI document: 2.0.0
 * Contact: support@cloudrf.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The Point model module.
 * @module model/Point
 * @version 2.0.0
 */
class Point {
    /**
     * Constructs a new <code>Point</code>.
     * @alias module:model/Point
     */
    constructor() { 
        
        Point.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
        obj['alt'] = 1;
        obj['lat'] = 38.916;
        obj['lon'] = 1.411;
    }

    /**
     * Constructs a <code>Point</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Point} obj Optional instance to populate.
     * @return {module:model/Point} The populated <code>Point</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Point();

            if (data.hasOwnProperty('alt')) {
                obj['alt'] = ApiClient.convertToType(data['alt'], 'Number');
            }
            if (data.hasOwnProperty('lat')) {
                obj['lat'] = ApiClient.convertToType(data['lat'], 'Number');
            }
            if (data.hasOwnProperty('lon')) {
                obj['lon'] = ApiClient.convertToType(data['lon'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Point</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Point</code>.
     */
    static validateJSON(data) {

        return true;
    }


}



/**
 * Altitude above ground level in metres OR feet
 * @member {Number} alt
 * @default 1
 */
Point.prototype['alt'] = 1;

/**
 * Latitude in decimal degrees
 * @member {Number} lat
 * @default 38.916
 */
Point.prototype['lat'] = 38.916;

/**
 * Longitude in decimal degrees
 * @member {Number} lon
 * @default 1.411
 */
Point.prototype['lon'] = 1.411;






export default Point;

