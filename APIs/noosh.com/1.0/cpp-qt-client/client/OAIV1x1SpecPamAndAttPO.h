/**
 * Noosh API application
 * Full description of Noosh API
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIV1x1SpecPamAndAttPO.h
 *
 * Java type: com.noosh.domain.nooshapi.persist.po.v1x1.V1x1SpecPamAndAttPO
 */

#ifndef OAIV1x1SpecPamAndAttPO_H
#define OAIV1x1SpecPamAndAttPO_H

#include <QJsonObject>

#include <QJsonValue>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIV1x1SpecPamAndAttPO : public OAIObject {
public:
    OAIV1x1SpecPamAndAttPO();
    OAIV1x1SpecPamAndAttPO(QString json);
    ~OAIV1x1SpecPamAndAttPO() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint64 getAttributeId() const;
    void setAttributeId(const qint64 &attribute_id);
    bool is_attribute_id_Set() const;
    bool is_attribute_id_Valid() const;

    QJsonValue getAttributeValue() const;
    void setAttributeValue(const QJsonValue &attribute_value);
    bool is_attribute_value_Set() const;
    bool is_attribute_value_Valid() const;

    QString getLabel() const;
    void setLabel(const QString &label);
    bool is_label_Set() const;
    bool is_label_Valid() const;

    qint64 getParamId() const;
    void setParamId(const qint64 &param_id);
    bool is_param_id_Set() const;
    bool is_param_id_Valid() const;

    QString getParamName() const;
    void setParamName(const QString &param_name);
    bool is_param_name_Set() const;
    bool is_param_name_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint64 m_attribute_id;
    bool m_attribute_id_isSet;
    bool m_attribute_id_isValid;

    QJsonValue m_attribute_value;
    bool m_attribute_value_isSet;
    bool m_attribute_value_isValid;

    QString m_label;
    bool m_label_isSet;
    bool m_label_isValid;

    qint64 m_param_id;
    bool m_param_id_isSet;
    bool m_param_id_isValid;

    QString m_param_name;
    bool m_param_name_isSet;
    bool m_param_name_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIV1x1SpecPamAndAttPO)

#endif // OAIV1x1SpecPamAndAttPO_H
