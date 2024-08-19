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

#include "OAIDatastoreSummary.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDatastoreSummary::OAIDatastoreSummary(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDatastoreSummary::OAIDatastoreSummary() {
    this->initializeModel();
}

OAIDatastoreSummary::~OAIDatastoreSummary() {}

void OAIDatastoreSummary::initializeModel() {

    m_datastore_id_isSet = false;
    m_datastore_id_isValid = false;

    m_datastore_name_isSet = false;
    m_datastore_name_isValid = false;

    m_datastore_status_isSet = false;
    m_datastore_status_isValid = false;

    m_datastore_arn_isSet = false;
    m_datastore_arn_isValid = false;

    m_created_at_isSet = false;
    m_created_at_isValid = false;

    m_updated_at_isSet = false;
    m_updated_at_isValid = false;
}

void OAIDatastoreSummary::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIDatastoreSummary::fromJsonObject(QJsonObject json) {

    m_datastore_id_isValid = ::OpenAPI::fromJsonValue(m_datastore_id, json[QString("datastoreId")]);
    m_datastore_id_isSet = !json[QString("datastoreId")].isNull() && m_datastore_id_isValid;

    m_datastore_name_isValid = ::OpenAPI::fromJsonValue(m_datastore_name, json[QString("datastoreName")]);
    m_datastore_name_isSet = !json[QString("datastoreName")].isNull() && m_datastore_name_isValid;

    m_datastore_status_isValid = ::OpenAPI::fromJsonValue(m_datastore_status, json[QString("datastoreStatus")]);
    m_datastore_status_isSet = !json[QString("datastoreStatus")].isNull() && m_datastore_status_isValid;

    m_datastore_arn_isValid = ::OpenAPI::fromJsonValue(m_datastore_arn, json[QString("datastoreArn")]);
    m_datastore_arn_isSet = !json[QString("datastoreArn")].isNull() && m_datastore_arn_isValid;

    m_created_at_isValid = ::OpenAPI::fromJsonValue(m_created_at, json[QString("createdAt")]);
    m_created_at_isSet = !json[QString("createdAt")].isNull() && m_created_at_isValid;

    m_updated_at_isValid = ::OpenAPI::fromJsonValue(m_updated_at, json[QString("updatedAt")]);
    m_updated_at_isSet = !json[QString("updatedAt")].isNull() && m_updated_at_isValid;
}

QString OAIDatastoreSummary::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIDatastoreSummary::asJsonObject() const {
    QJsonObject obj;
    if (m_datastore_id_isSet) {
        obj.insert(QString("datastoreId"), ::OpenAPI::toJsonValue(m_datastore_id));
    }
    if (m_datastore_name_isSet) {
        obj.insert(QString("datastoreName"), ::OpenAPI::toJsonValue(m_datastore_name));
    }
    if (m_datastore_status.isSet()) {
        obj.insert(QString("datastoreStatus"), ::OpenAPI::toJsonValue(m_datastore_status));
    }
    if (m_datastore_arn_isSet) {
        obj.insert(QString("datastoreArn"), ::OpenAPI::toJsonValue(m_datastore_arn));
    }
    if (m_created_at_isSet) {
        obj.insert(QString("createdAt"), ::OpenAPI::toJsonValue(m_created_at));
    }
    if (m_updated_at_isSet) {
        obj.insert(QString("updatedAt"), ::OpenAPI::toJsonValue(m_updated_at));
    }
    return obj;
}

QString OAIDatastoreSummary::getDatastoreId() const {
    return m_datastore_id;
}
void OAIDatastoreSummary::setDatastoreId(const QString &datastore_id) {
    m_datastore_id = datastore_id;
    m_datastore_id_isSet = true;
}

bool OAIDatastoreSummary::is_datastore_id_Set() const{
    return m_datastore_id_isSet;
}

bool OAIDatastoreSummary::is_datastore_id_Valid() const{
    return m_datastore_id_isValid;
}

QString OAIDatastoreSummary::getDatastoreName() const {
    return m_datastore_name;
}
void OAIDatastoreSummary::setDatastoreName(const QString &datastore_name) {
    m_datastore_name = datastore_name;
    m_datastore_name_isSet = true;
}

bool OAIDatastoreSummary::is_datastore_name_Set() const{
    return m_datastore_name_isSet;
}

bool OAIDatastoreSummary::is_datastore_name_Valid() const{
    return m_datastore_name_isValid;
}

OAIDatastoreStatus OAIDatastoreSummary::getDatastoreStatus() const {
    return m_datastore_status;
}
void OAIDatastoreSummary::setDatastoreStatus(const OAIDatastoreStatus &datastore_status) {
    m_datastore_status = datastore_status;
    m_datastore_status_isSet = true;
}

bool OAIDatastoreSummary::is_datastore_status_Set() const{
    return m_datastore_status_isSet;
}

bool OAIDatastoreSummary::is_datastore_status_Valid() const{
    return m_datastore_status_isValid;
}

QString OAIDatastoreSummary::getDatastoreArn() const {
    return m_datastore_arn;
}
void OAIDatastoreSummary::setDatastoreArn(const QString &datastore_arn) {
    m_datastore_arn = datastore_arn;
    m_datastore_arn_isSet = true;
}

bool OAIDatastoreSummary::is_datastore_arn_Set() const{
    return m_datastore_arn_isSet;
}

bool OAIDatastoreSummary::is_datastore_arn_Valid() const{
    return m_datastore_arn_isValid;
}

QDateTime OAIDatastoreSummary::getCreatedAt() const {
    return m_created_at;
}
void OAIDatastoreSummary::setCreatedAt(const QDateTime &created_at) {
    m_created_at = created_at;
    m_created_at_isSet = true;
}

bool OAIDatastoreSummary::is_created_at_Set() const{
    return m_created_at_isSet;
}

bool OAIDatastoreSummary::is_created_at_Valid() const{
    return m_created_at_isValid;
}

QDateTime OAIDatastoreSummary::getUpdatedAt() const {
    return m_updated_at;
}
void OAIDatastoreSummary::setUpdatedAt(const QDateTime &updated_at) {
    m_updated_at = updated_at;
    m_updated_at_isSet = true;
}

bool OAIDatastoreSummary::is_updated_at_Set() const{
    return m_updated_at_isSet;
}

bool OAIDatastoreSummary::is_updated_at_Valid() const{
    return m_updated_at_isValid;
}

bool OAIDatastoreSummary::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_datastore_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_datastore_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_datastore_status.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_datastore_arn_isSet) {
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
    } while (false);
    return isObjectUpdated;
}

bool OAIDatastoreSummary::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_datastore_id_isValid && m_datastore_name_isValid && m_datastore_status_isValid && true;
}

} // namespace OpenAPI
