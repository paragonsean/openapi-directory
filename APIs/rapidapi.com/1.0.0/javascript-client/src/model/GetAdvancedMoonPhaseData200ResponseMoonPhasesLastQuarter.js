/**
 * Moon API
 * # Moon-API.com Postman Collection  Welcome to the Moon Phase API Postman Collection! This collection contains a set of pre-configured API requests to interact with the Moon Phase API endpoints provided by [moon-api.com](https://moon-api.com). Explore the enchanting world of the moon and its ever-changing phases with ease using this collection.  ## Getting Started  To start using this Postman collection, follow these steps:  1. [Download and install Postman](https://www.postman.com/downloads/) if you haven't already. 2. Import the Moon API Postman Collection into your Postman app. 3. Set your RapidAPI key in the collection's environment variables. 4. Begin making requests to explore the moon phase data and retrieve lunar information.       ## Collection Structure  The Moon-API.com Postman Collection consists of the following requests:  - **Basic Moon Phase**: Retrieve the main moon phase data. - **Advanced Moon Phase**: Get detailed moon phase data based on a specific timezone and coordinates. - **Plain Text Moon Phase**: Get a plain text description of the current moon phase. - **Emoji Moon Phase**: Get the relevant emoji of the current moon phase. - **Lunar Calender**: Get the current year's moon phases in a markdown calender.       ## Environment Variables  The collection uses environment variables to store your RapidAPI key. To use this collection effectively, ensure you set the `X-Rapidapi-Key` variable in the collection's environment with your actual RapidAPI key.  ## How to Use  1. Select the desired request from the Moon API collection. 2. Click on the request to open it. 3. Send the request and view the response to retrieve the moon phase data.       ## Documentation  For more information on the Moon Phase API endpoints and their response formats, refer to the [official Moon API documentation](https://rapidapi.com/MoonAPIcom/api/moon-phase/details). Visit [moon-api.com](https://moon-api.com) to learn more about the Moon Phase API and the services provided.  Happy moon exploration with the Moon Phase API Postman Collection provided by [moon-api.com](https://moon-api.com)!
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
import GetAdvancedMoonPhaseData200ResponseMoonPhasesLastQuarterCurrent from './GetAdvancedMoonPhaseData200ResponseMoonPhasesLastQuarterCurrent';
import GetAdvancedMoonPhaseData200ResponseMoonPhasesLastQuarterNext from './GetAdvancedMoonPhaseData200ResponseMoonPhasesLastQuarterNext';

/**
 * The GetAdvancedMoonPhaseData200ResponseMoonPhasesLastQuarter model module.
 * @module model/GetAdvancedMoonPhaseData200ResponseMoonPhasesLastQuarter
 * @version 1.0.0
 */
class GetAdvancedMoonPhaseData200ResponseMoonPhasesLastQuarter {
    /**
     * Constructs a new <code>GetAdvancedMoonPhaseData200ResponseMoonPhasesLastQuarter</code>.
     * @alias module:model/GetAdvancedMoonPhaseData200ResponseMoonPhasesLastQuarter
     */
    constructor() { 
        
        GetAdvancedMoonPhaseData200ResponseMoonPhasesLastQuarter.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GetAdvancedMoonPhaseData200ResponseMoonPhasesLastQuarter</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetAdvancedMoonPhaseData200ResponseMoonPhasesLastQuarter} obj Optional instance to populate.
     * @return {module:model/GetAdvancedMoonPhaseData200ResponseMoonPhasesLastQuarter} The populated <code>GetAdvancedMoonPhaseData200ResponseMoonPhasesLastQuarter</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetAdvancedMoonPhaseData200ResponseMoonPhasesLastQuarter();

            if (data.hasOwnProperty('current')) {
                obj['current'] = GetAdvancedMoonPhaseData200ResponseMoonPhasesLastQuarterCurrent.constructFromObject(data['current']);
            }
            if (data.hasOwnProperty('next')) {
                obj['next'] = GetAdvancedMoonPhaseData200ResponseMoonPhasesLastQuarterNext.constructFromObject(data['next']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GetAdvancedMoonPhaseData200ResponseMoonPhasesLastQuarter</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetAdvancedMoonPhaseData200ResponseMoonPhasesLastQuarter</code>.
     */
    static validateJSON(data) {
        // validate the optional field `current`
        if (data['current']) { // data not null
          GetAdvancedMoonPhaseData200ResponseMoonPhasesLastQuarterCurrent.validateJSON(data['current']);
        }
        // validate the optional field `next`
        if (data['next']) { // data not null
          GetAdvancedMoonPhaseData200ResponseMoonPhasesLastQuarterNext.validateJSON(data['next']);
        }

        return true;
    }


}



/**
 * @member {module:model/GetAdvancedMoonPhaseData200ResponseMoonPhasesLastQuarterCurrent} current
 */
GetAdvancedMoonPhaseData200ResponseMoonPhasesLastQuarter.prototype['current'] = undefined;

/**
 * @member {module:model/GetAdvancedMoonPhaseData200ResponseMoonPhasesLastQuarterNext} next
 */
GetAdvancedMoonPhaseData200ResponseMoonPhasesLastQuarter.prototype['next'] = undefined;






export default GetAdvancedMoonPhaseData200ResponseMoonPhasesLastQuarter;

