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
 * OAIBasketLiveShippingServiceList_200_response.h
 *
 * 
 */

#ifndef OAIBasketLiveShippingServiceList_200_response_H
#define OAIBasketLiveShippingServiceList_200_response_H

#include <QJsonObject>

#include "OAIBasketLiveShippingServiceList_200_response_result.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIBasketLiveShippingServiceList_200_response_result;

class OAIBasketLiveShippingServiceList_200_response : public OAIObject {
public:
    OAIBasketLiveShippingServiceList_200_response();
    OAIBasketLiveShippingServiceList_200_response(QString json);
    ~OAIBasketLiveShippingServiceList_200_response() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIBasketLiveShippingServiceList_200_response_result getResult() const;
    void setResult(const OAIBasketLiveShippingServiceList_200_response_result &result);
    bool is_result_Set() const;
    bool is_result_Valid() const;

    qint32 getReturnCode() const;
    void setReturnCode(const qint32 &return_code);
    bool is_return_code_Set() const;
    bool is_return_code_Valid() const;

    QString getReturnMessage() const;
    void setReturnMessage(const QString &return_message);
    bool is_return_message_Set() const;
    bool is_return_message_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIBasketLiveShippingServiceList_200_response_result m_result;
    bool m_result_isSet;
    bool m_result_isValid;

    qint32 m_return_code;
    bool m_return_code_isSet;
    bool m_return_code_isValid;

    QString m_return_message;
    bool m_return_message_isSet;
    bool m_return_message_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIBasketLiveShippingServiceList_200_response)

#endif // OAIBasketLiveShippingServiceList_200_response_H
