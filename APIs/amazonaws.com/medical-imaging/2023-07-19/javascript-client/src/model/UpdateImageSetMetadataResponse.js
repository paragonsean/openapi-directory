/**
 * AWS Health Imaging
 * <p>This is the <i>AWS HealthImaging API Reference</i>. AWS HealthImaging is an AWS service for storing, accessing, and analyzing medical images. For an introduction to the service, see the <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide\"> <i>AWS HealthImaging Developer Guide</i> </a>.</p> <note> <p>We recommend using one of the AWS Software Development Kits (SDKs) for your programming language, as they take care of request authentication, serialization, and connection management. For more information, see <a href=\"http://aws.amazon.com/developer/tools\">Tools to build on AWS</a>.</p> <p>For information about using AWS HealthImaging API actions in one of the language-specific AWS SDKs, refer to the <i>See Also</i> link at the end of each section that describes an API action or data type.</p> </note> <p>The following sections list AWS HealthImaging API actions categorized according to functionality. Links are provided to actions within this Reference, along with links back to corresponding sections in the <i>AWS HealthImaging Developer Guide</i> so you can view console procedures and CLI/SDK code examples.</p> <p class=\"title\"> <b>Data store actions</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_CreateDatastore.html\">CreateDatastore</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/create-data-store.html\">Creating a data store</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_GetDatastore.html\">GetDatastore</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/get-data-store.html\">Getting data store properties</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_ListDatastores.html\">ListDatastores</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/list-data-stores.html\">Listing data stores</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_DeleteDatastore.html\">DeleteDatastore</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/delete-data-store.html\">Deleting a data store</a>.</p> </li> </ul> <p class=\"title\"> <b>Import job actions</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_StartDICOMImportJob.html\">StartDICOMImportJob</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/start-dicom-import-job.html\">Starting an import job</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_GetDICOMImportJob.html\">GetDICOMImportJob</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/get-dicom-import-job.html\">Getting import job properties</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_ListDICOMImportJobs.html\">ListDICOMImportJobs</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/list-dicom-import-jobs.html\">Listing import jobs</a>.</p> </li> </ul> <p class=\"title\"> <b>Image set access actions</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_SearchImageSets.html\">SearchImageSets</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/search-image-sets.html\">Searching image sets</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_GetImageSet.html\">GetImageSet</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/get-image-set-properties.html\">Getting image set properties</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_GetImageSetMetadata.html\">GetImageSetMetadata</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/get-image-set-metadata.html\">Getting image set metadata</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_GetImageFrame.html\">GetImageFrame</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/get-image-frame.html\">Getting image set pixel data</a>.</p> </li> </ul> <p class=\"title\"> <b>Image set modification actions</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_ListImageSetVersions.html\">ListImageSetVersions</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/list-image-set-versions.html\">Listing image set versions</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_UpdateImageSetMetadata.html\">UpdateImageSetMetadata</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/update-image-set-metadata.html\">Updating image set metadata</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_CopyImageSet.html\">CopyImageSet</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/copy-image-set.html\">Copying an image set</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_DeleteImageSet.html\">DeleteImageSet</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/delete-image-set.html\">Deleting an image set</a>.</p> </li> </ul> <p class=\"title\"> <b>Tagging actions</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_TagResource.html\">TagResource</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/tag-list-untag-data-store.html\">Tagging a data store</a> and <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/tag-list-untag-image-set.html\">Tagging an image set</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_ListTagsForResource.html\">ListTagsForResource</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/tag-list-untag-data-store.html\">Tagging a data store</a> and <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/tag-list-untag-image-set.html\">Tagging an image set</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_UntagResource.html\">UntagResource</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/tag-list-untag-data-store.html\">Tagging a data store</a> and <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/tag-list-untag-image-set.html\">Tagging an image set</a>.</p> </li> </ul>
 *
 * The version of the OpenAPI document: 2023-07-19
 * Contact: mike.ralphson@gmail.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import ImageSetState from './ImageSetState';
import ImageSetWorkflowStatus from './ImageSetWorkflowStatus';

/**
 * The UpdateImageSetMetadataResponse model module.
 * @module model/UpdateImageSetMetadataResponse
 * @version 2023-07-19
 */
class UpdateImageSetMetadataResponse {
    /**
     * Constructs a new <code>UpdateImageSetMetadataResponse</code>.
     * @alias module:model/UpdateImageSetMetadataResponse
     * @param datastoreId {String} 
     * @param imageSetId {String} 
     * @param latestVersionId {String} 
     * @param imageSetState {module:model/ImageSetState} 
     */
    constructor(datastoreId, imageSetId, latestVersionId, imageSetState) { 
        
        UpdateImageSetMetadataResponse.initialize(this, datastoreId, imageSetId, latestVersionId, imageSetState);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, datastoreId, imageSetId, latestVersionId, imageSetState) { 
        obj['datastoreId'] = datastoreId;
        obj['imageSetId'] = imageSetId;
        obj['latestVersionId'] = latestVersionId;
        obj['imageSetState'] = imageSetState;
    }

    /**
     * Constructs a <code>UpdateImageSetMetadataResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UpdateImageSetMetadataResponse} obj Optional instance to populate.
     * @return {module:model/UpdateImageSetMetadataResponse} The populated <code>UpdateImageSetMetadataResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UpdateImageSetMetadataResponse();

            if (data.hasOwnProperty('datastoreId')) {
                obj['datastoreId'] = ApiClient.convertToType(data['datastoreId'], 'String');
            }
            if (data.hasOwnProperty('imageSetId')) {
                obj['imageSetId'] = ApiClient.convertToType(data['imageSetId'], 'String');
            }
            if (data.hasOwnProperty('latestVersionId')) {
                obj['latestVersionId'] = ApiClient.convertToType(data['latestVersionId'], 'String');
            }
            if (data.hasOwnProperty('imageSetState')) {
                obj['imageSetState'] = ApiClient.convertToType(data['imageSetState'], ImageSetState);
            }
            if (data.hasOwnProperty('imageSetWorkflowStatus')) {
                obj['imageSetWorkflowStatus'] = ApiClient.convertToType(data['imageSetWorkflowStatus'], ImageSetWorkflowStatus);
            }
            if (data.hasOwnProperty('createdAt')) {
                obj['createdAt'] = ApiClient.convertToType(data['createdAt'], 'Date');
            }
            if (data.hasOwnProperty('updatedAt')) {
                obj['updatedAt'] = ApiClient.convertToType(data['updatedAt'], 'Date');
            }
            if (data.hasOwnProperty('message')) {
                obj['message'] = ApiClient.convertToType(data['message'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UpdateImageSetMetadataResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UpdateImageSetMetadataResponse</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of UpdateImageSetMetadataResponse.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `datastoreId`
        if (data['datastoreId']) { // data not null
          String.validateJSON(data['datastoreId']);
        }
        // validate the optional field `imageSetId`
        if (data['imageSetId']) { // data not null
          String.validateJSON(data['imageSetId']);
        }
        // validate the optional field `latestVersionId`
        if (data['latestVersionId']) { // data not null
          String.validateJSON(data['latestVersionId']);
        }
        // validate the optional field `imageSetState`
        if (data['imageSetState']) { // data not null
          ImageSetState.validateJSON(data['imageSetState']);
        }
        // validate the optional field `imageSetWorkflowStatus`
        if (data['imageSetWorkflowStatus']) { // data not null
          ImageSetWorkflowStatus.validateJSON(data['imageSetWorkflowStatus']);
        }
        // validate the optional field `createdAt`
        if (data['createdAt']) { // data not null
          Date.validateJSON(data['createdAt']);
        }
        // validate the optional field `updatedAt`
        if (data['updatedAt']) { // data not null
          Date.validateJSON(data['updatedAt']);
        }
        // validate the optional field `message`
        if (data['message']) { // data not null
          String.validateJSON(data['message']);
        }

        return true;
    }


}

UpdateImageSetMetadataResponse.RequiredProperties = ["datastoreId", "imageSetId", "latestVersionId", "imageSetState"];

/**
 * @member {String} datastoreId
 */
UpdateImageSetMetadataResponse.prototype['datastoreId'] = undefined;

/**
 * @member {String} imageSetId
 */
UpdateImageSetMetadataResponse.prototype['imageSetId'] = undefined;

/**
 * @member {String} latestVersionId
 */
UpdateImageSetMetadataResponse.prototype['latestVersionId'] = undefined;

/**
 * @member {module:model/ImageSetState} imageSetState
 */
UpdateImageSetMetadataResponse.prototype['imageSetState'] = undefined;

/**
 * @member {module:model/ImageSetWorkflowStatus} imageSetWorkflowStatus
 */
UpdateImageSetMetadataResponse.prototype['imageSetWorkflowStatus'] = undefined;

/**
 * @member {Date} createdAt
 */
UpdateImageSetMetadataResponse.prototype['createdAt'] = undefined;

/**
 * @member {Date} updatedAt
 */
UpdateImageSetMetadataResponse.prototype['updatedAt'] = undefined;

/**
 * @member {String} message
 */
UpdateImageSetMetadataResponse.prototype['message'] = undefined;






export default UpdateImageSetMetadataResponse;

