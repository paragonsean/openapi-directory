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
 * OAIProduct_ChildItem_Combination.h
 *
 * 
 */

#ifndef OAIProduct_ChildItem_Combination_H
#define OAIProduct_ChildItem_Combination_H

#include <QJsonObject>

#include "OAIObject.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIProduct_ChildItem_Combination : public OAIObject {
public:
    OAIProduct_ChildItem_Combination();
    OAIProduct_ChildItem_Combination(QString json);
    ~OAIProduct_ChildItem_Combination() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIObject getAdditionalFields() const;
    void setAdditionalFields(const OAIObject &additional_fields);
    bool is_additional_fields_Set() const;
    bool is_additional_fields_Valid() const;

    OAIObject getCustomFields() const;
    void setCustomFields(const OAIObject &custom_fields);
    bool is_custom_fields_Set() const;
    bool is_custom_fields_Valid() const;

    QString getOptionId() const;
    void setOptionId(const QString &option_id);
    bool is_option_id_Set() const;
    bool is_option_id_Valid() const;

    QString getOptionValueId() const;
    void setOptionValueId(const QString &option_value_id);
    bool is_option_value_id_Set() const;
    bool is_option_value_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIObject m_additional_fields;
    bool m_additional_fields_isSet;
    bool m_additional_fields_isValid;

    OAIObject m_custom_fields;
    bool m_custom_fields_isSet;
    bool m_custom_fields_isValid;

    QString m_option_id;
    bool m_option_id_isSet;
    bool m_option_id_isValid;

    QString m_option_value_id;
    bool m_option_value_id_isSet;
    bool m_option_value_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIProduct_ChildItem_Combination)

#endif // OAIProduct_ChildItem_Combination_H
