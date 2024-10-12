/**
 * Listen API: Podcast Search, Directory, and Insights API
 * Simple & no-nonsense podcast search & directory API. Search all podcasts and episodes by people, places, or topics. 
 *
 * The version of the OpenAPI document: 2.0
 * Contact: hello@listennotes.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import BestPodcastsResponse from './model/BestPodcastsResponse';
import CuratedListFull from './model/CuratedListFull';
import CuratedListSearchResult from './model/CuratedListSearchResult';
import CuratedListSimple from './model/CuratedListSimple';
import CustomAudio from './model/CustomAudio';
import DeletePodcastResponse from './model/DeletePodcastResponse';
import DeletedItem from './model/DeletedItem';
import EpisodeFull from './model/EpisodeFull';
import EpisodeMinimum from './model/EpisodeMinimum';
import EpisodeSearchResult from './model/EpisodeSearchResult';
import EpisodeSearchResultPodcast from './model/EpisodeSearchResultPodcast';
import EpisodeSimple from './model/EpisodeSimple';
import Genre from './model/Genre';
import GetCuratedPodcastsResponse from './model/GetCuratedPodcastsResponse';
import GetEpisodeRecommendationsResponse from './model/GetEpisodeRecommendationsResponse';
import GetEpisodesInBatchResponse from './model/GetEpisodesInBatchResponse';
import GetGenresResponse from './model/GetGenresResponse';
import GetLanguagesResponse from './model/GetLanguagesResponse';
import GetPodcastRecommendationsResponse from './model/GetPodcastRecommendationsResponse';
import GetPodcastsInBatchResponse from './model/GetPodcastsInBatchResponse';
import GetRegionsResponse from './model/GetRegionsResponse';
import PlaylistItem from './model/PlaylistItem';
import PlaylistItemData from './model/PlaylistItemData';
import PlaylistResponse from './model/PlaylistResponse';
import PlaylistVisibilityField from './model/PlaylistVisibilityField';
import PlaylistsResponse from './model/PlaylistsResponse';
import PlaylistsResponsePlaylistsInner from './model/PlaylistsResponsePlaylistsInner';
import PodcastAudienceResponse from './model/PodcastAudienceResponse';
import PodcastAudienceResponseByRegionsInner from './model/PodcastAudienceResponseByRegionsInner';
import PodcastDomainResponse from './model/PodcastDomainResponse';
import PodcastExtraField from './model/PodcastExtraField';
import PodcastFull from './model/PodcastFull';
import PodcastLookingForField from './model/PodcastLookingForField';
import PodcastMinimum from './model/PodcastMinimum';
import PodcastMinimumRss from './model/PodcastMinimumRss';
import PodcastSearchResult from './model/PodcastSearchResult';
import PodcastSimple from './model/PodcastSimple';
import PodcastTypeField from './model/PodcastTypeField';
import PodcastTypeaheadResult from './model/PodcastTypeaheadResult';
import RelatedSearchesResponse from './model/RelatedSearchesResponse';
import SearchResponse from './model/SearchResponse';
import SearchResponseResultsInner from './model/SearchResponseResultsInner';
import SpellCheckResponse from './model/SpellCheckResponse';
import SpellCheckResponseTokensInner from './model/SpellCheckResponseTokensInner';
import SubmitPodcastResponse from './model/SubmitPodcastResponse';
import TrendingSearchesResponse from './model/TrendingSearchesResponse';
import TypeaheadResponse from './model/TypeaheadResponse';
import DirectoryAPIApi from './api/DirectoryAPIApi';
import InsightsAPIApi from './api/InsightsAPIApi';
import PlaylistAPIApi from './api/PlaylistAPIApi';
import PodcasterAPIApi from './api/PodcasterAPIApi';
import SearchAPIApi from './api/SearchAPIApi';


/**
* Simple &amp; no-nonsense podcast search &amp; directory API. Search all podcasts and episodes by people, places, or topics. .<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var ListenApiPodcastSearchDirectoryAndInsightsApi = require('index'); // See note below*.
* var xxxSvc = new ListenApiPodcastSearchDirectoryAndInsightsApi.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new ListenApiPodcastSearchDirectoryAndInsightsApi.Yyy(); // Construct a model instance.
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
* var xxxSvc = new ListenApiPodcastSearchDirectoryAndInsightsApi.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new ListenApiPodcastSearchDirectoryAndInsightsApi.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 2.0
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The BestPodcastsResponse model constructor.
     * @property {module:model/BestPodcastsResponse}
     */
    BestPodcastsResponse,

    /**
     * The CuratedListFull model constructor.
     * @property {module:model/CuratedListFull}
     */
    CuratedListFull,

    /**
     * The CuratedListSearchResult model constructor.
     * @property {module:model/CuratedListSearchResult}
     */
    CuratedListSearchResult,

    /**
     * The CuratedListSimple model constructor.
     * @property {module:model/CuratedListSimple}
     */
    CuratedListSimple,

    /**
     * The CustomAudio model constructor.
     * @property {module:model/CustomAudio}
     */
    CustomAudio,

    /**
     * The DeletePodcastResponse model constructor.
     * @property {module:model/DeletePodcastResponse}
     */
    DeletePodcastResponse,

    /**
     * The DeletedItem model constructor.
     * @property {module:model/DeletedItem}
     */
    DeletedItem,

    /**
     * The EpisodeFull model constructor.
     * @property {module:model/EpisodeFull}
     */
    EpisodeFull,

    /**
     * The EpisodeMinimum model constructor.
     * @property {module:model/EpisodeMinimum}
     */
    EpisodeMinimum,

    /**
     * The EpisodeSearchResult model constructor.
     * @property {module:model/EpisodeSearchResult}
     */
    EpisodeSearchResult,

    /**
     * The EpisodeSearchResultPodcast model constructor.
     * @property {module:model/EpisodeSearchResultPodcast}
     */
    EpisodeSearchResultPodcast,

    /**
     * The EpisodeSimple model constructor.
     * @property {module:model/EpisodeSimple}
     */
    EpisodeSimple,

    /**
     * The Genre model constructor.
     * @property {module:model/Genre}
     */
    Genre,

    /**
     * The GetCuratedPodcastsResponse model constructor.
     * @property {module:model/GetCuratedPodcastsResponse}
     */
    GetCuratedPodcastsResponse,

    /**
     * The GetEpisodeRecommendationsResponse model constructor.
     * @property {module:model/GetEpisodeRecommendationsResponse}
     */
    GetEpisodeRecommendationsResponse,

    /**
     * The GetEpisodesInBatchResponse model constructor.
     * @property {module:model/GetEpisodesInBatchResponse}
     */
    GetEpisodesInBatchResponse,

    /**
     * The GetGenresResponse model constructor.
     * @property {module:model/GetGenresResponse}
     */
    GetGenresResponse,

    /**
     * The GetLanguagesResponse model constructor.
     * @property {module:model/GetLanguagesResponse}
     */
    GetLanguagesResponse,

    /**
     * The GetPodcastRecommendationsResponse model constructor.
     * @property {module:model/GetPodcastRecommendationsResponse}
     */
    GetPodcastRecommendationsResponse,

    /**
     * The GetPodcastsInBatchResponse model constructor.
     * @property {module:model/GetPodcastsInBatchResponse}
     */
    GetPodcastsInBatchResponse,

    /**
     * The GetRegionsResponse model constructor.
     * @property {module:model/GetRegionsResponse}
     */
    GetRegionsResponse,

    /**
     * The PlaylistItem model constructor.
     * @property {module:model/PlaylistItem}
     */
    PlaylistItem,

    /**
     * The PlaylistItemData model constructor.
     * @property {module:model/PlaylistItemData}
     */
    PlaylistItemData,

    /**
     * The PlaylistResponse model constructor.
     * @property {module:model/PlaylistResponse}
     */
    PlaylistResponse,

    /**
     * The PlaylistVisibilityField model constructor.
     * @property {module:model/PlaylistVisibilityField}
     */
    PlaylistVisibilityField,

    /**
     * The PlaylistsResponse model constructor.
     * @property {module:model/PlaylistsResponse}
     */
    PlaylistsResponse,

    /**
     * The PlaylistsResponsePlaylistsInner model constructor.
     * @property {module:model/PlaylistsResponsePlaylistsInner}
     */
    PlaylistsResponsePlaylistsInner,

    /**
     * The PodcastAudienceResponse model constructor.
     * @property {module:model/PodcastAudienceResponse}
     */
    PodcastAudienceResponse,

    /**
     * The PodcastAudienceResponseByRegionsInner model constructor.
     * @property {module:model/PodcastAudienceResponseByRegionsInner}
     */
    PodcastAudienceResponseByRegionsInner,

    /**
     * The PodcastDomainResponse model constructor.
     * @property {module:model/PodcastDomainResponse}
     */
    PodcastDomainResponse,

    /**
     * The PodcastExtraField model constructor.
     * @property {module:model/PodcastExtraField}
     */
    PodcastExtraField,

    /**
     * The PodcastFull model constructor.
     * @property {module:model/PodcastFull}
     */
    PodcastFull,

    /**
     * The PodcastLookingForField model constructor.
     * @property {module:model/PodcastLookingForField}
     */
    PodcastLookingForField,

    /**
     * The PodcastMinimum model constructor.
     * @property {module:model/PodcastMinimum}
     */
    PodcastMinimum,

    /**
     * The PodcastMinimumRss model constructor.
     * @property {module:model/PodcastMinimumRss}
     */
    PodcastMinimumRss,

    /**
     * The PodcastSearchResult model constructor.
     * @property {module:model/PodcastSearchResult}
     */
    PodcastSearchResult,

    /**
     * The PodcastSimple model constructor.
     * @property {module:model/PodcastSimple}
     */
    PodcastSimple,

    /**
     * The PodcastTypeField model constructor.
     * @property {module:model/PodcastTypeField}
     */
    PodcastTypeField,

    /**
     * The PodcastTypeaheadResult model constructor.
     * @property {module:model/PodcastTypeaheadResult}
     */
    PodcastTypeaheadResult,

    /**
     * The RelatedSearchesResponse model constructor.
     * @property {module:model/RelatedSearchesResponse}
     */
    RelatedSearchesResponse,

    /**
     * The SearchResponse model constructor.
     * @property {module:model/SearchResponse}
     */
    SearchResponse,

    /**
     * The SearchResponseResultsInner model constructor.
     * @property {module:model/SearchResponseResultsInner}
     */
    SearchResponseResultsInner,

    /**
     * The SpellCheckResponse model constructor.
     * @property {module:model/SpellCheckResponse}
     */
    SpellCheckResponse,

    /**
     * The SpellCheckResponseTokensInner model constructor.
     * @property {module:model/SpellCheckResponseTokensInner}
     */
    SpellCheckResponseTokensInner,

    /**
     * The SubmitPodcastResponse model constructor.
     * @property {module:model/SubmitPodcastResponse}
     */
    SubmitPodcastResponse,

    /**
     * The TrendingSearchesResponse model constructor.
     * @property {module:model/TrendingSearchesResponse}
     */
    TrendingSearchesResponse,

    /**
     * The TypeaheadResponse model constructor.
     * @property {module:model/TypeaheadResponse}
     */
    TypeaheadResponse,

    /**
    * The DirectoryAPIApi service constructor.
    * @property {module:api/DirectoryAPIApi}
    */
    DirectoryAPIApi,

    /**
    * The InsightsAPIApi service constructor.
    * @property {module:api/InsightsAPIApi}
    */
    InsightsAPIApi,

    /**
    * The PlaylistAPIApi service constructor.
    * @property {module:api/PlaylistAPIApi}
    */
    PlaylistAPIApi,

    /**
    * The PodcasterAPIApi service constructor.
    * @property {module:api/PodcasterAPIApi}
    */
    PodcasterAPIApi,

    /**
    * The SearchAPIApi service constructor.
    * @property {module:api/SearchAPIApi}
    */
    SearchAPIApi
};
