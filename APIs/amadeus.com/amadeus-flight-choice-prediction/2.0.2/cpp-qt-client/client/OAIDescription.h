/**
 * Flight Choice Prediction
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, to see what is included in test please refer to our **[data collection](https://github.com/amadeus4dev/data-collection)**. 
 *
 * The version of the OpenAPI document: 2.0.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIDescription.h
 *
 * 
 */

#ifndef OAIDescription_H
#define OAIDescription_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIDescription : public OAIObject {
public:
    OAIDescription();
    OAIDescription(QString json);
    ~OAIDescription() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getDescriptionType() const;
    void setDescriptionType(const QString &description_type);
    bool is_description_type_Set() const;
    bool is_description_type_Valid() const;

    QString getText() const;
    void setText(const QString &text);
    bool is_text_Set() const;
    bool is_text_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_description_type;
    bool m_description_type_isSet;
    bool m_description_type_isValid;

    QString m_text;
    bool m_text_isSet;
    bool m_text_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIDescription)

#endif // OAIDescription_H
