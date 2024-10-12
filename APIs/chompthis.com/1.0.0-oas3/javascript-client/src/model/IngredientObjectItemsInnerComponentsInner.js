/**
 * Chomp Food Database API Documentation
 * ## Important An **[API key](https://chompthis.com/api/)** is required for access to this API. Get yours at **[https://chompthis.com/api](https://chompthis.com/api/)**.  ### Getting Started   * **[Subscribe](https://chompthis.com/api/#pricing)** to the API.   * Scroll down and click the \"**Authorize**\" button.   * Enter your API key into the \"**value**\" input, click the \"**Authorize**\" button, then click the \"**Close**\" button.   * Scroll down to the section titled \"**default**\" and click on the API endpoint you wish to use.   * Click the \"**Try it out**\" button.   * Enter the information the endpoint requires.   * Click the \"**Execute**\" button.  ### Example    * Branded food response object: **[View example &raquo;](https://raw.githubusercontent.com/chompfoods/examples/master/branded-food-response-object.json)**   * Ingredient response object: **[View example &raquo;](https://raw.githubusercontent.com/chompfoods/examples/master/ingredient-response-object.json)**   * Error response object: **[View example &raquo;](https://raw.githubusercontent.com/chompfoods/examples/master/error-response-object.json)**  ### How Do I Find My API Key?   * Your API key was sent to the email address you used to create your subscription.   * You will also find your API key in the **[Client Center](https://chompthis.com/api/manage.php)**.   * Read **[this article](https://desk.zoho.com/portal/chompthis/kb/articles/how-do-i-find-my-api-key)** for more information.  ### Helpful Links   * **Help & Support**     * [Knowledge Base &raquo;](https://desk.zoho.com/portal/chompthis/kb/chomp)     * [Support &raquo;](https://chompthis.com/api/ticket-new.php)     * [Client Center &raquo;](https://chompthis.com/api/manage.php)   * **Pricing**     * [Subscription Options &raquo;](https://chompthis.com/api/)     * [Cost Calculator &raquo;](https://chompthis.com/api/cost-calculator.php)   * **Guidelines**     * [Terms & License &raquo;](https://chompthis.com/api/terms.php)     * [Attribution &raquo;](https://chompthis.com/api/docs/attribution.php) 
 *
 * The version of the OpenAPI document: 1.0.0-oas3
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The IngredientObjectItemsInnerComponentsInner model module.
 * @module model/IngredientObjectItemsInnerComponentsInner
 * @version 1.0.0-oas3
 */
class IngredientObjectItemsInnerComponentsInner {
    /**
     * Constructs a new <code>IngredientObjectItemsInnerComponentsInner</code>.
     * An object containing information on a specific component of this food item
     * @alias module:model/IngredientObjectItemsInnerComponentsInner
     */
    constructor() { 
        
        IngredientObjectItemsInnerComponentsInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>IngredientObjectItemsInnerComponentsInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/IngredientObjectItemsInnerComponentsInner} obj Optional instance to populate.
     * @return {module:model/IngredientObjectItemsInnerComponentsInner} The populated <code>IngredientObjectItemsInnerComponentsInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new IngredientObjectItemsInnerComponentsInner();

            if (data.hasOwnProperty('data_points')) {
                obj['data_points'] = ApiClient.convertToType(data['data_points'], 'Number');
            }
            if (data.hasOwnProperty('gram_weight')) {
                obj['gram_weight'] = ApiClient.convertToType(data['gram_weight'], 'Number');
            }
            if (data.hasOwnProperty('is_refuse')) {
                obj['is_refuse'] = ApiClient.convertToType(data['is_refuse'], 'Boolean');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('pct_weight')) {
                obj['pct_weight'] = ApiClient.convertToType(data['pct_weight'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>IngredientObjectItemsInnerComponentsInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>IngredientObjectItemsInnerComponentsInner</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }

        return true;
    }


}



/**
 * The number of obersvations on which the measure is based
 * @member {Number} data_points
 */
IngredientObjectItemsInnerComponentsInner.prototype['data_points'] = undefined;

/**
 * The weight of the component in grams
 * @member {Number} gram_weight
 */
IngredientObjectItemsInnerComponentsInner.prototype['gram_weight'] = undefined;

/**
 * Whether the component is refuse, i.e. not edible
 * @member {Boolean} is_refuse
 */
IngredientObjectItemsInnerComponentsInner.prototype['is_refuse'] = undefined;

/**
 * The kind of component, e.g. bone
 * @member {String} name
 */
IngredientObjectItemsInnerComponentsInner.prototype['name'] = undefined;

/**
 * The weight of the component as a percentage of the total weight of the food
 * @member {Number} pct_weight
 */
IngredientObjectItemsInnerComponentsInner.prototype['pct_weight'] = undefined;






export default IngredientObjectItemsInnerComponentsInner;

