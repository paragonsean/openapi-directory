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
import Customer from '../model/Customer';
import CustomerWithPasswordNoID from '../model/CustomerWithPasswordNoID';
import NotFound from '../model/NotFound';

/**
* Customers service.
* @module api/CustomersApi
* @version 1.0.0
*/
export default class CustomersApi {

    /**
    * Constructs a new CustomersApi. 
    * @alias module:api/CustomersApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the customersCountJsonGet operation.
     * @callback module:api/CustomersApi~customersCountJsonGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Count} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Count all Customers.
     * @param {String} login API OAuth login.
     * @param {String} authtoken API OAuth token.
     * @param {module:api/CustomersApi~customersCountJsonGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Count}
     */
    customersCountJsonGet(login, authtoken, callback) {
      let postBody = null;
      // verify the required parameter 'login' is set
      if (login === undefined || login === null) {
        throw new Error("Missing the required parameter 'login' when calling customersCountJsonGet");
      }
      // verify the required parameter 'authtoken' is set
      if (authtoken === undefined || authtoken === null) {
        throw new Error("Missing the required parameter 'authtoken' when calling customersCountJsonGet");
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
        '/customers/count.json', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the customersEmailEmailJsonGet operation.
     * @callback module:api/CustomersApi~customersEmailEmailJsonGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Customer} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve a single Customer by email.
     * @param {String} login API OAuth login.
     * @param {String} authtoken API OAuth token.
     * @param {String} email Email of the Customer
     * @param {module:api/CustomersApi~customersEmailEmailJsonGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Customer}
     */
    customersEmailEmailJsonGet(login, authtoken, email, callback) {
      let postBody = null;
      // verify the required parameter 'login' is set
      if (login === undefined || login === null) {
        throw new Error("Missing the required parameter 'login' when calling customersEmailEmailJsonGet");
      }
      // verify the required parameter 'authtoken' is set
      if (authtoken === undefined || authtoken === null) {
        throw new Error("Missing the required parameter 'authtoken' when calling customersEmailEmailJsonGet");
      }
      // verify the required parameter 'email' is set
      if (email === undefined || email === null) {
        throw new Error("Missing the required parameter 'email' when calling customersEmailEmailJsonGet");
      }

      let pathParams = {
        'email': email
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
      let returnType = Customer;
      return this.apiClient.callApi(
        '/customers/email/{email}.json', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the customersIdJsonDelete operation.
     * @callback module:api/CustomersApi~customersIdJsonDeleteCallback
     * @param {String} error Error message, if any.
     * @param {String} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete an existing Customer.
     * @param {String} login API OAuth login.
     * @param {String} authtoken API OAuth token.
     * @param {Number} id Id of the Customer
     * @param {module:api/CustomersApi~customersIdJsonDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link String}
     */
    customersIdJsonDelete(login, authtoken, id, callback) {
      let postBody = null;
      // verify the required parameter 'login' is set
      if (login === undefined || login === null) {
        throw new Error("Missing the required parameter 'login' when calling customersIdJsonDelete");
      }
      // verify the required parameter 'authtoken' is set
      if (authtoken === undefined || authtoken === null) {
        throw new Error("Missing the required parameter 'authtoken' when calling customersIdJsonDelete");
      }
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling customersIdJsonDelete");
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
        '/customers/{id}.json', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the customersIdJsonGet operation.
     * @callback module:api/CustomersApi~customersIdJsonGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Customer} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve a single Customer by id.
     * @param {String} login API OAuth login.
     * @param {String} authtoken API OAuth token.
     * @param {Number} id Id of the Customer
     * @param {module:api/CustomersApi~customersIdJsonGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Customer}
     */
    customersIdJsonGet(login, authtoken, id, callback) {
      let postBody = null;
      // verify the required parameter 'login' is set
      if (login === undefined || login === null) {
        throw new Error("Missing the required parameter 'login' when calling customersIdJsonGet");
      }
      // verify the required parameter 'authtoken' is set
      if (authtoken === undefined || authtoken === null) {
        throw new Error("Missing the required parameter 'authtoken' when calling customersIdJsonGet");
      }
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling customersIdJsonGet");
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
      let returnType = Customer;
      return this.apiClient.callApi(
        '/customers/{id}.json', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the customersIdJsonPut operation.
     * @callback module:api/CustomersApi~customersIdJsonPutCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Customer} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update a new Customer.
     * @param {String} login API OAuth login.
     * @param {String} authtoken API OAuth token.
     * @param {Number} id Id of the Customer
     * @param {module:model/CustomerWithPasswordNoID} customerWithPasswordNoID Customer parameters.
     * @param {module:api/CustomersApi~customersIdJsonPutCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Customer}
     */
    customersIdJsonPut(login, authtoken, id, customerWithPasswordNoID, callback) {
      let postBody = customerWithPasswordNoID;
      // verify the required parameter 'login' is set
      if (login === undefined || login === null) {
        throw new Error("Missing the required parameter 'login' when calling customersIdJsonPut");
      }
      // verify the required parameter 'authtoken' is set
      if (authtoken === undefined || authtoken === null) {
        throw new Error("Missing the required parameter 'authtoken' when calling customersIdJsonPut");
      }
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling customersIdJsonPut");
      }
      // verify the required parameter 'customerWithPasswordNoID' is set
      if (customerWithPasswordNoID === undefined || customerWithPasswordNoID === null) {
        throw new Error("Missing the required parameter 'customerWithPasswordNoID' when calling customersIdJsonPut");
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
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = Customer;
      return this.apiClient.callApi(
        '/customers/{id}.json', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the customersJsonGet operation.
     * @callback module:api/CustomersApi~customersJsonGetCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/Customer>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve all Customers.
     * @param {String} login API OAuth login.
     * @param {String} authtoken API OAuth token.
     * @param {Object} opts Optional parameters
     * @param {Number} [limit = 50)] List restriction
     * @param {Number} [page = 1)] List page
     * @param {module:api/CustomersApi~customersJsonGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/Customer>}
     */
    customersJsonGet(login, authtoken, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'login' is set
      if (login === undefined || login === null) {
        throw new Error("Missing the required parameter 'login' when calling customersJsonGet");
      }
      // verify the required parameter 'authtoken' is set
      if (authtoken === undefined || authtoken === null) {
        throw new Error("Missing the required parameter 'authtoken' when calling customersJsonGet");
      }

      let pathParams = {
      };
      let queryParams = {
        'login': login,
        'authtoken': authtoken,
        'limit': opts['limit'],
        'page': opts['page']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [Customer];
      return this.apiClient.callApi(
        '/customers.json', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the customersJsonPost operation.
     * @callback module:api/CustomersApi~customersJsonPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Customer} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a new Customer.
     * @param {String} login API OAuth login.
     * @param {String} authtoken API OAuth token.
     * @param {module:model/CustomerWithPasswordNoID} customerWithPasswordNoID Customer parameters.
     * @param {module:api/CustomersApi~customersJsonPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Customer}
     */
    customersJsonPost(login, authtoken, customerWithPasswordNoID, callback) {
      let postBody = customerWithPasswordNoID;
      // verify the required parameter 'login' is set
      if (login === undefined || login === null) {
        throw new Error("Missing the required parameter 'login' when calling customersJsonPost");
      }
      // verify the required parameter 'authtoken' is set
      if (authtoken === undefined || authtoken === null) {
        throw new Error("Missing the required parameter 'authtoken' when calling customersJsonPost");
      }
      // verify the required parameter 'customerWithPasswordNoID' is set
      if (customerWithPasswordNoID === undefined || customerWithPasswordNoID === null) {
        throw new Error("Missing the required parameter 'customerWithPasswordNoID' when calling customersJsonPost");
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
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = Customer;
      return this.apiClient.callApi(
        '/customers.json', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
