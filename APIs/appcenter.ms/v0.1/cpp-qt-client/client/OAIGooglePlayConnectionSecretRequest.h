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
 * OAIGooglePlayConnectionSecretRequest.h
 *
 * Google Play connection secrets this should be the JSON file data which is provided by google play
 */

#ifndef OAIGooglePlayConnectionSecretRequest_H
#define OAIGooglePlayConnectionSecretRequest_H

#include <QJsonObject>

#include "OAIObject.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIGooglePlayConnectionSecretRequest : public OAIObject {
public:
    OAIGooglePlayConnectionSecretRequest();
    OAIGooglePlayConnectionSecretRequest(QString json);
    ~OAIGooglePlayConnectionSecretRequest() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIObject getData() const;
    void setData(const OAIObject &data);
    bool is_data_Set() const;
    bool is_data_Valid() const;

    QString getCredentialType() const;
    void setCredentialType(const QString &credential_type);
    bool is_credential_type_Set() const;
    bool is_credential_type_Valid() const;

    QString getDisplayName() const;
    void setDisplayName(const QString &display_name);
    bool is_display_name_Set() const;
    bool is_display_name_Valid() const;

    QString getServiceType() const;
    void setServiceType(const QString &service_type);
    bool is_service_type_Set() const;
    bool is_service_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIObject m_data;
    bool m_data_isSet;
    bool m_data_isValid;

    QString m_credential_type;
    bool m_credential_type_isSet;
    bool m_credential_type_isValid;

    QString m_display_name;
    bool m_display_name_isSet;
    bool m_display_name_isValid;

    QString m_service_type;
    bool m_service_type_isSet;
    bool m_service_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGooglePlayConnectionSecretRequest)

#endif // OAIGooglePlayConnectionSecretRequest_H
