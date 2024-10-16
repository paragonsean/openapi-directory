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
 * OAIUpdateNetworkWirelessSsidHotspot20_request_naiRealms_inner.h
 *
 * 
 */

#ifndef OAIUpdateNetworkWirelessSsidHotspot20_request_naiRealms_inner_H
#define OAIUpdateNetworkWirelessSsidHotspot20_request_naiRealms_inner_H

#include <QJsonObject>

#include "OAIUpdateNetworkWirelessSsidHotspot20_request_naiRealms_inner_methods_inner.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIUpdateNetworkWirelessSsidHotspot20_request_naiRealms_inner_methods_inner;

class OAIUpdateNetworkWirelessSsidHotspot20_request_naiRealms_inner : public OAIObject {
public:
    OAIUpdateNetworkWirelessSsidHotspot20_request_naiRealms_inner();
    OAIUpdateNetworkWirelessSsidHotspot20_request_naiRealms_inner(QString json);
    ~OAIUpdateNetworkWirelessSsidHotspot20_request_naiRealms_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getFormat() const;
    void setFormat(const QString &format);
    bool is_format_Set() const;
    bool is_format_Valid() const;

    QList<OAIUpdateNetworkWirelessSsidHotspot20_request_naiRealms_inner_methods_inner> getMethods() const;
    void setMethods(const QList<OAIUpdateNetworkWirelessSsidHotspot20_request_naiRealms_inner_methods_inner> &methods);
    bool is_methods_Set() const;
    bool is_methods_Valid() const;

    QString getRealm() const;
    void setRealm(const QString &realm);
    bool is_realm_Set() const;
    bool is_realm_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_format;
    bool m_format_isSet;
    bool m_format_isValid;

    QList<OAIUpdateNetworkWirelessSsidHotspot20_request_naiRealms_inner_methods_inner> m_methods;
    bool m_methods_isSet;
    bool m_methods_isValid;

    QString m_realm;
    bool m_realm_isSet;
    bool m_realm_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIUpdateNetworkWirelessSsidHotspot20_request_naiRealms_inner)

#endif // OAIUpdateNetworkWirelessSsidHotspot20_request_naiRealms_inner_H
