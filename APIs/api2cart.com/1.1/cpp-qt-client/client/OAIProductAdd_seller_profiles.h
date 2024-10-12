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
 * OAIProductAdd_seller_profiles.h
 *
 * If the seller is subscribed to \&quot;Business Policies\&quot;, use the seller_profiles instead of the shipping_details, payment_methods and return_accepted params.&lt;hr&gt;&lt;div style&#x3D;\&quot;font-style:normal\&quot;&gt;Param structure:&lt;div style&#x3D;\&quot;margin-left: 2%;\&quot;&gt;&lt;code style&#x3D;\&quot;padding:0; background-color:#ffffff;font-size:85%;font-family:monospace;\&quot;&gt;seller_profiles[&lt;b&gt;shipping_profile_id&lt;/b&gt;] &#x3D; integer&lt;/br&gt;seller_profiles[&lt;b&gt;payment_profile_id&lt;/b&gt;] &#x3D; integer&lt;/br&gt;seller_profiles[&lt;b&gt;return_profile_id&lt;/b&gt;] &#x3D; integer&lt;/br&gt;&lt;/code&gt;&lt;/div&gt;&lt;/div&gt;
 */

#ifndef OAIProductAdd_seller_profiles_H
#define OAIProductAdd_seller_profiles_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIProductAdd_seller_profiles : public OAIObject {
public:
    OAIProductAdd_seller_profiles();
    OAIProductAdd_seller_profiles(QString json);
    ~OAIProductAdd_seller_profiles() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getPaymentProfileId() const;
    void setPaymentProfileId(const QString &payment_profile_id);
    bool is_payment_profile_id_Set() const;
    bool is_payment_profile_id_Valid() const;

    QString getReturnProfileId() const;
    void setReturnProfileId(const QString &return_profile_id);
    bool is_return_profile_id_Set() const;
    bool is_return_profile_id_Valid() const;

    QString getShippingProfileId() const;
    void setShippingProfileId(const QString &shipping_profile_id);
    bool is_shipping_profile_id_Set() const;
    bool is_shipping_profile_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_payment_profile_id;
    bool m_payment_profile_id_isSet;
    bool m_payment_profile_id_isValid;

    QString m_return_profile_id;
    bool m_return_profile_id_isSet;
    bool m_return_profile_id_isValid;

    QString m_shipping_profile_id;
    bool m_shipping_profile_id_isSet;
    bool m_shipping_profile_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIProductAdd_seller_profiles)

#endif // OAIProductAdd_seller_profiles_H
