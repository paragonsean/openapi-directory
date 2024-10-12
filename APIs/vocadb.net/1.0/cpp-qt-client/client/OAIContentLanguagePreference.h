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
 * OAIContentLanguagePreference.h
 *
 * 
 */

#ifndef OAIContentLanguagePreference_H
#define OAIContentLanguagePreference_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIContentLanguagePreference : public OAIEnum {
public:
    OAIContentLanguagePreference();
    OAIContentLanguagePreference(QString json);
    ~OAIContentLanguagePreference() override;

    QString asJson() const override;
    QJsonValue asJsonValue() const override;
    void fromJsonValue(QJsonValue json) override;
    void fromJson(QString jsonString) override;

    enum class eOAIContentLanguagePreference {
        INVALID_VALUE_OPENAPI_GENERATED = 0,
        DEFAULT, 
        JAPANESE, 
        ROMAJI, 
        ENGLISH
    };
    OAIContentLanguagePreference::eOAIContentLanguagePreference getValue() const;
    void setValue(const OAIContentLanguagePreference::eOAIContentLanguagePreference& value);
    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    eOAIContentLanguagePreference m_value;
    bool m_value_isSet;
    bool m_value_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIContentLanguagePreference)

#endif // OAIContentLanguagePreference_H
