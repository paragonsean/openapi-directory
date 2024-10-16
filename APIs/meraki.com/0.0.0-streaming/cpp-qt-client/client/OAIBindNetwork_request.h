/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 23 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 0.0.0-streaming
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIBindNetwork_request.h
 *
 * 
 */

#ifndef OAIBindNetwork_request_H
#define OAIBindNetwork_request_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIBindNetwork_request : public OAIObject {
public:
    OAIBindNetwork_request();
    OAIBindNetwork_request(QString json);
    ~OAIBindNetwork_request() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isAutoBind() const;
    void setAutoBind(const bool &auto_bind);
    bool is_auto_bind_Set() const;
    bool is_auto_bind_Valid() const;

    QString getConfigTemplateId() const;
    void setConfigTemplateId(const QString &config_template_id);
    bool is_config_template_id_Set() const;
    bool is_config_template_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_auto_bind;
    bool m_auto_bind_isSet;
    bool m_auto_bind_isValid;

    QString m_config_template_id;
    bool m_config_template_id_isSet;
    bool m_config_template_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIBindNetwork_request)

#endif // OAIBindNetwork_request_H
