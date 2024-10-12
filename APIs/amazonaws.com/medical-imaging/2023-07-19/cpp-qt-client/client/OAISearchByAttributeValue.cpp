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

#include "OAISearchByAttributeValue.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISearchByAttributeValue::OAISearchByAttributeValue(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISearchByAttributeValue::OAISearchByAttributeValue() {
    this->initializeModel();
}

OAISearchByAttributeValue::~OAISearchByAttributeValue() {}

void OAISearchByAttributeValue::initializeModel() {

    m_dicom_patient_id_isSet = false;
    m_dicom_patient_id_isValid = false;

    m_dicom_accession_number_isSet = false;
    m_dicom_accession_number_isValid = false;

    m_dicom_study_id_isSet = false;
    m_dicom_study_id_isValid = false;

    m_dicom_study_instance_uid_isSet = false;
    m_dicom_study_instance_uid_isValid = false;

    m_created_at_isSet = false;
    m_created_at_isValid = false;

    m_dicom_study_date_and_time_isSet = false;
    m_dicom_study_date_and_time_isValid = false;
}

void OAISearchByAttributeValue::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISearchByAttributeValue::fromJsonObject(QJsonObject json) {

    m_dicom_patient_id_isValid = ::OpenAPI::fromJsonValue(m_dicom_patient_id, json[QString("DICOMPatientId")]);
    m_dicom_patient_id_isSet = !json[QString("DICOMPatientId")].isNull() && m_dicom_patient_id_isValid;

    m_dicom_accession_number_isValid = ::OpenAPI::fromJsonValue(m_dicom_accession_number, json[QString("DICOMAccessionNumber")]);
    m_dicom_accession_number_isSet = !json[QString("DICOMAccessionNumber")].isNull() && m_dicom_accession_number_isValid;

    m_dicom_study_id_isValid = ::OpenAPI::fromJsonValue(m_dicom_study_id, json[QString("DICOMStudyId")]);
    m_dicom_study_id_isSet = !json[QString("DICOMStudyId")].isNull() && m_dicom_study_id_isValid;

    m_dicom_study_instance_uid_isValid = ::OpenAPI::fromJsonValue(m_dicom_study_instance_uid, json[QString("DICOMStudyInstanceUID")]);
    m_dicom_study_instance_uid_isSet = !json[QString("DICOMStudyInstanceUID")].isNull() && m_dicom_study_instance_uid_isValid;

    m_created_at_isValid = ::OpenAPI::fromJsonValue(m_created_at, json[QString("createdAt")]);
    m_created_at_isSet = !json[QString("createdAt")].isNull() && m_created_at_isValid;

    m_dicom_study_date_and_time_isValid = ::OpenAPI::fromJsonValue(m_dicom_study_date_and_time, json[QString("DICOMStudyDateAndTime")]);
    m_dicom_study_date_and_time_isSet = !json[QString("DICOMStudyDateAndTime")].isNull() && m_dicom_study_date_and_time_isValid;
}

QString OAISearchByAttributeValue::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISearchByAttributeValue::asJsonObject() const {
    QJsonObject obj;
    if (m_dicom_patient_id_isSet) {
        obj.insert(QString("DICOMPatientId"), ::OpenAPI::toJsonValue(m_dicom_patient_id));
    }
    if (m_dicom_accession_number_isSet) {
        obj.insert(QString("DICOMAccessionNumber"), ::OpenAPI::toJsonValue(m_dicom_accession_number));
    }
    if (m_dicom_study_id_isSet) {
        obj.insert(QString("DICOMStudyId"), ::OpenAPI::toJsonValue(m_dicom_study_id));
    }
    if (m_dicom_study_instance_uid_isSet) {
        obj.insert(QString("DICOMStudyInstanceUID"), ::OpenAPI::toJsonValue(m_dicom_study_instance_uid));
    }
    if (m_created_at_isSet) {
        obj.insert(QString("createdAt"), ::OpenAPI::toJsonValue(m_created_at));
    }
    if (m_dicom_study_date_and_time.isSet()) {
        obj.insert(QString("DICOMStudyDateAndTime"), ::OpenAPI::toJsonValue(m_dicom_study_date_and_time));
    }
    return obj;
}

QString OAISearchByAttributeValue::getDicomPatientId() const {
    return m_dicom_patient_id;
}
void OAISearchByAttributeValue::setDicomPatientId(const QString &dicom_patient_id) {
    m_dicom_patient_id = dicom_patient_id;
    m_dicom_patient_id_isSet = true;
}

bool OAISearchByAttributeValue::is_dicom_patient_id_Set() const{
    return m_dicom_patient_id_isSet;
}

bool OAISearchByAttributeValue::is_dicom_patient_id_Valid() const{
    return m_dicom_patient_id_isValid;
}

QString OAISearchByAttributeValue::getDicomAccessionNumber() const {
    return m_dicom_accession_number;
}
void OAISearchByAttributeValue::setDicomAccessionNumber(const QString &dicom_accession_number) {
    m_dicom_accession_number = dicom_accession_number;
    m_dicom_accession_number_isSet = true;
}

bool OAISearchByAttributeValue::is_dicom_accession_number_Set() const{
    return m_dicom_accession_number_isSet;
}

bool OAISearchByAttributeValue::is_dicom_accession_number_Valid() const{
    return m_dicom_accession_number_isValid;
}

QString OAISearchByAttributeValue::getDicomStudyId() const {
    return m_dicom_study_id;
}
void OAISearchByAttributeValue::setDicomStudyId(const QString &dicom_study_id) {
    m_dicom_study_id = dicom_study_id;
    m_dicom_study_id_isSet = true;
}

bool OAISearchByAttributeValue::is_dicom_study_id_Set() const{
    return m_dicom_study_id_isSet;
}

bool OAISearchByAttributeValue::is_dicom_study_id_Valid() const{
    return m_dicom_study_id_isValid;
}

QString OAISearchByAttributeValue::getDicomStudyInstanceUid() const {
    return m_dicom_study_instance_uid;
}
void OAISearchByAttributeValue::setDicomStudyInstanceUid(const QString &dicom_study_instance_uid) {
    m_dicom_study_instance_uid = dicom_study_instance_uid;
    m_dicom_study_instance_uid_isSet = true;
}

bool OAISearchByAttributeValue::is_dicom_study_instance_uid_Set() const{
    return m_dicom_study_instance_uid_isSet;
}

bool OAISearchByAttributeValue::is_dicom_study_instance_uid_Valid() const{
    return m_dicom_study_instance_uid_isValid;
}

QDateTime OAISearchByAttributeValue::getCreatedAt() const {
    return m_created_at;
}
void OAISearchByAttributeValue::setCreatedAt(const QDateTime &created_at) {
    m_created_at = created_at;
    m_created_at_isSet = true;
}

bool OAISearchByAttributeValue::is_created_at_Set() const{
    return m_created_at_isSet;
}

bool OAISearchByAttributeValue::is_created_at_Valid() const{
    return m_created_at_isValid;
}

OAISearchByAttributeValue_DICOMStudyDateAndTime OAISearchByAttributeValue::getDicomStudyDateAndTime() const {
    return m_dicom_study_date_and_time;
}
void OAISearchByAttributeValue::setDicomStudyDateAndTime(const OAISearchByAttributeValue_DICOMStudyDateAndTime &dicom_study_date_and_time) {
    m_dicom_study_date_and_time = dicom_study_date_and_time;
    m_dicom_study_date_and_time_isSet = true;
}

bool OAISearchByAttributeValue::is_dicom_study_date_and_time_Set() const{
    return m_dicom_study_date_and_time_isSet;
}

bool OAISearchByAttributeValue::is_dicom_study_date_and_time_Valid() const{
    return m_dicom_study_date_and_time_isValid;
}

bool OAISearchByAttributeValue::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_dicom_patient_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dicom_accession_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dicom_study_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dicom_study_instance_uid_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dicom_study_date_and_time.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISearchByAttributeValue::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
