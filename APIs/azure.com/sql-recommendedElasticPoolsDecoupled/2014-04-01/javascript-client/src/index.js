/**
 * Azure SQL Database
 * Provides create, read, update and delete functionality for Azure SQL Database resources including recommendations and operations.
 *
 * The version of the OpenAPI document: 2014-04-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import RecommendedElasticPool from './model/RecommendedElasticPool';
import RecommendedElasticPoolListMetricsResult from './model/RecommendedElasticPoolListMetricsResult';
import RecommendedElasticPoolListResult from './model/RecommendedElasticPoolListResult';
import RecommendedElasticPoolMetric from './model/RecommendedElasticPoolMetric';
import RecommendedElasticPoolProperties from './model/RecommendedElasticPoolProperties';
import RecommendedElasticPoolPropertiesDatabasesInner from './model/RecommendedElasticPoolPropertiesDatabasesInner';
import RecommendedElasticPoolsApi from './api/RecommendedElasticPoolsApi';


/**
* Provides create, read, update and delete functionality for Azure SQL Database resources including recommendations and operations..<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var AzureSqlDatabase = require('index'); // See note below*.
* var xxxSvc = new AzureSqlDatabase.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new AzureSqlDatabase.Yyy(); // Construct a model instance.
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
* var xxxSvc = new AzureSqlDatabase.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new AzureSqlDatabase.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 2014-04-01
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The RecommendedElasticPool model constructor.
     * @property {module:model/RecommendedElasticPool}
     */
    RecommendedElasticPool,

    /**
     * The RecommendedElasticPoolListMetricsResult model constructor.
     * @property {module:model/RecommendedElasticPoolListMetricsResult}
     */
    RecommendedElasticPoolListMetricsResult,

    /**
     * The RecommendedElasticPoolListResult model constructor.
     * @property {module:model/RecommendedElasticPoolListResult}
     */
    RecommendedElasticPoolListResult,

    /**
     * The RecommendedElasticPoolMetric model constructor.
     * @property {module:model/RecommendedElasticPoolMetric}
     */
    RecommendedElasticPoolMetric,

    /**
     * The RecommendedElasticPoolProperties model constructor.
     * @property {module:model/RecommendedElasticPoolProperties}
     */
    RecommendedElasticPoolProperties,

    /**
     * The RecommendedElasticPoolPropertiesDatabasesInner model constructor.
     * @property {module:model/RecommendedElasticPoolPropertiesDatabasesInner}
     */
    RecommendedElasticPoolPropertiesDatabasesInner,

    /**
    * The RecommendedElasticPoolsApi service constructor.
    * @property {module:api/RecommendedElasticPoolsApi}
    */
    RecommendedElasticPoolsApi
};
