/**
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAICreateFileUploadRequest.h
 *
 * Request model for creating an upload channel
 */

#ifndef OAICreateFileUploadRequest_H
#define OAICreateFileUploadRequest_H

#include <QJsonObject>

#include "OAIObjectExpiration.h"
#include <QDateTime>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIObjectExpiration;

class OAICreateFileUploadRequest : public OAIObject {
public:
    OAICreateFileUploadRequest();
    OAICreateFileUploadRequest(QString json);
    ~OAICreateFileUploadRequest() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getClassification() const;
    void setClassification(const qint32 &classification);
    bool is_classification_Set() const;
    bool is_classification_Valid() const;

    bool isDirectS3Upload() const;
    void setDirectS3Upload(const bool &direct_s3_upload);
    bool is_direct_s3_upload_Set() const;
    bool is_direct_s3_upload_Valid() const;

    OAIObjectExpiration getExpiration() const;
    void setExpiration(const OAIObjectExpiration &expiration);
    bool is_expiration_Set() const;
    bool is_expiration_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getNotes() const;
    void setNotes(const QString &notes);
    bool is_notes_Set() const;
    bool is_notes_Valid() const;

    qint64 getParentId() const;
    void setParentId(const qint64 &parent_id);
    bool is_parent_id_Set() const;
    bool is_parent_id_Valid() const;

    qint64 getSize() const;
    void setSize(const qint64 &size);
    bool is_size_Set() const;
    bool is_size_Valid() const;

    QDateTime getTimestampCreation() const;
    void setTimestampCreation(const QDateTime &timestamp_creation);
    bool is_timestamp_creation_Set() const;
    bool is_timestamp_creation_Valid() const;

    QDateTime getTimestampModification() const;
    void setTimestampModification(const QDateTime &timestamp_modification);
    bool is_timestamp_modification_Set() const;
    bool is_timestamp_modification_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_classification;
    bool m_classification_isSet;
    bool m_classification_isValid;

    bool m_direct_s3_upload;
    bool m_direct_s3_upload_isSet;
    bool m_direct_s3_upload_isValid;

    OAIObjectExpiration m_expiration;
    bool m_expiration_isSet;
    bool m_expiration_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_notes;
    bool m_notes_isSet;
    bool m_notes_isValid;

    qint64 m_parent_id;
    bool m_parent_id_isSet;
    bool m_parent_id_isValid;

    qint64 m_size;
    bool m_size_isSet;
    bool m_size_isValid;

    QDateTime m_timestamp_creation;
    bool m_timestamp_creation_isSet;
    bool m_timestamp_creation_isValid;

    QDateTime m_timestamp_modification;
    bool m_timestamp_modification_isSet;
    bool m_timestamp_modification_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICreateFileUploadRequest)

#endif // OAICreateFileUploadRequest_H
