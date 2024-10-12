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
import ThemeThemesDetails from './ThemeThemesDetails';

/**
 * The ThemeColorsDetails model module.
 * @module model/ThemeColorsDetails
 * @version 0.1.0
 */
class ThemeColorsDetails {
    /**
     * Constructs a new <code>ThemeColorsDetails</code>.
     * @alias module:model/ThemeColorsDetails
     */
    constructor() { 
        
        ThemeColorsDetails.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ThemeColorsDetails</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ThemeColorsDetails} obj Optional instance to populate.
     * @return {module:model/ThemeColorsDetails} The populated <code>ThemeColorsDetails</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ThemeColorsDetails();

            if (data.hasOwnProperty('accent1')) {
                obj['accent1'] = ApiClient.convertToType(data['accent1'], 'String');
            }
            if (data.hasOwnProperty('accent2')) {
                obj['accent2'] = ApiClient.convertToType(data['accent2'], 'String');
            }
            if (data.hasOwnProperty('accent3')) {
                obj['accent3'] = ApiClient.convertToType(data['accent3'], 'String');
            }
            if (data.hasOwnProperty('accent4')) {
                obj['accent4'] = ApiClient.convertToType(data['accent4'], 'String');
            }
            if (data.hasOwnProperty('accent5')) {
                obj['accent5'] = ApiClient.convertToType(data['accent5'], 'String');
            }
            if (data.hasOwnProperty('accent6')) {
                obj['accent6'] = ApiClient.convertToType(data['accent6'], 'String');
            }
            if (data.hasOwnProperty('dark1')) {
                obj['dark1'] = ApiClient.convertToType(data['dark1'], 'String');
            }
            if (data.hasOwnProperty('dark2')) {
                obj['dark2'] = ApiClient.convertToType(data['dark2'], 'String');
            }
            if (data.hasOwnProperty('dateCreated')) {
                obj['dateCreated'] = ApiClient.convertToType(data['dateCreated'], 'Date');
            }
            if (data.hasOwnProperty('dateModified')) {
                obj['dateModified'] = ApiClient.convertToType(data['dateModified'], 'Date');
            }
            if (data.hasOwnProperty('followedHyperlink')) {
                obj['followedHyperlink'] = ApiClient.convertToType(data['followedHyperlink'], 'String');
            }
            if (data.hasOwnProperty('hyperlink')) {
                obj['hyperlink'] = ApiClient.convertToType(data['hyperlink'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('light1')) {
                obj['light1'] = ApiClient.convertToType(data['light1'], 'String');
            }
            if (data.hasOwnProperty('light2')) {
                obj['light2'] = ApiClient.convertToType(data['light2'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
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
     * Validates the JSON data with respect to <code>ThemeColorsDetails</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ThemeColorsDetails</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['accent1'] && !(typeof data['accent1'] === 'string' || data['accent1'] instanceof String)) {
            throw new Error("Expected the field `accent1` to be a primitive type in the JSON string but got " + data['accent1']);
        }
        // ensure the json data is a string
        if (data['accent2'] && !(typeof data['accent2'] === 'string' || data['accent2'] instanceof String)) {
            throw new Error("Expected the field `accent2` to be a primitive type in the JSON string but got " + data['accent2']);
        }
        // ensure the json data is a string
        if (data['accent3'] && !(typeof data['accent3'] === 'string' || data['accent3'] instanceof String)) {
            throw new Error("Expected the field `accent3` to be a primitive type in the JSON string but got " + data['accent3']);
        }
        // ensure the json data is a string
        if (data['accent4'] && !(typeof data['accent4'] === 'string' || data['accent4'] instanceof String)) {
            throw new Error("Expected the field `accent4` to be a primitive type in the JSON string but got " + data['accent4']);
        }
        // ensure the json data is a string
        if (data['accent5'] && !(typeof data['accent5'] === 'string' || data['accent5'] instanceof String)) {
            throw new Error("Expected the field `accent5` to be a primitive type in the JSON string but got " + data['accent5']);
        }
        // ensure the json data is a string
        if (data['accent6'] && !(typeof data['accent6'] === 'string' || data['accent6'] instanceof String)) {
            throw new Error("Expected the field `accent6` to be a primitive type in the JSON string but got " + data['accent6']);
        }
        // ensure the json data is a string
        if (data['dark1'] && !(typeof data['dark1'] === 'string' || data['dark1'] instanceof String)) {
            throw new Error("Expected the field `dark1` to be a primitive type in the JSON string but got " + data['dark1']);
        }
        // ensure the json data is a string
        if (data['dark2'] && !(typeof data['dark2'] === 'string' || data['dark2'] instanceof String)) {
            throw new Error("Expected the field `dark2` to be a primitive type in the JSON string but got " + data['dark2']);
        }
        // ensure the json data is a string
        if (data['followedHyperlink'] && !(typeof data['followedHyperlink'] === 'string' || data['followedHyperlink'] instanceof String)) {
            throw new Error("Expected the field `followedHyperlink` to be a primitive type in the JSON string but got " + data['followedHyperlink']);
        }
        // ensure the json data is a string
        if (data['hyperlink'] && !(typeof data['hyperlink'] === 'string' || data['hyperlink'] instanceof String)) {
            throw new Error("Expected the field `hyperlink` to be a primitive type in the JSON string but got " + data['hyperlink']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['light1'] && !(typeof data['light1'] === 'string' || data['light1'] instanceof String)) {
            throw new Error("Expected the field `light1` to be a primitive type in the JSON string but got " + data['light1']);
        }
        // ensure the json data is a string
        if (data['light2'] && !(typeof data['light2'] === 'string' || data['light2'] instanceof String)) {
            throw new Error("Expected the field `light2` to be a primitive type in the JSON string but got " + data['light2']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
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
 * @member {String} accent1
 */
ThemeColorsDetails.prototype['accent1'] = undefined;

/**
 * @member {String} accent2
 */
ThemeColorsDetails.prototype['accent2'] = undefined;

/**
 * @member {String} accent3
 */
ThemeColorsDetails.prototype['accent3'] = undefined;

/**
 * @member {String} accent4
 */
ThemeColorsDetails.prototype['accent4'] = undefined;

/**
 * @member {String} accent5
 */
ThemeColorsDetails.prototype['accent5'] = undefined;

/**
 * @member {String} accent6
 */
ThemeColorsDetails.prototype['accent6'] = undefined;

/**
 * @member {String} dark1
 */
ThemeColorsDetails.prototype['dark1'] = undefined;

/**
 * @member {String} dark2
 */
ThemeColorsDetails.prototype['dark2'] = undefined;

/**
 * @member {Date} dateCreated
 */
ThemeColorsDetails.prototype['dateCreated'] = undefined;

/**
 * @member {Date} dateModified
 */
ThemeColorsDetails.prototype['dateModified'] = undefined;

/**
 * @member {String} followedHyperlink
 */
ThemeColorsDetails.prototype['followedHyperlink'] = undefined;

/**
 * @member {String} hyperlink
 */
ThemeColorsDetails.prototype['hyperlink'] = undefined;

/**
 * @member {String} id
 */
ThemeColorsDetails.prototype['id'] = undefined;

/**
 * @member {String} light1
 */
ThemeColorsDetails.prototype['light1'] = undefined;

/**
 * @member {String} light2
 */
ThemeColorsDetails.prototype['light2'] = undefined;

/**
 * @member {String} name
 */
ThemeColorsDetails.prototype['name'] = undefined;

/**
 * @member {module:model/ThemeThemesDetails} theme
 */
ThemeColorsDetails.prototype['theme'] = undefined;

/**
 * @member {String} themeId
 */
ThemeColorsDetails.prototype['themeId'] = undefined;

/**
 * @member {String} userCreated
 */
ThemeColorsDetails.prototype['userCreated'] = undefined;

/**
 * @member {String} userModified
 */
ThemeColorsDetails.prototype['userModified'] = undefined;






export default ThemeColorsDetails;

