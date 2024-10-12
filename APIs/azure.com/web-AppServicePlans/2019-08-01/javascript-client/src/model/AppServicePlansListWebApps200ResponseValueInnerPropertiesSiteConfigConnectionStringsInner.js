/**
 * AppServicePlans API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-08-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigConnectionStringsInner model module.
 * @module model/AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigConnectionStringsInner
 * @version 2019-08-01
 */
class AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigConnectionStringsInner {
    /**
     * Constructs a new <code>AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigConnectionStringsInner</code>.
     * Database connection string information.
     * @alias module:model/AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigConnectionStringsInner
     */
    constructor() { 
        
        AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigConnectionStringsInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigConnectionStringsInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigConnectionStringsInner} obj Optional instance to populate.
     * @return {module:model/AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigConnectionStringsInner} The populated <code>AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigConnectionStringsInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigConnectionStringsInner();

            if (data.hasOwnProperty('connectionString')) {
                obj['connectionString'] = ApiClient.convertToType(data['connectionString'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigConnectionStringsInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigConnectionStringsInner</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['connectionString'] && !(typeof data['connectionString'] === 'string' || data['connectionString'] instanceof String)) {
            throw new Error("Expected the field `connectionString` to be a primitive type in the JSON string but got " + data['connectionString']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}



/**
 * Connection string value.
 * @member {String} connectionString
 */
AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigConnectionStringsInner.prototype['connectionString'] = undefined;

/**
 * Name of connection string.
 * @member {String} name
 */
AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigConnectionStringsInner.prototype['name'] = undefined;

/**
 * Type of database.
 * @member {module:model/AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigConnectionStringsInner.TypeEnum} type
 */
AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigConnectionStringsInner.prototype['type'] = undefined;





/**
 * Allowed values for the <code>type</code> property.
 * @enum {String}
 * @readonly
 */
AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigConnectionStringsInner['TypeEnum'] = {

    /**
     * value: "MySql"
     * @const
     */
    "MySql": "MySql",

    /**
     * value: "SQLServer"
     * @const
     */
    "SQLServer": "SQLServer",

    /**
     * value: "SQLAzure"
     * @const
     */
    "SQLAzure": "SQLAzure",

    /**
     * value: "Custom"
     * @const
     */
    "Custom": "Custom",

    /**
     * value: "NotificationHub"
     * @const
     */
    "NotificationHub": "NotificationHub",

    /**
     * value: "ServiceBus"
     * @const
     */
    "ServiceBus": "ServiceBus",

    /**
     * value: "EventHub"
     * @const
     */
    "EventHub": "EventHub",

    /**
     * value: "ApiHub"
     * @const
     */
    "ApiHub": "ApiHub",

    /**
     * value: "DocDb"
     * @const
     */
    "DocDb": "DocDb",

    /**
     * value: "RedisCache"
     * @const
     */
    "RedisCache": "RedisCache",

    /**
     * value: "PostgreSQL"
     * @const
     */
    "PostgreSQL": "PostgreSQL"
};



export default AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigConnectionStringsInner;

