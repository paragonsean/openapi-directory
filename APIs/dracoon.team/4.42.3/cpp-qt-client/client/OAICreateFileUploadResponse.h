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
 * OAICreateFileUploadResponse.h
 *
 * Upload channel information
 */

#ifndef OAICreateFileUploadResponse_H
#define OAICreateFileUploadResponse_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAICreateFileUploadResponse : public OAIObject {
public:
    OAICreateFileUploadResponse();
    OAICreateFileUploadResponse(QString json);
    ~OAICreateFileUploadResponse() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getToken() const;
    void setToken(const QString &token);
    bool is_token_Set() const;
    bool is_token_Valid() const;

    QString getUploadId() const;
    void setUploadId(const QString &upload_id);
    bool is_upload_id_Set() const;
    bool is_upload_id_Valid() const;

    QString getUploadUrl() const;
    void setUploadUrl(const QString &upload_url);
    bool is_upload_url_Set() const;
    bool is_upload_url_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_token;
    bool m_token_isSet;
    bool m_token_isValid;

    QString m_upload_id;
    bool m_upload_id_isSet;
    bool m_upload_id_isValid;

    QString m_upload_url;
    bool m_upload_url_isSet;
    bool m_upload_url_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICreateFileUploadResponse)

#endif // OAICreateFileUploadResponse_H
