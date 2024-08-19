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

#include "OAIStartDICOMImportJobResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIStartDICOMImportJobResponse::OAIStartDICOMImportJobResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIStartDICOMImportJobResponse::OAIStartDICOMImportJobResponse() {
    this->initializeModel();
}

OAIStartDICOMImportJobResponse::~OAIStartDICOMImportJobResponse() {}

void OAIStartDICOMImportJobResponse::initializeModel() {

    m_datastore_id_isSet = false;
    m_datastore_id_isValid = false;

    m_job_id_isSet = false;
    m_job_id_isValid = false;

    m_job_status_isSet = false;
    m_job_status_isValid = false;

    m_submitted_at_isSet = false;
    m_submitted_at_isValid = false;
}

void OAIStartDICOMImportJobResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIStartDICOMImportJobResponse::fromJsonObject(QJsonObject json) {

    m_datastore_id_isValid = ::OpenAPI::fromJsonValue(m_datastore_id, json[QString("datastoreId")]);
    m_datastore_id_isSet = !json[QString("datastoreId")].isNull() && m_datastore_id_isValid;

    m_job_id_isValid = ::OpenAPI::fromJsonValue(m_job_id, json[QString("jobId")]);
    m_job_id_isSet = !json[QString("jobId")].isNull() && m_job_id_isValid;

    m_job_status_isValid = ::OpenAPI::fromJsonValue(m_job_status, json[QString("jobStatus")]);
    m_job_status_isSet = !json[QString("jobStatus")].isNull() && m_job_status_isValid;

    m_submitted_at_isValid = ::OpenAPI::fromJsonValue(m_submitted_at, json[QString("submittedAt")]);
    m_submitted_at_isSet = !json[QString("submittedAt")].isNull() && m_submitted_at_isValid;
}

QString OAIStartDICOMImportJobResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIStartDICOMImportJobResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_datastore_id_isSet) {
        obj.insert(QString("datastoreId"), ::OpenAPI::toJsonValue(m_datastore_id));
    }
    if (m_job_id_isSet) {
        obj.insert(QString("jobId"), ::OpenAPI::toJsonValue(m_job_id));
    }
    if (m_job_status.isSet()) {
        obj.insert(QString("jobStatus"), ::OpenAPI::toJsonValue(m_job_status));
    }
    if (m_submitted_at_isSet) {
        obj.insert(QString("submittedAt"), ::OpenAPI::toJsonValue(m_submitted_at));
    }
    return obj;
}

QString OAIStartDICOMImportJobResponse::getDatastoreId() const {
    return m_datastore_id;
}
void OAIStartDICOMImportJobResponse::setDatastoreId(const QString &datastore_id) {
    m_datastore_id = datastore_id;
    m_datastore_id_isSet = true;
}

bool OAIStartDICOMImportJobResponse::is_datastore_id_Set() const{
    return m_datastore_id_isSet;
}

bool OAIStartDICOMImportJobResponse::is_datastore_id_Valid() const{
    return m_datastore_id_isValid;
}

QString OAIStartDICOMImportJobResponse::getJobId() const {
    return m_job_id;
}
void OAIStartDICOMImportJobResponse::setJobId(const QString &job_id) {
    m_job_id = job_id;
    m_job_id_isSet = true;
}

bool OAIStartDICOMImportJobResponse::is_job_id_Set() const{
    return m_job_id_isSet;
}

bool OAIStartDICOMImportJobResponse::is_job_id_Valid() const{
    return m_job_id_isValid;
}

OAIJobStatus OAIStartDICOMImportJobResponse::getJobStatus() const {
    return m_job_status;
}
void OAIStartDICOMImportJobResponse::setJobStatus(const OAIJobStatus &job_status) {
    m_job_status = job_status;
    m_job_status_isSet = true;
}

bool OAIStartDICOMImportJobResponse::is_job_status_Set() const{
    return m_job_status_isSet;
}

bool OAIStartDICOMImportJobResponse::is_job_status_Valid() const{
    return m_job_status_isValid;
}

QDateTime OAIStartDICOMImportJobResponse::getSubmittedAt() const {
    return m_submitted_at;
}
void OAIStartDICOMImportJobResponse::setSubmittedAt(const QDateTime &submitted_at) {
    m_submitted_at = submitted_at;
    m_submitted_at_isSet = true;
}

bool OAIStartDICOMImportJobResponse::is_submitted_at_Set() const{
    return m_submitted_at_isSet;
}

bool OAIStartDICOMImportJobResponse::is_submitted_at_Valid() const{
    return m_submitted_at_isValid;
}

bool OAIStartDICOMImportJobResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_datastore_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_job_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_job_status.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_submitted_at_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIStartDICOMImportJobResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_datastore_id_isValid && m_job_id_isValid && m_job_status_isValid && m_submitted_at_isValid && true;
}

} // namespace OpenAPI
