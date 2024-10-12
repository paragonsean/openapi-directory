/**
 * VocaDbWeb
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAITranslationType.h
 *
 * 
 */

#ifndef OAITranslationType_H
#define OAITranslationType_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAITranslationType : public OAIEnum {
public:
    OAITranslationType();
    OAITranslationType(QString json);
    ~OAITranslationType() override;

    QString asJson() const override;
    QJsonValue asJsonValue() const override;
    void fromJsonValue(QJsonValue json) override;
    void fromJson(QString jsonString) override;

    enum class eOAITranslationType {
        INVALID_VALUE_OPENAPI_GENERATED = 0,
        ORIGINAL, 
        ROMANIZED, 
        TRANSLATION
    };
    OAITranslationType::eOAITranslationType getValue() const;
    void setValue(const OAITranslationType::eOAITranslationType& value);
    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    eOAITranslationType m_value;
    bool m_value_isSet;
    bool m_value_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITranslationType)

#endif // OAITranslationType_H
