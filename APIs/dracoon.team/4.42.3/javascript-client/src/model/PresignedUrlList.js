/**
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import PresignedUrl from './PresignedUrl';

/**
 * The PresignedUrlList model module.
 * @module model/PresignedUrlList
 * @version 4.42.3
 */
class PresignedUrlList {
    /**
     * Constructs a new <code>PresignedUrlList</code>.
     * List of generated presigned URLs
     * @alias module:model/PresignedUrlList
     * @param urls {Array.<module:model/PresignedUrl>} List of S3 presigned URLs
     */
    constructor(urls) { 
        
        PresignedUrlList.initialize(this, urls);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, urls) { 
        obj['urls'] = urls;
    }

    /**
     * Constructs a <code>PresignedUrlList</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PresignedUrlList} obj Optional instance to populate.
     * @return {module:model/PresignedUrlList} The populated <code>PresignedUrlList</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PresignedUrlList();

            if (data.hasOwnProperty('urls')) {
                obj['urls'] = ApiClient.convertToType(data['urls'], [PresignedUrl]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PresignedUrlList</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PresignedUrlList</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of PresignedUrlList.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        if (data['urls']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['urls'])) {
                throw new Error("Expected the field `urls` to be an array in the JSON data but got " + data['urls']);
            }
            // validate the optional field `urls` (array)
            for (const item of data['urls']) {
                PresignedUrl.validateJSON(item);
            };
        }

        return true;
    }


}

PresignedUrlList.RequiredProperties = ["urls"];

/**
 * List of S3 presigned URLs
 * @member {Array.<module:model/PresignedUrl>} urls
 */
PresignedUrlList.prototype['urls'] = undefined;






export default PresignedUrlList;

