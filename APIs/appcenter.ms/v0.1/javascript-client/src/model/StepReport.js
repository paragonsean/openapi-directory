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
import StepReportDeviceScreenshotsInner from './StepReportDeviceScreenshotsInner';

/**
 * The StepReport model module.
 * @module model/StepReport
 * @version v0.1
 */
class StepReport {
    /**
     * Constructs a new <code>StepReport</code>.
     * @alias module:model/StepReport
     * @param deviceScreenshots {Array.<module:model/StepReportDeviceScreenshotsInner>} 
     * @param finishedSnapshots {Array.<String>} 
     */
    constructor(deviceScreenshots, finishedSnapshots) { 
        
        StepReport.initialize(this, deviceScreenshots, finishedSnapshots);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, deviceScreenshots, finishedSnapshots) { 
        obj['deviceScreenshots'] = deviceScreenshots;
        obj['finishedSnapshots'] = finishedSnapshots;
    }

    /**
     * Constructs a <code>StepReport</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/StepReport} obj Optional instance to populate.
     * @return {module:model/StepReport} The populated <code>StepReport</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new StepReport();

            if (data.hasOwnProperty('deviceScreenshots')) {
                obj['deviceScreenshots'] = ApiClient.convertToType(data['deviceScreenshots'], [StepReportDeviceScreenshotsInner]);
            }
            if (data.hasOwnProperty('finishedSnapshots')) {
                obj['finishedSnapshots'] = ApiClient.convertToType(data['finishedSnapshots'], ['String']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>StepReport</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>StepReport</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of StepReport.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        if (data['deviceScreenshots']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['deviceScreenshots'])) {
                throw new Error("Expected the field `deviceScreenshots` to be an array in the JSON data but got " + data['deviceScreenshots']);
            }
            // validate the optional field `deviceScreenshots` (array)
            for (const item of data['deviceScreenshots']) {
                StepReportDeviceScreenshotsInner.validateJSON(item);
            };
        }
        // ensure the json data is an array
        if (!Array.isArray(data['finishedSnapshots'])) {
            throw new Error("Expected the field `finishedSnapshots` to be an array in the JSON data but got " + data['finishedSnapshots']);
        }

        return true;
    }


}

StepReport.RequiredProperties = ["deviceScreenshots", "finishedSnapshots"];

/**
 * @member {Array.<module:model/StepReportDeviceScreenshotsInner>} deviceScreenshots
 */
StepReport.prototype['deviceScreenshots'] = undefined;

/**
 * @member {Array.<String>} finishedSnapshots
 */
StepReport.prototype['finishedSnapshots'] = undefined;






export default StepReport;

