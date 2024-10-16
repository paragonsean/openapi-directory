/**
 * Personnel Data
 * API for reading and writing personnel data incl. data about attendances and absences
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIAbsenceEntitlement.h
 *
 * 
 */

#ifndef OAIAbsenceEntitlement_H
#define OAIAbsenceEntitlement_H

#include <QJsonObject>

#include "OAIAbsenceEntitlement_value_inner.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIAbsenceEntitlement_value_inner;

class OAIAbsenceEntitlement : public OAIObject {
public:
    OAIAbsenceEntitlement();
    OAIAbsenceEntitlement(QString json);
    ~OAIAbsenceEntitlement() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getLabel() const;
    void setLabel(const QString &label);
    bool is_label_Set() const;
    bool is_label_Valid() const;

    QList<OAIAbsenceEntitlement_value_inner> getValue() const;
    void setValue(const QList<OAIAbsenceEntitlement_value_inner> &value);
    bool is_value_Set() const;
    bool is_value_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_label;
    bool m_label_isSet;
    bool m_label_isValid;

    QList<OAIAbsenceEntitlement_value_inner> m_value;
    bool m_value_isSet;
    bool m_value_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAbsenceEntitlement)

#endif // OAIAbsenceEntitlement_H
