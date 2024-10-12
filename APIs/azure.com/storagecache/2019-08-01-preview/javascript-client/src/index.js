/**
 * Storage Cache Mgmt Client
 * A Storage Cache provides scalable caching service for NAS clients, serving data from either NFSv3 or Blob at-rest storage (referred to as \"Storage Targets\"). These operations allow you to manage caches.
 *
 * The version of the OpenAPI document: 2019-08-01-preview
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import ApiOperation from './model/ApiOperation';
import ApiOperationDisplay from './model/ApiOperationDisplay';
import ApiOperationListResult from './model/ApiOperationListResult';
import Cache from './model/Cache';
import CacheHealth from './model/CacheHealth';
import CacheProperties from './model/CacheProperties';
import CacheSku from './model/CacheSku';
import CacheUpgradeStatus from './model/CacheUpgradeStatus';
import CachesListResult from './model/CachesListResult';
import ClfsTarget from './model/ClfsTarget';
import CloudError from './model/CloudError';
import CloudErrorBody from './model/CloudErrorBody';
import NamespaceJunction from './model/NamespaceJunction';
import Nfs3Target from './model/Nfs3Target';
import ResourceSku from './model/ResourceSku';
import ResourceSkuCapabilities from './model/ResourceSkuCapabilities';
import ResourceSkuLocationInfo from './model/ResourceSkuLocationInfo';
import ResourceSkusResult from './model/ResourceSkusResult';
import Restriction from './model/Restriction';
import StorageTarget from './model/StorageTarget';
import StorageTargetProperties from './model/StorageTargetProperties';
import StorageTargetsResult from './model/StorageTargetsResult';
import UnknownTarget from './model/UnknownTarget';
import UsageModel from './model/UsageModel';
import UsageModelDisplay from './model/UsageModelDisplay';
import UsageModelsResult from './model/UsageModelsResult';
import CachesApi from './api/CachesApi';
import OperationsApi from './api/OperationsApi';
import SKUsApi from './api/SKUsApi';
import StorageTargetsApi from './api/StorageTargetsApi';
import UsageModelsApi from './api/UsageModelsApi';


/**
* A Storage Cache provides scalable caching service for NAS clients, serving data from either NFSv3 or Blob at-rest storage (referred to as \&quot;Storage Targets\&quot;). These operations allow you to manage caches..<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var StorageCacheMgmtClient = require('index'); // See note below*.
* var xxxSvc = new StorageCacheMgmtClient.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new StorageCacheMgmtClient.Yyy(); // Construct a model instance.
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
* var xxxSvc = new StorageCacheMgmtClient.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new StorageCacheMgmtClient.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 2019-08-01-preview
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The ApiOperation model constructor.
     * @property {module:model/ApiOperation}
     */
    ApiOperation,

    /**
     * The ApiOperationDisplay model constructor.
     * @property {module:model/ApiOperationDisplay}
     */
    ApiOperationDisplay,

    /**
     * The ApiOperationListResult model constructor.
     * @property {module:model/ApiOperationListResult}
     */
    ApiOperationListResult,

    /**
     * The Cache model constructor.
     * @property {module:model/Cache}
     */
    Cache,

    /**
     * The CacheHealth model constructor.
     * @property {module:model/CacheHealth}
     */
    CacheHealth,

    /**
     * The CacheProperties model constructor.
     * @property {module:model/CacheProperties}
     */
    CacheProperties,

    /**
     * The CacheSku model constructor.
     * @property {module:model/CacheSku}
     */
    CacheSku,

    /**
     * The CacheUpgradeStatus model constructor.
     * @property {module:model/CacheUpgradeStatus}
     */
    CacheUpgradeStatus,

    /**
     * The CachesListResult model constructor.
     * @property {module:model/CachesListResult}
     */
    CachesListResult,

    /**
     * The ClfsTarget model constructor.
     * @property {module:model/ClfsTarget}
     */
    ClfsTarget,

    /**
     * The CloudError model constructor.
     * @property {module:model/CloudError}
     */
    CloudError,

    /**
     * The CloudErrorBody model constructor.
     * @property {module:model/CloudErrorBody}
     */
    CloudErrorBody,

    /**
     * The NamespaceJunction model constructor.
     * @property {module:model/NamespaceJunction}
     */
    NamespaceJunction,

    /**
     * The Nfs3Target model constructor.
     * @property {module:model/Nfs3Target}
     */
    Nfs3Target,

    /**
     * The ResourceSku model constructor.
     * @property {module:model/ResourceSku}
     */
    ResourceSku,

    /**
     * The ResourceSkuCapabilities model constructor.
     * @property {module:model/ResourceSkuCapabilities}
     */
    ResourceSkuCapabilities,

    /**
     * The ResourceSkuLocationInfo model constructor.
     * @property {module:model/ResourceSkuLocationInfo}
     */
    ResourceSkuLocationInfo,

    /**
     * The ResourceSkusResult model constructor.
     * @property {module:model/ResourceSkusResult}
     */
    ResourceSkusResult,

    /**
     * The Restriction model constructor.
     * @property {module:model/Restriction}
     */
    Restriction,

    /**
     * The StorageTarget model constructor.
     * @property {module:model/StorageTarget}
     */
    StorageTarget,

    /**
     * The StorageTargetProperties model constructor.
     * @property {module:model/StorageTargetProperties}
     */
    StorageTargetProperties,

    /**
     * The StorageTargetsResult model constructor.
     * @property {module:model/StorageTargetsResult}
     */
    StorageTargetsResult,

    /**
     * The UnknownTarget model constructor.
     * @property {module:model/UnknownTarget}
     */
    UnknownTarget,

    /**
     * The UsageModel model constructor.
     * @property {module:model/UsageModel}
     */
    UsageModel,

    /**
     * The UsageModelDisplay model constructor.
     * @property {module:model/UsageModelDisplay}
     */
    UsageModelDisplay,

    /**
     * The UsageModelsResult model constructor.
     * @property {module:model/UsageModelsResult}
     */
    UsageModelsResult,

    /**
    * The CachesApi service constructor.
    * @property {module:api/CachesApi}
    */
    CachesApi,

    /**
    * The OperationsApi service constructor.
    * @property {module:api/OperationsApi}
    */
    OperationsApi,

    /**
    * The SKUsApi service constructor.
    * @property {module:api/SKUsApi}
    */
    SKUsApi,

    /**
    * The StorageTargetsApi service constructor.
    * @property {module:api/StorageTargetsApi}
    */
    StorageTargetsApi,

    /**
    * The UsageModelsApi service constructor.
    * @property {module:api/UsageModelsApi}
    */
    UsageModelsApi
};
