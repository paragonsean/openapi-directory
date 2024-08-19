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
 */

#include "OAIImageSetWorkflowStatus.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIImageSetWorkflowStatus::OAIImageSetWorkflowStatus(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIImageSetWorkflowStatus::OAIImageSetWorkflowStatus() {
    this->initializeModel();
}

OAIImageSetWorkflowStatus::~OAIImageSetWorkflowStatus() {}

void OAIImageSetWorkflowStatus::initializeModel() {

    m_value_isSet = false;
    m_value_isValid = false;
    m_value = eOAIImageSetWorkflowStatus::INVALID_VALUE_OPENAPI_GENERATED;
}

void OAIImageSetWorkflowStatus::fromJson(QString jsonString) {
    
    if ( jsonString.compare("CREATED", Qt::CaseInsensitive) == 0) {
        m_value = eOAIImageSetWorkflowStatus::CREATED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("COPIED", Qt::CaseInsensitive) == 0) {
        m_value = eOAIImageSetWorkflowStatus::COPIED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("COPYING", Qt::CaseInsensitive) == 0) {
        m_value = eOAIImageSetWorkflowStatus::COPYING;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("COPYING_WITH_READ_ONLY_ACCESS", Qt::CaseInsensitive) == 0) {
        m_value = eOAIImageSetWorkflowStatus::COPYING_WITH_READ_ONLY_ACCESS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("COPY_FAILED", Qt::CaseInsensitive) == 0) {
        m_value = eOAIImageSetWorkflowStatus::COPY_FAILED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("UPDATING", Qt::CaseInsensitive) == 0) {
        m_value = eOAIImageSetWorkflowStatus::UPDATING;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("UPDATED", Qt::CaseInsensitive) == 0) {
        m_value = eOAIImageSetWorkflowStatus::UPDATED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("UPDATE_FAILED", Qt::CaseInsensitive) == 0) {
        m_value = eOAIImageSetWorkflowStatus::UPDATE_FAILED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("DELETING", Qt::CaseInsensitive) == 0) {
        m_value = eOAIImageSetWorkflowStatus::DELETING;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("DELETED", Qt::CaseInsensitive) == 0) {
        m_value = eOAIImageSetWorkflowStatus::DELETED;
        m_value_isSet = m_value_isValid = true;
    }
}

void OAIImageSetWorkflowStatus::fromJsonValue(QJsonValue json) {
fromJson(json.toString());
}

QString OAIImageSetWorkflowStatus::asJson() const {
    
    QString val;
    switch (m_value){
        case eOAIImageSetWorkflowStatus::CREATED:
            val = "CREATED";
            break;
        case eOAIImageSetWorkflowStatus::COPIED:
            val = "COPIED";
            break;
        case eOAIImageSetWorkflowStatus::COPYING:
            val = "COPYING";
            break;
        case eOAIImageSetWorkflowStatus::COPYING_WITH_READ_ONLY_ACCESS:
            val = "COPYING_WITH_READ_ONLY_ACCESS";
            break;
        case eOAIImageSetWorkflowStatus::COPY_FAILED:
            val = "COPY_FAILED";
            break;
        case eOAIImageSetWorkflowStatus::UPDATING:
            val = "UPDATING";
            break;
        case eOAIImageSetWorkflowStatus::UPDATED:
            val = "UPDATED";
            break;
        case eOAIImageSetWorkflowStatus::UPDATE_FAILED:
            val = "UPDATE_FAILED";
            break;
        case eOAIImageSetWorkflowStatus::DELETING:
            val = "DELETING";
            break;
        case eOAIImageSetWorkflowStatus::DELETED:
            val = "DELETED";
            break;
        default:
            break;
    }
    return val;
}

QJsonValue OAIImageSetWorkflowStatus::asJsonValue() const {
    
    return QJsonValue(asJson());
}


OAIImageSetWorkflowStatus::eOAIImageSetWorkflowStatus OAIImageSetWorkflowStatus::getValue() const {
    return m_value;
}

void OAIImageSetWorkflowStatus::setValue(const OAIImageSetWorkflowStatus::eOAIImageSetWorkflowStatus& value){
    m_value = value;
    m_value_isSet = true;
}
bool OAIImageSetWorkflowStatus::isSet() const {
    
    return m_value_isSet;
}

bool OAIImageSetWorkflowStatus::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_value_isValid;
}

} // namespace OpenAPI
