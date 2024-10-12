/**
 * Flight Choice Prediction
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, to see what is included in test please refer to our **[data collection](https://github.com/amadeus4dev/data-collection)**. 
 *
 * The version of the OpenAPI document: 2.0.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIOriginalFlightEndPoint.h
 *
 * departure or arrival information
 */

#ifndef OAIOriginalFlightEndPoint_H
#define OAIOriginalFlightEndPoint_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIOriginalFlightEndPoint : public OAIObject {
public:
    OAIOriginalFlightEndPoint();
    OAIOriginalFlightEndPoint(QString json);
    ~OAIOriginalFlightEndPoint() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getIataCode() const;
    void setIataCode(const QString &iata_code);
    bool is_iata_code_Set() const;
    bool is_iata_code_Valid() const;

    QString getTerminal() const;
    void setTerminal(const QString &terminal);
    bool is_terminal_Set() const;
    bool is_terminal_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_iata_code;
    bool m_iata_code_isSet;
    bool m_iata_code_isValid;

    QString m_terminal;
    bool m_terminal_isSet;
    bool m_terminal_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIOriginalFlightEndPoint)

#endif // OAIOriginalFlightEndPoint_H
