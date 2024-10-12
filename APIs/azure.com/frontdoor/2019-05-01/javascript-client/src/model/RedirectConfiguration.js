/**
 * FrontDoorManagementClient
 * Use these APIs to manage Azure Front Door resources through the Azure Resource Manager. You must make sure that requests made to these resources are secure.
 *
 * The version of the OpenAPI document: 2019-05-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import RouteConfiguration from './RouteConfiguration';

/**
 * The RedirectConfiguration model module.
 * @module model/RedirectConfiguration
 * @version 2019-05-01
 */
class RedirectConfiguration {
    /**
     * Constructs a new <code>RedirectConfiguration</code>.
     * Describes Redirect Route.
     * @alias module:model/RedirectConfiguration
     * @extends module:model/RouteConfiguration
     * @implements module:model/RouteConfiguration
     * @param odataType {String} 
     */
    constructor(odataType) { 
        RouteConfiguration.initialize(this, odataType);
        RedirectConfiguration.initialize(this, odataType);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, odataType) { 
    }

    /**
     * Constructs a <code>RedirectConfiguration</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/RedirectConfiguration} obj Optional instance to populate.
     * @return {module:model/RedirectConfiguration} The populated <code>RedirectConfiguration</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new RedirectConfiguration();
            RouteConfiguration.constructFromObject(data, obj);
            RouteConfiguration.constructFromObject(data, obj);

            if (data.hasOwnProperty('customFragment')) {
                obj['customFragment'] = ApiClient.convertToType(data['customFragment'], 'String');
            }
            if (data.hasOwnProperty('customHost')) {
                obj['customHost'] = ApiClient.convertToType(data['customHost'], 'String');
            }
            if (data.hasOwnProperty('customPath')) {
                obj['customPath'] = ApiClient.convertToType(data['customPath'], 'String');
            }
            if (data.hasOwnProperty('customQueryString')) {
                obj['customQueryString'] = ApiClient.convertToType(data['customQueryString'], 'String');
            }
            if (data.hasOwnProperty('redirectProtocol')) {
                obj['redirectProtocol'] = ApiClient.convertToType(data['redirectProtocol'], 'String');
            }
            if (data.hasOwnProperty('redirectType')) {
                obj['redirectType'] = ApiClient.convertToType(data['redirectType'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>RedirectConfiguration</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>RedirectConfiguration</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of RedirectConfiguration.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['customFragment'] && !(typeof data['customFragment'] === 'string' || data['customFragment'] instanceof String)) {
            throw new Error("Expected the field `customFragment` to be a primitive type in the JSON string but got " + data['customFragment']);
        }
        // ensure the json data is a string
        if (data['customHost'] && !(typeof data['customHost'] === 'string' || data['customHost'] instanceof String)) {
            throw new Error("Expected the field `customHost` to be a primitive type in the JSON string but got " + data['customHost']);
        }
        // ensure the json data is a string
        if (data['customPath'] && !(typeof data['customPath'] === 'string' || data['customPath'] instanceof String)) {
            throw new Error("Expected the field `customPath` to be a primitive type in the JSON string but got " + data['customPath']);
        }
        // ensure the json data is a string
        if (data['customQueryString'] && !(typeof data['customQueryString'] === 'string' || data['customQueryString'] instanceof String)) {
            throw new Error("Expected the field `customQueryString` to be a primitive type in the JSON string but got " + data['customQueryString']);
        }
        // ensure the json data is a string
        if (data['redirectProtocol'] && !(typeof data['redirectProtocol'] === 'string' || data['redirectProtocol'] instanceof String)) {
            throw new Error("Expected the field `redirectProtocol` to be a primitive type in the JSON string but got " + data['redirectProtocol']);
        }
        // ensure the json data is a string
        if (data['redirectType'] && !(typeof data['redirectType'] === 'string' || data['redirectType'] instanceof String)) {
            throw new Error("Expected the field `redirectType` to be a primitive type in the JSON string but got " + data['redirectType']);
        }

        return true;
    }


}

RedirectConfiguration.RequiredProperties = ["@odata.type"];

/**
 * Fragment to add to the redirect URL. Fragment is the part of the URL that comes after #. Do not include the #.
 * @member {String} customFragment
 */
RedirectConfiguration.prototype['customFragment'] = undefined;

/**
 * Host to redirect. Leave empty to use the incoming host as the destination host.
 * @member {String} customHost
 */
RedirectConfiguration.prototype['customHost'] = undefined;

/**
 * The full path to redirect. Path cannot be empty and must start with /. Leave empty to use the incoming path as destination path.
 * @member {String} customPath
 */
RedirectConfiguration.prototype['customPath'] = undefined;

/**
 * The set of query strings to be placed in the redirect URL. Setting this value would replace any existing query string; leave empty to preserve the incoming query string. Query string must be in <key>=<value> format. The first ? and & will be added automatically so do not include them in the front, but do separate multiple query strings with &.
 * @member {String} customQueryString
 */
RedirectConfiguration.prototype['customQueryString'] = undefined;

/**
 * The protocol of the destination to where the traffic is redirected
 * @member {module:model/RedirectConfiguration.RedirectProtocolEnum} redirectProtocol
 */
RedirectConfiguration.prototype['redirectProtocol'] = undefined;

/**
 * The redirect type the rule will use when redirecting traffic.
 * @member {module:model/RedirectConfiguration.RedirectTypeEnum} redirectType
 */
RedirectConfiguration.prototype['redirectType'] = undefined;


// Implement RouteConfiguration interface:
/**
 * @member {String} @odata.type
 */
RouteConfiguration.prototype['@odata.type'] = undefined;



/**
 * Allowed values for the <code>redirectProtocol</code> property.
 * @enum {String}
 * @readonly
 */
RedirectConfiguration['RedirectProtocolEnum'] = {

    /**
     * value: "HttpOnly"
     * @const
     */
    "HttpOnly": "HttpOnly",

    /**
     * value: "HttpsOnly"
     * @const
     */
    "HttpsOnly": "HttpsOnly",

    /**
     * value: "MatchRequest"
     * @const
     */
    "MatchRequest": "MatchRequest"
};


/**
 * Allowed values for the <code>redirectType</code> property.
 * @enum {String}
 * @readonly
 */
RedirectConfiguration['RedirectTypeEnum'] = {

    /**
     * value: "Moved"
     * @const
     */
    "Moved": "Moved",

    /**
     * value: "Found"
     * @const
     */
    "Found": "Found",

    /**
     * value: "TemporaryRedirect"
     * @const
     */
    "TemporaryRedirect": "TemporaryRedirect",

    /**
     * value: "PermanentRedirect"
     * @const
     */
    "PermanentRedirect": "PermanentRedirect"
};



export default RedirectConfiguration;

