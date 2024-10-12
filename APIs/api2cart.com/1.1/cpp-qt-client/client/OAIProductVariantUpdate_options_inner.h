/**
 * Swagger API2Cart
 * API2Cart
 *
 * The version of the OpenAPI document: 1.1
 * Contact: contact@api2cart.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIProductVariantUpdate_options_inner.h
 *
 * 
 */

#ifndef OAIProductVariantUpdate_options_inner_H
#define OAIProductVariantUpdate_options_inner_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIProductVariantUpdate_options_inner : public OAIObject {
public:
    OAIProductVariantUpdate_options_inner();
    OAIProductVariantUpdate_options_inner(QString json);
    ~OAIProductVariantUpdate_options_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getOptionName() const;
    void setOptionName(const QString &option_name);
    bool is_option_name_Set() const;
    bool is_option_name_Valid() const;

    QString getOptionValue() const;
    void setOptionValue(const QString &option_value);
    bool is_option_value_Set() const;
    bool is_option_value_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_option_name;
    bool m_option_name_isSet;
    bool m_option_name_isValid;

    QString m_option_value;
    bool m_option_value_isSet;
    bool m_option_value_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIProductVariantUpdate_options_inner)

#endif // OAIProductVariantUpdate_options_inner_H
