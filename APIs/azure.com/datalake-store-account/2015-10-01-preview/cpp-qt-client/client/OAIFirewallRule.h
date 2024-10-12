/**
 * DataLakeStoreAccountManagementClient
 * Creates an Azure Data Lake Store account management client.
 *
 * The version of the OpenAPI document: 2015-10-01-preview
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIFirewallRule.h
 *
 * Data Lake Store firewall rule information
 */

#ifndef OAIFirewallRule_H
#define OAIFirewallRule_H

#include <QJsonObject>

#include "OAIFirewallRuleProperties.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIFirewallRuleProperties;

class OAIFirewallRule : public OAIObject {
public:
    OAIFirewallRule();
    OAIFirewallRule(QString json);
    ~OAIFirewallRule() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getLocation() const;
    void setLocation(const QString &location);
    bool is_location_Set() const;
    bool is_location_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    OAIFirewallRuleProperties getProperties() const;
    void setProperties(const OAIFirewallRuleProperties &properties);
    bool is_properties_Set() const;
    bool is_properties_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_location;
    bool m_location_isSet;
    bool m_location_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    OAIFirewallRuleProperties m_properties;
    bool m_properties_isSet;
    bool m_properties_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIFirewallRule)

#endif // OAIFirewallRule_H
