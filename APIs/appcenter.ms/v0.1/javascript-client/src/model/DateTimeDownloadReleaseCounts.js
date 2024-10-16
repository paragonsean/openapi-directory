/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import DateTimeDownloadReleaseCountsCountsInner from './DateTimeDownloadReleaseCountsCountsInner';

/**
 * The DateTimeDownloadReleaseCounts model module.
 * @module model/DateTimeDownloadReleaseCounts
 * @version v0.1
 */
class DateTimeDownloadReleaseCounts {
    /**
     * Constructs a new <code>DateTimeDownloadReleaseCounts</code>.
     * @alias module:model/DateTimeDownloadReleaseCounts
     */
    constructor() { 
        
        DateTimeDownloadReleaseCounts.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>DateTimeDownloadReleaseCounts</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/DateTimeDownloadReleaseCounts} obj Optional instance to populate.
     * @return {module:model/DateTimeDownloadReleaseCounts} The populated <code>DateTimeDownloadReleaseCounts</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new DateTimeDownloadReleaseCounts();

            if (data.hasOwnProperty('counts')) {
                obj['counts'] = ApiClient.convertToType(data['counts'], [DateTimeDownloadReleaseCountsCountsInner]);
            }
            if (data.hasOwnProperty('total')) {
                obj['total'] = ApiClient.convertToType(data['total'], 'Number');
            }
            if (data.hasOwnProperty('unique')) {
                obj['unique'] = ApiClient.convertToType(data['unique'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>DateTimeDownloadReleaseCounts</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>DateTimeDownloadReleaseCounts</code>.
     */
    static validateJSON(data) {
        if (data['counts']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['counts'])) {
                throw new Error("Expected the field `counts` to be an array in the JSON data but got " + data['counts']);
            }
            // validate the optional field `counts` (array)
            for (const item of data['counts']) {
                DateTimeDownloadReleaseCountsCountsInner.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * Release counts per day.
 * @member {Array.<module:model/DateTimeDownloadReleaseCountsCountsInner>} counts
 */
DateTimeDownloadReleaseCounts.prototype['counts'] = undefined;

/**
 * @member {Number} total
 */
DateTimeDownloadReleaseCounts.prototype['total'] = undefined;

/**
 * @member {Number} unique
 */
DateTimeDownloadReleaseCounts.prototype['unique'] = undefined;






export default DateTimeDownloadReleaseCounts;

