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
 * OAIGetOrganizationSummaryTopDevicesModelsByUsage_200_response_inner.h
 *
 * 
 */

#ifndef OAIGetOrganizationSummaryTopDevicesModelsByUsage_200_response_inner_H
#define OAIGetOrganizationSummaryTopDevicesModelsByUsage_200_response_inner_H

#include <QJsonObject>

#include "OAIGetOrganizationSummaryTopDevicesModelsByUsage_200_response_inner_usage.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIGetOrganizationSummaryTopDevicesModelsByUsage_200_response_inner_usage;

class OAIGetOrganizationSummaryTopDevicesModelsByUsage_200_response_inner : public OAIObject {
public:
    OAIGetOrganizationSummaryTopDevicesModelsByUsage_200_response_inner();
    OAIGetOrganizationSummaryTopDevicesModelsByUsage_200_response_inner(QString json);
    ~OAIGetOrganizationSummaryTopDevicesModelsByUsage_200_response_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getCount() const;
    void setCount(const qint32 &count);
    bool is_count_Set() const;
    bool is_count_Valid() const;

    QString getModel() const;
    void setModel(const QString &model);
    bool is_model_Set() const;
    bool is_model_Valid() const;

    OAIGetOrganizationSummaryTopDevicesModelsByUsage_200_response_inner_usage getUsage() const;
    void setUsage(const OAIGetOrganizationSummaryTopDevicesModelsByUsage_200_response_inner_usage &usage);
    bool is_usage_Set() const;
    bool is_usage_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_count;
    bool m_count_isSet;
    bool m_count_isValid;

    QString m_model;
    bool m_model_isSet;
    bool m_model_isValid;

    OAIGetOrganizationSummaryTopDevicesModelsByUsage_200_response_inner_usage m_usage;
    bool m_usage_isSet;
    bool m_usage_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGetOrganizationSummaryTopDevicesModelsByUsage_200_response_inner)

#endif // OAIGetOrganizationSummaryTopDevicesModelsByUsage_200_response_inner_H
