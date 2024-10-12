/**
 * BBC Nitro API
 * BBC Nitro is the BBC's application programming interface (API) for BBC Programmes Metadata.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: nitro@bbc.co.uk
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIEmbargoed.h
 *
 * 
 */

#ifndef OAIEmbargoed_H
#define OAIEmbargoed_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIEmbargoed : public OAIEnum {
public:
    OAIEmbargoed();
    OAIEmbargoed(QString json);
    ~OAIEmbargoed() override;

    QString asJson() const override;
    QJsonValue asJsonValue() const override;
    void fromJsonValue(QJsonValue json) override;
    void fromJson(QString jsonString) override;

    enum class eOAIEmbargoed {
        INVALID_VALUE_OPENAPI_GENERATED = 0,
        TRUE, 
        FALSE
    };
    OAIEmbargoed::eOAIEmbargoed getValue() const;
    void setValue(const OAIEmbargoed::eOAIEmbargoed& value);
    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    eOAIEmbargoed m_value;
    bool m_value_isSet;
    bool m_value_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIEmbargoed)

#endif // OAIEmbargoed_H
