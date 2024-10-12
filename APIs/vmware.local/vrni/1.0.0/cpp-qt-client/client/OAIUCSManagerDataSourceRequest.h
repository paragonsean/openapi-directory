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
 * OAIUCSManagerDataSourceRequest.h
 *
 * 
 */

#ifndef OAIUCSManagerDataSourceRequest_H
#define OAIUCSManagerDataSourceRequest_H

#include <QJsonObject>

#include "OAIDataSourceType.h"
#include "OAIPasswordCredentials.h"
#include "OAISwitchDataSource.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIPasswordCredentials;

class OAIUCSManagerDataSourceRequest : public OAIObject {
public:
    OAIUCSManagerDataSourceRequest();
    OAIUCSManagerDataSourceRequest(QString json);
    ~OAIUCSManagerDataSourceRequest() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isEnabled() const;
    void setEnabled(const bool &enabled);
    bool is_enabled_Set() const;
    bool is_enabled_Valid() const;

    QString getEntityId() const;
    void setEntityId(const QString &entity_id);
    bool is_entity_id_Set() const;
    bool is_entity_id_Valid() const;

    OAIDataSourceType getEntityType() const;
    void setEntityType(const OAIDataSourceType &entity_type);
    bool is_entity_type_Set() const;
    bool is_entity_type_Valid() const;

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

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_enabled;
    bool m_enabled_isSet;
    bool m_enabled_isValid;

    QString m_entity_id;
    bool m_entity_id_isSet;
    bool m_entity_id_isValid;

    OAIDataSourceType m_entity_type;
    bool m_entity_type_isSet;
    bool m_entity_type_isValid;

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
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIUCSManagerDataSourceRequest)

#endif // OAIUCSManagerDataSourceRequest_H
