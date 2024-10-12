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

/*
 * OAIImageSetsMetadataSummary_DICOMTags.h
 *
 * 
 */

#ifndef OAIImageSetsMetadataSummary_DICOMTags_H
#define OAIImageSetsMetadataSummary_DICOMTags_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIImageSetsMetadataSummary_DICOMTags : public OAIObject {
public:
    OAIImageSetsMetadataSummary_DICOMTags();
    OAIImageSetsMetadataSummary_DICOMTags(QString json);
    ~OAIImageSetsMetadataSummary_DICOMTags() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getDicomPatientId() const;
    void setDicomPatientId(const QString &dicom_patient_id);
    bool is_dicom_patient_id_Set() const;
    bool is_dicom_patient_id_Valid() const;

    QString getDicomPatientName() const;
    void setDicomPatientName(const QString &dicom_patient_name);
    bool is_dicom_patient_name_Set() const;
    bool is_dicom_patient_name_Valid() const;

    QString getDicomPatientBirthDate() const;
    void setDicomPatientBirthDate(const QString &dicom_patient_birth_date);
    bool is_dicom_patient_birth_date_Set() const;
    bool is_dicom_patient_birth_date_Valid() const;

    QString getDicomPatientSex() const;
    void setDicomPatientSex(const QString &dicom_patient_sex);
    bool is_dicom_patient_sex_Set() const;
    bool is_dicom_patient_sex_Valid() const;

    QString getDicomStudyInstanceUid() const;
    void setDicomStudyInstanceUid(const QString &dicom_study_instance_uid);
    bool is_dicom_study_instance_uid_Set() const;
    bool is_dicom_study_instance_uid_Valid() const;

    QString getDicomStudyId() const;
    void setDicomStudyId(const QString &dicom_study_id);
    bool is_dicom_study_id_Set() const;
    bool is_dicom_study_id_Valid() const;

    QString getDicomStudyDescription() const;
    void setDicomStudyDescription(const QString &dicom_study_description);
    bool is_dicom_study_description_Set() const;
    bool is_dicom_study_description_Valid() const;

    qint32 getDicomNumberOfStudyRelatedSeries() const;
    void setDicomNumberOfStudyRelatedSeries(const qint32 &dicom_number_of_study_related_series);
    bool is_dicom_number_of_study_related_series_Set() const;
    bool is_dicom_number_of_study_related_series_Valid() const;

    qint32 getDicomNumberOfStudyRelatedInstances() const;
    void setDicomNumberOfStudyRelatedInstances(const qint32 &dicom_number_of_study_related_instances);
    bool is_dicom_number_of_study_related_instances_Set() const;
    bool is_dicom_number_of_study_related_instances_Valid() const;

    QString getDicomAccessionNumber() const;
    void setDicomAccessionNumber(const QString &dicom_accession_number);
    bool is_dicom_accession_number_Set() const;
    bool is_dicom_accession_number_Valid() const;

    QString getDicomStudyDate() const;
    void setDicomStudyDate(const QString &dicom_study_date);
    bool is_dicom_study_date_Set() const;
    bool is_dicom_study_date_Valid() const;

    QString getDicomStudyTime() const;
    void setDicomStudyTime(const QString &dicom_study_time);
    bool is_dicom_study_time_Set() const;
    bool is_dicom_study_time_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_dicom_patient_id;
    bool m_dicom_patient_id_isSet;
    bool m_dicom_patient_id_isValid;

    QString m_dicom_patient_name;
    bool m_dicom_patient_name_isSet;
    bool m_dicom_patient_name_isValid;

    QString m_dicom_patient_birth_date;
    bool m_dicom_patient_birth_date_isSet;
    bool m_dicom_patient_birth_date_isValid;

    QString m_dicom_patient_sex;
    bool m_dicom_patient_sex_isSet;
    bool m_dicom_patient_sex_isValid;

    QString m_dicom_study_instance_uid;
    bool m_dicom_study_instance_uid_isSet;
    bool m_dicom_study_instance_uid_isValid;

    QString m_dicom_study_id;
    bool m_dicom_study_id_isSet;
    bool m_dicom_study_id_isValid;

    QString m_dicom_study_description;
    bool m_dicom_study_description_isSet;
    bool m_dicom_study_description_isValid;

    qint32 m_dicom_number_of_study_related_series;
    bool m_dicom_number_of_study_related_series_isSet;
    bool m_dicom_number_of_study_related_series_isValid;

    qint32 m_dicom_number_of_study_related_instances;
    bool m_dicom_number_of_study_related_instances_isSet;
    bool m_dicom_number_of_study_related_instances_isValid;

    QString m_dicom_accession_number;
    bool m_dicom_accession_number_isSet;
    bool m_dicom_accession_number_isValid;

    QString m_dicom_study_date;
    bool m_dicom_study_date_isSet;
    bool m_dicom_study_date_isValid;

    QString m_dicom_study_time;
    bool m_dicom_study_time_isSet;
    bool m_dicom_study_time_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIImageSetsMetadataSummary_DICOMTags)

#endif // OAIImageSetsMetadataSummary_DICOMTags_H
