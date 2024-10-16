/**
 * Meshery API.
 * the purpose of this application is to provide an application that is using plain go code to define an API  This should demonstrate all the possible comment annotations that are available to turn go code into a fully compliant swagger 2.0 spec
 *
 * The version of the OpenAPI document: 0.4.27
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAISessionAffinityConfig.h
 *
 * 
 */

#ifndef OAISessionAffinityConfig_H
#define OAISessionAffinityConfig_H

#include <QJsonObject>

#include "OAIClientIPConfig.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIClientIPConfig;

class OAISessionAffinityConfig : public OAIObject {
public:
    OAISessionAffinityConfig();
    OAISessionAffinityConfig(QString json);
    ~OAISessionAffinityConfig() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIClientIPConfig getClientIp() const;
    void setClientIp(const OAIClientIPConfig &client_ip);
    bool is_client_ip_Set() const;
    bool is_client_ip_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIClientIPConfig m_client_ip;
    bool m_client_ip_isSet;
    bool m_client_ip_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAISessionAffinityConfig)

#endif // OAISessionAffinityConfig_H
