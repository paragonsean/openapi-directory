/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIGetNetworkSmTrustedAccessConfigs_200_response_inner.h
 *
 * 
 */

#ifndef OAIGetNetworkSmTrustedAccessConfigs_200_response_inner_H
#define OAIGetNetworkSmTrustedAccessConfigs_200_response_inner_H

#include <QJsonObject>

#include <QDateTime>
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIGetNetworkSmTrustedAccessConfigs_200_response_inner : public OAIObject {
public:
    OAIGetNetworkSmTrustedAccessConfigs_200_response_inner();
    OAIGetNetworkSmTrustedAccessConfigs_200_response_inner(QString json);
    ~OAIGetNetworkSmTrustedAccessConfigs_200_response_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QDateTime getAccessEndAt() const;
    void setAccessEndAt(const QDateTime &access_end_at);
    bool is_access_end_at_Set() const;
    bool is_access_end_at_Valid() const;

    QDateTime getAccessStartAt() const;
    void setAccessStartAt(const QDateTime &access_start_at);
    bool is_access_start_at_Set() const;
    bool is_access_start_at_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getScope() const;
    void setScope(const QString &scope);
    bool is_scope_Set() const;
    bool is_scope_Valid() const;

    QString getSsidName() const;
    void setSsidName(const QString &ssid_name);
    bool is_ssid_name_Set() const;
    bool is_ssid_name_Valid() const;

    QList<QString> getTags() const;
    void setTags(const QList<QString> &tags);
    bool is_tags_Set() const;
    bool is_tags_Valid() const;

    QString getTimeboundType() const;
    void setTimeboundType(const QString &timebound_type);
    bool is_timebound_type_Set() const;
    bool is_timebound_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QDateTime m_access_end_at;
    bool m_access_end_at_isSet;
    bool m_access_end_at_isValid;

    QDateTime m_access_start_at;
    bool m_access_start_at_isSet;
    bool m_access_start_at_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_scope;
    bool m_scope_isSet;
    bool m_scope_isValid;

    QString m_ssid_name;
    bool m_ssid_name_isSet;
    bool m_ssid_name_isValid;

    QList<QString> m_tags;
    bool m_tags_isSet;
    bool m_tags_isValid;

    QString m_timebound_type;
    bool m_timebound_type_isSet;
    bool m_timebound_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGetNetworkSmTrustedAccessConfigs_200_response_inner)

#endif // OAIGetNetworkSmTrustedAccessConfigs_200_response_inner_H
