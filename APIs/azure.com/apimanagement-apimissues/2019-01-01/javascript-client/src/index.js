/**
 * ApiManagementClient
 * Use this REST API to get all the issues across an Azure Api Management service.
 *
 * The version of the OpenAPI document: 2019-01-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import IssueGet200Response from './model/IssueGet200Response';
import IssueListByService200Response from './model/IssueListByService200Response';
import IssueListByService200ResponseValueInner from './model/IssueListByService200ResponseValueInner';
import IssueListByService200ResponseValueInnerProperties from './model/IssueListByService200ResponseValueInnerProperties';
import IssueListByServiceDefaultResponse from './model/IssueListByServiceDefaultResponse';
import IssueListByServiceDefaultResponseError from './model/IssueListByServiceDefaultResponseError';
import IssueListByServiceDefaultResponseErrorDetailsInner from './model/IssueListByServiceDefaultResponseErrorDetailsInner';
import IssueApi from './api/IssueApi';


/**
* Use this REST API to get all the issues across an Azure Api Management service..<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var ApiManagementClient = require('index'); // See note below*.
* var xxxSvc = new ApiManagementClient.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new ApiManagementClient.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* <em>*NOTE: For a top-level AMD script, use require(['index'], function(){...})
* and put the application logic within the callback function.</em>
* </p>
* <p>
* A non-AMD browser application (discouraged) might do something like this:
* <pre>
* var xxxSvc = new ApiManagementClient.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new ApiManagementClient.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 2019-01-01
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The IssueGet200Response model constructor.
     * @property {module:model/IssueGet200Response}
     */
    IssueGet200Response,

    /**
     * The IssueListByService200Response model constructor.
     * @property {module:model/IssueListByService200Response}
     */
    IssueListByService200Response,

    /**
     * The IssueListByService200ResponseValueInner model constructor.
     * @property {module:model/IssueListByService200ResponseValueInner}
     */
    IssueListByService200ResponseValueInner,

    /**
     * The IssueListByService200ResponseValueInnerProperties model constructor.
     * @property {module:model/IssueListByService200ResponseValueInnerProperties}
     */
    IssueListByService200ResponseValueInnerProperties,

    /**
     * The IssueListByServiceDefaultResponse model constructor.
     * @property {module:model/IssueListByServiceDefaultResponse}
     */
    IssueListByServiceDefaultResponse,

    /**
     * The IssueListByServiceDefaultResponseError model constructor.
     * @property {module:model/IssueListByServiceDefaultResponseError}
     */
    IssueListByServiceDefaultResponseError,

    /**
     * The IssueListByServiceDefaultResponseErrorDetailsInner model constructor.
     * @property {module:model/IssueListByServiceDefaultResponseErrorDetailsInner}
     */
    IssueListByServiceDefaultResponseErrorDetailsInner,

    /**
    * The IssueApi service constructor.
    * @property {module:api/IssueApi}
    */
    IssueApi
};
