/**
 * Taxamo
 * Taxamo’s elegant suite of APIs and comprehensive reporting dashboard enables digital merchants to easily comply with EU regulatory requirements on tax calculation, evidence collection, tax return creation and data storage.
 *
 * The version of the OpenAPI document: 1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIUs_tax_id.h
 *
 * 
 */

#ifndef OAIUs_tax_id_H
#define OAIUs_tax_id_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIUs_tax_id : public OAIObject {
public:
    OAIUs_tax_id();
    OAIUs_tax_id(QString json);
    ~OAIUs_tax_id() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getStateOfIssue() const;
    void setStateOfIssue(const QString &state_of_issue);
    bool is_state_of_issue_Set() const;
    bool is_state_of_issue_Valid() const;

    QString getTaxId() const;
    void setTaxId(const QString &tax_id);
    bool is_tax_id_Set() const;
    bool is_tax_id_Valid() const;

    QString getTaxIdType() const;
    void setTaxIdType(const QString &tax_id_type);
    bool is_tax_id_type_Set() const;
    bool is_tax_id_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_state_of_issue;
    bool m_state_of_issue_isSet;
    bool m_state_of_issue_isValid;

    QString m_tax_id;
    bool m_tax_id_isSet;
    bool m_tax_id_isValid;

    QString m_tax_id_type;
    bool m_tax_id_type_isSet;
    bool m_tax_id_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIUs_tax_id)

#endif // OAIUs_tax_id_H
