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


import ApiClient from "../ApiClient";
import BrandedFoodObject from '../model/BrandedFoodObject';
import IngredientObject from '../model/IngredientObject';

/**
* Default service.
* @module api/DefaultApi
* @version 1.0.0-oas3
*/
export default class DefaultApi {

    /**
    * Constructs a new DefaultApi. 
    * @alias module:api/DefaultApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the foodBrandedBarcodePhpGet operation.
     * @callback module:api/DefaultApi~foodBrandedBarcodePhpGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/BrandedFoodObject} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a branded food item using a barcode
     * ## Get data for a branded food using the food's UPC/EAN barcode.  **Example**  > ```https://chompthis.com/api/v2/food/branded/barcode.php?api_key=API_KEY&code=CODE```  **Tips**   * Read our **[Knowledge Base article](https://desk.zoho.com/portal/chompthis/kb/articles/im-having-trouble-getting-matches-for-barcodes-what-can-id-do)** for helpful tips and tricks. 
     * @param {String} code #### UPC/EAN barcode  **Example** > ```&code=0842234000988``` 
     * @param {module:api/DefaultApi~foodBrandedBarcodePhpGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/BrandedFoodObject}
     */
    foodBrandedBarcodePhpGet(code, callback) {
      let postBody = null;
      // verify the required parameter 'code' is set
      if (code === undefined || code === null) {
        throw new Error("Missing the required parameter 'code' when calling foodBrandedBarcodePhpGet");
      }

      let pathParams = {
      };
      let queryParams = {
        'code': code
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['ApiKeyAuth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = BrandedFoodObject;
      return this.apiClient.callApi(
        '/food/branded/barcode.php', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the foodBrandedNamePhpGet operation.
     * @callback module:api/DefaultApi~foodBrandedNamePhpGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/BrandedFoodObject} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a branded food item by name
     * ## Search for branded food items by name.  **Example** > ```https://chompthis.com/api/v2/food/branded/name.php?api_key=API_KEY&name=NAME```  **Tips**   * Get started by using our **[food lookup tool](https://chompthis.com/api/lookup.php)**.  > This API endpoint is only available to Standard and Premium API subscribers. Please consider upgrading your subscription if you are subscribed to the Limited plan. **[Read this](https://desk.zoho.com/portal/chompthis/kb/articles/can-i-upgrade-downgrade-my-subscription)** if you aren't sure how to upgrade your subscription. 
     * @param {String} name #### Search for branded food items using a general food name keyword. This does not have to exactly match the \"official\" name for the food.  **Example** > ```&name=Starburst``` 
     * @param {Object} opts Optional parameters
     * @param {module:model/Number} [limit] #### Set maximum number of records you want the API to return. The default value is \"**10**.\"  **Example** > ```&limit=10``` 
     * @param {Number} [page] #### This is how you paginate the search result. By default, you will see the first 10 records. You must increment the page number to access the next 10 records, and so on. The default value is \"**1**.\"  **Example** > ```&page=1``` 
     * @param {module:api/DefaultApi~foodBrandedNamePhpGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/BrandedFoodObject}
     */
    foodBrandedNamePhpGet(name, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'name' is set
      if (name === undefined || name === null) {
        throw new Error("Missing the required parameter 'name' when calling foodBrandedNamePhpGet");
      }

      let pathParams = {
      };
      let queryParams = {
        'name': name,
        'limit': opts['limit'],
        'page': opts['page']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['ApiKeyAuth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = BrandedFoodObject;
      return this.apiClient.callApi(
        '/food/branded/name.php', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the foodBrandedSearchPhpGet operation.
     * @callback module:api/DefaultApi~foodBrandedSearchPhpGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/BrandedFoodObject} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get data for branded food items using various search parameters
     * ## Search for branded food items using various parameters.  **Example** > ```https://chompthis.com/api/v2/food/branded/search.php?api_key=API_KEY&brand=BRAND&country=COUNTRY&page=1```  **Tips**    * Get started by using the **[Query Builder](https://chompthis.com/api/build.php)**.  > This API endpoint is only available to Standard and Premium API subscribers. Please consider upgrading your subscription if you are subscribed to the Limited plan. **[Read this](https://desk.zoho.com/portal/chompthis/kb/articles/can-i-upgrade-downgrade-my-subscription)** if you aren't sure how to upgrade your subscription. 
     * @param {Object} opts Optional parameters
     * @param {String} [allergen] #### Filter the search to only include branded foods that contain a specific allergen.  **Example** > ```&allergen=Peanuts```  **Important Note**: This parameter cannot be used alone. It must be paired with at least 1 additional parameter. 
     * @param {String} [brand] #### Filter the search to only include branded foods that are owned by a specific brand.  **Example** > ```&brand=Starbucks``` 
     * @param {String} [category] #### Filter the search to only include branded foods from a specific category.  **Example** > ```&category=Plant Based Foods``` 
     * @param {String} [country] #### Filter the search to only include branded foods that are sold in a specific country.  **Example** > ```&country=United States```  **Important Note**: This parameter cannot be used alone. It must be paired with at least 1 additional parameter. 
     * @param {module:model/String} [diet] #### Filter the search to only include branded foods that are considered compatible with a specific diet.  **Important Note**: This parameter cannot be used alone. It must be paired with at least 1 additional parameter. 
     * @param {String} [ingredient] #### Filter the search to only include branded foods that contain a specific ingredient.  **Example** > ```&ingredient=Salt``` 
     * @param {String} [keyword] #### Filter the search to only include branded foods that are associated with a specific keyword.  **Example** > ```&keyword=Organic```  **Important Note**: This parameter cannot be used alone. It must be paired with at least 1 additional parameter. 
     * @param {String} [mineral] #### Filter the search to only include branded foods that contain a specific mineral.  **Example** > ```&mineral=Potassium``` 
     * @param {String} [nutrient] #### Filter the search to only include branded foods that contain a specific nutrient.  **Example** > ```&nutrient=Caffeine```  **Important Note**: This parameter cannot be used alone. It must be paired with at least 1 additional parameter. 
     * @param {String} [palmOil] #### Filter the search to only include branded foods that contain a specific ingredient made using palm oil.  **Example** > ```&palm_oil=E160a Beta Carotene``` 
     * @param {String} [trace] ### Filter the search to only include branded foods that contain a specific trace ingredient.  **Example** > ```&trace=Tree Nuts```  **Important Note**: This parameter cannot be used alone. It must be paired with at least 1 additional parameter. 
     * @param {String} [vitamin] #### Filter the search to only include branded foods that contain a specific vitamin.  **Example** > ```&vitamin=Biotin``` 
     * @param {module:model/Number} [limit] #### Set maximum number of records you want the API to return. The default value is \"**10**.\"  **Example** > ```&limit=10``` 
     * @param {Number} [page] #### This is how you paginate the search result. By default, you will see the first 10 records. You must increment the page number to access the next 10 records, and so on. The default value is \"**1**.\"  **Example** > ```&page=1``` 
     * @param {module:api/DefaultApi~foodBrandedSearchPhpGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/BrandedFoodObject}
     */
    foodBrandedSearchPhpGet(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'allergen': opts['allergen'],
        'brand': opts['brand'],
        'category': opts['category'],
        'country': opts['country'],
        'diet': opts['diet'],
        'ingredient': opts['ingredient'],
        'keyword': opts['keyword'],
        'mineral': opts['mineral'],
        'nutrient': opts['nutrient'],
        'palm_oil': opts['palmOil'],
        'trace': opts['trace'],
        'vitamin': opts['vitamin'],
        'limit': opts['limit'],
        'page': opts['page']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['ApiKeyAuth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = BrandedFoodObject;
      return this.apiClient.callApi(
        '/food/branded/search.php', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the foodIngredientSearchPhpGet operation.
     * @callback module:api/DefaultApi~foodIngredientSearchPhpGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/IngredientObject} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get raw/generic food ingredient item(s)
     * ## Get data for a specific ingredient or a specific set of ingredients.  **Example #1: Single Ingredient** > ```https://chompthis.com/api/v2/ingredient/search.php?api_key=API_KEY&find=raw broccoli```  **Example #2: Set of Ingredients** > ```https://chompthis.com/api/v2/ingredient/search.php?api_key=API_KEY&find=raw broccoli,mashed potatoes,chicken drumstick```  **Tips**   * Expose ingredient endpoints by using our **[food lookup tool](https://chompthis.com/api/lookup.php)**.  > This API endpoint is only available to Standard and Premium API subscribers. Please consider upgrading your subscription if you are subscribed to the Limited plan. **[Read this](https://desk.zoho.com/portal/chompthis/kb/articles/can-i-upgrade-downgrade-my-subscription)** if you aren't sure how to upgrade your subscription. 
     * @param {String} find Search our database for a single ingredient or a specific set of ingredients.  **Example #1: Single Ingredient** > ```&find=raw broccoli```  **Example #2: Set of Ingredients** > ```&find=raw broccoli,buttermilk waffle,mashed potatoes```  **Important Notes**    * Comma-separated lists cannot contain more than **10 ingredients**. You must perform additional API calls if you are looking up more than 10 ingredients. 
     * @param {Object} opts Optional parameters
     * @param {module:model/Number} [limit] #### Set maximum number of records you want the API to return, per search term. The default value is \"**1**.\"  **Example** > ```&limit=3``` 
     * @param {module:api/DefaultApi~foodIngredientSearchPhpGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/IngredientObject}
     */
    foodIngredientSearchPhpGet(find, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'find' is set
      if (find === undefined || find === null) {
        throw new Error("Missing the required parameter 'find' when calling foodIngredientSearchPhpGet");
      }

      let pathParams = {
      };
      let queryParams = {
        'find': find,
        'limit': opts['limit']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['ApiKeyAuth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = IngredientObject;
      return this.apiClient.callApi(
        '/food/ingredient/search.php', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
