/**
 * Rebilly REST API
 * # Introduction The Rebilly API is built on HTTP.  Our API is RESTful.  It has predictable resource URLs.  It returns HTTP response codes to indicate errors.  It also accepts and returns JSON in the HTTP body.  You can use your favorite HTTP/REST library for your programming language to use Rebilly's API, or you can use one of our SDKs (currently available in [PHP](https://github.com/Rebilly/rebilly-php) and [Javascript](https://github.com/Rebilly/rebilly-js-sdk)).  We have other APIs that are also available.  Every action from our [app](https://app.rebilly.com) is supported by an API which is documented and available for use so that you may automate any workflows necessary.  This document contains the most commonly integrated resources.  # Authentication  When you sign up for an account, you are given your first secret API key. You can generate additional API keys, and delete API keys (as you may need to rotate your keys in the future). You authenticate to the Rebilly API by providing your secret key in the request header.  Rebilly offers three forms of authentication:  secret key, publishable key, JSON Web Tokens, and public signature key. - [Secret API key](#section/Authentication/SecretApiKey): used for requests made   from the server side. Never share these keys. Keep them guarded and secure. - [Publishable API key](#section/Authentication/PublishableApiKey): used for    requests from the client side. For now can only be used to create    a [Payment Token](#operation/PostToken) and    a [File token](#operation/PostFile). - [JWT](#section/Authentication/JWT): short lifetime tokens that can be assigned a specific expiration time.  Never share your secret keys. Keep them guarded and secure.  &lt;!-- ReDoc-Inject: &lt;security-definitions&gt; --&gt;  # Errors Rebilly follow's the error response format proposed in [RFC 7807](https://tools.ietf.org/html/rfc7807) also known as Problem Details for HTTP APIs.  As with our normal API responses, your client must be prepared to gracefully handle additional members of the response.  ## Forbidden &lt;RedocResponse pointer={\"#/components/responses/Forbidden\"} /&gt;  ## Conflict &lt;RedocResponse pointer={\"#/components/responses/Conflict\"} /&gt;  ## NotFound &lt;RedocResponse pointer={\"#/components/responses/NotFound\"} /&gt;  ## Unauthorized &lt;RedocResponse pointer={\"#/components/responses/Unauthorized\"} /&gt;  ## ValidationError &lt;RedocResponse pointer={\"#/components/responses/ValidationError\"} /&gt;  # SDKs  Rebilly offers a Javascript SDK and a PHP SDK to help interact with the API.  However, no SDK is required to use the API.  Rebilly also offers [FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/),  a client-side iFrame-based solution to help create payment tokens while minimizing PCI DSS compliance burdens and maximizing the customizability. [FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/) is interacting with the [payment tokens creation operation](#operation/PostToken).  ## Javascript SDK  Installation and usage instructions can be found [here](https://docs.rebilly.com/docs/developer-docs/sdks). SDK code examples are included in these docs.  ## PHP SDK For all PHP SDK examples provided in these docs you will need to configure the `$client`. You may do it like this:  ```php $client = new Rebilly\\Client([     'apiKey' =&gt; 'YourApiKeyHere',     'baseUrl' =&gt; 'https://api.rebilly.com', ]); ```  # Using filter with collections Rebilly provides collections filtering. You can use `?filter` param on collections to define which records should be shown in the response.  Here is filter format description:  - Fields and values in filter are separated with `:`: `?filter=firstName:John`.  - Sub-fields are separated with `.`: `?filter=billingAddress.country:US`.  - Multiple filters are separated with `;`: `?filter=firstName:John;lastName:Doe`. They will be joined with `AND` logic. In this example: `firstName:John` AND `lastName:Doe`.  - You can use multiple values using `,` as values separator: `?filter=firstName:John,Bob`. Multiple values specified for a field will be joined with `OR` logic. In this example: `firstName:John` OR `firstName:Bob`.  - To negate the filter use `!`: `?filter=firstName:!John`. Note that you can negate multiple values like this: `?filter=firstName:!John,!Bob`. This filter rule will exclude all Johns and Bobs from the response.  - You can use range filters like this: `?filter=amount:1..10`.  - You can use gte (greater than or equals) filter like this: `?filter=amount:1..`, or lte (less than or equals) than filter like this: `?filter=amount:..10`. This also works for datetime-based fields.  - You can create some [predefined values lists](https://user-api-docs.rebilly.com/#tag/Lists) and use them in filter: `?filter=firstName:@yourListName`. You can also exclude list values: `?filter=firstName:!@yourListName`.  - Datetime-based fields accept values formatted using RFC 3339 like this: `?filter=createdTime:2021-02-14T13:30:00Z`.   # Expand to include embedded objects Rebilly provides the ability to pre-load additional  objects with a request.   You can use `?expand` param on most requests to expand and include embedded objects within the `_embedded` property of the response.  The `_embedded` property contains an array of  objects keyed by the expand parameter value(s).  You may expand multiple objects by passing them as comma-separated to the expand value like so:  ``` ?expand=recentInvoice,customer ```  And in the response, you would see:  ``` \"_embedded\": [     \"recentInvoice\": {...},     \"customer\": {...} ] ``` Expand may be utilitized not only on `GET` requests but also on `PATCH`, `POST`, `PUT` requests too.   # Getting started guide  Rebilly's API has over 300 operations.  That's more than you'll  need to implement your use cases.  If you have a use  case you would like to implement, please consult us for feedback on the best API operations for the task.  Our getting started guide will demonstrate a basic order form use case.  It will allow us to highlight core resources in Rebilly that will be helpful for many other use cases too.  Within 25 minutes, you'll have sent API requests (via our console) to create a subscription order. 
 *
 * The version of the OpenAPI document: 2.1
 * Contact: integrations@rebilly.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import Error from '../model/Error';
import InvalidError from '../model/InvalidError';
import Invoice from '../model/Invoice';
import InvoiceIssue from '../model/InvoiceIssue';
import OrderTimeline from '../model/OrderTimeline';
import Subscription from '../model/Subscription';
import SubscriptionCancellation from '../model/SubscriptionCancellation';
import SubscriptionChange from '../model/SubscriptionChange';
import SubscriptionInvoice from '../model/SubscriptionInvoice';
import SubscriptionReactivation from '../model/SubscriptionReactivation';

/**
* Orders service.
* @module api/OrdersApi
* @version 2.1
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
     * Callback function to receive the result of the deleteSubscriptionCancellation operation.
     * @callback module:api/OrdersApi~deleteSubscriptionCancellationCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete a cancellation
     * Delete an order's cancellation. Only draft can be deleted.
     * @param {String} id The resource identifier string.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/OrdersApi~deleteSubscriptionCancellationCallback} callback The callback function, accepting three arguments: error, data, response
     */
    deleteSubscriptionCancellation(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling deleteSubscriptionCancellation");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
        'Organization-Id': opts['organizationId']
      };
      let formParams = {
      };

      let authNames = ['SecretApiKey', 'JWT'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/subscription-cancellations/{id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteSubscriptionTimeline operation.
     * @callback module:api/OrdersApi~deleteSubscriptionTimelineCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete an Order Timeline message
     * Delete an Order Timeline message with predefined identifier string. 
     * @param {String} id The resource identifier string.
     * @param {String} messageId The Order Timeline message ID.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/OrdersApi~deleteSubscriptionTimelineCallback} callback The callback function, accepting three arguments: error, data, response
     */
    deleteSubscriptionTimeline(id, messageId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling deleteSubscriptionTimeline");
      }
      // verify the required parameter 'messageId' is set
      if (messageId === undefined || messageId === null) {
        throw new Error("Missing the required parameter 'messageId' when calling deleteSubscriptionTimeline");
      }

      let pathParams = {
        'id': id,
        'messageId': messageId
      };
      let queryParams = {
      };
      let headerParams = {
        'Organization-Id': opts['organizationId']
      };
      let formParams = {
      };

      let authNames = ['SecretApiKey', 'JWT'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/subscriptions/{id}/timeline/{messageId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getSubscription operation.
     * @callback module:api/OrdersApi~getSubscriptionCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Subscription} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an order
     * Retrieve an order with specified identifier string. 
     * @param {String} id The resource identifier string.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {String} [expand] Expand a response to get a full related object included inside of the `_embedded` path in the response. To expand multiple objects, it accepts a comma-separated list of objects (example: `expand=recentInvoice,initialInvoice`). Available arguments are:   - recentInvoice   - initialInvoice   - customer   - website  See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info. 
     * @param {module:api/OrdersApi~getSubscriptionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Subscription}
     */
    getSubscription(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getSubscription");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'expand': opts['expand']
      };
      let headerParams = {
        'Organization-Id': opts['organizationId']
      };
      let formParams = {
      };

      let authNames = ['SecretApiKey', 'JWT'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Subscription;
      return this.apiClient.callApi(
        '/subscriptions/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getSubscriptionCancellation operation.
     * @callback module:api/OrdersApi~getSubscriptionCancellationCallback
     * @param {String} error Error message, if any.
     * @param {module:model/SubscriptionCancellation} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an order сancellation
     * Retrieve an order сancellation with specified identifier string.
     * @param {String} id The resource identifier string.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/OrdersApi~getSubscriptionCancellationCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/SubscriptionCancellation}
     */
    getSubscriptionCancellation(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getSubscriptionCancellation");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
        'Organization-Id': opts['organizationId']
      };
      let formParams = {
      };

      let authNames = ['SecretApiKey', 'JWT'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = SubscriptionCancellation;
      return this.apiClient.callApi(
        '/subscription-cancellations/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getSubscriptionCancellationCollection operation.
     * @callback module:api/OrdersApi~getSubscriptionCancellationCollectionCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/SubscriptionCancellation>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve a list of cancellations
     * Retrieve a list of cancellations for all subscriptions.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {Number} [limit] The collection items limit.
     * @param {Number} [offset] The collection items offset.
     * @param {String} [filter] The collection items filter requires a special format. Use \",\" for multiple allowed values.  Use \";\" for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format. 
     * @param {Array.<String>} [sort] The collection items sort field and order (prefix with \"-\" for descending sort).
     * @param {module:api/OrdersApi~getSubscriptionCancellationCollectionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/SubscriptionCancellation>}
     */
    getSubscriptionCancellationCollection(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'limit': opts['limit'],
        'offset': opts['offset'],
        'filter': opts['filter'],
        'sort': this.apiClient.buildCollectionParam(opts['sort'], 'csv')
      };
      let headerParams = {
        'Organization-Id': opts['organizationId']
      };
      let formParams = {
      };

      let authNames = ['SecretApiKey', 'JWT'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [SubscriptionCancellation];
      return this.apiClient.callApi(
        '/subscription-cancellations', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getSubscriptionCollection operation.
     * @callback module:api/OrdersApi~getSubscriptionCollectionCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/Subscription>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve a list of orders
     * Retrieve a list of orders. 
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {String} [filter] The collection items filter requires a special format. Use \",\" for multiple allowed values.  Use \";\" for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format. 
     * @param {Array.<String>} [sort] The collection items sort field and order (prefix with \"-\" for descending sort).
     * @param {Number} [limit] The collection items limit.
     * @param {Number} [offset] The collection items offset.
     * @param {String} [q] The partial search of the text fields.
     * @param {String} [expand] Expand a response to get a full related object included inside of the `_embedded` path in the response. To expand multiple objects, it accepts a comma-separated list of objects (example: `expand=recentInvoice,initialInvoice`). Available arguments are:   - recentInvoice   - initialInvoice   - customer   - website  See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info. 
     * @param {module:api/OrdersApi~getSubscriptionCollectionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/Subscription>}
     */
    getSubscriptionCollection(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'filter': opts['filter'],
        'sort': this.apiClient.buildCollectionParam(opts['sort'], 'csv'),
        'limit': opts['limit'],
        'offset': opts['offset'],
        'q': opts['q'],
        'expand': opts['expand']
      };
      let headerParams = {
        'Organization-Id': opts['organizationId']
      };
      let formParams = {
      };

      let authNames = ['SecretApiKey', 'JWT'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [Subscription];
      return this.apiClient.callApi(
        '/subscriptions', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getSubscriptionReactivation operation.
     * @callback module:api/OrdersApi~getSubscriptionReactivationCallback
     * @param {String} error Error message, if any.
     * @param {module:model/SubscriptionReactivation} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an order reactivation
     * Retrieve an order reactivation with specified identifier string.
     * @param {String} id The resource identifier string.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/OrdersApi~getSubscriptionReactivationCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/SubscriptionReactivation}
     */
    getSubscriptionReactivation(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getSubscriptionReactivation");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
        'Organization-Id': opts['organizationId']
      };
      let formParams = {
      };

      let authNames = ['SecretApiKey', 'JWT'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = SubscriptionReactivation;
      return this.apiClient.callApi(
        '/subscription-reactivations/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getSubscriptionReactivationCollection operation.
     * @callback module:api/OrdersApi~getSubscriptionReactivationCollectionCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/SubscriptionReactivation>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve a list of reactivations
     * Retrieve a list of reactivations for all subscriptions.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {Number} [limit] The collection items limit.
     * @param {Number} [offset] The collection items offset.
     * @param {String} [filter] The collection items filter requires a special format. Use \",\" for multiple allowed values.  Use \";\" for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format. 
     * @param {Array.<String>} [sort] The collection items sort field and order (prefix with \"-\" for descending sort).
     * @param {module:api/OrdersApi~getSubscriptionReactivationCollectionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/SubscriptionReactivation>}
     */
    getSubscriptionReactivationCollection(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'limit': opts['limit'],
        'offset': opts['offset'],
        'filter': opts['filter'],
        'sort': this.apiClient.buildCollectionParam(opts['sort'], 'csv')
      };
      let headerParams = {
        'Organization-Id': opts['organizationId']
      };
      let formParams = {
      };

      let authNames = ['SecretApiKey', 'JWT'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [SubscriptionReactivation];
      return this.apiClient.callApi(
        '/subscription-reactivations', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getSubscriptionTimeline operation.
     * @callback module:api/OrdersApi~getSubscriptionTimelineCallback
     * @param {String} error Error message, if any.
     * @param {module:model/OrderTimeline} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an Order Timeline message
     * Retrieve a order message with specified identifier string. 
     * @param {String} id The resource identifier string.
     * @param {String} messageId The Order Timeline message ID.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/OrdersApi~getSubscriptionTimelineCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/OrderTimeline}
     */
    getSubscriptionTimeline(id, messageId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getSubscriptionTimeline");
      }
      // verify the required parameter 'messageId' is set
      if (messageId === undefined || messageId === null) {
        throw new Error("Missing the required parameter 'messageId' when calling getSubscriptionTimeline");
      }

      let pathParams = {
        'id': id,
        'messageId': messageId
      };
      let queryParams = {
      };
      let headerParams = {
        'Organization-Id': opts['organizationId']
      };
      let formParams = {
      };

      let authNames = ['SecretApiKey', 'JWT'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = OrderTimeline;
      return this.apiClient.callApi(
        '/subscriptions/{id}/timeline/{messageId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getSubscriptionTimelineCollection operation.
     * @callback module:api/OrdersApi~getSubscriptionTimelineCollectionCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/OrderTimeline>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve a list of order timeline messages
     * Retrieve a list of order timeline messages. 
     * @param {String} id The resource identifier string.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {Number} [limit] The collection items limit.
     * @param {Number} [offset] The collection items offset.
     * @param {String} [filter] The collection items filter requires a special format. Use \",\" for multiple allowed values.  Use \";\" for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format. 
     * @param {Array.<String>} [sort] The collection items sort field and order (prefix with \"-\" for descending sort).
     * @param {String} [q] The partial search of the text fields.
     * @param {module:api/OrdersApi~getSubscriptionTimelineCollectionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/OrderTimeline>}
     */
    getSubscriptionTimelineCollection(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getSubscriptionTimelineCollection");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'limit': opts['limit'],
        'offset': opts['offset'],
        'filter': opts['filter'],
        'sort': this.apiClient.buildCollectionParam(opts['sort'], 'csv'),
        'q': opts['q']
      };
      let headerParams = {
        'Organization-Id': opts['organizationId']
      };
      let formParams = {
      };

      let authNames = ['SecretApiKey', 'JWT'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [OrderTimeline];
      return this.apiClient.callApi(
        '/subscriptions/{id}/timeline', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getSubscriptionUpcomingInvoiceCollection operation.
     * @callback module:api/OrdersApi~getSubscriptionUpcomingInvoiceCollectionCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/Invoice>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve subscription order's upcoming invoice
     * Retrieve an upcoming invoice from the specified subscription order. The endpoint is temporary before upcoming invoices get a complete integration. 
     * @param {String} id The resource identifier string.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {String} [expand] Expand a response to get a full related object included inside of the `_embedded` path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info. 
     * @param {module:api/OrdersApi~getSubscriptionUpcomingInvoiceCollectionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/Invoice>}
     */
    getSubscriptionUpcomingInvoiceCollection(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getSubscriptionUpcomingInvoiceCollection");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'expand': opts['expand']
      };
      let headerParams = {
        'Organization-Id': opts['organizationId']
      };
      let formParams = {
      };

      let authNames = ['SecretApiKey', 'JWT'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [Invoice];
      return this.apiClient.callApi(
        '/subscriptions/{id}/upcoming-invoices', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the postSubscription operation.
     * @callback module:api/OrdersApi~postSubscriptionCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Subscription} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create an order
     * Create an order. Consider using the upsert. operation to accomplish this task. 
     * @param {module:model/Subscription} subscription Order resource.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {String} [expand] Expand a response to get a full related object included inside of the `_embedded` path in the response. To expand multiple objects, it accepts a comma-separated list of objects (example: `expand=recentInvoice,initialInvoice`). Available arguments are:   - recentInvoice   - initialInvoice   - customer   - website  See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info. 
     * @param {module:api/OrdersApi~postSubscriptionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Subscription}
     */
    postSubscription(subscription, opts, callback) {
      opts = opts || {};
      let postBody = subscription;
      // verify the required parameter 'subscription' is set
      if (subscription === undefined || subscription === null) {
        throw new Error("Missing the required parameter 'subscription' when calling postSubscription");
      }

      let pathParams = {
      };
      let queryParams = {
        'expand': opts['expand']
      };
      let headerParams = {
        'Organization-Id': opts['organizationId']
      };
      let formParams = {
      };

      let authNames = ['SecretApiKey', 'JWT'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = Subscription;
      return this.apiClient.callApi(
        '/subscriptions', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the postSubscriptionCancellation operation.
     * @callback module:api/OrdersApi~postSubscriptionCancellationCallback
     * @param {String} error Error message, if any.
     * @param {module:model/SubscriptionCancellation} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Cancel an order
     * Cancel an order or preview the cancellation parameters before that.
     * @param {module:model/SubscriptionCancellation} subscriptionCancellation Cancellation resource.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/OrdersApi~postSubscriptionCancellationCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/SubscriptionCancellation}
     */
    postSubscriptionCancellation(subscriptionCancellation, opts, callback) {
      opts = opts || {};
      let postBody = subscriptionCancellation;
      // verify the required parameter 'subscriptionCancellation' is set
      if (subscriptionCancellation === undefined || subscriptionCancellation === null) {
        throw new Error("Missing the required parameter 'subscriptionCancellation' when calling postSubscriptionCancellation");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'Organization-Id': opts['organizationId']
      };
      let formParams = {
      };

      let authNames = ['SecretApiKey', 'JWT'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = SubscriptionCancellation;
      return this.apiClient.callApi(
        '/subscription-cancellations', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the postSubscriptionInterimInvoice operation.
     * @callback module:api/OrdersApi~postSubscriptionInterimInvoiceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Invoice} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Issue an interim invoice for a subscription order
     * Issue an interim invoice for a subscription, typically used in conjunction. with plan changes and pro rata adjustments. This process creates an invoice, adds the subscription's line items to the invoice, and issues the invoice, and applies payment to it if a transaction id is supplied. 
     * @param {String} id The resource identifier string.
     * @param {module:model/SubscriptionInvoice} subscriptionInvoice Issue an interim invoice.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/OrdersApi~postSubscriptionInterimInvoiceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Invoice}
     */
    postSubscriptionInterimInvoice(id, subscriptionInvoice, opts, callback) {
      opts = opts || {};
      let postBody = subscriptionInvoice;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling postSubscriptionInterimInvoice");
      }
      // verify the required parameter 'subscriptionInvoice' is set
      if (subscriptionInvoice === undefined || subscriptionInvoice === null) {
        throw new Error("Missing the required parameter 'subscriptionInvoice' when calling postSubscriptionInterimInvoice");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
        'Organization-Id': opts['organizationId']
      };
      let formParams = {
      };

      let authNames = ['SecretApiKey', 'JWT'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = Invoice;
      return this.apiClient.callApi(
        '/subscriptions/{id}/interim-invoice', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the postSubscriptionItemsChange operation.
     * @callback module:api/OrdersApi~postSubscriptionItemsChangeCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Subscription} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Change an order's items
     * Change an order's items or quantities and designate when and if there should be pro-rata credits given. 
     * @param {String} id The resource identifier string.
     * @param {module:model/SubscriptionChange} subscriptionChange Change items request.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/OrdersApi~postSubscriptionItemsChangeCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Subscription}
     */
    postSubscriptionItemsChange(id, subscriptionChange, opts, callback) {
      opts = opts || {};
      let postBody = subscriptionChange;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling postSubscriptionItemsChange");
      }
      // verify the required parameter 'subscriptionChange' is set
      if (subscriptionChange === undefined || subscriptionChange === null) {
        throw new Error("Missing the required parameter 'subscriptionChange' when calling postSubscriptionItemsChange");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
        'Organization-Id': opts['organizationId']
      };
      let formParams = {
      };

      let authNames = ['SecretApiKey', 'JWT'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = Subscription;
      return this.apiClient.callApi(
        '/subscriptions/{id}/change-items', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the postSubscriptionReactivation operation.
     * @callback module:api/OrdersApi~postSubscriptionReactivationCallback
     * @param {String} error Error message, if any.
     * @param {module:model/SubscriptionReactivation} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Reactivate an order
     * Reactivate a subscription.
     * @param {module:model/SubscriptionReactivation} subscriptionReactivation Reactivation resource.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/OrdersApi~postSubscriptionReactivationCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/SubscriptionReactivation}
     */
    postSubscriptionReactivation(subscriptionReactivation, opts, callback) {
      opts = opts || {};
      let postBody = subscriptionReactivation;
      // verify the required parameter 'subscriptionReactivation' is set
      if (subscriptionReactivation === undefined || subscriptionReactivation === null) {
        throw new Error("Missing the required parameter 'subscriptionReactivation' when calling postSubscriptionReactivation");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'Organization-Id': opts['organizationId']
      };
      let formParams = {
      };

      let authNames = ['SecretApiKey', 'JWT'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = SubscriptionReactivation;
      return this.apiClient.callApi(
        '/subscription-reactivations', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the postSubscriptionTimeline operation.
     * @callback module:api/OrdersApi~postSubscriptionTimelineCallback
     * @param {String} error Error message, if any.
     * @param {module:model/OrderTimeline} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create an order Timeline comment
     * Create an order Timeline comment. 
     * @param {String} id The resource identifier string.
     * @param {module:model/OrderTimeline} orderTimeline Order Timeline resource.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/OrdersApi~postSubscriptionTimelineCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/OrderTimeline}
     */
    postSubscriptionTimeline(id, orderTimeline, opts, callback) {
      opts = opts || {};
      let postBody = orderTimeline;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling postSubscriptionTimeline");
      }
      // verify the required parameter 'orderTimeline' is set
      if (orderTimeline === undefined || orderTimeline === null) {
        throw new Error("Missing the required parameter 'orderTimeline' when calling postSubscriptionTimeline");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
        'Organization-Id': opts['organizationId']
      };
      let formParams = {
      };

      let authNames = ['SecretApiKey', 'JWT'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = OrderTimeline;
      return this.apiClient.callApi(
        '/subscriptions/{id}/timeline', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the postUpcomingInvoiceIssuance operation.
     * @callback module:api/OrdersApi~postUpcomingInvoiceIssuanceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Invoice} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Issue an upcoming invoice for early pay
     * Issue an upcoming invoice with specified identifier string for early pay. 
     * @param {String} id The resource identifier string.
     * @param {String} invoiceId The Upcoming Invoice ID.
     * @param {module:model/InvoiceIssue} invoiceIssue InvoiceIssue resource.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/OrdersApi~postUpcomingInvoiceIssuanceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Invoice}
     */
    postUpcomingInvoiceIssuance(id, invoiceId, invoiceIssue, opts, callback) {
      opts = opts || {};
      let postBody = invoiceIssue;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling postUpcomingInvoiceIssuance");
      }
      // verify the required parameter 'invoiceId' is set
      if (invoiceId === undefined || invoiceId === null) {
        throw new Error("Missing the required parameter 'invoiceId' when calling postUpcomingInvoiceIssuance");
      }
      // verify the required parameter 'invoiceIssue' is set
      if (invoiceIssue === undefined || invoiceIssue === null) {
        throw new Error("Missing the required parameter 'invoiceIssue' when calling postUpcomingInvoiceIssuance");
      }

      let pathParams = {
        'id': id,
        'invoiceId': invoiceId
      };
      let queryParams = {
      };
      let headerParams = {
        'Organization-Id': opts['organizationId']
      };
      let formParams = {
      };

      let authNames = ['SecretApiKey', 'JWT'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = Invoice;
      return this.apiClient.callApi(
        '/subscriptions/{id}/upcoming-invoices/{invoiceId}/issue', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the putSubscription operation.
     * @callback module:api/OrdersApi~putSubscriptionCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Subscription} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Upsert an order with predefined ID
     * Create or update an order with predefined identifier string. 
     * @param {String} id The resource identifier string.
     * @param {module:model/Subscription} subscription Order resource.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {String} [expand] Expand a response to get a full related object included inside of the `_embedded` path in the response. To expand multiple objects, it accepts a comma-separated list of objects (example: `expand=recentInvoice,initialInvoice`). Available arguments are:   - recentInvoice   - initialInvoice   - customer   - website  See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info. 
     * @param {module:api/OrdersApi~putSubscriptionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Subscription}
     */
    putSubscription(id, subscription, opts, callback) {
      opts = opts || {};
      let postBody = subscription;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling putSubscription");
      }
      // verify the required parameter 'subscription' is set
      if (subscription === undefined || subscription === null) {
        throw new Error("Missing the required parameter 'subscription' when calling putSubscription");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'expand': opts['expand']
      };
      let headerParams = {
        'Organization-Id': opts['organizationId']
      };
      let formParams = {
      };

      let authNames = ['SecretApiKey', 'JWT'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = Subscription;
      return this.apiClient.callApi(
        '/subscriptions/{id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the putSubscriptionCancellation operation.
     * @callback module:api/OrdersApi~putSubscriptionCancellationCallback
     * @param {String} error Error message, if any.
     * @param {module:model/SubscriptionCancellation} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Cancel an order
     * Cancel a subscription.
     * @param {String} id The resource identifier string.
     * @param {module:model/SubscriptionCancellation} subscriptionCancellation Cancellation resource.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/OrdersApi~putSubscriptionCancellationCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/SubscriptionCancellation}
     */
    putSubscriptionCancellation(id, subscriptionCancellation, opts, callback) {
      opts = opts || {};
      let postBody = subscriptionCancellation;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling putSubscriptionCancellation");
      }
      // verify the required parameter 'subscriptionCancellation' is set
      if (subscriptionCancellation === undefined || subscriptionCancellation === null) {
        throw new Error("Missing the required parameter 'subscriptionCancellation' when calling putSubscriptionCancellation");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
        'Organization-Id': opts['organizationId']
      };
      let formParams = {
      };

      let authNames = ['SecretApiKey', 'JWT'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = SubscriptionCancellation;
      return this.apiClient.callApi(
        '/subscription-cancellations/{id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
