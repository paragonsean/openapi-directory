/**
 * Flight Offers Search
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 2.2.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAICarrierEntry.h
 *
 * 
 */

#ifndef OAICarrierEntry_H
#define OAICarrierEntry_H

#include <QJsonObject>

#include <QMap>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAICarrierEntry : public OAIObject {
public:
    OAICarrierEntry();
    OAICarrierEntry(QString json);
    ~OAICarrierEntry() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getKey() const;
    void setKey(const QString &key);
    bool is_key_Set() const;
    bool is_key_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_key;
    bool m_key_isSet;
    bool m_key_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICarrierEntry)

#endif // OAICarrierEntry_H
