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
 * OAIProductCurrencyAdd_200_response_result.h
 *
 * 
 */

#ifndef OAIProductCurrencyAdd_200_response_result_H
#define OAIProductCurrencyAdd_200_response_result_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIProductCurrencyAdd_200_response_result : public OAIObject {
public:
    OAIProductCurrencyAdd_200_response_result();
    OAIProductCurrencyAdd_200_response_result(QString json);
    ~OAIProductCurrencyAdd_200_response_result() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCurrencyId() const;
    void setCurrencyId(const QString &currency_id);
    bool is_currency_id_Set() const;
    bool is_currency_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_currency_id;
    bool m_currency_id_isSet;
    bool m_currency_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIProductCurrencyAdd_200_response_result)

#endif // OAIProductCurrencyAdd_200_response_result_H
