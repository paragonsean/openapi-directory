/**
 * MonitorManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2015-04-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import EventData from './EventData';

/**
 * The EventDataCollection model module.
 * @module model/EventDataCollection
 * @version 2015-04-01
 */
class EventDataCollection {
    /**
     * Constructs a new <code>EventDataCollection</code>.
     * Represents collection of events.
     * @alias module:model/EventDataCollection
     * @param value {Array.<module:model/EventData>} this list that includes the Azure audit logs.
     */
    constructor(value) { 
        
        EventDataCollection.initialize(this, value);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, value) { 
        obj['value'] = value;
    }

    /**
     * Constructs a <code>EventDataCollection</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/EventDataCollection} obj Optional instance to populate.
     * @return {module:model/EventDataCollection} The populated <code>EventDataCollection</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new EventDataCollection();

            if (data.hasOwnProperty('nextLink')) {
                obj['nextLink'] = ApiClient.convertToType(data['nextLink'], 'String');
            }
            if (data.hasOwnProperty('value')) {
                obj['value'] = ApiClient.convertToType(data['value'], [EventData]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>EventDataCollection</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>EventDataCollection</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of EventDataCollection.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['nextLink'] && !(typeof data['nextLink'] === 'string' || data['nextLink'] instanceof String)) {
            throw new Error("Expected the field `nextLink` to be a primitive type in the JSON string but got " + data['nextLink']);
        }
        if (data['value']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['value'])) {
                throw new Error("Expected the field `value` to be an array in the JSON data but got " + data['value']);
            }
            // validate the optional field `value` (array)
            for (const item of data['value']) {
                EventData.validateJSON(item);
            };
        }

        return true;
    }


}

EventDataCollection.RequiredProperties = ["value"];

/**
 * Provides the link to retrieve the next set of events.
 * @member {String} nextLink
 */
EventDataCollection.prototype['nextLink'] = undefined;

/**
 * this list that includes the Azure audit logs.
 * @member {Array.<module:model/EventData>} value
 */
EventDataCollection.prototype['value'] = undefined;






export default EventDataCollection;

