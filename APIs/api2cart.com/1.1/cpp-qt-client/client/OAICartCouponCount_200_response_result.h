/**
 * Swagger API2Cart
 * API2Cart
 *
 * The version of the OpenAPI document: 1.1
 * Contact: contact@api2cart.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAICartCouponCount_200_response_result.h
 *
 * 
 */

#ifndef OAICartCouponCount_200_response_result_H
#define OAICartCouponCount_200_response_result_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAICartCouponCount_200_response_result : public OAIObject {
public:
    OAICartCouponCount_200_response_result();
    OAICartCouponCount_200_response_result(QString json);
    ~OAICartCouponCount_200_response_result() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCouponsCount() const;
    void setCouponsCount(const QString &coupons_count);
    bool is_coupons_count_Set() const;
    bool is_coupons_count_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_coupons_count;
    bool m_coupons_count_isSet;
    bool m_coupons_count_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICartCouponCount_200_response_result)

#endif // OAICartCouponCount_200_response_result_H
