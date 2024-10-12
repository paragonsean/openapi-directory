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
import Attachment from '../model/Attachment';
import Error from '../model/Error';
import InvalidError from '../model/InvalidError';
import PostFileRequest from '../model/PostFileRequest';

/**
* Files service.
* @module api/FilesApi
* @version 2.1
*/
export default class FilesApi {

    /**
    * Constructs a new FilesApi. 
    * @alias module:api/FilesApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the deleteAttachment operation.
     * @callback module:api/FilesApi~deleteAttachmentCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete an Attachment
     * Delete the Attachment with predefined identifier string. 
     * @param {String} id The resource identifier string.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/FilesApi~deleteAttachmentCallback} callback The callback function, accepting three arguments: error, data, response
     */
    deleteAttachment(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling deleteAttachment");
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
        '/attachments/{id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteFile operation.
     * @callback module:api/FilesApi~deleteFileCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete a File
     * Delete the File with predefined identifier string. 
     * @param {String} id The resource identifier string.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/FilesApi~deleteFileCallback} callback The callback function, accepting three arguments: error, data, response
     */
    deleteFile(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling deleteFile");
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
        '/files/{id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getAttachment operation.
     * @callback module:api/FilesApi~getAttachmentCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Attachment} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an Attachment
     * Retrieve a Attachment with specified identifier string. 
     * @param {String} id The resource identifier string.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/FilesApi~getAttachmentCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Attachment}
     */
    getAttachment(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getAttachment");
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
      let returnType = Attachment;
      return this.apiClient.callApi(
        '/attachments/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getAttachmentCollection operation.
     * @callback module:api/FilesApi~getAttachmentCollectionCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/Attachment>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve a list of Attachments
     * Retrieve a list of attachments. You may sort by the id, name, relatedId, relatedType, fileId, createdTime, and updatedTime. 
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {Number} [limit] The collection items limit.
     * @param {Number} [offset] The collection items offset.
     * @param {String} [filter] The collection items filter requires a special format. Use \",\" for multiple allowed values.  Use \";\" for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format. 
     * @param {String} [q] The partial search of the text fields.
     * @param {String} [expand] Expand a response to get a full related object included inside of the `_embedded` path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info. 
     * @param {String} [fields] Limit the returned fields to the list specified, separated by comma. Note that id is always returned.
     * @param {Array.<String>} [sort] The collection items sort field and order (prefix with \"-\" for descending sort).
     * @param {module:api/FilesApi~getAttachmentCollectionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/Attachment>}
     */
    getAttachmentCollection(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'limit': opts['limit'],
        'offset': opts['offset'],
        'filter': opts['filter'],
        'q': opts['q'],
        'expand': opts['expand'],
        'fields': opts['fields'],
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
      let returnType = [Attachment];
      return this.apiClient.callApi(
        '/attachments', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getFile operation.
     * @callback module:api/FilesApi~getFileCallback
     * @param {String} error Error message, if any.
     * @param {File} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve a File Record
     * Retrieve a File with specified identifier string. 
     * @param {String} id The resource identifier string.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/FilesApi~getFileCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link File}
     */
    getFile(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getFile");
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
      let returnType = File;
      return this.apiClient.callApi(
        '/files/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getFileCollection operation.
     * @callback module:api/FilesApi~getFileCollectionCallback
     * @param {String} error Error message, if any.
     * @param {Array.<File>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve a list of files
     * Retrieve a list of files. 
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {Number} [limit] The collection items limit.
     * @param {Number} [offset] The collection items offset.
     * @param {String} [filter] The collection items filter requires a special format. Use \",\" for multiple allowed values.  Use \";\" for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format. 
     * @param {String} [q] The partial search of the text fields.
     * @param {String} [expand] Expand a response to get a full related object included inside of the `_embedded` path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info. 
     * @param {String} [fields] Limit the returned fields to the list specified, separated by comma. Note that id is always returned.
     * @param {Array.<String>} [sort] The collection items sort field and order (prefix with \"-\" for descending sort).
     * @param {module:api/FilesApi~getFileCollectionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<File>}
     */
    getFileCollection(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'limit': opts['limit'],
        'offset': opts['offset'],
        'filter': opts['filter'],
        'q': opts['q'],
        'expand': opts['expand'],
        'fields': opts['fields'],
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
      let returnType = [File];
      return this.apiClient.callApi(
        '/files', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getFileDownload operation.
     * @callback module:api/FilesApi~getFileDownloadCallback
     * @param {String} error Error message, if any.
     * @param {String} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Download a file
     * Download a file. 
     * @param {String} id The resource identifier string.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {String} [imageSize] Resize image to specified size. Supports any sizes from 10x10 to 2000x2000 (format `{width}x{height}`). The image will be returned in the original size if the value is invalid. This parameter will be ignored for non-image files.
     * @param {module:api/FilesApi~getFileDownloadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link String}
     */
    getFileDownload(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getFileDownload");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'imageSize': opts['imageSize']
      };
      let headerParams = {
        'Organization-Id': opts['organizationId']
      };
      let formParams = {
      };

      let authNames = ['SecretApiKey', 'JWT'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = 'String';
      return this.apiClient.callApi(
        '/files/{id}/download', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getFileDownloadExtension operation.
     * @callback module:api/FilesApi~getFileDownloadExtensionCallback
     * @param {String} error Error message, if any.
     * @param {String} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Download image in specific format
     * Download image in specific format. Images are converted server-side. 
     * @param {String} id The resource identifier string.
     * @param {module:model/String} extension File extension which also indicates the desired file format.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/FilesApi~getFileDownloadExtensionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link String}
     */
    getFileDownloadExtension(id, extension, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getFileDownloadExtension");
      }
      // verify the required parameter 'extension' is set
      if (extension === undefined || extension === null) {
        throw new Error("Missing the required parameter 'extension' when calling getFileDownloadExtension");
      }

      let pathParams = {
        'id': id,
        'extension': extension
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
      let returnType = 'String';
      return this.apiClient.callApi(
        '/files/{id}/download{extension}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the postAttachment operation.
     * @callback module:api/FilesApi~postAttachmentCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Attachment} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create an Attachment
     * Create an Attachment. 
     * @param {module:model/Attachment} attachment Attachment resource.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/FilesApi~postAttachmentCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Attachment}
     */
    postAttachment(attachment, opts, callback) {
      opts = opts || {};
      let postBody = attachment;
      // verify the required parameter 'attachment' is set
      if (attachment === undefined || attachment === null) {
        throw new Error("Missing the required parameter 'attachment' when calling postAttachment");
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
      let returnType = Attachment;
      return this.apiClient.callApi(
        '/attachments', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the postFile operation.
     * @callback module:api/FilesApi~postFileCallback
     * @param {String} error Error message, if any.
     * @param {File} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a file
     * Additionally, a file can be sent with:.  - multipart/form-data POST request: in this case all property names are the same as the JSON ones (`file` is an uploaded file)  - file body request: the file body is sent as the request body, with the appropriate `Content-Type`. No additional  properties can be set along the request data  The following file types only are allowed:  - jpg  - png  - gif  - pdf  - mp3   If using a Publishable Api Key, only private files can be created. The files can later on be modified or used using  a secret API key. 
     * @param {module:model/PostFileRequest} postFileRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/FilesApi~postFileCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link File}
     */
    postFile(postFileRequest, opts, callback) {
      opts = opts || {};
      let postBody = postFileRequest;
      // verify the required parameter 'postFileRequest' is set
      if (postFileRequest === undefined || postFileRequest === null) {
        throw new Error("Missing the required parameter 'postFileRequest' when calling postFile");
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

      let authNames = ['SecretApiKey', 'JWT', 'PublishableApiKey'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = File;
      return this.apiClient.callApi(
        '/files', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the putAttachment operation.
     * @callback module:api/FilesApi~putAttachmentCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Attachment} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update the Attachment with predefined ID
     * Update the Attachment with predefined ID. 
     * @param {String} id The resource identifier string.
     * @param {module:model/Attachment} attachment Attachment resource.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/FilesApi~putAttachmentCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Attachment}
     */
    putAttachment(id, attachment, opts, callback) {
      opts = opts || {};
      let postBody = attachment;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling putAttachment");
      }
      // verify the required parameter 'attachment' is set
      if (attachment === undefined || attachment === null) {
        throw new Error("Missing the required parameter 'attachment' when calling putAttachment");
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
      let returnType = Attachment;
      return this.apiClient.callApi(
        '/attachments/{id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the putFile operation.
     * @callback module:api/FilesApi~putFileCallback
     * @param {String} error Error message, if any.
     * @param {File} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update the File with predefined ID
     * Update the File with predefined ID. Note that file can be uploaded with POST. only. 
     * @param {String} id The resource identifier string.
     * @param {File} file File resource.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/FilesApi~putFileCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link File}
     */
    putFile(id, file, opts, callback) {
      opts = opts || {};
      let postBody = file;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling putFile");
      }
      // verify the required parameter 'file' is set
      if (file === undefined || file === null) {
        throw new Error("Missing the required parameter 'file' when calling putFile");
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
      let returnType = File;
      return this.apiClient.callApi(
        '/files/{id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
