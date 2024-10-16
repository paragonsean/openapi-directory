/**
 * CallFire API Documentation
 * CallFire
 *
 * The version of the OpenAPI document: V2
 * Contact: support@callfire.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIKeywordConfig.h
 *
 * ~
 */

#ifndef OAIKeywordConfig_H
#define OAIKeywordConfig_H

#include <QJsonObject>

#include "OAITextInboundConfig.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAITextInboundConfig;

class OAIKeywordConfig : public OAIObject {
public:
    OAIKeywordConfig();
    OAIKeywordConfig(QString json);
    ~OAIKeywordConfig() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getKeyword() const;
    void setKeyword(const QString &keyword);
    bool is_keyword_Set() const;
    bool is_keyword_Valid() const;

    OAITextInboundConfig getTextInboundConfig() const;
    void setTextInboundConfig(const OAITextInboundConfig &text_inbound_config);
    bool is_text_inbound_config_Set() const;
    bool is_text_inbound_config_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_keyword;
    bool m_keyword_isSet;
    bool m_keyword_isValid;

    OAITextInboundConfig m_text_inbound_config;
    bool m_text_inbound_config_isSet;
    bool m_text_inbound_config_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIKeywordConfig)

#endif // OAIKeywordConfig_H
