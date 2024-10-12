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
import CoreReadyToPay from '../model/CoreReadyToPay';
import Error from '../model/Error';
import InvalidError from '../model/InvalidError';
import PatchTransactionRequest from '../model/PatchTransactionRequest';
import PayoutRequest from '../model/PayoutRequest';
import ReadyToPayMethodsInner from '../model/ReadyToPayMethodsInner';
import Transaction from '../model/Transaction';
import TransactionQuery from '../model/TransactionQuery';
import TransactionRefund from '../model/TransactionRefund';
import TransactionRequest from '../model/TransactionRequest';
import TransactionTimeline from '../model/TransactionTimeline';
import TransactionUpdate from '../model/TransactionUpdate';

/**
* Transactions service.
* @module api/TransactionsApi
* @version 2.1
*/
export default class TransactionsApi {

    /**
    * Constructs a new TransactionsApi. 
    * @alias module:api/TransactionsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the deleteTransactionTimeline operation.
     * @callback module:api/TransactionsApi~deleteTransactionTimelineCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete a Transaction Timeline message
     * Delete a Transaction Timeline message with predefined identifier string. 
     * @param {String} id The resource identifier string.
     * @param {String} messageId The Transaction Timeline message ID.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/TransactionsApi~deleteTransactionTimelineCallback} callback The callback function, accepting three arguments: error, data, response
     */
    deleteTransactionTimeline(id, messageId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling deleteTransactionTimeline");
      }
      // verify the required parameter 'messageId' is set
      if (messageId === undefined || messageId === null) {
        throw new Error("Missing the required parameter 'messageId' when calling deleteTransactionTimeline");
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
        '/transactions/{id}/timeline/{messageId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getTransaction operation.
     * @callback module:api/TransactionsApi~getTransactionCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Transaction} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve a Transaction
     * Retrieve a Transaction with specified identifier string. 
     * @param {String} id The resource identifier string.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {String} [expand] Expand a response to get a full related object included inside of the `_embedded` path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info. 
     * @param {module:api/TransactionsApi~getTransactionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Transaction}
     */
    getTransaction(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getTransaction");
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
      let returnType = Transaction;
      return this.apiClient.callApi(
        '/transactions/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getTransactionCollection operation.
     * @callback module:api/TransactionsApi~getTransactionCollectionCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/Transaction>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve a list of transactions
     * Retrieve a list of transactions. 
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {Number} [limit] The collection items limit.
     * @param {Number} [offset] The collection items offset.
     * @param {String} [filter] The collection items filter requires a special format. Use \",\" for multiple allowed values.  Use \";\" for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format. 
     * @param {String} [q] The partial search of the text fields.
     * @param {Array.<String>} [sort] The collection items sort field and order (prefix with \"-\" for descending sort).
     * @param {String} [expand] Expand a response to get a full related object included inside of the `_embedded` path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info. 
     * @param {module:api/TransactionsApi~getTransactionCollectionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/Transaction>}
     */
    getTransactionCollection(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'limit': opts['limit'],
        'offset': opts['offset'],
        'filter': opts['filter'],
        'q': opts['q'],
        'sort': this.apiClient.buildCollectionParam(opts['sort'], 'csv'),
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
      let returnType = [Transaction];
      return this.apiClient.callApi(
        '/transactions', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getTransactionTimeline operation.
     * @callback module:api/TransactionsApi~getTransactionTimelineCallback
     * @param {String} error Error message, if any.
     * @param {module:model/TransactionTimeline} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve a transaction Timeline message
     * Retrieve a timeline message with specified identifier string. 
     * @param {String} id The resource identifier string.
     * @param {String} messageId The Transaction Timeline message ID.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/TransactionsApi~getTransactionTimelineCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/TransactionTimeline}
     */
    getTransactionTimeline(id, messageId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getTransactionTimeline");
      }
      // verify the required parameter 'messageId' is set
      if (messageId === undefined || messageId === null) {
        throw new Error("Missing the required parameter 'messageId' when calling getTransactionTimeline");
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
      let returnType = TransactionTimeline;
      return this.apiClient.callApi(
        '/transactions/{id}/timeline/{messageId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getTransactionTimelineCollection operation.
     * @callback module:api/TransactionsApi~getTransactionTimelineCollectionCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/TransactionTimeline>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve a list of transaction timeline messages
     * Retrieve a list of transaction timeline messages. 
     * @param {String} id The resource identifier string.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {Number} [limit] The collection items limit.
     * @param {Number} [offset] The collection items offset.
     * @param {String} [filter] The collection items filter requires a special format. Use \",\" for multiple allowed values.  Use \";\" for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format. 
     * @param {module:api/TransactionsApi~getTransactionTimelineCollectionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/TransactionTimeline>}
     */
    getTransactionTimelineCollection(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getTransactionTimelineCollection");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'limit': opts['limit'],
        'offset': opts['offset'],
        'filter': opts['filter']
      };
      let headerParams = {
        'Organization-Id': opts['organizationId']
      };
      let formParams = {
      };

      let authNames = ['SecretApiKey', 'JWT'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [TransactionTimeline];
      return this.apiClient.callApi(
        '/transactions/{id}/timeline', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patchTransaction operation.
     * @callback module:api/TransactionsApi~patchTransactionCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Transaction} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update a transaction
     * Update a transaction's custom fields. 
     * @param {String} id The resource identifier string.
     * @param {module:model/PatchTransactionRequest} patchTransactionRequest Use the patch transaction request to modify custom fields.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/TransactionsApi~patchTransactionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Transaction}
     */
    patchTransaction(id, patchTransactionRequest, opts, callback) {
      opts = opts || {};
      let postBody = patchTransactionRequest;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling patchTransaction");
      }
      // verify the required parameter 'patchTransactionRequest' is set
      if (patchTransactionRequest === undefined || patchTransactionRequest === null) {
        throw new Error("Missing the required parameter 'patchTransactionRequest' when calling patchTransaction");
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
      let returnType = Transaction;
      return this.apiClient.callApi(
        '/transactions/{id}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the postPayout operation.
     * @callback module:api/TransactionsApi~postPayoutCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Transaction} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a credit transaction
     * Create a transaction of type `credit`. 
     * @param {module:model/PayoutRequest} payoutRequest Transaction resource.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/TransactionsApi~postPayoutCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Transaction}
     */
    postPayout(payoutRequest, opts, callback) {
      opts = opts || {};
      let postBody = payoutRequest;
      // verify the required parameter 'payoutRequest' is set
      if (payoutRequest === undefined || payoutRequest === null) {
        throw new Error("Missing the required parameter 'payoutRequest' when calling postPayout");
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
      let returnType = Transaction;
      return this.apiClient.callApi(
        '/payouts', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the postReadyToPay operation.
     * @callback module:api/TransactionsApi~postReadyToPayCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/ReadyToPayMethodsInner>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Ready to Pay
     * Get available payment methods for a specific transaction or a purchase.  The payment methods order shown to a customer **SHOULD** be the same as the order in the response.  The list of available methods is generated from available [Gateway Accounts](https://user-api-docs.rebilly.com/tag/Gateway-Accounts) intersected with the last matched [Rules Engine](https://user-api-docs.rebilly.com/tag/Rules#operation/PutEventRule) `adjust-ready-to-pay` action on `ready-to-pay-requested` event.  If there were no actions matched for the specific request – all methods supported by the Gateway Accounts are sent.  To invert this behavior – place an all-matching rule at the very end of the `ready-to-pay-requested` event in Rules Engine with an empty `paymentMethods` property of the `adjust-ready-to-pay` action. 
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:model/CoreReadyToPay} [coreReadyToPay] 
     * @param {module:api/TransactionsApi~postReadyToPayCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/ReadyToPayMethodsInner>}
     */
    postReadyToPay(opts, callback) {
      opts = opts || {};
      let postBody = opts['coreReadyToPay'];

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
      let returnType = [ReadyToPayMethodsInner];
      return this.apiClient.callApi(
        '/ready-to-pay', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the postTransaction operation.
     * @callback module:api/TransactionsApi~postTransactionCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Transaction} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a transaction
     * Create a transaction of type `sale` or `authorize`. This endpoint supports two main styles of transactions:   1. A real-time decision and response.   2. User approval/interaction is required.  A real-time decision is very familiar.  You send a request, and inspect the `result` of the response for `approved` or `declined`.  However, many transactions, especially those for alternative methods, require the user to interact with a 3rd party.  You may be able to envision PayPal, for example, the user must give permission to complete the payment (or accept the billing agreement).  Even payment cards may require user approval in the case of 3D secure authentication.  In the event that approval is required, you will receive a response back and notice that the `result` is `unknown`.  You will find that the `status` is `waiting-approval`. And you will find in the `_links` section of the response a link for the `approvalUrl`.  In this case you would either open the `approvalUrl` in an iframe or in a pop (better workflow for mobile). 
     * @param {module:model/TransactionRequest} transactionRequest Transaction resource.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {String} [expand] Expand a response to get a full related object included inside of the `_embedded` path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info. 
     * @param {module:api/TransactionsApi~postTransactionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Transaction}
     */
    postTransaction(transactionRequest, opts, callback) {
      opts = opts || {};
      let postBody = transactionRequest;
      // verify the required parameter 'transactionRequest' is set
      if (transactionRequest === undefined || transactionRequest === null) {
        throw new Error("Missing the required parameter 'transactionRequest' when calling postTransaction");
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
      let returnType = Transaction;
      return this.apiClient.callApi(
        '/transactions', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the postTransactionQuery operation.
     * @callback module:api/TransactionsApi~postTransactionQueryCallback
     * @param {String} error Error message, if any.
     * @param {module:model/TransactionQuery} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Query a Transaction
     * Query a Transaction with a specified identifier string. The query will contact the gateway account to find the result and amount/currency. The response should be analyzed.  If deemed appropriate, the transaction could be updated using the Transaction Update API. 
     * @param {String} id The resource identifier string.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/TransactionsApi~postTransactionQueryCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/TransactionQuery}
     */
    postTransactionQuery(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling postTransactionQuery");
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
      let returnType = TransactionQuery;
      return this.apiClient.callApi(
        '/transactions/{id}/query', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the postTransactionRefund operation.
     * @callback module:api/TransactionsApi~postTransactionRefundCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Transaction} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Refund a Transaction
     * Refund a Transaction with specified identifier string. Note that the refund will be in the same currency as the original transaction. 
     * @param {String} id The resource identifier string.
     * @param {module:model/TransactionRefund} transactionRefund Transaction resource.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/TransactionsApi~postTransactionRefundCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Transaction}
     */
    postTransactionRefund(id, transactionRefund, opts, callback) {
      opts = opts || {};
      let postBody = transactionRefund;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling postTransactionRefund");
      }
      // verify the required parameter 'transactionRefund' is set
      if (transactionRefund === undefined || transactionRefund === null) {
        throw new Error("Missing the required parameter 'transactionRefund' when calling postTransactionRefund");
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
      let returnType = Transaction;
      return this.apiClient.callApi(
        '/transactions/{id}/refund', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the postTransactionTimeline operation.
     * @callback module:api/TransactionsApi~postTransactionTimelineCallback
     * @param {String} error Error message, if any.
     * @param {module:model/TransactionTimeline} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a transaction Timeline comment
     * Create a transaction Timeline comment. 
     * @param {String} id The resource identifier string.
     * @param {module:model/TransactionTimeline} transactionTimeline Transaction Timeline resource.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/TransactionsApi~postTransactionTimelineCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/TransactionTimeline}
     */
    postTransactionTimeline(id, transactionTimeline, opts, callback) {
      opts = opts || {};
      let postBody = transactionTimeline;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling postTransactionTimeline");
      }
      // verify the required parameter 'transactionTimeline' is set
      if (transactionTimeline === undefined || transactionTimeline === null) {
        throw new Error("Missing the required parameter 'transactionTimeline' when calling postTransactionTimeline");
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
      let returnType = TransactionTimeline;
      return this.apiClient.callApi(
        '/transactions/{id}/timeline', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the postTransactionUpdate operation.
     * @callback module:api/TransactionsApi~postTransactionUpdateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Transaction} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update a Transaction status
     * Update a Transaction manually to completed status with given result with optional currency and amount.
     * @param {String} id The resource identifier string.
     * @param {module:model/TransactionUpdate} transactionUpdate 
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/TransactionsApi~postTransactionUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Transaction}
     */
    postTransactionUpdate(id, transactionUpdate, opts, callback) {
      opts = opts || {};
      let postBody = transactionUpdate;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling postTransactionUpdate");
      }
      // verify the required parameter 'transactionUpdate' is set
      if (transactionUpdate === undefined || transactionUpdate === null) {
        throw new Error("Missing the required parameter 'transactionUpdate' when calling postTransactionUpdate");
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
      let returnType = Transaction;
      return this.apiClient.callApi(
        '/transactions/{id}/update', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
