/**
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAISales_rule_data_rule_extension_interface.h
 *
 * ExtensionInterface class for @see \\Magento\\SalesRule\\Api\\Data\\RuleInterface
 */

#ifndef OAISales_rule_data_rule_extension_interface_H
#define OAISales_rule_data_rule_extension_interface_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAISales_rule_data_rule_extension_interface : public OAIObject {
public:
    OAISales_rule_data_rule_extension_interface();
    OAISales_rule_data_rule_extension_interface(QString json);
    ~OAISales_rule_data_rule_extension_interface() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getRewardPointsDelta() const;
    void setRewardPointsDelta(const qint32 &reward_points_delta);
    bool is_reward_points_delta_Set() const;
    bool is_reward_points_delta_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_reward_points_delta;
    bool m_reward_points_delta_isSet;
    bool m_reward_points_delta_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAISales_rule_data_rule_extension_interface)

#endif // OAISales_rule_data_rule_extension_interface_H
