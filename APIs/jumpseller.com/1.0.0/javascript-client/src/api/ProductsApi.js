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
import Product from '../model/Product';
import ProductEdit from '../model/ProductEdit';
import StatusInvalid from '../model/StatusInvalid';

/**
* Products service.
* @module api/ProductsApi
* @version 1.0.0
*/
export default class ProductsApi {

    /**
    * Constructs a new ProductsApi. 
    * @alias module:api/ProductsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the productsAfterIdJsonGet operation.
     * @callback module:api/ProductsApi~productsAfterIdJsonGetCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/Product>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieves Products after the given id.
     * @param {String} login API OAuth login.
     * @param {String} authtoken API OAuth token.
     * @param {Number} id Id of the Product
     * @param {Object} opts Optional parameters
     * @param {String} [locale] Locale code of the translation
     * @param {module:api/ProductsApi~productsAfterIdJsonGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/Product>}
     */
    productsAfterIdJsonGet(login, authtoken, id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'login' is set
      if (login === undefined || login === null) {
        throw new Error("Missing the required parameter 'login' when calling productsAfterIdJsonGet");
      }
      // verify the required parameter 'authtoken' is set
      if (authtoken === undefined || authtoken === null) {
        throw new Error("Missing the required parameter 'authtoken' when calling productsAfterIdJsonGet");
      }
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling productsAfterIdJsonGet");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'login': login,
        'authtoken': authtoken,
        'locale': opts['locale']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [Product];
      return this.apiClient.callApi(
        '/products/after/{id}.json', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the productsCategoryCategoryIdCountJsonGet operation.
     * @callback module:api/ProductsApi~productsCategoryCategoryIdCountJsonGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Count} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Count Products filtered by category.
     * @param {String} login API OAuth login.
     * @param {String} authtoken API OAuth token.
     * @param {Number} categoryId Category ID of the Product used as filter
     * @param {Object} opts Optional parameters
     * @param {String} [locale] Locale code of the translation
     * @param {module:api/ProductsApi~productsCategoryCategoryIdCountJsonGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Count}
     */
    productsCategoryCategoryIdCountJsonGet(login, authtoken, categoryId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'login' is set
      if (login === undefined || login === null) {
        throw new Error("Missing the required parameter 'login' when calling productsCategoryCategoryIdCountJsonGet");
      }
      // verify the required parameter 'authtoken' is set
      if (authtoken === undefined || authtoken === null) {
        throw new Error("Missing the required parameter 'authtoken' when calling productsCategoryCategoryIdCountJsonGet");
      }
      // verify the required parameter 'categoryId' is set
      if (categoryId === undefined || categoryId === null) {
        throw new Error("Missing the required parameter 'categoryId' when calling productsCategoryCategoryIdCountJsonGet");
      }

      let pathParams = {
        'category_id': categoryId
      };
      let queryParams = {
        'login': login,
        'authtoken': authtoken,
        'locale': opts['locale']
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
        '/products/category/{category_id}/count.json', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the productsCategoryCategoryIdJsonGet operation.
     * @callback module:api/ProductsApi~productsCategoryCategoryIdJsonGetCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/Product>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve Products filtered by category.
     * @param {String} login API OAuth login.
     * @param {String} authtoken API OAuth token.
     * @param {Number} categoryId Category ID of the Product used as filter
     * @param {Object} opts Optional parameters
     * @param {String} [locale] Locale code of the translation
     * @param {module:api/ProductsApi~productsCategoryCategoryIdJsonGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/Product>}
     */
    productsCategoryCategoryIdJsonGet(login, authtoken, categoryId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'login' is set
      if (login === undefined || login === null) {
        throw new Error("Missing the required parameter 'login' when calling productsCategoryCategoryIdJsonGet");
      }
      // verify the required parameter 'authtoken' is set
      if (authtoken === undefined || authtoken === null) {
        throw new Error("Missing the required parameter 'authtoken' when calling productsCategoryCategoryIdJsonGet");
      }
      // verify the required parameter 'categoryId' is set
      if (categoryId === undefined || categoryId === null) {
        throw new Error("Missing the required parameter 'categoryId' when calling productsCategoryCategoryIdJsonGet");
      }

      let pathParams = {
        'category_id': categoryId
      };
      let queryParams = {
        'login': login,
        'authtoken': authtoken,
        'locale': opts['locale']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [Product];
      return this.apiClient.callApi(
        '/products/category/{category_id}.json', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the productsCountJsonGet operation.
     * @callback module:api/ProductsApi~productsCountJsonGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Count} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Count all Products.
     * @param {String} login API OAuth login.
     * @param {String} authtoken API OAuth token.
     * @param {module:api/ProductsApi~productsCountJsonGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Count}
     */
    productsCountJsonGet(login, authtoken, callback) {
      let postBody = null;
      // verify the required parameter 'login' is set
      if (login === undefined || login === null) {
        throw new Error("Missing the required parameter 'login' when calling productsCountJsonGet");
      }
      // verify the required parameter 'authtoken' is set
      if (authtoken === undefined || authtoken === null) {
        throw new Error("Missing the required parameter 'authtoken' when calling productsCountJsonGet");
      }

      let pathParams = {
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
        '/products/count.json', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the productsIdJsonDelete operation.
     * @callback module:api/ProductsApi~productsIdJsonDeleteCallback
     * @param {String} error Error message, if any.
     * @param {String} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete an existing Product.
     * @param {String} login API OAuth login.
     * @param {String} authtoken API OAuth token.
     * @param {Number} id Id of the Product
     * @param {module:api/ProductsApi~productsIdJsonDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link String}
     */
    productsIdJsonDelete(login, authtoken, id, callback) {
      let postBody = null;
      // verify the required parameter 'login' is set
      if (login === undefined || login === null) {
        throw new Error("Missing the required parameter 'login' when calling productsIdJsonDelete");
      }
      // verify the required parameter 'authtoken' is set
      if (authtoken === undefined || authtoken === null) {
        throw new Error("Missing the required parameter 'authtoken' when calling productsIdJsonDelete");
      }
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling productsIdJsonDelete");
      }

      let pathParams = {
        'id': id
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
        '/products/{id}.json', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the productsIdJsonGet operation.
     * @callback module:api/ProductsApi~productsIdJsonGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Product} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve a single Product.
     * @param {String} login API OAuth login.
     * @param {String} authtoken API OAuth token.
     * @param {Number} id ID of the Product
     * @param {Object} opts Optional parameters
     * @param {String} [locale] Locale code of the translation
     * @param {module:api/ProductsApi~productsIdJsonGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Product}
     */
    productsIdJsonGet(login, authtoken, id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'login' is set
      if (login === undefined || login === null) {
        throw new Error("Missing the required parameter 'login' when calling productsIdJsonGet");
      }
      // verify the required parameter 'authtoken' is set
      if (authtoken === undefined || authtoken === null) {
        throw new Error("Missing the required parameter 'authtoken' when calling productsIdJsonGet");
      }
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling productsIdJsonGet");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'login': login,
        'authtoken': authtoken,
        'locale': opts['locale']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Product;
      return this.apiClient.callApi(
        '/products/{id}.json', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the productsIdJsonPut operation.
     * @callback module:api/ProductsApi~productsIdJsonPutCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Product} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Modify an existing Product.
     * @param {String} login API OAuth login.
     * @param {String} authtoken API OAuth token.
     * @param {Number} id Id of the Product
     * @param {module:model/ProductEdit} productEdit Product parameters to change
     * @param {Object} opts Optional parameters
     * @param {String} [locale] Locale code of the translation
     * @param {module:api/ProductsApi~productsIdJsonPutCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Product}
     */
    productsIdJsonPut(login, authtoken, id, productEdit, opts, callback) {
      opts = opts || {};
      let postBody = productEdit;
      // verify the required parameter 'login' is set
      if (login === undefined || login === null) {
        throw new Error("Missing the required parameter 'login' when calling productsIdJsonPut");
      }
      // verify the required parameter 'authtoken' is set
      if (authtoken === undefined || authtoken === null) {
        throw new Error("Missing the required parameter 'authtoken' when calling productsIdJsonPut");
      }
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling productsIdJsonPut");
      }
      // verify the required parameter 'productEdit' is set
      if (productEdit === undefined || productEdit === null) {
        throw new Error("Missing the required parameter 'productEdit' when calling productsIdJsonPut");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'login': login,
        'authtoken': authtoken,
        'locale': opts['locale']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = Product;
      return this.apiClient.callApi(
        '/products/{id}.json', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the productsJsonGet operation.
     * @callback module:api/ProductsApi~productsJsonGetCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/Product>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve all Products.
     * @param {String} login API OAuth login.
     * @param {String} authtoken API OAuth token.
     * @param {Object} opts Optional parameters
     * @param {Number} [limit = 50)] List restriction
     * @param {Number} [page = 1)] List page
     * @param {String} [locale] Locale code of the translation
     * @param {module:api/ProductsApi~productsJsonGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/Product>}
     */
    productsJsonGet(login, authtoken, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'login' is set
      if (login === undefined || login === null) {
        throw new Error("Missing the required parameter 'login' when calling productsJsonGet");
      }
      // verify the required parameter 'authtoken' is set
      if (authtoken === undefined || authtoken === null) {
        throw new Error("Missing the required parameter 'authtoken' when calling productsJsonGet");
      }

      let pathParams = {
      };
      let queryParams = {
        'login': login,
        'authtoken': authtoken,
        'limit': opts['limit'],
        'page': opts['page'],
        'locale': opts['locale']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [Product];
      return this.apiClient.callApi(
        '/products.json', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the productsJsonPost operation.
     * @callback module:api/ProductsApi~productsJsonPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Product} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a new Product.
     * @param {String} login API OAuth login.
     * @param {String} authtoken API OAuth token.
     * @param {module:model/ProductEdit} productEdit Product parameters.
     * @param {Object} opts Optional parameters
     * @param {String} [locale] Locale code of the translation
     * @param {module:api/ProductsApi~productsJsonPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Product}
     */
    productsJsonPost(login, authtoken, productEdit, opts, callback) {
      opts = opts || {};
      let postBody = productEdit;
      // verify the required parameter 'login' is set
      if (login === undefined || login === null) {
        throw new Error("Missing the required parameter 'login' when calling productsJsonPost");
      }
      // verify the required parameter 'authtoken' is set
      if (authtoken === undefined || authtoken === null) {
        throw new Error("Missing the required parameter 'authtoken' when calling productsJsonPost");
      }
      // verify the required parameter 'productEdit' is set
      if (productEdit === undefined || productEdit === null) {
        throw new Error("Missing the required parameter 'productEdit' when calling productsJsonPost");
      }

      let pathParams = {
      };
      let queryParams = {
        'login': login,
        'authtoken': authtoken,
        'locale': opts['locale']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = Product;
      return this.apiClient.callApi(
        '/products.json', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the productsSearchJsonGet operation.
     * @callback module:api/ProductsApi~productsSearchJsonGetCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/Product>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve a Product List from a query.
     * Endpoint example:   ```text https://api.jumpseller.com/v1/products/search.json?login=XXXXXX&authtoken=XXXXX&query=test&fields=name,description  ```
     * @param {String} login API OAuth login.
     * @param {String} authtoken API OAuth token.
     * @param {String} query Text to query for the Product
     * @param {Object} opts Optional parameters
     * @param {String} [locale] Locale code of the translation
     * @param {module:model/String} [fields] Comma separated values of the fields to query for the Product
     * @param {module:api/ProductsApi~productsSearchJsonGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/Product>}
     */
    productsSearchJsonGet(login, authtoken, query, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'login' is set
      if (login === undefined || login === null) {
        throw new Error("Missing the required parameter 'login' when calling productsSearchJsonGet");
      }
      // verify the required parameter 'authtoken' is set
      if (authtoken === undefined || authtoken === null) {
        throw new Error("Missing the required parameter 'authtoken' when calling productsSearchJsonGet");
      }
      // verify the required parameter 'query' is set
      if (query === undefined || query === null) {
        throw new Error("Missing the required parameter 'query' when calling productsSearchJsonGet");
      }

      let pathParams = {
      };
      let queryParams = {
        'login': login,
        'authtoken': authtoken,
        'locale': opts['locale'],
        'query': query,
        'fields': opts['fields']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [Product];
      return this.apiClient.callApi(
        '/products/search.json', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the productsStatusStatusCountJsonGet operation.
     * @callback module:api/ProductsApi~productsStatusStatusCountJsonGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Count} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Count Products filtered by status.
     * @param {String} login API OAuth login.
     * @param {String} authtoken API OAuth token.
     * @param {module:model/String} status Status of the Product used as filter
     * @param {Object} opts Optional parameters
     * @param {String} [locale] Locale code of the translation
     * @param {module:api/ProductsApi~productsStatusStatusCountJsonGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Count}
     */
    productsStatusStatusCountJsonGet(login, authtoken, status, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'login' is set
      if (login === undefined || login === null) {
        throw new Error("Missing the required parameter 'login' when calling productsStatusStatusCountJsonGet");
      }
      // verify the required parameter 'authtoken' is set
      if (authtoken === undefined || authtoken === null) {
        throw new Error("Missing the required parameter 'authtoken' when calling productsStatusStatusCountJsonGet");
      }
      // verify the required parameter 'status' is set
      if (status === undefined || status === null) {
        throw new Error("Missing the required parameter 'status' when calling productsStatusStatusCountJsonGet");
      }

      let pathParams = {
        'status': status
      };
      let queryParams = {
        'login': login,
        'authtoken': authtoken,
        'locale': opts['locale']
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
        '/products/status/{status}/count.json', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the productsStatusStatusJsonGet operation.
     * @callback module:api/ProductsApi~productsStatusStatusJsonGetCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/Product>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve Products filtered by status.
     * @param {String} login API OAuth login.
     * @param {String} authtoken API OAuth token.
     * @param {module:model/String} status Status of the Product used as filter
     * @param {Object} opts Optional parameters
     * @param {String} [locale] Locale code of the translation
     * @param {module:api/ProductsApi~productsStatusStatusJsonGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/Product>}
     */
    productsStatusStatusJsonGet(login, authtoken, status, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'login' is set
      if (login === undefined || login === null) {
        throw new Error("Missing the required parameter 'login' when calling productsStatusStatusJsonGet");
      }
      // verify the required parameter 'authtoken' is set
      if (authtoken === undefined || authtoken === null) {
        throw new Error("Missing the required parameter 'authtoken' when calling productsStatusStatusJsonGet");
      }
      // verify the required parameter 'status' is set
      if (status === undefined || status === null) {
        throw new Error("Missing the required parameter 'status' when calling productsStatusStatusJsonGet");
      }

      let pathParams = {
        'status': status
      };
      let queryParams = {
        'login': login,
        'authtoken': authtoken,
        'locale': opts['locale']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [Product];
      return this.apiClient.callApi(
        '/products/status/{status}.json', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
