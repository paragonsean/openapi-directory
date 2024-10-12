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
 * OAIProductCount_200_response_result.h
 *
 * 
 */

#ifndef OAIProductCount_200_response_result_H
#define OAIProductCount_200_response_result_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIProductCount_200_response_result : public OAIObject {
public:
    OAIProductCount_200_response_result();
    OAIProductCount_200_response_result(QString json);
    ~OAIProductCount_200_response_result() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getProductsCount() const;
    void setProductsCount(const qint32 &products_count);
    bool is_products_count_Set() const;
    bool is_products_count_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_products_count;
    bool m_products_count_isSet;
    bool m_products_count_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIProductCount_200_response_result)

#endif // OAIProductCount_200_response_result_H
