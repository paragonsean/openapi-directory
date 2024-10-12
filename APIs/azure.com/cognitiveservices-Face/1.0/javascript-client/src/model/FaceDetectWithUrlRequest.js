/**
 * Face Client
 * An API for face detection, verification, and identification.
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The FaceDetectWithUrlRequest model module.
 * @module model/FaceDetectWithUrlRequest
 * @version 1.0
 */
class FaceDetectWithUrlRequest {
    /**
     * Constructs a new <code>FaceDetectWithUrlRequest</code>.
     * @alias module:model/FaceDetectWithUrlRequest
     * @param url {String} Publicly reachable URL of an image
     */
    constructor(url) { 
        
        FaceDetectWithUrlRequest.initialize(this, url);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, url) { 
        obj['url'] = url;
    }

    /**
     * Constructs a <code>FaceDetectWithUrlRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/FaceDetectWithUrlRequest} obj Optional instance to populate.
     * @return {module:model/FaceDetectWithUrlRequest} The populated <code>FaceDetectWithUrlRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new FaceDetectWithUrlRequest();

            if (data.hasOwnProperty('url')) {
                obj['url'] = ApiClient.convertToType(data['url'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>FaceDetectWithUrlRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>FaceDetectWithUrlRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of FaceDetectWithUrlRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['url'] && !(typeof data['url'] === 'string' || data['url'] instanceof String)) {
            throw new Error("Expected the field `url` to be a primitive type in the JSON string but got " + data['url']);
        }

        return true;
    }


}

FaceDetectWithUrlRequest.RequiredProperties = ["url"];

/**
 * Publicly reachable URL of an image
 * @member {String} url
 */
FaceDetectWithUrlRequest.prototype['url'] = undefined;






export default FaceDetectWithUrlRequest;

