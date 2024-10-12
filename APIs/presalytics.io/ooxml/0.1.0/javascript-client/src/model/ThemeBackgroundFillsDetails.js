/**
 * OOXML Automation
 * This API helps users convert Excel and Powerpoint documents into rich, live dashboards and stories.
 *
 * The version of the OpenAPI document: 0.1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import SharedFillMapDetails from './SharedFillMapDetails';
import ThemeThemesDetails from './ThemeThemesDetails';

/**
 * The ThemeBackgroundFillsDetails model module.
 * @module model/ThemeBackgroundFillsDetails
 * @version 0.1.0
 */
class ThemeBackgroundFillsDetails {
    /**
     * Constructs a new <code>ThemeBackgroundFillsDetails</code>.
     * @alias module:model/ThemeBackgroundFillsDetails
     */
    constructor() { 
        
        ThemeBackgroundFillsDetails.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ThemeBackgroundFillsDetails</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ThemeBackgroundFillsDetails} obj Optional instance to populate.
     * @return {module:model/ThemeBackgroundFillsDetails} The populated <code>ThemeBackgroundFillsDetails</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ThemeBackgroundFillsDetails();

            if (data.hasOwnProperty('dateCreated')) {
                obj['dateCreated'] = ApiClient.convertToType(data['dateCreated'], 'Date');
            }
            if (data.hasOwnProperty('dateModified')) {
                obj['dateModified'] = ApiClient.convertToType(data['dateModified'], 'Date');
            }
            if (data.hasOwnProperty('fillMap')) {
                obj['fillMap'] = SharedFillMapDetails.constructFromObject(data['fillMap']);
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('intensityId')) {
                obj['intensityId'] = ApiClient.convertToType(data['intensityId'], 'Number');
            }
            if (data.hasOwnProperty('theme')) {
                obj['theme'] = ThemeThemesDetails.constructFromObject(data['theme']);
            }
            if (data.hasOwnProperty('themeId')) {
                obj['themeId'] = ApiClient.convertToType(data['themeId'], 'String');
            }
            if (data.hasOwnProperty('userCreated')) {
                obj['userCreated'] = ApiClient.convertToType(data['userCreated'], 'String');
            }
            if (data.hasOwnProperty('userModified')) {
                obj['userModified'] = ApiClient.convertToType(data['userModified'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ThemeBackgroundFillsDetails</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ThemeBackgroundFillsDetails</code>.
     */
    static validateJSON(data) {
        // validate the optional field `fillMap`
        if (data['fillMap']) { // data not null
          SharedFillMapDetails.validateJSON(data['fillMap']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // validate the optional field `theme`
        if (data['theme']) { // data not null
          ThemeThemesDetails.validateJSON(data['theme']);
        }
        // ensure the json data is a string
        if (data['themeId'] && !(typeof data['themeId'] === 'string' || data['themeId'] instanceof String)) {
            throw new Error("Expected the field `themeId` to be a primitive type in the JSON string but got " + data['themeId']);
        }
        // ensure the json data is a string
        if (data['userCreated'] && !(typeof data['userCreated'] === 'string' || data['userCreated'] instanceof String)) {
            throw new Error("Expected the field `userCreated` to be a primitive type in the JSON string but got " + data['userCreated']);
        }
        // ensure the json data is a string
        if (data['userModified'] && !(typeof data['userModified'] === 'string' || data['userModified'] instanceof String)) {
            throw new Error("Expected the field `userModified` to be a primitive type in the JSON string but got " + data['userModified']);
        }

        return true;
    }


}



/**
 * @member {Date} dateCreated
 */
ThemeBackgroundFillsDetails.prototype['dateCreated'] = undefined;

/**
 * @member {Date} dateModified
 */
ThemeBackgroundFillsDetails.prototype['dateModified'] = undefined;

/**
 * @member {module:model/SharedFillMapDetails} fillMap
 */
ThemeBackgroundFillsDetails.prototype['fillMap'] = undefined;

/**
 * @member {String} id
 */
ThemeBackgroundFillsDetails.prototype['id'] = undefined;

/**
 * @member {Number} intensityId
 */
ThemeBackgroundFillsDetails.prototype['intensityId'] = undefined;

/**
 * @member {module:model/ThemeThemesDetails} theme
 */
ThemeBackgroundFillsDetails.prototype['theme'] = undefined;

/**
 * @member {String} themeId
 */
ThemeBackgroundFillsDetails.prototype['themeId'] = undefined;

/**
 * @member {String} userCreated
 */
ThemeBackgroundFillsDetails.prototype['userCreated'] = undefined;

/**
 * @member {String} userModified
 */
ThemeBackgroundFillsDetails.prototype['userModified'] = undefined;






export default ThemeBackgroundFillsDetails;

