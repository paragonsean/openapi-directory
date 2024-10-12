/**
 * groov View Public API
 * #### Revised: 2019-11-21  ### Overview groov View Public API revision 1. 
 *
 * The version of the OpenAPI document: R4.2a
 * Contact: developer@opto22.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIFloatArrayValue.h
 *
 * 
 */

#ifndef OAIFloatArrayValue_H
#define OAIFloatArrayValue_H

#include <QJsonObject>

#include "OAITagValue.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIFloatArrayValue : public OAIObject {
public:
    OAIFloatArrayValue();
    OAIFloatArrayValue(QString json);
    ~OAIFloatArrayValue() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getValueType() const;
    void setValueType(const QString &value_type);
    bool is_value_type_Set() const;
    bool is_value_type_Valid() const;

    QList<float> getValue() const;
    void setValue(const QList<float> &value);
    bool is_value_Set() const;
    bool is_value_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_value_type;
    bool m_value_type_isSet;
    bool m_value_type_isValid;

    QList<float> m_value;
    bool m_value_isSet;
    bool m_value_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIFloatArrayValue)

#endif // OAIFloatArrayValue_H
