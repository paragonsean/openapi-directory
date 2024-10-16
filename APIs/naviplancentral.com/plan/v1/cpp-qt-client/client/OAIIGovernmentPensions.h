/**
 * NaviPlan API
 * An API for accessing NaviPlan plan data for a client.
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIIGovernmentPensions.h
 *
 * 
 */

#ifndef OAIIGovernmentPensions_H
#define OAIIGovernmentPensions_H

#include <QJsonObject>

#include "OAICurrency.h"
#include "OAIICanadianGovernmentPensions.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIICanadianGovernmentPensions;
class OAICurrency;

class OAIIGovernmentPensions : public OAIObject {
public:
    OAIIGovernmentPensions();
    OAIIGovernmentPensions(QString json);
    ~OAIIGovernmentPensions() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIICanadianGovernmentPensions getEstimatedCanadianGovernmentPensions() const;
    void setEstimatedCanadianGovernmentPensions(const OAIICanadianGovernmentPensions &estimated_canadian_government_pensions);
    bool is_estimated_canadian_government_pensions_Set() const;
    bool is_estimated_canadian_government_pensions_Valid() const;

    OAICurrency getEstimatedSocialSecurity() const;
    void setEstimatedSocialSecurity(const OAICurrency &estimated_social_security);
    bool is_estimated_social_security_Set() const;
    bool is_estimated_social_security_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIICanadianGovernmentPensions m_estimated_canadian_government_pensions;
    bool m_estimated_canadian_government_pensions_isSet;
    bool m_estimated_canadian_government_pensions_isValid;

    OAICurrency m_estimated_social_security;
    bool m_estimated_social_security_isSet;
    bool m_estimated_social_security_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIIGovernmentPensions)

#endif // OAIIGovernmentPensions_H
