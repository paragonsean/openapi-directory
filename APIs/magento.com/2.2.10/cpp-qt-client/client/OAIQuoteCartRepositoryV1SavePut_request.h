/**
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIQuoteCartRepositoryV1SavePut_request.h
 *
 * 
 */

#ifndef OAIQuoteCartRepositoryV1SavePut_request_H
#define OAIQuoteCartRepositoryV1SavePut_request_H

#include <QJsonObject>

#include "OAIQuote_data_cart_interface.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIQuote_data_cart_interface;

class OAIQuoteCartRepositoryV1SavePut_request : public OAIObject {
public:
    OAIQuoteCartRepositoryV1SavePut_request();
    OAIQuoteCartRepositoryV1SavePut_request(QString json);
    ~OAIQuoteCartRepositoryV1SavePut_request() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIQuote_data_cart_interface getQuote() const;
    void setQuote(const OAIQuote_data_cart_interface &quote);
    bool is_quote_Set() const;
    bool is_quote_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIQuote_data_cart_interface m_quote;
    bool m_quote_isSet;
    bool m_quote_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIQuoteCartRepositoryV1SavePut_request)

#endif // OAIQuoteCartRepositoryV1SavePut_request_H
