/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 23 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 0.0.0-streaming
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAICreateNetworkPiiRequest_request.h
 *
 * 
 */

#ifndef OAICreateNetworkPiiRequest_request_H
#define OAICreateNetworkPiiRequest_request_H

#include <QJsonObject>

#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAICreateNetworkPiiRequest_request : public OAIObject {
public:
    OAICreateNetworkPiiRequest_request();
    OAICreateNetworkPiiRequest_request(QString json);
    ~OAICreateNetworkPiiRequest_request() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<QString> getDatasets() const;
    void setDatasets(const QList<QString> &datasets);
    bool is_datasets_Set() const;
    bool is_datasets_Valid() const;

    QString getEmail() const;
    void setEmail(const QString &email);
    bool is_email_Set() const;
    bool is_email_Valid() const;

    QString getMac() const;
    void setMac(const QString &mac);
    bool is_mac_Set() const;
    bool is_mac_Valid() const;

    QString getSmDeviceId() const;
    void setSmDeviceId(const QString &sm_device_id);
    bool is_sm_device_id_Set() const;
    bool is_sm_device_id_Valid() const;

    QString getSmUserId() const;
    void setSmUserId(const QString &sm_user_id);
    bool is_sm_user_id_Set() const;
    bool is_sm_user_id_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    QString getUsername() const;
    void setUsername(const QString &username);
    bool is_username_Set() const;
    bool is_username_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<QString> m_datasets;
    bool m_datasets_isSet;
    bool m_datasets_isValid;

    QString m_email;
    bool m_email_isSet;
    bool m_email_isValid;

    QString m_mac;
    bool m_mac_isSet;
    bool m_mac_isValid;

    QString m_sm_device_id;
    bool m_sm_device_id_isSet;
    bool m_sm_device_id_isValid;

    QString m_sm_user_id;
    bool m_sm_user_id_isSet;
    bool m_sm_user_id_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;

    QString m_username;
    bool m_username_isSet;
    bool m_username_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICreateNetworkPiiRequest_request)

#endif // OAICreateNetworkPiiRequest_request_H
