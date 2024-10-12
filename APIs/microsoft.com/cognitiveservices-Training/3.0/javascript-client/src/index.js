/**
 * Custom Vision Training Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 3.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import BoundingBox from './model/BoundingBox';
import CustomVisionError from './model/CustomVisionError';
import Domain from './model/Domain';
import Export from './model/Export';
import Image from './model/Image';
import ImageCreateResult from './model/ImageCreateResult';
import ImageCreateSummary from './model/ImageCreateSummary';
import ImageFileCreateBatch from './model/ImageFileCreateBatch';
import ImageFileCreateEntry from './model/ImageFileCreateEntry';
import ImageIdCreateBatch from './model/ImageIdCreateBatch';
import ImageIdCreateEntry from './model/ImageIdCreateEntry';
import ImagePerformance from './model/ImagePerformance';
import ImagePrediction from './model/ImagePrediction';
import ImageRegion from './model/ImageRegion';
import ImageRegionCreateBatch from './model/ImageRegionCreateBatch';
import ImageRegionCreateEntry from './model/ImageRegionCreateEntry';
import ImageRegionCreateResult from './model/ImageRegionCreateResult';
import ImageRegionCreateSummary from './model/ImageRegionCreateSummary';
import ImageRegionProposal from './model/ImageRegionProposal';
import ImageTag from './model/ImageTag';
import ImageTagCreateBatch from './model/ImageTagCreateBatch';
import ImageTagCreateEntry from './model/ImageTagCreateEntry';
import ImageTagCreateSummary from './model/ImageTagCreateSummary';
import ImageUrl from './model/ImageUrl';
import ImageUrlCreateBatch from './model/ImageUrlCreateBatch';
import ImageUrlCreateEntry from './model/ImageUrlCreateEntry';
import Iteration from './model/Iteration';
import IterationPerformance from './model/IterationPerformance';
import Prediction from './model/Prediction';
import PredictionQueryResult from './model/PredictionQueryResult';
import PredictionQueryTag from './model/PredictionQueryTag';
import PredictionQueryToken from './model/PredictionQueryToken';
import Project from './model/Project';
import ProjectSettings from './model/ProjectSettings';
import Region from './model/Region';
import RegionProposal from './model/RegionProposal';
import StoredImagePrediction from './model/StoredImagePrediction';
import Tag from './model/Tag';
import TagPerformance from './model/TagPerformance';
import DomainsApiApi from './api/DomainsApiApi';
import ImageApiApi from './api/ImageApiApi';
import ImageRegionProposalApiApi from './api/ImageRegionProposalApiApi';
import PredictionsApiApi from './api/PredictionsApiApi';
import ProjectApiApi from './api/ProjectApiApi';
import TagsApiApi from './api/TagsApiApi';


/**
* JS API client generated by OpenAPI Generator.<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var CustomVisionTrainingClient = require('index'); // See note below*.
* var xxxSvc = new CustomVisionTrainingClient.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new CustomVisionTrainingClient.Yyy(); // Construct a model instance.
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
* var xxxSvc = new CustomVisionTrainingClient.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new CustomVisionTrainingClient.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 3.0
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The BoundingBox model constructor.
     * @property {module:model/BoundingBox}
     */
    BoundingBox,

    /**
     * The CustomVisionError model constructor.
     * @property {module:model/CustomVisionError}
     */
    CustomVisionError,

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
     * The ImagePerformance model constructor.
     * @property {module:model/ImagePerformance}
     */
    ImagePerformance,

    /**
     * The ImagePrediction model constructor.
     * @property {module:model/ImagePrediction}
     */
    ImagePrediction,

    /**
     * The ImageRegion model constructor.
     * @property {module:model/ImageRegion}
     */
    ImageRegion,

    /**
     * The ImageRegionCreateBatch model constructor.
     * @property {module:model/ImageRegionCreateBatch}
     */
    ImageRegionCreateBatch,

    /**
     * The ImageRegionCreateEntry model constructor.
     * @property {module:model/ImageRegionCreateEntry}
     */
    ImageRegionCreateEntry,

    /**
     * The ImageRegionCreateResult model constructor.
     * @property {module:model/ImageRegionCreateResult}
     */
    ImageRegionCreateResult,

    /**
     * The ImageRegionCreateSummary model constructor.
     * @property {module:model/ImageRegionCreateSummary}
     */
    ImageRegionCreateSummary,

    /**
     * The ImageRegionProposal model constructor.
     * @property {module:model/ImageRegionProposal}
     */
    ImageRegionProposal,

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
     * The Prediction model constructor.
     * @property {module:model/Prediction}
     */
    Prediction,

    /**
     * The PredictionQueryResult model constructor.
     * @property {module:model/PredictionQueryResult}
     */
    PredictionQueryResult,

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
     * The Region model constructor.
     * @property {module:model/Region}
     */
    Region,

    /**
     * The RegionProposal model constructor.
     * @property {module:model/RegionProposal}
     */
    RegionProposal,

    /**
     * The StoredImagePrediction model constructor.
     * @property {module:model/StoredImagePrediction}
     */
    StoredImagePrediction,

    /**
     * The Tag model constructor.
     * @property {module:model/Tag}
     */
    Tag,

    /**
     * The TagPerformance model constructor.
     * @property {module:model/TagPerformance}
     */
    TagPerformance,

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
    * The ImageRegionProposalApiApi service constructor.
    * @property {module:api/ImageRegionProposalApiApi}
    */
    ImageRegionProposalApiApi,

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
