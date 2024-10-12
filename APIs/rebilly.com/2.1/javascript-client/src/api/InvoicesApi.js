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
import InvoiceItem from '../model/InvoiceItem';
import InvoiceReissue from '../model/InvoiceReissue';
import InvoiceTimeline from '../model/InvoiceTimeline';
import InvoiceTransaction from '../model/InvoiceTransaction';
import InvoiceTransactionAllocation from '../model/InvoiceTransactionAllocation';

/**
* Invoices service.
* @module api/InvoicesApi
* @version 2.1
*/
export default class InvoicesApi {

    /**
    * Constructs a new InvoicesApi. 
    * @alias module:api/InvoicesApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the deleteInvoiceTimeline operation.
     * @callback module:api/InvoicesApi~deleteInvoiceTimelineCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete an Invoice Timeline message
     * Delete an Invoice Timeline message with predefined identifier string. 
     * @param {String} id The resource identifier string.
     * @param {String} messageId The Invoice Timeline message ID.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/InvoicesApi~deleteInvoiceTimelineCallback} callback The callback function, accepting three arguments: error, data, response
     */
    deleteInvoiceTimeline(id, messageId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling deleteInvoiceTimeline");
      }
      // verify the required parameter 'messageId' is set
      if (messageId === undefined || messageId === null) {
        throw new Error("Missing the required parameter 'messageId' when calling deleteInvoiceTimeline");
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
        '/invoices/{id}/timeline/{messageId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getCustomerUpcomingInvoiceCollection operation.
     * @callback module:api/InvoicesApi~getCustomerUpcomingInvoiceCollectionCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/Invoice>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve customer's upcoming invoices
     * Retrieve a list of upcoming invoices from the subscriptions which belong to. the given customer. The endpoint is temporary before upcoming invoices get a complete integration. 
     * @param {String} id The resource identifier string.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {String} [expand] Expand a response to get a full related object included inside of the `_embedded` path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info. 
     * @param {module:api/InvoicesApi~getCustomerUpcomingInvoiceCollectionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/Invoice>}
     */
    getCustomerUpcomingInvoiceCollection(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getCustomerUpcomingInvoiceCollection");
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
        '/customers/{id}/upcoming-invoices', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getInvoice operation.
     * @callback module:api/InvoicesApi~getInvoiceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Invoice} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an invoice
     * Retrieve an invoice with specified identifier string. 
     * @param {String} id The resource identifier string.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:model/String} [accept = 'application/json')] The response media type.
     * @param {String} [expand] Expand a response to get a full related object included inside of the `_embedded` path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info. 
     * @param {module:api/InvoicesApi~getInvoiceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Invoice}
     */
    getInvoice(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getInvoice");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'expand': opts['expand']
      };
      let headerParams = {
        'Organization-Id': opts['organizationId'],
        'Accept': opts['accept']
      };
      let formParams = {
      };

      let authNames = ['SecretApiKey', 'JWT'];
      let contentTypes = [];
      let accepts = ['application/json', 'application/pdf'];
      let returnType = Invoice;
      return this.apiClient.callApi(
        '/invoices/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getInvoiceCollection operation.
     * @callback module:api/InvoicesApi~getInvoiceCollectionCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/Invoice>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve a list of invoices
     * Retrieve a list of invoices. 
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {String} [filter] The collection items filter requires a special format. Use \",\" for multiple allowed values.  Use \";\" for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format. 
     * @param {Array.<String>} [sort] The collection items sort field and order (prefix with \"-\" for descending sort).
     * @param {Number} [limit] The collection items limit.
     * @param {Number} [offset] The collection items offset.
     * @param {String} [q] The partial search of the text fields.
     * @param {String} [expand] Expand a response to get a full related object included inside of the `_embedded` path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info. 
     * @param {module:api/InvoicesApi~getInvoiceCollectionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/Invoice>}
     */
    getInvoiceCollection(opts, callback) {
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
      let returnType = [Invoice];
      return this.apiClient.callApi(
        '/invoices', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getInvoiceItemCollection operation.
     * @callback module:api/InvoicesApi~getInvoiceItemCollectionCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/InvoiceItem>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve invoice items
     * Retrieve an invoice items with specified invoice identifier string. 
     * @param {String} id The resource identifier string.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {Number} [limit] The collection items limit.
     * @param {Number} [offset] The collection items offset.
     * @param {String} [expand] Expand a response to get a full related object included inside of the `_embedded` path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info. 
     * @param {module:api/InvoicesApi~getInvoiceItemCollectionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/InvoiceItem>}
     */
    getInvoiceItemCollection(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getInvoiceItemCollection");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'limit': opts['limit'],
        'offset': opts['offset'],
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
      let returnType = [InvoiceItem];
      return this.apiClient.callApi(
        '/invoices/{id}/items', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getInvoiceTimeline operation.
     * @callback module:api/InvoicesApi~getInvoiceTimelineCallback
     * @param {String} error Error message, if any.
     * @param {module:model/InvoiceTimeline} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an Invoice Timeline message
     * Retrieve a invoice message with specified identifier string. 
     * @param {String} id The resource identifier string.
     * @param {String} messageId The Invoice Timeline message ID.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/InvoicesApi~getInvoiceTimelineCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/InvoiceTimeline}
     */
    getInvoiceTimeline(id, messageId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getInvoiceTimeline");
      }
      // verify the required parameter 'messageId' is set
      if (messageId === undefined || messageId === null) {
        throw new Error("Missing the required parameter 'messageId' when calling getInvoiceTimeline");
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
      let returnType = InvoiceTimeline;
      return this.apiClient.callApi(
        '/invoices/{id}/timeline/{messageId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getInvoiceTimelineCollection operation.
     * @callback module:api/InvoicesApi~getInvoiceTimelineCollectionCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/InvoiceTimeline>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve a list of invoice timeline messages
     * Retrieve a list of invoice timeline messages. 
     * @param {String} id The resource identifier string.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {Number} [limit] The collection items limit.
     * @param {Number} [offset] The collection items offset.
     * @param {String} [filter] The collection items filter requires a special format. Use \",\" for multiple allowed values.  Use \";\" for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format. 
     * @param {Array.<String>} [sort] The collection items sort field and order (prefix with \"-\" for descending sort).
     * @param {String} [q] The partial search of the text fields.
     * @param {module:api/InvoicesApi~getInvoiceTimelineCollectionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/InvoiceTimeline>}
     */
    getInvoiceTimelineCollection(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getInvoiceTimelineCollection");
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
      let returnType = [InvoiceTimeline];
      return this.apiClient.callApi(
        '/invoices/{id}/timeline', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getInvoiceTransactionAllocationCollection operation.
     * @callback module:api/InvoicesApi~getInvoiceTransactionAllocationCollectionCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/InvoiceTransactionAllocation>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get transaction amounts allocated to an invoice
     * Get the precise amounts from a transaction allocated as invoice payments.
     * @param {String} id The resource identifier string.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {Number} [limit] The collection items limit.
     * @param {Number} [offset] The collection items offset.
     * @param {module:api/InvoicesApi~getInvoiceTransactionAllocationCollectionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/InvoiceTransactionAllocation>}
     */
    getInvoiceTransactionAllocationCollection(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getInvoiceTransactionAllocationCollection");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'limit': opts['limit'],
        'offset': opts['offset']
      };
      let headerParams = {
        'Organization-Id': opts['organizationId']
      };
      let formParams = {
      };

      let authNames = ['SecretApiKey', 'JWT'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [InvoiceTransactionAllocation];
      return this.apiClient.callApi(
        '/invoices/{id}/transaction-allocations', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the postInvoice operation.
     * @callback module:api/InvoicesApi~postInvoiceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Invoice} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create an invoice
     * Create an invoice. 
     * @param {module:model/Invoice} invoice Invoice resource.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/InvoicesApi~postInvoiceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Invoice}
     */
    postInvoice(invoice, opts, callback) {
      opts = opts || {};
      let postBody = invoice;
      // verify the required parameter 'invoice' is set
      if (invoice === undefined || invoice === null) {
        throw new Error("Missing the required parameter 'invoice' when calling postInvoice");
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
      let returnType = Invoice;
      return this.apiClient.callApi(
        '/invoices', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the postInvoiceAbandonment operation.
     * @callback module:api/InvoicesApi~postInvoiceAbandonmentCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Invoice} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Abandon an invoice
     * Abandon an invoice with specified identifier string. 
     * @param {String} id The resource identifier string.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/InvoicesApi~postInvoiceAbandonmentCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Invoice}
     */
    postInvoiceAbandonment(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling postInvoiceAbandonment");
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
      let returnType = Invoice;
      return this.apiClient.callApi(
        '/invoices/{id}/abandon', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the postInvoiceIssuance operation.
     * @callback module:api/InvoicesApi~postInvoiceIssuanceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Invoice} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Issue an invoice
     * Issue an invoice with specified identifier string. It must be in `draft` status. 
     * @param {String} id The resource identifier string.
     * @param {module:model/InvoiceIssue} invoiceIssue InvoiceIssue resource.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/InvoicesApi~postInvoiceIssuanceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Invoice}
     */
    postInvoiceIssuance(id, invoiceIssue, opts, callback) {
      opts = opts || {};
      let postBody = invoiceIssue;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling postInvoiceIssuance");
      }
      // verify the required parameter 'invoiceIssue' is set
      if (invoiceIssue === undefined || invoiceIssue === null) {
        throw new Error("Missing the required parameter 'invoiceIssue' when calling postInvoiceIssuance");
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
        '/invoices/{id}/issue', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the postInvoiceItem operation.
     * @callback module:api/InvoicesApi~postInvoiceItemCallback
     * @param {String} error Error message, if any.
     * @param {module:model/InvoiceItem} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create an invoice item
     * Create an invoice item. 
     * @param {String} id The resource identifier string.
     * @param {module:model/InvoiceItem} invoiceItem InvoiceItem resource.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/InvoicesApi~postInvoiceItemCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/InvoiceItem}
     */
    postInvoiceItem(id, invoiceItem, opts, callback) {
      opts = opts || {};
      let postBody = invoiceItem;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling postInvoiceItem");
      }
      // verify the required parameter 'invoiceItem' is set
      if (invoiceItem === undefined || invoiceItem === null) {
        throw new Error("Missing the required parameter 'invoiceItem' when calling postInvoiceItem");
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
      let returnType = InvoiceItem;
      return this.apiClient.callApi(
        '/invoices/{id}/items', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the postInvoiceRecalculation operation.
     * @callback module:api/InvoicesApi~postInvoiceRecalculationCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Invoice} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Recalculate an invoice
     * Recalculate an invoice with specified identifier string. It will recalculate shipping rates, taxes, discounts. It is useful when coupon was revoked or customer redeemed coupon after invoice was issued and you want to apply it to this invoice. 
     * @param {String} id The resource identifier string.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/InvoicesApi~postInvoiceRecalculationCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Invoice}
     */
    postInvoiceRecalculation(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling postInvoiceRecalculation");
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
      let returnType = Invoice;
      return this.apiClient.callApi(
        '/invoices/{id}/recalculate', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the postInvoiceReissuance operation.
     * @callback module:api/InvoicesApi~postInvoiceReissuanceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Invoice} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Reissue an invoice
     * Reissue an invoice with specified identifier string. It must be issued. (status must be `unpaid` or `past-due`). 
     * @param {String} id The resource identifier string.
     * @param {module:model/InvoiceReissue} invoiceReissue InvoiceReissue resource.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/InvoicesApi~postInvoiceReissuanceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Invoice}
     */
    postInvoiceReissuance(id, invoiceReissue, opts, callback) {
      opts = opts || {};
      let postBody = invoiceReissue;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling postInvoiceReissuance");
      }
      // verify the required parameter 'invoiceReissue' is set
      if (invoiceReissue === undefined || invoiceReissue === null) {
        throw new Error("Missing the required parameter 'invoiceReissue' when calling postInvoiceReissuance");
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
        '/invoices/{id}/reissue', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the postInvoiceTimeline operation.
     * @callback module:api/InvoicesApi~postInvoiceTimelineCallback
     * @param {String} error Error message, if any.
     * @param {module:model/InvoiceTimeline} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create an invoice Timeline comment
     * Create an invoice Timeline comment. 
     * @param {String} id The resource identifier string.
     * @param {module:model/InvoiceTimeline} invoiceTimeline Invoice Timeline resource.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/InvoicesApi~postInvoiceTimelineCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/InvoiceTimeline}
     */
    postInvoiceTimeline(id, invoiceTimeline, opts, callback) {
      opts = opts || {};
      let postBody = invoiceTimeline;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling postInvoiceTimeline");
      }
      // verify the required parameter 'invoiceTimeline' is set
      if (invoiceTimeline === undefined || invoiceTimeline === null) {
        throw new Error("Missing the required parameter 'invoiceTimeline' when calling postInvoiceTimeline");
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
      let returnType = InvoiceTimeline;
      return this.apiClient.callApi(
        '/invoices/{id}/timeline', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the postInvoiceTransaction operation.
     * @callback module:api/InvoicesApi~postInvoiceTransactionCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Invoice} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Apply a transaction to an invoice
     * Apply a transaction to an invoice. The invoice must be unpaid. The transaction must have a non-zero unused amount (not fully applied to other invoices). 
     * @param {String} id The resource identifier string.
     * @param {module:model/InvoiceTransaction} invoiceTransaction InvoiceTransaction resource.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/InvoicesApi~postInvoiceTransactionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Invoice}
     */
    postInvoiceTransaction(id, invoiceTransaction, opts, callback) {
      opts = opts || {};
      let postBody = invoiceTransaction;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling postInvoiceTransaction");
      }
      // verify the required parameter 'invoiceTransaction' is set
      if (invoiceTransaction === undefined || invoiceTransaction === null) {
        throw new Error("Missing the required parameter 'invoiceTransaction' when calling postInvoiceTransaction");
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
        '/invoices/{id}/transaction', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the postInvoiceVoid operation.
     * @callback module:api/InvoicesApi~postInvoiceVoidCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Invoice} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Void an invoice
     * Void an invoice with specified identifier string. 
     * @param {String} id The resource identifier string.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/InvoicesApi~postInvoiceVoidCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Invoice}
     */
    postInvoiceVoid(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling postInvoiceVoid");
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
      let returnType = Invoice;
      return this.apiClient.callApi(
        '/invoices/{id}/void', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the putInvoice operation.
     * @callback module:api/InvoicesApi~putInvoiceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Invoice} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create or update an invoice with predefined ID
     * Create or update an invoice with predefined identifier string. 
     * @param {String} id The resource identifier string.
     * @param {module:model/Invoice} invoice Invoice resource.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/InvoicesApi~putInvoiceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Invoice}
     */
    putInvoice(id, invoice, opts, callback) {
      opts = opts || {};
      let postBody = invoice;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling putInvoice");
      }
      // verify the required parameter 'invoice' is set
      if (invoice === undefined || invoice === null) {
        throw new Error("Missing the required parameter 'invoice' when calling putInvoice");
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
        '/invoices/{id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
