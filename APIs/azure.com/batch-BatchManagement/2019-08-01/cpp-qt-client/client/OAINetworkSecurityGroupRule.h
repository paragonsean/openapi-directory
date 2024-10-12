/**
 * BatchManagement
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-08-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAINetworkSecurityGroupRule.h
 *
 * 
 */

#ifndef OAINetworkSecurityGroupRule_H
#define OAINetworkSecurityGroupRule_H

#include <QJsonObject>

#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAINetworkSecurityGroupRule : public OAIObject {
public:
    OAINetworkSecurityGroupRule();
    OAINetworkSecurityGroupRule(QString json);
    ~OAINetworkSecurityGroupRule() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAccess() const;
    void setAccess(const QString &access);
    bool is_access_Set() const;
    bool is_access_Valid() const;

    qint32 getPriority() const;
    void setPriority(const qint32 &priority);
    bool is_priority_Set() const;
    bool is_priority_Valid() const;

    QString getSourceAddressPrefix() const;
    void setSourceAddressPrefix(const QString &source_address_prefix);
    bool is_source_address_prefix_Set() const;
    bool is_source_address_prefix_Valid() const;

    QList<QString> getSourcePortRanges() const;
    void setSourcePortRanges(const QList<QString> &source_port_ranges);
    bool is_source_port_ranges_Set() const;
    bool is_source_port_ranges_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_access;
    bool m_access_isSet;
    bool m_access_isValid;

    qint32 m_priority;
    bool m_priority_isSet;
    bool m_priority_isValid;

    QString m_source_address_prefix;
    bool m_source_address_prefix_isSet;
    bool m_source_address_prefix_isValid;

    QList<QString> m_source_port_ranges;
    bool m_source_port_ranges_isSet;
    bool m_source_port_ranges_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAINetworkSecurityGroupRule)

#endif // OAINetworkSecurityGroupRule_H
