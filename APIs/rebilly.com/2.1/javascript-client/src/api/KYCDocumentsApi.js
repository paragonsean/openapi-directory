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
import KycDocument2 from '../model/KycDocument2';
import KycDocumentRejection from '../model/KycDocumentRejection';
import KycRequest from '../model/KycRequest';
import PatchKycRequestRequest from '../model/PatchKycRequestRequest';
import PostKycDocumentMatchesRequest from '../model/PostKycDocumentMatchesRequest';

/**
* KYCDocuments service.
* @module api/KYCDocumentsApi
* @version 2.1
*/
export default class KYCDocumentsApi {

    /**
    * Constructs a new KYCDocumentsApi. 
    * @alias module:api/KYCDocumentsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the deleteKycRequest operation.
     * @callback module:api/KYCDocumentsApi~deleteKycRequestCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete the KYC request
     * Delete the KYC request with the predefined identifier string. 
     * @param {String} id The resource identifier string.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/KYCDocumentsApi~deleteKycRequestCallback} callback The callback function, accepting three arguments: error, data, response
     */
    deleteKycRequest(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling deleteKycRequest");
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
        '/kyc-requests/{id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getKycDocument operation.
     * @callback module:api/KYCDocumentsApi~getKycDocumentCallback
     * @param {String} error Error message, if any.
     * @param {module:model/KycDocument2} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve a KYC Document
     * Retrieve a KYC document with specified identifier string.
     * @param {String} id The resource identifier string.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/KYCDocumentsApi~getKycDocumentCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/KycDocument2}
     */
    getKycDocument(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getKycDocument");
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
      let returnType = KycDocument2;
      return this.apiClient.callApi(
        '/kyc-documents/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getKycDocumentCollection operation.
     * @callback module:api/KYCDocumentsApi~getKycDocumentCollectionCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/KycDocument2>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve a list of KYC documents
     * Retrieve a list of KYC documents. 
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {Number} [limit] The collection items limit.
     * @param {Number} [offset] The collection items offset.
     * @param {String} [filter] The collection items filter requires a special format. Use \",\" for multiple allowed values.  Use \";\" for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format. 
     * @param {Array.<String>} [sort] The collection items sort field and order (prefix with \"-\" for descending sort).
     * @param {module:api/KYCDocumentsApi~getKycDocumentCollectionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/KycDocument2>}
     */
    getKycDocumentCollection(opts, callback) {
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
      let returnType = [KycDocument2];
      return this.apiClient.callApi(
        '/kyc-documents', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getKycRequest operation.
     * @callback module:api/KYCDocumentsApi~getKycRequestCallback
     * @param {String} error Error message, if any.
     * @param {module:model/KycRequest} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve a KYC request
     * Retrieve a KYC request with specified identifier string.
     * @param {String} id The resource identifier string.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/KYCDocumentsApi~getKycRequestCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/KycRequest}
     */
    getKycRequest(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getKycRequest");
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
      let returnType = KycRequest;
      return this.apiClient.callApi(
        '/kyc-requests/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getKycRequestCollection operation.
     * @callback module:api/KYCDocumentsApi~getKycRequestCollectionCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/KycRequest>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve a list of KYC requests
     * Retrieve a list of KYC requests. 
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {Number} [limit] The collection items limit.
     * @param {Number} [offset] The collection items offset.
     * @param {String} [filter] The collection items filter requires a special format. Use \",\" for multiple allowed values.  Use \";\" for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format. 
     * @param {Array.<String>} [sort] The collection items sort field and order (prefix with \"-\" for descending sort).
     * @param {module:api/KYCDocumentsApi~getKycRequestCollectionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/KycRequest>}
     */
    getKycRequestCollection(opts, callback) {
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
      let returnType = [KycRequest];
      return this.apiClient.callApi(
        '/kyc-requests', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patchKycRequest operation.
     * @callback module:api/KYCDocumentsApi~patchKycRequestCallback
     * @param {String} error Error message, if any.
     * @param {module:model/KycRequest} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update a KYC request
     * Update a KYC request.
     * @param {String} id The resource identifier string.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:model/PatchKycRequestRequest} [patchKycRequestRequest] 
     * @param {module:api/KYCDocumentsApi~patchKycRequestCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/KycRequest}
     */
    patchKycRequest(id, opts, callback) {
      opts = opts || {};
      let postBody = opts['patchKycRequestRequest'];
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling patchKycRequest");
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
      let returnType = KycRequest;
      return this.apiClient.callApi(
        '/kyc-requests/{id}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the postKycDocument operation.
     * @callback module:api/KYCDocumentsApi~postKycDocumentCallback
     * @param {String} error Error message, if any.
     * @param {module:model/KycDocument2} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a KYC Document
     * Create a KYC Document. 
     * @param {module:model/KycDocument2} kycDocument2 Kyc document resource.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/KYCDocumentsApi~postKycDocumentCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/KycDocument2}
     */
    postKycDocument(kycDocument2, opts, callback) {
      opts = opts || {};
      let postBody = kycDocument2;
      // verify the required parameter 'kycDocument2' is set
      if (kycDocument2 === undefined || kycDocument2 === null) {
        throw new Error("Missing the required parameter 'kycDocument2' when calling postKycDocument");
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
      let returnType = KycDocument2;
      return this.apiClient.callApi(
        '/kyc-documents', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the postKycDocumentAcceptance operation.
     * @callback module:api/KYCDocumentsApi~postKycDocumentAcceptanceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/KycDocument2} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Accept a KYC document
     * Marks that status of the document as `accepted`. Updates the review time and reviewer information. Intended to be used for manual overrides. 
     * @param {String} id The resource identifier string.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/KYCDocumentsApi~postKycDocumentAcceptanceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/KycDocument2}
     */
    postKycDocumentAcceptance(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling postKycDocumentAcceptance");
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
      let returnType = KycDocument2;
      return this.apiClient.callApi(
        '/kyc-documents/{id}/acceptance', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the postKycDocumentMatches operation.
     * @callback module:api/KYCDocumentsApi~postKycDocumentMatchesCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update a KYC document's documentMatches
     * Updates a KYC document's documentMatches. Intended to be used for manual overrides. 
     * @param {String} id The resource identifier string.
     * @param {module:model/PostKycDocumentMatchesRequest} postKycDocumentMatchesRequest Kyc document resource.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/KYCDocumentsApi~postKycDocumentMatchesCallback} callback The callback function, accepting three arguments: error, data, response
     */
    postKycDocumentMatches(id, postKycDocumentMatchesRequest, opts, callback) {
      opts = opts || {};
      let postBody = postKycDocumentMatchesRequest;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling postKycDocumentMatches");
      }
      // verify the required parameter 'postKycDocumentMatchesRequest' is set
      if (postKycDocumentMatchesRequest === undefined || postKycDocumentMatchesRequest === null) {
        throw new Error("Missing the required parameter 'postKycDocumentMatchesRequest' when calling postKycDocumentMatches");
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
      let returnType = null;
      return this.apiClient.callApi(
        '/kyc-documents/{id}/matches', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the postKycDocumentRejection operation.
     * @callback module:api/KYCDocumentsApi~postKycDocumentRejectionCallback
     * @param {String} error Error message, if any.
     * @param {module:model/KycDocument2} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Reject a KYC document
     * Marks that status of the document as `rejected`. Updates the review time and reviewer information. Intended to be used for manual overrides. 
     * @param {String} id The resource identifier string.
     * @param {module:model/KycDocumentRejection} kycDocumentRejection KYC document resource.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/KYCDocumentsApi~postKycDocumentRejectionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/KycDocument2}
     */
    postKycDocumentRejection(id, kycDocumentRejection, opts, callback) {
      opts = opts || {};
      let postBody = kycDocumentRejection;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling postKycDocumentRejection");
      }
      // verify the required parameter 'kycDocumentRejection' is set
      if (kycDocumentRejection === undefined || kycDocumentRejection === null) {
        throw new Error("Missing the required parameter 'kycDocumentRejection' when calling postKycDocumentRejection");
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
      let returnType = KycDocument2;
      return this.apiClient.callApi(
        '/kyc-documents/{id}/rejection', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the postKycDocumentReview operation.
     * @callback module:api/KYCDocumentsApi~postKycDocumentReviewCallback
     * @param {String} error Error message, if any.
     * @param {module:model/KycDocument2} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Review a KYC document
     * Mark the KYC document as reviewed. Updates the review time and reviewer. information.
     * @param {String} id The resource identifier string.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/KYCDocumentsApi~postKycDocumentReviewCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/KycDocument2}
     */
    postKycDocumentReview(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling postKycDocumentReview");
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
      let returnType = KycDocument2;
      return this.apiClient.callApi(
        '/kyc-documents/{id}/review', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the postKycRequest operation.
     * @callback module:api/KYCDocumentsApi~postKycRequestCallback
     * @param {String} error Error message, if any.
     * @param {module:model/KycRequest} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a KYC Request
     * Create a KYC Request. 
     * @param {module:model/KycRequest} kycRequest Kyc request resource.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/KYCDocumentsApi~postKycRequestCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/KycRequest}
     */
    postKycRequest(kycRequest, opts, callback) {
      opts = opts || {};
      let postBody = kycRequest;
      // verify the required parameter 'kycRequest' is set
      if (kycRequest === undefined || kycRequest === null) {
        throw new Error("Missing the required parameter 'kycRequest' when calling postKycRequest");
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
      let returnType = KycRequest;
      return this.apiClient.callApi(
        '/kyc-requests', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the putKycDocument operation.
     * @callback module:api/KYCDocumentsApi~putKycDocumentCallback
     * @param {String} error Error message, if any.
     * @param {module:model/KycDocument2} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create or update a KYC document with predefined ID
     * Create or update a KYC document with predefined identifier string.
     * @param {String} id The resource identifier string.
     * @param {module:model/KycDocument2} kycDocument2 KYC document resource.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/KYCDocumentsApi~putKycDocumentCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/KycDocument2}
     */
    putKycDocument(id, kycDocument2, opts, callback) {
      opts = opts || {};
      let postBody = kycDocument2;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling putKycDocument");
      }
      // verify the required parameter 'kycDocument2' is set
      if (kycDocument2 === undefined || kycDocument2 === null) {
        throw new Error("Missing the required parameter 'kycDocument2' when calling putKycDocument");
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
      let returnType = KycDocument2;
      return this.apiClient.callApi(
        '/kyc-documents/{id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
