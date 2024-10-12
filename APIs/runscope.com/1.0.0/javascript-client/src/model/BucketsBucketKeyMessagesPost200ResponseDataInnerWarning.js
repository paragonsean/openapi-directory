/**
 * Runscope API
 * Manage Runscope programmatically.
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The BucketsBucketKeyMessagesPost200ResponseDataInnerWarning model module.
 * @module model/BucketsBucketKeyMessagesPost200ResponseDataInnerWarning
 * @version 1.0.0
 */
class BucketsBucketKeyMessagesPost200ResponseDataInnerWarning {
    /**
     * Constructs a new <code>BucketsBucketKeyMessagesPost200ResponseDataInnerWarning</code>.
     * An object representing warnings (non-fatal warnings) for this item. Only present if status is warning, otherwise this will be null.
     * @alias module:model/BucketsBucketKeyMessagesPost200ResponseDataInnerWarning
     */
    constructor() { 
        
        BucketsBucketKeyMessagesPost200ResponseDataInnerWarning.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>BucketsBucketKeyMessagesPost200ResponseDataInnerWarning</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/BucketsBucketKeyMessagesPost200ResponseDataInnerWarning} obj Optional instance to populate.
     * @return {module:model/BucketsBucketKeyMessagesPost200ResponseDataInnerWarning} The populated <code>BucketsBucketKeyMessagesPost200ResponseDataInnerWarning</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new BucketsBucketKeyMessagesPost200ResponseDataInnerWarning();

            if (data.hasOwnProperty('code')) {
                obj['code'] = ApiClient.convertToType(data['code'], 'Number');
            }
            if (data.hasOwnProperty('message')) {
                obj['message'] = ApiClient.convertToType(data['message'], 'String');
            }
            if (data.hasOwnProperty('more_info')) {
                obj['more_info'] = ApiClient.convertToType(data['more_info'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>BucketsBucketKeyMessagesPost200ResponseDataInnerWarning</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>BucketsBucketKeyMessagesPost200ResponseDataInnerWarning</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['message'] && !(typeof data['message'] === 'string' || data['message'] instanceof String)) {
            throw new Error("Expected the field `message` to be a primitive type in the JSON string but got " + data['message']);
        }
        // ensure the json data is a string
        if (data['more_info'] && !(typeof data['more_info'] === 'string' || data['more_info'] instanceof String)) {
            throw new Error("Expected the field `more_info` to be a primitive type in the JSON string but got " + data['more_info']);
        }

        return true;
    }


}



/**
 * A numeric error code for the specific problem we encountered with this message. (warning status only)
 * @member {Number} code
 */
BucketsBucketKeyMessagesPost200ResponseDataInnerWarning.prototype['code'] = undefined;

/**
 * A description of the problem we encountered with this message. (warning status only)
 * @member {String} message
 */
BucketsBucketKeyMessagesPost200ResponseDataInnerWarning.prototype['message'] = undefined;

/**
 * A link to more help about the warning. (warning status only)
 * @member {String} more_info
 */
BucketsBucketKeyMessagesPost200ResponseDataInnerWarning.prototype['more_info'] = undefined;






export default BucketsBucketKeyMessagesPost200ResponseDataInnerWarning;

