/**
 * NetworkManagementClient
 * The Microsoft Azure Network management API provides a RESTful set of web services that interact with Microsoft Azure Networks service to manage your network resources. The API has entities that capture the relationship between an end user and the Microsoft Azure Networks service.
 *
 * The version of the OpenAPI document: 2019-06-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import ExpressRouteCircuitPeeringId from './model/ExpressRouteCircuitPeeringId';
import ExpressRouteConnection from './model/ExpressRouteConnection';
import ExpressRouteConnectionId from './model/ExpressRouteConnectionId';
import ExpressRouteConnectionList from './model/ExpressRouteConnectionList';
import ExpressRouteConnectionProperties from './model/ExpressRouteConnectionProperties';
import ExpressRouteGateway from './model/ExpressRouteGateway';
import ExpressRouteGatewayList from './model/ExpressRouteGatewayList';
import ExpressRouteGatewayProperties from './model/ExpressRouteGatewayProperties';
import ExpressRouteGatewayPropertiesAutoScaleConfiguration from './model/ExpressRouteGatewayPropertiesAutoScaleConfiguration';
import ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds from './model/ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds';
import VirtualHubId from './model/VirtualHubId';
import ExpressRouteConnectionsApi from './api/ExpressRouteConnectionsApi';
import ExpressRouteGatewaysApi from './api/ExpressRouteGatewaysApi';


/**
* The Microsoft Azure Network management API provides a RESTful set of web services that interact with Microsoft Azure Networks service to manage your network resources. The API has entities that capture the relationship between an end user and the Microsoft Azure Networks service..<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var NetworkManagementClient = require('index'); // See note below*.
* var xxxSvc = new NetworkManagementClient.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new NetworkManagementClient.Yyy(); // Construct a model instance.
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
* var xxxSvc = new NetworkManagementClient.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new NetworkManagementClient.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 2019-06-01
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The ExpressRouteCircuitPeeringId model constructor.
     * @property {module:model/ExpressRouteCircuitPeeringId}
     */
    ExpressRouteCircuitPeeringId,

    /**
     * The ExpressRouteConnection model constructor.
     * @property {module:model/ExpressRouteConnection}
     */
    ExpressRouteConnection,

    /**
     * The ExpressRouteConnectionId model constructor.
     * @property {module:model/ExpressRouteConnectionId}
     */
    ExpressRouteConnectionId,

    /**
     * The ExpressRouteConnectionList model constructor.
     * @property {module:model/ExpressRouteConnectionList}
     */
    ExpressRouteConnectionList,

    /**
     * The ExpressRouteConnectionProperties model constructor.
     * @property {module:model/ExpressRouteConnectionProperties}
     */
    ExpressRouteConnectionProperties,

    /**
     * The ExpressRouteGateway model constructor.
     * @property {module:model/ExpressRouteGateway}
     */
    ExpressRouteGateway,

    /**
     * The ExpressRouteGatewayList model constructor.
     * @property {module:model/ExpressRouteGatewayList}
     */
    ExpressRouteGatewayList,

    /**
     * The ExpressRouteGatewayProperties model constructor.
     * @property {module:model/ExpressRouteGatewayProperties}
     */
    ExpressRouteGatewayProperties,

    /**
     * The ExpressRouteGatewayPropertiesAutoScaleConfiguration model constructor.
     * @property {module:model/ExpressRouteGatewayPropertiesAutoScaleConfiguration}
     */
    ExpressRouteGatewayPropertiesAutoScaleConfiguration,

    /**
     * The ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds model constructor.
     * @property {module:model/ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds}
     */
    ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds,

    /**
     * The VirtualHubId model constructor.
     * @property {module:model/VirtualHubId}
     */
    VirtualHubId,

    /**
    * The ExpressRouteConnectionsApi service constructor.
    * @property {module:api/ExpressRouteConnectionsApi}
    */
    ExpressRouteConnectionsApi,

    /**
    * The ExpressRouteGatewaysApi service constructor.
    * @property {module:api/ExpressRouteGatewaysApi}
    */
    ExpressRouteGatewaysApi
};
