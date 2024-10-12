/**
 * Trip Parser
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.
 *
 * The version of the OpenAPI document: 3.0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAILocation.h
 *
 * Description of a particular point or place in physical space
 */

#ifndef OAILocation_H
#define OAILocation_H

#include <QJsonObject>

#include "OAIAddress.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIAddress;

class OAILocation : public OAIObject {
public:
    OAILocation();
    OAILocation(QString json);
    ~OAILocation() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIAddress getAddress() const;
    void setAddress(const OAIAddress &address);
    bool is_address_Set() const;
    bool is_address_Valid() const;

    QString getIataCode() const;
    void setIataCode(const QString &iata_code);
    bool is_iata_code_Set() const;
    bool is_iata_code_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIAddress m_address;
    bool m_address_isSet;
    bool m_address_isValid;

    QString m_iata_code;
    bool m_iata_code_isSet;
    bool m_iata_code_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAILocation)

#endif // OAILocation_H
