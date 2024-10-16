/**
 * CallFire API Documentation
 * CallFire
 *
 * The version of the OpenAPI document: V2
 * Contact: support@callfire.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import CallRecording from './CallRecording';
import ItemList from './ItemList';

/**
 * The CallRecordingList model module.
 * @module model/CallRecordingList
 * @version V2
 */
class CallRecordingList {
    /**
     * Constructs a new <code>CallRecordingList</code>.
     * ~
     * @alias module:model/CallRecordingList
     * @implements module:model/ItemList
     */
    constructor() { 
        ItemList.initialize(this);
        CallRecordingList.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>CallRecordingList</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CallRecordingList} obj Optional instance to populate.
     * @return {module:model/CallRecordingList} The populated <code>CallRecordingList</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CallRecordingList();
            ItemList.constructFromObject(data, obj);

            if (data.hasOwnProperty('items')) {
                obj['items'] = ApiClient.convertToType(data['items'], [CallRecording]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CallRecordingList</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CallRecordingList</code>.
     */
    static validateJSON(data) {
        if (data['items']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['items'])) {
                throw new Error("Expected the field `items` to be an array in the JSON data but got " + data['items']);
            }
            // validate the optional field `items` (array)
            for (const item of data['items']) {
                CallRecording.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {Array.<module:model/CallRecording>} items
 */
CallRecordingList.prototype['items'] = undefined;


// Implement ItemList interface:
/**
 * ~
 * @member {Array.<Object>} items
 */
ItemList.prototype['items'] = undefined;




export default CallRecordingList;

