/**
 * Api Documentation
 * Api Documentation
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import Customer from './model/Customer';
import JwtResponse from './model/JwtResponse';
import LoginUser from './model/LoginUser';
import Problem from './model/Problem';
import ResponseEntity from './model/ResponseEntity';
import ResponseStatus from './model/ResponseStatus';
import AuthenticationApiControllerApi from './api/AuthenticationApiControllerApi';


/**
* Api Documentation.<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var ApiDocumentation = require('index'); // See note below*.
* var xxxSvc = new ApiDocumentation.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new ApiDocumentation.Yyy(); // Construct a model instance.
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
* var xxxSvc = new ApiDocumentation.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new ApiDocumentation.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 1.0
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The Customer model constructor.
     * @property {module:model/Customer}
     */
    Customer,

    /**
     * The JwtResponse model constructor.
     * @property {module:model/JwtResponse}
     */
    JwtResponse,

    /**
     * The LoginUser model constructor.
     * @property {module:model/LoginUser}
     */
    LoginUser,

    /**
     * The Problem model constructor.
     * @property {module:model/Problem}
     */
    Problem,

    /**
     * The ResponseEntity model constructor.
     * @property {module:model/ResponseEntity}
     */
    ResponseEntity,

    /**
     * The ResponseStatus model constructor.
     * @property {module:model/ResponseStatus}
     */
    ResponseStatus,

    /**
    * The AuthenticationApiControllerApi service constructor.
    * @property {module:api/AuthenticationApiControllerApi}
    */
    AuthenticationApiControllerApi
};
