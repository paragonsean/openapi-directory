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
 * OAIPublicDownloadTokenGenerateResponse.h
 *
 * Download URL
 */

#ifndef OAIPublicDownloadTokenGenerateResponse_H
#define OAIPublicDownloadTokenGenerateResponse_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIPublicDownloadTokenGenerateResponse : public OAIObject {
public:
    OAIPublicDownloadTokenGenerateResponse();
    OAIPublicDownloadTokenGenerateResponse(QString json);
    ~OAIPublicDownloadTokenGenerateResponse() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getDownloadUrl() const;
    void setDownloadUrl(const QString &download_url);
    bool is_download_url_Set() const;
    bool is_download_url_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_download_url;
    bool m_download_url_isSet;
    bool m_download_url_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPublicDownloadTokenGenerateResponse)

#endif // OAIPublicDownloadTokenGenerateResponse_H
