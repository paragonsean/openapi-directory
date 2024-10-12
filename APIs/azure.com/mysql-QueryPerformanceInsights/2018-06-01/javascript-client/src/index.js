/**
 * MySQLManagementClient
 * The Microsoft Azure management API provides create, read, update, and delete functionality for Azure MySQL resources including servers, databases, firewall rules, VNET rules, security alert policies, log files and configurations with new business model.
 *
 * The version of the OpenAPI document: 2018-06-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import QueryStatistic from './model/QueryStatistic';
import QueryStatisticProperties from './model/QueryStatisticProperties';
import QueryText from './model/QueryText';
import QueryTextProperties from './model/QueryTextProperties';
import QueryTextsResultList from './model/QueryTextsResultList';
import TopQueryStatisticsInput from './model/TopQueryStatisticsInput';
import TopQueryStatisticsInputProperties from './model/TopQueryStatisticsInputProperties';
import TopQueryStatisticsResultList from './model/TopQueryStatisticsResultList';
import WaitStatistic from './model/WaitStatistic';
import WaitStatisticProperties from './model/WaitStatisticProperties';
import WaitStatisticsInput from './model/WaitStatisticsInput';
import WaitStatisticsInputProperties from './model/WaitStatisticsInputProperties';
import WaitStatisticsResultList from './model/WaitStatisticsResultList';
import QueryTextsApi from './api/QueryTextsApi';
import TopQueryStatisticsApi from './api/TopQueryStatisticsApi';
import WaitStatisticsApi from './api/WaitStatisticsApi';


/**
* The Microsoft Azure management API provides create, read, update, and delete functionality for Azure MySQL resources including servers, databases, firewall rules, VNET rules, security alert policies, log files and configurations with new business model..<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var MySqlManagementClient = require('index'); // See note below*.
* var xxxSvc = new MySqlManagementClient.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new MySqlManagementClient.Yyy(); // Construct a model instance.
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
* var xxxSvc = new MySqlManagementClient.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new MySqlManagementClient.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 2018-06-01
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The QueryStatistic model constructor.
     * @property {module:model/QueryStatistic}
     */
    QueryStatistic,

    /**
     * The QueryStatisticProperties model constructor.
     * @property {module:model/QueryStatisticProperties}
     */
    QueryStatisticProperties,

    /**
     * The QueryText model constructor.
     * @property {module:model/QueryText}
     */
    QueryText,

    /**
     * The QueryTextProperties model constructor.
     * @property {module:model/QueryTextProperties}
     */
    QueryTextProperties,

    /**
     * The QueryTextsResultList model constructor.
     * @property {module:model/QueryTextsResultList}
     */
    QueryTextsResultList,

    /**
     * The TopQueryStatisticsInput model constructor.
     * @property {module:model/TopQueryStatisticsInput}
     */
    TopQueryStatisticsInput,

    /**
     * The TopQueryStatisticsInputProperties model constructor.
     * @property {module:model/TopQueryStatisticsInputProperties}
     */
    TopQueryStatisticsInputProperties,

    /**
     * The TopQueryStatisticsResultList model constructor.
     * @property {module:model/TopQueryStatisticsResultList}
     */
    TopQueryStatisticsResultList,

    /**
     * The WaitStatistic model constructor.
     * @property {module:model/WaitStatistic}
     */
    WaitStatistic,

    /**
     * The WaitStatisticProperties model constructor.
     * @property {module:model/WaitStatisticProperties}
     */
    WaitStatisticProperties,

    /**
     * The WaitStatisticsInput model constructor.
     * @property {module:model/WaitStatisticsInput}
     */
    WaitStatisticsInput,

    /**
     * The WaitStatisticsInputProperties model constructor.
     * @property {module:model/WaitStatisticsInputProperties}
     */
    WaitStatisticsInputProperties,

    /**
     * The WaitStatisticsResultList model constructor.
     * @property {module:model/WaitStatisticsResultList}
     */
    WaitStatisticsResultList,

    /**
    * The QueryTextsApi service constructor.
    * @property {module:api/QueryTextsApi}
    */
    QueryTextsApi,

    /**
    * The TopQueryStatisticsApi service constructor.
    * @property {module:api/TopQueryStatisticsApi}
    */
    TopQueryStatisticsApi,

    /**
    * The WaitStatisticsApi service constructor.
    * @property {module:api/WaitStatisticsApi}
    */
    WaitStatisticsApi
};
