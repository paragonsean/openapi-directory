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
 * OAIAccountCartList_200_response_result_carts_inner.h
 *
 * 
 */

#ifndef OAIAccountCartList_200_response_result_carts_inner_H
#define OAIAccountCartList_200_response_result_carts_inner_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIAccountCartList_200_response_result_carts_inner : public OAIObject {
public:
    OAIAccountCartList_200_response_result_carts_inner();
    OAIAccountCartList_200_response_result_carts_inner(QString json);
    ~OAIAccountCartList_200_response_result_carts_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCartId() const;
    void setCartId(const QString &cart_id);
    bool is_cart_id_Set() const;
    bool is_cart_id_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getStoreKey() const;
    void setStoreKey(const QString &store_key);
    bool is_store_key_Set() const;
    bool is_store_key_Valid() const;

    QString getTotalCalls() const;
    void setTotalCalls(const QString &total_calls);
    bool is_total_calls_Set() const;
    bool is_total_calls_Valid() const;

    QString getUrl() const;
    void setUrl(const QString &url);
    bool is_url_Set() const;
    bool is_url_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_cart_id;
    bool m_cart_id_isSet;
    bool m_cart_id_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_store_key;
    bool m_store_key_isSet;
    bool m_store_key_isValid;

    QString m_total_calls;
    bool m_total_calls_isSet;
    bool m_total_calls_isValid;

    QString m_url;
    bool m_url_isSet;
    bool m_url_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAccountCartList_200_response_result_carts_inner)

#endif // OAIAccountCartList_200_response_result_carts_inner_H
