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
 * OAIUpdateNetworkSwitchDscpToCosMappings_request_mappings_inner.h
 *
 * 
 */

#ifndef OAIUpdateNetworkSwitchDscpToCosMappings_request_mappings_inner_H
#define OAIUpdateNetworkSwitchDscpToCosMappings_request_mappings_inner_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIUpdateNetworkSwitchDscpToCosMappings_request_mappings_inner : public OAIObject {
public:
    OAIUpdateNetworkSwitchDscpToCosMappings_request_mappings_inner();
    OAIUpdateNetworkSwitchDscpToCosMappings_request_mappings_inner(QString json);
    ~OAIUpdateNetworkSwitchDscpToCosMappings_request_mappings_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getCos() const;
    void setCos(const qint32 &cos);
    bool is_cos_Set() const;
    bool is_cos_Valid() const;

    qint32 getDscp() const;
    void setDscp(const qint32 &dscp);
    bool is_dscp_Set() const;
    bool is_dscp_Valid() const;

    QString getTitle() const;
    void setTitle(const QString &title);
    bool is_title_Set() const;
    bool is_title_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_cos;
    bool m_cos_isSet;
    bool m_cos_isValid;

    qint32 m_dscp;
    bool m_dscp_isSet;
    bool m_dscp_isValid;

    QString m_title;
    bool m_title_isSet;
    bool m_title_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIUpdateNetworkSwitchDscpToCosMappings_request_mappings_inner)

#endif // OAIUpdateNetworkSwitchDscpToCosMappings_request_mappings_inner_H
