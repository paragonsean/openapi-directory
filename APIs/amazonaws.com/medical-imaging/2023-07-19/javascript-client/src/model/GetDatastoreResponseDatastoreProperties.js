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
import DatastoreProperties from './DatastoreProperties';
import DatastoreStatus from './DatastoreStatus';

/**
 * The GetDatastoreResponseDatastoreProperties model module.
 * @module model/GetDatastoreResponseDatastoreProperties
 * @version 2023-07-19
 */
class GetDatastoreResponseDatastoreProperties {
    /**
     * Constructs a new <code>GetDatastoreResponseDatastoreProperties</code>.
     * @alias module:model/GetDatastoreResponseDatastoreProperties
     * @implements module:model/DatastoreProperties
     * @param datastoreId {String} 
     * @param datastoreName {String} 
     * @param datastoreStatus {module:model/DatastoreStatus} 
     */
    constructor(datastoreId, datastoreName, datastoreStatus) { 
        DatastoreProperties.initialize(this, datastoreId, datastoreName, datastoreStatus);
        GetDatastoreResponseDatastoreProperties.initialize(this, datastoreId, datastoreName, datastoreStatus);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, datastoreId, datastoreName, datastoreStatus) { 
        obj['datastoreId'] = datastoreId;
        obj['datastoreName'] = datastoreName;
        obj['datastoreStatus'] = datastoreStatus;
    }

    /**
     * Constructs a <code>GetDatastoreResponseDatastoreProperties</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetDatastoreResponseDatastoreProperties} obj Optional instance to populate.
     * @return {module:model/GetDatastoreResponseDatastoreProperties} The populated <code>GetDatastoreResponseDatastoreProperties</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetDatastoreResponseDatastoreProperties();
            DatastoreProperties.constructFromObject(data, obj);

            if (data.hasOwnProperty('datastoreId')) {
                obj['datastoreId'] = ApiClient.convertToType(data['datastoreId'], 'String');
            }
            if (data.hasOwnProperty('datastoreName')) {
                obj['datastoreName'] = ApiClient.convertToType(data['datastoreName'], 'String');
            }
            if (data.hasOwnProperty('datastoreStatus')) {
                obj['datastoreStatus'] = ApiClient.convertToType(data['datastoreStatus'], DatastoreStatus);
            }
            if (data.hasOwnProperty('kmsKeyArn')) {
                obj['kmsKeyArn'] = ApiClient.convertToType(data['kmsKeyArn'], 'String');
            }
            if (data.hasOwnProperty('datastoreArn')) {
                obj['datastoreArn'] = ApiClient.convertToType(data['datastoreArn'], 'String');
            }
            if (data.hasOwnProperty('createdAt')) {
                obj['createdAt'] = ApiClient.convertToType(data['createdAt'], 'Date');
            }
            if (data.hasOwnProperty('updatedAt')) {
                obj['updatedAt'] = ApiClient.convertToType(data['updatedAt'], 'Date');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GetDatastoreResponseDatastoreProperties</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetDatastoreResponseDatastoreProperties</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of GetDatastoreResponseDatastoreProperties.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `datastoreId`
        if (data['datastoreId']) { // data not null
          String.validateJSON(data['datastoreId']);
        }
        // validate the optional field `datastoreName`
        if (data['datastoreName']) { // data not null
          String.validateJSON(data['datastoreName']);
        }
        // validate the optional field `datastoreStatus`
        if (data['datastoreStatus']) { // data not null
          DatastoreStatus.validateJSON(data['datastoreStatus']);
        }
        // validate the optional field `kmsKeyArn`
        if (data['kmsKeyArn']) { // data not null
          String.validateJSON(data['kmsKeyArn']);
        }
        // validate the optional field `datastoreArn`
        if (data['datastoreArn']) { // data not null
          String.validateJSON(data['datastoreArn']);
        }
        // validate the optional field `createdAt`
        if (data['createdAt']) { // data not null
          Date.validateJSON(data['createdAt']);
        }
        // validate the optional field `updatedAt`
        if (data['updatedAt']) { // data not null
          Date.validateJSON(data['updatedAt']);
        }

        return true;
    }


}

GetDatastoreResponseDatastoreProperties.RequiredProperties = ["datastoreId", "datastoreName", "datastoreStatus"];

/**
 * @member {String} datastoreId
 */
GetDatastoreResponseDatastoreProperties.prototype['datastoreId'] = undefined;

/**
 * @member {String} datastoreName
 */
GetDatastoreResponseDatastoreProperties.prototype['datastoreName'] = undefined;

/**
 * @member {module:model/DatastoreStatus} datastoreStatus
 */
GetDatastoreResponseDatastoreProperties.prototype['datastoreStatus'] = undefined;

/**
 * @member {String} kmsKeyArn
 */
GetDatastoreResponseDatastoreProperties.prototype['kmsKeyArn'] = undefined;

/**
 * @member {String} datastoreArn
 */
GetDatastoreResponseDatastoreProperties.prototype['datastoreArn'] = undefined;

/**
 * @member {Date} createdAt
 */
GetDatastoreResponseDatastoreProperties.prototype['createdAt'] = undefined;

/**
 * @member {Date} updatedAt
 */
GetDatastoreResponseDatastoreProperties.prototype['updatedAt'] = undefined;


// Implement DatastoreProperties interface:
/**
 * @member {String} datastoreId
 */
DatastoreProperties.prototype['datastoreId'] = undefined;
/**
 * @member {String} datastoreName
 */
DatastoreProperties.prototype['datastoreName'] = undefined;
/**
 * @member {module:model/DatastoreStatus} datastoreStatus
 */
DatastoreProperties.prototype['datastoreStatus'] = undefined;
/**
 * @member {String} kmsKeyArn
 */
DatastoreProperties.prototype['kmsKeyArn'] = undefined;
/**
 * @member {String} datastoreArn
 */
DatastoreProperties.prototype['datastoreArn'] = undefined;
/**
 * @member {Date} createdAt
 */
DatastoreProperties.prototype['createdAt'] = undefined;
/**
 * @member {Date} updatedAt
 */
DatastoreProperties.prototype['updatedAt'] = undefined;




export default GetDatastoreResponseDatastoreProperties;

