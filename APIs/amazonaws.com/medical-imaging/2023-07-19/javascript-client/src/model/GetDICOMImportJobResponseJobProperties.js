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
import DICOMImportJobProperties from './DICOMImportJobProperties';
import JobStatus from './JobStatus';

/**
 * The GetDICOMImportJobResponseJobProperties model module.
 * @module model/GetDICOMImportJobResponseJobProperties
 * @version 2023-07-19
 */
class GetDICOMImportJobResponseJobProperties {
    /**
     * Constructs a new <code>GetDICOMImportJobResponseJobProperties</code>.
     * @alias module:model/GetDICOMImportJobResponseJobProperties
     * @implements module:model/DICOMImportJobProperties
     * @param jobId {String} 
     * @param jobName {String} 
     * @param jobStatus {module:model/JobStatus} 
     * @param datastoreId {String} 
     * @param dataAccessRoleArn {String} 
     * @param inputS3Uri {String} 
     * @param outputS3Uri {String} 
     */
    constructor(jobId, jobName, jobStatus, datastoreId, dataAccessRoleArn, inputS3Uri, outputS3Uri) { 
        DICOMImportJobProperties.initialize(this, jobId, jobName, jobStatus, datastoreId, dataAccessRoleArn, inputS3Uri, outputS3Uri);
        GetDICOMImportJobResponseJobProperties.initialize(this, jobId, jobName, jobStatus, datastoreId, dataAccessRoleArn, inputS3Uri, outputS3Uri);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, jobId, jobName, jobStatus, datastoreId, dataAccessRoleArn, inputS3Uri, outputS3Uri) { 
        obj['jobId'] = jobId;
        obj['jobName'] = jobName;
        obj['jobStatus'] = jobStatus;
        obj['datastoreId'] = datastoreId;
        obj['dataAccessRoleArn'] = dataAccessRoleArn;
        obj['inputS3Uri'] = inputS3Uri;
        obj['outputS3Uri'] = outputS3Uri;
    }

    /**
     * Constructs a <code>GetDICOMImportJobResponseJobProperties</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetDICOMImportJobResponseJobProperties} obj Optional instance to populate.
     * @return {module:model/GetDICOMImportJobResponseJobProperties} The populated <code>GetDICOMImportJobResponseJobProperties</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetDICOMImportJobResponseJobProperties();
            DICOMImportJobProperties.constructFromObject(data, obj);

            if (data.hasOwnProperty('jobId')) {
                obj['jobId'] = ApiClient.convertToType(data['jobId'], 'String');
            }
            if (data.hasOwnProperty('jobName')) {
                obj['jobName'] = ApiClient.convertToType(data['jobName'], 'String');
            }
            if (data.hasOwnProperty('jobStatus')) {
                obj['jobStatus'] = ApiClient.convertToType(data['jobStatus'], JobStatus);
            }
            if (data.hasOwnProperty('datastoreId')) {
                obj['datastoreId'] = ApiClient.convertToType(data['datastoreId'], 'String');
            }
            if (data.hasOwnProperty('dataAccessRoleArn')) {
                obj['dataAccessRoleArn'] = ApiClient.convertToType(data['dataAccessRoleArn'], 'String');
            }
            if (data.hasOwnProperty('endedAt')) {
                obj['endedAt'] = ApiClient.convertToType(data['endedAt'], 'Date');
            }
            if (data.hasOwnProperty('submittedAt')) {
                obj['submittedAt'] = ApiClient.convertToType(data['submittedAt'], 'Date');
            }
            if (data.hasOwnProperty('inputS3Uri')) {
                obj['inputS3Uri'] = ApiClient.convertToType(data['inputS3Uri'], 'String');
            }
            if (data.hasOwnProperty('outputS3Uri')) {
                obj['outputS3Uri'] = ApiClient.convertToType(data['outputS3Uri'], 'String');
            }
            if (data.hasOwnProperty('message')) {
                obj['message'] = ApiClient.convertToType(data['message'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GetDICOMImportJobResponseJobProperties</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetDICOMImportJobResponseJobProperties</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of GetDICOMImportJobResponseJobProperties.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `jobId`
        if (data['jobId']) { // data not null
          String.validateJSON(data['jobId']);
        }
        // validate the optional field `jobName`
        if (data['jobName']) { // data not null
          String.validateJSON(data['jobName']);
        }
        // validate the optional field `jobStatus`
        if (data['jobStatus']) { // data not null
          JobStatus.validateJSON(data['jobStatus']);
        }
        // validate the optional field `datastoreId`
        if (data['datastoreId']) { // data not null
          String.validateJSON(data['datastoreId']);
        }
        // validate the optional field `dataAccessRoleArn`
        if (data['dataAccessRoleArn']) { // data not null
          String.validateJSON(data['dataAccessRoleArn']);
        }
        // validate the optional field `endedAt`
        if (data['endedAt']) { // data not null
          Date.validateJSON(data['endedAt']);
        }
        // validate the optional field `submittedAt`
        if (data['submittedAt']) { // data not null
          Date.validateJSON(data['submittedAt']);
        }
        // validate the optional field `inputS3Uri`
        if (data['inputS3Uri']) { // data not null
          String.validateJSON(data['inputS3Uri']);
        }
        // validate the optional field `outputS3Uri`
        if (data['outputS3Uri']) { // data not null
          String.validateJSON(data['outputS3Uri']);
        }
        // validate the optional field `message`
        if (data['message']) { // data not null
          String.validateJSON(data['message']);
        }

        return true;
    }


}

GetDICOMImportJobResponseJobProperties.RequiredProperties = ["jobId", "jobName", "jobStatus", "datastoreId", "dataAccessRoleArn", "inputS3Uri", "outputS3Uri"];

/**
 * @member {String} jobId
 */
GetDICOMImportJobResponseJobProperties.prototype['jobId'] = undefined;

/**
 * @member {String} jobName
 */
GetDICOMImportJobResponseJobProperties.prototype['jobName'] = undefined;

/**
 * @member {module:model/JobStatus} jobStatus
 */
GetDICOMImportJobResponseJobProperties.prototype['jobStatus'] = undefined;

/**
 * @member {String} datastoreId
 */
GetDICOMImportJobResponseJobProperties.prototype['datastoreId'] = undefined;

/**
 * @member {String} dataAccessRoleArn
 */
GetDICOMImportJobResponseJobProperties.prototype['dataAccessRoleArn'] = undefined;

/**
 * @member {Date} endedAt
 */
GetDICOMImportJobResponseJobProperties.prototype['endedAt'] = undefined;

/**
 * @member {Date} submittedAt
 */
GetDICOMImportJobResponseJobProperties.prototype['submittedAt'] = undefined;

/**
 * @member {String} inputS3Uri
 */
GetDICOMImportJobResponseJobProperties.prototype['inputS3Uri'] = undefined;

/**
 * @member {String} outputS3Uri
 */
GetDICOMImportJobResponseJobProperties.prototype['outputS3Uri'] = undefined;

/**
 * @member {String} message
 */
GetDICOMImportJobResponseJobProperties.prototype['message'] = undefined;


// Implement DICOMImportJobProperties interface:
/**
 * @member {String} jobId
 */
DICOMImportJobProperties.prototype['jobId'] = undefined;
/**
 * @member {String} jobName
 */
DICOMImportJobProperties.prototype['jobName'] = undefined;
/**
 * @member {module:model/JobStatus} jobStatus
 */
DICOMImportJobProperties.prototype['jobStatus'] = undefined;
/**
 * @member {String} datastoreId
 */
DICOMImportJobProperties.prototype['datastoreId'] = undefined;
/**
 * @member {String} dataAccessRoleArn
 */
DICOMImportJobProperties.prototype['dataAccessRoleArn'] = undefined;
/**
 * @member {Date} endedAt
 */
DICOMImportJobProperties.prototype['endedAt'] = undefined;
/**
 * @member {Date} submittedAt
 */
DICOMImportJobProperties.prototype['submittedAt'] = undefined;
/**
 * @member {String} inputS3Uri
 */
DICOMImportJobProperties.prototype['inputS3Uri'] = undefined;
/**
 * @member {String} outputS3Uri
 */
DICOMImportJobProperties.prototype['outputS3Uri'] = undefined;
/**
 * @member {String} message
 */
DICOMImportJobProperties.prototype['message'] = undefined;




export default GetDICOMImportJobResponseJobProperties;

