/**
 * TrainingApi
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.2
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import Account from './model/Account';
import AccountQuota from './model/AccountQuota';
import ApiKeys from './model/ApiKeys';
import Domain from './model/Domain';
import Export from './model/Export';
import Image from './model/Image';
import ImageCreateResult from './model/ImageCreateResult';
import ImageCreateSummary from './model/ImageCreateSummary';
import ImageFileCreateBatch from './model/ImageFileCreateBatch';
import ImageFileCreateEntry from './model/ImageFileCreateEntry';
import ImageIdCreateBatch from './model/ImageIdCreateBatch';
import ImageIdCreateEntry from './model/ImageIdCreateEntry';
import ImagePredictionResult from './model/ImagePredictionResult';
import ImageTag from './model/ImageTag';
import ImageTagCreateBatch from './model/ImageTagCreateBatch';
import ImageTagCreateEntry from './model/ImageTagCreateEntry';
import ImageTagCreateSummary from './model/ImageTagCreateSummary';
import ImageTagPrediction from './model/ImageTagPrediction';
import ImageUrl from './model/ImageUrl';
import ImageUrlCreateBatch from './model/ImageUrlCreateBatch';
import ImageUrlCreateEntry from './model/ImageUrlCreateEntry';
import Iteration from './model/Iteration';
import IterationPerformance from './model/IterationPerformance';
import KeyPair from './model/KeyPair';
import PerProjectQuota from './model/PerProjectQuota';
import Prediction from './model/Prediction';
import PredictionQuery from './model/PredictionQuery';
import PredictionQueryTag from './model/PredictionQueryTag';
import PredictionQueryToken from './model/PredictionQueryToken';
import PredictionTag from './model/PredictionTag';
import Project from './model/Project';
import ProjectSettings from './model/ProjectSettings';
import Quota from './model/Quota';
import Tag from './model/Tag';
import TagList from './model/TagList';
import TagPerformance from './model/TagPerformance';
import AccountApiApi from './api/AccountApiApi';
import DomainsApiApi from './api/DomainsApiApi';
import ImageApiApi from './api/ImageApiApi';
import PredictionsApiApi from './api/PredictionsApiApi';
import ProjectApiApi from './api/ProjectApiApi';
import TagsApiApi from './api/TagsApiApi';


/**
* JS API client generated by OpenAPI Generator.<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var TrainingApi = require('index'); // See note below*.
* var xxxSvc = new TrainingApi.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new TrainingApi.Yyy(); // Construct a model instance.
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
* var xxxSvc = new TrainingApi.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new TrainingApi.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 1.2
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The Account model constructor.
     * @property {module:model/Account}
     */
    Account,

    /**
     * The AccountQuota model constructor.
     * @property {module:model/AccountQuota}
     */
    AccountQuota,

    /**
     * The ApiKeys model constructor.
     * @property {module:model/ApiKeys}
     */
    ApiKeys,

    /**
     * The Domain model constructor.
     * @property {module:model/Domain}
     */
    Domain,

    /**
     * The Export model constructor.
     * @property {module:model/Export}
     */
    Export,

    /**
     * The Image model constructor.
     * @property {module:model/Image}
     */
    Image,

    /**
     * The ImageCreateResult model constructor.
     * @property {module:model/ImageCreateResult}
     */
    ImageCreateResult,

    /**
     * The ImageCreateSummary model constructor.
     * @property {module:model/ImageCreateSummary}
     */
    ImageCreateSummary,

    /**
     * The ImageFileCreateBatch model constructor.
     * @property {module:model/ImageFileCreateBatch}
     */
    ImageFileCreateBatch,

    /**
     * The ImageFileCreateEntry model constructor.
     * @property {module:model/ImageFileCreateEntry}
     */
    ImageFileCreateEntry,

    /**
     * The ImageIdCreateBatch model constructor.
     * @property {module:model/ImageIdCreateBatch}
     */
    ImageIdCreateBatch,

    /**
     * The ImageIdCreateEntry model constructor.
     * @property {module:model/ImageIdCreateEntry}
     */
    ImageIdCreateEntry,

    /**
     * The ImagePredictionResult model constructor.
     * @property {module:model/ImagePredictionResult}
     */
    ImagePredictionResult,

    /**
     * The ImageTag model constructor.
     * @property {module:model/ImageTag}
     */
    ImageTag,

    /**
     * The ImageTagCreateBatch model constructor.
     * @property {module:model/ImageTagCreateBatch}
     */
    ImageTagCreateBatch,

    /**
     * The ImageTagCreateEntry model constructor.
     * @property {module:model/ImageTagCreateEntry}
     */
    ImageTagCreateEntry,

    /**
     * The ImageTagCreateSummary model constructor.
     * @property {module:model/ImageTagCreateSummary}
     */
    ImageTagCreateSummary,

    /**
     * The ImageTagPrediction model constructor.
     * @property {module:model/ImageTagPrediction}
     */
    ImageTagPrediction,

    /**
     * The ImageUrl model constructor.
     * @property {module:model/ImageUrl}
     */
    ImageUrl,

    /**
     * The ImageUrlCreateBatch model constructor.
     * @property {module:model/ImageUrlCreateBatch}
     */
    ImageUrlCreateBatch,

    /**
     * The ImageUrlCreateEntry model constructor.
     * @property {module:model/ImageUrlCreateEntry}
     */
    ImageUrlCreateEntry,

    /**
     * The Iteration model constructor.
     * @property {module:model/Iteration}
     */
    Iteration,

    /**
     * The IterationPerformance model constructor.
     * @property {module:model/IterationPerformance}
     */
    IterationPerformance,

    /**
     * The KeyPair model constructor.
     * @property {module:model/KeyPair}
     */
    KeyPair,

    /**
     * The PerProjectQuota model constructor.
     * @property {module:model/PerProjectQuota}
     */
    PerProjectQuota,

    /**
     * The Prediction model constructor.
     * @property {module:model/Prediction}
     */
    Prediction,

    /**
     * The PredictionQuery model constructor.
     * @property {module:model/PredictionQuery}
     */
    PredictionQuery,

    /**
     * The PredictionQueryTag model constructor.
     * @property {module:model/PredictionQueryTag}
     */
    PredictionQueryTag,

    /**
     * The PredictionQueryToken model constructor.
     * @property {module:model/PredictionQueryToken}
     */
    PredictionQueryToken,

    /**
     * The PredictionTag model constructor.
     * @property {module:model/PredictionTag}
     */
    PredictionTag,

    /**
     * The Project model constructor.
     * @property {module:model/Project}
     */
    Project,

    /**
     * The ProjectSettings model constructor.
     * @property {module:model/ProjectSettings}
     */
    ProjectSettings,

    /**
     * The Quota model constructor.
     * @property {module:model/Quota}
     */
    Quota,

    /**
     * The Tag model constructor.
     * @property {module:model/Tag}
     */
    Tag,

    /**
     * The TagList model constructor.
     * @property {module:model/TagList}
     */
    TagList,

    /**
     * The TagPerformance model constructor.
     * @property {module:model/TagPerformance}
     */
    TagPerformance,

    /**
    * The AccountApiApi service constructor.
    * @property {module:api/AccountApiApi}
    */
    AccountApiApi,

    /**
    * The DomainsApiApi service constructor.
    * @property {module:api/DomainsApiApi}
    */
    DomainsApiApi,

    /**
    * The ImageApiApi service constructor.
    * @property {module:api/ImageApiApi}
    */
    ImageApiApi,

    /**
    * The PredictionsApiApi service constructor.
    * @property {module:api/PredictionsApiApi}
    */
    PredictionsApiApi,

    /**
    * The ProjectApiApi service constructor.
    * @property {module:api/ProjectApiApi}
    */
    ProjectApiApi,

    /**
    * The TagsApiApi service constructor.
    * @property {module:api/TagsApiApi}
    */
    TagsApiApi
};
