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

#include "OAIImageSetsMetadataSummary_DICOMTags.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIImageSetsMetadataSummary_DICOMTags::OAIImageSetsMetadataSummary_DICOMTags(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIImageSetsMetadataSummary_DICOMTags::OAIImageSetsMetadataSummary_DICOMTags() {
    this->initializeModel();
}

OAIImageSetsMetadataSummary_DICOMTags::~OAIImageSetsMetadataSummary_DICOMTags() {}

void OAIImageSetsMetadataSummary_DICOMTags::initializeModel() {

    m_dicom_patient_id_isSet = false;
    m_dicom_patient_id_isValid = false;

    m_dicom_patient_name_isSet = false;
    m_dicom_patient_name_isValid = false;

    m_dicom_patient_birth_date_isSet = false;
    m_dicom_patient_birth_date_isValid = false;

    m_dicom_patient_sex_isSet = false;
    m_dicom_patient_sex_isValid = false;

    m_dicom_study_instance_uid_isSet = false;
    m_dicom_study_instance_uid_isValid = false;

    m_dicom_study_id_isSet = false;
    m_dicom_study_id_isValid = false;

    m_dicom_study_description_isSet = false;
    m_dicom_study_description_isValid = false;

    m_dicom_number_of_study_related_series_isSet = false;
    m_dicom_number_of_study_related_series_isValid = false;

    m_dicom_number_of_study_related_instances_isSet = false;
    m_dicom_number_of_study_related_instances_isValid = false;

    m_dicom_accession_number_isSet = false;
    m_dicom_accession_number_isValid = false;

    m_dicom_study_date_isSet = false;
    m_dicom_study_date_isValid = false;

    m_dicom_study_time_isSet = false;
    m_dicom_study_time_isValid = false;
}

void OAIImageSetsMetadataSummary_DICOMTags::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIImageSetsMetadataSummary_DICOMTags::fromJsonObject(QJsonObject json) {

    m_dicom_patient_id_isValid = ::OpenAPI::fromJsonValue(m_dicom_patient_id, json[QString("DICOMPatientId")]);
    m_dicom_patient_id_isSet = !json[QString("DICOMPatientId")].isNull() && m_dicom_patient_id_isValid;

    m_dicom_patient_name_isValid = ::OpenAPI::fromJsonValue(m_dicom_patient_name, json[QString("DICOMPatientName")]);
    m_dicom_patient_name_isSet = !json[QString("DICOMPatientName")].isNull() && m_dicom_patient_name_isValid;

    m_dicom_patient_birth_date_isValid = ::OpenAPI::fromJsonValue(m_dicom_patient_birth_date, json[QString("DICOMPatientBirthDate")]);
    m_dicom_patient_birth_date_isSet = !json[QString("DICOMPatientBirthDate")].isNull() && m_dicom_patient_birth_date_isValid;

    m_dicom_patient_sex_isValid = ::OpenAPI::fromJsonValue(m_dicom_patient_sex, json[QString("DICOMPatientSex")]);
    m_dicom_patient_sex_isSet = !json[QString("DICOMPatientSex")].isNull() && m_dicom_patient_sex_isValid;

    m_dicom_study_instance_uid_isValid = ::OpenAPI::fromJsonValue(m_dicom_study_instance_uid, json[QString("DICOMStudyInstanceUID")]);
    m_dicom_study_instance_uid_isSet = !json[QString("DICOMStudyInstanceUID")].isNull() && m_dicom_study_instance_uid_isValid;

    m_dicom_study_id_isValid = ::OpenAPI::fromJsonValue(m_dicom_study_id, json[QString("DICOMStudyId")]);
    m_dicom_study_id_isSet = !json[QString("DICOMStudyId")].isNull() && m_dicom_study_id_isValid;

    m_dicom_study_description_isValid = ::OpenAPI::fromJsonValue(m_dicom_study_description, json[QString("DICOMStudyDescription")]);
    m_dicom_study_description_isSet = !json[QString("DICOMStudyDescription")].isNull() && m_dicom_study_description_isValid;

    m_dicom_number_of_study_related_series_isValid = ::OpenAPI::fromJsonValue(m_dicom_number_of_study_related_series, json[QString("DICOMNumberOfStudyRelatedSeries")]);
    m_dicom_number_of_study_related_series_isSet = !json[QString("DICOMNumberOfStudyRelatedSeries")].isNull() && m_dicom_number_of_study_related_series_isValid;

    m_dicom_number_of_study_related_instances_isValid = ::OpenAPI::fromJsonValue(m_dicom_number_of_study_related_instances, json[QString("DICOMNumberOfStudyRelatedInstances")]);
    m_dicom_number_of_study_related_instances_isSet = !json[QString("DICOMNumberOfStudyRelatedInstances")].isNull() && m_dicom_number_of_study_related_instances_isValid;

    m_dicom_accession_number_isValid = ::OpenAPI::fromJsonValue(m_dicom_accession_number, json[QString("DICOMAccessionNumber")]);
    m_dicom_accession_number_isSet = !json[QString("DICOMAccessionNumber")].isNull() && m_dicom_accession_number_isValid;

    m_dicom_study_date_isValid = ::OpenAPI::fromJsonValue(m_dicom_study_date, json[QString("DICOMStudyDate")]);
    m_dicom_study_date_isSet = !json[QString("DICOMStudyDate")].isNull() && m_dicom_study_date_isValid;

    m_dicom_study_time_isValid = ::OpenAPI::fromJsonValue(m_dicom_study_time, json[QString("DICOMStudyTime")]);
    m_dicom_study_time_isSet = !json[QString("DICOMStudyTime")].isNull() && m_dicom_study_time_isValid;
}

QString OAIImageSetsMetadataSummary_DICOMTags::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIImageSetsMetadataSummary_DICOMTags::asJsonObject() const {
    QJsonObject obj;
    if (m_dicom_patient_id_isSet) {
        obj.insert(QString("DICOMPatientId"), ::OpenAPI::toJsonValue(m_dicom_patient_id));
    }
    if (m_dicom_patient_name_isSet) {
        obj.insert(QString("DICOMPatientName"), ::OpenAPI::toJsonValue(m_dicom_patient_name));
    }
    if (m_dicom_patient_birth_date_isSet) {
        obj.insert(QString("DICOMPatientBirthDate"), ::OpenAPI::toJsonValue(m_dicom_patient_birth_date));
    }
    if (m_dicom_patient_sex_isSet) {
        obj.insert(QString("DICOMPatientSex"), ::OpenAPI::toJsonValue(m_dicom_patient_sex));
    }
    if (m_dicom_study_instance_uid_isSet) {
        obj.insert(QString("DICOMStudyInstanceUID"), ::OpenAPI::toJsonValue(m_dicom_study_instance_uid));
    }
    if (m_dicom_study_id_isSet) {
        obj.insert(QString("DICOMStudyId"), ::OpenAPI::toJsonValue(m_dicom_study_id));
    }
    if (m_dicom_study_description_isSet) {
        obj.insert(QString("DICOMStudyDescription"), ::OpenAPI::toJsonValue(m_dicom_study_description));
    }
    if (m_dicom_number_of_study_related_series_isSet) {
        obj.insert(QString("DICOMNumberOfStudyRelatedSeries"), ::OpenAPI::toJsonValue(m_dicom_number_of_study_related_series));
    }
    if (m_dicom_number_of_study_related_instances_isSet) {
        obj.insert(QString("DICOMNumberOfStudyRelatedInstances"), ::OpenAPI::toJsonValue(m_dicom_number_of_study_related_instances));
    }
    if (m_dicom_accession_number_isSet) {
        obj.insert(QString("DICOMAccessionNumber"), ::OpenAPI::toJsonValue(m_dicom_accession_number));
    }
    if (m_dicom_study_date_isSet) {
        obj.insert(QString("DICOMStudyDate"), ::OpenAPI::toJsonValue(m_dicom_study_date));
    }
    if (m_dicom_study_time_isSet) {
        obj.insert(QString("DICOMStudyTime"), ::OpenAPI::toJsonValue(m_dicom_study_time));
    }
    return obj;
}

QString OAIImageSetsMetadataSummary_DICOMTags::getDicomPatientId() const {
    return m_dicom_patient_id;
}
void OAIImageSetsMetadataSummary_DICOMTags::setDicomPatientId(const QString &dicom_patient_id) {
    m_dicom_patient_id = dicom_patient_id;
    m_dicom_patient_id_isSet = true;
}

bool OAIImageSetsMetadataSummary_DICOMTags::is_dicom_patient_id_Set() const{
    return m_dicom_patient_id_isSet;
}

bool OAIImageSetsMetadataSummary_DICOMTags::is_dicom_patient_id_Valid() const{
    return m_dicom_patient_id_isValid;
}

QString OAIImageSetsMetadataSummary_DICOMTags::getDicomPatientName() const {
    return m_dicom_patient_name;
}
void OAIImageSetsMetadataSummary_DICOMTags::setDicomPatientName(const QString &dicom_patient_name) {
    m_dicom_patient_name = dicom_patient_name;
    m_dicom_patient_name_isSet = true;
}

bool OAIImageSetsMetadataSummary_DICOMTags::is_dicom_patient_name_Set() const{
    return m_dicom_patient_name_isSet;
}

bool OAIImageSetsMetadataSummary_DICOMTags::is_dicom_patient_name_Valid() const{
    return m_dicom_patient_name_isValid;
}

QString OAIImageSetsMetadataSummary_DICOMTags::getDicomPatientBirthDate() const {
    return m_dicom_patient_birth_date;
}
void OAIImageSetsMetadataSummary_DICOMTags::setDicomPatientBirthDate(const QString &dicom_patient_birth_date) {
    m_dicom_patient_birth_date = dicom_patient_birth_date;
    m_dicom_patient_birth_date_isSet = true;
}

bool OAIImageSetsMetadataSummary_DICOMTags::is_dicom_patient_birth_date_Set() const{
    return m_dicom_patient_birth_date_isSet;
}

bool OAIImageSetsMetadataSummary_DICOMTags::is_dicom_patient_birth_date_Valid() const{
    return m_dicom_patient_birth_date_isValid;
}

QString OAIImageSetsMetadataSummary_DICOMTags::getDicomPatientSex() const {
    return m_dicom_patient_sex;
}
void OAIImageSetsMetadataSummary_DICOMTags::setDicomPatientSex(const QString &dicom_patient_sex) {
    m_dicom_patient_sex = dicom_patient_sex;
    m_dicom_patient_sex_isSet = true;
}

bool OAIImageSetsMetadataSummary_DICOMTags::is_dicom_patient_sex_Set() const{
    return m_dicom_patient_sex_isSet;
}

bool OAIImageSetsMetadataSummary_DICOMTags::is_dicom_patient_sex_Valid() const{
    return m_dicom_patient_sex_isValid;
}

QString OAIImageSetsMetadataSummary_DICOMTags::getDicomStudyInstanceUid() const {
    return m_dicom_study_instance_uid;
}
void OAIImageSetsMetadataSummary_DICOMTags::setDicomStudyInstanceUid(const QString &dicom_study_instance_uid) {
    m_dicom_study_instance_uid = dicom_study_instance_uid;
    m_dicom_study_instance_uid_isSet = true;
}

bool OAIImageSetsMetadataSummary_DICOMTags::is_dicom_study_instance_uid_Set() const{
    return m_dicom_study_instance_uid_isSet;
}

bool OAIImageSetsMetadataSummary_DICOMTags::is_dicom_study_instance_uid_Valid() const{
    return m_dicom_study_instance_uid_isValid;
}

QString OAIImageSetsMetadataSummary_DICOMTags::getDicomStudyId() const {
    return m_dicom_study_id;
}
void OAIImageSetsMetadataSummary_DICOMTags::setDicomStudyId(const QString &dicom_study_id) {
    m_dicom_study_id = dicom_study_id;
    m_dicom_study_id_isSet = true;
}

bool OAIImageSetsMetadataSummary_DICOMTags::is_dicom_study_id_Set() const{
    return m_dicom_study_id_isSet;
}

bool OAIImageSetsMetadataSummary_DICOMTags::is_dicom_study_id_Valid() const{
    return m_dicom_study_id_isValid;
}

QString OAIImageSetsMetadataSummary_DICOMTags::getDicomStudyDescription() const {
    return m_dicom_study_description;
}
void OAIImageSetsMetadataSummary_DICOMTags::setDicomStudyDescription(const QString &dicom_study_description) {
    m_dicom_study_description = dicom_study_description;
    m_dicom_study_description_isSet = true;
}

bool OAIImageSetsMetadataSummary_DICOMTags::is_dicom_study_description_Set() const{
    return m_dicom_study_description_isSet;
}

bool OAIImageSetsMetadataSummary_DICOMTags::is_dicom_study_description_Valid() const{
    return m_dicom_study_description_isValid;
}

qint32 OAIImageSetsMetadataSummary_DICOMTags::getDicomNumberOfStudyRelatedSeries() const {
    return m_dicom_number_of_study_related_series;
}
void OAIImageSetsMetadataSummary_DICOMTags::setDicomNumberOfStudyRelatedSeries(const qint32 &dicom_number_of_study_related_series) {
    m_dicom_number_of_study_related_series = dicom_number_of_study_related_series;
    m_dicom_number_of_study_related_series_isSet = true;
}

bool OAIImageSetsMetadataSummary_DICOMTags::is_dicom_number_of_study_related_series_Set() const{
    return m_dicom_number_of_study_related_series_isSet;
}

bool OAIImageSetsMetadataSummary_DICOMTags::is_dicom_number_of_study_related_series_Valid() const{
    return m_dicom_number_of_study_related_series_isValid;
}

qint32 OAIImageSetsMetadataSummary_DICOMTags::getDicomNumberOfStudyRelatedInstances() const {
    return m_dicom_number_of_study_related_instances;
}
void OAIImageSetsMetadataSummary_DICOMTags::setDicomNumberOfStudyRelatedInstances(const qint32 &dicom_number_of_study_related_instances) {
    m_dicom_number_of_study_related_instances = dicom_number_of_study_related_instances;
    m_dicom_number_of_study_related_instances_isSet = true;
}

bool OAIImageSetsMetadataSummary_DICOMTags::is_dicom_number_of_study_related_instances_Set() const{
    return m_dicom_number_of_study_related_instances_isSet;
}

bool OAIImageSetsMetadataSummary_DICOMTags::is_dicom_number_of_study_related_instances_Valid() const{
    return m_dicom_number_of_study_related_instances_isValid;
}

QString OAIImageSetsMetadataSummary_DICOMTags::getDicomAccessionNumber() const {
    return m_dicom_accession_number;
}
void OAIImageSetsMetadataSummary_DICOMTags::setDicomAccessionNumber(const QString &dicom_accession_number) {
    m_dicom_accession_number = dicom_accession_number;
    m_dicom_accession_number_isSet = true;
}

bool OAIImageSetsMetadataSummary_DICOMTags::is_dicom_accession_number_Set() const{
    return m_dicom_accession_number_isSet;
}

bool OAIImageSetsMetadataSummary_DICOMTags::is_dicom_accession_number_Valid() const{
    return m_dicom_accession_number_isValid;
}

QString OAIImageSetsMetadataSummary_DICOMTags::getDicomStudyDate() const {
    return m_dicom_study_date;
}
void OAIImageSetsMetadataSummary_DICOMTags::setDicomStudyDate(const QString &dicom_study_date) {
    m_dicom_study_date = dicom_study_date;
    m_dicom_study_date_isSet = true;
}

bool OAIImageSetsMetadataSummary_DICOMTags::is_dicom_study_date_Set() const{
    return m_dicom_study_date_isSet;
}

bool OAIImageSetsMetadataSummary_DICOMTags::is_dicom_study_date_Valid() const{
    return m_dicom_study_date_isValid;
}

QString OAIImageSetsMetadataSummary_DICOMTags::getDicomStudyTime() const {
    return m_dicom_study_time;
}
void OAIImageSetsMetadataSummary_DICOMTags::setDicomStudyTime(const QString &dicom_study_time) {
    m_dicom_study_time = dicom_study_time;
    m_dicom_study_time_isSet = true;
}

bool OAIImageSetsMetadataSummary_DICOMTags::is_dicom_study_time_Set() const{
    return m_dicom_study_time_isSet;
}

bool OAIImageSetsMetadataSummary_DICOMTags::is_dicom_study_time_Valid() const{
    return m_dicom_study_time_isValid;
}

bool OAIImageSetsMetadataSummary_DICOMTags::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_dicom_patient_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dicom_patient_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dicom_patient_birth_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dicom_patient_sex_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dicom_study_instance_uid_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dicom_study_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dicom_study_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dicom_number_of_study_related_series_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dicom_number_of_study_related_instances_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dicom_accession_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dicom_study_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dicom_study_time_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIImageSetsMetadataSummary_DICOMTags::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
