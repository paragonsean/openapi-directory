/**
 * Chain49 API
 * Kickstart your next crypto project - extended trezor/blockbook API with 10+ blockchains available instantly and 50+ possible on request running on the finest hardware in Germany's best datacenters at Hetzner  Websocket only via api.chain49.com endpoint possible (RapidAPI does not support it yet)
 *
 * The version of the OpenAPI document: 2.0
 * Contact: contact@chain49.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIGetBlockchain_200_response.h
 *
 * 
 */

#ifndef OAIGetBlockchain_200_response_H
#define OAIGetBlockchain_200_response_H

#include <QJsonObject>

#include "OAIGetBlockchain_200_response_backend.h"
#include "OAIGetBlockchain_200_response_blockbook.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIGetBlockchain_200_response_backend;
class OAIGetBlockchain_200_response_blockbook;

class OAIGetBlockchain_200_response : public OAIObject {
public:
    OAIGetBlockchain_200_response();
    OAIGetBlockchain_200_response(QString json);
    ~OAIGetBlockchain_200_response() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIGetBlockchain_200_response_backend getBackend() const;
    void setBackend(const OAIGetBlockchain_200_response_backend &backend);
    bool is_backend_Set() const;
    bool is_backend_Valid() const;

    OAIGetBlockchain_200_response_blockbook getBlockbook() const;
    void setBlockbook(const OAIGetBlockchain_200_response_blockbook &blockbook);
    bool is_blockbook_Set() const;
    bool is_blockbook_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIGetBlockchain_200_response_backend m_backend;
    bool m_backend_isSet;
    bool m_backend_isValid;

    OAIGetBlockchain_200_response_blockbook m_blockbook;
    bool m_blockbook_isSet;
    bool m_blockbook_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGetBlockchain_200_response)

#endif // OAIGetBlockchain_200_response_H
