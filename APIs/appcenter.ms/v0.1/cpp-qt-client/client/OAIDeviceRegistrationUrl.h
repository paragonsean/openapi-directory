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
 * OAIDeviceRegistrationUrl.h
 *
 * The url that can be navigated to in order to start the device registration process.
 */

#ifndef OAIDeviceRegistrationUrl_H
#define OAIDeviceRegistrationUrl_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIDeviceRegistrationUrl : public OAIObject {
public:
    OAIDeviceRegistrationUrl();
    OAIDeviceRegistrationUrl(QString json);
    ~OAIDeviceRegistrationUrl() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getRegistrationUrl() const;
    void setRegistrationUrl(const QString &registration_url);
    bool is_registration_url_Set() const;
    bool is_registration_url_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_registration_url;
    bool m_registration_url_isSet;
    bool m_registration_url_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIDeviceRegistrationUrl)

#endif // OAIDeviceRegistrationUrl_H
