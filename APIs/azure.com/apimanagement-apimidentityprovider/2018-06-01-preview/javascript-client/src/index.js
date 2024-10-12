/**
 * ApiManagementClient
 * Use these REST APIs for performing operations on Identity Provider entity associated with your Azure API Management deployment. Setting up an external Identity Provider for authentication can help you manage the developer portal logins using the OAuth2 flow.
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
import IdentityProviderGet200Response from './model/IdentityProviderGet200Response';
import IdentityProviderListByService200Response from './model/IdentityProviderListByService200Response';
import IdentityProviderListByService200ResponseValueInner from './model/IdentityProviderListByService200ResponseValueInner';
import IdentityProviderListByService200ResponseValueInnerProperties from './model/IdentityProviderListByService200ResponseValueInnerProperties';
import IdentityProviderListByServiceDefaultResponse from './model/IdentityProviderListByServiceDefaultResponse';
import IdentityProviderListByServiceDefaultResponseError from './model/IdentityProviderListByServiceDefaultResponseError';
import IdentityProviderListByServiceDefaultResponseErrorDetailsInner from './model/IdentityProviderListByServiceDefaultResponseErrorDetailsInner';
import IdentityProviderUpdateRequest from './model/IdentityProviderUpdateRequest';
import IdentityProviderUpdateRequestProperties from './model/IdentityProviderUpdateRequestProperties';
import IdentityProviderApi from './api/IdentityProviderApi';


/**
* Use these REST APIs for performing operations on Identity Provider entity associated with your Azure API Management deployment. Setting up an external Identity Provider for authentication can help you manage the developer portal logins using the OAuth2 flow..<br>
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
     * The IdentityProviderGet200Response model constructor.
     * @property {module:model/IdentityProviderGet200Response}
     */
    IdentityProviderGet200Response,

    /**
     * The IdentityProviderListByService200Response model constructor.
     * @property {module:model/IdentityProviderListByService200Response}
     */
    IdentityProviderListByService200Response,

    /**
     * The IdentityProviderListByService200ResponseValueInner model constructor.
     * @property {module:model/IdentityProviderListByService200ResponseValueInner}
     */
    IdentityProviderListByService200ResponseValueInner,

    /**
     * The IdentityProviderListByService200ResponseValueInnerProperties model constructor.
     * @property {module:model/IdentityProviderListByService200ResponseValueInnerProperties}
     */
    IdentityProviderListByService200ResponseValueInnerProperties,

    /**
     * The IdentityProviderListByServiceDefaultResponse model constructor.
     * @property {module:model/IdentityProviderListByServiceDefaultResponse}
     */
    IdentityProviderListByServiceDefaultResponse,

    /**
     * The IdentityProviderListByServiceDefaultResponseError model constructor.
     * @property {module:model/IdentityProviderListByServiceDefaultResponseError}
     */
    IdentityProviderListByServiceDefaultResponseError,

    /**
     * The IdentityProviderListByServiceDefaultResponseErrorDetailsInner model constructor.
     * @property {module:model/IdentityProviderListByServiceDefaultResponseErrorDetailsInner}
     */
    IdentityProviderListByServiceDefaultResponseErrorDetailsInner,

    /**
     * The IdentityProviderUpdateRequest model constructor.
     * @property {module:model/IdentityProviderUpdateRequest}
     */
    IdentityProviderUpdateRequest,

    /**
     * The IdentityProviderUpdateRequestProperties model constructor.
     * @property {module:model/IdentityProviderUpdateRequestProperties}
     */
    IdentityProviderUpdateRequestProperties,

    /**
    * The IdentityProviderApi service constructor.
    * @property {module:api/IdentityProviderApi}
    */
    IdentityProviderApi
};
