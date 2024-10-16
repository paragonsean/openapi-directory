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
 * OAIUpdateOrganizationBrandingPoliciesPriorities_request.h
 *
 * 
 */

#ifndef OAIUpdateOrganizationBrandingPoliciesPriorities_request_H
#define OAIUpdateOrganizationBrandingPoliciesPriorities_request_H

#include <QJsonObject>

#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIUpdateOrganizationBrandingPoliciesPriorities_request : public OAIObject {
public:
    OAIUpdateOrganizationBrandingPoliciesPriorities_request();
    OAIUpdateOrganizationBrandingPoliciesPriorities_request(QString json);
    ~OAIUpdateOrganizationBrandingPoliciesPriorities_request() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<QString> getBrandingPolicyIds() const;
    void setBrandingPolicyIds(const QList<QString> &branding_policy_ids);
    bool is_branding_policy_ids_Set() const;
    bool is_branding_policy_ids_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<QString> m_branding_policy_ids;
    bool m_branding_policy_ids_isSet;
    bool m_branding_policy_ids_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIUpdateOrganizationBrandingPoliciesPriorities_request)

#endif // OAIUpdateOrganizationBrandingPoliciesPriorities_request_H
