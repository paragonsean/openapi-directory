/**
 * Google Pay Passes API
 * API for issuers to save and manage Google Wallet Objects.
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAICallbackOptions.h
 *
 * 
 */

#ifndef OAICallbackOptions_H
#define OAICallbackOptions_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAICallbackOptions : public OAIObject {
public:
    OAICallbackOptions();
    OAICallbackOptions(QString json);
    ~OAICallbackOptions() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getUpdateRequestUrl() const;
    void setUpdateRequestUrl(const QString &update_request_url);
    bool is_update_request_url_Set() const;
    bool is_update_request_url_Valid() const;

    QString getUrl() const;
    void setUrl(const QString &url);
    bool is_url_Set() const;
    bool is_url_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_update_request_url;
    bool m_update_request_url_isSet;
    bool m_update_request_url_isValid;

    QString m_url;
    bool m_url_isSet;
    bool m_url_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICallbackOptions)

#endif // OAICallbackOptions_H
