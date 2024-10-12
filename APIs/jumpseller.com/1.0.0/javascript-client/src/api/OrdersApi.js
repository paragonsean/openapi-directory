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
import Order from '../model/Order';
import OrderCreate from '../model/OrderCreate';
import OrderEdit from '../model/OrderEdit';
import OrderHistory from '../model/OrderHistory';
import OrderHistoryEdit from '../model/OrderHistoryEdit';
import StatusInvalid from '../model/StatusInvalid';

/**
* Orders service.
* @module api/OrdersApi
* @version 1.0.0
*/
export default class OrdersApi {

    /**
    * Constructs a new OrdersApi. 
    * @alias module:api/OrdersApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the ordersAfterIdJsonGet operation.
     * @callback module:api/OrdersApi~ordersAfterIdJsonGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Order} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve orders filtered by Order Id.
     * For example the GET /orders/after/5000 will return Order 5001, 5002, 5003, etc.
     * @param {String} login API OAuth login.
     * @param {String} authtoken API OAuth token.
     * @param {Number} id Id of the Order
     * @param {module:api/OrdersApi~ordersAfterIdJsonGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Order}
     */
    ordersAfterIdJsonGet(login, authtoken, id, callback) {
      let postBody = null;
      // verify the required parameter 'login' is set
      if (login === undefined || login === null) {
        throw new Error("Missing the required parameter 'login' when calling ordersAfterIdJsonGet");
      }
      // verify the required parameter 'authtoken' is set
      if (authtoken === undefined || authtoken === null) {
        throw new Error("Missing the required parameter 'authtoken' when calling ordersAfterIdJsonGet");
      }
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling ordersAfterIdJsonGet");
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
      let returnType = Order;
      return this.apiClient.callApi(
        '/orders/after/{id}.json', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the ordersCountJsonGet operation.
     * @callback module:api/OrdersApi~ordersCountJsonGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Count} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Count all Orders.
     * @param {String} login API OAuth login.
     * @param {String} authtoken API OAuth token.
     * @param {module:api/OrdersApi~ordersCountJsonGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Count}
     */
    ordersCountJsonGet(login, authtoken, callback) {
      let postBody = null;
      // verify the required parameter 'login' is set
      if (login === undefined || login === null) {
        throw new Error("Missing the required parameter 'login' when calling ordersCountJsonGet");
      }
      // verify the required parameter 'authtoken' is set
      if (authtoken === undefined || authtoken === null) {
        throw new Error("Missing the required parameter 'authtoken' when calling ordersCountJsonGet");
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
        '/orders/count.json', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the ordersIdHistoryJsonGet operation.
     * @callback module:api/OrdersApi~ordersIdHistoryJsonGetCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/OrderHistory>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve all Order History.
     * @param {String} login API OAuth login.
     * @param {String} authtoken API OAuth token.
     * @param {Number} id Id of the Order
     * @param {module:api/OrdersApi~ordersIdHistoryJsonGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/OrderHistory>}
     */
    ordersIdHistoryJsonGet(login, authtoken, id, callback) {
      let postBody = null;
      // verify the required parameter 'login' is set
      if (login === undefined || login === null) {
        throw new Error("Missing the required parameter 'login' when calling ordersIdHistoryJsonGet");
      }
      // verify the required parameter 'authtoken' is set
      if (authtoken === undefined || authtoken === null) {
        throw new Error("Missing the required parameter 'authtoken' when calling ordersIdHistoryJsonGet");
      }
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling ordersIdHistoryJsonGet");
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
      let returnType = [OrderHistory];
      return this.apiClient.callApi(
        '/orders/{id}/history.json', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the ordersIdHistoryJsonPost operation.
     * @callback module:api/OrdersApi~ordersIdHistoryJsonPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/OrderHistory} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a new Order History Entry.
     * @param {String} login API OAuth login.
     * @param {String} authtoken API OAuth token.
     * @param {Number} id Id of the OrderHistory
     * @param {module:model/OrderHistoryEdit} orderHistoryEdit Order History parameters.
     * @param {module:api/OrdersApi~ordersIdHistoryJsonPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/OrderHistory}
     */
    ordersIdHistoryJsonPost(login, authtoken, id, orderHistoryEdit, callback) {
      let postBody = orderHistoryEdit;
      // verify the required parameter 'login' is set
      if (login === undefined || login === null) {
        throw new Error("Missing the required parameter 'login' when calling ordersIdHistoryJsonPost");
      }
      // verify the required parameter 'authtoken' is set
      if (authtoken === undefined || authtoken === null) {
        throw new Error("Missing the required parameter 'authtoken' when calling ordersIdHistoryJsonPost");
      }
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling ordersIdHistoryJsonPost");
      }
      // verify the required parameter 'orderHistoryEdit' is set
      if (orderHistoryEdit === undefined || orderHistoryEdit === null) {
        throw new Error("Missing the required parameter 'orderHistoryEdit' when calling ordersIdHistoryJsonPost");
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
      let returnType = OrderHistory;
      return this.apiClient.callApi(
        '/orders/{id}/history.json', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the ordersIdJsonGet operation.
     * @callback module:api/OrdersApi~ordersIdJsonGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Order} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve a single Order.
     * @param {String} login API OAuth login.
     * @param {String} authtoken API OAuth token.
     * @param {Number} id Id of the Order
     * @param {module:api/OrdersApi~ordersIdJsonGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Order}
     */
    ordersIdJsonGet(login, authtoken, id, callback) {
      let postBody = null;
      // verify the required parameter 'login' is set
      if (login === undefined || login === null) {
        throw new Error("Missing the required parameter 'login' when calling ordersIdJsonGet");
      }
      // verify the required parameter 'authtoken' is set
      if (authtoken === undefined || authtoken === null) {
        throw new Error("Missing the required parameter 'authtoken' when calling ordersIdJsonGet");
      }
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling ordersIdJsonGet");
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
      let returnType = Order;
      return this.apiClient.callApi(
        '/orders/{id}.json', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the ordersIdJsonPut operation.
     * @callback module:api/OrdersApi~ordersIdJsonPutCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Order} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Modify an existing Order.
     * Only `status`, `shipment_status`, `tracking_number`, `tracking_company`, `tracking_url`, `additional_information` and `additional_fields` are available for update. An email is send if `shipment_status` changes.
     * @param {String} login API OAuth login.
     * @param {String} authtoken API OAuth token.
     * @param {Number} id Id of the Order
     * @param {module:model/OrderEdit} orderEdit Order parameters to change
     * @param {module:api/OrdersApi~ordersIdJsonPutCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Order}
     */
    ordersIdJsonPut(login, authtoken, id, orderEdit, callback) {
      let postBody = orderEdit;
      // verify the required parameter 'login' is set
      if (login === undefined || login === null) {
        throw new Error("Missing the required parameter 'login' when calling ordersIdJsonPut");
      }
      // verify the required parameter 'authtoken' is set
      if (authtoken === undefined || authtoken === null) {
        throw new Error("Missing the required parameter 'authtoken' when calling ordersIdJsonPut");
      }
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling ordersIdJsonPut");
      }
      // verify the required parameter 'orderEdit' is set
      if (orderEdit === undefined || orderEdit === null) {
        throw new Error("Missing the required parameter 'orderEdit' when calling ordersIdJsonPut");
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
      let returnType = Order;
      return this.apiClient.callApi(
        '/orders/{id}.json', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the ordersJsonGet operation.
     * @callback module:api/OrdersApi~ordersJsonGetCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/Order>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve all Orders.
     * @param {String} login API OAuth login.
     * @param {String} authtoken API OAuth token.
     * @param {Object} opts Optional parameters
     * @param {Number} [limit = 50)] List restriction
     * @param {Number} [page = 1)] List page
     * @param {module:api/OrdersApi~ordersJsonGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/Order>}
     */
    ordersJsonGet(login, authtoken, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'login' is set
      if (login === undefined || login === null) {
        throw new Error("Missing the required parameter 'login' when calling ordersJsonGet");
      }
      // verify the required parameter 'authtoken' is set
      if (authtoken === undefined || authtoken === null) {
        throw new Error("Missing the required parameter 'authtoken' when calling ordersJsonGet");
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
      let returnType = [Order];
      return this.apiClient.callApi(
        '/orders.json', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the ordersJsonPost operation.
     * @callback module:api/OrdersApi~ordersJsonPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Order} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a new Order.
     * Orders created externally keep the given order product's values (bypassing internal promotion or product amounts).
     * @param {String} login API OAuth login.
     * @param {String} authtoken API OAuth token.
     * @param {module:model/OrderCreate} orderCreate Order parameters.
     * @param {module:api/OrdersApi~ordersJsonPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Order}
     */
    ordersJsonPost(login, authtoken, orderCreate, callback) {
      let postBody = orderCreate;
      // verify the required parameter 'login' is set
      if (login === undefined || login === null) {
        throw new Error("Missing the required parameter 'login' when calling ordersJsonPost");
      }
      // verify the required parameter 'authtoken' is set
      if (authtoken === undefined || authtoken === null) {
        throw new Error("Missing the required parameter 'authtoken' when calling ordersJsonPost");
      }
      // verify the required parameter 'orderCreate' is set
      if (orderCreate === undefined || orderCreate === null) {
        throw new Error("Missing the required parameter 'orderCreate' when calling ordersJsonPost");
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
      let returnType = Order;
      return this.apiClient.callApi(
        '/orders.json', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the ordersStatusStatusJsonGet operation.
     * @callback module:api/OrdersApi~ordersStatusStatusJsonGetCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/Order>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve orders filtered by status.
     * @param {String} login API OAuth login.
     * @param {String} authtoken API OAuth token.
     * @param {module:model/String} status Status of the Order used as filter
     * @param {module:api/OrdersApi~ordersStatusStatusJsonGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/Order>}
     */
    ordersStatusStatusJsonGet(login, authtoken, status, callback) {
      let postBody = null;
      // verify the required parameter 'login' is set
      if (login === undefined || login === null) {
        throw new Error("Missing the required parameter 'login' when calling ordersStatusStatusJsonGet");
      }
      // verify the required parameter 'authtoken' is set
      if (authtoken === undefined || authtoken === null) {
        throw new Error("Missing the required parameter 'authtoken' when calling ordersStatusStatusJsonGet");
      }
      // verify the required parameter 'status' is set
      if (status === undefined || status === null) {
        throw new Error("Missing the required parameter 'status' when calling ordersStatusStatusJsonGet");
      }

      let pathParams = {
        'status': status
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
      let returnType = [Order];
      return this.apiClient.callApi(
        '/orders/status/{status}.json', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
