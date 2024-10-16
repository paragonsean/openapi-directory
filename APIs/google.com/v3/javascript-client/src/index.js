/**
 * Travel Partner API
 * The Travel Partner API provides you with a RESTful interface to the Google Hotel Center platform. It enables an app to efficiently retrieve and change Hotel Center data, and is thus suitable for managing large or complex accounts.
 *
 * The version of the OpenAPI document: v3
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import AccountLink from './model/AccountLink';
import AccountLinkTarget from './model/AccountLinkTarget';
import Brand from './model/Brand';
import CreateReconciliationReportResponse from './model/CreateReconciliationReportResponse';
import DataIssueDetail from './model/DataIssueDetail';
import DisplayNameDisapprovalReason from './model/DisplayNameDisapprovalReason';
import FreeBookingLinksResult from './model/FreeBookingLinksResult';
import HotelList from './model/HotelList';
import HotelPricePerItinerary from './model/HotelPricePerItinerary';
import HotelView from './model/HotelView';
import Icon from './model/Icon';
import Image from './model/Image';
import Key from './model/Key';
import LatLng from './model/LatLng';
import ListAccountLinksResponse from './model/ListAccountLinksResponse';
import ListBrandsResponse from './model/ListBrandsResponse';
import ListHotelViewsResponse from './model/ListHotelViewsResponse';
import ListIconsResponse from './model/ListIconsResponse';
import ListPriceAccuracyViewsResponse from './model/ListPriceAccuracyViewsResponse';
import ListPriceCoverageViewsResponse from './model/ListPriceCoverageViewsResponse';
import ListReconciliationReportsResponse from './model/ListReconciliationReportsResponse';
import LocalizedText from './model/LocalizedText';
import MissedParticipationCountDetails from './model/MissedParticipationCountDetails';
import ModelDate from './model/ModelDate';
import NoPriceCountDetails from './model/NoPriceCountDetails';
import ParsedListing from './model/ParsedListing';
import ParticipationResult from './model/ParticipationResult';
import PriceAccuracyRow from './model/PriceAccuracyRow';
import PriceAccuracyView from './model/PriceAccuracyView';
import PriceCoverageBucket from './model/PriceCoverageBucket';
import PriceCoverageView from './model/PriceCoverageView';
import PriceMissingCountDetails from './model/PriceMissingCountDetails';
import PriceProblemCountDetails from './model/PriceProblemCountDetails';
import PriceRecord from './model/PriceRecord';
import PriceUnavailableCountDetails from './model/PriceUnavailableCountDetails';
import PriceView from './model/PriceView';
import PropertyPerformanceResult from './model/PropertyPerformanceResult';
import QueryFreeBookingLinksReportResponse from './model/QueryFreeBookingLinksReportResponse';
import QueryParticipationReportResponse from './model/QueryParticipationReportResponse';
import QueryPropertyPerformanceReportResponse from './model/QueryPropertyPerformanceReportResponse';
import Rating from './model/Rating';
import ReconciliationReport from './model/ReconciliationReport';
import ReconciliationReportValidationIssue from './model/ReconciliationReportValidationIssue';
import Review from './model/Review';
import SetLiveOnGoogleRequest from './model/SetLiveOnGoogleRequest';
import SetLiveOnGoogleResponse from './model/SetLiveOnGoogleResponse';
import SummarizeHotelViewsResponse from './model/SummarizeHotelViewsResponse';
import SummarizePriceAccuracyResponse from './model/SummarizePriceAccuracyResponse';
import ValidateReconciliationReportResponse from './model/ValidateReconciliationReportResponse';
import VerifyListingsRequest from './model/VerifyListingsRequest';
import VerifyListingsResponse from './model/VerifyListingsResponse';
import AccountsApi from './api/AccountsApi';


/**
* The Travel Partner API provides you with a RESTful interface to the Google Hotel Center platform. It enables an app to efficiently retrieve and change Hotel Center data, and is thus suitable for managing large or complex accounts..<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var TravelPartnerApi = require('index'); // See note below*.
* var xxxSvc = new TravelPartnerApi.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new TravelPartnerApi.Yyy(); // Construct a model instance.
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
* var xxxSvc = new TravelPartnerApi.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new TravelPartnerApi.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version v3
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The AccountLink model constructor.
     * @property {module:model/AccountLink}
     */
    AccountLink,

    /**
     * The AccountLinkTarget model constructor.
     * @property {module:model/AccountLinkTarget}
     */
    AccountLinkTarget,

    /**
     * The Brand model constructor.
     * @property {module:model/Brand}
     */
    Brand,

    /**
     * The CreateReconciliationReportResponse model constructor.
     * @property {module:model/CreateReconciliationReportResponse}
     */
    CreateReconciliationReportResponse,

    /**
     * The DataIssueDetail model constructor.
     * @property {module:model/DataIssueDetail}
     */
    DataIssueDetail,

    /**
     * The DisplayNameDisapprovalReason model constructor.
     * @property {module:model/DisplayNameDisapprovalReason}
     */
    DisplayNameDisapprovalReason,

    /**
     * The FreeBookingLinksResult model constructor.
     * @property {module:model/FreeBookingLinksResult}
     */
    FreeBookingLinksResult,

    /**
     * The HotelList model constructor.
     * @property {module:model/HotelList}
     */
    HotelList,

    /**
     * The HotelPricePerItinerary model constructor.
     * @property {module:model/HotelPricePerItinerary}
     */
    HotelPricePerItinerary,

    /**
     * The HotelView model constructor.
     * @property {module:model/HotelView}
     */
    HotelView,

    /**
     * The Icon model constructor.
     * @property {module:model/Icon}
     */
    Icon,

    /**
     * The Image model constructor.
     * @property {module:model/Image}
     */
    Image,

    /**
     * The Key model constructor.
     * @property {module:model/Key}
     */
    Key,

    /**
     * The LatLng model constructor.
     * @property {module:model/LatLng}
     */
    LatLng,

    /**
     * The ListAccountLinksResponse model constructor.
     * @property {module:model/ListAccountLinksResponse}
     */
    ListAccountLinksResponse,

    /**
     * The ListBrandsResponse model constructor.
     * @property {module:model/ListBrandsResponse}
     */
    ListBrandsResponse,

    /**
     * The ListHotelViewsResponse model constructor.
     * @property {module:model/ListHotelViewsResponse}
     */
    ListHotelViewsResponse,

    /**
     * The ListIconsResponse model constructor.
     * @property {module:model/ListIconsResponse}
     */
    ListIconsResponse,

    /**
     * The ListPriceAccuracyViewsResponse model constructor.
     * @property {module:model/ListPriceAccuracyViewsResponse}
     */
    ListPriceAccuracyViewsResponse,

    /**
     * The ListPriceCoverageViewsResponse model constructor.
     * @property {module:model/ListPriceCoverageViewsResponse}
     */
    ListPriceCoverageViewsResponse,

    /**
     * The ListReconciliationReportsResponse model constructor.
     * @property {module:model/ListReconciliationReportsResponse}
     */
    ListReconciliationReportsResponse,

    /**
     * The LocalizedText model constructor.
     * @property {module:model/LocalizedText}
     */
    LocalizedText,

    /**
     * The MissedParticipationCountDetails model constructor.
     * @property {module:model/MissedParticipationCountDetails}
     */
    MissedParticipationCountDetails,

    /**
     * The ModelDate model constructor.
     * @property {module:model/ModelDate}
     */
    ModelDate,

    /**
     * The NoPriceCountDetails model constructor.
     * @property {module:model/NoPriceCountDetails}
     */
    NoPriceCountDetails,

    /**
     * The ParsedListing model constructor.
     * @property {module:model/ParsedListing}
     */
    ParsedListing,

    /**
     * The ParticipationResult model constructor.
     * @property {module:model/ParticipationResult}
     */
    ParticipationResult,

    /**
     * The PriceAccuracyRow model constructor.
     * @property {module:model/PriceAccuracyRow}
     */
    PriceAccuracyRow,

    /**
     * The PriceAccuracyView model constructor.
     * @property {module:model/PriceAccuracyView}
     */
    PriceAccuracyView,

    /**
     * The PriceCoverageBucket model constructor.
     * @property {module:model/PriceCoverageBucket}
     */
    PriceCoverageBucket,

    /**
     * The PriceCoverageView model constructor.
     * @property {module:model/PriceCoverageView}
     */
    PriceCoverageView,

    /**
     * The PriceMissingCountDetails model constructor.
     * @property {module:model/PriceMissingCountDetails}
     */
    PriceMissingCountDetails,

    /**
     * The PriceProblemCountDetails model constructor.
     * @property {module:model/PriceProblemCountDetails}
     */
    PriceProblemCountDetails,

    /**
     * The PriceRecord model constructor.
     * @property {module:model/PriceRecord}
     */
    PriceRecord,

    /**
     * The PriceUnavailableCountDetails model constructor.
     * @property {module:model/PriceUnavailableCountDetails}
     */
    PriceUnavailableCountDetails,

    /**
     * The PriceView model constructor.
     * @property {module:model/PriceView}
     */
    PriceView,

    /**
     * The PropertyPerformanceResult model constructor.
     * @property {module:model/PropertyPerformanceResult}
     */
    PropertyPerformanceResult,

    /**
     * The QueryFreeBookingLinksReportResponse model constructor.
     * @property {module:model/QueryFreeBookingLinksReportResponse}
     */
    QueryFreeBookingLinksReportResponse,

    /**
     * The QueryParticipationReportResponse model constructor.
     * @property {module:model/QueryParticipationReportResponse}
     */
    QueryParticipationReportResponse,

    /**
     * The QueryPropertyPerformanceReportResponse model constructor.
     * @property {module:model/QueryPropertyPerformanceReportResponse}
     */
    QueryPropertyPerformanceReportResponse,

    /**
     * The Rating model constructor.
     * @property {module:model/Rating}
     */
    Rating,

    /**
     * The ReconciliationReport model constructor.
     * @property {module:model/ReconciliationReport}
     */
    ReconciliationReport,

    /**
     * The ReconciliationReportValidationIssue model constructor.
     * @property {module:model/ReconciliationReportValidationIssue}
     */
    ReconciliationReportValidationIssue,

    /**
     * The Review model constructor.
     * @property {module:model/Review}
     */
    Review,

    /**
     * The SetLiveOnGoogleRequest model constructor.
     * @property {module:model/SetLiveOnGoogleRequest}
     */
    SetLiveOnGoogleRequest,

    /**
     * The SetLiveOnGoogleResponse model constructor.
     * @property {module:model/SetLiveOnGoogleResponse}
     */
    SetLiveOnGoogleResponse,

    /**
     * The SummarizeHotelViewsResponse model constructor.
     * @property {module:model/SummarizeHotelViewsResponse}
     */
    SummarizeHotelViewsResponse,

    /**
     * The SummarizePriceAccuracyResponse model constructor.
     * @property {module:model/SummarizePriceAccuracyResponse}
     */
    SummarizePriceAccuracyResponse,

    /**
     * The ValidateReconciliationReportResponse model constructor.
     * @property {module:model/ValidateReconciliationReportResponse}
     */
    ValidateReconciliationReportResponse,

    /**
     * The VerifyListingsRequest model constructor.
     * @property {module:model/VerifyListingsRequest}
     */
    VerifyListingsRequest,

    /**
     * The VerifyListingsResponse model constructor.
     * @property {module:model/VerifyListingsResponse}
     */
    VerifyListingsResponse,

    /**
    * The AccountsApi service constructor.
    * @property {module:api/AccountsApi}
    */
    AccountsApi
};
