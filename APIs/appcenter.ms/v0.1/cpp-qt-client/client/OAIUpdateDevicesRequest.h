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
 * OAIUpdateDevicesRequest.h
 *
 * Information required to publish devices to the Apple Developer account and resign the application.
 */

#ifndef OAIUpdateDevicesRequest_H
#define OAIUpdateDevicesRequest_H

#include <QJsonObject>

#include "OAIUpdateDevicesRequest_destinations_inner.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIUpdateDevicesRequest_destinations_inner;

class OAIUpdateDevicesRequest : public OAIObject {
public:
    OAIUpdateDevicesRequest();
    OAIUpdateDevicesRequest(QString json);
    ~OAIUpdateDevicesRequest() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAccountServiceConnectionId() const;
    void setAccountServiceConnectionId(const QString &account_service_connection_id);
    bool is_account_service_connection_id_Set() const;
    bool is_account_service_connection_id_Valid() const;

    QList<OAIUpdateDevicesRequest_destinations_inner> getDestinations() const;
    void setDestinations(const QList<OAIUpdateDevicesRequest_destinations_inner> &destinations);
    bool is_destinations_Set() const;
    bool is_destinations_Valid() const;

    QList<QString> getDevices() const;
    void setDevices(const QList<QString> &devices);
    bool is_devices_Set() const;
    bool is_devices_Valid() const;

    QString getP12Base64() const;
    void setP12Base64(const QString &p12_base64);
    bool is_p12_base64_Set() const;
    bool is_p12_base64_Valid() const;

    QString getP12Password() const;
    void setP12Password(const QString &p12_password);
    bool is_p12_password_Set() const;
    bool is_p12_password_Valid() const;

    QString getP12ServiceConnectionId() const;
    void setP12ServiceConnectionId(const QString &p12_service_connection_id);
    bool is_p12_service_connection_id_Set() const;
    bool is_p12_service_connection_id_Valid() const;

    QString getPassword() const;
    void setPassword(const QString &password);
    bool is_password_Set() const;
    bool is_password_Valid() const;

    bool isPublishAllDevices() const;
    void setPublishAllDevices(const bool &publish_all_devices);
    bool is_publish_all_devices_Set() const;
    bool is_publish_all_devices_Valid() const;

    double getReleaseId() const;
    void setReleaseId(const double &release_id);
    bool is_release_id_Set() const;
    bool is_release_id_Valid() const;

    QString getUsername() const;
    void setUsername(const QString &username);
    bool is_username_Set() const;
    bool is_username_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_account_service_connection_id;
    bool m_account_service_connection_id_isSet;
    bool m_account_service_connection_id_isValid;

    QList<OAIUpdateDevicesRequest_destinations_inner> m_destinations;
    bool m_destinations_isSet;
    bool m_destinations_isValid;

    QList<QString> m_devices;
    bool m_devices_isSet;
    bool m_devices_isValid;

    QString m_p12_base64;
    bool m_p12_base64_isSet;
    bool m_p12_base64_isValid;

    QString m_p12_password;
    bool m_p12_password_isSet;
    bool m_p12_password_isValid;

    QString m_p12_service_connection_id;
    bool m_p12_service_connection_id_isSet;
    bool m_p12_service_connection_id_isValid;

    QString m_password;
    bool m_password_isSet;
    bool m_password_isValid;

    bool m_publish_all_devices;
    bool m_publish_all_devices_isSet;
    bool m_publish_all_devices_isValid;

    double m_release_id;
    bool m_release_id_isSet;
    bool m_release_id_isValid;

    QString m_username;
    bool m_username_isSet;
    bool m_username_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIUpdateDevicesRequest)

#endif // OAIUpdateDevicesRequest_H
