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

#include "OAIImageSetProperties.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIImageSetProperties::OAIImageSetProperties(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIImageSetProperties::OAIImageSetProperties() {
    this->initializeModel();
}

OAIImageSetProperties::~OAIImageSetProperties() {}

void OAIImageSetProperties::initializeModel() {

    m_image_set_id_isSet = false;
    m_image_set_id_isValid = false;

    m_version_id_isSet = false;
    m_version_id_isValid = false;

    m_image_set_state_isSet = false;
    m_image_set_state_isValid = false;

    m_image_set_workflow_status_isSet = false;
    m_image_set_workflow_status_isValid = false;

    m_created_at_isSet = false;
    m_created_at_isValid = false;

    m_updated_at_isSet = false;
    m_updated_at_isValid = false;

    m_deleted_at_isSet = false;
    m_deleted_at_isValid = false;

    m_message_isSet = false;
    m_message_isValid = false;
}

void OAIImageSetProperties::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIImageSetProperties::fromJsonObject(QJsonObject json) {

    m_image_set_id_isValid = ::OpenAPI::fromJsonValue(m_image_set_id, json[QString("imageSetId")]);
    m_image_set_id_isSet = !json[QString("imageSetId")].isNull() && m_image_set_id_isValid;

    m_version_id_isValid = ::OpenAPI::fromJsonValue(m_version_id, json[QString("versionId")]);
    m_version_id_isSet = !json[QString("versionId")].isNull() && m_version_id_isValid;

    m_image_set_state_isValid = ::OpenAPI::fromJsonValue(m_image_set_state, json[QString("imageSetState")]);
    m_image_set_state_isSet = !json[QString("imageSetState")].isNull() && m_image_set_state_isValid;

    m_image_set_workflow_status_isValid = ::OpenAPI::fromJsonValue(m_image_set_workflow_status, json[QString("ImageSetWorkflowStatus")]);
    m_image_set_workflow_status_isSet = !json[QString("ImageSetWorkflowStatus")].isNull() && m_image_set_workflow_status_isValid;

    m_created_at_isValid = ::OpenAPI::fromJsonValue(m_created_at, json[QString("createdAt")]);
    m_created_at_isSet = !json[QString("createdAt")].isNull() && m_created_at_isValid;

    m_updated_at_isValid = ::OpenAPI::fromJsonValue(m_updated_at, json[QString("updatedAt")]);
    m_updated_at_isSet = !json[QString("updatedAt")].isNull() && m_updated_at_isValid;

    m_deleted_at_isValid = ::OpenAPI::fromJsonValue(m_deleted_at, json[QString("deletedAt")]);
    m_deleted_at_isSet = !json[QString("deletedAt")].isNull() && m_deleted_at_isValid;

    m_message_isValid = ::OpenAPI::fromJsonValue(m_message, json[QString("message")]);
    m_message_isSet = !json[QString("message")].isNull() && m_message_isValid;
}

QString OAIImageSetProperties::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIImageSetProperties::asJsonObject() const {
    QJsonObject obj;
    if (m_image_set_id_isSet) {
        obj.insert(QString("imageSetId"), ::OpenAPI::toJsonValue(m_image_set_id));
    }
    if (m_version_id_isSet) {
        obj.insert(QString("versionId"), ::OpenAPI::toJsonValue(m_version_id));
    }
    if (m_image_set_state.isSet()) {
        obj.insert(QString("imageSetState"), ::OpenAPI::toJsonValue(m_image_set_state));
    }
    if (m_image_set_workflow_status.isSet()) {
        obj.insert(QString("ImageSetWorkflowStatus"), ::OpenAPI::toJsonValue(m_image_set_workflow_status));
    }
    if (m_created_at_isSet) {
        obj.insert(QString("createdAt"), ::OpenAPI::toJsonValue(m_created_at));
    }
    if (m_updated_at_isSet) {
        obj.insert(QString("updatedAt"), ::OpenAPI::toJsonValue(m_updated_at));
    }
    if (m_deleted_at_isSet) {
        obj.insert(QString("deletedAt"), ::OpenAPI::toJsonValue(m_deleted_at));
    }
    if (m_message_isSet) {
        obj.insert(QString("message"), ::OpenAPI::toJsonValue(m_message));
    }
    return obj;
}

QString OAIImageSetProperties::getImageSetId() const {
    return m_image_set_id;
}
void OAIImageSetProperties::setImageSetId(const QString &image_set_id) {
    m_image_set_id = image_set_id;
    m_image_set_id_isSet = true;
}

bool OAIImageSetProperties::is_image_set_id_Set() const{
    return m_image_set_id_isSet;
}

bool OAIImageSetProperties::is_image_set_id_Valid() const{
    return m_image_set_id_isValid;
}

QString OAIImageSetProperties::getVersionId() const {
    return m_version_id;
}
void OAIImageSetProperties::setVersionId(const QString &version_id) {
    m_version_id = version_id;
    m_version_id_isSet = true;
}

bool OAIImageSetProperties::is_version_id_Set() const{
    return m_version_id_isSet;
}

bool OAIImageSetProperties::is_version_id_Valid() const{
    return m_version_id_isValid;
}

OAIImageSetState OAIImageSetProperties::getImageSetState() const {
    return m_image_set_state;
}
void OAIImageSetProperties::setImageSetState(const OAIImageSetState &image_set_state) {
    m_image_set_state = image_set_state;
    m_image_set_state_isSet = true;
}

bool OAIImageSetProperties::is_image_set_state_Set() const{
    return m_image_set_state_isSet;
}

bool OAIImageSetProperties::is_image_set_state_Valid() const{
    return m_image_set_state_isValid;
}

OAIImageSetWorkflowStatus OAIImageSetProperties::getImageSetWorkflowStatus() const {
    return m_image_set_workflow_status;
}
void OAIImageSetProperties::setImageSetWorkflowStatus(const OAIImageSetWorkflowStatus &image_set_workflow_status) {
    m_image_set_workflow_status = image_set_workflow_status;
    m_image_set_workflow_status_isSet = true;
}

bool OAIImageSetProperties::is_image_set_workflow_status_Set() const{
    return m_image_set_workflow_status_isSet;
}

bool OAIImageSetProperties::is_image_set_workflow_status_Valid() const{
    return m_image_set_workflow_status_isValid;
}

QDateTime OAIImageSetProperties::getCreatedAt() const {
    return m_created_at;
}
void OAIImageSetProperties::setCreatedAt(const QDateTime &created_at) {
    m_created_at = created_at;
    m_created_at_isSet = true;
}

bool OAIImageSetProperties::is_created_at_Set() const{
    return m_created_at_isSet;
}

bool OAIImageSetProperties::is_created_at_Valid() const{
    return m_created_at_isValid;
}

QDateTime OAIImageSetProperties::getUpdatedAt() const {
    return m_updated_at;
}
void OAIImageSetProperties::setUpdatedAt(const QDateTime &updated_at) {
    m_updated_at = updated_at;
    m_updated_at_isSet = true;
}

bool OAIImageSetProperties::is_updated_at_Set() const{
    return m_updated_at_isSet;
}

bool OAIImageSetProperties::is_updated_at_Valid() const{
    return m_updated_at_isValid;
}

QDateTime OAIImageSetProperties::getDeletedAt() const {
    return m_deleted_at;
}
void OAIImageSetProperties::setDeletedAt(const QDateTime &deleted_at) {
    m_deleted_at = deleted_at;
    m_deleted_at_isSet = true;
}

bool OAIImageSetProperties::is_deleted_at_Set() const{
    return m_deleted_at_isSet;
}

bool OAIImageSetProperties::is_deleted_at_Valid() const{
    return m_deleted_at_isValid;
}

QString OAIImageSetProperties::getMessage() const {
    return m_message;
}
void OAIImageSetProperties::setMessage(const QString &message) {
    m_message = message;
    m_message_isSet = true;
}

bool OAIImageSetProperties::is_message_Set() const{
    return m_message_isSet;
}

bool OAIImageSetProperties::is_message_Valid() const{
    return m_message_isValid;
}

bool OAIImageSetProperties::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_image_set_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_version_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_image_set_state.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_image_set_workflow_status.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_updated_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_deleted_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_message_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIImageSetProperties::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_image_set_id_isValid && m_version_id_isValid && m_image_set_state_isValid && true;
}

} // namespace OpenAPI
