/**
 * Seatmap Display
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.9.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAITax.h
 *
 * a tax
 */

#ifndef OAITax_H
#define OAITax_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAITax : public OAIObject {
public:
    OAITax();
    OAITax(QString json);
    ~OAITax() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAmount() const;
    void setAmount(const QString &amount);
    bool is_amount_Set() const;
    bool is_amount_Valid() const;

    QString getCode() const;
    void setCode(const QString &code);
    bool is_code_Set() const;
    bool is_code_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_amount;
    bool m_amount_isSet;
    bool m_amount_isValid;

    QString m_code;
    bool m_code_isSet;
    bool m_code_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITax)

#endif // OAITax_H
