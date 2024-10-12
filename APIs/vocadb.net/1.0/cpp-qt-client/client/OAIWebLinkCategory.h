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
 * OAIWebLinkCategory.h
 *
 * 
 */

#ifndef OAIWebLinkCategory_H
#define OAIWebLinkCategory_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIWebLinkCategory : public OAIEnum {
public:
    OAIWebLinkCategory();
    OAIWebLinkCategory(QString json);
    ~OAIWebLinkCategory() override;

    QString asJson() const override;
    QJsonValue asJsonValue() const override;
    void fromJsonValue(QJsonValue json) override;
    void fromJson(QString jsonString) override;

    enum class eOAIWebLinkCategory {
        INVALID_VALUE_OPENAPI_GENERATED = 0,
        OFFICIAL, 
        COMMERCIAL, 
        REFERENCE, 
        OTHER
    };
    OAIWebLinkCategory::eOAIWebLinkCategory getValue() const;
    void setValue(const OAIWebLinkCategory::eOAIWebLinkCategory& value);
    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    eOAIWebLinkCategory m_value;
    bool m_value_isSet;
    bool m_value_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIWebLinkCategory)

#endif // OAIWebLinkCategory_H
