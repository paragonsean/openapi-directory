/**
 * ApiManagementClient
 * Use these REST APIs for performing operations on the ApiVersionSet entity associated with your Azure API Management deployment. Using this entity you create and manage API Version Sets that are used to group APIs for consistent versioning.
 *
 * The version of the OpenAPI document: 2018-06-01-preview
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import ApiVersionSetCollection from './model/ApiVersionSetCollection';
import ApiVersionSetContract from './model/ApiVersionSetContract';
import ApiVersionSetContractProperties from './model/ApiVersionSetContractProperties';
import ApiVersionSetEntityBase from './model/ApiVersionSetEntityBase';
import ApiVersionSetListByServiceDefaultResponse from './model/ApiVersionSetListByServiceDefaultResponse';
import ApiVersionSetListByServiceDefaultResponseError from './model/ApiVersionSetListByServiceDefaultResponseError';
import ApiVersionSetListByServiceDefaultResponseErrorDetailsInner from './model/ApiVersionSetListByServiceDefaultResponseErrorDetailsInner';
import ApiVersionSetUpdateParameters from './model/ApiVersionSetUpdateParameters';
import ApiVersionSetUpdateParametersProperties from './model/ApiVersionSetUpdateParametersProperties';
import ApiVersionSetsApi from './api/ApiVersionSetsApi';


/**
* Use these REST APIs for performing operations on the ApiVersionSet entity associated with your Azure API Management deployment. Using this entity you create and manage API Version Sets that are used to group APIs for consistent versioning..<br>
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
* @version 2018-06-01-preview
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The ApiVersionSetCollection model constructor.
     * @property {module:model/ApiVersionSetCollection}
     */
    ApiVersionSetCollection,

    /**
     * The ApiVersionSetContract model constructor.
     * @property {module:model/ApiVersionSetContract}
     */
    ApiVersionSetContract,

    /**
     * The ApiVersionSetContractProperties model constructor.
     * @property {module:model/ApiVersionSetContractProperties}
     */
    ApiVersionSetContractProperties,

    /**
     * The ApiVersionSetEntityBase model constructor.
     * @property {module:model/ApiVersionSetEntityBase}
     */
    ApiVersionSetEntityBase,

    /**
     * The ApiVersionSetListByServiceDefaultResponse model constructor.
     * @property {module:model/ApiVersionSetListByServiceDefaultResponse}
     */
    ApiVersionSetListByServiceDefaultResponse,

    /**
     * The ApiVersionSetListByServiceDefaultResponseError model constructor.
     * @property {module:model/ApiVersionSetListByServiceDefaultResponseError}
     */
    ApiVersionSetListByServiceDefaultResponseError,

    /**
     * The ApiVersionSetListByServiceDefaultResponseErrorDetailsInner model constructor.
     * @property {module:model/ApiVersionSetListByServiceDefaultResponseErrorDetailsInner}
     */
    ApiVersionSetListByServiceDefaultResponseErrorDetailsInner,

    /**
     * The ApiVersionSetUpdateParameters model constructor.
     * @property {module:model/ApiVersionSetUpdateParameters}
     */
    ApiVersionSetUpdateParameters,

    /**
     * The ApiVersionSetUpdateParametersProperties model constructor.
     * @property {module:model/ApiVersionSetUpdateParametersProperties}
     */
    ApiVersionSetUpdateParametersProperties,

    /**
    * The ApiVersionSetsApi service constructor.
    * @property {module:api/ApiVersionSetsApi}
    */
    ApiVersionSetsApi
};
