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
import DICOMTags from './DICOMTags';

/**
 * The ImageSetsMetadataSummaryDICOMTags model module.
 * @module model/ImageSetsMetadataSummaryDICOMTags
 * @version 2023-07-19
 */
class ImageSetsMetadataSummaryDICOMTags {
    /**
     * Constructs a new <code>ImageSetsMetadataSummaryDICOMTags</code>.
     * @alias module:model/ImageSetsMetadataSummaryDICOMTags
     * @implements module:model/DICOMTags
     */
    constructor() { 
        DICOMTags.initialize(this);
        ImageSetsMetadataSummaryDICOMTags.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ImageSetsMetadataSummaryDICOMTags</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ImageSetsMetadataSummaryDICOMTags} obj Optional instance to populate.
     * @return {module:model/ImageSetsMetadataSummaryDICOMTags} The populated <code>ImageSetsMetadataSummaryDICOMTags</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ImageSetsMetadataSummaryDICOMTags();
            DICOMTags.constructFromObject(data, obj);

            if (data.hasOwnProperty('DICOMPatientId')) {
                obj['DICOMPatientId'] = ApiClient.convertToType(data['DICOMPatientId'], 'String');
            }
            if (data.hasOwnProperty('DICOMPatientName')) {
                obj['DICOMPatientName'] = ApiClient.convertToType(data['DICOMPatientName'], 'String');
            }
            if (data.hasOwnProperty('DICOMPatientBirthDate')) {
                obj['DICOMPatientBirthDate'] = ApiClient.convertToType(data['DICOMPatientBirthDate'], 'String');
            }
            if (data.hasOwnProperty('DICOMPatientSex')) {
                obj['DICOMPatientSex'] = ApiClient.convertToType(data['DICOMPatientSex'], 'String');
            }
            if (data.hasOwnProperty('DICOMStudyInstanceUID')) {
                obj['DICOMStudyInstanceUID'] = ApiClient.convertToType(data['DICOMStudyInstanceUID'], 'String');
            }
            if (data.hasOwnProperty('DICOMStudyId')) {
                obj['DICOMStudyId'] = ApiClient.convertToType(data['DICOMStudyId'], 'String');
            }
            if (data.hasOwnProperty('DICOMStudyDescription')) {
                obj['DICOMStudyDescription'] = ApiClient.convertToType(data['DICOMStudyDescription'], 'String');
            }
            if (data.hasOwnProperty('DICOMNumberOfStudyRelatedSeries')) {
                obj['DICOMNumberOfStudyRelatedSeries'] = ApiClient.convertToType(data['DICOMNumberOfStudyRelatedSeries'], 'Number');
            }
            if (data.hasOwnProperty('DICOMNumberOfStudyRelatedInstances')) {
                obj['DICOMNumberOfStudyRelatedInstances'] = ApiClient.convertToType(data['DICOMNumberOfStudyRelatedInstances'], 'Number');
            }
            if (data.hasOwnProperty('DICOMAccessionNumber')) {
                obj['DICOMAccessionNumber'] = ApiClient.convertToType(data['DICOMAccessionNumber'], 'String');
            }
            if (data.hasOwnProperty('DICOMStudyDate')) {
                obj['DICOMStudyDate'] = ApiClient.convertToType(data['DICOMStudyDate'], 'String');
            }
            if (data.hasOwnProperty('DICOMStudyTime')) {
                obj['DICOMStudyTime'] = ApiClient.convertToType(data['DICOMStudyTime'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ImageSetsMetadataSummaryDICOMTags</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ImageSetsMetadataSummaryDICOMTags</code>.
     */
    static validateJSON(data) {
        // validate the optional field `DICOMPatientId`
        if (data['DICOMPatientId']) { // data not null
          String.validateJSON(data['DICOMPatientId']);
        }
        // validate the optional field `DICOMPatientName`
        if (data['DICOMPatientName']) { // data not null
          String.validateJSON(data['DICOMPatientName']);
        }
        // validate the optional field `DICOMPatientBirthDate`
        if (data['DICOMPatientBirthDate']) { // data not null
          String.validateJSON(data['DICOMPatientBirthDate']);
        }
        // validate the optional field `DICOMPatientSex`
        if (data['DICOMPatientSex']) { // data not null
          String.validateJSON(data['DICOMPatientSex']);
        }
        // validate the optional field `DICOMStudyInstanceUID`
        if (data['DICOMStudyInstanceUID']) { // data not null
          String.validateJSON(data['DICOMStudyInstanceUID']);
        }
        // validate the optional field `DICOMStudyId`
        if (data['DICOMStudyId']) { // data not null
          String.validateJSON(data['DICOMStudyId']);
        }
        // validate the optional field `DICOMStudyDescription`
        if (data['DICOMStudyDescription']) { // data not null
          String.validateJSON(data['DICOMStudyDescription']);
        }
        // validate the optional field `DICOMNumberOfStudyRelatedSeries`
        if (data['DICOMNumberOfStudyRelatedSeries']) { // data not null
          Number.validateJSON(data['DICOMNumberOfStudyRelatedSeries']);
        }
        // validate the optional field `DICOMNumberOfStudyRelatedInstances`
        if (data['DICOMNumberOfStudyRelatedInstances']) { // data not null
          Number.validateJSON(data['DICOMNumberOfStudyRelatedInstances']);
        }
        // validate the optional field `DICOMAccessionNumber`
        if (data['DICOMAccessionNumber']) { // data not null
          String.validateJSON(data['DICOMAccessionNumber']);
        }
        // validate the optional field `DICOMStudyDate`
        if (data['DICOMStudyDate']) { // data not null
          String.validateJSON(data['DICOMStudyDate']);
        }
        // validate the optional field `DICOMStudyTime`
        if (data['DICOMStudyTime']) { // data not null
          String.validateJSON(data['DICOMStudyTime']);
        }

        return true;
    }


}



/**
 * @member {String} DICOMPatientId
 */
ImageSetsMetadataSummaryDICOMTags.prototype['DICOMPatientId'] = undefined;

/**
 * @member {String} DICOMPatientName
 */
ImageSetsMetadataSummaryDICOMTags.prototype['DICOMPatientName'] = undefined;

/**
 * @member {String} DICOMPatientBirthDate
 */
ImageSetsMetadataSummaryDICOMTags.prototype['DICOMPatientBirthDate'] = undefined;

/**
 * @member {String} DICOMPatientSex
 */
ImageSetsMetadataSummaryDICOMTags.prototype['DICOMPatientSex'] = undefined;

/**
 * @member {String} DICOMStudyInstanceUID
 */
ImageSetsMetadataSummaryDICOMTags.prototype['DICOMStudyInstanceUID'] = undefined;

/**
 * @member {String} DICOMStudyId
 */
ImageSetsMetadataSummaryDICOMTags.prototype['DICOMStudyId'] = undefined;

/**
 * @member {String} DICOMStudyDescription
 */
ImageSetsMetadataSummaryDICOMTags.prototype['DICOMStudyDescription'] = undefined;

/**
 * @member {Number} DICOMNumberOfStudyRelatedSeries
 */
ImageSetsMetadataSummaryDICOMTags.prototype['DICOMNumberOfStudyRelatedSeries'] = undefined;

/**
 * @member {Number} DICOMNumberOfStudyRelatedInstances
 */
ImageSetsMetadataSummaryDICOMTags.prototype['DICOMNumberOfStudyRelatedInstances'] = undefined;

/**
 * @member {String} DICOMAccessionNumber
 */
ImageSetsMetadataSummaryDICOMTags.prototype['DICOMAccessionNumber'] = undefined;

/**
 * @member {String} DICOMStudyDate
 */
ImageSetsMetadataSummaryDICOMTags.prototype['DICOMStudyDate'] = undefined;

/**
 * @member {String} DICOMStudyTime
 */
ImageSetsMetadataSummaryDICOMTags.prototype['DICOMStudyTime'] = undefined;


// Implement DICOMTags interface:
/**
 * @member {String} DICOMPatientId
 */
DICOMTags.prototype['DICOMPatientId'] = undefined;
/**
 * @member {String} DICOMPatientName
 */
DICOMTags.prototype['DICOMPatientName'] = undefined;
/**
 * @member {String} DICOMPatientBirthDate
 */
DICOMTags.prototype['DICOMPatientBirthDate'] = undefined;
/**
 * @member {String} DICOMPatientSex
 */
DICOMTags.prototype['DICOMPatientSex'] = undefined;
/**
 * @member {String} DICOMStudyInstanceUID
 */
DICOMTags.prototype['DICOMStudyInstanceUID'] = undefined;
/**
 * @member {String} DICOMStudyId
 */
DICOMTags.prototype['DICOMStudyId'] = undefined;
/**
 * @member {String} DICOMStudyDescription
 */
DICOMTags.prototype['DICOMStudyDescription'] = undefined;
/**
 * @member {Number} DICOMNumberOfStudyRelatedSeries
 */
DICOMTags.prototype['DICOMNumberOfStudyRelatedSeries'] = undefined;
/**
 * @member {Number} DICOMNumberOfStudyRelatedInstances
 */
DICOMTags.prototype['DICOMNumberOfStudyRelatedInstances'] = undefined;
/**
 * @member {String} DICOMAccessionNumber
 */
DICOMTags.prototype['DICOMAccessionNumber'] = undefined;
/**
 * @member {String} DICOMStudyDate
 */
DICOMTags.prototype['DICOMStudyDate'] = undefined;
/**
 * @member {String} DICOMStudyTime
 */
DICOMTags.prototype['DICOMStudyTime'] = undefined;




export default ImageSetsMetadataSummaryDICOMTags;

