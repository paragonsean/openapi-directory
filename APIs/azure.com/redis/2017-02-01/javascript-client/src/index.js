/**
 * RedisManagementClient
 * REST API for Azure Redis Cache Service.
 *
 * The version of the OpenAPI document: 2017-02-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import ExportRDBParameters from './model/ExportRDBParameters';
import ImportRDBParameters from './model/ImportRDBParameters';
import Operation from './model/Operation';
import OperationDisplay from './model/OperationDisplay';
import OperationListResult from './model/OperationListResult';
import ProxyResource from './model/ProxyResource';
import RedisAccessKeys from './model/RedisAccessKeys';
import RedisCreateParameters from './model/RedisCreateParameters';
import RedisCreateProperties from './model/RedisCreateProperties';
import RedisFirewallRule from './model/RedisFirewallRule';
import RedisFirewallRuleListResult from './model/RedisFirewallRuleListResult';
import RedisFirewallRuleProperties from './model/RedisFirewallRuleProperties';
import RedisForceRebootResponse from './model/RedisForceRebootResponse';
import RedisLinkedServer from './model/RedisLinkedServer';
import RedisLinkedServerCreateParameters from './model/RedisLinkedServerCreateParameters';
import RedisLinkedServerCreateProperties from './model/RedisLinkedServerCreateProperties';
import RedisLinkedServerList from './model/RedisLinkedServerList';
import RedisLinkedServerProperties from './model/RedisLinkedServerProperties';
import RedisLinkedServerWithProperties from './model/RedisLinkedServerWithProperties';
import RedisLinkedServerWithPropertiesList from './model/RedisLinkedServerWithPropertiesList';
import RedisListResult from './model/RedisListResult';
import RedisPatchSchedule from './model/RedisPatchSchedule';
import RedisProperties from './model/RedisProperties';
import RedisRebootParameters from './model/RedisRebootParameters';
import RedisRegenerateKeyParameters from './model/RedisRegenerateKeyParameters';
import RedisResource from './model/RedisResource';
import RedisResourceProperties from './model/RedisResourceProperties';
import RedisUpdateParameters from './model/RedisUpdateParameters';
import RedisUpdateProperties from './model/RedisUpdateProperties';
import Resource from './model/Resource';
import ScheduleEntries from './model/ScheduleEntries';
import ScheduleEntry from './model/ScheduleEntry';
import Sku from './model/Sku';
import TrackedResource from './model/TrackedResource';
import FirewallRulesApi from './api/FirewallRulesApi';
import OperationsApi from './api/OperationsApi';
import RedisApi from './api/RedisApi';


/**
* REST API for Azure Redis Cache Service..<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var RedisManagementClient = require('index'); // See note below*.
* var xxxSvc = new RedisManagementClient.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new RedisManagementClient.Yyy(); // Construct a model instance.
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
* var xxxSvc = new RedisManagementClient.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new RedisManagementClient.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 2017-02-01
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The ExportRDBParameters model constructor.
     * @property {module:model/ExportRDBParameters}
     */
    ExportRDBParameters,

    /**
     * The ImportRDBParameters model constructor.
     * @property {module:model/ImportRDBParameters}
     */
    ImportRDBParameters,

    /**
     * The Operation model constructor.
     * @property {module:model/Operation}
     */
    Operation,

    /**
     * The OperationDisplay model constructor.
     * @property {module:model/OperationDisplay}
     */
    OperationDisplay,

    /**
     * The OperationListResult model constructor.
     * @property {module:model/OperationListResult}
     */
    OperationListResult,

    /**
     * The ProxyResource model constructor.
     * @property {module:model/ProxyResource}
     */
    ProxyResource,

    /**
     * The RedisAccessKeys model constructor.
     * @property {module:model/RedisAccessKeys}
     */
    RedisAccessKeys,

    /**
     * The RedisCreateParameters model constructor.
     * @property {module:model/RedisCreateParameters}
     */
    RedisCreateParameters,

    /**
     * The RedisCreateProperties model constructor.
     * @property {module:model/RedisCreateProperties}
     */
    RedisCreateProperties,

    /**
     * The RedisFirewallRule model constructor.
     * @property {module:model/RedisFirewallRule}
     */
    RedisFirewallRule,

    /**
     * The RedisFirewallRuleListResult model constructor.
     * @property {module:model/RedisFirewallRuleListResult}
     */
    RedisFirewallRuleListResult,

    /**
     * The RedisFirewallRuleProperties model constructor.
     * @property {module:model/RedisFirewallRuleProperties}
     */
    RedisFirewallRuleProperties,

    /**
     * The RedisForceRebootResponse model constructor.
     * @property {module:model/RedisForceRebootResponse}
     */
    RedisForceRebootResponse,

    /**
     * The RedisLinkedServer model constructor.
     * @property {module:model/RedisLinkedServer}
     */
    RedisLinkedServer,

    /**
     * The RedisLinkedServerCreateParameters model constructor.
     * @property {module:model/RedisLinkedServerCreateParameters}
     */
    RedisLinkedServerCreateParameters,

    /**
     * The RedisLinkedServerCreateProperties model constructor.
     * @property {module:model/RedisLinkedServerCreateProperties}
     */
    RedisLinkedServerCreateProperties,

    /**
     * The RedisLinkedServerList model constructor.
     * @property {module:model/RedisLinkedServerList}
     */
    RedisLinkedServerList,

    /**
     * The RedisLinkedServerProperties model constructor.
     * @property {module:model/RedisLinkedServerProperties}
     */
    RedisLinkedServerProperties,

    /**
     * The RedisLinkedServerWithProperties model constructor.
     * @property {module:model/RedisLinkedServerWithProperties}
     */
    RedisLinkedServerWithProperties,

    /**
     * The RedisLinkedServerWithPropertiesList model constructor.
     * @property {module:model/RedisLinkedServerWithPropertiesList}
     */
    RedisLinkedServerWithPropertiesList,

    /**
     * The RedisListResult model constructor.
     * @property {module:model/RedisListResult}
     */
    RedisListResult,

    /**
     * The RedisPatchSchedule model constructor.
     * @property {module:model/RedisPatchSchedule}
     */
    RedisPatchSchedule,

    /**
     * The RedisProperties model constructor.
     * @property {module:model/RedisProperties}
     */
    RedisProperties,

    /**
     * The RedisRebootParameters model constructor.
     * @property {module:model/RedisRebootParameters}
     */
    RedisRebootParameters,

    /**
     * The RedisRegenerateKeyParameters model constructor.
     * @property {module:model/RedisRegenerateKeyParameters}
     */
    RedisRegenerateKeyParameters,

    /**
     * The RedisResource model constructor.
     * @property {module:model/RedisResource}
     */
    RedisResource,

    /**
     * The RedisResourceProperties model constructor.
     * @property {module:model/RedisResourceProperties}
     */
    RedisResourceProperties,

    /**
     * The RedisUpdateParameters model constructor.
     * @property {module:model/RedisUpdateParameters}
     */
    RedisUpdateParameters,

    /**
     * The RedisUpdateProperties model constructor.
     * @property {module:model/RedisUpdateProperties}
     */
    RedisUpdateProperties,

    /**
     * The Resource model constructor.
     * @property {module:model/Resource}
     */
    Resource,

    /**
     * The ScheduleEntries model constructor.
     * @property {module:model/ScheduleEntries}
     */
    ScheduleEntries,

    /**
     * The ScheduleEntry model constructor.
     * @property {module:model/ScheduleEntry}
     */
    ScheduleEntry,

    /**
     * The Sku model constructor.
     * @property {module:model/Sku}
     */
    Sku,

    /**
     * The TrackedResource model constructor.
     * @property {module:model/TrackedResource}
     */
    TrackedResource,

    /**
    * The FirewallRulesApi service constructor.
    * @property {module:api/FirewallRulesApi}
    */
    FirewallRulesApi,

    /**
    * The OperationsApi service constructor.
    * @property {module:api/OperationsApi}
    */
    OperationsApi,

    /**
    * The RedisApi service constructor.
    * @property {module:api/RedisApi}
    */
    RedisApi
};
