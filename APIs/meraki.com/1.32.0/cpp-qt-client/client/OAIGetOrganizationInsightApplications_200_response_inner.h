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
 * OAIGetOrganizationInsightApplications_200_response_inner.h
 *
 * 
 */

#ifndef OAIGetOrganizationInsightApplications_200_response_inner_H
#define OAIGetOrganizationInsightApplications_200_response_inner_H

#include <QJsonObject>

#include "OAIGetOrganizationInsightApplications_200_response_inner_thresholds.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIGetOrganizationInsightApplications_200_response_inner_thresholds;

class OAIGetOrganizationInsightApplications_200_response_inner : public OAIObject {
public:
    OAIGetOrganizationInsightApplications_200_response_inner();
    OAIGetOrganizationInsightApplications_200_response_inner(QString json);
    ~OAIGetOrganizationInsightApplications_200_response_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getApplicationId() const;
    void setApplicationId(const QString &application_id);
    bool is_application_id_Set() const;
    bool is_application_id_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    OAIGetOrganizationInsightApplications_200_response_inner_thresholds getThresholds() const;
    void setThresholds(const OAIGetOrganizationInsightApplications_200_response_inner_thresholds &thresholds);
    bool is_thresholds_Set() const;
    bool is_thresholds_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_application_id;
    bool m_application_id_isSet;
    bool m_application_id_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    OAIGetOrganizationInsightApplications_200_response_inner_thresholds m_thresholds;
    bool m_thresholds_isSet;
    bool m_thresholds_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGetOrganizationInsightApplications_200_response_inner)

#endif // OAIGetOrganizationInsightApplications_200_response_inner_H
