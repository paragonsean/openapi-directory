/**
 * MonitorManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2015-04-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import ErrorResponse from './model/ErrorResponse';
import EventData from './model/EventData';
import EventDataCollection from './model/EventDataCollection';
import HttpRequestInfo from './model/HttpRequestInfo';
import LocalizableString from './model/LocalizableString';
import SenderAuthorization from './model/SenderAuthorization';
import TenantActivityLogsApi from './api/TenantActivityLogsApi';


/**
* JS API client generated by OpenAPI Generator.<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var MonitorManagementClient = require('index'); // See note below*.
* var xxxSvc = new MonitorManagementClient.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new MonitorManagementClient.Yyy(); // Construct a model instance.
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
* var xxxSvc = new MonitorManagementClient.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new MonitorManagementClient.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 2015-04-01
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The ErrorResponse model constructor.
     * @property {module:model/ErrorResponse}
     */
    ErrorResponse,

    /**
     * The EventData model constructor.
     * @property {module:model/EventData}
     */
    EventData,

    /**
     * The EventDataCollection model constructor.
     * @property {module:model/EventDataCollection}
     */
    EventDataCollection,

    /**
     * The HttpRequestInfo model constructor.
     * @property {module:model/HttpRequestInfo}
     */
    HttpRequestInfo,

    /**
     * The LocalizableString model constructor.
     * @property {module:model/LocalizableString}
     */
    LocalizableString,

    /**
     * The SenderAuthorization model constructor.
     * @property {module:model/SenderAuthorization}
     */
    SenderAuthorization,

    /**
    * The TenantActivityLogsApi service constructor.
    * @property {module:api/TenantActivityLogsApi}
    */
    TenantActivityLogsApi
};
