/**
 * OnSched API Utility
 * Endpoints for system utilities. e.g.Health
 *
 * The version of the OpenAPI document: v1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import ThreadPoolInfo from './model/ThreadPoolInfo';
import HealthApi from './api/HealthApi';


/**
* Endpoints for system utilities. e.g.Health.<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var OnSchedApiUtility = require('index'); // See note below*.
* var xxxSvc = new OnSchedApiUtility.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new OnSchedApiUtility.Yyy(); // Construct a model instance.
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
* var xxxSvc = new OnSchedApiUtility.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new OnSchedApiUtility.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version v1
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The ThreadPoolInfo model constructor.
     * @property {module:model/ThreadPoolInfo}
     */
    ThreadPoolInfo,

    /**
    * The HealthApi service constructor.
    * @property {module:api/HealthApi}
    */
    HealthApi
};
