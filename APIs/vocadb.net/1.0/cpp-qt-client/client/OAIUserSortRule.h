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
 * OAIUserSortRule.h
 *
 * 
 */

#ifndef OAIUserSortRule_H
#define OAIUserSortRule_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIUserSortRule : public OAIEnum {
public:
    OAIUserSortRule();
    OAIUserSortRule(QString json);
    ~OAIUserSortRule() override;

    QString asJson() const override;
    QJsonValue asJsonValue() const override;
    void fromJsonValue(QJsonValue json) override;
    void fromJson(QString jsonString) override;

    enum class eOAIUserSortRule {
        INVALID_VALUE_OPENAPI_GENERATED = 0,
        REGISTERDATE, 
        NAME, 
        GROUP
    };
    OAIUserSortRule::eOAIUserSortRule getValue() const;
    void setValue(const OAIUserSortRule::eOAIUserSortRule& value);
    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    eOAIUserSortRule m_value;
    bool m_value_isSet;
    bool m_value_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIUserSortRule)

#endif // OAIUserSortRule_H
