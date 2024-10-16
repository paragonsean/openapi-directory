/**
 * Blazemeter API Explorer
 * Live API Documentation
 *
 * The version of the OpenAPI document: 4
 * Contact: support@blazemeter.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import ApiResponse from './model/ApiResponse';
import UserModel1 from './model/UserModel1';
import UserModel2 from './model/UserModel2';
import UserModel3 from './model/UserModel3';
import UserModel4 from './model/UserModel4';
import UserModel5 from './model/UserModel5';
import UserApi from './api/UserApi';


/**
* Live API Documentation.<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var BlazemeterApiExplorer = require('index'); // See note below*.
* var xxxSvc = new BlazemeterApiExplorer.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new BlazemeterApiExplorer.Yyy(); // Construct a model instance.
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
* var xxxSvc = new BlazemeterApiExplorer.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new BlazemeterApiExplorer.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 4
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The ApiResponse model constructor.
     * @property {module:model/ApiResponse}
     */
    ApiResponse,

    /**
     * The UserModel1 model constructor.
     * @property {module:model/UserModel1}
     */
    UserModel1,

    /**
     * The UserModel2 model constructor.
     * @property {module:model/UserModel2}
     */
    UserModel2,

    /**
     * The UserModel3 model constructor.
     * @property {module:model/UserModel3}
     */
    UserModel3,

    /**
     * The UserModel4 model constructor.
     * @property {module:model/UserModel4}
     */
    UserModel4,

    /**
     * The UserModel5 model constructor.
     * @property {module:model/UserModel5}
     */
    UserModel5,

    /**
    * The UserApi service constructor.
    * @property {module:api/UserApi}
    */
    UserApi
};
