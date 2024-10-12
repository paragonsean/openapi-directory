/**
 * Climate FieldView Platform APIs
 * **Last Modified**: Wed Jan  4 12:47:29 UTC 2023   All endpoints are only accessible via HTTPS.  * All API endpoints are located at `https://platform.climate.com` (e.g. `https://platform.climate.com/v4/fields`).  * The authorization token endpoint is located at `https://api.climate.com/api/oauth/token`.  ## Troubleshooting  `X-Http-Request-Id` response header will be returned on every call, successful or not. If you experience an issue with our api and need to contact technical support, please supply the value of the `X-Http-Request-Id` header along with an approximate time of when the request was made.  ## Request Limits  When you’re onboarded to Climate’s API platform, your `x-api-key` is assigned a custom usage plan. Usage plans are unique to each partner and have the following key attributes:   1. Throttling information     * burstLimit: Maximum rate limit over a period ranging from 1 second to a few seconds     * rateLimit: A steady-state rate limit  2. Quota information     * Limit: The maximum number of requests that can be made in a given month  When the request rate threshold is exceeded, a `429` response code is returned. Optionally, the [`Retry-After`](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.37) header may be returned:   Following are examples of rate limit errors:  1. Rate limit exceeded:  <br>HTTP/1.1 429  <br>Content-Type: application/json <br>Content-Length: 32     {\"message\":\"Too Many Requests\"}  2. Quota exhausted: <br>HTTP/1.1 429  <br>Content-Type: application/json <br>Content-Length: 29      {\"message\":\"Limit Exceeded\"}  ## Pagination  Pagination is performed via headers. Any request which returns a `\"results\"` array may be paginated. The following figure shows how query results are laid out with X-Limit=4 and no filter applied.  <img style=\"width:70%;height:auto;\" src=\"https://s3-us-west-2.amazonaws.com/climate-com/images/svg_upload_tests/paging.png\">  * If there are no results, a response code of `304` will be returned.  * If the response is the last set of results, a response code of `200` or `206` will be returned.  * If there are more results, a response code of `206` will be returned.  * If `X-Next-Token` is provided in the request headers but the token has expired, a response code of `409` will be returned. This is only applicable for some endpoints; see specific endpoint documentation below.  #### X-Limit  The page size can be controlled with the `X-Limit` header. Valid values are `1-100` and defaults to `100`.  #### X-Next-Token  If the results are paginated, a response header of `X-Next-Token` will be returned. Use the associated value in the subsequent request (via the `X-Next-Token` request header) to retrieve the next page. The following sequence diagram shows how to use `X-Next-Token` to fetch all the records.  <img src=\"https://s3-us-west-2.amazonaws.com/climate-com/images/svg_upload_tests/x-next-token.svg\">   ## Chunked Uploads  Uploads larger than `5MiB` (`5242880 bytes`) must be done in `5MiB` chunks (with the exception of the final chunk). Each chunk request MUST contain a `Content-Range` header specifying the portion of the upload, and a `Content-Type` header specifying binary content type (`application/octet-stream`). Range uploads must be contiguous. The maximum upload size is capped at `500MiB` (`524288000 bytes`).  ## Chunked Downloads  Downloads larger than `5MiB` (`5242880 bytes`) must be done in `1-5MiB` chunks (with the exception of the final chunk, which may be less than `1MiB`). Each chunk request MUST contain a `Range` header specifying the requested portion of the download, and an `Accept` header specifying binary and json content types  (`application/octet-stream,application/json`) or all content types (`*_/_*`).  ## Drivers  If you need drivers to process agronomic data, download the ADAPT plugin below. We only support the plugin in the Windows environment, minimum is Windows 7 SP1.  For asPlanted, asHarvested and asApplied data: * [ADAPT Plugin](https://dev.fieldview.com/drivers/ClimateADAPTPlugin_latest.exe) <br>Release notes can be found [here](https://dev.fieldview.com/drivers/adapt-release-notes.txt). <br>Download and use of the ADAPT plugin means that you agree to the EULA for use of the ADAPT plugin.  <br>Please review the [EULA](https://dev.fieldview.com/EULA/ADAPT%20Plugin%20EULA-06-19.pdf) (last updated on June 6th, 2019) before download and use of the ADAPT plugin. <br>For more information, please refer to:   * [ADAPT Resources](https://adaptframework.org/)   * [ADAPT Overview](https://aggateway.atlassian.net/wiki/spaces/ADM/overview)   * [ADAPT FAQ](https://aggateway.atlassian.net/wiki/spaces/ADM/pages/165942474/ADAPT+Frequently-Asked+Questions+FAQ)   * [ADAPT Videos](https://adaptframework.org/adapt-videos/)  ## Sample Test Data  Sample agronomic data: * [asPlanted and asHarvested data](https://dev.fieldview.com/sample-agronomic-data/Planting_Harvesting_data_04_18_2018_21_46_18.zip) * [asApplied data set 1](https://dev.fieldview.com/sample-agronomic-data/as-applied-data1.zip) * [asApplied data set 2](https://dev.fieldview.com/sample-agronomic-data/as-applied-data2.zip) <br>To upload the sample data to your account, please follow the instructions in this [link](https://support.climate.com/kt#/kA02A000000AaxzSAC/en_US).  Sample soil data: * [Sample soil data](https://dev.fieldview.com/sample-soil-data/soil-sample.xml) --- 
 *
 * The version of the OpenAPI document: 4.0.11
 * Contact: developer@climate.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import ApplicationActivities from './model/ApplicationActivities';
import ApplicationActivityContents from './model/ApplicationActivityContents';
import ApplicationActivitySummary from './model/ApplicationActivitySummary';
import Area from './model/Area';
import Boundaries from './model/Boundaries';
import BoundariesQuery from './model/BoundariesQuery';
import Boundary from './model/Boundary';
import BoundaryProperties from './model/BoundaryProperties';
import BoundaryUpload from './model/BoundaryUpload';
import CreatedExport from './model/CreatedExport';
import Error from './model/Error';
import ErrorError from './model/ErrorError';
import Export from './model/Export';
import ExportContents from './model/ExportContents';
import ExportStatus from './model/ExportStatus';
import FarmOrganization from './model/FarmOrganization';
import Field from './model/Field';
import Fields from './model/Fields';
import Geometry from './model/Geometry';
import HarvestActivities from './model/HarvestActivities';
import HarvestActivityContents from './model/HarvestActivityContents';
import HarvestActivitySummary from './model/HarvestActivitySummary';
import Operation from './model/Operation';
import Operations from './model/Operations';
import Parent from './model/Parent';
import PlantingActivities from './model/PlantingActivities';
import PlantingActivityContents from './model/PlantingActivityContents';
import PlantingActivitySummary from './model/PlantingActivitySummary';
import Point from './model/Point';
import ResourceOwner from './model/ResourceOwner';
import ScoutingObservation from './model/ScoutingObservation';
import ScoutingObservationAttachment from './model/ScoutingObservationAttachment';
import ScoutingObservationAttachmentContents from './model/ScoutingObservationAttachmentContents';
import ScoutingObservationAttachments from './model/ScoutingObservationAttachments';
import ScoutingObservationSummary from './model/ScoutingObservationSummary';
import ScoutingObservations from './model/ScoutingObservations';
import ScoutingTag from './model/ScoutingTag';
import Upload from './model/Upload';
import UploadStatus from './model/UploadStatus';
import UploadStatusQuery from './model/UploadStatusQuery';
import UploadStatuses from './model/UploadStatuses';
import UploadedBoundaryId from './model/UploadedBoundaryId';
import BoundariesApi from './api/BoundariesApi';
import ExportsApi from './api/ExportsApi';
import FarmOrganizationsApi from './api/FarmOrganizationsApi';
import FieldsApi from './api/FieldsApi';
import LayersApi from './api/LayersApi';
import OperationsApi from './api/OperationsApi';
import ResourceOwnersApi from './api/ResourceOwnersApi';
import UploadsApi from './api/UploadsApi';


/**
* **Last Modified**: Wed Jan  4 12:47:29 UTC 2023   All endpoints are only accessible via HTTPS.  * All API endpoints are located at &#x60;https://platform.climate.com&#x60; (e.g. &#x60;https://platform.climate.com/v4/fields&#x60;).  * The authorization token endpoint is located at &#x60;https://api.climate.com/api/oauth/token&#x60;.  ## Troubleshooting  &#x60;X-Http-Request-Id&#x60; response header will be returned on every call, successful or not. If you experience an issue with our api and need to contact technical support, please supply the value of the &#x60;X-Http-Request-Id&#x60; header along with an approximate time of when the request was made.  ## Request Limits  When you’re onboarded to Climate’s API platform, your &#x60;x-api-key&#x60; is assigned a custom usage plan. Usage plans are unique to each partner and have the following key attributes:   1. Throttling information     * burstLimit: Maximum rate limit over a period ranging from 1 second to a few seconds     * rateLimit: A steady-state rate limit  2. Quota information     * Limit: The maximum number of requests that can be made in a given month  When the request rate threshold is exceeded, a &#x60;429&#x60; response code is returned. Optionally, the [&#x60;Retry-After&#x60;](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.37) header may be returned:   Following are examples of rate limit errors:  1. Rate limit exceeded:  &lt;br&gt;HTTP/1.1 429  &lt;br&gt;Content-Type: application/json &lt;br&gt;Content-Length: 32     {\&quot;message\&quot;:\&quot;Too Many Requests\&quot;}  2. Quota exhausted: &lt;br&gt;HTTP/1.1 429  &lt;br&gt;Content-Type: application/json &lt;br&gt;Content-Length: 29      {\&quot;message\&quot;:\&quot;Limit Exceeded\&quot;}  ## Pagination  Pagination is performed via headers. Any request which returns a &#x60;\&quot;results\&quot;&#x60; array may be paginated. The following figure shows how query results are laid out with X-Limit&#x3D;4 and no filter applied.  &lt;img style&#x3D;\&quot;width:70%;height:auto;\&quot; src&#x3D;\&quot;https://s3-us-west-2.amazonaws.com/climate-com/images/svg_upload_tests/paging.png\&quot;&gt;  * If there are no results, a response code of &#x60;304&#x60; will be returned.  * If the response is the last set of results, a response code of &#x60;200&#x60; or &#x60;206&#x60; will be returned.  * If there are more results, a response code of &#x60;206&#x60; will be returned.  * If &#x60;X-Next-Token&#x60; is provided in the request headers but the token has expired, a response code of &#x60;409&#x60; will be returned. This is only applicable for some endpoints; see specific endpoint documentation below.  #### X-Limit  The page size can be controlled with the &#x60;X-Limit&#x60; header. Valid values are &#x60;1-100&#x60; and defaults to &#x60;100&#x60;.  #### X-Next-Token  If the results are paginated, a response header of &#x60;X-Next-Token&#x60; will be returned. Use the associated value in the subsequent request (via the &#x60;X-Next-Token&#x60; request header) to retrieve the next page. The following sequence diagram shows how to use &#x60;X-Next-Token&#x60; to fetch all the records.  &lt;img src&#x3D;\&quot;https://s3-us-west-2.amazonaws.com/climate-com/images/svg_upload_tests/x-next-token.svg\&quot;&gt;   ## Chunked Uploads  Uploads larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) must be done in &#x60;5MiB&#x60; chunks (with the exception of the final chunk). Each chunk request MUST contain a &#x60;Content-Range&#x60; header specifying the portion of the upload, and a &#x60;Content-Type&#x60; header specifying binary content type (&#x60;application/octet-stream&#x60;). Range uploads must be contiguous. The maximum upload size is capped at &#x60;500MiB&#x60; (&#x60;524288000 bytes&#x60;).  ## Chunked Downloads  Downloads larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) must be done in &#x60;1-5MiB&#x60; chunks (with the exception of the final chunk, which may be less than &#x60;1MiB&#x60;). Each chunk request MUST contain a &#x60;Range&#x60; header specifying the requested portion of the download, and an &#x60;Accept&#x60; header specifying binary and json content types  (&#x60;application/octet-stream,application/json&#x60;) or all content types (&#x60;*_/_*&#x60;).  ## Drivers  If you need drivers to process agronomic data, download the ADAPT plugin below. We only support the plugin in the Windows environment, minimum is Windows 7 SP1.  For asPlanted, asHarvested and asApplied data: * [ADAPT Plugin](https://dev.fieldview.com/drivers/ClimateADAPTPlugin_latest.exe) &lt;br&gt;Release notes can be found [here](https://dev.fieldview.com/drivers/adapt-release-notes.txt). &lt;br&gt;Download and use of the ADAPT plugin means that you agree to the EULA for use of the ADAPT plugin.  &lt;br&gt;Please review the [EULA](https://dev.fieldview.com/EULA/ADAPT%20Plugin%20EULA-06-19.pdf) (last updated on June 6th, 2019) before download and use of the ADAPT plugin. &lt;br&gt;For more information, please refer to:   * [ADAPT Resources](https://adaptframework.org/)   * [ADAPT Overview](https://aggateway.atlassian.net/wiki/spaces/ADM/overview)   * [ADAPT FAQ](https://aggateway.atlassian.net/wiki/spaces/ADM/pages/165942474/ADAPT+Frequently-Asked+Questions+FAQ)   * [ADAPT Videos](https://adaptframework.org/adapt-videos/)  ## Sample Test Data  Sample agronomic data: * [asPlanted and asHarvested data](https://dev.fieldview.com/sample-agronomic-data/Planting_Harvesting_data_04_18_2018_21_46_18.zip) * [asApplied data set 1](https://dev.fieldview.com/sample-agronomic-data/as-applied-data1.zip) * [asApplied data set 2](https://dev.fieldview.com/sample-agronomic-data/as-applied-data2.zip) &lt;br&gt;To upload the sample data to your account, please follow the instructions in this [link](https://support.climate.com/kt#/kA02A000000AaxzSAC/en_US).  Sample soil data: * [Sample soil data](https://dev.fieldview.com/sample-soil-data/soil-sample.xml) --- .<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var ClimateFieldViewPlatformApis = require('index'); // See note below*.
* var xxxSvc = new ClimateFieldViewPlatformApis.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new ClimateFieldViewPlatformApis.Yyy(); // Construct a model instance.
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
* var xxxSvc = new ClimateFieldViewPlatformApis.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new ClimateFieldViewPlatformApis.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 4.0.11
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The ApplicationActivities model constructor.
     * @property {module:model/ApplicationActivities}
     */
    ApplicationActivities,

    /**
     * The ApplicationActivityContents model constructor.
     * @property {module:model/ApplicationActivityContents}
     */
    ApplicationActivityContents,

    /**
     * The ApplicationActivitySummary model constructor.
     * @property {module:model/ApplicationActivitySummary}
     */
    ApplicationActivitySummary,

    /**
     * The Area model constructor.
     * @property {module:model/Area}
     */
    Area,

    /**
     * The Boundaries model constructor.
     * @property {module:model/Boundaries}
     */
    Boundaries,

    /**
     * The BoundariesQuery model constructor.
     * @property {module:model/BoundariesQuery}
     */
    BoundariesQuery,

    /**
     * The Boundary model constructor.
     * @property {module:model/Boundary}
     */
    Boundary,

    /**
     * The BoundaryProperties model constructor.
     * @property {module:model/BoundaryProperties}
     */
    BoundaryProperties,

    /**
     * The BoundaryUpload model constructor.
     * @property {module:model/BoundaryUpload}
     */
    BoundaryUpload,

    /**
     * The CreatedExport model constructor.
     * @property {module:model/CreatedExport}
     */
    CreatedExport,

    /**
     * The Error model constructor.
     * @property {module:model/Error}
     */
    Error,

    /**
     * The ErrorError model constructor.
     * @property {module:model/ErrorError}
     */
    ErrorError,

    /**
     * The Export model constructor.
     * @property {module:model/Export}
     */
    Export,

    /**
     * The ExportContents model constructor.
     * @property {module:model/ExportContents}
     */
    ExportContents,

    /**
     * The ExportStatus model constructor.
     * @property {module:model/ExportStatus}
     */
    ExportStatus,

    /**
     * The FarmOrganization model constructor.
     * @property {module:model/FarmOrganization}
     */
    FarmOrganization,

    /**
     * The Field model constructor.
     * @property {module:model/Field}
     */
    Field,

    /**
     * The Fields model constructor.
     * @property {module:model/Fields}
     */
    Fields,

    /**
     * The Geometry model constructor.
     * @property {module:model/Geometry}
     */
    Geometry,

    /**
     * The HarvestActivities model constructor.
     * @property {module:model/HarvestActivities}
     */
    HarvestActivities,

    /**
     * The HarvestActivityContents model constructor.
     * @property {module:model/HarvestActivityContents}
     */
    HarvestActivityContents,

    /**
     * The HarvestActivitySummary model constructor.
     * @property {module:model/HarvestActivitySummary}
     */
    HarvestActivitySummary,

    /**
     * The Operation model constructor.
     * @property {module:model/Operation}
     */
    Operation,

    /**
     * The Operations model constructor.
     * @property {module:model/Operations}
     */
    Operations,

    /**
     * The Parent model constructor.
     * @property {module:model/Parent}
     */
    Parent,

    /**
     * The PlantingActivities model constructor.
     * @property {module:model/PlantingActivities}
     */
    PlantingActivities,

    /**
     * The PlantingActivityContents model constructor.
     * @property {module:model/PlantingActivityContents}
     */
    PlantingActivityContents,

    /**
     * The PlantingActivitySummary model constructor.
     * @property {module:model/PlantingActivitySummary}
     */
    PlantingActivitySummary,

    /**
     * The Point model constructor.
     * @property {module:model/Point}
     */
    Point,

    /**
     * The ResourceOwner model constructor.
     * @property {module:model/ResourceOwner}
     */
    ResourceOwner,

    /**
     * The ScoutingObservation model constructor.
     * @property {module:model/ScoutingObservation}
     */
    ScoutingObservation,

    /**
     * The ScoutingObservationAttachment model constructor.
     * @property {module:model/ScoutingObservationAttachment}
     */
    ScoutingObservationAttachment,

    /**
     * The ScoutingObservationAttachmentContents model constructor.
     * @property {module:model/ScoutingObservationAttachmentContents}
     */
    ScoutingObservationAttachmentContents,

    /**
     * The ScoutingObservationAttachments model constructor.
     * @property {module:model/ScoutingObservationAttachments}
     */
    ScoutingObservationAttachments,

    /**
     * The ScoutingObservationSummary model constructor.
     * @property {module:model/ScoutingObservationSummary}
     */
    ScoutingObservationSummary,

    /**
     * The ScoutingObservations model constructor.
     * @property {module:model/ScoutingObservations}
     */
    ScoutingObservations,

    /**
     * The ScoutingTag model constructor.
     * @property {module:model/ScoutingTag}
     */
    ScoutingTag,

    /**
     * The Upload model constructor.
     * @property {module:model/Upload}
     */
    Upload,

    /**
     * The UploadStatus model constructor.
     * @property {module:model/UploadStatus}
     */
    UploadStatus,

    /**
     * The UploadStatusQuery model constructor.
     * @property {module:model/UploadStatusQuery}
     */
    UploadStatusQuery,

    /**
     * The UploadStatuses model constructor.
     * @property {module:model/UploadStatuses}
     */
    UploadStatuses,

    /**
     * The UploadedBoundaryId model constructor.
     * @property {module:model/UploadedBoundaryId}
     */
    UploadedBoundaryId,

    /**
    * The BoundariesApi service constructor.
    * @property {module:api/BoundariesApi}
    */
    BoundariesApi,

    /**
    * The ExportsApi service constructor.
    * @property {module:api/ExportsApi}
    */
    ExportsApi,

    /**
    * The FarmOrganizationsApi service constructor.
    * @property {module:api/FarmOrganizationsApi}
    */
    FarmOrganizationsApi,

    /**
    * The FieldsApi service constructor.
    * @property {module:api/FieldsApi}
    */
    FieldsApi,

    /**
    * The LayersApi service constructor.
    * @property {module:api/LayersApi}
    */
    LayersApi,

    /**
    * The OperationsApi service constructor.
    * @property {module:api/OperationsApi}
    */
    OperationsApi,

    /**
    * The ResourceOwnersApi service constructor.
    * @property {module:api/ResourceOwnersApi}
    */
    ResourceOwnersApi,

    /**
    * The UploadsApi service constructor.
    * @property {module:api/UploadsApi}
    */
    UploadsApi
};
