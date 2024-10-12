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

#include "OAIGetDICOMImportJobResponse_jobProperties.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetDICOMImportJobResponse_jobProperties::OAIGetDICOMImportJobResponse_jobProperties(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetDICOMImportJobResponse_jobProperties::OAIGetDICOMImportJobResponse_jobProperties() {
    this->initializeModel();
}

OAIGetDICOMImportJobResponse_jobProperties::~OAIGetDICOMImportJobResponse_jobProperties() {}

void OAIGetDICOMImportJobResponse_jobProperties::initializeModel() {

    m_job_id_isSet = false;
    m_job_id_isValid = false;

    m_job_name_isSet = false;
    m_job_name_isValid = false;

    m_job_status_isSet = false;
    m_job_status_isValid = false;

    m_datastore_id_isSet = false;
    m_datastore_id_isValid = false;

    m_data_access_role_arn_isSet = false;
    m_data_access_role_arn_isValid = false;

    m_ended_at_isSet = false;
    m_ended_at_isValid = false;

    m_submitted_at_isSet = false;
    m_submitted_at_isValid = false;

    m_input_s3_uri_isSet = false;
    m_input_s3_uri_isValid = false;

    m_output_s3_uri_isSet = false;
    m_output_s3_uri_isValid = false;

    m_message_isSet = false;
    m_message_isValid = false;
}

void OAIGetDICOMImportJobResponse_jobProperties::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetDICOMImportJobResponse_jobProperties::fromJsonObject(QJsonObject json) {

    m_job_id_isValid = ::OpenAPI::fromJsonValue(m_job_id, json[QString("jobId")]);
    m_job_id_isSet = !json[QString("jobId")].isNull() && m_job_id_isValid;

    m_job_name_isValid = ::OpenAPI::fromJsonValue(m_job_name, json[QString("jobName")]);
    m_job_name_isSet = !json[QString("jobName")].isNull() && m_job_name_isValid;

    m_job_status_isValid = ::OpenAPI::fromJsonValue(m_job_status, json[QString("jobStatus")]);
    m_job_status_isSet = !json[QString("jobStatus")].isNull() && m_job_status_isValid;

    m_datastore_id_isValid = ::OpenAPI::fromJsonValue(m_datastore_id, json[QString("datastoreId")]);
    m_datastore_id_isSet = !json[QString("datastoreId")].isNull() && m_datastore_id_isValid;

    m_data_access_role_arn_isValid = ::OpenAPI::fromJsonValue(m_data_access_role_arn, json[QString("dataAccessRoleArn")]);
    m_data_access_role_arn_isSet = !json[QString("dataAccessRoleArn")].isNull() && m_data_access_role_arn_isValid;

    m_ended_at_isValid = ::OpenAPI::fromJsonValue(m_ended_at, json[QString("endedAt")]);
    m_ended_at_isSet = !json[QString("endedAt")].isNull() && m_ended_at_isValid;

    m_submitted_at_isValid = ::OpenAPI::fromJsonValue(m_submitted_at, json[QString("submittedAt")]);
    m_submitted_at_isSet = !json[QString("submittedAt")].isNull() && m_submitted_at_isValid;

    m_input_s3_uri_isValid = ::OpenAPI::fromJsonValue(m_input_s3_uri, json[QString("inputS3Uri")]);
    m_input_s3_uri_isSet = !json[QString("inputS3Uri")].isNull() && m_input_s3_uri_isValid;

    m_output_s3_uri_isValid = ::OpenAPI::fromJsonValue(m_output_s3_uri, json[QString("outputS3Uri")]);
    m_output_s3_uri_isSet = !json[QString("outputS3Uri")].isNull() && m_output_s3_uri_isValid;

    m_message_isValid = ::OpenAPI::fromJsonValue(m_message, json[QString("message")]);
    m_message_isSet = !json[QString("message")].isNull() && m_message_isValid;
}

QString OAIGetDICOMImportJobResponse_jobProperties::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetDICOMImportJobResponse_jobProperties::asJsonObject() const {
    QJsonObject obj;
    if (m_job_id_isSet) {
        obj.insert(QString("jobId"), ::OpenAPI::toJsonValue(m_job_id));
    }
    if (m_job_name_isSet) {
        obj.insert(QString("jobName"), ::OpenAPI::toJsonValue(m_job_name));
    }
    if (m_job_status.isSet()) {
        obj.insert(QString("jobStatus"), ::OpenAPI::toJsonValue(m_job_status));
    }
    if (m_datastore_id_isSet) {
        obj.insert(QString("datastoreId"), ::OpenAPI::toJsonValue(m_datastore_id));
    }
    if (m_data_access_role_arn_isSet) {
        obj.insert(QString("dataAccessRoleArn"), ::OpenAPI::toJsonValue(m_data_access_role_arn));
    }
    if (m_ended_at_isSet) {
        obj.insert(QString("endedAt"), ::OpenAPI::toJsonValue(m_ended_at));
    }
    if (m_submitted_at_isSet) {
        obj.insert(QString("submittedAt"), ::OpenAPI::toJsonValue(m_submitted_at));
    }
    if (m_input_s3_uri_isSet) {
        obj.insert(QString("inputS3Uri"), ::OpenAPI::toJsonValue(m_input_s3_uri));
    }
    if (m_output_s3_uri_isSet) {
        obj.insert(QString("outputS3Uri"), ::OpenAPI::toJsonValue(m_output_s3_uri));
    }
    if (m_message_isSet) {
        obj.insert(QString("message"), ::OpenAPI::toJsonValue(m_message));
    }
    return obj;
}

QString OAIGetDICOMImportJobResponse_jobProperties::getJobId() const {
    return m_job_id;
}
void OAIGetDICOMImportJobResponse_jobProperties::setJobId(const QString &job_id) {
    m_job_id = job_id;
    m_job_id_isSet = true;
}

bool OAIGetDICOMImportJobResponse_jobProperties::is_job_id_Set() const{
    return m_job_id_isSet;
}

bool OAIGetDICOMImportJobResponse_jobProperties::is_job_id_Valid() const{
    return m_job_id_isValid;
}

QString OAIGetDICOMImportJobResponse_jobProperties::getJobName() const {
    return m_job_name;
}
void OAIGetDICOMImportJobResponse_jobProperties::setJobName(const QString &job_name) {
    m_job_name = job_name;
    m_job_name_isSet = true;
}

bool OAIGetDICOMImportJobResponse_jobProperties::is_job_name_Set() const{
    return m_job_name_isSet;
}

bool OAIGetDICOMImportJobResponse_jobProperties::is_job_name_Valid() const{
    return m_job_name_isValid;
}

OAIJobStatus OAIGetDICOMImportJobResponse_jobProperties::getJobStatus() const {
    return m_job_status;
}
void OAIGetDICOMImportJobResponse_jobProperties::setJobStatus(const OAIJobStatus &job_status) {
    m_job_status = job_status;
    m_job_status_isSet = true;
}

bool OAIGetDICOMImportJobResponse_jobProperties::is_job_status_Set() const{
    return m_job_status_isSet;
}

bool OAIGetDICOMImportJobResponse_jobProperties::is_job_status_Valid() const{
    return m_job_status_isValid;
}

QString OAIGetDICOMImportJobResponse_jobProperties::getDatastoreId() const {
    return m_datastore_id;
}
void OAIGetDICOMImportJobResponse_jobProperties::setDatastoreId(const QString &datastore_id) {
    m_datastore_id = datastore_id;
    m_datastore_id_isSet = true;
}

bool OAIGetDICOMImportJobResponse_jobProperties::is_datastore_id_Set() const{
    return m_datastore_id_isSet;
}

bool OAIGetDICOMImportJobResponse_jobProperties::is_datastore_id_Valid() const{
    return m_datastore_id_isValid;
}

QString OAIGetDICOMImportJobResponse_jobProperties::getDataAccessRoleArn() const {
    return m_data_access_role_arn;
}
void OAIGetDICOMImportJobResponse_jobProperties::setDataAccessRoleArn(const QString &data_access_role_arn) {
    m_data_access_role_arn = data_access_role_arn;
    m_data_access_role_arn_isSet = true;
}

bool OAIGetDICOMImportJobResponse_jobProperties::is_data_access_role_arn_Set() const{
    return m_data_access_role_arn_isSet;
}

bool OAIGetDICOMImportJobResponse_jobProperties::is_data_access_role_arn_Valid() const{
    return m_data_access_role_arn_isValid;
}

QDateTime OAIGetDICOMImportJobResponse_jobProperties::getEndedAt() const {
    return m_ended_at;
}
void OAIGetDICOMImportJobResponse_jobProperties::setEndedAt(const QDateTime &ended_at) {
    m_ended_at = ended_at;
    m_ended_at_isSet = true;
}

bool OAIGetDICOMImportJobResponse_jobProperties::is_ended_at_Set() const{
    return m_ended_at_isSet;
}

bool OAIGetDICOMImportJobResponse_jobProperties::is_ended_at_Valid() const{
    return m_ended_at_isValid;
}

QDateTime OAIGetDICOMImportJobResponse_jobProperties::getSubmittedAt() const {
    return m_submitted_at;
}
void OAIGetDICOMImportJobResponse_jobProperties::setSubmittedAt(const QDateTime &submitted_at) {
    m_submitted_at = submitted_at;
    m_submitted_at_isSet = true;
}

bool OAIGetDICOMImportJobResponse_jobProperties::is_submitted_at_Set() const{
    return m_submitted_at_isSet;
}

bool OAIGetDICOMImportJobResponse_jobProperties::is_submitted_at_Valid() const{
    return m_submitted_at_isValid;
}

QString OAIGetDICOMImportJobResponse_jobProperties::getInputS3Uri() const {
    return m_input_s3_uri;
}
void OAIGetDICOMImportJobResponse_jobProperties::setInputS3Uri(const QString &input_s3_uri) {
    m_input_s3_uri = input_s3_uri;
    m_input_s3_uri_isSet = true;
}

bool OAIGetDICOMImportJobResponse_jobProperties::is_input_s3_uri_Set() const{
    return m_input_s3_uri_isSet;
}

bool OAIGetDICOMImportJobResponse_jobProperties::is_input_s3_uri_Valid() const{
    return m_input_s3_uri_isValid;
}

QString OAIGetDICOMImportJobResponse_jobProperties::getOutputS3Uri() const {
    return m_output_s3_uri;
}
void OAIGetDICOMImportJobResponse_jobProperties::setOutputS3Uri(const QString &output_s3_uri) {
    m_output_s3_uri = output_s3_uri;
    m_output_s3_uri_isSet = true;
}

bool OAIGetDICOMImportJobResponse_jobProperties::is_output_s3_uri_Set() const{
    return m_output_s3_uri_isSet;
}

bool OAIGetDICOMImportJobResponse_jobProperties::is_output_s3_uri_Valid() const{
    return m_output_s3_uri_isValid;
}

QString OAIGetDICOMImportJobResponse_jobProperties::getMessage() const {
    return m_message;
}
void OAIGetDICOMImportJobResponse_jobProperties::setMessage(const QString &message) {
    m_message = message;
    m_message_isSet = true;
}

bool OAIGetDICOMImportJobResponse_jobProperties::is_message_Set() const{
    return m_message_isSet;
}

bool OAIGetDICOMImportJobResponse_jobProperties::is_message_Valid() const{
    return m_message_isValid;
}

bool OAIGetDICOMImportJobResponse_jobProperties::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_job_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_job_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_job_status.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_datastore_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_data_access_role_arn_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ended_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_submitted_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_input_s3_uri_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_output_s3_uri_isSet) {
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

bool OAIGetDICOMImportJobResponse_jobProperties::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_job_id_isValid && m_job_name_isValid && m_job_status_isValid && m_datastore_id_isValid && m_data_access_role_arn_isValid && m_input_s3_uri_isValid && m_output_s3_uri_isValid && true;
}

} // namespace OpenAPI
