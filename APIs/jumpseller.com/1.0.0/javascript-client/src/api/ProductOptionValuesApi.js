/**
 * Jumpseller API
 * # Endpoint Structure  All URLs are in the format:   ```text https://api.jumpseller.com/v1/path.json?login=XXXXXX&authtoken=storetoken   ```  The path is prefixed by the API version and the URL takes as parameters the login (your store specific API login) and your authentication token. <br/><br/> ***  # Version  The current version of the API is **v1**.   If we change the API in backward-incompatible ways, we'll increase the version number and maintain stable support for the old urls. <br/><br/> ***  # Authentication  The API uses a token-based authentication with a combination of a login key and an auth token. **Both parameters can be found on the left sidebar of the Account section, accessed from the main menu of your Admin Panel**. The auth token of the user can be reset on the same page.  ![Store Login](/images/support/api/apilogin.png)  The auth token is a **32 characters** string.  If you are developing a Jumpseller App, the authentication should be done using [OAuth-2](/support/oauth-2). Please read the article [Build an App](/support/apps) for more information. <br/><br/> ***  # Curl Examples  To request all the products at your store, you would append the products index path to the base url to create an URL with the format:    ```text https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX ```  In curl, you can invoque that URL with:    ```text curl -X GET \"https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX\" ```  To create a product, you will include the JSON data and specify the MIME Type:    ```text curl -X POST -d '{ \"product\" : {\"name\": \"My new Product!\", \"price\": 100} }' \"https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX\" -H \"Content-Type:application/json\" ```  and to update the product identified with 123:    ```text curl -X PUT -d '{ \"product\" : {\"name\": \"My updated Product!\", \"price\": 99} }' \"https://api.jumpseller.com/v1/products/123.json?login=XXXXXX&authtoken=XXXXX\" -H \"Content-Type:application/json\" ```  or delete it:    ```text curl -X DELETE \"https://api.jumpseller.com/v1/products/123.json?login=XXXXXX&authtoken=XXXXX\" -H \"Content-Type:application/json\" ``` <br/><br/> ***  # PHP Examples  Create a new Product (POST method)  ```php $url = 'https://api.jumpseller.com/v1/products.json?login=XXXXX&authtoken=XXXXX; $ch = curl_init($url); curl_setopt($ch, CURLOPT_RETURNTRANSFER, true); curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));  curl_setopt($ch, CURLOPT_CUSTOMREQUEST, \"POST\"); //post method curl_setopt($ch, CURLOPT_POSTFIELDS, '{ \"product\" : {\"name\": \"My updated Product!\", \"price\": 99} }');  $result = curl_exec($ch); print_r($result); curl_close($ch); ``` <br/><br/> ***  # Plain JSON only. No XML.  * We only support JSON for data serialization. * Our node format has no root element.   * We use snake_case to describe attribute keys (like \"created_at\").   * All empty value are replaced with **null** strings. * All API URLs end in .json to indicate that they accept and return JSON. * POST and PUT methods require you to explicitly state the MIME type of your request's body content as **\"application/json\"**. <br/><br/> ***  # Rate Limit You can perform a maximum of:  + 240 (two hundred forty) requests per minute and + 8 (eight) requests per second   If you exceed this limit, you'll get a 403 Forbidden (Rate Limit Exceeded) response for subsequent requests.    The rate limits apply by IP address and by store. This means that multiple requests on different stores are not counted towards the same rate limit.  This limits are necessary to ensure resources are correctly used. Your application should be aware of this limits and retry any unsuccessful request, check the following Ruby stub:  ```ruby tries = 0; max_tries = 3; begin   HTTParty.send(method, uri) # perform an API call.   sleep 0.5   tries += 1 rescue   unless tries >= max_tries     sleep 1.0 # wait the necessary time before retrying the call again.     retry   end end ```  Finally, you can review the Response Headers of each request:  ```text Jumpseller-PerMinuteRateLimit-Limit: 60   Jumpseller-PerMinuteRateLimit-Remaining: 59 # requests available on the per-second interval   Jumpseller-PerSecondRateLimit-Limit: 2   Jumpseller-PerSecondRateLimit-Remaining: 1 # requests available on the per-second interval ```   to better model your application requests intervals.  In the event of getting your IP banned, the Response Header `Jumpseller-BannedByRateLimit-Reset` informs you the time when will your ban be reseted. <br/><br/> ***  # Pagination  By default we will return 50 objects (products, orders, etc) per page. There is a maximum of 100, using a query string `&limit=100`. If the result set gets paginated it is your responsibility to check the next page for more objects -- you do this by using query strings `&page=2`, `&page=3` and so on.  ```text https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX&page=3&limit=100 ``` <br/><br/> ***  # More * [Jumpseller API wrapper](https://gitlab.com/jumpseller-api/ruby) provides a public Ruby abstraction over our API; * [Apps Page](/apps) showcases external integrations with Jumpseller done by technical experts; * [Imgbb API](https://api.imgbb.com/) provides an easy way to upload and temporaly host for images and files. <br/><br/> *** <br/><br/> 
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import Count from '../model/Count';
import NotFound from '../model/NotFound';
import ProductOptionValue from '../model/ProductOptionValue';
import ProductOptionValueEdit from '../model/ProductOptionValueEdit';

/**
* ProductOptionValues service.
* @module api/ProductOptionValuesApi
* @version 1.0.0
*/
export default class ProductOptionValuesApi {

    /**
    * Constructs a new ProductOptionValuesApi. 
    * @alias module:api/ProductOptionValuesApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the productsIdOptionsOptionIdValuesCountJsonGet operation.
     * @callback module:api/ProductOptionValuesApi~productsIdOptionsOptionIdValuesCountJsonGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Count} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Count all Product Option Values.
     * @param {String} login API OAuth login.
     * @param {String} authtoken API OAuth token.
     * @param {Number} id ID of the Product
     * @param {Number} optionId ID of the Product Option
     * @param {module:api/ProductOptionValuesApi~productsIdOptionsOptionIdValuesCountJsonGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Count}
     */
    productsIdOptionsOptionIdValuesCountJsonGet(login, authtoken, id, optionId, callback) {
      let postBody = null;
      // verify the required parameter 'login' is set
      if (login === undefined || login === null) {
        throw new Error("Missing the required parameter 'login' when calling productsIdOptionsOptionIdValuesCountJsonGet");
      }
      // verify the required parameter 'authtoken' is set
      if (authtoken === undefined || authtoken === null) {
        throw new Error("Missing the required parameter 'authtoken' when calling productsIdOptionsOptionIdValuesCountJsonGet");
      }
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling productsIdOptionsOptionIdValuesCountJsonGet");
      }
      // verify the required parameter 'optionId' is set
      if (optionId === undefined || optionId === null) {
        throw new Error("Missing the required parameter 'optionId' when calling productsIdOptionsOptionIdValuesCountJsonGet");
      }

      let pathParams = {
        'id': id,
        'option_id': optionId
      };
      let queryParams = {
        'login': login,
        'authtoken': authtoken
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Count;
      return this.apiClient.callApi(
        '/products/{id}/options/{option_id}/values/count.json', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the productsIdOptionsOptionIdValuesJsonGet operation.
     * @callback module:api/ProductOptionValuesApi~productsIdOptionsOptionIdValuesJsonGetCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/ProductOptionValue>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve all Product Option Values.
     * @param {String} login API OAuth login.
     * @param {String} authtoken API OAuth token.
     * @param {Number} id ID of the Product
     * @param {Number} optionId ID of the Product Option
     * @param {module:api/ProductOptionValuesApi~productsIdOptionsOptionIdValuesJsonGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/ProductOptionValue>}
     */
    productsIdOptionsOptionIdValuesJsonGet(login, authtoken, id, optionId, callback) {
      let postBody = null;
      // verify the required parameter 'login' is set
      if (login === undefined || login === null) {
        throw new Error("Missing the required parameter 'login' when calling productsIdOptionsOptionIdValuesJsonGet");
      }
      // verify the required parameter 'authtoken' is set
      if (authtoken === undefined || authtoken === null) {
        throw new Error("Missing the required parameter 'authtoken' when calling productsIdOptionsOptionIdValuesJsonGet");
      }
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling productsIdOptionsOptionIdValuesJsonGet");
      }
      // verify the required parameter 'optionId' is set
      if (optionId === undefined || optionId === null) {
        throw new Error("Missing the required parameter 'optionId' when calling productsIdOptionsOptionIdValuesJsonGet");
      }

      let pathParams = {
        'id': id,
        'option_id': optionId
      };
      let queryParams = {
        'login': login,
        'authtoken': authtoken
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [ProductOptionValue];
      return this.apiClient.callApi(
        '/products/{id}/options/{option_id}/values.json', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the productsIdOptionsOptionIdValuesJsonPost operation.
     * @callback module:api/ProductOptionValuesApi~productsIdOptionsOptionIdValuesJsonPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ProductOptionValue} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a new Product Option Value.
     * @param {String} login API OAuth login.
     * @param {String} authtoken API OAuth token.
     * @param {Number} id Id of the Product
     * @param {Number} optionId Id of the Product Option
     * @param {module:model/ProductOptionValueEdit} productOptionValueEdit Product Option Value parameters.
     * @param {module:api/ProductOptionValuesApi~productsIdOptionsOptionIdValuesJsonPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ProductOptionValue}
     */
    productsIdOptionsOptionIdValuesJsonPost(login, authtoken, id, optionId, productOptionValueEdit, callback) {
      let postBody = productOptionValueEdit;
      // verify the required parameter 'login' is set
      if (login === undefined || login === null) {
        throw new Error("Missing the required parameter 'login' when calling productsIdOptionsOptionIdValuesJsonPost");
      }
      // verify the required parameter 'authtoken' is set
      if (authtoken === undefined || authtoken === null) {
        throw new Error("Missing the required parameter 'authtoken' when calling productsIdOptionsOptionIdValuesJsonPost");
      }
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling productsIdOptionsOptionIdValuesJsonPost");
      }
      // verify the required parameter 'optionId' is set
      if (optionId === undefined || optionId === null) {
        throw new Error("Missing the required parameter 'optionId' when calling productsIdOptionsOptionIdValuesJsonPost");
      }
      // verify the required parameter 'productOptionValueEdit' is set
      if (productOptionValueEdit === undefined || productOptionValueEdit === null) {
        throw new Error("Missing the required parameter 'productOptionValueEdit' when calling productsIdOptionsOptionIdValuesJsonPost");
      }

      let pathParams = {
        'id': id,
        'option_id': optionId
      };
      let queryParams = {
        'login': login,
        'authtoken': authtoken
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ProductOptionValue;
      return this.apiClient.callApi(
        '/products/{id}/options/{option_id}/values.json', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the productsIdOptionsOptionIdValuesValueIdJsonDelete operation.
     * @callback module:api/ProductOptionValuesApi~productsIdOptionsOptionIdValuesValueIdJsonDeleteCallback
     * @param {String} error Error message, if any.
     * @param {String} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete a Product Option Value.
     * @param {String} login API OAuth login.
     * @param {String} authtoken API OAuth token.
     * @param {Number} id Id of the Product
     * @param {Number} optionId Id of the Product Option
     * @param {Number} valueId ID of the Product Option Value
     * @param {module:api/ProductOptionValuesApi~productsIdOptionsOptionIdValuesValueIdJsonDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link String}
     */
    productsIdOptionsOptionIdValuesValueIdJsonDelete(login, authtoken, id, optionId, valueId, callback) {
      let postBody = null;
      // verify the required parameter 'login' is set
      if (login === undefined || login === null) {
        throw new Error("Missing the required parameter 'login' when calling productsIdOptionsOptionIdValuesValueIdJsonDelete");
      }
      // verify the required parameter 'authtoken' is set
      if (authtoken === undefined || authtoken === null) {
        throw new Error("Missing the required parameter 'authtoken' when calling productsIdOptionsOptionIdValuesValueIdJsonDelete");
      }
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling productsIdOptionsOptionIdValuesValueIdJsonDelete");
      }
      // verify the required parameter 'optionId' is set
      if (optionId === undefined || optionId === null) {
        throw new Error("Missing the required parameter 'optionId' when calling productsIdOptionsOptionIdValuesValueIdJsonDelete");
      }
      // verify the required parameter 'valueId' is set
      if (valueId === undefined || valueId === null) {
        throw new Error("Missing the required parameter 'valueId' when calling productsIdOptionsOptionIdValuesValueIdJsonDelete");
      }

      let pathParams = {
        'id': id,
        'option_id': optionId,
        'value_id': valueId
      };
      let queryParams = {
        'login': login,
        'authtoken': authtoken
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = 'String';
      return this.apiClient.callApi(
        '/products/{id}/options/{option_id}/values/{value_id}.json', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the productsIdOptionsOptionIdValuesValueIdJsonGet operation.
     * @callback module:api/ProductOptionValuesApi~productsIdOptionsOptionIdValuesValueIdJsonGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ProductOptionValue} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve a single Product Option Value.
     * @param {String} login API OAuth login.
     * @param {String} authtoken API OAuth token.
     * @param {Number} id Id of the Product
     * @param {Number} optionId Id of the Product Option
     * @param {Number} valueId ID of the Product Option Value
     * @param {module:api/ProductOptionValuesApi~productsIdOptionsOptionIdValuesValueIdJsonGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ProductOptionValue}
     */
    productsIdOptionsOptionIdValuesValueIdJsonGet(login, authtoken, id, optionId, valueId, callback) {
      let postBody = null;
      // verify the required parameter 'login' is set
      if (login === undefined || login === null) {
        throw new Error("Missing the required parameter 'login' when calling productsIdOptionsOptionIdValuesValueIdJsonGet");
      }
      // verify the required parameter 'authtoken' is set
      if (authtoken === undefined || authtoken === null) {
        throw new Error("Missing the required parameter 'authtoken' when calling productsIdOptionsOptionIdValuesValueIdJsonGet");
      }
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling productsIdOptionsOptionIdValuesValueIdJsonGet");
      }
      // verify the required parameter 'optionId' is set
      if (optionId === undefined || optionId === null) {
        throw new Error("Missing the required parameter 'optionId' when calling productsIdOptionsOptionIdValuesValueIdJsonGet");
      }
      // verify the required parameter 'valueId' is set
      if (valueId === undefined || valueId === null) {
        throw new Error("Missing the required parameter 'valueId' when calling productsIdOptionsOptionIdValuesValueIdJsonGet");
      }

      let pathParams = {
        'id': id,
        'option_id': optionId,
        'value_id': valueId
      };
      let queryParams = {
        'login': login,
        'authtoken': authtoken
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ProductOptionValue;
      return this.apiClient.callApi(
        '/products/{id}/options/{option_id}/values/{value_id}.json', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the productsIdOptionsOptionIdValuesValueIdJsonPut operation.
     * @callback module:api/ProductOptionValuesApi~productsIdOptionsOptionIdValuesValueIdJsonPutCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ProductOptionValue} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Modify an existing Product Option Value.
     * @param {String} login API OAuth login.
     * @param {String} authtoken API OAuth token.
     * @param {Number} id Id of the Product
     * @param {Number} optionId Id of the Product Option
     * @param {Number} valueId Id of the Product Option Value
     * @param {module:model/ProductOptionValueEdit} productOptionValueEdit Product option value parameters to change
     * @param {module:api/ProductOptionValuesApi~productsIdOptionsOptionIdValuesValueIdJsonPutCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ProductOptionValue}
     */
    productsIdOptionsOptionIdValuesValueIdJsonPut(login, authtoken, id, optionId, valueId, productOptionValueEdit, callback) {
      let postBody = productOptionValueEdit;
      // verify the required parameter 'login' is set
      if (login === undefined || login === null) {
        throw new Error("Missing the required parameter 'login' when calling productsIdOptionsOptionIdValuesValueIdJsonPut");
      }
      // verify the required parameter 'authtoken' is set
      if (authtoken === undefined || authtoken === null) {
        throw new Error("Missing the required parameter 'authtoken' when calling productsIdOptionsOptionIdValuesValueIdJsonPut");
      }
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling productsIdOptionsOptionIdValuesValueIdJsonPut");
      }
      // verify the required parameter 'optionId' is set
      if (optionId === undefined || optionId === null) {
        throw new Error("Missing the required parameter 'optionId' when calling productsIdOptionsOptionIdValuesValueIdJsonPut");
      }
      // verify the required parameter 'valueId' is set
      if (valueId === undefined || valueId === null) {
        throw new Error("Missing the required parameter 'valueId' when calling productsIdOptionsOptionIdValuesValueIdJsonPut");
      }
      // verify the required parameter 'productOptionValueEdit' is set
      if (productOptionValueEdit === undefined || productOptionValueEdit === null) {
        throw new Error("Missing the required parameter 'productOptionValueEdit' when calling productsIdOptionsOptionIdValuesValueIdJsonPut");
      }

      let pathParams = {
        'id': id,
        'option_id': optionId,
        'value_id': valueId
      };
      let queryParams = {
        'login': login,
        'authtoken': authtoken
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ProductOptionValue;
      return this.apiClient.callApi(
        '/products/{id}/options/{option_id}/values/{value_id}.json', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
