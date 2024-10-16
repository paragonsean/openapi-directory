/**
 * Axesso Api
 * Use this api to fetch information to Amazon products and more.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: support@axesso.de
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIBuyRecommendationResponse.h
 *
 * 
 */

#ifndef OAIBuyRecommendationResponse_H
#define OAIBuyRecommendationResponse_H

#include <QJsonObject>

#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIBuyRecommendationResponse : public OAIObject {
public:
    OAIBuyRecommendationResponse();
    OAIBuyRecommendationResponse(QString json);
    ~OAIBuyRecommendationResponse() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<QString> getBuyRecommendations() const;
    void setBuyRecommendations(const QList<QString> &buy_recommendations);
    bool is_buy_recommendations_Set() const;
    bool is_buy_recommendations_Valid() const;

    qint64 getNumberOfProducts() const;
    void setNumberOfProducts(const qint64 &number_of_products);
    bool is_number_of_products_Set() const;
    bool is_number_of_products_Valid() const;

    QString getResponseMessage() const;
    void setResponseMessage(const QString &response_message);
    bool is_response_message_Set() const;
    bool is_response_message_Valid() const;

    QString getResponseStatus() const;
    void setResponseStatus(const QString &response_status);
    bool is_response_status_Set() const;
    bool is_response_status_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<QString> m_buy_recommendations;
    bool m_buy_recommendations_isSet;
    bool m_buy_recommendations_isValid;

    qint64 m_number_of_products;
    bool m_number_of_products_isSet;
    bool m_number_of_products_isValid;

    QString m_response_message;
    bool m_response_message_isSet;
    bool m_response_message_isValid;

    QString m_response_status;
    bool m_response_status_isSet;
    bool m_response_status_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIBuyRecommendationResponse)

#endif // OAIBuyRecommendationResponse_H
