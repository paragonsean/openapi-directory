/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIErrors_DeleteError_200_response.h
 *
 * 
 */

#ifndef OAIErrors_DeleteError_200_response_H
#define OAIErrors_DeleteError_200_response_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIErrors_DeleteError_200_response : public OAIObject {
public:
    OAIErrors_DeleteError_200_response();
    OAIErrors_DeleteError_200_response(QString json);
    ~OAIErrors_DeleteError_200_response() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAppId() const;
    void setAppId(const QString &app_id);
    bool is_app_id_Set() const;
    bool is_app_id_Valid() const;

    qint32 getAttachmentsDeleted() const;
    void setAttachmentsDeleted(const qint32 &attachments_deleted);
    bool is_attachments_deleted_Set() const;
    bool is_attachments_deleted_Valid() const;

    qint32 getBlobsFailed() const;
    void setBlobsFailed(const qint32 &blobs_failed);
    bool is_blobs_failed_Set() const;
    bool is_blobs_failed_Valid() const;

    qint32 getBlobsSucceeded() const;
    void setBlobsSucceeded(const qint32 &blobs_succeeded);
    bool is_blobs_succeeded_Set() const;
    bool is_blobs_succeeded_Valid() const;

    QString getErrorGroupId() const;
    void setErrorGroupId(const QString &error_group_id);
    bool is_error_group_id_Set() const;
    bool is_error_group_id_Valid() const;

    QString getErrorId() const;
    void setErrorId(const QString &error_id);
    bool is_error_id_Set() const;
    bool is_error_id_Valid() const;

    qint32 getErrorsDeleted() const;
    void setErrorsDeleted(const qint32 &errors_deleted);
    bool is_errors_deleted_Set() const;
    bool is_errors_deleted_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_app_id;
    bool m_app_id_isSet;
    bool m_app_id_isValid;

    qint32 m_attachments_deleted;
    bool m_attachments_deleted_isSet;
    bool m_attachments_deleted_isValid;

    qint32 m_blobs_failed;
    bool m_blobs_failed_isSet;
    bool m_blobs_failed_isValid;

    qint32 m_blobs_succeeded;
    bool m_blobs_succeeded_isSet;
    bool m_blobs_succeeded_isValid;

    QString m_error_group_id;
    bool m_error_group_id_isSet;
    bool m_error_group_id_isValid;

    QString m_error_id;
    bool m_error_id_isSet;
    bool m_error_id_isValid;

    qint32 m_errors_deleted;
    bool m_errors_deleted_isSet;
    bool m_errors_deleted_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIErrors_DeleteError_200_response)

#endif // OAIErrors_DeleteError_200_response_H
