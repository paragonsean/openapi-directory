/**
 * vRealize Network Insight API Reference
 * vRealize Network Insight API Reference
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIDellSwitchDataSourceRequest.h
 *
 * 
 */

#ifndef OAIDellSwitchDataSourceRequest_H
#define OAIDellSwitchDataSourceRequest_H

#include <QJsonObject>

#include "OAIDellSwitchType.h"
#include "OAIPasswordCredentials.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIPasswordCredentials;

class OAIDellSwitchDataSourceRequest : public OAIObject {
public:
    OAIDellSwitchDataSourceRequest();
    OAIDellSwitchDataSourceRequest(QString json);
    ~OAIDellSwitchDataSourceRequest() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isEnabled() const;
    void setEnabled(const bool &enabled);
    bool is_enabled_Set() const;
    bool is_enabled_Valid() const;

    QString getFqdn() const;
    void setFqdn(const QString &fqdn);
    bool is_fqdn_Set() const;
    bool is_fqdn_Valid() const;

    QString getIp() const;
    void setIp(const QString &ip);
    bool is_ip_Set() const;
    bool is_ip_Valid() const;

    QString getNickname() const;
    void setNickname(const QString &nickname);
    bool is_nickname_Set() const;
    bool is_nickname_Valid() const;

    QString getNotes() const;
    void setNotes(const QString &notes);
    bool is_notes_Set() const;
    bool is_notes_Valid() const;

    QString getProxyId() const;
    void setProxyId(const QString &proxy_id);
    bool is_proxy_id_Set() const;
    bool is_proxy_id_Valid() const;

    OAIPasswordCredentials getCredentials() const;
    void setCredentials(const OAIPasswordCredentials &credentials);
    bool is_credentials_Set() const;
    bool is_credentials_Valid() const;

    OAIDellSwitchType getSwitchType() const;
    void setSwitchType(const OAIDellSwitchType &switch_type);
    bool is_switch_type_Set() const;
    bool is_switch_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_enabled;
    bool m_enabled_isSet;
    bool m_enabled_isValid;

    QString m_fqdn;
    bool m_fqdn_isSet;
    bool m_fqdn_isValid;

    QString m_ip;
    bool m_ip_isSet;
    bool m_ip_isValid;

    QString m_nickname;
    bool m_nickname_isSet;
    bool m_nickname_isValid;

    QString m_notes;
    bool m_notes_isSet;
    bool m_notes_isValid;

    QString m_proxy_id;
    bool m_proxy_id_isSet;
    bool m_proxy_id_isValid;

    OAIPasswordCredentials m_credentials;
    bool m_credentials_isSet;
    bool m_credentials_isValid;

    OAIDellSwitchType m_switch_type;
    bool m_switch_type_isSet;
    bool m_switch_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIDellSwitchDataSourceRequest)

#endif // OAIDellSwitchDataSourceRequest_H
