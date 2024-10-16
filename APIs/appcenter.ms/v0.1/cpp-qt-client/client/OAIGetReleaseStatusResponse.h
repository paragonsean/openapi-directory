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
 * OAIGetReleaseStatusResponse.h
 *
 * 
 */

#ifndef OAIGetReleaseStatusResponse_H
#define OAIGetReleaseStatusResponse_H

#include <QJsonObject>

#include <QJsonValue>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIGetReleaseStatusResponse : public OAIObject {
public:
    OAIGetReleaseStatusResponse();
    OAIGetReleaseStatusResponse(QString json);
    ~OAIGetReleaseStatusResponse() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getErrorDetails() const;
    void setErrorDetails(const QString &error_details);
    bool is_error_details_Set() const;
    bool is_error_details_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    double getReleaseDistinctId() const;
    void setReleaseDistinctId(const double &release_distinct_id);
    bool is_release_distinct_id_Set() const;
    bool is_release_distinct_id_Valid() const;

    QJsonValue getReleaseUrl() const;
    void setReleaseUrl(const QJsonValue &release_url);
    bool is_release_url_Set() const;
    bool is_release_url_Valid() const;

    QString getUploadStatus() const;
    void setUploadStatus(const QString &upload_status);
    bool is_upload_status_Set() const;
    bool is_upload_status_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_error_details;
    bool m_error_details_isSet;
    bool m_error_details_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    double m_release_distinct_id;
    bool m_release_distinct_id_isSet;
    bool m_release_distinct_id_isValid;

    QJsonValue m_release_url;
    bool m_release_url_isSet;
    bool m_release_url_isValid;

    QString m_upload_status;
    bool m_upload_status_isSet;
    bool m_upload_status_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGetReleaseStatusResponse)

#endif // OAIGetReleaseStatusResponse_H
