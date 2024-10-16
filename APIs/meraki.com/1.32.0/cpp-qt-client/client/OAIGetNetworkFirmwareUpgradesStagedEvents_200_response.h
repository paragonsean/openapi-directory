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
 * OAIGetNetworkFirmwareUpgradesStagedEvents_200_response.h
 *
 * 
 */

#ifndef OAIGetNetworkFirmwareUpgradesStagedEvents_200_response_H
#define OAIGetNetworkFirmwareUpgradesStagedEvents_200_response_H

#include <QJsonObject>

#include "OAICreateNetworkFirmwareUpgradesRollback_200_response_reasons_inner.h"
#include "OAIGetNetworkFirmwareUpgradesStagedEvents_200_response_products.h"
#include "OAIGetNetworkFirmwareUpgradesStagedEvents_200_response_stages_inner.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIGetNetworkFirmwareUpgradesStagedEvents_200_response_products;
class OAICreateNetworkFirmwareUpgradesRollback_200_response_reasons_inner;
class OAIGetNetworkFirmwareUpgradesStagedEvents_200_response_stages_inner;

class OAIGetNetworkFirmwareUpgradesStagedEvents_200_response : public OAIObject {
public:
    OAIGetNetworkFirmwareUpgradesStagedEvents_200_response();
    OAIGetNetworkFirmwareUpgradesStagedEvents_200_response(QString json);
    ~OAIGetNetworkFirmwareUpgradesStagedEvents_200_response() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIGetNetworkFirmwareUpgradesStagedEvents_200_response_products getProducts() const;
    void setProducts(const OAIGetNetworkFirmwareUpgradesStagedEvents_200_response_products &products);
    bool is_products_Set() const;
    bool is_products_Valid() const;

    QList<OAICreateNetworkFirmwareUpgradesRollback_200_response_reasons_inner> getReasons() const;
    void setReasons(const QList<OAICreateNetworkFirmwareUpgradesRollback_200_response_reasons_inner> &reasons);
    bool is_reasons_Set() const;
    bool is_reasons_Valid() const;

    QList<OAIGetNetworkFirmwareUpgradesStagedEvents_200_response_stages_inner> getStages() const;
    void setStages(const QList<OAIGetNetworkFirmwareUpgradesStagedEvents_200_response_stages_inner> &stages);
    bool is_stages_Set() const;
    bool is_stages_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIGetNetworkFirmwareUpgradesStagedEvents_200_response_products m_products;
    bool m_products_isSet;
    bool m_products_isValid;

    QList<OAICreateNetworkFirmwareUpgradesRollback_200_response_reasons_inner> m_reasons;
    bool m_reasons_isSet;
    bool m_reasons_isValid;

    QList<OAIGetNetworkFirmwareUpgradesStagedEvents_200_response_stages_inner> m_stages;
    bool m_stages_isSet;
    bool m_stages_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGetNetworkFirmwareUpgradesStagedEvents_200_response)

#endif // OAIGetNetworkFirmwareUpgradesStagedEvents_200_response_H
