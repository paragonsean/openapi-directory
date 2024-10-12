/**
 * StorSimple8000SeriesManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-06-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAINicIPv6.h
 *
 * Details related to the IPv6 address configuration.
 */

#ifndef OAINicIPv6_H
#define OAINicIPv6_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAINicIPv6 : public OAIObject {
public:
    OAINicIPv6();
    OAINicIPv6(QString json);
    ~OAINicIPv6() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getController0Ipv6Address() const;
    void setController0Ipv6Address(const QString &controller0_ipv6_address);
    bool is_controller0_ipv6_address_Set() const;
    bool is_controller0_ipv6_address_Valid() const;

    QString getController1Ipv6Address() const;
    void setController1Ipv6Address(const QString &controller1_ipv6_address);
    bool is_controller1_ipv6_address_Set() const;
    bool is_controller1_ipv6_address_Valid() const;

    QString getIpv6Address() const;
    void setIpv6Address(const QString &ipv6_address);
    bool is_ipv6_address_Set() const;
    bool is_ipv6_address_Valid() const;

    QString getIpv6Gateway() const;
    void setIpv6Gateway(const QString &ipv6_gateway);
    bool is_ipv6_gateway_Set() const;
    bool is_ipv6_gateway_Valid() const;

    QString getIpv6Prefix() const;
    void setIpv6Prefix(const QString &ipv6_prefix);
    bool is_ipv6_prefix_Set() const;
    bool is_ipv6_prefix_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_controller0_ipv6_address;
    bool m_controller0_ipv6_address_isSet;
    bool m_controller0_ipv6_address_isValid;

    QString m_controller1_ipv6_address;
    bool m_controller1_ipv6_address_isSet;
    bool m_controller1_ipv6_address_isValid;

    QString m_ipv6_address;
    bool m_ipv6_address_isSet;
    bool m_ipv6_address_isValid;

    QString m_ipv6_gateway;
    bool m_ipv6_gateway_isSet;
    bool m_ipv6_gateway_isValid;

    QString m_ipv6_prefix;
    bool m_ipv6_prefix_isSet;
    bool m_ipv6_prefix_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAINicIPv6)

#endif // OAINicIPv6_H
