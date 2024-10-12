/**
 *  API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-02-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIDeploymentLocations_hostingEnvironments_inner_vipMappings_inner.h
 *
 * Virtual IP mapping.
 */

#ifndef OAIDeploymentLocations_hostingEnvironments_inner_vipMappings_inner_H
#define OAIDeploymentLocations_hostingEnvironments_inner_vipMappings_inner_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIDeploymentLocations_hostingEnvironments_inner_vipMappings_inner : public OAIObject {
public:
    OAIDeploymentLocations_hostingEnvironments_inner_vipMappings_inner();
    OAIDeploymentLocations_hostingEnvironments_inner_vipMappings_inner(QString json);
    ~OAIDeploymentLocations_hostingEnvironments_inner_vipMappings_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isInUse() const;
    void setInUse(const bool &in_use);
    bool is_in_use_Set() const;
    bool is_in_use_Valid() const;

    qint32 getInternalHttpPort() const;
    void setInternalHttpPort(const qint32 &internal_http_port);
    bool is_internal_http_port_Set() const;
    bool is_internal_http_port_Valid() const;

    qint32 getInternalHttpsPort() const;
    void setInternalHttpsPort(const qint32 &internal_https_port);
    bool is_internal_https_port_Set() const;
    bool is_internal_https_port_Valid() const;

    QString getVirtualIp() const;
    void setVirtualIp(const QString &virtual_ip);
    bool is_virtual_ip_Set() const;
    bool is_virtual_ip_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_in_use;
    bool m_in_use_isSet;
    bool m_in_use_isValid;

    qint32 m_internal_http_port;
    bool m_internal_http_port_isSet;
    bool m_internal_http_port_isValid;

    qint32 m_internal_https_port;
    bool m_internal_https_port_isSet;
    bool m_internal_https_port_isValid;

    QString m_virtual_ip;
    bool m_virtual_ip_isSet;
    bool m_virtual_ip_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIDeploymentLocations_hostingEnvironments_inner_vipMappings_inner)

#endif // OAIDeploymentLocations_hostingEnvironments_inner_vipMappings_inner_H
