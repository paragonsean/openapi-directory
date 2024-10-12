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
 * OAICreateOrganizationAdaptivePolicyAcl_request.h
 *
 * 
 */

#ifndef OAICreateOrganizationAdaptivePolicyAcl_request_H
#define OAICreateOrganizationAdaptivePolicyAcl_request_H

#include <QJsonObject>

#include "OAICreateOrganizationAdaptivePolicyAcl_request_rules_inner.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAICreateOrganizationAdaptivePolicyAcl_request_rules_inner;

class OAICreateOrganizationAdaptivePolicyAcl_request : public OAIObject {
public:
    OAICreateOrganizationAdaptivePolicyAcl_request();
    OAICreateOrganizationAdaptivePolicyAcl_request(QString json);
    ~OAICreateOrganizationAdaptivePolicyAcl_request() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    QString getIpVersion() const;
    void setIpVersion(const QString &ip_version);
    bool is_ip_version_Set() const;
    bool is_ip_version_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QList<OAICreateOrganizationAdaptivePolicyAcl_request_rules_inner> getRules() const;
    void setRules(const QList<OAICreateOrganizationAdaptivePolicyAcl_request_rules_inner> &rules);
    bool is_rules_Set() const;
    bool is_rules_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    QString m_ip_version;
    bool m_ip_version_isSet;
    bool m_ip_version_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QList<OAICreateOrganizationAdaptivePolicyAcl_request_rules_inner> m_rules;
    bool m_rules_isSet;
    bool m_rules_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICreateOrganizationAdaptivePolicyAcl_request)

#endif // OAICreateOrganizationAdaptivePolicyAcl_request_H
