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

#include "OAIStartDICOMImportJobRequest.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIStartDICOMImportJobRequest::OAIStartDICOMImportJobRequest(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIStartDICOMImportJobRequest::OAIStartDICOMImportJobRequest() {
    this->initializeModel();
}

OAIStartDICOMImportJobRequest::~OAIStartDICOMImportJobRequest() {}

void OAIStartDICOMImportJobRequest::initializeModel() {

    m_job_name_isSet = false;
    m_job_name_isValid = false;

    m_data_access_role_arn_isSet = false;
    m_data_access_role_arn_isValid = false;

    m_client_token_isSet = false;
    m_client_token_isValid = false;

    m_input_s3_uri_isSet = false;
    m_input_s3_uri_isValid = false;

    m_output_s3_uri_isSet = false;
    m_output_s3_uri_isValid = false;
}

void OAIStartDICOMImportJobRequest::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIStartDICOMImportJobRequest::fromJsonObject(QJsonObject json) {

    m_job_name_isValid = ::OpenAPI::fromJsonValue(m_job_name, json[QString("jobName")]);
    m_job_name_isSet = !json[QString("jobName")].isNull() && m_job_name_isValid;

    m_data_access_role_arn_isValid = ::OpenAPI::fromJsonValue(m_data_access_role_arn, json[QString("dataAccessRoleArn")]);
    m_data_access_role_arn_isSet = !json[QString("dataAccessRoleArn")].isNull() && m_data_access_role_arn_isValid;

    m_client_token_isValid = ::OpenAPI::fromJsonValue(m_client_token, json[QString("clientToken")]);
    m_client_token_isSet = !json[QString("clientToken")].isNull() && m_client_token_isValid;

    m_input_s3_uri_isValid = ::OpenAPI::fromJsonValue(m_input_s3_uri, json[QString("inputS3Uri")]);
    m_input_s3_uri_isSet = !json[QString("inputS3Uri")].isNull() && m_input_s3_uri_isValid;

    m_output_s3_uri_isValid = ::OpenAPI::fromJsonValue(m_output_s3_uri, json[QString("outputS3Uri")]);
    m_output_s3_uri_isSet = !json[QString("outputS3Uri")].isNull() && m_output_s3_uri_isValid;
}

QString OAIStartDICOMImportJobRequest::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIStartDICOMImportJobRequest::asJsonObject() const {
    QJsonObject obj;
    if (m_job_name_isSet) {
        obj.insert(QString("jobName"), ::OpenAPI::toJsonValue(m_job_name));
    }
    if (m_data_access_role_arn_isSet) {
        obj.insert(QString("dataAccessRoleArn"), ::OpenAPI::toJsonValue(m_data_access_role_arn));
    }
    if (m_client_token_isSet) {
        obj.insert(QString("clientToken"), ::OpenAPI::toJsonValue(m_client_token));
    }
    if (m_input_s3_uri_isSet) {
        obj.insert(QString("inputS3Uri"), ::OpenAPI::toJsonValue(m_input_s3_uri));
    }
    if (m_output_s3_uri_isSet) {
        obj.insert(QString("outputS3Uri"), ::OpenAPI::toJsonValue(m_output_s3_uri));
    }
    return obj;
}

QString OAIStartDICOMImportJobRequest::getJobName() const {
    return m_job_name;
}
void OAIStartDICOMImportJobRequest::setJobName(const QString &job_name) {
    m_job_name = job_name;
    m_job_name_isSet = true;
}

bool OAIStartDICOMImportJobRequest::is_job_name_Set() const{
    return m_job_name_isSet;
}

bool OAIStartDICOMImportJobRequest::is_job_name_Valid() const{
    return m_job_name_isValid;
}

QString OAIStartDICOMImportJobRequest::getDataAccessRoleArn() const {
    return m_data_access_role_arn;
}
void OAIStartDICOMImportJobRequest::setDataAccessRoleArn(const QString &data_access_role_arn) {
    m_data_access_role_arn = data_access_role_arn;
    m_data_access_role_arn_isSet = true;
}

bool OAIStartDICOMImportJobRequest::is_data_access_role_arn_Set() const{
    return m_data_access_role_arn_isSet;
}

bool OAIStartDICOMImportJobRequest::is_data_access_role_arn_Valid() const{
    return m_data_access_role_arn_isValid;
}

QString OAIStartDICOMImportJobRequest::getClientToken() const {
    return m_client_token;
}
void OAIStartDICOMImportJobRequest::setClientToken(const QString &client_token) {
    m_client_token = client_token;
    m_client_token_isSet = true;
}

bool OAIStartDICOMImportJobRequest::is_client_token_Set() const{
    return m_client_token_isSet;
}

bool OAIStartDICOMImportJobRequest::is_client_token_Valid() const{
    return m_client_token_isValid;
}

QString OAIStartDICOMImportJobRequest::getInputS3Uri() const {
    return m_input_s3_uri;
}
void OAIStartDICOMImportJobRequest::setInputS3Uri(const QString &input_s3_uri) {
    m_input_s3_uri = input_s3_uri;
    m_input_s3_uri_isSet = true;
}

bool OAIStartDICOMImportJobRequest::is_input_s3_uri_Set() const{
    return m_input_s3_uri_isSet;
}

bool OAIStartDICOMImportJobRequest::is_input_s3_uri_Valid() const{
    return m_input_s3_uri_isValid;
}

QString OAIStartDICOMImportJobRequest::getOutputS3Uri() const {
    return m_output_s3_uri;
}
void OAIStartDICOMImportJobRequest::setOutputS3Uri(const QString &output_s3_uri) {
    m_output_s3_uri = output_s3_uri;
    m_output_s3_uri_isSet = true;
}

bool OAIStartDICOMImportJobRequest::is_output_s3_uri_Set() const{
    return m_output_s3_uri_isSet;
}

bool OAIStartDICOMImportJobRequest::is_output_s3_uri_Valid() const{
    return m_output_s3_uri_isValid;
}

bool OAIStartDICOMImportJobRequest::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_job_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_data_access_role_arn_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_client_token_isSet) {
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
    } while (false);
    return isObjectUpdated;
}

bool OAIStartDICOMImportJobRequest::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_data_access_role_arn_isValid && m_client_token_isValid && m_input_s3_uri_isValid && m_output_s3_uri_isValid && true;
}

} // namespace OpenAPI
