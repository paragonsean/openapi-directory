/**
 * KeyServ
 * KeyServ API
 *
 * The version of the OpenAPI document: 1.4.5
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import KeyView from './KeyView';
import SubscriptionView from './SubscriptionView';

/**
 * The SubscriptionsApiFind200Response model module.
 * @module model/SubscriptionsApiFind200Response
 * @version 1.4.5
 */
class SubscriptionsApiFind200Response {
    /**
     * Constructs a new <code>SubscriptionsApiFind200Response</code>.
     * @alias module:model/SubscriptionsApiFind200Response
     * @param {(module:model/SubscriptionView)} instance The actual instance to initialize SubscriptionsApiFind200Response.
     */
    constructor(instance = null) {
        if (instance === null) {
            this.actualInstance = null;
            return;
        }
        var match = 0;
        var errorMessages = [];
        try {
            if (typeof instance === "SubscriptionView") {
                this.actualInstance = instance;
            } else {
                // plain JS object
                // validate the object
                SubscriptionView.validateJSON(instance); // throw an exception if no match
                // create SubscriptionView from JS object
                this.actualInstance = SubscriptionView.constructFromObject(instance);
            }
            match++;
        } catch(err) {
            // json data failed to deserialize into SubscriptionView
            errorMessages.push("Failed to construct SubscriptionView: " + err)
        }

        if (match > 1) {
            throw new Error("Multiple matches found constructing `SubscriptionsApiFind200Response` with oneOf schemas SubscriptionView. Input: " + JSON.stringify(instance));
        } else if (match === 0) {
            this.actualInstance = null; // clear the actual instance in case there are multiple matches
            throw new Error("No match found constructing `SubscriptionsApiFind200Response` with oneOf schemas SubscriptionView. Details: " +
                            errorMessages.join(", "));
        } else { // only 1 match
            // the input is valid
        }
    }

    /**
     * Constructs a <code>SubscriptionsApiFind200Response</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SubscriptionsApiFind200Response} obj Optional instance to populate.
     * @return {module:model/SubscriptionsApiFind200Response} The populated <code>SubscriptionsApiFind200Response</code> instance.
     */
    static constructFromObject(data, obj) {
        return new SubscriptionsApiFind200Response(data);
    }

    /**
     * Gets the actual instance, which can be <code>SubscriptionView</code>.
     * @return {(module:model/SubscriptionView)} The actual instance.
     */
    getActualInstance() {
        return this.actualInstance;
    }

    /**
     * Sets the actual instance, which can be <code>SubscriptionView</code>.
     * @param {(module:model/SubscriptionView)} obj The actual instance.
     */
    setActualInstance(obj) {
       this.actualInstance = SubscriptionsApiFind200Response.constructFromObject(obj).getActualInstance();
    }

    /**
     * Returns the JSON representation of the actual instance.
     * @return {string}
     */
    toJSON = function(){
        return this.getActualInstance();
    }

    /**
     * Create an instance of SubscriptionsApiFind200Response from a JSON string.
     * @param {string} json_string JSON string.
     * @return {module:model/SubscriptionsApiFind200Response} An instance of SubscriptionsApiFind200Response.
     */
    static fromJSON = function(json_string){
        return SubscriptionsApiFind200Response.constructFromObject(JSON.parse(json_string));
    }
}

/**
 * @member {String} action
 */
SubscriptionsApiFind200Response.prototype['action'] = undefined;

/**
 * @member {Boolean} callbackOnModify
 */
SubscriptionsApiFind200Response.prototype['callbackOnModify'] = undefined;

/**
 * @member {String} callbackUrl
 */
SubscriptionsApiFind200Response.prototype['callbackUrl'] = undefined;

/**
 * @member {Date} commenced
 */
SubscriptionsApiFind200Response.prototype['commenced'] = undefined;

/**
 * @member {Date} created
 */
SubscriptionsApiFind200Response.prototype['created'] = undefined;

/**
 * @member {Object} custom
 */
SubscriptionsApiFind200Response.prototype['custom'] = undefined;

/**
 * @member {String} frequency
 */
SubscriptionsApiFind200Response.prototype['frequency'] = undefined;

/**
 * @member {Array.<module:model/KeyView>} keys
 */
SubscriptionsApiFind200Response.prototype['keys'] = undefined;

/**
 * @member {String} name
 */
SubscriptionsApiFind200Response.prototype['name'] = undefined;

/**
 * @member {Date} updated
 */
SubscriptionsApiFind200Response.prototype['updated'] = undefined;


SubscriptionsApiFind200Response.OneOf = ["SubscriptionView"];

export default SubscriptionsApiFind200Response;

