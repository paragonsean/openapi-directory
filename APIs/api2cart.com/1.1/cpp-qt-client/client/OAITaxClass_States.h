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
 * OAITaxClass_States.h
 *
 * 
 */

#ifndef OAITaxClass_States_H
#define OAITaxClass_States_H

#include <QJsonObject>

#include "OAIObject.h"
#include "OAITaxClass_ZipCodes.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAITaxClass_ZipCodes;

class OAITaxClass_States : public OAIObject {
public:
    OAITaxClass_States();
    OAITaxClass_States(QString json);
    ~OAITaxClass_States() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIObject getAdditionalFields() const;
    void setAdditionalFields(const OAIObject &additional_fields);
    bool is_additional_fields_Set() const;
    bool is_additional_fields_Valid() const;

    QString getCode() const;
    void setCode(const QString &code);
    bool is_code_Set() const;
    bool is_code_Valid() const;

    OAIObject getCustomFields() const;
    void setCustomFields(const OAIObject &custom_fields);
    bool is_custom_fields_Set() const;
    bool is_custom_fields_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    double getTax() const;
    void setTax(const double &tax);
    bool is_tax_Set() const;
    bool is_tax_Valid() const;

    qint32 getTaxType() const;
    void setTaxType(const qint32 &tax_type);
    bool is_tax_type_Set() const;
    bool is_tax_type_Valid() const;

    QList<OAITaxClass_ZipCodes> getZipCodes() const;
    void setZipCodes(const QList<OAITaxClass_ZipCodes> &zip_codes);
    bool is_zip_codes_Set() const;
    bool is_zip_codes_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIObject m_additional_fields;
    bool m_additional_fields_isSet;
    bool m_additional_fields_isValid;

    QString m_code;
    bool m_code_isSet;
    bool m_code_isValid;

    OAIObject m_custom_fields;
    bool m_custom_fields_isSet;
    bool m_custom_fields_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    double m_tax;
    bool m_tax_isSet;
    bool m_tax_isValid;

    qint32 m_tax_type;
    bool m_tax_type_isSet;
    bool m_tax_type_isValid;

    QList<OAITaxClass_ZipCodes> m_zip_codes;
    bool m_zip_codes_isSet;
    bool m_zip_codes_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITaxClass_States)

#endif // OAITaxClass_States_H
