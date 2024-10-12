/**
 * Mailscript
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.4.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAICriteriaOperand.h
 *
 * 
 */

#ifndef OAICriteriaOperand_H
#define OAICriteriaOperand_H

#include <QJsonObject>

#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAICriteriaOperand : public OAIObject {
public:
    OAICriteriaOperand();
    OAICriteriaOperand(QString json);
    ~OAICriteriaOperand() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<QString> getRAnd() const;
    void setRAnd(const QList<QString> &r_and);
    bool is_r_and_Set() const;
    bool is_r_and_Valid() const;

    QList<QString> getROr() const;
    void setROr(const QList<QString> &r_or);
    bool is_r_or_Set() const;
    bool is_r_or_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<QString> m_r_and;
    bool m_r_and_isSet;
    bool m_r_and_isValid;

    QList<QString> m_r_or;
    bool m_r_or_isSet;
    bool m_r_or_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICriteriaOperand)

#endif // OAICriteriaOperand_H
