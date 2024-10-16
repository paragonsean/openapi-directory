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

/**
 * The TestRunStatistics model module.
 * @module model/TestRunStatistics
 * @version v0.1
 */
class TestRunStatistics {
    /**
     * Constructs a new <code>TestRunStatistics</code>.
     * Summary single test run on Xamarin Test Cloud
     * @alias module:model/TestRunStatistics
     */
    constructor() { 
        
        TestRunStatistics.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>TestRunStatistics</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TestRunStatistics} obj Optional instance to populate.
     * @return {module:model/TestRunStatistics} The populated <code>TestRunStatistics</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TestRunStatistics();

            if (data.hasOwnProperty('devices')) {
                obj['devices'] = ApiClient.convertToType(data['devices'], 'Number');
            }
            if (data.hasOwnProperty('devicesFailed')) {
                obj['devicesFailed'] = ApiClient.convertToType(data['devicesFailed'], 'Number');
            }
            if (data.hasOwnProperty('devicesFinished')) {
                obj['devicesFinished'] = ApiClient.convertToType(data['devicesFinished'], 'Number');
            }
            if (data.hasOwnProperty('failed')) {
                obj['failed'] = ApiClient.convertToType(data['failed'], 'Number');
            }
            if (data.hasOwnProperty('passed')) {
                obj['passed'] = ApiClient.convertToType(data['passed'], 'Number');
            }
            if (data.hasOwnProperty('peakMemory')) {
                obj['peakMemory'] = ApiClient.convertToType(data['peakMemory'], 'Number');
            }
            if (data.hasOwnProperty('skipped')) {
                obj['skipped'] = ApiClient.convertToType(data['skipped'], 'Number');
            }
            if (data.hasOwnProperty('total')) {
                obj['total'] = ApiClient.convertToType(data['total'], 'Number');
            }
            if (data.hasOwnProperty('totalDeviceMinutes')) {
                obj['totalDeviceMinutes'] = ApiClient.convertToType(data['totalDeviceMinutes'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>TestRunStatistics</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>TestRunStatistics</code>.
     */
    static validateJSON(data) {

        return true;
    }


}



/**
 * Number of devices running the test
 * @member {Number} devices
 */
TestRunStatistics.prototype['devices'] = undefined;

/**
 * Number of failed devices
 * @member {Number} devicesFailed
 */
TestRunStatistics.prototype['devicesFailed'] = undefined;

/**
 * Number of finished devices
 * @member {Number} devicesFinished
 */
TestRunStatistics.prototype['devicesFinished'] = undefined;

/**
 * Number of failed tests
 * @member {Number} failed
 */
TestRunStatistics.prototype['failed'] = undefined;

/**
 * Number of passed tests
 * @member {Number} passed
 */
TestRunStatistics.prototype['passed'] = undefined;

/**
 * The max amount of MB used during the test run
 * @member {Number} peakMemory
 */
TestRunStatistics.prototype['peakMemory'] = undefined;

/**
 * Number of skipped tests
 * @member {Number} skipped
 */
TestRunStatistics.prototype['skipped'] = undefined;

/**
 * Number of tests in total
 * @member {Number} total
 */
TestRunStatistics.prototype['total'] = undefined;

/**
 * The number of minutes of device time the test has been runnign
 * @member {Number} totalDeviceMinutes
 */
TestRunStatistics.prototype['totalDeviceMinutes'] = undefined;






export default TestRunStatistics;

