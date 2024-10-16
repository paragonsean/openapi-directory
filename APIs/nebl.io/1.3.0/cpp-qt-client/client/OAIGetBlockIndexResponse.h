/**
 * Neblio REST API Suite
 * APIs for Interacting with NTP1 Tokens & The Neblio Blockchain
 *
 * The version of the OpenAPI document: 1.3.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIGetBlockIndexResponse.h
 *
 * 
 */

#ifndef OAIGetBlockIndexResponse_H
#define OAIGetBlockIndexResponse_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIGetBlockIndexResponse : public OAIObject {
public:
    OAIGetBlockIndexResponse();
    OAIGetBlockIndexResponse(QString json);
    ~OAIGetBlockIndexResponse() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getBlockHash() const;
    void setBlockHash(const QString &block_hash);
    bool is_block_hash_Set() const;
    bool is_block_hash_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_block_hash;
    bool m_block_hash_isSet;
    bool m_block_hash_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGetBlockIndexResponse)

#endif // OAIGetBlockIndexResponse_H
