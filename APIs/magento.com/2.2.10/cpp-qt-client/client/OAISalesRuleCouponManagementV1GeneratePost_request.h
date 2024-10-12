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
 * OAISalesRuleCouponManagementV1GeneratePost_request.h
 *
 * 
 */

#ifndef OAISalesRuleCouponManagementV1GeneratePost_request_H
#define OAISalesRuleCouponManagementV1GeneratePost_request_H

#include <QJsonObject>

#include "OAISales_rule_data_coupon_generation_spec_interface.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAISales_rule_data_coupon_generation_spec_interface;

class OAISalesRuleCouponManagementV1GeneratePost_request : public OAIObject {
public:
    OAISalesRuleCouponManagementV1GeneratePost_request();
    OAISalesRuleCouponManagementV1GeneratePost_request(QString json);
    ~OAISalesRuleCouponManagementV1GeneratePost_request() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAISales_rule_data_coupon_generation_spec_interface getCouponSpec() const;
    void setCouponSpec(const OAISales_rule_data_coupon_generation_spec_interface &coupon_spec);
    bool is_coupon_spec_Set() const;
    bool is_coupon_spec_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAISales_rule_data_coupon_generation_spec_interface m_coupon_spec;
    bool m_coupon_spec_isSet;
    bool m_coupon_spec_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAISalesRuleCouponManagementV1GeneratePost_request)

#endif // OAISalesRuleCouponManagementV1GeneratePost_request_H
