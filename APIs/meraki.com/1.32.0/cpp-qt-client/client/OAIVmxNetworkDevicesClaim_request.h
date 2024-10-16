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
 * OAIVmxNetworkDevicesClaim_request.h
 *
 * 
 */

#ifndef OAIVmxNetworkDevicesClaim_request_H
#define OAIVmxNetworkDevicesClaim_request_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIVmxNetworkDevicesClaim_request : public OAIObject {
public:
    OAIVmxNetworkDevicesClaim_request();
    OAIVmxNetworkDevicesClaim_request(QString json);
    ~OAIVmxNetworkDevicesClaim_request() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getSize() const;
    void setSize(const QString &size);
    bool is_size_Set() const;
    bool is_size_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_size;
    bool m_size_isSet;
    bool m_size_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIVmxNetworkDevicesClaim_request)

#endif // OAIVmxNetworkDevicesClaim_request_H
