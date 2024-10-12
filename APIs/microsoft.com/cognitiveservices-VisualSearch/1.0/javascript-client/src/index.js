/**
 * Visual Search Client
 * Visual Search API lets you discover insights about an image such as visually similar images, shopping sources, and related searches. The API can also perform text recognition, identify entities (people, places, things), return other topical content for the user to explore, and more. For more information, see [Visual Search Overview](https://docs.microsoft.com/azure/cognitive-services/bing-visual-search/overview).  **NOTE:** To comply with the new EU Copyright Directive in France, the Bing Visual Search API must omit some content from certain EU News sources for French users. The removed content may include thumbnail images and videos, video previews, and snippets which accompany search results from these sources. As a consequence, the Bing APIs may serve fewer results with thumbnail images and videos, video previews, and snippets to French users.
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import Action from './model/Action';
import AggregateOffer from './model/AggregateOffer';
import AggregateRating from './model/AggregateRating';
import CreativeWork from './model/CreativeWork';
import CropArea from './model/CropArea';
import Error from './model/Error';
import ErrorResponse from './model/ErrorResponse';
import Filters from './model/Filters';
import Identifiable from './model/Identifiable';
import ImageAction from './model/ImageAction';
import ImageEntityAction from './model/ImageEntityAction';
import ImageInfo from './model/ImageInfo';
import ImageKnowledge from './model/ImageKnowledge';
import ImageModuleAction from './model/ImageModuleAction';
import ImageObject from './model/ImageObject';
import ImageRecipesAction from './model/ImageRecipesAction';
import ImageRelatedSearchesAction from './model/ImageRelatedSearchesAction';
import ImageShoppingSourcesAction from './model/ImageShoppingSourcesAction';
import ImageTag from './model/ImageTag';
import ImageTagRegion from './model/ImageTagRegion';
import ImagesImageMetadata from './model/ImagesImageMetadata';
import ImagesModule from './model/ImagesModule';
import ImagesVisualSearchRequest from './model/ImagesVisualSearchRequest';
import Intangible from './model/Intangible';
import KnowledgeRequest from './model/KnowledgeRequest';
import MediaObject from './model/MediaObject';
import NormalizedQuadrilateral from './model/NormalizedQuadrilateral';
import Offer from './model/Offer';
import Organization from './model/Organization';
import Person from './model/Person';
import Point2D from './model/Point2D';
import PropertiesItem from './model/PropertiesItem';
import Query from './model/Query';
import Rating from './model/Rating';
import Recipe from './model/Recipe';
import RecipesModule from './model/RecipesModule';
import RelatedSearchesModule from './model/RelatedSearchesModule';
import Response from './model/Response';
import ResponseBase from './model/ResponseBase';
import StructuredValue from './model/StructuredValue';
import Thing from './model/Thing';
import VisualSearchRequest from './model/VisualSearchRequest';
import ImageVisualSearchApi from './api/ImageVisualSearchApi';


/**
* Visual Search API lets you discover insights about an image such as visually similar images, shopping sources, and related searches. The API can also perform text recognition, identify entities (people, places, things), return other topical content for the user to explore, and more. For more information, see [Visual Search Overview](https://docs.microsoft.com/azure/cognitive-services/bing-visual-search/overview).  **NOTE:** To comply with the new EU Copyright Directive in France, the Bing Visual Search API must omit some content from certain EU News sources for French users. The removed content may include thumbnail images and videos, video previews, and snippets which accompany search results from these sources. As a consequence, the Bing APIs may serve fewer results with thumbnail images and videos, video previews, and snippets to French users..<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var VisualSearchClient = require('index'); // See note below*.
* var xxxSvc = new VisualSearchClient.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new VisualSearchClient.Yyy(); // Construct a model instance.
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
* var xxxSvc = new VisualSearchClient.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new VisualSearchClient.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 1.0
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The Action model constructor.
     * @property {module:model/Action}
     */
    Action,

    /**
     * The AggregateOffer model constructor.
     * @property {module:model/AggregateOffer}
     */
    AggregateOffer,

    /**
     * The AggregateRating model constructor.
     * @property {module:model/AggregateRating}
     */
    AggregateRating,

    /**
     * The CreativeWork model constructor.
     * @property {module:model/CreativeWork}
     */
    CreativeWork,

    /**
     * The CropArea model constructor.
     * @property {module:model/CropArea}
     */
    CropArea,

    /**
     * The Error model constructor.
     * @property {module:model/Error}
     */
    Error,

    /**
     * The ErrorResponse model constructor.
     * @property {module:model/ErrorResponse}
     */
    ErrorResponse,

    /**
     * The Filters model constructor.
     * @property {module:model/Filters}
     */
    Filters,

    /**
     * The Identifiable model constructor.
     * @property {module:model/Identifiable}
     */
    Identifiable,

    /**
     * The ImageAction model constructor.
     * @property {module:model/ImageAction}
     */
    ImageAction,

    /**
     * The ImageEntityAction model constructor.
     * @property {module:model/ImageEntityAction}
     */
    ImageEntityAction,

    /**
     * The ImageInfo model constructor.
     * @property {module:model/ImageInfo}
     */
    ImageInfo,

    /**
     * The ImageKnowledge model constructor.
     * @property {module:model/ImageKnowledge}
     */
    ImageKnowledge,

    /**
     * The ImageModuleAction model constructor.
     * @property {module:model/ImageModuleAction}
     */
    ImageModuleAction,

    /**
     * The ImageObject model constructor.
     * @property {module:model/ImageObject}
     */
    ImageObject,

    /**
     * The ImageRecipesAction model constructor.
     * @property {module:model/ImageRecipesAction}
     */
    ImageRecipesAction,

    /**
     * The ImageRelatedSearchesAction model constructor.
     * @property {module:model/ImageRelatedSearchesAction}
     */
    ImageRelatedSearchesAction,

    /**
     * The ImageShoppingSourcesAction model constructor.
     * @property {module:model/ImageShoppingSourcesAction}
     */
    ImageShoppingSourcesAction,

    /**
     * The ImageTag model constructor.
     * @property {module:model/ImageTag}
     */
    ImageTag,

    /**
     * The ImageTagRegion model constructor.
     * @property {module:model/ImageTagRegion}
     */
    ImageTagRegion,

    /**
     * The ImagesImageMetadata model constructor.
     * @property {module:model/ImagesImageMetadata}
     */
    ImagesImageMetadata,

    /**
     * The ImagesModule model constructor.
     * @property {module:model/ImagesModule}
     */
    ImagesModule,

    /**
     * The ImagesVisualSearchRequest model constructor.
     * @property {module:model/ImagesVisualSearchRequest}
     */
    ImagesVisualSearchRequest,

    /**
     * The Intangible model constructor.
     * @property {module:model/Intangible}
     */
    Intangible,

    /**
     * The KnowledgeRequest model constructor.
     * @property {module:model/KnowledgeRequest}
     */
    KnowledgeRequest,

    /**
     * The MediaObject model constructor.
     * @property {module:model/MediaObject}
     */
    MediaObject,

    /**
     * The NormalizedQuadrilateral model constructor.
     * @property {module:model/NormalizedQuadrilateral}
     */
    NormalizedQuadrilateral,

    /**
     * The Offer model constructor.
     * @property {module:model/Offer}
     */
    Offer,

    /**
     * The Organization model constructor.
     * @property {module:model/Organization}
     */
    Organization,

    /**
     * The Person model constructor.
     * @property {module:model/Person}
     */
    Person,

    /**
     * The Point2D model constructor.
     * @property {module:model/Point2D}
     */
    Point2D,

    /**
     * The PropertiesItem model constructor.
     * @property {module:model/PropertiesItem}
     */
    PropertiesItem,

    /**
     * The Query model constructor.
     * @property {module:model/Query}
     */
    Query,

    /**
     * The Rating model constructor.
     * @property {module:model/Rating}
     */
    Rating,

    /**
     * The Recipe model constructor.
     * @property {module:model/Recipe}
     */
    Recipe,

    /**
     * The RecipesModule model constructor.
     * @property {module:model/RecipesModule}
     */
    RecipesModule,

    /**
     * The RelatedSearchesModule model constructor.
     * @property {module:model/RelatedSearchesModule}
     */
    RelatedSearchesModule,

    /**
     * The Response model constructor.
     * @property {module:model/Response}
     */
    Response,

    /**
     * The ResponseBase model constructor.
     * @property {module:model/ResponseBase}
     */
    ResponseBase,

    /**
     * The StructuredValue model constructor.
     * @property {module:model/StructuredValue}
     */
    StructuredValue,

    /**
     * The Thing model constructor.
     * @property {module:model/Thing}
     */
    Thing,

    /**
     * The VisualSearchRequest model constructor.
     * @property {module:model/VisualSearchRequest}
     */
    VisualSearchRequest,

    /**
    * The ImageVisualSearchApi service constructor.
    * @property {module:api/ImageVisualSearchApi}
    */
    ImageVisualSearchApi
};
